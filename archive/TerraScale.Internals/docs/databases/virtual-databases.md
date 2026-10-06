# Virtual databases & the per-project TerraBase database

This document explains TerraScale's storage model: how the "databases" you see in
the Dashboard map onto physical TerraBase databases, and how each
(database, environment) pair becomes an isolated virtual database.

## TL;DR

- Each **customer project** owns exactly **one** physical TerraBase database, named
  `proj-{projectId}` (lowercased ULID).
- Each "database" shown in the Dashboard is a **logical database** (metadata only).
- Every logical database always gets **three environments**: Development, Preview,
  Production.
- Each `(logical database, environment)` pair is a **virtual database**: a logical
  partition *inside* the single project TerraBase database, encoded into the
  physical collection name.
- TerraBase has no native multi-tenancy, so isolation is enforced at the
  application seam, not by the server.

---

The configured TerraScale platform project is the sole exception: in addition
to its project-scoped backing store, it owns the four fixed product service
databases, including the neutral `TerraScale.Platform` store, documented in
[service-databases-sharding-and-backups.md](./service-databases-sharding-and-backups.md).
Customer projects cannot attach those service databases. Dashboard Next owns no
TerraBase database or client; it consumes product data through the typed
TerraScale TypeScript SDK.

## 1. The physical layer: one TerraBase database per customer project

A project's physical TerraBase database is created lazily when its first
storage-backed resource (logical database, queue, or project-auth record) is
provisioned. Creating a project or changing the
regions of a still-empty project does not allocate an idle RF3 database. The
first database path is owned by:

- `Internals/src/Platform/TerraScale.Platform/Features/Projects/Services/ProjectDatabaseProvisioner.cs`
  → `ProjectDatabaseProvisioner.EnsureProjectDatabaseAsync`

That method computes the physical name and delegates to the database manager:

```text
PhysicalDatabaseName(projectId) = "proj-" + projectId.ToString().ToLowerInvariant()
EnsureProjectDatabaseAsync → TerraBaseDatabaseManager.EnsureProjectShardedDatabaseAsync(
    name,
    shardCount >= 3,
    replicationFactor = 3,
    dynamicNodeDistribution = true)
```

Provisioning is idempotent and fail-closed. The first call creates
`proj-{projectId}` with at least three shards and three actual members on the
orchestrator and every shard in the current selected regional cell. Subsequent
calls revalidate and heal that topology upward; promotables and rehab nodes do
not count as ready members. Project regions control which regional cells host
and actively replicate the database, not the local RF. See
[regions-and-replication.md](./regions-and-replication.md).

There is never more than one physical TerraBase database per customer project.

## 2. The logical layer: what the Dashboard calls a "database"

The "databases" surfaced in the Dashboard are **logical databases** — pure
metadata. They are represented by:

- `ProjectDatabase` in
  `Internals/src/Platform/TerraScale.Platform/Features/Projects/Models/ProjectDatabase.cs`

A logical database carries no storage of its own. When you "create a database"
from the Dashboard, TerraScale:

1. Ensures the project's physical database exists (Section 1).
2. Creates a `ProjectDatabase` metadata record.
3. Always creates **three** `ProjectDatabaseEnvironment` rows beneath it.

The three environments are fixed and defined by
`CoreMetadataService.StandardDatabaseEnvironments`:

```text
("Development", EnvironmentKind.Dev)
("Preview",     EnvironmentKind.Preview)
("Production",  EnvironmentKind.Prod)
```

Created together in `CoreMetadataService.CreateProjectDatabaseAsync`. You cannot
create a logical database without all three environments; the wizard does not
expose environment configuration (defaults are applied — see
[create-database-wizard.md](./create-database-wizard.md)).

## 3. The virtual layer: partitioning inside one physical DB

Each `(logical database, environment)` pair is a **virtual database**: a logical
partition inside the single project TerraBase database. They are **not**
separate physical TerraBase databases.

Partitioning is done by encoding the partition into every document's physical
collection name:

- `RepositoryPartition.EncodePhysicalCollection` in
  `Internals/src/Platform/TerraScale.Platform/Features/Database/TerraBase/Documents/RepositoryPartition.cs`

```text
physical collection = ts.{logicalDatabaseId}.{environmentId}.{friendlyCollection}
```

Examples:

```text
ts.01H...dev.01H...prev.users      ← Preview "users" collection
ts.01H...dev.01H...prod.users      ← Production "users" collection (distinct collection, distinct schema)
ts.01H...dev.01H...dev.orders      ← Development "orders" collection
```

Empty/missing tokens collapse to `default`. This gives **storage-level
isolation**: each virtual database is a distinct TerraBase collection with its
own schema and no cross-partition leakage, achieved without query-time filters.

