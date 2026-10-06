---
title: TerraScale CLI
description: Command families exposed by the TerraScale CLI.
sidebar:
  order: 13
  badge:
    text: New
    variant: tip
---

The TerraScale CLI is implemented by `TerraScale.CLI`. It uses Spectre.Console command families over the public TerraScale Platform HTTP APIs and local CLI profiles.

## Authentication and Profiles

Use os comandos de login para criar ou atualizar credenciais locais. O Dashboard aceita login sem senha por e-mail, e a API pública atual também mantém operações legadas de login de contas enquanto a migração da ADR-0041 não está concluída. A CLI armazena localmente o token resultante ou uma API key:

```bash
terrascale login token
terrascale login api-key
terrascale whoami
terrascale logout
```

Profile commands are available under `profile` and the `profiles` alias:

```bash
terrascale profile list
terrascale profile show
terrascale profile use
terrascale profile set
terrascale profile delete
```

`whoami` also has the `me` alias. `logout` revokes the active session when the current profile has token credentials that can call the logout route.

## Core and Health

```bash
terrascale version
terrascale status
terrascale services health
terrascale openapi
```

`status` and `health` are aliases for service health. `services health` also has the `status` alias.

## Organizations, Users, and Projects

Top-level organization and user commands:

```bash
terrascale organization list
terrascale organization get
terrascale organization create
terrascale user list
terrascale user get
terrascale user create
```

`organization` has `organizations`, `org`, and `orgs` aliases. `user` has the `users` alias.

Project commands:

```bash
terrascale project list
terrascale project get
terrascale project create
terrascale project audit list
terrascale project permission get
terrascale project permission grant
terrascale project group list
terrascale project group create
terrascale project group members list
terrascale project group members add
```

`project` has the `projects` alias. Permission commands also expose `permissions`, `check`, and `evaluate` aliases where the CLI source registers them.

## Project Databases and Auth

Project-scoped database commands:

```bash
terrascale project databases list
terrascale project databases get
terrascale project databases create
terrascale project databases delete
terrascale project databases environments list
terrascale project databases environments get
terrascale project databases environments create
terrascale project databases environments delete
```

Project auth commands are registered under `auth` with `project-auth` as an alias:

```bash
terrascale auth api-key list
terrascale auth api-key create
terrascale auth api-key rotate
terrascale auth api-key delete
terrascale auth provider list
terrascale auth provider get
terrascale auth provider upsert
terrascale auth provider delete
terrascale auth user list
terrascale auth user get
terrascale auth user create
terrascale auth user roles
terrascale auth user update
terrascale auth user delete
```

The API route families behind project auth are `/api/v1/projects/{projectId}/auth/api-keys`, `/api/v1/projects/{projectId}/auth/providers`, `/api/v1/projects/{projectId}/auth/users`, and `/api/v1/projects/{projectId}/auth/m2m-applications`.

## Database, Repository, and Document Commands

Database commands:

```bash
terrascale database list
terrascale database get
terrascale database create
terrascale database delete
terrascale database stats
terrascale database collections
```

Repository commands:

```bash
terrascale repository list
terrascale repository get
terrascale repository create
terrascale repository delete
terrascale repository schema get
terrascale repository schema set
terrascale repository schema validate
```

Document commands:

```bash
terrascale document list
terrascale document get
terrascale document create
terrascale document put
terrascale document patch
terrascale document batch
terrascale document delete
terrascale document query
```

Aliases include `databases` and `db`, `repositories` and `repo`, and `documents` and `doc`. `document query` also has the `tql` alias.

## Raw API and Streams

Raw API commands:

```bash
terrascale api get
terrascale api post
terrascale api put
terrascale api patch
terrascale api delete
terrascale api head
terrascale api stream
terrascale stream
```

Use these when you need to exercise a public route before a higher-level CLI command exists.

## Queue Commands

Queue, topic, subscription, and consumer commands are real CLI surfaces:

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
terrascale topic list
terrascale topic create
terrascale topic delete
terrascale subscription list
terrascale subscription create
terrascale subscription delete
terrascale consumer inspect
```

C# `client.Queues` and TypeScript `client.queues` wrap the same project queue routes. The CLI remains useful for operations, metrics, and topic/subscription workflows.

The CLI also registers Docker-style top-level aliases such as `build`, `bake`, `images`, `pull`, `push`, `image`, `manifest`, `container`, `builder`, `buildx`, `compose`, and `system`.
