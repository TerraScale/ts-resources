---
title: C# SDK
description: Guide to the TerraScale.DotNet SDK for public HTTP APIs.
sidebar:
  order: 1
  badge:
    text: New
    variant: tip
---

The current TerraScale C# SDK package is `TerraScale.DotNet`. Its public entry point is `TerraScaleClient` in the `TerraScale.DotNet` namespace. The package covers region catalog, database, collection, repository, document, TQL, schema, change-stream, billing, project, project database, environment, queue, usage, project auth API-key, machine-to-machine application, notification, backup, restore-point, and restore operations.

It does not include account sign-in helpers, user-profile helpers, organization-management helpers, auth-provider helpers, invitation helpers, audit helpers, admin helpers, or generated OpenAPI operation clients.

## Install

```bash
dotnet add package TerraScale.DotNet
```

## Configure

Use a caller-owned `HttpClient`:

```csharp
using TerraScale.DotNet;

var client = new TerraScaleClient(
    new HttpClient(),
    new TerraScaleClientOptions
    {
        BaseAddress = new Uri("https://api.terrascale.tech"),
        ProjectId = "01J2K7RTEQC3F4NG9HZ8Y62P6A",
        ApiKey = Environment.GetEnvironmentVariable("TERRASCALE_API_KEY")
    });
```

Or register the SDK with `IHttpClientFactory`:

```csharp
using TerraScale.DotNet;

builder.Services.AddTerraScaleClient(options =>
{
    options.BaseAddress = new Uri("https://api.terrascale.tech");
    options.ProjectId = builder.Configuration["TerraScale:ProjectId"];
    options.ApiKey = builder.Configuration["TerraScale:ApiKey"];
});
```

API-key authentication sends `X-TerraScale-Auth-Key` and `X-TerraScale-Project-Id`. Bearer authentication uses either `BearerToken` or `BearerTokenProvider` and sends `Authorization: Bearer ...`. Configure one authentication mode per client.

```csharp
var bearerClient = new TerraScaleClient(
    new HttpClient(),
    new TerraScaleClientOptions
    {
        BaseAddress = new Uri("https://api.terrascale.tech"),
        BearerTokenProvider = cancellationToken => new ValueTask<string>(
            tokenProvider.GetAccessToken(cancellationToken))
    });
```

## Client Families

`TerraScaleClient` exposes these public clients:

| Property | Purpose |
| --- | --- |
| `Databases` | List, create, get, and delete databases. |
| `Collections` | List database collections. |
| `Repositories` | List, create, get, and delete repositories. |
| `Documents` | Create, read, update, patch, delete, batch, and list repository documents. |
| `Tql` | Run TerraScale Query Language requests against repositories. |
| `Schemas` | Get, configure, and validate repository schemas. |
| `Changes` | Subscribe to repository and TQL server-sent event streams. |
| `Billing` | Read organization billing, invoices, checkout sessions, and portal sessions. |
| `Projects` | List, create, get, update, inspect region placements, and permanently delete projects in organizations. |
| `Regions` | List and get launch-region catalog entries (`GET /api/v1/regions`). |
| `ProjectDatabases` | List, create, get, and delete project-scoped logical databases. |
| `Queues` | Create, list, get, delete, publish, receive, peek, purge, and acknowledge project queues and topics. |
| `Environments` | List, create, get, and delete project database environments. |
| `ProjectUsage` | Read project usage summaries and workload time-series projections. |
| `ApiKeys` | List, create, rotate, and revoke project auth API keys. |
| `M2MApplications` | List, create, rotate, delete, and exchange project machine-to-machine applications for bearer tokens. |
| `Notifications` | List signed-in user notifications globally or by organization or project, and mark one or all read. |
| `Backups` | Configura políticas de backup; planeja, confirma explicitamente e executa backups sob demanda; lista pontos de restauração; e inicia restaurações lado a lado. |

`Repository<TEntity>(string repository)` creates a typed facade over the document and TQL clients. `ForDatabase(string databaseId)` and `ForEnvironment(string databaseId, string environmentId)` set default repository-creation scope.

## Idempotency

Opt in with `TerraScaleClientOptions.IdempotencyKeyFactory`. The SDK creates one key per logical mutation, reuses it across retries, and does not retry an unsafe mutation without a key. Keys must be nonblank and at most 128 characters. Replayable results expire after 24 hours; replays include `Idempotency-Replayed: true`, while reuse with different input returns `409 idempotency_key_reused`.

## Projects, Project Databases, and Environments

Use `Projects`, `ProjectDatabases`, and `Environments` for the project metadata API.

