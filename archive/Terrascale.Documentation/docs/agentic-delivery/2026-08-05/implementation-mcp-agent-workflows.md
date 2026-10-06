# MCP agent workflow documentation implementation

Date: 2026-08-05

## Delivered

- Added the English MCP Agent Workflows guide for the current `terrascale-mcp` v0.1.0 release.
- Documented verified stdio installation, checksum verification, fixed-project scope, credential handling, HTTPS and loopback development rule, read-only tools, resources, prompts, and safe recovery inspection.
- Corrected English TypeScript examples and SDK guidance to use typed client families. The public client does not expose a generic `request(...)` escape hatch.
- Added a missing-capability route that requests a reviewed typed public contract instead of bypassing the SDK or MCP boundary.

## Verified source boundaries

- `TerraScale.Mcp` uses only the public `TerraScale.DotNet` SDK and fixed `TERRASCALE_PROJECT_ID` scope.
- MCP recovery reads list or get backup jobs, list restore points, and list or get restore jobs through safe metadata projections only.
- No MCP write tool, backup-policy read, point-in-time recovery, direct TerraBase access, private RPC, credential persistence, or production certification claim is documented.

## Validation

Run `npm run check` and the static-site build after the documentation changes. Review the final diff and links before publishing.
