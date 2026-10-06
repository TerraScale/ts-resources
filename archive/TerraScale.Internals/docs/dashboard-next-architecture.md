# Dashboard Next Architecture

Scope: the `TerraScale.Dashboard` sibling repository (app at the repo root), the
production Vinext + VitePlus + Tailwind Dashboard.

This app is the full-stack, external-customer-style TerraScale Dashboard. It
owns every Dashboard-specific route, route handler, server action, orchestration
flow, view model, and Dashboard-only persistence choice. It talks to TerraScale
only through typed public product APIs in the TerraScale TypeScript SDK. Browser
leaves may use same-origin `fetch` for Dashboard-owned route handlers, but no
Dashboard server code may use raw `fetch` for TerraScale product data, direct
TerraBase access, private API shortcuts, Blazor fragments, Razor components, or
Datastar.

`TerraScale.Platform` exposes reusable public product capabilities only. It must not
contain a Dashboard feature slice, `/api/v1/dashboard` routes, Dashboard DTOs,
services, options, or Dashboard-specific auth, notification, or business logic.

## Goals

- Ship a production customer dashboard with Vinext App Router, React 19,
  VitePlus, Tailwind, and the TerraScale TypeScript SDK.
- Keep the runtime boundary identical to an external customer app: browser or
  server route code -> TypeScript SDK -> public REST -> `TerraScale.Platform`.
- Keep every Dashboard endpoint and workflow inside Dashboard Next. Compose
  typed SDK operations locally instead of adding Dashboard-specific API paths.
- Own Dashboard onboarding state in the Dashboard app while creating real
  TerraScale projects and databases through public API contracts.
- Stay the only production Dashboard implementation. The deleted legacy Blazor
  Dashboard must not be reintroduced.

## Runtime Model

The app has three layers:

| Layer | Owns | Rules |
|-------|------|-------|
| Vinext routes | App Router pages, layouts, route handlers, loaders/actions, route guards, metadata | Routes stay thin and call feature slices. Dashboard-specific endpoints live here. |
| Feature slices | UI, view models, server actions/loaders, SDK orchestration, validation, tests | Each product area owns its Dashboard behavior. |
| SDK boundary | TerraScale TypeScript SDK factory, auth/session transport, typed API calls | Only this layer creates SDK clients or handles REST details. |

No app code may call TerraBase, internal Dashboard contracts, private API
endpoints, or raw TerraScale product endpoints. If a workflow is
Dashboard-specific, compose existing typed SDK methods inside the owning
feature slice. Add an API and SDK operation only when it is a reusable,
Dashboard-agnostic product capability available to external customers.

## Local Development

Run commands from the `TerraScale.Dashboard` sibling checkout:

```bash
vp install --frozen-lockfile
vp run vinext:dev
vp check
vp run vinext:check
vp run playwright:e2e
vp run vinext:build
vp run vinext:start
vp preview
```

Current VitePlus commands:

| Command | Script | Purpose |
|---------|--------|---------|
| `vp install --frozen-lockfile` | VitePlus install command | Restore dependencies from the committed lockfile. |
| `vp run vinext:dev` | `vinext:dev` task | Vinext development server. |
| `vp run vinext:build` | `vinext:build` task | Production build. |
| `vp run vinext:start` | `vinext:start` task | Run the standalone production build. |
| `vp check` | VitePlus check command | VitePlus format, lint, type, and project checks. |
| `vp run vinext:check` | `vinext:check` task | Vinext App Router route validation. |
| `vp run playwright:e2e` | `playwright:e2e` task | AppHost-backed Playwright e2e suite. |
| `vp preview` | VitePlus preview command | Preview built assets locally. |

Do not introduce pnpm, yarn, bun, corepack, or another lockfile. Do not replace
these with direct `npm`, `npm run`, `npx`, `vite`, `next`, `vinext`,
`playwright`, or custom Node commands. Package scripts may exist only as
compatibility wrappers that delegate back to `vp`.

## VitePlus, Vinext, Tailwind

The package is private and pinned to Node 22+ with a committed npm lockfile
backend. Dashboard Next workflows use VitePlus `vp` directly:

- `vinext` drives App Router routing and production rendering.
- `vite-plus` and `@voidzero-dev/vite-plus-core` provide the VitePlus runtime.
- `@vitejs/plugin-react`, `@vitejs/plugin-rsc`, and `react-server-dom-webpack`
  are the React 19/RSC integration surface.
- `@tailwindcss/vite` is the Tailwind integration. Prefer Tailwind v4 CSS-first
  configuration and keep app-wide theme tokens in the app stylesheet rather
  than adding ad hoc route CSS.
- `lucide-react` is the icon source.
- `dotted-map` is available for the region map and must be route-lazy.

Vinext auto-detects the `app/` router and loads `next.config.js`. The VitePlus
config exists for VitePlus, Tailwind, and task integration rather than App Router
discovery. Because the app uses `output: "standalone"`, `vinext:start` runs
`node dist/standalone/server.js`; use `HOST` and `PORT` for binding, not
`HOSTNAME`.

Vinext/VitePlus config and Tailwind entry files live inside the app only.

## AppHost Integration

`TerraScale.AppHost` starts Dashboard Next as the local Dashboard surface.
AppHost builds and starts the Next app
through VitePlus `vp` tasks, starts the standalone Vinext server on an
Aspire/randomized loopback port, and injects `TERRASCALE_API_BASE_URL`,
`TERRASCALE_AUTH_API_BASE_URL`, and
`TERRASCALE_DASHBOARD_PUBLIC_URL` from the live local stack. AppHost must not
wire in the deleted legacy Blazor Dashboard.

