# Agentic delivery exploration

Date: 2026-08-04
Status: planning record, not a production-readiness claim.

## Scope and decision record

This report set turns the current product evidence into an ordered delivery plan for branch-first lifecycle, recoverability, observability, and an agent-facing MCP surface. The decision is to build those capabilities through the existing public product contracts, not through Dashboard, database, or control-plane shortcuts.

Dashboard remains a full-stack external customer application. Its server uses typed `@terrascale/sdk` operations and its browser talks only to Dashboard-owned same-origin handlers. MCP is likewise an external typed-SDK client adapter. Neither may use MagicOnion, direct TerraBase, private routes, special headers, tenant bypasses, or control-plane credentials.

## Evidence index

| Area | Confirmed evidence | Report |
| --- | --- | --- |
| Product application | Platform, Authentication, Payments, Dashboard, onboarding, billing, backup, and monitoring code in `TerraScale.Internals/src` | [Internals](exploration-internals.md) |
| Public clients | `TerraScale.TypeScript/src/client.ts`; `TerraScale.DotNet/src/TerraScale.DotNet/TerraScaleClient.cs` | [Interfaces](exploration-interfaces.md) |
| Storage engine | periodic-backup, restore, and replication implementation under `TerraBase/src/TerraBase.Server` | [Engine](exploration-engine.md) |
| Control plane | `TerraScale.Orchestrator/docs/guides/production-readiness-audit-2026-08-04.md` and `README.md` | [Orchestrator](exploration-orchestrator.md) |
| Agent delivery | no product MCP source found in the reviewed product repositories | [MCP](exploration-mcp.md) |
| C# MCP delivery | dedicated read-only standard-stdio C# MCP server at `TerraScale.Mcp`, release source `17d4bfa`, tag `v0.1.0`; post-release README fixes `39539f5` and `6f50b7c` precisely identify installation artifacts | [Delivery record](implementation-csharp-mcp.md) |
| C# MCP review | final independent review after `17d4bfa`, including the README correction, is clean with no actionable issues; scope is MCP product and release artifacts, not total DBaaS readiness | [Final independent review](review-csharp-mcp-initial.md) |
| Security and reliability | production-readiness audit and reviewed Internals transport, rate-limit, audit, and hosting controls | [Security and reliability](exploration-security-reliability.md) |
| Market design | lifecycle and safety patterns synthesized for adoption | [Competitive patterns](exploration-competitive-patterns.md) |

Absence statements are bounded to the reviewed source and current public surfaces. They do not assert that a capability can never exist elsewhere.

## Dependency-ordered backlog

1. **Contract foundation**: define public branch, recovery-workspace, operation, audit, capability, and scoped-authorization contracts. Add TypeScript and .NET SDK parity rules before UI, CLI, or MCP work.
2. **Engine and lifecycle**: implement managed branch semantics above TerraBase, including immutable source point, TTL, quotas, cleanup, and restore-to-isolated-workspace. Do not present engine backups as managed branches.
3. **Production substrate**: qualify the real runtime, NATS, storage, TerraBase-admin, telemetry, and DR adapters needed to execute lifecycle operations safely.
4. **Product experience**: compose the new public contracts in Dashboard and CLI. Add deep tenant, project, database, branch, operation, and recovery observability.
5. **MCP**: ship read-first tools, resources, and prompts as a typed-SDK adapter; add mutations only with explicit confirmation, idempotency, audit, and capability checks.
6. **Reliability release**: rehearse point-in-time recovery and regional DR, publish evidence, then enable production lifecycle and mutation capabilities by policy.

## Production acceptance gates

Release is blocked until all applicable gates pass:

- Public REST and typed SDK contracts have conformance, authorization, tenant-isolation, and compatibility coverage.
- Branch and restore workflows are explicit, idempotent state machines with durable operation history and safe cancellation or compensation.
- Backup restore is proven in an isolated workspace; PITR and regional DR drills meet approved RPO/RTO targets with retained evidence.
- Orchestrator adapters are real-system qualified. Development RF=1 or pure-decision tests are not production evidence.
- Dashboard, CLI, API, and MCP expose the same authorized capability set without privileged paths.
- MCP mutations require reviewed confirmation, a stable idempotency key, scoped identity, and an immutable audit record.
