---
title: Backups and Restore
description: Configure TerraScale database backup policies, run on-demand backups, list restore points, and restore into a new database.
sidebar:
  order: 8
  badge:
    text: New
    variant: tip
---

TerraScale backup APIs are project database APIs. They live under `/api/v1/projects/{projectId}/databases/{databaseId}` and use logical ULID identifiers for backup jobs, restore jobs, and restored databases.

Restores are side-by-side. Starting a restore always materializes a new logical database identified by `restoredDatabaseId`. The source database identified by `databaseId` is never overwritten by the restore endpoint. Promotion is a separate application or operations step after you validate the restored database. The source-reviewed API and SDK surfaces do not expose a `promote` backup route or SDK helper.

## Backup Policy

A backup policy defines the schedule and retention for one project database.

```http
PUT /api/v1/projects/{projectId}/databases/{databaseId}/backups/policy
Authorization: Bearer <access-token>
Content-Type: application/json
```

```json
{
  "fullBackupCron": "0 3 * * *",
  "incrementalBackupCron": "0 */6 * * *",
  "retentionDays": 14,
  "disabled": false
}
```

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `fullBackupCron` | string | Yes | Cron expression for full backups. |
| `incrementalBackupCron` | string or null | No | Cron expression for incremental backups. |
| `retentionDays` | integer | No | Retention in days. The API accepts `0` through `3650`; `0` disables the TerraBase retention policy. |
| `disabled` | boolean | No | Disables the configured periodic task when `true`. |

The response is `BackupPolicyResponse`:

```json
{
  "backupPolicyId": "01J2K7RTEQC3F4NG9HZ8Y62P6P",
  "projectId": "01J2K7RTEQC3F4NG9HZ8Y62P6A",
  "databaseId": "01J2K7RTEQC3F4NG9HZ8Y62P6B",
  "databaseName": "orders-production",
  "fullBackupCron": "0 3 * * *",
  "incrementalBackupCron": "0 */6 * * *",
  "retentionDays": 14,
  "disabled": false,
  "destinationType": "LocalFolder",
  "status": "Configured",
  "createdAt": "2026-07-05T12:00:00Z",
  "updatedAt": "2026-07-05T12:00:00Z"
}
```

## On-Demand Backups

On-demand backups require an explicit two-step confirmation. The retired `POST .../backups` route no longer starts a backup. First plan the action:

```http
POST /api/v1/projects/{projectId}/databases/{databaseId}/backups:plan
Authorization: Bearer <access-token>
Content-Type: application/json
```

```json
{
  "operationSessionId": "backup-review-2026-07-05"
}
```

Planning returns `200 OK` with `action`, `projectId`, `databaseId`, `databaseName`, `requestDigest`, `confirmationToken`, and `expiresAt`. The confirmation is bound to the authenticated user, session, project/database target, and request digest, and expires after five minutes.

Present those plan details to a human or authorized agent and wait for explicit confirmation. Planning is read-only: it does not create a backup job. Never automatically execute a plan response.

```http
POST /api/v1/projects/{projectId}/databases/{databaseId}/backups:execute
Authorization: Bearer <access-token>
Idempotency-Key: backup-execution-2026-07-05
Content-Type: application/json
```

```json
{
  "operationSessionId": "backup-review-2026-07-05",
  "confirmationToken": "<confirmation-token-returned-by-plan>"
}
```

Execution requires `Idempotency-Key` and returns `202 Accepted` with `BackupJobResponse`. For a network-uncertain request, retry the unchanged request with the same key. A replay may include `Idempotency-Replayed: true`; reusing a key for a different request is rejected. When the confirmation expires or its user, session, target, or request changes, plan again and obtain a new explicit confirmation.

List and get backup jobs:

```http
GET /api/v1/projects/{projectId}/databases/{databaseId}/backups?skip=0&take=100
GET /api/v1/projects/{projectId}/databases/{databaseId}/backups/{backupId}
```

## Restore Points

Restore points are the backup artifacts visible to TerraScale for a project database.

```http
GET /api/v1/projects/{projectId}/databases/{databaseId}/restore-points
Authorization: Bearer <access-token>
```

```json
[
  {
    "name": "restore-point-20260705",
    "backupId": "01J2K7RTEQC3F4NG9HZ8Y62P6C",
    "createdAt": "2026-07-05T12:10:00Z",
    "isSnapshotRestore": false,
    "isEncrypted": true,
    "isIncremental": false,
    "filesToRestore": 4
  }
]
```

## Side-by-Side Restore

Start a restore from a backup job:

```http
POST /api/v1/projects/{projectId}/databases/{databaseId}/restores
Authorization: Bearer <access-token>
Content-Type: application/json
```

```json
{
  "backupId": "01J2K7RTEQC3F4NG9HZ8Y62P6C",
  "idempotencyKey": "restore-orders-2026-07-05"
}
```

The API returns `202 Accepted` with `RestoreJobResponse`. `databaseId` is the source database. `restoredDatabaseId` is the new database created by the restore.

```json
{
  "restoreId": "01J2K7RTEQC3F4NG9HZ8Y62P6R",
  "projectId": "01J2K7RTEQC3F4NG9HZ8Y62P6A",
  "databaseId": "01J2K7RTEQC3F4NG9HZ8Y62P6B",
  "backupId": "01J2K7RTEQC3F4NG9HZ8Y62P6C",
  "restoredDatabaseId": "01J2K7RTEQC3F4NG9HZ8Y62P6D",
  "restoredDatabaseName": "orders-production-restore-01j2k7rteq",
  "status": "Running",
  "requestedBy": "operator@example.com",
  "requestedAt": "2026-07-05T12:15:00Z",
  "updatedAt": "2026-07-05T12:15:01Z",
  "completedAt": null,
  "errorMessage": null
}
```

