# MCP recovery and operational read-scope review

## Decision

Approved as a fixed-configured-project, read-only scope for the public typed-SDK-only MCP adapter. This is an approval decision, not a claim that the approved tools, SDK methods, routes, or projections are implemented.

The MCP adapter remains an ordinary public client. It must use typed public SDK contracts only and must not access MagicOnion, direct TerraBase, NATS, private routes, privileged Dashboard behavior, or a generic request escape hatch.

## Approved capabilities

The adapter may expose only these read-only capabilities for its fixed configured project and identity:

- Environment list and get.
- Region placements.
- Project latency, without caller location coordinates.
- Organization usage derived from the configured project.
- Backups list and get.
- Restore points list.
- Restore jobs list and get.

IDs accepted by these capabilities must be bounded and validated before use. Recovery responses must be reviewed safe projections that omit `RequestedBy`, `ErrorMessage`, raw data, credentials, and provider response bodies.

## Explicit denials

This decision does not approve:

- Configuration, trigger, or restore mutations.
- Creating or deleting environments.
- Raw data access or TQL.
- Backup-policy claims, because no public SDK GET capability exists for them.
- Caller location coordinates.
- Direct billing account, invoice, checkout, or portal access. Billing URLs and metadata have not received a sensitivity review.
- Any mutation capability or generic request escape hatch.

## Required controls and evidence before implementation approval

Implementation must apply standard MCP safe error reduction, maintain fixed identity and project scope, and prove that each tool maps only to approved GET-only public routes. Tests must inventory tools, resources, and prompts so additions are intentional, and must verify the GET-only route set and the safe recovery projections.

Live tests are permitted only when nonsecret identifiers are injected. They must not require credentials, raw provider responses, customer data, or caller location coordinates in tool input or output.

The existing MCP and SDK parity exploration establishes the relevant constraints: MCP is a public typed-SDK adapter, mutations require separate authority and lifecycle evidence, and a generic request escape hatch is prohibited. The operational and recovery additions above are limited to safe read projections pending public SDK and route verification.

## Documentation claim guardrail

Do not claim that MCP returns a request ID unless an implementation exposes that value through a reviewed safe projection. README and related MCP claims must remain aligned with the actually implemented, safely exposed fields.
