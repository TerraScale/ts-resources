# Competitive-pattern exploration

Status: planning and evidence record, not production-ready. Sources were accessed on 2026-08-05; the conclusions below are design inferences, not claims of feature parity.

## External evidence

- [Vercel MCP](https://vercel.com/docs/agent-resources/vercel-mcp) documents remote OAuth, user-scoped access, and human confirmation.
- [Turso branching](https://docs.turso.tech/features/branching) and [point-in-time recovery](https://docs.turso.tech/features/point-in-time-recovery) describe branches and recovery as a new database that can be validated, cut over, and cleaned up.
- [Neon branching](https://neon.com/docs/guides/branching-intro) and its [restore-candidate changelog](https://neon.com/docs/changelog/2026-02-06) show lifecycle patterns alongside billing-aligned API and MCP delivery.
- [Polar sandbox](https://polar.sh/docs/integrate/sandbox) and [Polar MCP](https://polar.sh/docs/integrate/mcp) describe separately scoped sandbox user, organization, API, and MCP environments.

## Inferred delivery patterns

Adopt a shared public capability model across API, SDKs, Dashboard, CLI, and MCP. Require explicit agent authority and idempotent, observable lifecycle operations. Treat restore as a candidate followed by validation and explicit promotion. Apply TTL and cost guardrails to ephemeral lifecycle resources. Make billing customer-visible, and maintain a truly separate payment test environment.
