---
title: Queue API
description: Project queue and topic APIs plus CLI and SDK helpers.
---

# Queue API

TerraScale Queue exposes project-scoped queues and topics under `/api/v1/projects/{projectId}/queues`. The C# and TypeScript SDKs both ship queue helpers (`client.Queues` / `client.queues`). The CLI registers matching command families.

## HTTP Routes

| Operation | Method and path |
| --- | --- |
| List or create | `GET` / `POST /api/v1/projects/{projectId}/queues` |
| Get or delete | `GET` / `DELETE /api/v1/projects/{projectId}/queues/{queueId}` |
| Publish | `POST /api/v1/projects/{projectId}/queues/{queueId}:publish` |
| Peek | `GET /api/v1/projects/{projectId}/queues/{queueId}:peek` |
| Purge | `POST /api/v1/projects/{projectId}/queues/{queueId}:purge` |
| Receive | `POST /api/v1/projects/{projectId}/queues/{queueId}:receive` |
| Complete | `POST /api/v1/projects/{projectId}/queues/{queueId}:complete` |
| Abandon | `POST /api/v1/projects/{projectId}/queues/{queueId}:abandon` |
| Dead-letter | `POST /api/v1/projects/{projectId}/queues/{queueId}:dead-letter` |
| Renew lock | `POST /api/v1/projects/{projectId}/queues/{queueId}:renew-lock` |

Los payloads de creación requieren `kind` con valor `queue` o `topic`. La recepción devuelve recibos regionales opacos; los métodos de confirmación requieren `{ receipt, region }`.

## CLI Command Family

```bash
terrascale queue list
terrascale queue create
terrascale queue delete
terrascale queue describe
terrascale queue send
terrascale queue receive
terrascale queue peek
terrascale queue purge
terrascale queue metrics
terrascale queue retry
terrascale queue dead-letter
terrascale queue replay
terrascale queue policy get
terrascale queue policy set
```

Related families include `topic`, `subscription`, and `consumer inspect`.

## SDK Helpers

### C#

```csharp
var queue = await client.Queues.CreateAsync(projectId, "jobs", TerraScaleQueueKinds.Queue);
await client.Queues.PublishAsync(projectId, queue.QueueId, new { task = "index" });
```

### TypeScript

```ts
const queue = await client.queues.create({ name: 'jobs', kind: 'queue' });
if (queue.ok) {
  await client.queues.publish(queue.value.queueId, { data: { task: 'index' } });
}
```

## Related Guides

- [TerraScale CLI](/guides/cli/)
- [C# SDK](/guides/sdks/csharp/)
- [TypeScript SDK](/guides/sdks/typescript/)
- [Batch operations](/reference/api/batch-operations/)
- [Transactional semantics](/reference/api/transactions/)
