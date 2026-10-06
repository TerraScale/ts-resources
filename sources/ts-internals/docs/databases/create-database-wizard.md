# Dashboard create database flow

Scope: the Dashboard database creation workflow.

Dashboard creates databases through the TerraScale TypeScript SDK
and public REST API contracts. It never creates TerraBase physical databases
directly and never exposes physical database or partition names to customers.

## Product model

- A Project may own many native TerraBase databases through
  `TerraScale.Database`.
- A small database starts as one SQLite file and splits by key range only after
  a D-28 trigger. Dashboard does not choose a shard count.
- The owner selects one to three active regions from GRU, SFO, and FRA.
- Every selected region stores every key-range shard and accepts writes.
- Production uses RF=2 per selected Region. The UI explains that
  `RegionalDurable` avoids WAN latency but accepts a complete-Region loss
  window.
- Litestream backup and PITR are automatic. The plan sets the retention window.

## UI flow

The create flow is a routed page, typically `/databases/new`, because it needs
multiple steps and a shareable URL.

1. Load the selected project through the SDK.
2. Load the public region catalog and any availability state through the SDK.
3. Collect name, description, selected active regions, and durability
   preference. Display the plan's PITR window.
4. Show an accessible region selector with a lazy `dotted-map` visualization.
5. Submit through the SDK to the public create-database API.
6. Navigate to the created database detail page.

## Region map

Dashboard uses the `dotted-map` npm package from the
`ts-dashboard` sibling repository's `package.json`. Do not vendor runtime
copies into `public/`.

Map components should be route-lazy and typed:

- selected region
- available region
- disabled or future region
- degraded region
- active write and placement summary

The map is visual support only. Every region choice must also be available
through keyboard-accessible controls.

## API boundary

The Dashboard request carries public values only:

- project ID as `Ulid`
- database name and optional description
- selected region codes from the public region catalog
- supported durability options

Dashboard owns the workflow and its ordinary public route handling.
`TerraScale.Database` owns database admission and the public create contract.
TerraBase and Orchestrator own physical placement. Dashboard cannot select
members, construct shard files, choose replication factor, or use a private
provisioning route.

## Verification

Create-database work should be covered by Playwright e2e through the DevHost-managed lab:

- unauthenticated users redirect before protected data renders
- existing projects load through the SDK
- invalid input renders validation messages
- successful create returns a public database ID and navigates to detail
- selected regions and durability persist
- a Region outside the catalog fails before provisioning
- the plan's PITR window is displayed
- one through three launch regions can be selected
- the first acknowledged write is available within the five-second creation
  SLO
