# Project regions and global replication

TerraScale owns region placement at the **project** boundary. A project selects
one or more currently available region codes; its databases, queues, and
project-scoped authentication inherit that placement. Child resources cannot
silently widen or narrow the project's data-residency boundary.

## Storage model

Each customer project has one physical TerraBase database named `proj-{projectId}` in
every selected regional cell. Logical databases and environments are virtual
partitions inside that physical database. Authentication documents, queue
definitions, and the durable queue replication outbox use the same project
database.

Within one regional cell the project database is always sharded with at least
three shards, dynamic node distribution, and local RF=3 on both the
orchestrator and every shard. Provisioning fails closed when a cell has fewer
than three data-capable TerraBase nodes; it never falls back to a non-sharded
or under-replicated project database. Region count is **not** a TerraBase
replication factor: selecting ten regions creates ten regional copies, each
with its own mandatory sharded RF=3 topology.

All seeded launch plans cap project selection at ten regions. That is the
qualified full-mesh ceiling for this release because direct peer cost grows
quadratically. `PlanEntitlements.MaxRegions` remains a configurable plan value
so a later topology can raise the limit after it is separately qualified; the
region catalog itself is not reduced to ten entries.

The configured TerraScale platform project is the sole storage-model exception.
In addition to its project-scoped backing store, it owns the four allowlisted
product service databases (`TerraScale.Authentication`, `TerraScale.Platform`,
`TerraScale.Payments`, and `TerraScale.Queue`). Bootstrap reconciles that
project's configured regions through the same placement-generation
compare-and-swap path. Customer projects cannot attach platform service
databases.

```text
Project placement: [gru, sfo, fra, ...]
  ├─ GRU cell: proj-{id}, >=3 shards, orchestrator + shard RF=3
  ├─ SFO cell: proj-{id}, >=3 shards, orchestrator + shard RF=3
  ├─ FRA cell: proj-{id}, >=3 shards, orchestrator + shard RF=3
  └─ selected future cells: same mandatory local topology

Inside every copy:
  ├─ logical database/environment document partitions
  ├─ project authentication records and regional authority epoch
  ├─ queue definitions
  └─ durable queue replication outbox and idempotency markers
```

## Placement lifecycle

`Project.Regions` is the desired state. Every placement change increments
`Project.PlacementGeneration`; stale generations cannot overwrite newer
placement in TerraBase.

Each logical project generation reserves two monotonic TerraBase record
generations: odd `2g-1` keeps the old-plus-desired transition mesh alive, and
even `2g` commits the final desired tag set only after catch-up and drain
checks pass. The API exposes the logical generation; the two engine phases are
an internal CAS detail. This lets region removal narrow tags without weakening
TerraBase's rule that every tag change must advance the record generation.

Regional APIs subscribe to the TerraBase Projects change feed. A selected cell
creates or updates its local project database immediately. A removed cell first
drains placement, then deletes its local copy after the generation has
converged. The operator's peer inventory scan remains an infrequent repair
path, not the normal control path.

API replicas in one cell do not all run that subscription or inventory sweep.
A TerraBase compare-exchange lease elects one regional placement-control
process, and the change listener plus reconciler share its cancellation epoch.
Losing or failing to renew the lease stops both workers before another replica
takes over; the normal five-second lease and one-second renewal cadence bound
failover without multiplying full-project scans by the API HPA replica count.

TerraBase database records carry generic, case-insensitive `PlacementTags` such
as `region:gru` plus `PlacementGeneration`. Server-wide peer tasks use OR
selectors, so a destination receives only databases tagged for that region.
Generation-zero or untagged project records are noncompliant and fail closed;
greenfield state must be recreated with an explicit positive generation and
region tags. An empty tag set with a positive generation is an explicit drain.

## Replication and consistency

Selected cells use direct, bidirectional TerraBase external replication. Any
healthy selected region can accept writes. Every project database explicitly
uses TerraBase's deterministic latest-write conflict solver. Concurrent writes
to the same document converge to one value (last-modified time with the engine's
stable tie-break), so applications that must reject lost updates use versions or
compare-and-exchange rather than relying on arrival order.

Local commits wake direct replication immediately. Changes received from a
peer use a bounded, jittered relay wake as a failed-link repair path, which
avoids synchronizing every full-mesh connection on every batch.

The product objectives are:

- local regional read/write p95 below 20 ms when the client is close to the
  serving region;
- replicated visibility in every healthy selected region within one second.

