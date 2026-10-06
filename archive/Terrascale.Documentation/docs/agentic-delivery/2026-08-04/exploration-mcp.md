# MCP exploration

## Current state

No product MCP implementation was found in the reviewed Internals, TypeScript SDK, .NET SDK, TerraBase, or Orchestrator source. This is a product gap, not permission to couple an agent directly to private services.

## Chosen architecture

Implement MCP as an external adapter over the normal typed public SDK. It receives the caller's scoped public identity and invokes the same versioned REST contracts as Dashboard, CLI, and customer applications. It has no MagicOnion, NATS, direct TerraBase, control-plane, Dashboard-private, or special-header path.

Start with read-first tools and resources: capability discovery, project and database inventory, health and operation status, branch lineage, backup catalog, recovery-workspace status, audit history, and guided incident prompts. Prompts are advisory and must make their required scope and destructive implications clear.

## Mutation policy

Mutations require a preflight that returns scope, affected resources, risk, cost or retention effect when available, idempotency key, and confirmation token. The final call must record the actor, tool, approved parameters, correlation identifier, public operation identifier, and outcome. Destructive or irreversible operations need explicit user confirmation after preflight; no natural-language inference substitutes for it.

## Acceptance criteria

- Tool authorization equals API authorization for the same identity and tenant.
- Read resources redact secrets and internal topology.
- Mutations are idempotent and replay-safe, with durable public operation states.
- SDK/API/MCP conformance tests prove no privileged MCP route exists.
