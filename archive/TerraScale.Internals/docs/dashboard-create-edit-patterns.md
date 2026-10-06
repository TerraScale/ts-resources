# Dashboard Next Create/Edit UX

Scope: create and edit flows in `TerraScale.Dashboard.Next`.

Dashboard Next is a Vinext/VitePlus/React/Tailwind app. Create/edit flows use
route-backed feature slices, the TerraScale TypeScript SDK, and public REST
contracts. Do not copy old Blazor, Razor, Datastar, or
`TerraScale.Dashboard.Contracts` patterns into Dashboard Next.

## Surface Rule

| Surface | Use when | Examples |
|---|---|---|
| Dialog | The object fits one screen, one submit, and simple validation. | API key, invitation, team member, webhook endpoint, project rename. |
| Page | The flow has multiple steps, grouped sections, or benefits from a URL. | Create database, SSO/SCIM setup, complex admin user management. |

Create and edit for the same object should use the same surface unless the edit
flow is materially more complex.

## Dialog Pattern

- Use a route-owned React component with accessible `role="dialog"` semantics.
- Use lucide icons for icon buttons and clear labels/tooltips.
- Keep form state local to the route or feature component.
- Submit through a route action or SDK-backed feature service.
- On success, refresh the owning route data or navigate to the updated resource.
- On validation error, render field-level errors and preserve user input.

Do not add a second browser transport for a feature. Compose typed SDK methods
inside the owning Dashboard feature slice. Add public API and SDK support only
for a reusable, Dashboard-agnostic product capability.

## Page Pattern

Use a dedicated route when the user needs space, steps, or history:

- `/databases/new`
- `/databases/[databaseId]/edit`
- `/settings/sso/new`
- `/admin/users/[userId]`

Page flows should include a clear back path, loading state, validation state,
denied state, retryable error state, and success navigation. Route guards must
validate session state server-side before protected data renders.

## Data Boundary

All create/edit calls flow through:

Dashboard Next route/action -> owning feature slice -> typed TerraScale
TypeScript SDK method -> public Dashboard-agnostic product endpoint ->
`TerraScale.Platform`.

Never call TerraBase, private API endpoints, old Dashboard contracts,
raw `fetch`, or raw storage from Dashboard Next. All Dashboard-specific route
handlers and orchestration stay in Dashboard Next; `/api/v1/dashboard` and other
Dashboard-specific API routes are prohibited.

## Testing

Every new create/edit surface needs Playwright coverage through AppHost when it
is product behavior. Tests must use the real Platform/Auth/TerraBase stack and must
not use mocked, jsdom, component-only, or synthetic-cookie substitutes.
