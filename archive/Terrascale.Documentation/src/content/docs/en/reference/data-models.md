---
title: Data Models
description: Current data structures used by the TerraScale SDKs and public API.
sidebar:
  order: 10
---

This page summarizes current response and request shapes from the API and SDK source. Public persistent resource IDs are ULIDs. Retired database-resource, entity-resource, entity-upsert, SQL-request, and C# queue-message SDK models are not part of the current public SDK/API shape.

## DatabaseSummary

Returned by `GET /api/v1/databases`.

```csharp
public sealed record TerraScaleDatabaseSummary(
    string DatabaseId,
    string Name);
```

API DTO shape:

```csharp
public sealed record DatabaseSummary(
    Ulid DatabaseId,
    string Name);
```

## DatabaseDetails

Returned by database create and get operations.

```csharp
public sealed record TerraScaleDatabaseDetails(
    string DatabaseId,
    string Name,
    bool Disabled,
    bool Encrypted,
    string State,
    string LockMode,
    int ReplicationFactor,
    IReadOnlyList<string> Members,
    IReadOnlyList<string> Promotables,
    IReadOnlyList<string> Rehabs,
    string? ChangeToken,
    IReadOnlyDictionary<string, string> Settings);
```

Create requests use a name, replication factor, and optional string settings:

```json
{
  "name": "orders-production",
  "replicationFactor": 1,
  "settings": {
    "key": "value"
  }
}
```

## CollectionSummary and DatabaseStatisticsSummary

`GET /api/v1/databases/{databaseId}/collections` returns collection names and document counts.

```csharp
public sealed record CollectionSummary(
    string Name,
    long Documents);
```

`GET /api/v1/databases/{databaseId}/statistics` returns database-level counts.

```csharp
public sealed record DatabaseStatisticsSummary(
    Ulid DatabaseId,
    long Documents,
    int Indexes,
    long RevisionDocuments,
    long Conflicts,
    long Tombstones,
    long Attachments,
    string? ChangeToken,
    string? LastDocumentToken,
    string? LastDatabaseToken);
```

## RepositorySummary

Returned by repository list, create, and get operations.

```csharp
public sealed record RepositorySummary(
    Ulid RepositoryId,
    string Name,
    Ulid DatabaseId,
    Ulid? EnvironmentId,
    string Collection,
    bool SchemaValidationEnabled,
    DateTimeOffset CreatedAt,
    DateTimeOffset UpdatedAt);
```

The `TerraScale.DotNet` model has the same fields with IDs exposed as strings:

```csharp
public sealed record TerraScaleRepository(
    string RepositoryId,
    string Name,
    string DatabaseId,
    string? EnvironmentId,
    string Collection,
    bool SchemaValidationEnabled,
    DateTimeOffset CreatedAt,
    DateTimeOffset UpdatedAt);
```

Create requests use:

```csharp
public sealed record CreateRepositoryRequest
{
    public string Name { get; init; }
    public Ulid? DatabaseId { get; init; }
    public Ulid? EnvironmentId { get; init; }
    public string? Collection { get; init; }
    public bool SchemaValidationEnabled { get; init; } = true;
    public string? Schema { get; init; }
}
```

## Repository Schema Models

`GET /api/v1/repositories/{repositoryId}/schema` and `PUT /api/v1/repositories/{repositoryId}/schema` return:

```csharp
public sealed record RepositorySchemaResponse(
    Ulid RepositoryId,
    string Repository,
    Ulid DatabaseId,
    Ulid? EnvironmentId,
    string Collection,
    bool Enabled,
    string Schema);
```

Configure requests use:

```csharp
public sealed record ConfigureRepositorySchemaRequest
{
    public bool Enabled { get; init; } = true;
    public string? Schema { get; init; }
}
```

Validate requests and responses use:

```csharp
public sealed record ValidateRepositorySchemaRequest
{
    public int? MaxErrorMessages { get; init; }
    public long? MaxDocumentsToValidate { get; init; }
}

public sealed record RepositorySchemaValidationResponse(
    Ulid RepositoryId,
    string Repository,
    Ulid DatabaseId,
    Ulid? EnvironmentId,
    string Collection,
    Ulid OperationId);
```

