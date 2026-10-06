# Dashboard Next Admin

Scope: owner-only Admin behavior in `TerraScale.Dashboard.Next`.

Dashboard Next Admin is the owner view of TerraScale platform state. It is not a
second standalone app. All Admin routes, route handlers, orchestration, and view
logic live under Dashboard Next `/admin`. They consume typed, role-protected,
Dashboard-agnostic product administration APIs through `@terrascale/sdk/admin`.

## Security Boundary

- Generic owner permissions and product-data authorization are enforced by
  `TerraScale.Platform`, not by hidden navigation, client-side checks, visible role
  labels, or route obscurity. The API must not contain Dashboard routes or logic.
- `mariogk@terrascale.tech` is the built-in owner email. Configured owner
  email/user-id allowlists plus backend owner/admin roles or permissions are
  supplemental gates.
- Non-owner sessions must not receive admin data or perform admin actions.
- Admin routes in Dashboard Next must render denied states from API responses
  without preloading cross-tenant data.

## Transport

Dashboard Next Admin uses the same rule as the rest of Dashboard Next:

Dashboard Next route handler or feature code -> `@terrascale/sdk/admin` ->
public, Dashboard-agnostic product contract -> `TerraScale.Platform`.

Do not use `TerraScale.Dashboard.Contracts`, direct storage,
TerraBase clients, private API shortcuts, Blazor components, Razor components,
or Datastar fragments.

## Admin Surface

The Admin area is a single owner-only section under `/admin` with route-backed
tabs. Tabs are pages, not hidden client-side panels.

Expected tab set:

| Tab | Route | Purpose |
|---|---|---|
| Overview | `/admin` | Platform totals and owner-critical health |
| Users | `/admin/users` | Lookup, create, enable/disable, delete, roles, support notes |
| Organizations | `/admin/organizations` | Tenant and project inventory |
| Databases | `/admin/databases` | Logical databases, environments, regions, provisioning state |
| Usage | `/admin/usage` | Platform usage and top consumers |
| Billing | `/admin/billing` | Plans, subscriptions, invoices, payments |
| API Keys | `/admin/api-keys` | Keys, scopes, expiry, revocation |
| Access | `/admin/access` | Invitations, roles, SSO/SCIM, M2M clients |
| Backups | `/admin/backups` | Policies, jobs, restore status |
| Audit | `/admin/audit` | Owner-visible sensitive/admin action history |
| Notifications | `/admin/notifications` | Notification delivery health and owner actions |
| Infrastructure | `/admin/infrastructure` | Product health summary that complements Grafana |

## Adding Admin Functionality

Add admin functionality in one vertical change:

1. Implement the Dashboard route handler, orchestration, and UI in the owning
   Dashboard Next feature slice.
2. Compose existing typed `@terrascale/sdk/admin` operations locally.
3. Only when a reusable platform capability is missing, add a
   Dashboard-agnostic public API contract with server-side owner/admin
   enforcement and expose it through `@terrascale/sdk/admin`.
4. Add Playwright/AppHost coverage for owner access and non-owner denial.

## Customer-Facing Boundary

Customer-facing Dashboard pages must not show operation feeds, activity feeds,
system-event timelines, live status banners, or generic mutation-result streams.
Operational details belong in owner-only Admin or observability tools. The
bounded user notification center remains the customer-facing notification
channel.
