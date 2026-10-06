---
title: C# Management Status
description: Current status of C# account and management helpers.
sidebar:
  order: 2
  badge:
    text: Updated
    variant: caution
---

There is no current dedicated C# management-client package in the authoritative source set. Do not install or document that retired package shape for new integrations.

The supported C# package is [`TerraScale.DotNet`](/guides/sdks/csharp/). Its `TerraScaleClient` covers:

- `Databases`
- `Collections`
- `Repositories`
- `Documents`
- `Tql`
- `Schemas`
- `Changes`
- `Billing`
- `Projects`
- `Regions`
- `ProjectDatabases`
- `Queues`
- `Environments`
- `ProjectUsage`
- `ApiKeys`
- `M2MApplications`
- `Access`
- `Notifications`
- `Backups`

It does not expose account sign-in, user-profile, organization-management, auth-provider, invitation, audit, admin, or generated OpenAPI operation helpers.

## Current Management Helpers

Use `TerraScale.DotNet` for current project, region, project database, queue, environment, project usage, project auth API-key, M2M application, notification, and backup management helpers.

```csharp
var project = await client.Projects.GetAsync(projectId, cancellationToken);
var databases = await client.ProjectDatabases.ListAsync(projectId, cancellationToken: cancellationToken);
var usage = await client.ProjectUsage.GetAsync(projectId, cancellationToken);
var keys = await client.ApiKeys.ListAsync(projectId, cancellationToken: cancellationToken);
var apps = await client.M2MApplications.ListAsync(projectId, cancellationToken: cancellationToken);
var teamMembers = await client.Access.ListTeamMembersAsync(
    projectId,
    skip: 0,
    take: 100,
    cancellationToken);
var notifications = await client.Notifications.ListAsync(unreadOnly: true, cancellationToken: cancellationToken);
var backups = await client.Backups.ListAsync(projectId, databaseId, cancellationToken: cancellationToken);
```

Project API-key management lives at `/api/v1/projects/{projectId}/auth/api-keys`. Machine-to-machine applications live at `/api/v1/projects/{projectId}/auth/m2m-applications`. Anonymous M2M token exchange uses `/api/v1/projects/{projectId}/auth/m2m/token` through `CreateTokenAsync`, `CreateTokenFormAsync`, or `CreateTokenWithBasicCredentialsAsync`.

## Acceso de miembros del equipo del proyecto

`Access` es la familia de cliente público y tipado para el acceso de miembros del equipo del proyecto. Estos endpoints requieren una identidad bearer de propietario adecuada. Configura el cliente con `BearerToken` o `BearerTokenProvider`; una clave de API del proyecto no autoriza la gestión de miembros del equipo.

```csharp
var members = await client.Access.ListTeamMembersAsync(
    projectId,
    skip: 0,
    take: 100,
    cancellationToken);

var added = await client.Access.AddTeamMemberAsync(
    projectId,
    new TerraScaleAddProjectTeamMemberRequest(userId, "member"),
    cancellationToken);

var updated = await client.Access.UpdateTeamMemberAsync(
    projectId,
    userId,
    new TerraScaleUpdateProjectTeamMemberRequest("owner"),
    cancellationToken);

await client.Access.RemoveTeamMemberAsync(projectId, userId, cancellationToken);
```

El servicio proporciona para cada miembro `UserId`, `Email`, `DisplayName`, `Role` y `JoinedAt`, que admite valores nulos. Los valores de rol de cadena del ejemplo son valores de la API pública, no un bypass de autorización local.

> Advertencia: La automatización real para agregar, actualizar y quitar miembros necesita un contrato desechable o de solo creación impuesto por el servidor antes de poder modificar la membresía del equipo de forma segura. No uses API privadas de Platform, atajos del Dashboard, acceso directo a datos ni llamadas de solicitud genéricas como sustituto.

## Capacidades tipadas que faltan

No crees un contenedor de solicitudes genéricas ni evadas el límite del SDK tipado cuando `TerraScale.DotNet` no tenga una operación. Solicita una capacidad pública tipada mediante [soporte](/about/support/) e incluye el caso de uso, el ámbito de autorización, la forma de la solicitud y la respuesta, y si la intención es de lectura o mutación.

## Use The CLI For Operator Workflows

The TerraScale CLI has first-class command families for login, organizations, users, projects, project auth, databases, repositories, documents, queues, raw API calls, and streams.

See [TerraScale CLI](/guides/cli/).

## Next Steps

- [C# SDK](/guides/sdks/csharp/) - Supported C# package
- [Authentication](/reference/authentication/) - Bearer and API-key auth
- [Project API Keys](/reference/management/api-keys/) - Current project API-key routes
