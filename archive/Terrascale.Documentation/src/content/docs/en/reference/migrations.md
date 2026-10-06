---
title: Schema Evolution
description: Evolve TerraScale document models with schema operations instead of hand-written storage upgrade code.
---

TerraScale uses schema operations for ordinary model evolution. The SDKs submit typed model intent, the Server plans the schema diff, and TerraBase remains the typed document store behind the product boundary.

The common path is:

- infer or define a typed model in the TypeScript or C# SDK
- run a schema plan to see safety, affected fields, generated actions, and rewrite scope
- apply safe additive changes automatically in local and development environments
- require explicit approval for guarded production changes
- keep old and new stored shapes readable while background rewrites run
- inspect operation state, progress, failures, and schema versions through the API, SDK, and dashboard

This replaces the older pattern where application code owned routine storage upgrades. Users should not need to write mapping jobs, index jobs, or collection-management scripts for normal additive fields, defaults, indexes, or safe compatibility transforms.

## Current Model

Schema changes are represented as durable Server-owned operations. Each operation records the planned diff, safety class, target schema version, phase, progress, and any failure message. TerraScale stores those operation records in TerraBase and resumes recoverable work after restart unless the operation is explicitly paused.

Safe changes can complete immediately. Guarded changes move through staged phases such as expanding, backfilling, cutover, cleanup, and done. Failed operations can be retried from their persisted target schema version.

## Safe Changes

Safe changes are changes TerraScale can apply without user-authored storage upgrade code:

- add an optional field
- add a required field with a default
- add a generated index or access path
- widen a compatible field type
- add JSON/map query paths that auto-indexing has selected
- add a unique field after existing data passes duplicate validation

Use schema plan first when you want to inspect the exact operation before apply.

## Guarded Changes

Some changes need confirmation because TerraScale can preserve correctness only with an explicit operation:

- rename with an alias
- required field backfill
- index or access-path changes on large collections
- unique constraint reservation backfill
- compatibility transforms for old stored shapes

Production guarded changes require a `productionApprovalId` before apply.

## Blocked Changes

TerraScale rejects changes where it cannot infer safe intent:

- destructive field removal without a deliberate replacement plan
- ambiguous rename without an alias
- type narrowing that can lose data
- document identity or placement changes that need a product decision
- semantic rewrites that require business logic

For those cases, use a staged data rewrite designed as application or operations work. Keep it idempotent, observable, tenant-scoped, and tested against representative data before applying it to live records.

## Operation Observability

Track schema evolution through operation history and versions:

- current and target schema version
- safety class and generated storage actions
- affected collection and fields
- progress percentage and phase
- failure message and retry/resume guidance
- audit and request correlation IDs

## Best Practices

1. Treat SDK model definitions as the source of schema intent.
2. Use schema plan output in review and deployment workflows.
3. Prefer additive changes and defaults before destructive cleanup.
4. Keep compatibility reads enabled until background rewrites finish.
5. Use typed unique fields only when duplicate validation and reservation backfill can succeed.
6. Reserve manual data rewrites for destructive or semantic changes TerraScale cannot infer.

## Related

- [Validation](/reference/validation/)
- [Data Models](/reference/data-models/)
- [Best Practices](/reference/best-practices/)
- [TQL API](/reference/api/tql/)
