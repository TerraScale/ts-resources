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

## Acesso de membros da equipe do projeto

`Access` é a família de cliente público e tipado para o acesso de membros da equipe do projeto. Esses endpoints exigem uma identidade bearer de proprietário adequada. Configure o cliente com `BearerToken` ou `BearerTokenProvider`; uma chave de API do projeto não autoriza o gerenciamento de membros da equipe.

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

O serviço fornece para cada membro `UserId`, `Email`, `DisplayName`, `Role` e `JoinedAt`, que aceita nulo. Os valores de função em texto do exemplo são valores da API pública, não um bypass de autorização local.

> Aviso: A automação real para adicionar, atualizar e remover membros precisa de um contrato descartável ou apenas de criação imposto pelo servidor antes de poder alterar a associação da equipe com segurança. Não use APIs privadas da Platform, atalhos do Dashboard, acesso direto aos dados nem chamadas de solicitação genéricas como substitutos.

## Capacidades tipadas ausentes

Não crie um wrapper de solicitações genéricas nem contorne o limite do SDK tipado quando `TerraScale.DotNet` não tiver uma operação. Solicite uma capacidade pública tipada pelo [suporte](/about/support/) com o caso de uso, o escopo de autorização, a forma da solicitação e da resposta, e se a intenção é de leitura ou mutação.

## Use The CLI For Operator Workflows

The TerraScale CLI has first-class command families for login, organizations, users, projects, project auth, databases, repositories, documents, queues, raw API calls, and streams.

See [TerraScale CLI](/guides/cli/).

## Next Steps

- [C# SDK](/guides/sdks/csharp/) - Supported C# package
- [Authentication](/reference/authentication/) - Bearer and API-key auth
- [Project API Keys](/reference/management/api-keys/) - Current project API-key routes
