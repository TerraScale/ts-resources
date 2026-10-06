---
title: Public Alpha clients
description: API and client compatibility, qualification, and versioning policy.
sidebar:
  order: 4
---

TerraScale advertises a client only after it completes the same customer journey against the exact release candidate with the package bytes intended for publication. A source build or a test against another API revision does not qualify a client.

## Compatibility table

| Client | Supported runtime | Scope and current capability | Qualification state |
| --- | --- | --- | --- |
| API | HTTPS client using `/api/v1` | The caller's bearer or project-key authorization controls the requested Project | Pending exact release candidate evidence |
| .NET SDK | `TerraScale.DotNet` 0.1.0 on .NET 10 LTS | Typed public clients over the same `/api/v1` contract | Pending exact release candidate evidence |
| TypeScript SDK | `@terrascale/sdk` 0.2.0 on Node.js 22, Node.js 24, and current major browsers | Typed public clients over the same `/api/v1` contract | Pending exact release candidate evidence |
| MCP | `TerraScale.MCP` 0.1.0 on its bundled .NET 10 runtime | The configured `TERRASCALE_PROJECT_ID`, except the global `list_regions` read. Safe projections only. Document and export tools are not exposed. | Pending exact release candidate evidence |

Pending means the guide does not claim that the client passed launch qualification. Release evidence must replace that state with the API revision, client package SHA-256, client version, runtime, journey result, and observation time.

The Documentation OpenAPI snapshot currently records TerraScale.Internals revision `d807f69a5c8a096f912398a92f78a78533137d3a`. Synchronization alone is not release qualification.

## Shared customer journey

The API, .NET SDK, and TypeScript SDK candidate journey uses public authentication and `/api/v1` routes. It covers registration and verification, organization and Project setup, Database and Environment creation, Repository and Document work, TQL reads, selected-region placement, session consistency, usage display, plan selection, and export. MCP is not a full-journey client. Its current release only performs fixed-project read inspection and the global region read.

The target self-registration segment must begin with identity and email verification already counted as one completed step. It must then cover the first Organization, Project, and logical Database, payment-card verification for signup abuse control without a charge or subscription, and an explicit choice between no paid plan with no automatic renewal or Starter or Pro with monthly automatic renewal. An eligible paid Organization receives its first 30 days at no charge. Invited-user onboarding is qualified separately. This target is not yet part of the released journey and is tracked in [TerraScale.Internals issue 30](https://git.terrascale.tech/TerraScale/TerraScale.Internals/issues/30) and [TerraScale.TypeScript issue 6](https://git.terrascale.tech/TerraScale/TerraScale.TypeScript/issues/6).

The operation inventory compares the API contract, exported .NET methods, exported TypeScript methods, and the current MCP tool contract. A missing operation, an extra private operation, or a stale request shape fails qualification. Documentation never fills a client gap with an undocumented HTTP call, a Dashboard-only route, or privileged access.

## Launch operation inventory

The inventory is intentionally small and customer-scoped. It is the diff input used by release review:

| Customer operation | API contract | .NET SDK | TypeScript SDK | MCP |
| --- | --- | --- | --- | --- |
| Read launch regions | `GET /api/v1/regions` | `client.Regions.ListAsync()` | `client.regions.list()` | `list_regions` |
| Create and read repository documents | `/api/v1/repositories/{repositoryId}/documents` | typed repository/document client | typed repositories/documents client | not exposed in MCP 0.1.0 |
| Read project usage and latency evidence | documented `/api/v1` usage routes | `Usage` client | `usage` client | fixed-project usage and latency projections |
| Export a Project | published export contract | typed export operation when qualified | typed export operation when qualified | deferred, not exposed in MCP 0.1.0 |

The diff rejects an operation present only in a private or operator surface, a method or route absent from the current public contract, a stale request or response shape, and any undocumented raw-request escape hatch. MCP remains read-only at version 0.1.0. It has no mutation tools and no plan-to-execute bridge.

## Equivalent region-read example

The same public region catalog read has equivalent typed examples. The examples use fictional or environment-provided credentials and do not grant access.

API:

```bash
curl --fail-with-body 'https://api.terrascale.tech/api/v1/regions' \
  -H "Authorization: Bearer $TERRASCALE_TOKEN"
```

.NET SDK:

```csharp
var regions = await client.Regions.ListAsync(cancellationToken);
```

TypeScript SDK:

```ts
const regions = await client.regions.list();
```

MCP:

```json
{"name":"list_regions","arguments":{}}
```

MCP returns a bounded safe projection. It does not accept a project override for this call, and all other MCP tools use the configured project scope.

## MCP safety contract

MCP tools use the configured `TERRASCALE_PROJECT_ID` and the caller's authenticated public credential. The global `list_regions` read is the only exception. Tools do not receive operator authority, and their safe projections omit credentials, confirmation tokens, raw documents, raw errors, and diagnostic headers.

Read operations execute without confirmation when their fixed scope permits. `plan_database_backup` is a read-only handoff that discards any execution token. MCP has no execute tool, no mutation, and no automatic plan-to-execute bridge.

If a future public contract admits a mutation, an external approval authority must bind the configured project, canonical payload digest, authenticated caller, idempotency key, and expiry. The public server must consume the approval atomically and write a durable audit record containing the operation, result, project, actor, token outcome, idempotency key, and correlation ID. That is an admission requirement, not a current MCP capability.

## Versioning

A breaking public API change requires a new API version. TerraScale publishes migration guidance, gives at least six months notice before retiring the old version, and keeps supported SDK releases aligned during that notice period.

Client release notes identify the API versions supported by that client. Each published workflow records the client version, package digest, API version, API candidate revision, runtime, and test date used for its qualification.

## Release record

The current table remains pending because no decision-grade candidate run or package publication was authorized in this documentation change. The Orchestrator release record owns that evidence and may update this page only after admission passes.
