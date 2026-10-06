# Database isolation in TerraBase

Status: current. The workspace `GOAL.md` is authoritative.

## Safety decision

Collections are not tenant boundaries. Encoding tenant, project, or database
identity into a collection name would let query, index, backup, restore,
subscription, or administration paths bypass isolation.

TerraBase binds tenant, project, database, and principal identity to every
storage, query, index, replication, backup, recovery, sync, and usage
operation.

## Product model

An organization owns projects. A project owns databases within its plan limit.
Each database has a stable typed scope:

```text
TenantId
ProjectId
DatabaseId
```

The Database API derives that scope from the authenticated caller, route, and
verified grant. Caller JSON, headers, query text, and document content cannot
override it. The public API never exposes member names, file paths, shard key
ranges, or engine storage names.

## Storage shape

Each customer database starts as one SQLite file on each selected-region
replica. Rows store the document id, canonical JSON body bytes, CRDT metadata,
revision, expiry, and extracted index columns. The publication journal commits
in the same transaction as the mutation.

One writer owns each local file. When a database exceeds a D-28 split trigger,
TerraBase moves a deterministic key range into another file and updates
routing atomically. A query may scatter and gather across those files without
changing the public database identity.

Members host many database files and share process resources under bounded
per-database governance. A small database does not need a dedicated process or
preallocated shard set. A sustained high-load database may receive dedicated
placement without changing its public identity.

## Engine enforcement

TerraBase checks the typed scope before document and family access, TQL
planning, index work, schema operations, import and export, backup and restore,
reactive setup and reconnect, usage export, or administration. A scope mismatch
fails closed before storage or index access.

Database API uses named `terrabase-go` methods. It does not accept raw engine
operations or caller-selected physical placement.

## Lifecycle

Creation allocates catalog identity on shared members and must complete within
five seconds at p99. It never provisions a VM. Physical database files may be
created lazily on the first write.

Deletion fences writes and subscriptions, records the deletion generation,
removes active files, indexes, caches, and temporary data from every selected
region, and prevents identity reuse. Litestream backup objects expire under the
plan's PITR window or legal hold. Destroying the per-database key makes all
remaining encrypted copies unreadable.

## Required tests

- Cross-tenant, cross-project, and cross-database denial.
- TQL, index, subscription, checkpoint, export, backup, and restore isolation.
- Many small databases on one member with bounded per-database resources.
- One hot database under pressure while a small neighbor remains admitted.
- Key-range split without public identity change.
- Deletion across selected regions and the backup-retention window.
- Rejection of caller-controlled physical scope or collection-prefix escape.
