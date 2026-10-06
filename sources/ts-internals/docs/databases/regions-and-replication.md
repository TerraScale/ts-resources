# Database regions and replication

Status: current. The workspace `GOAL.md` and TerraBase contracts are
authoritative.

## Customer placement

A database owner selects one to three regions at launch. The launch catalog is
GRU, SFO, and FRA. Catalog availability, capacity, residency policy, plan
limits, and authorization constrain the choice.

Every selected region stores every key-range shard, accepts reads and writes,
and replicates with the other selected regions. A request that reaches an
unselected region routes to an eligible selected region or fails with a typed
placement outcome.

Placement belongs to the database. Project policy may restrict available
regions but does not force every database in a project to use the same set.

## Local replica shape

Each SQLite shard file has exactly one local writer. An RF=2 journal follower
keeps the second local copy and can be promoted after the current writer is
fenced. The two members are not concurrent writers for the same file.

`RegionalDurable` succeeds after the writer and its local RF=2 follower make
the mutation durable. If either copy is unavailable, the region does not weaken
the contract. Eligible traffic may route to another selected region while the
orchestrator replaces and catches up the failed member.

A single-region database becomes unavailable for writes until its local RF=2
pair can satisfy durability.

## Durability choices

| Level | Contract |
| --- | --- |
| `RegionalDurable` | The local writer and RF=2 follower make the mutation durable. No WAN acknowledgement. |
| `GlobalDurable` | At least two active regions acknowledge durable copies. The write fails closed when fewer than two regions are active. |

`RegionalDurable` accepts a complete-region loss window. If a region is
destroyed before replication reaches another region, its newest acknowledged
writes may be lost. The public API and SDK must state that plainly.

## Key-range sharding

A database starts as one SQLite file per selected-region replica. TerraBase
splits it by key range when one file sustains more than 10,000 writes per
second for five minutes, exceeds 10 GB, or breaches its p99 write-latency target
for 15 minutes.

The split creates a new file, backfills the selected key range, tails the
publication journal until caught up, switches routing atomically, verifies the
new placement, and removes the moved range. Queries scatter and gather through
the routing layer. A split never adds intra-region multi-master writes.

## Cross-region replication

Selected regions accept writes independently. TerraBase uses causal metadata,
CRDT merge, deterministic conflict resolution, durable repair, and snapshots
to converge after delay, reordering, reconnect, restart, or WAN partition.

Cross-region CRDT behavior is separate from the local RF=2 follower. Transport
delivery does not define correctness. Causal identity and deterministic merge
do.

NATS may carry optional control-plane configuration or discovery. It never
carries customer data or decides database membership, replication, recovery,
or durability.

## Backup and PITR

Litestream continuously ships each database file to OCI Object Storage. Backup
and PITR are disaster-recovery mechanisms, not replication or failover paths.
Restore always creates a new database.

Retention follows the plan: Free 1 day, Starter 7 days, Pro 30 days, and Scale
35 days. Backup streams use the database encryption key, so key destruction
also covers retained backups.

## Placement changes

Adding a region validates catalog, residency, capacity, plan, and authorization
before it creates RF=2 replicas. The workflow copies a verified snapshot,
catches up the publication journal, checks routing and health, then publishes
the new placement generation.

Removing a region fences new routing, proves another permitted copy satisfies
the requested durability, drains reactive sessions, removes active and
temporary copies, and keeps backup data only for its retention window or legal
hold. The public status reports progress and failure instead of claiming
completion from control-plane intent.

## Session consistency

Public reads support eventual, session, and causal policies. Reactive clients
receive read-your-writes and monotonic session reads by default.

A client moving between regions presents a sparse causal token. The serving
region satisfies it locally, waits or fetches under the requested policy, or
returns a typed unsatisfied result. It never invents causality from wall-clock
time.

## Customer status

The public status model separates placement intent, writer and follower health,
requested and observed durability, causal lag, repair, backup progress,
reactive lag, and capacity pressure. A healthy connection alone is not a
replication status.
