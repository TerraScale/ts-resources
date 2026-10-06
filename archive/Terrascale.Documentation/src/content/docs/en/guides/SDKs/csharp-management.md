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

## Project Team-Member Access

`Access` is the typed public client family for project team-member access. These endpoints require a suitable owner bearer identity. Configure the client with `BearerToken` or `BearerTokenProvider`; a project API key does not authorize team-member management.

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

The service supplies each member's `UserId`, `Email`, `DisplayName`, `Role`, and nullable `JoinedAt`. The string role values in the sample are public API values, not a local authorization bypass.

> Warning: Real add, update, and remove automation needs a server-enforced disposable or create-only contract before it can safely mutate team membership. Do not use private Platform APIs, Dashboard shortcuts, direct data access, or generic request calls as a substitute.

## Missing Typed Capabilities

Do not build a generic request wrapper or bypass the typed SDK boundary when `TerraScale.DotNet` lacks an operation. Request a typed public capability through [support](/about/support/) with the use case, authorization scope, request and response shape, and read or mutation intent.

## Use The CLI For Operator Workflows

The TerraScale CLI has first-class command families for login, organizations, users, projects, project auth, databases, repositories, documents, queues, raw API calls, and streams.

See [TerraScale CLI](/guides/cli/).

## Next Steps

- [C# SDK](/guides/sdks/csharp/) - Supported C# package
- [Authentication](/reference/authentication/) - Bearer and API-key auth
- [Project API Keys](/reference/management/api-keys/) - Current project API-key routes
