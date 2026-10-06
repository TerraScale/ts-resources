# TerraScale Sync architecture and implementation plan

Status: shared contract for implementation. This plan intentionally distinguishes
existing guarantees from guarantees that must be added and tested.

## 1. Product boundary

TerraScale Sync is a public Platform capability backed by TerraBase. It is not a
Dashboard slice, a wrapper over Changes/SSE, a queue product, or a new gateway
service.

One physical TerraBase project database is the authoritative consistency
boundary. Logical `DatabaseId` and `EnvironmentId` remain mandatory in every
query, mutation, dependency, cache, and authorization key. Project placement is
physical and is not duplicated for every logical database.

For Sync-enabled project databases, one placement and one database node tag
inside that placement form the revision authority and write leader. Other nodes
and placements are ordered read replicas. A replica cannot accept an official
direct write. Platform transparently routes mutations to the write leader;
TerraBase rejects a write received on another node with a safe authority-routing
response. This restriction is necessary because the existing multi-writer
change vector is causal, not a total commit order.

## 2. Revision and consistency model

### 2.1 DatabaseRevision

`DatabaseRevision` is the lexicographically ordered pair:

```text
RevisionEpoch  : unsigned 64-bit integer
CommitSequence : unsigned 64-bit integer
```

The wire form is a strongly validated pair, never a floating-point number or an
opaque string comparison. Sequence zero is the epoch barrier. Normal commits
increment `CommitSequence` once per successful document transaction.

The write leader owns the current epoch. Promotion uses a fenced control-plane
operation:

1. stop admission of writes to the old authority;
2. prove the candidate has applied the old authority’s contiguous watermark;
3. allocate a strictly greater epoch through the protected placement
   generation;
4. persist the epoch barrier in TerraBase;
5. publish the new write role;
6. resume writes.

Restore always creates a greater epoch and expires pre-restore cursors. A
`DatabaseRevision` never regresses across reconnect, relocation, or failover.

### 2.2 Atomic commit rule

Inside the same Voron write transaction that makes document changes visible,
TerraBase:

1. obtains the next sequence from transaction-local Sync state;
2. finalizes the transaction-local mutation collector;
3. writes one immutable `CommitDelta`;
4. advances the visible revision;
5. writes any mutation receipt completed by the transaction.

Failure rolls back all five. The post-commit callback only pulses an async
signal. Consumers recover by reading the durable log.

Sync-disabled databases execute one predictable feature check and allocate no
collector. Capture/Active modes append the durable log even with zero
subscribers, because a future subscriber or disconnected worker must not depend
on process-local history.

### 2.3 Query guarantee

Sync v1 exposes one correctness mode, `AuthoritativeSnapshot`:

- writes execute at the revision authority;
- a query reads one TerraBase document snapshot;
- required indexes are non-stale through the query’s execution revision;
- every dependency is captured during execution;
- the result records its `ExecutionRevision`;
- change-log validation may extend it to a later `ValidatedThroughRevision`
  only when no intervening delta overlaps;
- every state in one client transition is valid through the transition’s
  `DatabaseRevision`.

This is snapshot consistency within one physical project database. It is not a
claim of serializable multi-database transactions. Existing non-Sync eventual
query modes retain their existing semantics but cannot be registered as live
queries.

If a query spans a storage/index boundary that cannot meet this rule, TerraBase
rejects live registration with a structured unsupported-consistency error. It
does not silently weaken the mode.

## 3. TerraBase durable model

Internal Voron structures are versioned and excluded from user collections:

```text
Sync/State
  epoch
  next-sequence
  visible-revision
  earliest-retained-revision

Sync/CommitDeltas
  key: big-endian (epoch, sequence)
  value: header + compact mutation facts

Sync/ConsumerCheckpoints
  key: consumer/partition identity
  value: revision, lease generation, updated-at

Sync/MutationReceipts
  key: tenant + logical database + idempotency hash
  value: request fingerprint, outcome, committed revision, expiry

Sync/ResumeCursors
  key: keyed hash of stable session identity
  value: acknowledged revision, expiry
```

