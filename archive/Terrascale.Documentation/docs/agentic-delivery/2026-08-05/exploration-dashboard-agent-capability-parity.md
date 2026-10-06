# Dashboard and AI-agent capability parity exploration

Status: evidence-pinned exploration, not an implementation or production-readiness claim.

## Decision

Parity means that an authorized human in Dashboard and an authorized AI agent can use the *same released public capability*, subject to deliberately different interaction controls. It does not mean equal authority, a Dashboard proxy for MCP, or access to private transport. Dashboard server code composes named typed `@terrascale/sdk` operations; browser code calls only same-origin Dashboard handlers. MCP is an ordinary, configured-project adapter over typed public SDK operations. Neither may use a generic request escape hatch, private routes, MagicOnion, direct TerraBase, special headers, or tenant bypasses.

## Observed capability position

| Capability family | Human Dashboard | AI agent through MCP | Parity interpretation |
| --- | --- | --- | --- |
| Project, database, environment, access, billing, and administration workflows | Dashboard has public-SDK compositions, including mutations where the public contract permits them. | Intentionally unavailable for mutation, billing, credentials, administration, raw data, queues, and TQL. | Restricted by design. Do not close this gap by granting MCP broader authority. |
| Backup and restore inspection | Dashboard supports policy configuration, backup plan and confirmation, job status, and side-by-side restore composition. | Safe configured-project backup and restore-job reads are available. Restore-point and policy reads are withheld. | Read parity is partial and safety-scoped. Mutation parity is intentionally absent. |
| Backup execution | The public SDK has a typed, confirmed plan-to-execute flow with a caller-stable idempotency key. | `plan_database_backup` returns only action, database ID, digest, and expiry, discards the execution token, and has no execute tool. | Correct human-approval handoff, not an agent execution capability. |
| Recovery lifecycle and physical branches | Existing backup and restore views are not a physical-branch claim. | No branch or restore-candidate tools. | Both clients await a distinct public lifecycle contract and production qualification. |

The narrow Dashboard environment-deletion slice is no longer evidence of a reason to broaden MCP. The earlier parity record documents its implementation and review status separately. The primary unresolved issue is reusable public lifecycle semantics, not a client-specific route.

## Public-contract gaps to resolve before broad agent mutation

The backup confirmation flow is a useful capability-specific precedent, but it is not a general public mutation-admission or operation-receipt contract. A future agent-admitted mutation needs public, typed schemas for all of the following:

- prepare, non-agent-controlled approval, confirmation-token binding, execute, expiry and replay denial;
- stable idempotency, canonical request identity, authorization and tenant scope;
- durable operation receipt and queryable status: operation ID, safe state, timestamps, bounded failure category, retry guidance, audit reference, and replay result;
- lifecycle-specific policy, source lineage, retention, candidate validation, explicit promotion or cutover, and deletion semantics.

Do not infer these facts from a Dashboard toast, a backup job, an MCP annotation, or an engine implementation. The public SDK currently exposes backup-policy **configuration**, but there is no corresponding scoped public typed policy **read** suitable for MCP. The MCP adapter therefore correctly withholds policy claims. Restore-point response scope also prevents its safe MCP projection. These are contract and DTO gaps, not permission to add a private lookup.

## Access UX resilience

Dashboard access loading already aggregates typed-SDK failures and presents a partial-data warning. It should now make each unavailable section distinguishable from an empty result, retain the last safe view during a recoverable refresh failure, provide a scoped retry, and preserve form values and focus after invite, role, revoke, or authorization failures. Every retry must reuse the public operation's idempotency behavior when available. The same user-facing state must never be treated as an authorization decision: Platform remains the enforcement point.

MCP must return reduced, safe errors and must not turn an ambiguous timeout or unavailable response into a claimed mutation result. Until a durable public receipt exists, it must fail closed and direct the user to an approved human surface where appropriate.

## Phased delivery and evidence gates

| Phase | Accountable owner | Deliverable | Evidence gate |
| --- | --- | --- | --- |
| 0. Public semantics | Platform contract owner | Versioned REST and OpenAPI schemas for admission, receipt/status, scoped policy read, and lifecycle semantics. | Contract review proves authorization, tenant binding, replay/expiry denial, safe fields, and no Dashboard-only contract. |
| 1. Typed client parity | TypeScript and .NET SDK owners | Matching typed operations, DTOs, errors, idempotency and receipt polling. | Route/OpenAPI and field-nullability parity plus live public success and expected-denial evidence. |
| 2. Human composition | Dashboard owner | Server-only SDK orchestration, resilient access states, confirmation and operation-status UX. | Full-stack evidence proves same-origin browser boundary, typed SDK-only Platform access, retry behavior, tenant isolation, and accessible unavailable/conflict states. |
| 3. Agent admission | MCP owner with security authority | One narrowly admitted mutation after all Phase 0 and 1 contracts exist. | Independent proof of fixed scope, genuine approval authority, token binding, idempotent replay, audit receipt, safe output, and denial for replay, expiry, altered payload, and wrong caller or project. |
| 4. Recovery qualification | TerraBase, Platform, Orchestrator, operator authority | Physical recovery or branch substrate and runbooks. | Retained real-system restore, cleanup, provider-truth, retention, and clean-room DR evidence against approved targets. |

## Evidence provenance

Read-only inspection on 2026-08-05 used immutable source trees: `TerraScale.Internals` `85a72859787e6f35a2a6e3518c294810fd132eab`, `TerraScale.TypeScript` `9512c5c8d0fcaf3abbacb25a8465e77e44e6a155`, `TerraScale.Mcp` `6a02ac45668ef86eedc7109f7f05c80d0c79abb2`, and `TerraScale.DotNet` `d5437a0d1bc4fb0413f5249f297dc39dc79657b1`. The Dashboard boundary is recorded in `TerraScale.Dashboard.Next/AGENTS.md` and `src/lib/terrascale/factory.ts`; the TypeScript backup surface in `src/client.ts` and `src/models.ts`; and the MCP restriction in `README.md`, `TerraScaleReadService.cs`, and `docs/design/mcp-mutation-admission.md`. Related pinned readiness records are [MCP mutation readiness](readiness-mcp-mutation-boundary.md), [provisioning and recovery parity](readiness-provisioning-recovery-parity.md), and [public lifecycle parity](readiness-public-database-lifecycle-parity.md). No credentials, internal endpoints, or uncommitted source changes are evidence for this report.
