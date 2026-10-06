---
title: Rate Limits
description: Rate limits and retry guidance for TerraScale Platform API operations.
sidebar:
  order: 8
---

Rate limits protect the platform and keep performance predictable. Design clients to page results, batch independent work, and retry only transient failures.

## API Response

When rate limited, APIs return HTTP `429`. The C# SDK captures `Retry-After` as `TerraScaleApiException.RetryAfter` when the response includes it. The TypeScript SDK returns a `TerraScaleResult` failure with `kind: "rate-limit"`.

```json
{
  "code": "rate_limited",
  "message": "Rate limit exceeded.",
  "detail": null,
  "traceId": "00-..."
}
```

## Retry Pattern

```csharp
using TerraScale.DotNet;

async Task<T> ExecuteWithRetry<T>(Func<Task<T>> operation)
{
    var delay = TimeSpan.FromMilliseconds(200);

    for (var attempt = 0; attempt < 5; attempt++)
    {
        try
        {
            return await operation();
        }
        catch (TerraScaleApiException ex) when (
            ex.StatusCode is HttpStatusCode.TooManyRequests or
                HttpStatusCode.BadGateway or
                HttpStatusCode.ServiceUnavailable or
                HttpStatusCode.GatewayTimeout)
        {
            var wait = ex.RetryAfter ?? delay;
            await Task.Delay(wait + TimeSpan.FromMilliseconds(Random.Shared.Next(0, 100)));
            delay *= 2;
        }
    }

    return await operation();
}
```

Do not retry validation, authentication, authorization, not-found, or policy failures unless your application changes the request first.

## Batch Independent Work

Batch independent repository document changes to reduce request volume:

```csharp
await client.Documents.BatchAsync(
    "01J2K7RTEQC3F4NG9HZ8Y62P6A",
    [
        TerraScaleDocumentBatchOperation.Create(customer),
        TerraScaleDocumentBatchOperation.Patch(documentId, new { tier = "team" })
    ]);
```

Repository document batch route:

```http
POST /api/v1/repositories/{repositoryId}/documents/batch
```

Batching is not a transaction boundary. Keep all-or-nothing workflows in one aggregate document or model them as explicit workflow states.

## Control Concurrency

Throttle worker concurrency when a service can produce bursts:

```csharp
var semaphore = new SemaphoreSlim(100);

async Task<T> ExecuteWithThrottle<T>(Func<Task<T>> operation)
{
    await semaphore.WaitAsync();
    try
    {
        return await operation();
    }
    finally
    {
        semaphore.Release();
    }
}
```

Increase concurrency gradually and watch `429` responses, tail latency, and queue depth.

## Page Reads

Use explicit page sizes where endpoints support them.

```http
GET /api/v1/repositories/{repositoryId}/documents?skip=0&take=100
```

TQL accepts `skip` and `take` in the request body:

```json
{
  "query": "from customers where tier = 'team'",
  "skip": 0,
  "take": 100
}
```

## Monitoring

Track these signals:

- `429` response count by route
- Retry count and final failure count
- Queue depth and dead-letter count
- TQL page sizes
- Billing usage and quota guard failures

## Next Steps

- [Error Handling](/reference/error-handling/) - Error envelope and SDK exception handling
- [Document Batch Operations](/reference/api/batch-operations/) - Batch document route
- [Best Practices](/reference/best-practices/) - Application design checklist
