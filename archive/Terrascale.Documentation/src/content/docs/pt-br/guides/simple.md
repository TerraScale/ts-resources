---
title: Simple usage guide
description: Create a database, write a document, and query it with TerraScale.
sidebar:
  order: 2
---

This guide walks through the current public API path for a small application: create a database, create a repository, write a document, and query it with TQL.

## What You Need

- A TerraScale account
- A bearer token or project API key
- A project ID when using project API-key authentication
- The [API overview](/reference/api/) and [authentication guide](/reference/authentication/)

## Create A Database

```bash
curl -X POST "https://api.terrascale.tech/api/v1/databases" \
  -H "Authorization: Bearer $TERRASCALE_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-first-db",
    "replicationFactor": 1
  }'
```

## Create A Repository

```bash
curl -X POST "https://api.terrascale.tech/api/v1/repositories" \
  -H "Authorization: Bearer $TERRASCALE_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "customers",
    "databaseId": "01J2K7RTEQC3F4NG9HZ8Y62P6A",
    "collection": "customers",
    "schemaValidationEnabled": true
  }'
```

## Store A Document

```bash
curl -X POST "https://api.terrascale.tech/api/v1/repositories/01J2K7RTEQC3F4NG9HZ8Y62P6B/documents" \
  -H "Authorization: Bearer $TERRASCALE_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "data": {
      "email": "ava@example.com",
      "name": "Ava Chen",
      "plan": "starter"
    }
  }'
```

## Query Data

```bash
curl -X POST "https://api.terrascale.tech/api/v1/repositories/01J2K7RTEQC3F4NG9HZ8Y62P6B/tql" \
  -H "Authorization: Bearer $TERRASCALE_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "from customers where email = '\''ava@example.com'\''",
    "take": 10
  }'
```

## Use C#

```csharp
using TerraScale.DotNet;

public sealed record Customer(string Email, string Name, string Plan);

var customers = client.Repository<Customer>("01J2K7RTEQC3F4NG9HZ8Y62P6B");

await customers.CreateAsync(new Customer(
    Email: "ava@example.com",
    Name: "Ava Chen",
    Plan: "starter"));

var page = await customers.QueryAsync(
    TerraScaleQuery
        .From("customers")
        .WhereEqual("email", "ava@example.com")
        .Take(10));
```

## Use TypeScript

```ts
import { toUlid } from '@terrascale/sdk';

const page = await client.query.execute(
  { repositoryId: toUlid('01J2K7RTEQC3F4NG9HZ8Y62P6B') },
  {
    query: "from customers where email = 'ava@example.com'",
    take: 10
  },
);
```

## Next Steps

- [Getting started](/guides/getting-started/)
- [TypeScript SDK guide](/guides/sdks/typescript/)
- [C# SDK guide](/guides/sdks/csharp/)
- [Repository guide](/guides/repository/)
- [TQL API reference](/reference/api/tql/)
