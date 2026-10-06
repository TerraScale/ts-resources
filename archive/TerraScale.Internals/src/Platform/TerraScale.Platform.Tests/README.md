# TerraScale Platform Tests

## Overview

This project contains the internal test suite for TerraScale Platform API and endpoint
infrastructure. Tests use **TUnit 1.56.18** and cover endpoint conventions,
authentication, repository/database behavior, SDK compatibility, integration,
and end-to-end AppHost scenarios.

## Running Tests

```bash
# Run all tests
dotnet test --project src/Platform/TerraScale.Platform.Tests/TerraScale.Platform.Tests.csproj

# Run from solution root
dotnet test --project src/Platform/TerraScale.Platform.Tests
```

## Integration Tests

Most API integration tests use `TerraScaleAspireAppHostFixture`, which starts
`TerraScale.AppHost` through Aspire `DistributedApplicationTestingBuilder` and
waits for the service resources needed for API behavior tests:

- **TerraBase** executable resource
- **API** project
- **Authentication** project
- **Cloudflare Email Sending REST emulator**
- **NATS JetStream**

New AppHost/Aspire-facing coverage should use `TerraScaleAspireAppHostFixture`
or `DistributedApplicationTestingBuilder` against `TerraScale.AppHost`. Local
developer orchestration uses `TerraScale.AppHost`.

### AppHost Coverage

Aspire AppHost tests cover broad TerraBase repository/database behavior, public
`TerraScale.DotNet` SDK paths, organization creation, personal workspace
provisioning, access management, project usage/workload aggregation, generic
role-protected administration endpoints, storage migration, password hashing
and email verification, CoreMetadata endpoint routing, support notes, billing
webhook projection through provider-neutral queues, request/month metering, and
public user notification product endpoints. Provider client tests use bounded
test-local HTTP stubs; AppHost does not host a payment emulator.
`TerraScale.Platform` has no Dashboard-specific
endpoints or business logic; Dashboard routes and orchestration are tested in
Dashboard Next.

### Prerequisites

1. TerraBase must be checked out beside Internals at `../TerraBase`.
2. TerraScale.DotNet must be checked out beside Internals at `../TerraScale.DotNet`.

### Filtering Integration Tests

**Filter by property:**

```bash
dotnet test --project src/Platform/TerraScale.Platform.Tests --treenode-filter "/*/*/*/*[Category=Integration]"
```

**Run only Aspire AppHost tests:**

```bash
dotnet test --project src/Platform/TerraScale.Platform.Tests --treenode-filter "/*/*/*/*[Requires=AspireAppHost]"
```

## Test Architecture

### Aspire AppHost Integration Tests

The `TerraScaleAspireAppHostFixture` class starts `TerraScale.AppHost` through
Aspire `DistributedApplicationTestingBuilder`, waits for resources to become
healthy, and exposes Aspire-created HTTP clients for API, TerraBase, and the
local email emulator. The fixture assigns a fresh temporary TerraBase data
directory per test session and removes it on disposal, so AppHost tests do not
reuse state from previous local runs.