These are healthy-network objectives, not partition guarantees. A WAN
partition makes a strict one-second maximum impossible. `eng/TerraScale.MultiRegionSlo.cs`
measures concurrent origin reads and writes, validates the returned document
marker and direct serving-region headers, and reports p50/p95/p99/max replica
visibility. Release qualification uses `--release`, which refuses to run with
fewer than ten unique named region endpoints or fewer than twenty samples per
origin. It gates each origin's local read/write p95 independently, rotates the
write origin through every endpoint, reports every directed origin-to-target
link, and runs concurrent same-ID writes that must converge everywhere within
one second. A slow, one-way, conflicting, or nominally read-only region cannot
hide inside a combined percentile.

## Dynamic region catalog

The API reads `TERRASCALE_REGION_CATALOG_JSON`, a JSON array with:

- `code`, `displayName`, and `country`;
- `latitude` and `longitude` for region UX;
- `ociRegionCode` and `clusterNodeTag` inventory metadata;
- `available`, which controls new project selection.

The three-region GRU/SFO/FRA catalog is only a local fallback. Adding or
disabling a production region is a control-plane configuration change rather
than an API release. New selections reject unknown or unavailable regions;
stored placement preserves disabled or temporarily unknown codes so a catalog
change never moves existing customer data implicitly.

## Regional routing

Project routes inspect project placement before executing:

- a request served in a selected region stays local;
- an edge request outside placement is forwarded to the closest healthy
  selected origin;
- region response headers expose edge, serving, and current cell identity;
- write forwarding never expands project residency.

A metadata-only project has no Ready data region yet. Its first logical-
database creation, queue creation, or project-auth request is therefore routed
to a controlled bootstrap coordinator instead of failing with a transient
`project_region_unavailable`. If the request is already executing in a selected
cell, that known-available cell is the bootstrap coordinator; an edge cell
outside placement uses the canonical first selected region. Project-auth reads
and writes continue through the bootstrap path until at least one selected
placement is Ready, so an immediate create-then-list is coherent. Normal
active-active routing resumes as soon as a Ready region exists.

Project configuration PATCH requests are still protected by placement-
generation and document-version compare-and-swap, but they are not permanently
pinned to the first selected region. An explicitly preferred Ready region, the
current Ready selected region, or the first remaining Ready region can execute
the mutation. This lets a project remove a failed first-selected region without
depending on that failed region's API endpoint.

The Dashboard and SDKs obtain the catalog from `GET /api/v1/regions`; they do
not compile region codes into enums.

## Queues

Queue definitions inherit project regions. NATS JetStream remains cell-local
for low latency. TerraScale records each queue mutation in the project
database's durable outbox and delivers authenticated, idempotent unary
MagicOnion replication commands to the other selected regional Platforms.
This private RPC hop is not a public product API. It avoids a fragile global
NATS WAN cluster while preserving regional operation during a link failure.

Outbox wake-up signals and project reconciliation run with bounded concurrency;
the durable sweep is the recovery source of truth. Due delivery eligibility and
paging are evaluated by TerraBase using queryable outbox summary fields, so a
sweep never loads every queued message body into API memory.

Queue definitions are read in bounded TerraBase pages, queue-list statistics
use bounded concurrency, and each regional reconciliation sweep inventories
NATS streams once before grouping them by physical `project.{projectId}.`
prefix. A signal-only pass performs targeted repair and waits for the next
authoritative inventory before destructive cleanup.

Publish payloads are checked against the queue's `MaxMessageSizeBytes` before
an outbox document is written. A regional RPC result carrying status 400, 413,
or 422 is a permanent delivery rejection: the outbox delivery is terminally
canceled with an auditable `remote-rpc-{status}` reason instead of retrying
forever. Transport failures, timeouts, and other transient results continue
through bounded exponential retry.

Queue fanout is at-least-once **per selected region**. Each selected cell gets
its own regional copy and can process that copy independently, so one logical
publish can result in work being handled once in each selected region. There is
no cross-region exactly-once consumer protocol. Portable, signed, time-limited
receipt tokens support receive, complete, abandon, dead-letter, and lock
renewal without server-local receipt state. Consumers must use message IDs for
idempotency.

Removing a region starts a durable queue drain for that project and placement
generation. The cell stops being an origin for new project work, drains its
replication outbox, and keeps each local stream while messages, consumer pending
work, acknowledgements, or waiting receives remain. Inventory or transport
uncertainty also blocks deletion. The drain deadline only changes the durable
state from `Draining` to `Blocked`; it never forces deletion. The regional
placement reconciler may delete the physical project database and mark the cell
`Removed` only after the exact-generation queue drain is `Completed` with no
pending outbox or local streams. Re-selecting the region cancels the drain and
reconciles its streams again.

