# Competitive patterns with bounded reuse

Status: external design evidence reviewed on 2026-08-05. These are reusable patterns, not TerraScale feature claims.

| Pattern | Official evidence | Bounded TerraScale application |
| --- | --- | --- |
| Scoped MCP | [Vercel MCP](https://vercel.com/docs/agent-resources/vercel-mcp) uses OAuth and warns users to verify third-party marketplace installation sources; [Vercel CLI MCP](https://vercel.com/docs/cli/mcp) supports project-specific configuration. | Keep MCP bound to one configured project and public contracts. Do not infer that remote MCP or mutations are ready. |
| Managed recovery coverage | [Fly Managed Postgres](https://fly.io/docs/mpg/) explicitly includes automatic backups and recovery, high availability, and encrypted transport/storage. | Publish recovery coverage only after the corresponding TerraScale backup, restore, and DR evidence exists. |
| Disposable branch lifecycle | [Turso branching](https://docs.turso.tech/features/branching) creates a separate database, requires explicit cleanup, and counts it against quota; [Turso PITR](https://docs.turso.tech/features/point-in-time-recovery) restores into a new database and requires explicit application cutover. | If delivered, branches and restore candidates need expiration, lineage, validation, deliberate promotion/cutover, and deletion. No branch, clone, PITR, promotion, or merge capability is currently claimed. |
| Meter-to-invoice attribution | [Turso usage and billing](https://docs.turso.tech/help/usage-and-billing) identifies row reads, row writes, and storage as billable observations. | Attribute lifecycle and recovery resource consumption to a customer-visible meter before invoicing. Do not infer a billing model from competitor usage units. |
| Public idempotent provisioning and agent caution | [Neon branching](https://neon.com/docs/guides/branching-intro) documents branch lifecycle; [Neon MCP](https://neon.com/docs/ai/neon-mcp-server) advises reviewing and authorizing agent actions and limiting MCP to development/testing. | Expose provisioning through a bounded public, idempotent operation with audit and approval. Retain read-only MCP until the public mutation admission gates are met. |

These patterns reinforce, but do not replace, TerraScale's [MCP admission policy](../../../../TerraScale.Mcp/docs/design/mcp-mutation-admission.md) and [Orchestrator readiness audit](../../../../TerraScale.Orchestrator/docs/guides/production-readiness-audit-2026-08-04.md). Competitor documentation is not evidence of TerraScale delivery.

## Evidence provenance

The external links are official vendor documentation accessed on 2026-08-05; they are time-bound web observations rather than immutable TerraScale source evidence. The local MCP policy was read with `git show` from `TerraScale.Mcp` commit `480c77cd225720f7012a4e1d132a59d1dc36e90c`, `docs/design/mcp-mutation-admission.md`. The local readiness audit was read the same way from `TerraScale.Orchestrator` commit `85a162ca45258361ccdb303ce0d5b1047ce59f7e`, `docs/guides/production-readiness-audit-2026-08-04.md`.
