---
title: TypeScript SDK
description: Guide for the @terrascale/sdk package.
sidebar:
  order: 12
  badge:
    text: New
    variant: tip
---

## TypeScript SDK

The current TerraScale TypeScript package is `@terrascale/sdk`. Its public factory is `createTerraScaleClient(config)`. The SDK uses versioned JSON HTTP routes and sends bearer credentials through its transport.

The package does not expose an `apiKey` client option and does not publish the previous client package name.

## Install

```bash
npm install @terrascale/sdk
```

## Create a Client

```ts
import { createTerraScaleClient, toUlid } from '@terrascale/sdk';

const client = createTerraScaleClient({
  apiBaseUrl: 'https://api.terrascale.tech',
  authBaseUrl: 'https://auth.terrascale.tech',
  projectId: toUlid('01J2K7RTEQC3F4NG9HZ8Y62P6A'),
  accessToken: async () => getAccessToken()
});
```

`TerraScaleRuntimeConfig` requires `apiBaseUrl`. It also accepts `authBaseUrl`, `projectId`, `accessToken`, `defaultHeaders`, a custom `fetch`, request metrics, and an idempotency-key factory.

`accessToken` may be a string or a function that returns a token. The transport sends it as `Authorization: Bearer ...`, sets `accept: application/json`, and forwards `x-terrascale-project-id` when `projectId` is configured. There is no Dashboard-only header or tenant bypass.

## Public Client Families

`createTerraScaleClient` returns these public families:

| Family | Purpose |
| --- | --- |
| `auth` | Session, passwordless email sign-in links, email verification, refresh, logout, and account-session calls. |
| `onboarding` | Account information, MFA choice, payment validation, and initial organization and project setup. |
| `organizations` | Organization, membership, invitation, project, deletion, and region-placement lifecycle calls. |
| `regions` | Launch-region catalog list and get calls (`GET /api/v1/regions`). |
| `databases` | Project database and database-environment list, create, get, and delete calls. |
| `queues` | Project queue and topic lifecycle, publish, peek, purge, receive, and acknowledgement calls. |
| `repositories` | Repository definition list, create, get, and delete calls. |
| `backups` | Project database backup policy, backup job, restore-point, and restore calls. |
| `documents` | Repository document list, create, get, put, patch, batch, and delete calls. |
| `query` | TQL execution calls for repository data. |
| `schema` | Repository schema get, validate, and configure calls. |
| `apiKeys` | Project auth API-key list, create, rotate, and revoke calls. |
| `m2m` | Project auth machine-to-machine application list, create, rotate, revoke, and token calls. |
| `access` | Team-member access calls. |
| `usage` | Project totals, workload, latency, and history plus organization totals. |
| `billing` | Organization billing account, invoice, checkout, and portal-session calls. |
| `pricing` | Public pricing-plan catalog calls. |
| `audit` | Project audit-event reads. |
| `notifications` | Signed-in user notification inbox reads and mark-read mutations. |
| `security` | Project security-settings get and update calls. |

The public client exposes `config` and its typed client families. It does not expose a generic `request(...)` escape hatch. Dashboard code uses only typed client methods and owns Dashboard-specific endpoint composition in its full-stack project. The SDK has no Dashboard-specific client, DTO, route, identifier, or database helper.

If a public operation is missing, do not construct an undocumented route or work around the SDK boundary. Request a typed public capability through [support](/about/support/) with the use case, required authorization scope, request and response shape, and whether the operation reads or mutates state.

## Onboarding Contract Status

The client-family table describes the currently released typed surface. The target self-registration flow will open with identity and email verification already counted as one completed step, then cover the first Organization, Project, and logical Database plus payment-card verification for signup abuse control. It will let the User explicitly continue with no paid plan and no automatic renewal, retaining the Developer allowance, or select Starter or Pro with monthly automatic renewal and an eligible first 30 days at no charge. Invited-user onboarding remains separate.

