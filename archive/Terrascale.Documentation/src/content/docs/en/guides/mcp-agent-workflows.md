---
title: MCP Agent Workflows
description: Install the read-only TerraScale MCP server and use its typed public SDK workflows safely.
sidebar:
  order: 13
  badge:
    text: New
    variant: tip
---

`terrascale-mcp` is the current `v0.1.0` stdio MCP server for safe TerraScale discovery. It uses the public `TerraScale.DotNet` SDK and is read-only. It is not a privileged operator connection, and it cannot use TerraBase, private RPC, TQL, raw documents, queues, billing, credentials, or admin routes.

## Install and Configure

Download an approved platform bundle and its `checksums.json` from the authenticated TerraScale MCP `v0.1.0` release. Verify the bundle SHA-256 against that manifest before installing it. Bundles are not repository-signed at this time.

Configure the executable in your MCP client. Keep credentials in that client's local secret or environment configuration. Never put a credential in chat, a prompt, a tool argument, source control, or an agent log.

```toml
[mcp_servers.terrascale]
command = "/absolute/path/to/terrascale-mcp"
args = []

[mcp_servers.terrascale.env]
TERRASCALE_API_BASE_ADDRESS = "https://api.terrascale.tech"
TERRASCALE_PROJECT_ID = "your-project-id"
TERRASCALE_BEARER_TOKEN = "configure-in-local-secret-storage"
```

Set `TERRASCALE_API_BASE_ADDRESS` and `TERRASCALE_PROJECT_ID`, plus exactly one of `TERRASCALE_BEARER_TOKEN` or `TERRASCALE_API_KEY`. The server does not save either credential. It accepts HTTPS endpoints. HTTP is rejected except for a loopback development endpoint when `TERRASCALE_ALLOW_INSECURE_LOOPBACK_HTTP=true` is explicitly set.

## Scope and Safe Reads

Every tool except `list_regions` is limited to the configured project. Database, environment, backup, and restore identifiers are accepted only as children of that project. The server returns sanitized failures rather than API response bodies, messages, request IDs, headers, or credentials.

Use its tools to inspect the configured project, logical databases and environments, project and organization usage, region placements, and bounded workload or usage history. The available resources explain authentication, read-only mutation boundaries, operational scope, and recovery-read scope. The prompts `analyze-project-usage`, `review-operational-health`, and `review-backup-recovery-readiness` guide non-mutating analysis.

For backup and recovery readiness, agents can list or get backup jobs, list restore points, and list or get restore jobs. These are metadata-only safe projections. They omit requesters, error messages, provider data or URLs, raw data, and credentials. A backup policy cannot be inspected through MCP because the public SDK has no read capability for it.

## Mutations and Missing Capabilities

This MCP server cannot configure a backup policy, trigger a backup, start a restore, or make any other mutation. It does not provide point-in-time recovery. Use an approved public client and your reviewed operational process for a supported mutation.

Do not bypass the server with direct storage access, internal RPC, undocumented routes, or a generic SDK request helper. The public TypeScript and C# SDKs expose typed client families only. When a typed capability is missing, request it through [support](/about/support/) with the workflow, authorization scope, required input and output, sensitivity considerations, and whether it changes state. A future MCP mutation requires a published typed public contract, bounded input grammar, authorization semantics, response sensitivity review, real API coverage, and explicit approval and confirmation design.

## Agent Checklist

- Use HTTPS and configure one credential only in local secret storage.
- Keep the agent within `TERRASCALE_PROJECT_ID`; do not infer access to another project.
- Start with a resource or the matching prompt, then use only read tools needed for the question.
- Treat backup and restore results as inspection evidence, not authority to execute a recovery.
- Keep tool output and diagnostics out of tickets or chat when they could reveal customer metadata. Share only the minimum sanitized summary needed.
