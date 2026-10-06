---
title: Best Practices
description: Best practices for building applications with TerraScale.
sidebar:
  order: 11
---

Use this checklist when building against the current public `/api/v1` API, `@terrascale/sdk`, `TerraScale.DotNet`, and the TerraScale CLI.

## Data Modeling

### Use Repositories For Domain Documents

```csharp
public sealed record Customer(string Email, string Name, string Tier);

var customers = client.Repository<Customer>("01J2K7RTEQC3F4NG9HZ8Y62P6A");
await customers.UpsertAsync(
    "01J2K8AWQ2CT8QYV01T2CT8QYV",
    new Customer(
        Email: "team@example.com",
        Name: "Example Team",
        Tier: "premium"));
```

Repositories keep application data behind document, TQL, schema, and change-stream routes.

### Keep Document IDs Stable

Use ULID document IDs for deterministic retries.

```csharp
await customers.UpsertAsync(documentId, customer);
```

### Align Models With Schemas

Configure repository schemas when validation should be enforced:

```json
{
  "enabled": true,
  "schema": "{\"type\":\"object\",\"required\":[\"email\"],\"properties\":{\"email\":{\"type\":\"string\"}}}"
}
```

## Query Design

### Prefer TQL For Repository Reads

```csharp
var page = await customers.QueryAsync(
    TerraScaleQuery
        .From("customers")
        .WhereEqual("tier", "premium")
        .Take(50));
```

### Page Every List

Use `skip` and `take` where supported. Keep result windows explicit for user-facing reads.

```bash
curl "https://api.terrascale.tech/api/v1/repositories/01J2K7RTEQC3F4NG9HZ8Y62P6A/documents?skip=0&take=100" \
  -H "Authorization: Bearer $TERRASCALE_TOKEN"
```

## Reliability

### Treat Writes As Idempotent

Reuse the same document ID for retryable upserts. For background work, use queue idempotency keys or deterministic message identifiers in the queue workflow.

### Use Batch Operations For Independent Work

Batch independent document changes in one repository:

```csharp
await client.Documents.BatchAsync(
    "01J2K7RTEQC3F4NG9HZ8Y62P6A",
    [
        TerraScaleDocumentBatchOperation.Create(customer),
        TerraScaleDocumentBatchOperation.Patch(documentId, new { tier = "team" })
    ]);
```

### Keep Multi-Step Workflows Explicit

Dedicated multi-document transaction routes are not part of the current public API. If a workflow spans multiple records, model it as one aggregate document or use an application-level saga with clear states.

## Error Handling

### Preserve Error Context

The API error envelope includes `code`, `message`, optional `detail`, and optional `traceId`.

```csharp
try
{
    var loaded = await customers.GetAsync("01J2K8AWQ2CT8QYV01T2CT8QYV");
    return loaded.Data;
}
catch (TerraScaleApiException ex)
{
    logger.LogError(ex, "TerraScale request failed Status={StatusCode}", ex.StatusCode);
    throw;
}
```

### Retry Only Retryable Failures

Use backoff for rate limits, timeouts, and transient server failures. Do not blindly retry validation, authentication, authorization, or not-found errors.

## Security

- Store bearer tokens and API keys in secret storage.
- Use `X-TerraScale-Auth-Key` with `X-TerraScale-Project-Id` for project API-key authentication.
- Use bearer tokens for signed-in user flows.
- Keep direct storage access out of customer applications.

## Next Steps

- [API Overview](/reference/api/)
- [Authentication](/reference/authentication/)
- [C# SDK](/guides/sdks/csharp/)
- [TypeScript SDK](/guides/sdks/typescript/)
- [TerraScale CLI](/guides/cli/)