Track restore jobs:

```http
GET /api/v1/projects/{projectId}/databases/{databaseId}/restores?skip=0&take=100
GET /api/v1/projects/{projectId}/databases/{databaseId}/restores/{restoreId}
```

After the restore completes, validate the restored database by its `restoredDatabaseId`. Promote only after that validation by moving application traffic, credentials, configuration, or environment selection to the restored database through your normal deployment workflow. The restore endpoint itself does not mutate the original database.

## TypeScript SDK

The TypeScript SDK exposes backups through `client.backups`.

```ts
import { createTerraScaleClient, toUlid } from '@terrascale/sdk';

const client = createTerraScaleClient({
  apiBaseUrl: 'https://api.terrascale.tech',
  authBaseUrl: 'https://auth.terrascale.tech',
  projectId: toUlid('01J2K7RTEQC3F4NG9HZ8Y62P6A'),
  accessToken: async () => getAccessToken()
});

const databaseId = toUlid('01J2K7RTEQC3F4NG9HZ8Y62P6B');

const policy = await client.backups.configurePolicy(databaseId, {
  fullBackupCron: '0 3 * * *',
  incrementalBackupCron: '0 */6 * * *',
  retentionDays: 14,
  disabled: false
});

const operationSessionId = 'backup-review-2026-07-05';
const plan = await client.backups.planBackup(databaseId, { operationSessionId });
if (!plan.ok) throw new Error('Backup plan failed');

displayBackupPlanToHumanOrAgent(plan.value);
const humanConfirmed = await waitForExplicitHumanConfirmation(plan.value);
if (!humanConfirmed) return;

const execution = await client.backups.executeBackup(
  databaseId,
  { operationSessionId, confirmationToken: plan.value.confirmationToken },
  'backup-execution-2026-07-05'
);
if (!execution.ok) throw new Error('Backup execution failed');

const restorePoints = await client.backups.listRestorePoints(databaseId);
const restore = await client.backups.startRestore(databaseId, {
  backupId: execution.value.backupId,
  idempotencyKey: 'restore-orders-2026-07-05'
});

if (restore.ok) {
  console.log(restore.value.restoredDatabaseId);
}

const restores = await client.backups.listRestores(databaseId, { skip: 0, take: 25 });
```

`waitForExplicitHumanConfirmation` is application-owned. Do not replace it with an automatic execution step. The verified TypeScript method names are `configurePolicy`, `planBackup`, `executeBackup`, `listBackups`, `getBackup`, `listRestorePoints`, `startRestore`, `getRestore`, and `listRestores`. Retry an uncertain execution with the same idempotency key and request; a replay may be indicated by the `Idempotency-Replayed` response header.

## .NET SDK

The .NET SDK exposes backups through `TerraScaleClient.Backups`.

```csharp
using TerraScale.DotNet;

var policy = await client.Backups.ConfigurePolicyAsync(
    projectId,
    databaseId,
    new TerraScaleConfigureBackupPolicyRequest(
        FullBackupCron: "0 3 * * *",
        IncrementalBackupCron: "0 */6 * * *",
        RetentionDays: 14,
        Disabled: false),
    cancellationToken);

var operationSessionId = "backup-review-2026-07-05";
var plan = await client.Backups.PlanAsync(
    projectId,
    databaseId,
    new TerraScaleBackupConfirmationPlanRequest(operationSessionId),
    cancellationToken);

DisplayBackupPlanToHumanOrAgent(plan);
if (!await WaitForExplicitHumanConfirmationAsync(plan, cancellationToken)) return;

var execution = await client.Backups.ExecuteAsync(
    projectId,
    databaseId,
    new TerraScaleBackupConfirmationExecuteRequest(operationSessionId, plan.ConfirmationToken),
    idempotencyKey: "backup-execution-2026-07-05",
    cancellationToken);

var restorePoints = await client.Backups.ListRestorePointsAsync(
    projectId,
    databaseId,
    cancellationToken);

var restore = await client.Backups.StartRestoreAsync(
    projectId,
    databaseId,
    execution.Job.BackupId,
    idempotencyKey: "restore-orders-2026-07-05",
    cancellationToken);

Console.WriteLine(restore.RestoredDatabaseId);
```

`WaitForExplicitHumanConfirmationAsync` is application-owned and must not be automated. `ExecuteAsync` returns execution metadata: use `.Job` for the `BackupJobResponse` fields, `.StatusCode` for the HTTP status, and `.IdempotencyReplayed` to detect a replay. The verified .NET method names are `ConfigurePolicyAsync`, `PlanAsync`, `ExecuteAsync`, `ListAsync`, `GetAsync`, `ListRestorePointsAsync`, `StartRestoreAsync`, `ListRestoresAsync`, and `GetRestoreAsync`.

## Next Steps

- [Backups API Reference](/reference/api/backups/) - Route-level backup and restore details
- [C# SDK](/guides/sdks/csharp/) - .NET client families
- [TypeScript SDK](/guides/sdks/typescript/) - TypeScript client families