### 3.1 CommitDelta

A `CommitDelta` contains:

- physical project database identity;
- logical database/environment scopes touched, or an explicit unknown-scope
  fallback;
- `DatabaseRevision`;
- transaction/operation ID;
- origin and replication-origin region;
- commit timestamp;
- mutation facts;
- schema/collection/database barriers;
- serialization version and checksum.

Each mutation fact contains collection/table, operation, primary key, partition
key/range facts, and precision flags. Document storage records exact keys and
old/new document metadata without reparsing after commit.

Index commits write durable `IndexDelta` facts tied to source database revisions.
The index writer already knows old and new normalized terms/keys, so it records
exact secondary/search intervals there rather than running arbitrary static
index code in the document commit. An index that cannot expose precise facts
uses an explicit index-generation dependency and increments a fallback counter.

### 3.2 Replication

Leader-authored revisions and deltas replicate with their transaction. A replica
applies them in order and advances only a contiguous applied watermark. Duplicate
delivery is idempotent. A gap blocks publication and triggers recovery from the
leader’s durable range.

Replication-origin commits are not assigned a second public revision. A
promoted authority begins a new epoch only after fencing. Official direct
clients discover or are forwarded to the write authority.

### 3.3 Tail and retention

TerraBase exposes an authenticated internal tail API:

```text
ReadDeltas(afterRevision, maxRecords, maxBytes)
WaitForDelta(afterRevision, deadline)
Checkpoint(consumer, leaseGeneration, revision)
```

`WaitForDelta` is a signal-backed blocking read, not periodic polling. Every
wakeup is followed by a durable read.

Retention calculates the minimum of active partition checkpoints, unexpired
resume cursors, replica apply cursors, and operational safety margin. Deletion is
bounded and transactional. A request older than
`earliest-retained-revision` returns `CursorExpired`; Platform emits
`ResyncRequired`. Metrics expose retained bytes/revisions, oldest cursor, and
consumer lag.

## 4. Dependencies

`DependencySet` is a sorted, deduplicated collection of compact tagged records:

```text
DocumentKey(collection, key)
PartitionKey(collection, key)
PartitionInterval(collection, lower, upper, inclusivity)
IndexInterval(index, field, lower, upper, inclusivity, collation)
SearchTerms(index, field, normalized terms/predicate kind)
AggregateSource(source identity, interval)
CollectionGeneration(collection, generation)
IndexGeneration(index, generation)
SchemaGeneration(generation)
AuthorizationGeneration(generation)
PlannerGeneration(plan identity, generation)
DatabaseGeneration(generation)
```

Missing exact documents and empty ranges are recorded. Range endpoints use the
same collation/comparer as the executed plan. Query planner normalization is
serialized once and shared by query identity, execution, and dependency
capture.

The transaction-local mutation collector and query-local dependency collector
use pooled buffers and small inline storage. Finalization sorts/deduplicates
once. The disabled path allocates nothing.

## 5. Shared reactive execution

### 5.1 Query token

`QueryFingerprint` is SHA-256 over a canonical length-prefixed encoding of:

- physical project database;
- tenant, logical database, and environment;
- effective authorization-scope hash and authorization generation;
- normalized query AST and canonical arguments;
- schema/planner generations;
- consistency mode.

Raw arguments and user/tenant IDs are not logged or used as telemetry labels.
Two queries share execution only when their complete fingerprints match.

### 5.2 Query cell

One `QueryCell` owns:

- fingerprint and normalized executable query;
- immutable result or structured error;
- canonical result hash;
- execution and validated-through revisions;
- dependencies;
- continuation journal;
- listener count;
- memory estimate and recency;
- compute/invalidation state.