This target is tracked in [TerraScale.TypeScript issue 6](https://git.terrascale.tech/TerraScale/TerraScale.TypeScript/issues/6) and [TerraScale.Internals issue 30](https://git.terrascale.tech/TerraScale/TerraScale.Internals/issues/30). Until both contracts ship, do not present the full flow as released or construct undocumented routes to simulate it.

Public clients opt in to mutation idempotency with `idempotencyKeyFactory` on the client or `idempotencyKey` on an individual request. Set the request value to `false` to opt out of global generation.

## Database Deletion Confirmation

`client.databases.delete(databaseId, { confirm: true })` explicitly acknowledges deletion and sends `X-TerraScale-Delete-Confirmation` with that exact database ULID. It deletes the project-scoped logical database selected by the client project. The global physical-admin `DELETE /api/v1/databases/{databaseId}` route also requires the same header and appropriate administrator authorization. Missing or mismatched confirmation returns `400 Bad Request`.

## Durable Environment Deletion

Use the typed environment delete method and inspect both completion fields. Completion requires `deleted: true` and `status: 'Completed'`; an absent `status` is not completion. `deleted: false` or `status: 'RetryScheduled'` is pending; retain `operationId` for correlation and do not act before `retryAt`. Environment reads can show `Deleting` during that period. There is no public operation-status route and no generic request escape hatch, so do not work around the typed client with a private route or direct data access.

```ts
const deletion = await client.databases.deleteEnvironment(databaseId, environmentId);
if (!deletion.ok) throw new Error('Environment deletion request failed');

if (deletion.value.deleted && deletion.value.status === 'Completed') {
  console.log('Environment deletion completed');
} else if (deletion.value.status === 'RetryScheduled') {
  console.log(deletion.value.operationId, deletion.value.retryAt);
}
```

## Authentication Calls

The SDK exposes passwordless email sign-in: request a sign-in link, then complete the sign-in after opening it. This helper surface does not mean the ADR-0041 account migration is complete; the current published API still retains legacy account credential routes.

```ts
await client.auth.requestMagicLink({
  email: 'team@example.com',
  loginUrl: 'https://app.example.test/login'
});

const session = await client.auth.getSession();
const refreshed = await client.auth.refresh('refresh-token');
await client.auth.signOut();
```

The auth client calls routes such as `/api/v1/auth/passwordless/magic-link`, `/api/v1/auth/me`, `/api/v1/auth/refresh`, and `/api/v1/auth/logout`. Project auth routes are under `/api/v1/projects/{projectId}/auth/...`.

## Repository Data Routes

The current API source exposes global repository routes for document and TQL operations:

| Operation | Route |
| --- | --- |
| Create document | `POST /api/v1/repositories/{repositoryId}/documents` |
| List documents | `GET /api/v1/repositories/{repositoryId}/documents` |
| Get document | `GET /api/v1/repositories/{repositoryId}/documents/{documentId}` |
| Upsert document | `PUT /api/v1/repositories/{repositoryId}/documents/{documentId}` |
| Patch document | `PATCH /api/v1/repositories/{repositoryId}/documents/{documentId}` |
| Delete document | `DELETE /api/v1/repositories/{repositoryId}/documents/{documentId}` |
| Batch documents | `POST /api/v1/repositories/{repositoryId}/documents/batch` |
| Query with TQL | `POST /api/v1/repositories/{repositoryId}/tql` |
| Repository events | `GET /api/v1/repositories/{repositoryId}/events` |
| TQL events | `GET /api/v1/repositories/{repositoryId}/tql/events` |

## Regions and Queues

```ts
const regions = await client.regions.list();
const gru = await client.regions.get('gru');

const queue = await client.queues.create({ name: 'orders-jobs', kind: 'queue' });
if (queue.ok) {
  await client.queues.publish(queue.value.queueId, { data: { task: 'index' } });
  const received = await client.queues.receive(queue.value.queueId, {
    consumerName: 'worker',
    maxMessages: 10
  });
  if (received.ok) {
    for (const message of received.value) {
      await client.queues.complete(queue.value.queueId, {
        receipt: message.receipt,
        region: message.region
      });
    }
  }
}
```

Queue routes live under `/api/v1/projects/{projectId}/queues`. Create topics with `kind: 'topic'`. Received messages carry an opaque regional receipt; pass `{ receipt, region }` back to complete, abandon, dead-letter, and renew-lock.

## Project Credential Routes

The API route families for project credentials are:

| Credential | Routes |
| --- | --- |
| API keys | `GET /api/v1/projects/{projectId}/auth/api-keys`, `POST /api/v1/projects/{projectId}/auth/api-keys`, `DELETE /api/v1/projects/{projectId}/auth/api-keys/{keyId}`, `POST /api/v1/projects/{projectId}/auth/api-keys/{keyId}/rotate` |
| Machine-to-machine applications | `GET /api/v1/projects/{projectId}/auth/m2m-applications`, `POST /api/v1/projects/{projectId}/auth/m2m-applications`, `DELETE /api/v1/projects/{projectId}/auth/m2m-applications/{clientId}`, `POST /api/v1/projects/{projectId}/auth/m2m-applications/{clientId}/rotate`, `POST /api/v1/projects/{projectId}/auth/m2m/token` |

```ts
const apiKeys = await client.apiKeys.list();
```

## Backups and Restores

```ts
const databaseId = toUlid('01J2K7RTEQC3F4NG9HZ8Y62P6B');

await client.backups.configurePolicy(databaseId, {
  fullBackupCron: '0 3 * * *',
  incrementalBackupCron: '0 */6 * * *',
  retentionDays: 14,
  disabled: false
});

const operationSessionId = 'backup-review-2026-07-05';
const plan = await client.backups.planBackup(databaseId, { operationSessionId });
if (!plan.ok) throw new Error('Backup plan failed');

displayBackupPlanToHumanOrAgent(plan.value);
if (!await waitForExplicitHumanConfirmation(plan.value)) {
  throw new Error('Backup was not confirmed');
}

const execution = await client.backups.executeBackup(
  databaseId,
  { operationSessionId, confirmationToken: plan.value.confirmationToken },
  'backup-execution-2026-07-05'
);

if (execution.ok) {
  const restore = await client.backups.startRestore(databaseId, {
    backupId: execution.value.backupId,
    idempotencyKey: 'restore-orders-2026-07-05'
  });

  if (restore.ok) {
    console.log(restore.value.restoredDatabaseId);
  }
}
```

Backups use `POST /api/v1/projects/{projectId}/databases/{databaseId}/backups:plan` followed by the explicitly confirmed `.../backups:execute` call, plus `/backups`, `/backups/policy`, `/restore-points`, and `/restores`. `executeBackup` requires an idempotency key. `waitForExplicitHumanConfirmation` is application-owned and must not be automated. A restore returns `restoredDatabaseId` for the newly materialized database and does not overwrite the source database.

## Billing, Usage, Audit, and Notifications

```ts
const organizationId = toUlid('01J2K7RTEQC3F4NG9HZ8Y62P6A');

const account = await client.billing.getAccount(organizationId);
const invoices = await client.billing.listInvoices(organizationId, { skip: 0, take: 50 });
const checkout = await client.billing.createCheckoutSession(organizationId, {
  priceId: 'price_123',
  successUrl: 'https://app.example.test/success',
  cancelUrl: 'https://app.example.test/cancel'
});

const plans = await client.pricing.listPlans();
const usage = await client.usage.getProjectUsage();
const organizationUsage = await client.usage.getOrganizationUsage(organizationId);
const latency = await client.usage.getProjectLatency();
const usageHistory = await client.usage.getProjectUsageHistory('30d');
const audit = await client.audit.list();
const notifications = await client.notifications.list({ unreadOnly: true });
```

Notification helpers use `/api/v1/users/me/notifications` and its mark-read actions. Security helpers use `GET` and `PUT /api/v1/projects/{projectId}/security/settings`.

Each SDK call returns a `TerraScaleResult<T>`. Check `result.ok` before reading `result.value`.

## Validate

From the `TerraScale.TypeScript` repository:

```bash
npm run typecheck
npm run build
```