```csharp
var project = await client.Projects.CreateAsync(
    organizationId,
    "orders",
    defaultPermissionKeys: ["auth:login"],
    cancellationToken);

var database = await client.ProjectDatabases.CreateAsync(
    project.ProjectId,
    "orders-production",
    regions: ["gru"],
    cancellationToken);

var environment = await client.Environments.CreateAsync(
    project.ProjectId,
    database.DatabaseId,
    "Preview",
    kind: "Preview",
    cancellationToken);

var databases = await client.ProjectDatabases.ListAsync(project.ProjectId, cancellationToken: cancellationToken);
var environments = await client.Environments.ListAsync(project.ProjectId, database.DatabaseId, cancellationToken: cancellationToken);
```

These helpers call:

- `GET` and `POST /api/v1/organizations/{organizationId}/projects`
- `GET` and `PATCH /api/v1/projects/{projectId}`
- `GET /api/v1/projects/{projectId}/regions`
- `DELETE /api/v1/projects/{projectId}`
- `GET` and `POST /api/v1/projects/{projectId}/databases`
- `GET` and `DELETE /api/v1/projects/{projectId}/databases/{databaseId}`
- `GET` and `POST /api/v1/projects/{projectId}/databases/{databaseId}/environments`
- `GET` and `DELETE /api/v1/projects/{projectId}/databases/{databaseId}/environments/{environmentId}`

Tanto `Databases.DeleteAsync` quanto `ProjectDatabases.DeleteAsync` exigem `TerraScaleDeleteDatabaseOptions` cujo `Confirmation` corresponda exatamente ao `databaseId` de destino; o SDK o envia como `X-TerraScale-Delete-Confirmation`. `Databases` executa a exclusão física administrativa global, enquanto `ProjectDatabases` exclui um banco de dados lógico do projeto e exige autorização para esse projeto. Uma confirmação ausente ou diferente retorna `400 Bad Request`.

## Exclusão durável de ambientes

`Environments.DeleteAsync` é o caminho público tipado de exclusão. A API pública pode informar `Deleting` enquanto a limpeza está pendente. A conclusão requer que `Deleted` seja `true` e `Status` seja `"Completed"`; um `Status` ausente, `Deleted: false` ou `Status: "RetryScheduled"` não está concluído. Os campos anuláveis `OperationId`, `Status` e `RetryAt` fornecem o resultado da operação durável quando o serviço os retorna. Não substitua a chamada do SDK tipado por HTTP bruto, uma rota privada ou acesso direto a dados.

## Project Usage

```csharp
var usage = await client.ProjectUsage.GetAsync(projectId, cancellationToken);
var workload = await client.ProjectUsage.GetWorkloadAsync(
    projectId,
    range: "7d",
    cancellationToken);
```

These helpers call `GET /api/v1/projects/{projectId}/usage` and `GET /api/v1/projects/{projectId}/usage/workload`.

## Regions

```csharp
var regions = await client.Regions.ListAsync(cancellationToken);
var gru = await client.Regions.GetAsync("gru", cancellationToken);
```

These helpers call `GET /api/v1/regions` and `GET /api/v1/regions/{regionCode}`.

## Queues and Topics

Project queue helpers call `/api/v1/projects/{projectId}/queues`.

```csharp
var queue = await client.Queues.CreateAsync(
    projectId,
    "orders-jobs",
    TerraScaleQueueKinds.Queue,
    cancellationToken);

await client.Queues.PublishAsync(
    projectId,
    queue.QueueId,
    new { task = "index", orderId = "01J2K8AWQ2CT8QYV01T2CT8QYV" },
    cancellationToken);

var messages = await client.Queues.ReceiveAsync(
    projectId,
    queue.QueueId,
    new TerraScaleReceiveProjectQueueMessagesRequest(
        ConsumerName: "worker",
        MaxMessages: 10),
    cancellationToken);

foreach (var message in messages)
{
    await client.Queues.CompleteAsync(
        projectId,
        queue.QueueId,
        new TerraScaleProjectQueueReceipt(message.Receipt, message.Region),
        cancellationToken);
}
```

O tipo da fila é obrigatório. Use `TerraScaleQueueKinds.Topic` para tópicos publish/subscribe. As operações relacionadas incluem peek, purge, abandon, dead-letter e renew-lock.

## API Keys and M2M Applications

Project API-key helpers call `/api/v1/projects/{projectId}/auth/api-keys`.