The cell is the single-flight boundary. Repeated invalidations coalesce into one
newest target. The final listener’s removal cancels queued work; in-flight
TerraBase work is cancelled where safe and the inactive cell becomes evictable.

Canonical hashing uses deterministic UTF-8 JSON produced by TerraBase’s query
serializer and SHA-256. The system first compares length and hash, then bytes
when required to make collision handling deterministic. Result objects are
immutable.

### 5.3 Partitions and reverse indexes

Ownership is rendezvous-hashed by `(physical database, QueryFingerprint)` over
the current worker membership generation. Each `SyncPartition` holds:

- exact document/partition-key dictionaries;
- per-index augmented interval trees;
- collection/index/schema/auth/planner generation dictionaries;
- search-term dictionaries;
- query cells and durable checkpoint.

Each partition tails a database delta once, not once per query/socket. Ordinary
exact-key writes use dictionary candidates and interval overlap; they never scan
all subscriptions. Lease transfer fences the old owner, restores cells from
active session/query registrations, resumes the durable checkpoint, tolerates
duplicate deltas, and rebuilds reverse indexes before serving.

Cell registrations and session fanout may use cell-local product NATS for wake
hints and request/reply. NATS is not the revision log, checkpoint, lease
authority, or only representation of a transition.

### 5.4 Common revision barrier

After invalidation, query cells execute against current authoritative snapshots.
The coordinator then chooses the greatest relevant execution/log revision and
validates every cell dependency through it. Any overlapping delta schedules a
rerun. The cycle repeats until all cells are proven valid through one target or
a bounded work/latency limit causes coalescing to a newer complete target.

This fixed-point barrier allows a transition to combine shared results computed
at different snapshots only when each result is provably unchanged at the
transition revision. An unchanged hash advances validity and suppresses the
query payload/listener notification.

## 6. Session and protocol

### 6.1 Transport

The endpoint is `wss://<public-host>/api/v1/sync`. Protocol v1 uses a generated
discriminated JSON envelope over WebSocket:

```text
protocol
messageType
connectionSequence
messageSequence
payload
```

JSON keeps the browser and both SDKs dependency-free and debuggable. C# uses a
source-generated serializer. TypeScript validates every trust-boundary field.
Canonical query/result encodings are separate from the envelope and are never
based on JavaScript object insertion order.

Limits are enforced before allocation:

- 1 MiB maximum uncompressed client message;
- 256 KiB transition chunks;
- 8 MiB default / tenant-configured maximum transition;
- bounded permessage-deflate expansion ratio and decompressed bytes;
- 100 active queries by default with tenant quota overrides;
- 2 MiB default outgoing buffered bytes;
- one transition computation and one transition awaiting acknowledgement.

Large transitions carry transition ID, chunk index/count, uncompressed length,
and SHA-256. The client applies nothing until all chunks validate. Heartbeats
use protocol Ping frames so connection liveness and application state are
distinct.

### 6.2 Messages

Client messages:

- `Connect`
- `Authenticate`
- `ModifyQuerySet`
- `ExecuteMutation`
- `AcknowledgeTransition`
- `ClientTelemetry`
- `Ping`

Server messages:

- `Transition`
- `MutationResult`
- `AuthenticationError`
- `ResyncRequired`
- `RegionRouteChanged`
- `Ping`
- `FatalProtocolError`

`ModifyQuerySet` contains exact
`BaseQuerySetVersion`, `NewQuerySetVersion`, `AddQuery[]`, and `RemoveQuery[]`.
Versions increase by one; duplicate identical messages are idempotent and any
other mismatch is fatal/resync.

`SyncStateVersion` contains:

```text
QuerySetVersion
DatabaseRevision { RevisionEpoch, CommitSequence }
IdentityVersion
```

Every `Transition` contains exact start/end versions, updated/failed/removed
query arrays, optional bounded server timing, ingress region, serving region,
database region, and route generation. A client reducer applies it only when
`StartVersion` exactly equals current state. All removals, failures, and updates
are installed before one listener-notification pass.