## SDK Usage

Every TerraScale product-data read and write flows through the TerraScale
TypeScript SDK:

- Create one SDK client factory that reads base URL, credentials mode, and
  request context from Dashboard configuration.
- Server route handlers, loaders/actions, and feature services call typed SDK
  methods, not raw `fetch`, for TerraScale product data.
- Use public REST DTOs exactly as the SDK exposes them. Do not mirror internal
  Blazor DTOs.
- Keep tenant/project/database identifiers as public ULID strings from the API.
- Translate API errors into typed route/view states at the feature boundary.

Raw `fetch` to TerraScale product endpoints is acceptable only inside the
TypeScript SDK package. Browser leaves may call same-origin Dashboard-owned
routes with `fetch`; those route handlers remain the trust boundary and must use
typed SDK methods for every TerraScale product-data read or write.

## Auth and Session Model

The Dashboard Next app consumes public auth endpoints like an external client:

- Sign in, sign up, email verification, sign-in links, session refresh, and
  logout use public REST contracts through the SDK. TerraScale accounts are
  email-only (ADR-0041): no password, external OAuth, passkey, or MFA flows.
- Session cookies are HTTP-only, secure in production, same-site appropriate,
  and scoped to the Dashboard host.
- Protected routes verify the session on the server before rendering protected
  data. Client-only hiding is not an authorization boundary.
- Unauthenticated users redirect to `/login` with a safe return URL.
- The app must never infer auth state from display text, route visibility, or
  client-only role labels.
- Admin or owner-only UI, if added to Next, must rely on generic API-enforced
  owner permissions exposed through `@terrascale/sdk/admin` and must not receive
  cross-tenant data for non-owner sessions. Dashboard routes and orchestration
  remain local to Dashboard Next.

## Dashboard-Owned Bootstrap

Dashboard onboarding owns its endpoints and customer-facing bootstrap flow, but
every TerraScale product-data read and write still uses typed SDK APIs:

1. Resolve the signed-in user session through the SDK.
2. Load the user's organizations/projects through public REST.
3. If no usable project exists, create the default TerraScale project through
   the SDK.
4. If no database exists for the project, offer an explicit create-database
   flow that provisions a logical database through the SDK.
5. Persist selected project, database, environment, and region choices through
   public user preference or project APIs when those contracts exist.

The Dashboard must not create TerraBase databases directly. Physical database
creation, virtual database partitions, environments, replication, and placement
remain `TerraScale.Platform` responsibilities.

## Deployment and Configuration

Production deployment owns only the Next app artifact and its runtime settings:

| Setting | Purpose |
|---------|---------|
| `TERRASCALE_API_BASE_URL` | Public `TerraScale.Platform` REST base URL. |
| `TERRASCALE_DASHBOARD_PUBLIC_URL` | Canonical Dashboard Next URL for redirects. |
| `TERRASCALE_AUTH_API_BASE_URL` | Public TerraScale Auth REST base URL. |
| `HOST` | Standalone Vinext bind host. |
| `PORT` | Standalone Vinext bind port. |
| `TERRASCALE_AUTH_COOKIE_DOMAIN` | Cookie domain when shared across TerraScale hosts. |
| `TERRASCALE_ENVIRONMENT` | `Development`, `Preview`, or `Production`. |
| `TERRASCALE_SDK_TIMEOUT_MS` | SDK request timeout budget. |

Configuration must come from environment variables or secret storage. Do not
hard-code API URLs, credentials, owner identities, project IDs, database IDs, or
region assumptions in source.

Production images are owned by the app repository/workflow that builds this app
and must publish runtime images to OCI Container Registry only. Do not publish
TerraScale runtime images to Forgejo packages. Controlled production promotion
must use the immutable candidate from the protected `develop` to `main` release
workflow. TerraScale.Orchestrator owns delivery of its exact digest.

## CI

Required CI checks for Dashboard Next (via `.forgejo/workflows/ci.yml` and the
Deploy CLI):

- `vp install --frozen-lockfile`
- `vp check`
- `vp run vinext:check`
- `vp run vinext:build`
- `vp run playwright:e2e`

`vp run playwright:e2e` is an e2e suite: it starts `TerraScale.AppHost`, reads the
randomized AppHost-emitted Dashboard/Platform/Auth/TerraBase/EmailEmulator URLs, and
exercises the browser against the real local Platform/Auth/database stack. Do not add
mocked, jsdom, component-only, synthetic-cookie, or static-only tests as
Dashboard Next product proof.

There is no scheduled production-smoke Forgejo workflow. Live production
availability is verified through public health endpoints and Orchestrator
readiness evidence (see `docs/dashboard-production-ux.md`).

Do not use broad .NET test runs as the primary proof for this app. Dashboard
Next product proof is Playwright/AppHost e2e. C# tests may cover repository
policy, AppHost wiring, or Dashboard-agnostic product API contracts.

## Deleted Legacy Dashboard

The old Blazor SSR + Datastar Dashboard is deleted. Active code, docs,
workflows, AppHost wiring, Dockerfiles, and production manifests must reference
Dashboard Next only. Do not import Blazor, Datastar, or
Dashboard.Contracts code into Dashboard Next.