```csharp
var createdKey = await client.ApiKeys.CreateAsync(
    projectId,
    new TerraScaleCreateApiKeyRequest
    {
        Name = "Orders worker",
        Scopes = ["documents:read", "documents:write"],
        DatabaseId = databaseId,
        EnvironmentId = environmentId
    },
    cancellationToken);

var keys = await client.ApiKeys.ListAsync(projectId, limit: 100, cancellationToken: cancellationToken);
var rotated = await client.ApiKeys.RotateAsync(projectId, createdKey.ApiKey.KeyId, cancellationToken);
var revoked = await client.ApiKeys.RevokeAsync(projectId, createdKey.ApiKey.KeyId, cancellationToken);
```

Project machine-to-machine helpers call `/api/v1/projects/{projectId}/auth/m2m-applications` and the anonymous token exchange route `/api/v1/projects/{projectId}/auth/m2m/token`.

```csharp
var app = await client.M2MApplications.CreateAsync(
    projectId,
    new TerraScaleCreateM2MApplicationRequest
    {
        Name = "Orders sync",
        Scopes = ["documents:read", "documents:write"],
        DatabaseId = databaseId,
        EnvironmentId = environmentId
    },
    cancellationToken);

var tokenBootstrapClient = new TerraScaleClient(
    new HttpClient(),
    new TerraScaleClientOptions
    {
        BaseAddress = new Uri("https://api.terrascale.tech")
    });

var token = await tokenBootstrapClient.M2MApplications.CreateTokenAsync(
    projectId,
    app.Application.ClientId,
    app.ClientSecret,
    scope: "documents:read documents:write",
    cancellationToken);
```

The same anonymous token exchange is available through `CreateTokenFormAsync` and `CreateTokenWithBasicCredentialsAsync`.

## Notifications

```csharp
var notifications = await client.Notifications.ListAsync(
    skip: 0,
    take: 50,
    unreadOnly: true,
    cancellationToken);

if (notifications.Count > 0)
{
    await client.Notifications.MarkReadAsync(notifications[0].NotificationId, cancellationToken);
}

await client.Notifications.MarkAllReadAsync(cancellationToken);
```

Notification helpers call `/api/v1/users/me/notifications`, `/api/v1/users/me/notifications/{notificationId}:mark-read`, and `/api/v1/users/me/notifications:mark-all-read`.

## Backups and Restores

`Backups` abrange políticas de backup de bancos de dados de projeto, backups sob demanda planejados e confirmados explicitamente antes de `ExecuteAsync`, pontos de restauração e restaurações lado a lado. As chamadas de restauração sempre criam um novo banco de dados lógico e o retornam como `RestoredDatabaseId`; o endpoint de restauração não sobrescreve o banco de dados de origem.

```csharp
var policy = await client.Backups.ConfigurePolicyAsync(
    projectId,
    databaseId,
    new TerraScaleConfigureBackupPolicyRequest(
        FullBackupCron: "0 3 * * *",
        IncrementalBackupCron: "0 */6 * * *",
        RetentionDays: 14),
    cancellationToken);

var operationSessionId = "backup-review-2026-07-05";
var plan = await client.Backups.PlanAsync(
    projectId,
    databaseId,
    new TerraScaleBackupConfirmationPlanRequest(operationSessionId),
    cancellationToken);

DisplayBackupPlanToHumanOrAgent(plan);
if (!await WaitForExplicitHumanConfirmationAsync(plan, cancellationToken))
{
    throw new OperationCanceledException("Backup was not confirmed.");
}

var execution = await client.Backups.ExecuteAsync(
    projectId,
    databaseId,
    new TerraScaleBackupConfirmationExecuteRequest(operationSessionId, plan.ConfirmationToken),
    idempotencyKey: "backup-execution-2026-07-05",
    cancellationToken);

var restorePoints = await client.Backups.ListRestorePointsAsync(projectId, databaseId, cancellationToken);

var restore = await client.Backups.StartRestoreAsync(
    projectId,
    databaseId,
    execution.Job.BackupId,
    idempotencyKey: "restore-orders-2026-07-05",
    cancellationToken);

Console.WriteLine(restore.RestoredDatabaseId);
```

`WaitForExplicitHumanConfirmationAsync` is application-owned and must not be automated. `ExecuteAsync` returns `.Job`, `.StatusCode`, and `.IdempotencyReplayed`; retry an uncertain execution with the same idempotency key and request. See [Backups and Restore](/guides/backups-restore/) for the full workflow and route-level semantics.

## Databases and Collections

