# Public database lifecycle parity readiness

Status: public environment and backup/restore-point surfaces exist. Physical database branching, production recovery guarantees, and customer-safe lifecycle observability are not yet a delivered parity claim.

## Essential distinction

`ProjectDatabaseEnvironment` is a **virtual environment**. The Platform source states that environments share the project's single physical TerraBase database and that environment creation does not create a physical database. It is therefore a metadata, routing, and lifecycle scope. It is not a branch, clone, independent storage volume, or a point-in-time recovery target.

A future **physical branch** needs its own durable engine-backed data state and explicit source lineage. It must not be inferred from the existing `Dev`, `Preview`, `Prod`, `Merged`, or deletion-status labels, nor exposed as a renamed virtual-environment operation.

## What the current product surface supports

| Area | Evidence in the pinned tree | Boundary that remains |
| --- | --- | --- |
| Platform | Project environment create/list/get/delete, durable deletion/reconciliation, backup-plan/execute, restore points, and side-by-side restore orchestration exist. | No versioned physical-branch lifecycle contract, source selector, lineage, promotion/merge semantics, TTL guarantee, or production RPO/RTO commitment. |
| TypeScript SDK | Typed `DatabaseEnvironment`, environment client routes, backup and restore-point models, and route tests exist. | No typed physical-branch or recovery-candidate contract. Existing environment types must retain their virtual meaning. |
| .NET SDK | Current typed backup client evidence exists. | Add the same physical lifecycle surface only after Platform publishes it; do not use generic requests to bridge a missing contract. |
| Dashboard | It can compose typed `@terrascale/sdk` public calls and own its workflow/route handlers. | It cannot define a Dashboard-only branch API, call TerraBase directly, or hide unsupported recovery semantics behind UI language. |
| TerraBase | Backup/restore implementation is actively evolving, including restore setup cleanup. | Engine evidence must demonstrate a reproducible physical clone or restore candidate and its recovery behavior before public claims. |
| Orchestrator | Host and recovery decision models remain deliberately separate from product database placement. | It must not schedule or define customer branch semantics. Its production backup, retained-volume, and DR qualification remains incomplete. |

## Phased delivery boundary and ownership

| Phase | Accountable product | Code-completable deliverable | Required evidence gate |
| --- | --- | --- | --- |
| 0. Semantic contract | Platform | Versioned REST schemas for physical branch create-from-source or restore point, operation status, lineage, TTL, delete, candidate validation, explicit promotion/cutover, audit, authorization, idempotency, and capability discovery. | Contract review proves virtual environments retain their present meaning; OpenAPI schema and security validation; no Dashboard-only fields. |
| 1. Engine and recovery substrate | TerraBase with Platform integration | Physical branch or restore-candidate primitive, lifecycle-safe cleanup, source identity, and provider-independent status reporting. | Real integration tests prove source isolation, retry/idempotency, failed cleanup, candidate validation, and recovery. Evidence defines what is and is not an RPO/RTO commitment. |
| 2. Public client parity | TypeScript SDK and .NET SDK | Generated or handwritten typed clients, errors, pagination/status polling, and compatibility tests for every Phase 0 operation. | Each SDK is checked against the released OpenAPI artifact and passes live-boundary contract tests. No generic-request escape hatch. |
| 3. Customer composition | Dashboard | Dashboard-owned handlers and views that compose the released TypeScript SDK, show operation state and safe observability, and request explicit destructive confirmation. | Full-stack tests prove browser-to-handler-to-SDK behavior, authorization/tenant isolation, retry visibility, and no direct TerraBase or private transport use. |
| 4. Operational qualification | Platform, TerraBase, Orchestrator, SRE/operator authority | Telemetry, audit export, backup/recovery runbooks, alerting, and production host/storage integration. | Independently retained clean-room restore, provider-truth, retention, failure, and DR drill evidence against approved targets. External operators approve targets and production enablement. |

## Observability parity gap

Expose only customer-safe, public lifecycle facts: operation ID and state, source and target identifiers that the caller may read, timestamps, bounded failure category, audit reference, lifecycle health, and documented retention/availability state. Do not expose NATS subjects, private MagicOnion details, host identities, raw infrastructure telemetry, or internal credentials.

Platform owns public operation and audit schemas. TerraBase owns engine measurements needed to substantiate them. Orchestrator owns host/control-plane telemetry but cannot become a customer lifecycle API. Dashboard presents the typed public view. SDKs preserve those fields without inventing operational detail.

## Non-negotiable release rule

Do not call a virtual environment a branch. Do not call a restore point PITR. Do not promise recovery, lineage, merge, TTL, observability completeness, RPO, or RTO until the associated phase has passed its evidence gate.

## Evidence provenance

Read-only inspection on 2026-08-05 used current `develop` trees: `TerraScale.Internals` `207b57898ced4c9a0d2f72968a68377dbb22e380`, `TerraScale.DotNet` `d5437a0d1bc4fb0413f5249f297dc39dc79657b1`, `TerraScale.TypeScript` `9512c5c8d0fcaf3abbacb25a8465e77e44e6a155`, `TerraBase` `eefb5357712e214144c63106a237005864510572`, and `TerraScale.Orchestrator` `e27e4c9f4ca729e9790b063665ae90d608059d26`.

Primary source locations are `TerraScale.Internals/src/Platform/TerraScale.Platform/Features/Projects/Services/ProjectDatabaseEnvironmentService.cs`, `Features/Projects/Services/EnvironmentDeletionReconciliationWorker.cs`, and `Features/Backups/Services/DatabaseBackupOrchestrationService.cs`; `TerraScale.TypeScript/src/models.ts` and `src/client-routes.test.ts`; the .NET SDK source tree; and the Orchestrator production-readiness audit. The public OpenAPI artifact was last changed by Internals commit `9e9d3851742335869186747a09389143f749aff7`. No credentials, internal endpoints, or environment values were inspected or recorded.
