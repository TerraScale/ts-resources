# Physical database branch lifecycle foundation — 2026-08-05

## Implemented

- Public, authenticated v1 capability endpoint: `GET /api/v1/projects/{projectId}/database-branches/capability`.
- Public clone-request endpoint: `POST /api/v1/projects/{projectId}/database-branches`.
- Both endpoints enforce project-management authorization. The clone request also verifies that its source logical database belongs to the requested project before recording a high-risk project audit event.
- The capability response has `admissionState: "unavailable"`; physical clone, promotion, and merge are all `false`. Clone requests return `503 Service Unavailable` after the audit attempt.
- Contracts are generated into the Platform v1 OpenAPI document. AppHost tests cover the contract plus authenticated capability, anonymous denial, cross-project denial, and unavailable clone behavior.

## Intentionally not qualified

The existing backup restore implementation is a logical side-by-side restore: it restores to a staging database and materializes data into a new logical database in the one physical `proj-{projectId}` database. Its Development/Preview/Production environments are also virtual partitions. Neither is exposed as a physical database branch.

No physical clone, point-in-time recovery branch, branch promotion, branch merge, asynchronous branch-operation state machine, or branch idempotency contract is admitted yet. Those require an Orchestrator-backed controller that proves isolated physical target provisioning, restore/PITR provenance, durable operation reconciliation, rollback/cleanup, and promotion/merge safety. Until then the API fails closed rather than manufacturing a virtual branch or a simulated operation.
