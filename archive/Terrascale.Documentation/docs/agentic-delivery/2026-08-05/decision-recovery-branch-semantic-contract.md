# Recovery and initial branch semantic contract

Date: 2026-08-05
Status: planning decision and evidence requirement, not an availability or production-readiness claim.

## Scope and claim boundary

This document freezes the customer-safe meaning required before a public recovery or database-branch contract is designed in Platform. It is based on the production design assessment in the workspace report, not on a released Platform OpenAPI artifact, SDK export, or completed recovery drill. It therefore documents required semantics and proof gates only. It does not document paths, request schemas, SDK methods, limits, regions, RPO, RTO, or feature availability.

Do not state or imply that branching, point-in-time recovery (PITR), promotion, merge, recovery coverage, a particular recovery point, or a recovery objective is available until the owning public contract, release state, and applicable evidence gate below are complete.

## Terms

| Term | Required meaning |
| --- | --- |
| Recovery coverage | Observed evidence for a database: earliest recoverable time, latest eligible data cut, granularity, retention boundary, chain health, region scope, and whether recovery is currently possible. It is not an inferred schedule or an unverified objective. |
| Recovery point | An immutable, integrity-verified artifact or checkpoint eligible for materialization. It identifies its exact data-cut timestamp, source generation, compatibility state, lineage, and retention expiry. |
| Requested time | A customer-provided time used to select a point. The service must return the exact selected point and data-cut timestamp, or reject the request. |
| Recovery candidate | A new side-by-side target materialized from a selected recovery point. It is isolated, non-routable, and never overwrites the source. |
| Initial branch | A separately identified, independently writable logical database materialized from a completed recovery artifact or checkpoint. It has its own lifecycle, quota, credentials, and lineage. |
| Ready | The terminal state after durable publication and required validation. A target is not customer-routable or writable before Ready. |
| Hold | An authorized retention restriction that prevents deletion of referenced recovery evidence until the hold is released by an authorized workflow. |

## Initial branch and recovery semantics

- A recovery operation always creates a side-by-side candidate. It never changes, replaces, or routes traffic away from the source database.
- A candidate remains non-routable until validation and durable publication establish Ready. The source may continue serving writes while materialization runs; writes after the selected data cut are not included in the target.
- The initial branch is a materialized, separate database, not a storage-level copy-on-write view. Source and branch do not share mutable data after creation and may diverge permanently.
- A branch receives new credentials and explicit least-privilege authorization grant provisioning. It never inherits source authorization grants, sessions, API keys, or raw credentials.
- Requested-time recovery resolves only to a proved eligible checkpoint. Do not promise arbitrary wall-clock PITR unless continuous-log capture, ordering, integrity, replay, and exact checkpoint-watermark proof exist.
- A backup schedule or last successful backup is not recovery coverage. An uploaded object is not an eligible recovery point until continuity, integrity, compatibility, and application-consistency checks pass.

## Explicit non-goals for the initial release

- No copy-on-write, instant, or cost-free clone claim.
- No automatic merge, rebase, promotion, source replacement, or traffic routing.
- No in-place restore or source overwrite.
- No arbitrary-time PITR claim without the continuous-log proof stated above.
- No automatic customer access to a candidate before Ready.
- No Dashboard-only route, DTO, authorization shortcut, direct TerraBase access, generic SDK request, private endpoint, or privileged header.
- Public consumers use versioned REST and only contracted WebSocket or SSE behavior where streaming is part of the public contract. Backend-only mechanisms are never exposed.
- No MCP mutation in the initial release. MCP may only add separately approved, safe read projections after the public contract and typed SDK support exist.

## Plan, confirmation, idempotency, and expiry

Every recovery creation, branch creation, retention reduction, hold override, branch expiry/deletion, or future cutover is a separate operation with durable state. Each destructive or data-creating action requires:

1. An expiring server-side plan that binds the actor, authorization decision, source, resolved immutable point, target, current resource versions, requested TTL, impact, and operation digest.
2. An explicit confirmation of that exact plan. A changed source, target, point, policy, or resource version invalidates the confirmation.
3. A caller idempotency key and a durable operation record that make retries and lost responses safe to reconcile.
4. A terminal audit record and safe audit correlation identifier. Cancellation is permitted only before the documented irreversible boundary.

The plan must state that the source remains unchanged and that the result is a separate candidate or branch. It must resolve capacity, placement, compatibility, retention/hold constraints, authorization, and quota reservation before creating a target.

## Authorization, isolation, retention, and audit

