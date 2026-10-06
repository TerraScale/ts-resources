# MCP mutation readiness

Status: current MCP is read-only. This is a readiness record, not a release claim for MCP mutations.

## Current boundary

The MCP server is a standard-stdio, configured-project adapter over the public typed .NET SDK. Except for the region catalog, its tools are rooted in `TERRASCALE_PROJECT_ID`; it exposes safe projections and a backup-plan handoff, but no execution tool. It excludes creates, deletes, restores, credentials, billing, administration, raw data, queues, and TQL. See the [MCP inventory and scope](../../../../TerraScale.Mcp/README.md) and the [read-service implementation](../../../../TerraScale.Mcp/src/TerraScale.Mcp/TerraScaleReadService.cs).

Dashboard can compose public SDK mutations that MCP cannot. That is a deliberate safety boundary, not a reason to give an agent a private route, direct storage, generic HTTP escape hatch, Dashboard route, or special header.

## Mutation admission gates

Do not add an MCP mutation until all of the following are delivered for the same capability:

1. A versioned public REST contract and matching typed SDK method, with published authorization, tenant isolation, bounded input, and sensitivity semantics.
2. A server-enforced `prepare` to `confirm` to `execute` protocol. The short-lived, single-use token must bind project, canonical payload hash, authenticated caller/session, and idempotency key.
3. A genuine non-agent-controlled approval authority, stable idempotency and retry behavior, and durable audit evidence without credentials or confirmation tokens.
4. Live public-contract success and expected-denial tests for scope and authorization, plus replay, expiry, altered-payload, and binding-mismatch coverage.

The governing [mutation-admission policy](../../../../TerraScale.Mcp/docs/design/mcp-mutation-admission.md) makes all current writes deny-by-default. The existing `plan_database_backup` precedent does not weaken that rule: it discards the execution-capable token and directs execution to an out-of-band approval surface.

## Decision

Keep MCP project-bound, SDK-only, and read-only. Human and agent parity is reached only capability by capability through the same public contract. It must never mean privileged control-plane parity.

## Evidence provenance

All local evidence below was read with `git show` from immutable trees, not from sibling working trees. The MCP assertions and admission requirements are from `TerraScale.Mcp` commit `480c77cd225720f7012a4e1d132a59d1dc36e90c`: `README.md`, `src/TerraScale.Mcp/TerraScaleReadService.cs`, and `docs/design/mcp-mutation-admission.md`. That tree pins its `TerraScale.DotNet` submodule to `0286964d559fff314ced3269357ee1c4f8d5546b`; its SDK project declares package version `0.1.0` and `TerraScaleBackupsClient.cs` has SHA-256 `2d6c40daddb40bad135c93969b531ef2264ed1a1892417eed4f04fde2c98f872`.

The referenced public Platform snapshot is `TerraScale.Internals` commit `5ba9722953871fc46384d48e52e8660612b93c34`, `docs/product/openapi/server.openapi.json`, SHA-256 `ee71b5998353a4a8559e3197e572c513e82a577bda60858514a4b532001a351a`. It is evidence for the current backup plan and execute contract only, not for an MCP mutation admission.
