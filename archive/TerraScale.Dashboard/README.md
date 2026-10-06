# TerraScale.Dashboard

The production TerraScale Dashboard — a full-stack Vinext (React RSC) app on the
VitePlus `vp` toolchain with Tailwind CSS. This repository was extracted from
`TerraScale.Internals/src/Dashboard/TerraScale.Dashboard.Next` with its full git
history; the dashboard app lives at the repository root.

The Dashboard is an ordinary external TerraScale user: all TerraScale data flows
through typed operations of the `@terrascale/sdk` TypeScript SDK against the
public Platform/Auth APIs. It owns every Dashboard-specific route, route
handler, server action, orchestration flow, and view model.

## Workspace layout

This repository expects to sit next to its siblings in the TerraScale
workspace:

- `../TerraScale.TypeScript` — the SDK, consumed as a `file:` dependency.
- `../TerraScale.Internals` — Platform, Authentication, and the Aspire
  `TerraScale.AppHost` that composes the local stack (Dashboard, Platform,
  Auth, TerraBase, emulators).

## Commands

All lifecycle commands go through VitePlus `vp` (never raw npm/npx/vite/next):

```bash
vp install --frozen-lockfile   # install
vp run vinext:dev              # dev server (HMR) — see AGENTS.md for the AppHost-first rule
vp run vinext:build            # standalone production build (dist/standalone)
vp run vinext:start            # run the standalone build
vp check                       # lint/format/typecheck
vp run vinext:check            # route check
vp run playwright:e2e          # browser E2E through the local Aspire stack
vp run test:policy             # Vitest policy/unit suite
```

Local product testing runs through `TerraScale.AppHost`, which builds and starts
this repository as the `dashboard` resource and points it at the local
Platform/Auth URLs:

```bash
dotnet run --project ../TerraScale.Internals/src/Hosting/TerraScale.AppHost/TerraScale.AppHost.csproj
```

## Tests

- `e2e/` — Playwright browser proof of real product behavior over the local
  Aspire stack. Run with `vp run playwright:e2e`; its global setup boots
  `TerraScale.AppHost` and targets the emitted randomized Dashboard/Platform/
  Auth/TerraBase/EmailEmulator URLs. These suites own the full workspace
  topology, so they run serialized (one worker) under the workspace
  `AspireTopologyLease` — never concurrently with other full-topology suites.
- `tests/` — the repository policy suite (Vitest), guarding toolchain and
  repository-content invariants. Run with `vp run test:policy`; the same task
  also runs the unit tests colocated under `src/`.

See `AGENTS.md` for the full conventions and `DESIGN_SYSTEM.md` for the
design tokens.
