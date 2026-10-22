# TerraScale Sync exploration

Date: 2026-07-26

This document records the pre-implementation findings. It is evidence, not a
claim that Sync is implemented.

## Existing consistency and commit boundary

TerraBase document mutations ultimately use a Voron write transaction. The
document transaction wrapper is the narrow seam common to ordinary API writes,
bulk operations, replication, smuggler/import work, and supported direct
document operations:

- `DocumentsTransaction` owns document transaction pre-commit and post-commit
  callbacks.
- `AbstractTransactionOperationsMerger` serializes the common write path.
- `LowLevelTransaction.Commit` is the physical visibility boundary.
- `StorageEnvironment` serializes writers and advances the visible committed
  transaction.

The transaction merger alone is not sufficient. Replication, restore,
administrative repair, and some direct storage operations can construct document
transactions without entering the ordinary public API path. Revision allocation
and durable change publication therefore belong in `DocumentsTransaction`
immediately before the same Voron commit that makes document changes visible.
The post-commit callback may wake consumers, but cannot be the source of truth.

Existing document etags, change vectors, and Voron transaction IDs are not a
valid `DatabaseRevision`:

- etags can be consumed by failed work and are process-local allocation facts;
- change vectors describe causal replication state, not one total database
  order;
- Voron transaction IDs are local storage-engine versions and do not survive
  restore, relocation, or authority changes as a global database identity.

TerraBase currently has no durable, ordered logical commit stream with retained
consumer cursors. Its Changes WebSocket is process-local and lossy. Existing
subscription processing has useful acknowledgement patterns but represents a
different product contract.

## Read snapshots and queries

A non-streaming collection query can observe one document storage snapshot.
Indexed queries currently cross index, document, and sometimes cluster
transactions. Streaming queries pulse transactions. There is no general
query-at-requested-revision API.

Sync cannot label those paths snapshot-consistent without changing them. The
required TerraBase execution API is a bounded, non-streaming reactive query
batch that:

1. opens a document read snapshot;
2. reads the database revision inside that snapshot;
3. waits for required indexes according to the requested consistency mode;
4. executes each normalized query while recording dependencies;
5. returns execution revision, index watermarks, dependencies, canonical result
   material, and errors;
6. rejects query shapes that cannot honor the selected consistency contract.

The shared-query coordinator may combine results executed at different
revisions only after durable change-log validation proves every result unchanged
through one common target revision. This fixed-point validity barrier avoids
inventing historical snapshots:

```text
execute invalidated entries
        ↓
choose maximum observed execution/log revision
        ↓
validate every dependency through that revision
        ↓
rerun entries invalidated during the window
        ↓
repeat until all entries are valid through one revision
        ↓
emit one atomic transition at that revision
```

## Supported write paths

Public document PUT, DELETE, batch, and bulk-insert paths pass through document
transactions. Replication and smuggler/import also use document transactions.
Restore, replay, change-vector reset, repair, and selected storage maintenance
paths can bypass the transaction merger but still reach the document transaction
or storage boundary.

The implementation must leave a runnable coverage inventory. Any operation that
cannot provide precise mutation facts records an explicit collection, schema, or
database-generation fallback. Unknown direct physical writes cannot be ignored.

Restore is a discontinuity, not an ordinary commit. It must allocate a new
revision epoch, invalidate all old cursors, and require atomic resync. Replicas
must apply leader-authored revisions in order and publish only a contiguous
applied watermark.

## Dependency capture seams

Dependencies must be recorded during authoritative execution:

- document load APIs record exact document keys, including missing keys;
- collection scans record collection generation plus exact/prefix/range bounds,
  including empty bounds;
- Corax and Lucene query builders record normalized index predicates before
  enumeration;
- includes, loaded documents, counters, time series, compares, and metadata
  reads contribute their own dependencies;
- static indexes record index identity, definition generation, and source
  watermark;
- authorization and schema dependencies are attached by Platform to the
  TerraBase dependency result.

Precise secondary/search invalidation requires index-commit change facts for old
and new normalized keys or terms. Until a query class has that proof, it uses an
explicit index/collection-generation dependency and increments the fallback
metric. Returned objects alone are never used to infer dependencies.

## Current TerraScale streaming

Platform’s repository/TQL SSE implementation is not a Sync foundation. Each
client creates a TerraBase Changes connection and an unbounded channel. It
broadcasts collection document notifications, rejects meaningful TQL filtering,
has no durable revision, and cannot resume or form atomic transitions.

Sync receives a new public endpoint and durable path. The SSE routes remain
legacy event APIs only until their separate retirement; they are not wrapped,
adapted, or used as a fallback.

## Platform authorization and mutation seam

The existing public endpoint stack already resolves an actor before a WebSocket
is accepted. Database scope is `(project_id, database_id, environment_id)`, while
one physical `proj-{projectId}` TerraBase database holds logical database and
environment partitions.

Browser WebSockets cannot attach the ordinary bearer header. A browser first
obtains a short-lived, single-use opaque Sync ticket through authenticated REST,
then offers it in `Sec-WebSocket-Protocol`. The nearest ingress verifies enough
scope to route safely; the destination consumes and revalidates the ticket before
returning 101. Tickets never appear in URLs, logs, metrics, RSC props, or public
errors.

Current project-user tokens expose session/security-stamp inputs, but long-lived
connections need explicit authentication refresh and identity-generation
invalidation after upgrade.

Platform’s public TQL and mutation repository is the right public API adapter,
but is not the commit authority. Mutation idempotency and committed revision
must be coupled to the TerraBase transaction so direct, replicated, and retried
writes cannot bypass them.

