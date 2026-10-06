# Dashboard Next Production UX Evidence

Scope: production checks for `https://dash.terrascale.tech`.

Dashboard production is served by `TerraScale.Dashboard.Next`. The legacy Blazor
Dashboard production smoke and `TerraScale.Dashboard.Tests` project are deleted.
There is also no scheduled Forgejo production-smoke workflow; Dashboard product
proof in CI is its e2e profile in the unified release test matrix.

## Current Production Checks

Public production readiness is proven with live HTTP and Orchestrator evidence,
not a scheduled Actions smoke job.

## Manual Recheck

Run public endpoint checks from any environment that should deliberately touch
production:

```bash
curl -fsS -o /dev/null -w 'dashboard %{http_code}\n' https://dash.terrascale.tech/health/ready
curl -fsS -o /dev/null -w 'stack %{http_code}\n' https://dash.terrascale.tech/api/stack
curl -fsS -o /dev/null -w 'login %{http_code}\n' https://dash.terrascale.tech/login
```

Run local Dashboard Next checks from the `TerraScale.Dashboard` sibling checkout:

```bash
cd ../TerraScale.Dashboard
vp install --frozen-lockfile
vp check
vp run vinext:check
vp run vinext:build
vp exec playwright install chromium
vp run playwright:e2e
```

## Orchestrator Evidence

Production readiness is proven by live observed state, not by docs:

- The accepted Dashboard artifact digest matches the running workload.
- Ready Dashboard instances satisfy the workload health contract.
- Dashboard runtime configuration has
  `OTEL_SERVICE_NAME=TerraScale.Dashboard.Next`.
- Public `https://dash.terrascale.tech/health/ready` returns `200`.
- Public `https://dash.terrascale.tech/api/stack` returns `200`.
- Orchestrator and Grafana show no unresolved Dashboard rollout or health
  failures.

## Backlog

- Keep signed-in production checks available through dedicated smoke credentials
  when re-adding optional manual verification.
- Add route samples for `/databases`, `/data`, and `/api-keys` when a stable
  test project is available.
