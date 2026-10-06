# Dashboard Next UI Standard

Scope: UI and interaction guidance for `TerraScale.Dashboard.Next`.

Dashboard Next is a SaaS database dashboard for external customers. It should
feel like a focused operational product: dense, quiet, fast to scan, and built
for repeated database and project work. It is not a marketing site and must not
use Blazor fragments, Datastar workflows, or direct TerraBase
access.

## App Structure

Use Vinext App Router routes backed by feature slices:

| Route area | Purpose | Slice owner |
|------------|---------|-------------|
| `/login`, `/register`, `/verify-email` | Public email-only auth flows | `features/auth` |
| `/` or `/dashboard` | Signed-in overview | `features/overview` |
| `/organization` | Organization, project selection, and tenant settings entry | `features/organization` |
| `/databases` | Logical database list and create flow | `features/databases` |
| `/databases/[databaseId]` | Database detail, environments, regions, health | `features/databases` |
| `/data` | Repository and collection explorer | `features/data` |
| `/api-keys` | API key lifecycle | `features/api-keys` |
| `/access` | Members, invitations, roles | `features/access` |
| `/usage`, `/audit`, `/notifications`, `/settings`, `/profile` | Usage, audit, notifications, settings, and profile | owning feature slices |
| `/admin`, `/admin/users`, `/admin/databases`, `/admin/organizations`, `/admin/usage`, `/admin/pricing` | Owner-only global views | `features/admin` |

Route files should load session and route parameters, call slice services, and
render slice components. Business decisions and SDK orchestration belong in the
slice, not in shared route hubs.

Dashboard Next is the full-stack owner of Dashboard-specific routes, route
handlers, server actions, orchestration, and view models. Every TerraScale
product-data read and write uses typed public product APIs from the TypeScript
SDK. `TerraScale.Platform` must remain Dashboard-agnostic; Dashboard-specific API
routes such as `/api/v1/dashboard` are prohibited.

## Layout

- Use a persistent app shell with top app bar, project/database switchers,
  primary navigation, account menu, and notification entry point.
- Keep content full width inside the app shell with clear section boundaries.
  Do not center the main dashboard in a marketing-style max-width hero layout.
- Prefer tables, compact lists, segmented controls, tabs, and detail panels for
  operational data.
- Use cards only for repeated resources, dialogs, and genuinely framed tools.
  Do not nest cards inside cards.
- Empty states must offer the next concrete action, such as creating a project,
  creating a database, or inviting a teammate.
- Loading states must preserve layout dimensions so content does not jump when
  SDK data arrives.

## Tailwind Conventions

- Use Tailwind utilities for layout, spacing, typography, color, state, and
  responsive behavior.
- Keep shared design tokens in the Tailwind v4 CSS theme layer. Do not scatter
  hard-coded one-off colors across routes.
- Prefer neutral surfaces with restrained accent colors for status and actions.
  Avoid one-note purple/blue, beige, or dark-slate themes.
- Keep typography compact inside panels and controls. Do not use hero-scale text
  in dashboard surfaces.
- Use `lucide-react` icons in icon buttons and action buttons when an icon
  exists. Add accessible labels or tooltips for icon-only controls.
- Use stable dimensions for navigation items, counters, tiles, toolbar buttons,
  status chips, and data rows to prevent hover or data updates from shifting
  layout.
- Do not load Tailwind, fonts, icons, or core behavior from CDNs.

## Database UX Standards

Database screens must expose the concepts customers operate:

- Project: the billing and ownership container.
- Logical database: the customer-visible database resource.
- Environment: Development, Preview, Production.
- Region: customer-selected region intent.
- API keys and access: scoped to the correct project and database context.
- Usage and health: user-facing status without exposing internal operation
  feeds or system-event timelines.

Create database flow:

1. Name the logical database.
2. Choose project context.
3. Choose region or replication intent.
4. Confirm environments that will exist.
5. Submit through the TypeScript SDK.
6. Show success by navigating to the database detail or list with the new
   database visible.

Do not show raw TerraBase database names, physical collection partitions,
internal placement keys, operation history, system event streams, or private API
diagnostics in customer-facing pages.

## Auth Guards

- Public auth routes redirect signed-in users away from login/signup surfaces.
- Protected routes verify the session on the server and redirect unauthenticated
  users before rendering protected data.
- Client components may improve responsiveness, but authorization decisions must
  come from the server/API session check.
- Return URLs must stay same-origin and path-only.
- Expired sessions should show a clear login path without losing the intended
  destination.

## SDK Data States

Every SDK-backed view handles these states explicitly:

- Initial loading or server pending state.
- Empty state with a next action.
- Permission denied state.
- Validation error state.
- Retryable API/network error state.
- Successful loaded state.

Map API errors into concise, user-facing copy. Keep diagnostic details in logs
or authorized observability tools.

## Dotted Map Usage

Use `dotted-map` only for region selection or region visualization:

- Lazy-load the map component on routes that need it.
- Keep generated map data out of the main app shell bundle.
- Use accessible non-map controls, such as radio cards or a select, as the
  canonical input. The map is a visual selector, not the only way to choose.
- Do not replace `dotted-map` with a hand-drawn SVG world map or a heavy GIS
  library for the Dashboard region picker.
- Do not put the map inside nested decorative cards.

## Notifications and Activity

Dashboard Next may have a bounded notification center for actionable product
notifications addressed to the signed-in user. It must not add generic operation
feeds, activity feeds, system-event timelines, live status banners, or mutation
result streams that reveal internal platform activity.

## Testing Expectations

- Use `vp check`, `vp run vinext:check`, `vp run playwright:e2e`, and
  `vp run vinext:build` for app validation.
- Dashboard Next product tests are Playwright e2e tests that start AppHost and
  use the real Platform/Auth/TerraBase/EmailEmulator stack.
- SDK flows need integration or end-to-end coverage against real public API
  contracts, env-gated when credentials or mutable infrastructure are required.
- Do not mock TerraScale Platform API behavior as the main proof for auth, project,
  database, or API-key flows.
- Production smoke must verify public routes, assets, auth when secrets exist,
  protected rendering, and absence of browser console/page errors.

## Deleted Legacy Dashboard

The old Blazor Dashboard is deleted. Do not copy Datastar attributes, Razor
component patterns client code, Dashboard.Contracts DTOs, or
Blazor-specific CSS into Dashboard Next. Current cutover guardrails are tracked
in `docs/dashboard-next-parity.md`.