## Placement and routing

Placement is physically project-level. Existing metadata records selected
regions, generation, lifecycle status, initial catch-up, and drain information.
The current regional middleware:

- chooses ready placements;
- caches by a short TTL;
- uses a caller preferred region and geographic distance;
- forwards ordinary HTTP over private MagicOnion;
- does not evaluate current database revision, ongoing replication freshness,
  read/write role, capacity, measured RTT, overload, or maintenance;
- removes `Connection` and `Upgrade`, so it cannot proxy WebSockets.

MagicOnion remains appropriate for owned backend commands and ordinary streamed
HTTP replay. It must not become a custom WebSocket tunnel. A proven ASP.NET
reverse-proxy forwarder will carry remote upgrade requests over a distinct
private mTLS listener. The destination Platform instance, not the nearest
ingress, completes the upgrade.

Orchestrator already models endpoint generation, health, certificates,
registration, promotion, drain, emergency withdrawal, regional workloads, and
private network routes. It does not yet run an application reverse proxy or
database-aware route selector. Platform owns request selection; Orchestrator
publishes the private endpoint/health/capacity observations used by that
selection.

No new gateway workload is required:

```text
client
  -> nearest healthy regional Platform ingress
  -> ticket scope and physical project lookup
  -> eligible placement selection
     -> local Platform Sync endpoint
     -> remote Platform private backhaul endpoint
  -> destination reauthorization
  -> destination WebSocket upgrade beside TerraBase
```

An established socket is pinned. Drain or failure closes it with resumable
state; reconnect enters through the nearest ingress and must select a placement
at or above the client’s maximum observed revision.

## SDK and framework findings

### .NET

TerraScale.NET targets .NET 10 and can implement Sync with BCL
`ClientWebSocket`, bounded channels, `System.Text.Json` source generation, and
`IAsyncDisposable`. Existing bearer providers resolve per request and existing
REST mutations have bounded retry logic. Sync startup must remain explicit; the
SDK prohibits hidden background work.

The Blazor example belongs in
`TerraScale.DotNet/examples/TerraScale.Sync.BlazorServer`. It uses the existing
.NET 10 shared ASP.NET Core framework; no Blazor package is required. One scoped
Sync session serves one interactive server circuit. Prerender performs a
one-shot read; live registration starts from `OnAfterRenderAsync(firstRender)`
because that callback does not run during prerender. The application server
owns `/api/v1/sync`; the browser uses only Blazor's `/_blazor` SignalR circuit.
Components reference-count query listeners, marshal updates through
`InvokeAsync`, and dispose listeners with the circuit. A transient SignalR
disconnect does not dispose the retained circuit-scoped Sync session. Stateful
SignalR reconnect is a separate opt-in feature and must not be claimed without
an endpoint and browser proof.

### TypeScript and Vinext

TerraScale.TS is an ESM, dependency-free Node 22+ package with native fetch.
The Sync implementation can use native WebSocket, immutable snapshots, a local
canonical-key serializer, and a framework-neutral
`subscribe/getSnapshot/getServerSnapshot` store without a new runtime package.

The installed, proven Vinext stack is Vinext 0.2.0, React 19.2.7,
`@vitejs/plugin-rsc` 0.5.27, and VitePlus 0.2.6, whose embedded Vite reports
8.1.5. Vinext explicitly describes itself as experimental and under active
development. It supports App Router, RSC, route handlers, server actions,
streaming SSR, hydration, and HMR, but compatibility claims require build and
real-browser proof against these exact versions. Its `preferredRegion` and
route `runtime` configuration are ignored, and Node standalone support is less
mature. Regional behavior therefore comes solely from Sync routing. The
example belongs in `TerraScale.TypeScript/examples/terrascale-sync-vinext`;
substituting Next.js would not prove the requested stack.

Neither example can truthfully run yet. Platform has protocol and reducer
contracts but no Sync WebSocket endpoint, authenticated browser ticket API,
query execution, durable mutation receipt, or authoritative revision feed.
Example construction waits for those product contracts rather than introducing
sample-only transports or fake server behavior.

## External concepts studied

Public Convex documentation and source were studied only for observable
concepts: dependency-aware invalidation, shared identical-query execution,
versioned query sets, exact transition continuity, optimistic-base replay,
single-flight work, and bounded backpressure. TerraScale uses its own authority
model, storage layout, protocol, types, names, and implementation.

Microsoft’s Blazor/SignalR documentation informed circuit lifetime, WebSocket
preference, sticky sessions, retained disconnected circuits, and negotiated
stateful reconnect. Vinext behavior was verified against the installed package
and repository documentation.

## Primary risks carried into planning

- a scalar revision is unsafe with unrestricted multi-writer replication;
- indexed queries do not yet prove one snapshot contract;
- search/static index precision needs index-commit facts;
- restore and authority promotion need epoch fencing;
- retention must include resumable sessions and worker checkpoints;
- the development LXC alone cannot produce a valid performance baseline; the
  disposable KVM runner must stop DevHost, prove its cgroup quiescent, restore
  its prior state, allocate the 128 GiB disk only for persistent profiles, then
  close the host attestation before publication;
- current regional forwarding cannot carry WebSocket upgrades;
- the real examples cannot run until Platform and TerraBase expose the
  authoritative Sync server path;
- Vinext's experimental compatibility surface requires exact-version build,
  production-start, hydration, HMR, and browser evidence;
- dirty in-progress Platform placement/authentication work must be preserved and
  kept separate from the internal Sync routing projection.