### 6.3 Backpressure and acknowledgement

One bounded channel is owned by a physical connection. Obsolete unsent
intermediate work is replaced by the latest complete versioned state; the only
representation of an acknowledged/required transition is never discarded.
Slow clients receive a structured close reason plus resume data after queue,
bytes, or acknowledgement deadlines are exceeded.

Acknowledgement advances the resumable cursor and releases retained transition
buffers. Session expiry removes its cursor and registrations. Drain stops new
mutations, completes the current transition when bounded, emits
`RegionRouteChanged`, and closes.

### 6.4 Reconnect

`Connect` carries stable session ID, increasing connection sequence, last
applied/acknowledged versions, maximum observed revision, full active query set
with journals, pending mutation IDs, and previous region diagnostics.

The server rejects an older connection sequence. It selects a placement at or
above the maximum revision. If retained session/log state is available, it
reconstructs and resumes. Otherwise `ResyncRequired` names the expired boundary;
the server executes the complete active set, validates it through one revision,
and sends one atomic replacement transition.

Neither side guesses across a version gap.

## 7. Mutations and optimistic state

Every mutation is scoped by session, connection sequence, client request ID,
idempotency key, physical/logical database, tenant, and authorization hash.
TerraBase stores a keyed hash, request fingerprint, durable outcome, and
committed revision in the same transaction as the write.

A retry with the same key/fingerprint returns the receipt. A key with a
different fingerprint fails. An ambiguous failure is resolved by receipt lookup,
not blind re-execution.

The successful ordering is:

```text
ExecuteMutation accepted
  -> TerraBase commit + receipt + CommitDelta at revision R
  -> MutationResult(committedRevision=R)
  -> dependency invalidation and shared recomputation
  -> authoritative Transition validated through >= R
```

Clients keep immutable authoritative query state and an ordered list of
optimistic layers. Every server transition replaces the base atomically and
replays pending layers in original order. A successful layer is removed only
after both `MutationResult` and authoritative state at or above its committed
revision; a failure removes and rolls it back immediately. Cached objects are
never mutated in place.

## 8. Authentication and isolation

A cache/subscription key includes physical database, logical database,
environment, tenant, effective authorization hash, authorization generation,
schema generation, and consistency. No field is omitted because query text
matches.

Browser connection tickets are short-lived, opaque to the client, single-use,
audience-bound capabilities. Their encrypted/signed routing scope is verifiable
from a locally replicated key at ingress; the destination atomically consumes
the nonce and fully authorizes before upgrade. The browser offers
`terrascale-sync-v1` and a base64url `ticket.<capability>` token in
`Sec-WebSocket-Protocol`; the server selects only `terrascale-sync-v1`, never
echoes the capability, and redacts the complete header. Server SDKs use the
bearer provider during `Authenticate`.

Authentication refresh increments `IdentityVersion`. Until dependency-level
authorization is independently proven, any effective identity or authorization
generation change invalidates the session’s entire query set. Old identity
results are removed before new results become observable.

Payload sizes, AST depth/complexity, argument count/bytes, query count,
transition bytes, mutation/reconnect/session rates, and ticket/routing access are
validated with tenant quotas. Sensitive identifiers, arguments, results,
tokens, tickets, and idempotency keys are absent from ordinary logs and metric
dimensions.

## 9. Global routing

### 9.1 Directory

Platform composes an internal `ProjectRouteSnapshot` from:

- project placement generation and selected regions (Platform metadata);
- read/write role, current revision, replication freshness, and database health
  (TerraBase);
- private endpoint, workload health, capacity, overload, drain/maintenance, and
  connectivity generation (Orchestrator);
- measured private-backhaul RTT and observation generation.

This projection is separate from the public placement response and reveals no
private hostname, capacity, or topology. Generation changes invalidate cached
routes immediately; TTL only limits observation freshness.