The split between public and physical names is preserved on the document
itself:

- Friendly (public) collection name: `RepositoryDefinitionDocument.Collection`
- Physical (partition-encoded) collection name:
  `RepositoryDefinitionDocument.PhysicalCollection` /
  `RepositoryDefinitionDocument.EffectivePhysicalCollection`

## 4. The single data-access seam

All reads and writes flow through one seam:

- `TerraScaleRepositoryManager` / `TerraScaleRepositoryDocuments` under
  `Internals/src/Platform/TerraScale.Platform/Features/Database/TerraBase/Services/`

Every operation resolves the target via
`RepositoryStorageDefinition.PhysicalCollection`, so the partition encoding is
applied exactly once, at the boundary. No caller ever constructs a
`ts.{...}.{...}.{...}` string by hand.

## 5. Routing & authorization

Physical database resolution lives in `TerraScaleRepositoryManager`:
`ResolveCreateDatabaseNameAsync`. Because `ProjectDatabase` /
`ProjectDatabaseEnvironment.TerraBaseDatabaseName` now points at
`proj-{projectId}`, **every branch of the resolver lands in the shared project
database** regardless of which logical database or environment the caller is
targeting.

Authorization is by **logical coordinates**, not physical DB name. API keys are
checked via `TerraScaleApiKeyScope.AllowsRepository` against
`(LogicalDatabaseId, EnvironmentId)`. This means a key scoped to "Production of
database X" cannot read "Development of database X", even though both live in
the same physical TerraBase database — the seam enforces the boundary.

## 6. The honest tradeoff (read this)

TerraBase is a TerraScale-owned fork of RavenDB. Critically:

- TerraBase/RavenDB has **no native "virtual database" or tenant concept**.
- Collections are a **query/index partition**, not a **security boundary**.
- Sharding scales one database *out* (more nodes for the same DB) — the wrong
  direction for tenant isolation.

Virtual databases are therefore an **application-layer abstraction**. The
isolation is enforced at the seam (`TerraScaleRepositoryManager` /
`TerraScaleRepositoryDocuments`), not by the server. Consequences:

- Any **raw RQL or HTTP** issued directly against the physical `proj-{projectId}`
  database **bypasses** the abstraction entirely and can read across virtual
  databases.
- Operational/observability tooling that talks to TerraBase directly sees one
  physical database with many `ts.*` collections, not three tidy virtual DBs.
- The security boundary is the API + seam, never the storage engine.

This tradeoff is accepted deliberately: it keeps provisioning cheap (one
physical DB per project, replicated across the cluster) and lets the
`(LogicalDatabaseId, EnvironmentId)` coordinate system stay stable.

## 7. Hardening path (future)

The model is designed so that virtual databases can be promoted to real
physical databases with **no call-site change**:

- Flip `ProjectDatabaseEnvironment.TerraBaseDatabaseName` from `proj-{projectId}`
  back to a per-environment physical DB name.
- The `(LogicalDatabaseId, EnvironmentId)` coordinates are already persisted on
  every document and every environment row, so `ResolveCreateDatabaseNameAsync`
  simply starts resolving to a different physical name.
- The seam, the API-key scopes, and the public product contracts consumed through
  the TypeScript SDK are unchanged.

In other words: today's abstraction is forward-compatible with a
"one physical DB per environment" world if isolation requirements ever demand
server-enforced separation.

## 8. End-to-end flow

```text
Dashboard wizard
  └─ POST /api/v1/projects/{projectId}/databases (Name)
       └─ CreateProjectDatabaseEndpoint.HandleAsync
            ├─ ProjectDatabaseProvisioner.EnsureProjectDatabaseAsync
            │      └─ TerraBaseDatabaseManager.EnsureProjectShardedDatabaseAsync("proj-{projectId}")
            │             → >=3 shards, orchestrator + every shard RF3,
            │               three actual members, dynamic distribution
            └─ CoreMetadataService.CreateProjectDatabaseAsync
                 ├─ create ProjectDatabase            (logical metadata)
                 └─ create 3 × ProjectDatabaseEnvironment   (Dev, Preview, Prod)

Later: any document write
  └─ TerraScaleRepositoryDocuments (the seam)
       └─ RepositoryStorageDefinition.PhysicalCollection
            = ts.{logicalDatabaseId}.{environmentId}.{friendlyCollection}
            → stored inside proj-{projectId}
```

## Related

- [create-database-wizard.md](./create-database-wizard.md) — the Dashboard UX
  that triggers provisioning.
- [regions-and-replication.md](./regions-and-replication.md) — how project-owned
  `Regions` select the regional replication cells.
