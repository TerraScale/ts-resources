# Dashboard system database, sharding, and backup

Status: current target contract.

## One system Project

Dashboard-owned Better Auth, Organizations, Projects, Users, Payments, MCP,
entitlements, consent, configuration, and audit state lives in a dedicated
system Organization and Project through the same public TerraScale database
contract available to customers.

The Dashboard system Project receives no direct TerraBase access.

## Placement

The system Project uses `all-available-regions`. It starts in GRU, SFO, and
FRA and automatically expands after a new Region passes catalog admission.

Each selected region stores the database on an RF=2 member pair. A SQLite shard
file has one local writer. Critical identity, authorization, payment,
entitlement, and bootstrap mutations use `GlobalDurable`, which requires at
least two active regions.

The system Project has reserved capacity or dedicated placement so a customer
noisy neighbor cannot stop login, authorization, billing, or recovery. It still
uses ordinary public API admission and database semantics.

## Key-range shards

The database starts as one SQLite file. TerraBase splits a hot database by key
range when it sustains more than 10,000 writes per second for five minutes, the
file exceeds 10 GB, or p99 write latency breaches its target for 15 minutes.
The split backfills a new file, tails the publication journal, cuts routing
over atomically, and then removes the moved range.

Do not precreate three shards or add intra-region multi-master writes. Queries
scatter and gather across key ranges through the routing layer.

## Backup and PITR

Litestream continuously ships each encrypted SQLite file to OCI Object Storage
for backup and PITR. It is not a replication or failover mechanism.

Restore creates a new database and replays through the normal system Project
bootstrap and authorization gates. It never promotes an Object Storage copy in
place.

Critical system data follows the retention baseline in the workspace
`GOAL.md`. Payment, tax, usage, security, auth, admin, MCP audit, live
personal-data deletion, immutable-backup expiry, PITR, logs, traces, and
metrics do not share one arbitrary retention period.

## Bootstrap

Orchestrator provisions:

- fixed system Organization, Project, and database identities;
- a short-lived X.509 Dashboard workload identity;
- a signed, certificate-bound, audience-bound, replay-protected
  `BootstrapGrant`; and
- a locally available rotated trust bundle for Database API.

The grant allows only idempotent bootstrap operations on fixed system Project
identities. It cannot access customer Projects.

After bootstrap, Dashboard uses a rotated workload credential through the
normal `@terrascale/sdk` credential provider.

## Recovery order

Complete recovery is dependency-aware:

1. restore TerraBase system Project active replicas and causal state;
2. verify Merkle roots, policy generations, and coordinated identity state;
3. restore and qualify Database API;
4. restore Dashboard Better Auth and product routes;
5. reconcile Stripe and authoritative usage ingestion;
6. reissue or rotate workload credentials as required; and
7. admit customer and MCP traffic.

The process must also work when NATS is empty or unavailable.

## Verification

Required tests include:

- one-Region and all-Region bootstrap;
- complete system Project data loss and restore;
- expired, replayed, wrong-audience, and customer-Project grant denial;
- Better Auth unique identity, one-time token, session rotation, and revocation
  races across Regions;
- Stripe webhook duplication, reordering, reconciliation, and entitlement
  publication;
- authoritative usage segment replay without duplicate billing;
- Member and Region failure;
- noisy-neighbor pressure while login and authorization remain admitted; and
- absence of private Dashboard-to-TerraBase access.
