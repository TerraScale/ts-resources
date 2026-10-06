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

`TerraScaleRuntimeConfig` requiere `apiBaseUrl`. También acepta `authBaseUrl`, `projectId`, `accessToken`, `defaultHeaders`, un `fetch` personalizado, métricas de requests y una fábrica de claves de idempotencia.

`accessToken` puede ser un string o una función que devuelve un token. El transporte lo envía como `Authorization: Bearer ...`, configura `accept: application/json` y reenvía `x-terrascale-project-id` cuando `projectId` está configurado. No existe un header exclusivo del Dashboard ni un bypass de tenant.

## Public Client Families

`createTerraScaleClient` returns these public families:

| Family | Purpose |
| --- | --- |
| `auth` | Sesión, enlaces de acceso sin contraseña por correo, verificación de correo, refresh, logout y llamadas de sesiones de cuenta. |
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

El tipo público también expone `config` y el escape de bajo nivel `request(...)` para integraciones de clientes. El Dashboard usa solo métodos tipados y compone sus endpoints específicos dentro de su propio proyecto full-stack. El SDK no tiene cliente, DTO, ruta, identificador ni helper de base de datos específico del Dashboard.

## Estado del contrato de onboarding

La tabla de familias describe la superficie tipada publicada actualmente. El flujo objetivo de autorregistro comenzará con la verificación de identidad y correo electrónico ya contada como un paso completado. Luego cubrirá la primera Organization, Project y Database lógica, además de verificar una tarjeta de pago para controlar abusos en el registro. Permitirá continuar sin un plan de pago y sin renovación automática, conservando la asignación Developer, o seleccionar Starter o Pro con renovación automática mensual y los primeros 30 días sin cargo cuando la Organization sea elegible. El onboarding de Users invitados seguirá siendo un flujo separado.

Este objetivo se sigue en el [issue 6 de TerraScale.TypeScript](https://git.terrascale.tech/TerraScale/TerraScale.TypeScript/issues/6) y el [issue 30 de TerraScale.Internals](https://git.terrascale.tech/TerraScale/TerraScale.Internals/issues/30). Hasta que ambos contratos estén publicados, no presente el flujo completo como disponible ni construya rutas no documentadas para simularlo.

Public clients opt in to mutation idempotency with `idempotencyKeyFactory` on the client or `idempotencyKey` on an individual request. Set the request value to `false` to opt out of global generation.

## Confirmación de eliminación de base de datos

`client.databases.delete(databaseId, { confirm: true })` reconoce explícitamente la eliminación y envía `X-TerraScale-Delete-Confirmation` con ese ULID exacto de base de datos. Elimina la base de datos lógica del proyecto seleccionada por el cliente. La ruta física administrativa global `DELETE /api/v1/databases/{databaseId}` también requiere el mismo encabezado y la autorización administrativa adecuada. Una confirmación ausente o diferente devuelve `400 Bad Request`.

## Eliminación durable de entornos

Use el método tipado de eliminación de entorno e inspeccione ambos campos de finalización. La finalización requiere `deleted: true` y `status: 'Completed'`; un `status` ausente no indica finalización. `deleted: false` o `status: 'RetryScheduled'` sigue pendiente; conserve `operationId` para correlación y no actúe antes de `retryAt`. Las lecturas del entorno pueden mostrar `Deleting` durante ese período. No existe una ruta pública de estado de operación ni un escape de solicitud genérica, por lo que no use una ruta privada ni acceso directo a datos para sortear el cliente tipado.

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

El SDK expone acceso sin contraseña por correo: solicita un enlace y completa el acceso después de abrirlo. Esta superficie de helpers no significa que la migración de cuentas de ADR-0041 esté completa; la API pública actual todavía conserva rutas heredadas de credenciales de cuentas.

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
