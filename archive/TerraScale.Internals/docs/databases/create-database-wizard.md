# Dashboard Next Create Database Flow

Scope: the Dashboard Next logical database creation flow.

Dashboard Next creates logical databases through the TerraScale TypeScript SDK
and public REST API contracts. It never creates TerraBase physical databases
directly and never exposes physical database or partition names to customers.

## Product Model

- A project owns one physical TerraBase database, named internally by
  `TerraScale.Platform`.
- Dashboard databases are logical databases represented by public ULID IDs.
- Each logical database has Development, Preview, and Production environments.
- Regions control placement/replication intent. Only GRU has real production
  infrastructure today; future region codes still belong in public region
  contracts rather than Dashboard-only constants.

## UI Flow

The create flow is a routed page, typically `/databases/new`, because it needs
multiple steps and a shareable URL.

1. Load the selected project through the SDK.
2. Load the public region catalog and any availability state through the SDK.
3. Collect name, description, environment defaults, and selected regions.
4. Show an accessible region selector with a lazy `dotted-map` visualization.
5. Submit through the SDK to the public create-database API.
6. Navigate to the created database detail page.

## Region Map

Dashboard Next uses the `dotted-map` npm package from the
`TerraScale.Dashboard` sibling repository's `package.json`. Do not vendor runtime
copies into `public/`.

Map components should be route-lazy and typed:

- selected region
- available region
- disabled or future region
- degraded region
- replication/placement summary

The map is visual support only. Every region choice must also be available
through keyboard-accessible controls.

## API Boundary

The Dashboard request carries public values only:

- project ID as `Ulid`
- database name and optional description
- selected region codes from the public region catalog
- environment options exposed by public contracts

`TerraScale.Platform` owns physical database provisioning, virtual environment
partitions, replication factor, placement, and storage details.

## Verification

Create-database work should be covered by Playwright/AppHost e2e:

- unauthenticated users redirect before protected data renders
- existing projects load through the SDK
- invalid input renders validation messages
- successful create returns a public database ID and navigates to detail
- selected regions persist in the created resource