Recovery authority is distinct from normal database data access. The proposed permission family is `recovery-read`, `recovery-policy-manage`, `recovery-create`, `recovery-promote`, and `recovery-delete`. The first release may expose only the read, policy-manage, and create roles after proof. Promotion and deletion remain unavailable until their separate safeguards are proven. Machine credentials require explicit recovery scopes; broad database data access does not confer recovery authority.

Every lookup and action must begin with project membership and independently verify ownership of the source, target, recovery point, branch, operation, and audit event. Cross-project or cross-organization selection is denied without existence disclosure. Dashboard server code composes typed `@terrascale/sdk` calls as an external consumer, and browser code calls only Dashboard-owned handlers.

Successful artifact manifests are immutable. Retention must preserve every artifact chain referenced by an eligible point, active plan, branch, rollback window, or hold. Retention reduction, hold override, and deletion require the plan and confirmation sequence above. Reconciliation must retain uncertain forensic evidence rather than delete it automatically.

Audit evidence records actor and authorization basis, safe project/source/target/point/operation identifiers, request digest, idempotency outcome, state transitions, validation result, and safe reason code. It must not contain database data, object locations, credentials, tokens, encryption keys, connection strings, or internal topology.

## Customer claim rules

| Claim | Required evidence before it may be published |
| --- | --- |
| Availability of recovery coverage or recovery points | Released public contract, typed SDK parity, integrity and continuity proof, tenant-denial proof, and a current safe status projection. |
| A requested time can be recovered | Exact selected checkpoint and data-cut semantics, plus continuous-log proof if the claim is arbitrary wall-clock PITR. |
| Availability of branch creation | Released public contract, independently writable materialized-target proof, tenant isolation, quota/idempotency/audit evidence, and candidate non-routing proof. |
| Recovery objective, RPO, or RTO | Tier-specific measurements from retained clean-room drills, approved objective, alert/runbook exercise, and production release approval. |
| Promotion, merge, rebase, or source replacement | Dedicated accepted design and real proof for fencing, routing/session drain, conflict or ordering semantics, rollback, reconciliation, authorization, and destructive-operation controls. |

Local tests, implementation substrate, a planned schema, or an SDK type alone are not sufficient evidence for any customer availability or production claim.

## Implementation and evidence matrix

| Owner repository | Required deliverable | Proof gate before a related claim |
| --- | --- | --- |
| Terrascale.Documentation | This semantic contract, claim rules, and later customer guidance only after evidence review. | Independent review confirms every public statement is backed by released contract and retained evidence. |
| TerraBase | Artifact/checkpoint semantics, exact data-cut definition, ordered-chain integrity, restore compatibility, and any continuous-log capability. | Real engine recovery tests cover corruption, ordering, compatibility, restart, and target isolation. |
| TerraScale.Orchestrator | Backup destination, key-reference lifecycle, retention/reconciliation, placement, restart recovery, observability, and runbooks. | Provisioned recovery exercise proves lifecycle, retention, controller restart, regional failure handling, and backend mechanism isolation. |
| TerraScale.Internals Platform | Dashboard-agnostic versioned public recovery coverage, point, plan, operation, candidate, branch, authorization, quota, idempotency, and audit contract. | Real AppHost integration proves two-tenant isolation, plan expiry/mismatch, retries, no source overwrite, durable audit, and safe status projections. |
| TerraScale.TypeScript and TerraScale.DotNet | Typed public clients generated or implemented from the released Platform contract. | Contract parity and live-boundary success, denial, cancellation, and idempotency checks. |
| TerraScale.Internals Dashboard tree | Dashboard-owned composition of typed TypeScript SDK operations and recovery UI. | AppHost E2E proves SDK-only server access, same-origin browser boundary, confirmation, status, authorization denial, and target isolation. |
| TerraScale.Mcp | Safe read-only recovery and branch projections, if approved after Platform and SDK support. | Tool inventory and E2E prove configured-project binding, sanitized output, malformed-ID denial, and no mutation capability. |
| SRE, security, and independent DR review | Objective approval, threat/retention/key review, clean-room drill, alert/runbook exercise, and release decision. | Retained redacted clean-room evidence establishes measured RPO/RTO by tier before any production claim. |

## Contract change discipline

Platform owns the versioned public REST contract. Dashboard, SDKs, MCP, and this documentation must follow it as external consumers. New public streaming behavior requires an explicit versioned WebSocket or SSE contract; backend-only RPC is never exposed to public consumers. A future API document must be synchronized to the approved Platform artifact and record the source revision in its change evidence. Until then, this decision intentionally contains no endpoint shapes or client examples.
