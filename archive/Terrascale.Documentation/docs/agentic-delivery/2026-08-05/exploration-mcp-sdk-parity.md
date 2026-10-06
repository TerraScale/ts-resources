# MCP and SDK parity exploration

Status: planning and evidence record, not production-ready.

## Current public-client evidence

The C# standard-stdio MCP v0.1 has 12 read tools, 2 resources, and 2 prompts. It intentionally excludes mutations, billing, credentials, administration, and backups. Both typed SDKs support database and environment create, list, get, and delete plus backup and restore APIs. Neither SDK has a branch contract. TypeScript's public scope includes authentication, organization, audit, and administration; the .NET SDK intentionally forbids those areas.

## Delivery sequence

Define the Platform contract first, then add matching capabilities to both SDKs. Only then add narrowly safe MCP tools. Each mutation needs a structured grammar, caller-scoped authorization, explicit confirmation after preflight, stable idempotency, and immutable audit evidence. Do not add a generic request escape hatch.

## Acceptance evidence

Conformance tests must prove equivalent authorized behavior across API, both SDKs, Dashboard composition, and MCP. Read output must redact secrets and internal topology; mutations must expose durable public operation state and be safe to retry.
