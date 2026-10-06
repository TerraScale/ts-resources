# Dashboard Next Cutover Status

Scope: active cutover evidence and guardrails for the `TerraScale.Dashboard`
sibling repository (app at the repo root).

Dashboard Next is the production Dashboard surface. The legacy Blazor
`TerraScale.Dashboard` app and `TerraScale.Dashboard.Tests` project are deleted
and must not be reintroduced.

## Current State

| Area | Required state |
|---|---|
| Runtime app | `TerraScale.Dashboard.Next` Vinext/VitePlus/Tailwind app |
| Full-stack ownership | All Dashboard routes, route handlers, server actions, and orchestration live in Dashboard Next |
| Transport | TerraScale TypeScript SDK over public REST only |
| API boundary | `TerraScale.Platform` exposes Dashboard-agnostic product APIs only; no Dashboard feature slice or `/api/v1/dashboard` routes |
| Local stack | `TerraScale.AppHost` starts Dashboard Next and injects local Platform/Auth URLs |
| Production image | `terrascale-dashboard` image built from Dashboard Next standalone output |
| Production smoke | Removed — no scheduled smoke workflow; product proof is the Dashboard profile in the unified release test matrix |
| Product e2e | `TerraScale.Dashboard/e2e` through AppHost |
| Deleted legacy code | No legacy Blazor `TerraScale.Dashboard`/`TerraScale.Dashboard.Tests` projects; `src/Dashboard/` no longer exists in Internals |

## Non-Negotiable Boundaries

- Dashboard Next must not use direct TerraBase access, private API
  shortcuts, Blazor fragments, Razor components, Datastar, or
  `TerraScale.Dashboard.Contracts`.
- Dashboard-specific routes, route handlers, server actions, orchestration,
  view models, and persistence choices must stay inside Dashboard Next.
- Route files, route handlers, components, and feature services must not call
  raw `fetch`. Every TerraScale product-data read and write uses typed public
  product APIs from the TypeScript SDK.
- `TerraScale.Platform` must not contain Dashboard endpoints, DTOs, services, options,
  or business logic. Add API and SDK surface only for reusable,
  Dashboard-agnostic product capabilities.
- Dashboard tests must be Playwright e2e tests against AppHost. Do not add
  mocked, jsdom, component-only, static-only, synthetic-cookie, or
  Dashboard-only tests as product proof.
- Documentation, workflows, Dockerfiles, and AppHost wiring must point to
  Dashboard Next. Any instruction to build or run the old Dashboard is stale and
  must be removed.

## Verification Checklist

Use this checklist before claiming Dashboard cutover work is complete:

- The old Dashboard app and test project directories are absent.
- `TerraScale.Internals.slnx` has no old Dashboard project references.
- `.forgejo/workflows/ci.yml` uses the TerraScale.Deploy plan to run the
  Dashboard Next e2e gate, build its immutable candidate once, and promote that
  exact candidate after approval.
- Local development uses `TerraScale.AppHost`; the retired Docker Compose path must not be
  reintroduced for Dashboard Next.
- The Orchestrator workload descriptor sets
  `OTEL_SERVICE_NAME=TerraScale.Dashboard.Next` for the Dashboard runtime.
- `https://dash.terrascale.tech/health/ready` and
  `https://dash.terrascale.tech/api/stack` return `200`.
- Orchestrator reports the expected artifact digest and healthy Dashboard
  workload instances.

## What To Do With Old References

Old Blazor, Datastar, `TerraScale.Dashboard.dll`,
`TerraScale.Dashboard.Tests`, and legacy `src/Dashboard/TerraScale.Dashboard`
references in active docs or deployment paths are cleanup bugs. Replace them
with the `TerraScale.Dashboard` repository, public REST, SDK, VitePlus, and
Playwright/AppHost guidance. Historical
evidence may mention old names only when the file is explicitly archived and not
used as current engineering guidance.
