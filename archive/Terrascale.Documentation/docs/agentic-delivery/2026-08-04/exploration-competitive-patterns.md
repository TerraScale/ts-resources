# Competitive-pattern exploration

This is a design-pattern comparison, not a feature-parity or vendor claim.

## Patterns to adopt

| Pattern | Product application |
| --- | --- |
| Branch-first lifecycle | Treat preview, test, recovery, and migration environments as named, policy-controlled lifecycle objects, not ad hoc copies. |
| Inspectable recovery workspace | Make restore targets isolated and visible before production impact, with source, target, expiry, validation, and promotion state. |
| Explicit operation state machines | Model queued, planned, running, waiting, succeeded, failed, cancelled, and compensated states durably. |
| Capability parity | Keep authorized operations consistent across API, SDK, CLI, Dashboard, and MCP. Interface convenience must not create a privilege tier. |
| Scoped authorization | Bind every read and mutation to tenant, project, resource, role, and time-bounded authorization; make scope visible in preflight. |

## Guardrails

These patterns only become a production differentiator when coupled to tested restore evidence, bounded blast radius, durable audit trails, idempotency, and transparent failure states. Do not market branch, PITR, DR, or orchestration capabilities before the corresponding acceptance gates in the README pass.
