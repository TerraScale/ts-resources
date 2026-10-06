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

`TerraScaleRuntimeConfig` requer `apiBaseUrl`. Também aceita `authBaseUrl`, `projectId`, `accessToken`, `defaultHeaders`, um `fetch` customizado, métricas de requests e uma fábrica de chaves de idempotência.

`accessToken` pode ser uma string ou uma função que retorna um token. O transporte o envia como `Authorization: Bearer ...`, define `accept: application/json` e encaminha `x-terrascale-project-id` quando `projectId` está configurado. Não existe header exclusivo do Dashboard nem bypass de tenant.

## Public Client Families

`createTerraScaleClient` returns these public families:

| Family | Purpose |
| --- | --- |
| `auth` | Sessão, links de login sem senha por e-mail, verificação de e-mail, refresh, logout e chamadas de sessões de conta. |
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

O tipo público também expõe `config` e o escape de baixo nível `request(...)` para integrações de clientes. O Dashboard usa apenas métodos tipados e compõe seus endpoints específicos dentro do próprio projeto full-stack. O SDK não possui cliente, DTO, rota, identificador ou helper de banco de dados específico do Dashboard.

## Status do contrato de onboarding

A tabela de famílias descreve a superfície tipada publicada atualmente. O fluxo alvo de autorregistro começará com a verificação de identidade e e-mail já contada como uma etapa concluída. Em seguida, cobrirá a primeira Organization, o primeiro Project e a primeira Database lógica, além da verificação de um cartão de pagamento para controle de abuso no cadastro. O fluxo permitirá continuar sem plano pago e sem renovação automática, mantendo a franquia Developer, ou selecionar Starter ou Pro com renovação automática mensal e os primeiros 30 dias sem cobrança quando a Organization for elegível. O onboarding de Users convidados continuará separado.

Esse objetivo é acompanhado pelo [issue 6 do TerraScale.TypeScript](https://git.terrascale.tech/TerraScale/TerraScale.TypeScript/issues/6) e pelo [issue 30 do TerraScale.Internals](https://git.terrascale.tech/TerraScale/TerraScale.Internals/issues/30). Até que os dois contratos sejam publicados, não apresente o fluxo completo como disponível nem crie rotas não documentadas para simulá-lo.

Public clients opt in to mutation idempotency with `idempotencyKeyFactory` on the client or `idempotencyKey` on an individual request. Set the request value to `false` to opt out of global generation.

## Confirmação de exclusão de banco de dados

`client.databases.delete(databaseId, { confirm: true })` confirma explicitamente a exclusão e envia `X-TerraScale-Delete-Confirmation` com esse ULID exato do banco de dados. Ele exclui o banco de dados lógico do projeto selecionado pelo cliente. A rota física administrativa global `DELETE /api/v1/databases/{databaseId}` também exige o mesmo cabeçalho e a autorização administrativa adequada. Uma confirmação ausente ou diferente retorna `400 Bad Request`.

## Exclusão durável de ambientes

Use o método tipado de exclusão de ambiente e inspecione ambos os campos de conclusão. A conclusão requer `deleted: true` e `status: 'Completed'`; um `status` ausente não indica conclusão. `deleted: false` ou `status: 'RetryScheduled'` está pendente; preserve `operationId` para correlação e não aja antes de `retryAt`. Leituras do ambiente podem mostrar `Deleting` durante esse período. Não há rota pública de status da operação nem escape de solicitação genérica, portanto não use rota privada nem acesso direto a dados para contornar o cliente tipado.

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

O SDK expõe login sem senha por e-mail: solicite um link e conclua o login depois de abri-lo. Essa superfície de helpers não significa que a migração de contas da ADR-0041 esteja concluída; a API pública atual ainda mantém rotas legadas de credenciais de contas.

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
