# Exploration: system readiness

## Position

The active goal is a production DBaaS for humans and AI, gated by evidence. This increment improves its delivery evidence only. It is not a production-ready claim.

## Findings

Audits found broad existing foundations across Platform, Dashboard, and MCP. The following gaps remain material:

- Production control-plane composition and real qualification.
- Physical branches and point-in-time recovery.
- Customer observability.
- OpenAPI and SDK contract debt.
- Raw payment payload retention.
- Incomplete Polar sandbox evidence.
- Dirty and behind Internals and Orchestrator checkouts that must not be overwritten.

## Competitive design guidance

Official Vercel, Turso, and Neon documentation was researched. Its patterns are design guidance only, not a claim that TerraScale implements them. The applicable guidance is:

- Keep public typed APIs separate from MCP adapters.
- Model operation state separately from readiness state.
- Treat branch and restore candidates as lineage-bearing operations with cutover and quota controls.
- Require human-reviewed agent operations.

## Polar handling boundary

No sandbox secret was persisted. No approved secret manager is available, and a valid sandbox run also needs separately supplied webhook, price, and configuration values. The application supports owner-private file references.
