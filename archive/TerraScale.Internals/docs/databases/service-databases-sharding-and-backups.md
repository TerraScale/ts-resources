# Service databases: sharding, replication, and incremental backups

TerraScale’s four product/service databases:

- `TerraScale.Authentication`
- `TerraScale.Platform`
- `TerraScale.Payments`
- `TerraScale.Queue`

These are the sole exception to the one-physical-database-per-customer-project
model. Only the configured TerraScale platform project may attach them in
metadata. The names are an explicit allowlist; customer projects and arbitrary
physical database names are rejected by the product-database ensure path.

## Topology (desired)

| Setting | Value |
|---|---|
| Sharding | 3 shards (`0,1,2`) |
| Replication factor | 3 (orchestrator + each shard) |
| Dynamic node distribution | `true` |
| Placement | `global` (mesh-replicated across cells) |

Bootstrap also reconciles the platform project's configured regions using the
normal placement-generation compare-and-swap path. Service database options
always resolve all four fixed names and reject renamed/duplicate names, fewer
than three shards, RF below 3, or disabled dynamic distribution at startup.
There is no development fallback to a smaller live topology.

Bootstrap (GRU only) creates/ensures these via
`ProjectDatabaseProvisioner.EnsureNamedProductDatabaseAsync` →
`TerraBaseDatabaseManager.EnsureShardedDatabaseAsync`.

Customer `proj-*` databases use a separate, stricter contract: every selected
regional cell must expose at least three shards with RF=3 on the orchestrator
and every shard. Project provisioning fails closed when a cell has fewer than
three actual TerraBase data members. The service-database migration tool below
must never be used for `proj-*`; it uses global placement and does not preserve
project placement generations or residency.

### Snapshot backups are not supported on sharded DBs

TerraBase throws `NotSupportedInShardingException` for `BackupType.Snapshot`.
Service databases use logical **`BackupType.Backup`** so incremental chains work.

## Backups (desired)

| Setting | Value |
|---|---|
| Type | Logical `Backup` |
| Full | `0 0 * * *` (daily 00:00 UTC) |
| Incremental | `0 * * * *` (hourly) |
| Retention | **7 days only** |
| Destination | LocalFolder (dev/launch) or S3-compatible object storage (production durable path) |

Configured on bootstrap by `DatabaseBackupOrchestrationService.EnsureServiceDatabaseBackupPolicyAsync`.

Config section: `TerraScale:Backups` (`ServiceFullBackupCron`, `ServiceIncrementalBackupCron`, `ServiceRetentionDays`).

## Migrating existing non-sharded service DBs

TerraBase cannot convert non-sharded → sharded in place. Use the ops tool:

```bash
cd /workspaces/TerraScale/TerraScale.Internals
dotnet run --file eng/TerraScale.MigrateServiceDatabasesToSharded.cs -- \
  --urls https://127.0.0.1:28443 \
  --cert /path/tls.crt --key /path/tls.key \
  --export-dir /tmp/service-db-migration \
  --dry-run

# then without --dry-run, per DB or all:
dotnet run --file eng/TerraScale.MigrateServiceDatabasesToSharded.cs -- \
  --urls https://127.0.0.1:28443 \
  --cert /path/tls.crt --key /path/tls.key \
  --export-dir /tmp/service-db-migration
```

Preferred order: **Queue → Payments → Authentication → Platform**.

The tool accepts only those four names and rejects `--shards` or `--rf` values
below 3 before connecting to TerraBase.

After migration, restart the GRU Platform workload so product bootstrap attaches
backup policies (or wait for its next restart). Existing non-sharded service DBs
cause bootstrap to fail closed with a migration message.

Non-sharded customer `proj-*` databases are noncompliant greenfield state and
must be deleted/recreated or restored into a newly provisioned RF3-sharded
project database. Do not point the service migration tool at a project database.

## Related

- `Features/Projects/Services/ProjectDatabaseProvisioner.cs`
- `Features/Database/TerraBase/Services/TerraBaseDatabaseManager.cs`
- `Features/Backups/Services/DatabaseBackupOrchestrationService.cs`
- `eng/TerraScale.MigrateServiceDatabasesToSharded.cs`