## DocumentResponse

Repository document routes wrap application data with repository metadata.

```csharp
public sealed record DocumentResponse(
    Ulid RepositoryId,
    string Repository,
    Ulid Id,
    JsonElement Data,
    DateTimeOffset? LastModified,
    string? ChangeToken);
```

Create, upsert, and patch requests use `data`:

```json
{
  "data": {
    "email": "team@example.com",
    "plan": "team"
  }
}
```

List and TQL responses use:

```csharp
public sealed record DocumentPageResponse(
    Ulid RepositoryId,
    string Repository,
    int Skip,
    int Take,
    long Total,
    IReadOnlyList<DocumentResponse> Items);
```

Delete responses use:

```csharp
public sealed record DeletedDocumentResponse(
    Ulid RepositoryId,
    string Repository,
    Ulid Id,
    bool Deleted);
```

## DocumentBatchRequest

Batch routes accept create, upsert, patch, and delete operations.

```csharp
public sealed record DocumentBatchRequest
{
    public IReadOnlyList<DocumentBatchOperationRequest>? Operations { get; init; }
}

public sealed record DocumentBatchOperationRequest
{
    public string Operation { get; init; }
    public Ulid? DocumentId { get; init; }
    public JsonElement Data { get; init; }
}
```

Responses include one result per operation:

```csharp
public sealed record DocumentBatchResponse(
    Ulid RepositoryId,
    string Repository,
    IReadOnlyList<DocumentBatchOperationResponse> Results);
```

## TqlQueryRequest

The current query route is TQL, not SQL:

```csharp
public sealed record TqlQueryRequest
{
    public string Query { get; init; }
    public int? Skip { get; init; }
    public int? Take { get; init; }
}
```

Example request:

```json
{
  "query": "from customers where email = 'team@example.com'",
  "skip": 0,
  "take": 25
}
```

## RepositoryDocumentChangeEvent

Repository and TQL event streams emit document change events:

```csharp
public sealed record RepositoryDocumentChangeEvent(
    Ulid RepositoryId,
    string Repository,
    string Collection,
    Ulid Id,
    string Type,
    string? ChangeToken,
    DateTimeOffset ObservedAt);
```

## ProjectDatabaseResponse

Project database routes under `/api/v1/projects/{projectId}/databases` return:

```csharp
public sealed record ProjectDatabaseResponse(
    Ulid DatabaseId,
    Ulid ProjectId,
    string Name,
    IReadOnlyList<string> Regions,
    DateTimeOffset CreatedAt,
    long Version);
```

The TypeScript SDK mirrors this area with `ProjectDatabase`, `DatabaseEnvironment`, `RepositoryDefinition`, `DocumentEnvelope<TDocument>`, `QueryRequest`, and `QueryResult` types.

## Billing Models

The C# SDK billing client exposes:

```csharp
public sealed record TerraScaleBillingAccount(
    string BillingAccountId,
    string OrganizationId,
    string PlanId,
    string Status);

public sealed record TerraScaleBillingInvoice(
    string InvoiceId,
    string BillingAccountId,
    long AmountCents,
    string Currency,
    string Status,
    DateTimeOffset IssuedAt,
    string? HostedInvoiceUrl = null,
    string? InvoicePdf = null);
```

Checkout and portal requests use:

```csharp
public sealed record TerraScaleCreateCheckoutSessionRequest(
    string? PriceId = null,
    string? SuccessUrl = null,
    string? CancelUrl = null,
    string? CustomerEmail = null,
    int? Quantity = null);

public sealed record TerraScaleCreateBillingPortalSessionRequest(
    string? ReturnUrl = null);
```

## Next Steps

- [C# SDK](/guides/sdks/csharp/) - Use `TerraScale.DotNet`
- [TypeScript SDK](/guides/sdks/typescript/) - Use `@terrascale/sdk`
- [Repository Management](/reference/management/repositories/) - Create and manage repositories
- [API Overview](/reference/api/) - Current route families
