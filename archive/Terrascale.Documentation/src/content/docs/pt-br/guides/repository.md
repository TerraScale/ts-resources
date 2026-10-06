---
title: Repository Pattern Guide
description: Store and query repository documents with current TerraScale Platform APIs and SDKs.
sidebar:
  order: 3
---

Repositories are the current public data boundary for application documents. A repository maps to a TerraBase collection and exposes document CRUD, batch, TQL, schema, and change-stream routes.

## Before You Start

Make sure you have:

- A bearer token or project API key
- A database ID
- A repository ID from `POST /api/v1/repositories`
- `TerraScale.DotNet` for C# or `@terrascale/sdk` for TypeScript

## Repository Routes

| Operation | Route |
| --- | --- |
| Create repository | `POST /api/v1/repositories` |
| List repositories | `GET /api/v1/repositories` |
| Get repository | `GET /api/v1/repositories/{repositoryId}` |
| Delete repository | `DELETE /api/v1/repositories/{repositoryId}` |
| Create document | `POST /api/v1/repositories/{repositoryId}/documents` |
| Upsert document | `PUT /api/v1/repositories/{repositoryId}/documents/{documentId}` |
| Query with TQL | `POST /api/v1/repositories/{repositoryId}/tql` |

## Define A Model

Repository payloads are plain JSON objects. Public document IDs are ULIDs.

```csharp
public sealed record Customer(
    string Email,
    string Name,
    string Tier,
    IReadOnlyList<string> Tags);
```

```ts
type Customer = {
  email: string;
  name: string;
  tier: 'standard' | 'premium' | 'enterprise';
  tags: string[];
};
```

## Use C#

```csharp
using TerraScale.DotNet;

var customers = client.Repository<Customer>("01J2K7RTEQC3F4NG9HZ8Y62P6A");

var saved = await customers.UpsertAsync(
    "01J2K8AWQ2CT8QYV01T2CT8QYV",
    new Customer(
        Email: "team@example.com",
        Name: "Example Team",
        Tier: "premium",
        Tags: ["priority", "b2b"]));

var loaded = await customers.GetAsync(saved.Id);

var page = await customers.QueryAsync(
    TerraScaleQuery
        .From("customers")
        .WhereEqual("tier", "premium")
        .Take(50));
```

## Use TypeScript

Use os clientes tipados `documents` e `query`. `@terrascale/sdk` não expõe um auxiliar de solicitação genérico.

```ts
import { toUlid } from '@terrascale/sdk';

const repository = { repositoryId: toUlid('01J2K7RTEQC3F4NG9HZ8Y62P6A') };
const documentId = toUlid('01J2K8AWQ2CT8QYV01T2CT8QYV');

const saved = await client.documents.put(repository, documentId, {
  email: 'team@example.com',
  name: 'Example Team',
  tier: 'premium',
  tags: ['priority', 'b2b']
});

const page = await client.query.execute(repository, {
    query: "from customers where tier = 'premium'",
    take: 50
});
```

## Schema Validation

Repository schemas are configured through:

```text
GET /api/v1/repositories/{repositoryId}/schema
PUT /api/v1/repositories/{repositoryId}/schema
POST /api/v1/repositories/{repositoryId}/schema/validate
```

The configure request uses `enabled` and a JSON schema string:

```json
{
  "enabled": true,
  "schema": "{\"type\":\"object\",\"required\":[\"email\"],\"properties\":{\"email\":{\"type\":\"string\"}}}"
}
```

## Change Streams

Use repository event routes or the C# `Changes` client for server-sent events:

```csharp
await foreach (var change in client.Changes.SubscribeRepositoryAsync("01J2K7RTEQC3F4NG9HZ8Y62P6A"))
{
    Console.WriteLine($"{change.Type}: {change.Id}");
}
```

## Next Steps

- [Repository Management API](/reference/management/repositories/)
- [Document Operations](/reference/api/item-operations/)
- [TQL Query API](/reference/api/tql/)
- [C# SDK](/guides/sdks/csharp/)
- [TypeScript SDK](/guides/sdks/typescript/)