### 9.2 Selection

For a requested consistency role and minimum revision:

1. require authorized current-generation placement;
2. require fresh database and workload observations;
3. remove unhealthy, stale, draining, maintained, or overloaded entries;
4. require read/write role and `CurrentRevision >= MinimumRevision`;
5. prefer an eligible local placement;
6. otherwise minimize measured backhaul RTT plus bounded capacity penalty;
7. use valid prior affinity only as a tie-breaker;
8. use geographic distance only before a measured sample exists.

If no candidate is current, wait within the replication deadline, try the write
authority, or return a structured retry. Never serve a lower revision.

### 9.3 HTTP and WebSocket forwarding

Ordinary HTTP retains private MagicOnion replay and gains the shared selector
plus eligible fallback attempts.

Remote WebSocket/SignalR upgrades use YARP’s low-level HTTP forwarder over a
private mTLS Platform backhaul listener. The nearest ingress does not call
`AcceptWebSocketAsync`. It authenticates routing scope, selects a destination,
forwards the original upgrade, and pins the proxy stream. The destination
revalidates, returns 101, and hosts the session.

Forwarding preserves trace context, trusted original client address, tenant and
database scope, ticket, ingress region, route generation, and connection
sequence through authenticated internal headers. Public callers cannot inject
those headers.

No established WebSocket is migrated. Drain/failure closes it for resumable
reconnect through the nearest ingress. SignalR circuits use the same
pre-upgrade selection and lifetime affinity.

## 10. SDKs and examples

### .NET

`TerraScaleSyncClient` creates explicit `TerraScaleSyncSession` instances. A
session uses one BCL `ClientWebSocket`, one receive loop, one bounded send
channel, source-generated contracts, cancellation, `IAsyncDisposable`,
connection-state events, revision/region diagnostics, typed mutations,
`IAsyncEnumerable<TSnapshot>`, and callback subscriptions.

Local listeners reference-count one normalized query entry. Network add/remove
occurs only on zero-to-one and one-to-zero transitions.

The Blazor Interactive Server example uses one scoped session per circuit.
Prerender is a one-shot SDK read; live work starts after interactivity. The app
server owns Sync and the browser uses only Blazor’s SignalR circuit. It includes
an external-writer command in the same executable and Playwright tests for tabs,
reconnect, routing, no duplicate subscription/mutation, and unrelated writes.

### TypeScript

The SDK uses native WebSocket (injectable only as a runtime adapter), one state
machine, stable canonical query keys, immutable snapshots, reference-counted
listeners, optimistic layers, reconnect/resync, and the framework-neutral
`subscribe/getSnapshot/getServerSnapshot` contract. It has no React dependency.

The Vinext example pins the proven local stack, uses RSC for initial data, one
small client provider with `useSyncExternalStore`, and an authenticated route
handler for browser tickets. Hydration registers once. Playwright covers dev
HMR separately from data Sync and also covers standalone production start,
tabs, rollback, offline/reconnect, expired retention, regional routing, and
cross-example writes.

## 11. Observability

`TerraBase.Sync` and `TerraScale.Sync` expose ActivitySource/Meter signals for:

- commit-delta append size/duration and retained history;
- dependency count/bytes/type and conservative fallbacks;
- partition checkpoint lag and ownership transfer;
- invalidation candidates/overlaps and zero-overlap writes;
- query executions, single-flight joins, cache hit/memory/eviction;
- unchanged suppression and fixed-point passes;
- sessions, logical queries, queue bytes/depth, slow clients;
- transition compute/serialize/compress/fanout and commit-to-client latency;
- reconnect, incremental resume, resync, mutation rollback;
- directory lookup/observation age, selected region, local/backhaul, RTT,
  reroute, placement miss, and failover.

Dimensions are bounded enums/regions/outcomes only. Diagnostics offer privileged
per-session/database inspection without turning identifiers into metric labels.

