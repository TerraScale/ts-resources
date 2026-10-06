---
title: Replication
description: Current TerraScale replication and region-placement scope.
---

TerraScale project database creation accepts a `regions` array. Selected regions use active-active asynchronous replication. The public contract does not promise a maximum replication delay or an uptime percentage.

## Current Placement Inputs

Project database creation:

```http
POST /api/v1/projects/{projectId}/databases
```

```json
{
  "name": "orders-production",
  "regions": ["gru"]
}
```

The TypeScript SDK region catalog currently exports `gru`, `sfo`, and `fra`.

## Replication Status

A successful write is a durable acknowledgement from the receiving selected region. Other selected regions apply it asynchronously. Concurrent writes use last-write-wins unless an optional conditional mutation rejects a stale version. Public Alpha has no majority write mode.

Global, preferred, failover, and strict regional endpoints all stay within the Database's selected regions. The global endpoint chooses the nearest healthy selected region using current routing observations. A preferred endpoint tries the named selected region first, a failover endpoint follows the configured selected-region order, and a strict endpoint returns unavailable instead of serving from another region. The routing layer never serves from an unselected region.

Adding a region reports catch-up progress and retries failed steps. Removing a region drains it before deleting the placement. Usage follows actual placement, including bytes stored during catch-up, not only the requested region list. See the [Public Alpha data contract](/guides/public-alpha-data-contract/) for session tokens, stale-read opt-in, and monitoring observation rules.

## See Also

- [Regions](/reference/regions/)
- [Getting Started](/guides/getting-started/)
- [API Overview](/reference/api/)
