# Agentic delivery exploration

Date: 2026-08-05
Status: planning and evidence record. This work is **not production-ready**.

This set records the current delivery evidence for a safe public lifecycle and agent surface. Dashboard remains a full-stack external customer application: its server composes typed `@terrascale/sdk` calls, while browser code calls only Dashboard-owned same-origin handlers. MCP must be another public typed-SDK adapter, never a path to MagicOnion, direct TerraBase, NATS, or privileged Dashboard behavior.

## Evidence index

| Area | Record |
| --- | --- |
| Recovery and branching semantics | [Recovery and initial branch semantic contract](decision-recovery-branch-semantic-contract.md) |
| Control-plane execution | [Control-plane exploration](exploration-control-plane.md) |
| Dashboard and Platform | [Dashboard and Platform exploration](exploration-dashboard-platform.md) |
| Dashboard and AI-agent capability parity | [Dashboard and AI-agent capability parity exploration](exploration-dashboard-agent-capability-parity.md) |
| MCP and SDK parity | [MCP and SDK parity exploration](exploration-mcp-sdk-parity.md) |
| Billing and Polar | [Billing, security, and Polar exploration](exploration-billing-security-polar.md) |
| Market patterns | [Competitive-pattern exploration](exploration-competitive-patterns.md) |
| Orchestrator composition | [Orchestrator production composition audit](readiness-orchestrator-composition-audit.md) |

## Ordered delivery gates

1. Define public branch, lifecycle-operation, recovery-candidate, observability, capability, and audit contracts in Platform. Do not add a branch contract through Dashboard or MCP first.
2. Implement and prove TypeScript and .NET SDK parity for the contracts, including authorization, tenant isolation, compatibility, idempotency, and durable operation state.
3. Compose the public capabilities in Dashboard, with focused real-stack backup and recovery tests and customer-safe lifecycle health and database observability.
4. Qualify production control-plane actuators, identity, storage, recovery, GitOps trust, HA telemetry, and network boundaries before enabling automated production lifecycle execution.
5. Add safe MCP tools only after the public contracts exist: structured grammar, explicit confirmation, scoped authority, idempotency, and immutable audit evidence.
6. Decide fixed-only billing versus metered Polar export, then execute opt-in sandbox checkout, portal, subscription, webhook, reconciliation, and usage tests using separately injected owner-readable secrets.
7. Rehearse restore-candidate validation and promotion, cleanup, failure recovery, and DR against approved RPO/RTO targets. Publish retained evidence before declaring any production readiness.
