---
title: Platform Concepts
description: Product concepts across TerraScale database, auth, queue, billing, SDKs, dashboard, and operations.
sidebar:
  order: 2
---

TerraScale is a developer platform for database, auth, queue, billing, SDK, dashboard, and operational workflows. This page describes the current public concepts and avoids internal implementation shortcuts.

## Public API Boundary

Public product APIs use REST HTTP with versioned `/api/v1` routes. Public resource IDs are ULIDs. Direct TerraBase access and private service calls are not part of the public product contract.

TerraScale puede usar MagicOnion entre sus propios procesos de backend. Ese
transporte privado es un detalle de implementación, no un protocolo compatible
para clientes. Las aplicaciones, los SDK, la CLI y el Dashboard siguen usando
el mismo contrato REST versionado.

## Database

Databases are managed through:

```text
POST /api/v1/databases
GET /api/v1/databases
GET /api/v1/databases/{databaseId}
DELETE /api/v1/databases/{databaseId}
```

Database create requests use `name`, `replicationFactor`, and optional `settings`.

## Repositories and Documents

Repositories are the public data model for application documents. A repository maps to a collection and exposes document CRUD, batch, TQL, schema, and change-stream routes.

```text
POST /api/v1/repositories
POST /api/v1/repositories/{repositoryId}/documents
POST /api/v1/repositories/{repositoryId}/tql
```

## Auth

La autenticación con bearer token admite registro, verificación de correo, enlaces de acceso sin contraseña por correo, refresh, logout, usuario actual y sesiones de cuenta. ADR-0041 define el correo sin contraseña como modelo objetivo, pero el contrato público actual conserva operaciones heredadas de contraseña, MFA y passkey para cuentas durante la migración. Project auth agrega por separado usuarios, proveedores, API keys y aplicaciones machine-to-machine con alcance de proyecto.

Project API-key calls use:

```http
X-TerraScale-Auth-Key: tsauth_...
X-TerraScale-Project-Id: 01J2K7RTEQC3F4NG9HZ8Y62P6A
```

## Queue

Queue is exposed through `/api/v1/projects/{projectId}/queues`, C# `client.Queues`, TypeScript `client.queues`, and CLI queue/topic families (including retry, dead-letter, and replay where registered).

## Billing

Billing routes are organization-scoped and include billing accounts, invoices, checkout sessions, portal sessions, Stripe webhooks, and pricing plans. `TerraScale.DotNet` exposes billing helpers for account, invoice, checkout, and portal operations.

## SDKs

| SDK | Package | Current scope |
| --- | --- | --- |
| C# | `TerraScale.DotNet` | Regions, databases, collections, repositories, documents, TQL, schemas, changes, billing, projects, project databases, environments, queues, usage, API keys, M2M, notifications, backups. |
| TypeScript | `@terrascale/sdk` | Auth, organizations/projects, regions, databases, queues, repositories, documents, TQL, schema, backups, API keys, M2M, usage, notifications, billing, pricing, audit, security, and raw request access. |

## CLI

The TerraScale CLI exposes command families for login/logout, whoami, organizations, users, projects, project auth, databases, repositories, documents, queues, raw API calls, and streams.

## Completion Standard

A feature is complete when:

- It works through the intended public API, SDK, CLI, or dashboard path.
- It persists or reads real backend state.
- Contracts, SDKs, docs, dashboard, and tests agree.
- Errors, security, tenant isolation, telemetry, and audit behavior are testable.