An outbox delivery that has not reached a region when that destination is
deselected is terminally canceled with reason `region-deselected`; it is not
reported as delivered. The compact cancellation record is retained for a
bounded audit window. Region removal still drains copies already accepted by
the local cell, while no longer retrying WAN delivery into a residency target
the project has explicitly removed.

## Authentication

Tenant users, sessions, credentials, organizations, roles, invitations, MFA,
and project API keys live only in the project's physical database and inherit
its placement. `ProjectAuthStorage__Mode=Project` is the only accepted tenant
mode. There is no shared-tenant fallback, legacy copy, dual write, or migration
marker. This is a greenfield clean break. Platform/operator identities and
platform popup sessions remain in the allowlisted `TerraScale.Authentication`
service database for the configured platform project.

The first tenant-auth request is serialized at the bootstrap coordinator. Its
first write lazily provisions `proj-{projectId}` and creates a deterministic
`AuthAuthorities` document. Its storage epoch equals the current project
placement generation and it records the exact selected writer regions plus the
supported authority protocol. Every regional writer validates that authority
before opening a tenant-auth session. A writer is rejected when its region is
not selected, its project metadata is behind a replicated newer epoch, the
authority protocol is unsupported, or the region set disagrees at the same
generation. The bounded authority cache defaults to 500 ms and cannot be
configured above one second, so a removed cell cannot retain a long-lived
authorization decision.

Email lookup does not use a dynamic query. A normalized project email maps to a
deterministic ULID identity document and a deterministic initial user ULID.
Concurrent creates in multiple regions therefore converge on the same document
keys instead of producing query-order-dependent duplicate users. Email changes
advance an email version; a stale identity is ignored unless its project,
normalized email, user ID, and email version all match the current user.

Credential rotation uses optimistic concurrency and a monotonically increasing
secret version. The next secret is derived deterministically from a shared
regional secret and `(project, key, next version, credential type)`, so two
regions racing the same generation return the same secret and converge on the
same credential document. Revocation is an independent deterministic tombstone;
rotation and last-used telemetry cannot erase it. Last-used timestamps live in
a separate document so observational writes never overwrite security state.
The API-key validation cache is bounded below the one-second replication SLO.

The `project-auth-storage-mode` readiness check reports Project mode, native
epoch fencing, authority protocol version, and that tenant shared fallback is
disabled. Any other mode or an authority cache above one second fails options
validation during startup.

## Metering

One billable database or queue operation represents up to 4 KiB. Units are
`max(1, ceil(bytes / 4096))`. Reads use response bytes; mutations use request or
explicit payload bytes. Replicated mutations are multiplied by the number of
selected project regions, making the storage/compute cost of regional fanout
visible instead of hiding it in a flat request count.

The serving region publishes a deterministic event to its local durable NATS
JetStream before request completion. That event carries the organization,
placement generation, and immutable billed-target region snapshot that admitted
the operation, so a later placement change cannot retroactively change its
price. Aggregation is asynchronous and writes
TerraBase counters keyed by both writer region and billed target region, so no
two active regions mutate the same counter document. If the NATS acknowledgement
is ambiguous or fails, a writer-owned TerraBase outbox retains the event for
idempotent relay. Readiness exposes queue/outbox depth and oldest-event lag;
metering failures after a committed customer mutation never rewrite that
customer response.

## Operational rollout

1. Upgrade every TerraBase node until the placement capability is reported for
   the whole cluster.
2. Upgrade TerraBase.Operator and its CRD.
3. Enable placement-aware replication on each regional cluster.
4. Deploy regional APIs with the same catalog and private regional RPC endpoint map.
5. Recreate greenfield project state with current placement generations.
6. Deploy Platform and Authentication in every region with
   `ProjectAuthStorage__Mode=Project`, the same credential-derivation secret,
   and the same authority protocol before accepting tenant-auth traffic.
7. Run the ten-region latency and same-ID convergence SLO tool. Independently
   exercise queue backlog and injected link failure recovery before advertising
   the one-second objective; those fault injections are not performed by the
   latency tool.

The capability checks fail closed: selector writes are not sent to a
mixed-version TerraBase cluster, and selector-free project replication state is
recreated rather than carried forward.
