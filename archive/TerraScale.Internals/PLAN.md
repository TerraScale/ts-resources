# TerraScale Sync delivery plan

Status: architecture gate in progress. Broad implementation is blocked until the
starting performance baseline is valid and the contracts in
`docs/implementation/sync/PLAN.md` have executable contract tests.

The production design has four authorities:

1. TerraBase is the authority for database revisions, committed change facts,
   read dependencies, snapshots, replication watermarks, retention, and mutation
   idempotency.
2. TerraScale Platform is the public Sync endpoint, nearest regional ingress,
   shared query/session host, and policy enforcement point.
3. TerraScale Orchestrator is the authority for private Platform endpoints,
   workload health, capacity, drain state, certificates, and regional backhaul.
4. TerraScale.NET and TerraScale.TS are protocol clients. Framework examples
   consume those SDKs and contain no alternate synchronization path.

The detailed, cross-repository contract is
[`docs/implementation/sync/PLAN.md`](docs/implementation/sync/PLAN.md).
Exploration evidence is in
[`docs/implementation/sync/EXPLORATION.md`](docs/implementation/sync/EXPLORATION.md),
and the performance gate is in
[`docs/implementation/sync/performance/BASELINE.md`](docs/implementation/sync/performance/BASELINE.md).

## Delivery order

1. Establish and preserve the exact-source baseline.
2. Land generated protocol contracts and state-machine conformance tests.
3. Add TerraBase revision/change-log storage at the document transaction commit
   seam, then prove every supported write path and replication/restore behavior.
4. Add dependency capture and snapshot-aware reactive batch execution.
5. Add shared query ownership, reverse dependency indexes, cache, sessions,
   bounded transport, resume, and mutation ordering in Platform.
6. Add placement observations and pre-upgrade regional WebSocket forwarding.
7. Add both SDKs, then the Blazor Server and Vinext examples.
8. Run integration, browser, regional failure, load, and before/after benchmark
   gates.
9. Perform a no-edit hostile review, fix every valid finding, rerun every gate,
   deploy the real regional topology, and write the final evidence summary.

Each coherent change is committed and pushed to `develop` in its owning
repository. No compatibility implementation, polling fallback, or parallel
protocol is permitted.

## Repository ownership

| Repository | Sync ownership |
| --- | --- |
| `TerraBase` | revisions, change log, dependency capture, reactive read batch, retention, replication, restore epoch |
| `TerraScale.Internals` | public protocol endpoint, shared queries, sessions, routing projection, AppHost and integration tests |
| `TerraScale.Orchestrator` | private backhaul endpoints, service health/capacity/drain observations, regional test topology |
| `TerraScale.DotNet` | .NET client and Blazor Server example |
| `TerraScale.TypeScript` | TypeScript client/store and Vinext example |
| `TerraBase.Benchmark` | realistic database/load comparisons and immutable results |

`TerraScale.Infrastructure` and `Terrabase.Operator` remain retired. Dashboard
code is not a Sync backend and accesses Sync only through public SDK contracts.

## Architecture gates

Broad implementation starts only after all of these are true:

- The exact starting TerraBase image and source commit are immutable.
- Two valid Standard runs and one valid Persistent run in the attested
  `dedicated-kvm-guest` environment have passed and established the noise floor.
- `DatabaseRevision`, restore epochs, leader changes, replica watermarks, and
  reconnect monotonicity have one tested representation.
- Protocol transitions have exact start-version validation and atomic client
  reducer tests.
- Remote WebSocket routing selects and authenticates the destination before the
  101 response.
- Performance budgets and before/after run commands are fixed.

No accepted regression is known yet. Any later accepted regression must be
recorded here with its measurement, noise threshold, benefit, alternatives, and
compensating optimization.
