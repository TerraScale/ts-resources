# TerraScale Runtime Images

Local development runs through `TerraScale.AppHost`; see `docs/AppHost.md` and
`docs/local-dev-tailscale.md`. Do not use Docker Compose as the local TerraScale
orchestration path.

This directory keeps production runtime image assets only:

- Platform and Authentication publish containers with the .NET SDK container
  publisher through `TerraScale.Deploy.Cli`.
- The Dashboard Next runtime Dockerfile lives in the `TerraScale.Dashboard`
  repository (`deploy/Dashboard.Next.Runtime.Dockerfile` there).

## Production Release Automation

The unified `.forgejo/workflows/ci.yml` workflow uses `TerraScale.Deploy.Cli` to
discover affected targets. A `develop` to `main` promotion validates them and
builds immutable release candidates once; the approved `main` revision promotes
those exact stored artifacts without rebuilding them.

This repository owns runtime image assets only. `TerraScale.Orchestrator`
consumes the immutable artifacts and owns production rollout, health
verification, and rollback.