```csharp
var database = await client.Databases.CreateAsync(
    name: "orders-production",
    replicationFactor: 1);

var databases = await client.Databases.ListAsync(skip: 0, take: 100);
var loaded = await client.Databases.GetAsync(database.DatabaseId);
var collections = await client.Collections.ListAsync(database.DatabaseId);
```

`CreateAsync` accepts optional settings as `IReadOnlyDictionary<string, string>`. Database list pagination uses `skip` and `take`.

## Repositories and Schemas

Repositories are created through the global `/api/v1/repositories` route. Use `DatabaseId` and `EnvironmentId` options, `ForDatabase`, `ForEnvironment`, or per-call arguments when a repository must target a database or environment.

```csharp
var scoped = client.ForEnvironment(database.DatabaseId, "01J2K7RTEQC3F4NG9HZ8Y62P6B");

var repository = await scoped.Repositories.CreateAsync(
    name: "orders",
    collection: "orders",
    schemaValidationEnabled: true,
    schema: """
    {
      "type": "object",
      "required": ["orderNumber", "status"],
      "properties": {
        "orderNumber": { "type": "string" },
        "status": { "type": "string" }
      }
    }
    """);

var schema = await client.Schemas.GetAsync(repository.RepositoryId);

await client.Schemas.ConfigureAsync(
    repository.RepositoryId,
    enabled: true,
    schema: schema.Schema);

var validation = await client.Schemas.ValidateAsync(repository.RepositoryId);
```

## Documents

Document requests wrap the application payload under `data`. SDK helpers do that wrapping for you.

```csharp
public sealed record OrderDocument(string OrderNumber, string Status);

var created = await client.Documents.CreateAsync(
    repository.RepositoryId,
    new OrderDocument("A1001", "new"));

var fetched = await client.Documents.GetAsync(repository.RepositoryId, created.Id);

var updated = await client.Documents.UpsertAsync(
    repository.RepositoryId,
    created.Id,
    new OrderDocument("A1001", "paid"));

var patched = await client.Documents.PatchAsync(
    repository.RepositoryId,
    created.Id,
    new { status = "refunded" });

var page = await client.Documents.ListAsync(repository.RepositoryId, skip: 0, take: 25);
```

Batch operations support `create`, `upsert`, `patch`, and `delete`.

```csharp
var batch = await client.Documents.BatchAsync(
    repository.RepositoryId,
    [
        TerraScaleDocumentBatchOperation.Create(new OrderDocument("A1002", "new")),
        TerraScaleDocumentBatchOperation.Patch(created.Id, new { status = "paid" })
    ]);
```

## Typed Repositories and TQL

The typed facade materializes document `data` as your model type and delegates queries to the TQL client.

```csharp
var orders = client.Repository<OrderDocument>(repository.RepositoryId);

var typed = await orders.CreateAsync(new OrderDocument("A1003", "new"));

var query = TerraScaleQuery
    .From("orders")
    .WhereEqual("status", "new")
    .OrderBy("orderNumber")
    .Take(25);

var matchingOrders = await orders.QueryAsync(query);
var rawPage = await client.Tql.QueryAsync(repository.RepositoryId, query);
```

Raw TQL requests call `POST /api/v1/repositories/{repositoryId}/tql`.

## Change Streams

`Changes` reads server-sent events from repository streams.

```csharp
await foreach (var change in client.Changes.SubscribeRepositoryAsync(repository.RepositoryId))
{
    Console.WriteLine($"{change.Type}: {change.Id}");
}
```

Use `SubscribeTqlAsync(repositoryId, query)` when the stream should be constrained by a TQL source query.

## Billing

Billing helpers call organization billing routes.

```csharp
var organizationId = "01J2K7RTEQC3F4NG9HZ8Y62P6A";

var checkout = await client.Billing.CreateCheckoutSessionAsync(
    organizationId,
    new TerraScaleCreateCheckoutSessionRequest(
        PriceId: "price_123",
        SuccessUrl: "https://app.example.test/billing/success",
        CancelUrl: "https://app.example.test/billing/cancelled"));

var account = await client.Billing.GetAccountAsync(organizationId);
var invoices = await client.Billing.ListInvoicesAsync(organizationId, skip: 0, take: 50);

var portal = await client.Billing.CreatePortalSessionAsync(
    organizationId,
    new TerraScaleCreateBillingPortalSessionRequest(
        ReturnUrl: "https://app.example.test/billing"));
```

## Validate

From the `TerraScale.DotNet` repository:

```bash
dotnet build TerraScale.DotNet.slnx --configuration Release --no-restore
dotnet test TerraScale.DotNet.slnx --configuration Release --no-progress
```
