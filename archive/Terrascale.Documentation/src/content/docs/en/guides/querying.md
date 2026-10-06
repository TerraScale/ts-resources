---
title: Querying
description: How current TerraScale repository querying works.
sidebar:
  order: 9
---

TerraScale currently documents repository querying through TerraScale Query Language (TQL).

## TQL

TQL queries run against a repository:

```http
POST /api/v1/repositories/{repositoryId}/tql
```

```json
{
  "query": "from customers where plan = 'pro'",
  "skip": 0,
  "take": 10
}
```

The response is a document page with `repositoryId`, `repository`, `skip`, `take`, `total`, and `items`.

## C# Query Builder

```csharp
using TerraScale.DotNet;

var page = await client.Tql.QueryAsync(
    "01J2K7RTEQC3F4NG9HZ8Y62P6A",
    TerraScaleQuery
        .From("customers")
        .WhereEqual("plan", "pro")
        .OrderBy("email")
        .Take(10));
```

`TerraScaleQuery` supports equality, inequality, range comparisons, `in`, ordering, `skip`, and `take`.

## TypeScript SDK

```ts
const page = await client.query.execute(
  { repositoryId: toUlid('01J2K7RTEQC3F4NG9HZ8Y62P6A') },
  {
    query: "from customers where plan = 'pro'",
    take: 10
  },
);
```

## Query Status

Use TQL for current product queries. There is no separate public SQL or Mongo query route family.

## Next Steps

- [TQL API reference](/reference/api/tql/)
- [Repository guide](/guides/repository/)
- [Rate limits](/reference/rate-limits/)