## 12. Performance plan

The immutable starting image and controlled baseline described in
`performance/BASELINE.md` are mandatory before commit/query hot-path edits.
Every coherent TerraBase change runs the focused microbenchmark and the
same-image realistic comparison before landing.

Required variants:

1. original;
2. modified/capture disabled;
3. modified/capture active with zero listeners;
4. active listeners with mostly unrelated writes;
5. heavy overlap/invalidation.

Stable microbenchmarks fail above `max(3%, 2 × noise)`. Integration p95/p99
fails above `max(5%, 2 × noise)`. No dataset, hardware, affinity, warmup, sample,
or duration change can redefine the baseline.

Sync-specific benchmarks use production types for exact/range insertion and
lookup, empty range, removal, log append/tail, cache hit/single-flight,
hashing, transition serialization/compression/fanout, reconnect/resync,
placement lookup/local/backhaul/failover, and bounded slow-client behavior at
1k, 10k, and feasible 100k subscriptions. No ordinary write contains an
O(total subscriptions) loop.

## 13. Rollout, rollback, and retention safety

Per-database mode is:

- `Disabled`: no collection/log overhead; endpoint refuses registration.
- `Capture`: durable revisions/deltas/replication enabled; no public sessions.
- `Active`: capture plus public sessions.

Rollout advances Disabled → Capture → Active after health, lag, fallback, and
performance gates. Rollback Active → Capture drains sessions but preserves the
log and resumability. Capture → Disabled is allowed only after cursor expiry and
explicit acknowledgement that incremental resume will be lost.

Schema/storage formats are forward-readable for one deployed version and carry
checksums. Upgrade tests mix old/new replicas only where the exact format is
compatible; there is no alternate legacy Sync protocol.

## 14. Test and delivery gates

Before integration:

- commit atomicity, failed transaction, duplicate replication, gap, restore
  epoch, promotion fence, and every supported write-path tests;
- exact/missing/range/empty/index-old/index-new/search/aggregate/generation
  dependency tests;
- reverse-index scale tests proving unrelated writes do not scan all cells;
- shared computation, cancellation, unchanged hash, fixed-point and mass
  invalidation tests;
- protocol reducer, malformed payload, out-of-order/chunk/ack/slow-client,
  reconnect/retention/auth/idempotency/optimistic tests;
- placement generation, stale/health/revision/RTT/capacity/drain, pre-upgrade,
  affinity, failover, and no-regression tests.

Integration runs real TerraBase and Platform processes. Browser tests run both
real examples and cross-write between them. Randomized state-machine tests vary
subscriptions, mutations, disconnects, auth, lag, retention, ownership, slow
clients, and placement movement, then compare client state to an authoritative
TerraBase query.

The review thread changes no code. Its findings are recorded in `REVIEW.md`.
Every valid finding is fixed and all relevant suites/benchmarks rerun before
`FIX-PASS.md`, deployed regional verification, and `FINAL.md`.

## 15. Known pre-implementation blockers

- The development LXC is not a decision-grade benchmark runner. The direct
  QEMU/KVM launcher instead uses a disposable small guest, exact host/guest CPU
  isolation, and finalized host attestation.
- Memory-only and validation runs use a 1 GiB scratch disk; Persistent and Soak
  alone use an isolated 128 GiB raw guest disk on the existing host SSD. A
  separate NVMe device is not required.
- The KVM environment change still requires its exact-source passing review and
  valid starting self-test, Standard, and Persistent records before the timing
  gate opens.
- TerraBase lacks revision/delta storage, ordered replication watermarks, and a
  snapshot-aware reactive batch API.
- Platform regional forwarding cannot proxy WebSocket upgrades.
- Orchestrator has network/service planning foundations but no running backhaul
  endpoint publication path for this use.

These are implementation work, not accepted product limitations. No production
completion claim is permitted while any remains.
