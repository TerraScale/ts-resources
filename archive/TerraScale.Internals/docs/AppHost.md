# TerraScale AppHost

`TerraScale.AppHost` is the local orchestration entrypoint for Internals. It is a real
Aspire `DistributedApplication`; do not replace its resources with bespoke process or
container harnesses when Aspire can model the dependency directly.

## Resources

The AppHost starts:

- NATS with JetStream.
- TerraBase from the sibling `/workspaces/TerraScale/TerraBase` checkout.
- `TerraScale.Authentication`.
- `TerraScale.Platform`.
- A local email emulator.
- Dashboard Next from the sibling `/workspaces/TerraScale/TerraScale.Dashboard`
  checkout (override with `TERRASCALE_DASHBOARD_REPOSITORY_ROOT`).

All service endpoints use Aspire-managed randomized ports. Do not pin host ports in
AppHost code, launch settings, environment variables, docs, or tests. Read endpoints from
the AppHost output or from Aspire APIs.

Platform and Authentication also receive randomized `internal-rpc` endpoints.
They are non-external HTTP/2 listeners and are never passed to Dashboard or a
public client. Authentication receives the Platform internal endpoint for its
current region and uses it only to remove incomplete Signup verification data
before deleting a TerraScale User. Project authentication users do not call
this RPC. Authentication does not wait for Platform to become healthy, so this
reverse call does not create a circular startup dependency. Platform still
starts only after Authentication can accept its required internal RPC
dependency; public readiness remains available at `/health/ready`.

## Start

From the TerraScale.Internals repo root:

```bash
dotnet build -m src/Hosting/TerraScale.AppHost/TerraScale.AppHost.csproj
dotnet run --project src/Hosting/TerraScale.AppHost/TerraScale.AppHost.csproj --no-build
```

The AppHost prints the local service URLs:

```text
TerraBase:       http://localhost:45309
Authentication: http://localhost:38351
Platform:       http://localhost:36411
EmailEmulator:  http://localhost:46127/client/v4/
Dashboard:      http://localhost:45349
```

The Dashboard surface is Dashboard Next. AppHost builds the Vinext standalone output with
VitePlus, starts it on the randomized Dashboard URL, and injects the local Platform/Auth URLs.
The deleted legacy Blazor Dashboard must not be wired into AppHost again.

Payment traffic uses the same Polar or Stripe client as production. Polar is the default.
Set `Payments__Polar__AccessToken` and provider product IDs for Polar sandbox testing, or
set `Payments__Provider=stripe` with `Payments__Stripe__SecretKey` and Stripe test price
IDs. AppHost forwards every `Payments__*` setting to Platform; it does not start a payment
emulator.

## Interactive Dashboard Work

For normal full-stack validation, use the Dashboard URL printed by AppHost. For HMR work,
run the Dashboard Next dev server separately and point it at the local AppHost URLs:

```bash
cd ../TerraScale.Dashboard
TERRASCALE_API_BASE_URL=http://localhost:<api-port> \
TERRASCALE_AUTH_API_BASE_URL=http://localhost:<auth-port> \
vp run vinext:dev
```

Never point a dev Dashboard process at production `api.terrascale.tech` or
`auth.terrascale.tech`.

## Test Guidance

Aspire-backed tests should use `DistributedApplicationTestingBuilder`, wait for the target
resources to become healthy, and read endpoints or connection strings through Aspire APIs.

```csharp
await using var builder = await DistributedApplicationTestingBuilder
    .CreateAsync<Projects.TerraScale_AppHost>(cancellationToken);

await using var app = await builder.BuildAsync(cancellationToken);
await app.StartAsync(cancellationToken);
await app.ResourceNotifications.WaitForResourceHealthyAsync("platform", cancellationToken);

var apiClient = app.CreateHttpClient("platform", "http");
```

Existing API/service integration tests should use the Aspire AppHost fixtures directly.
Tests that verify AppHost or Aspire behavior should target the Aspire graph directly.
Transport tests may resolve `app.GetEndpoint("platform", "internal-rpc")`; product clients
must continue to use the named `http` endpoint.
