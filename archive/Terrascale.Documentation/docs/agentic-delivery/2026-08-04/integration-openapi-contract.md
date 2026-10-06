# OpenAPI contract integration record

## Result

The TypeScript SDK manifest has 149 routes, while the checked Documentation OpenAPI snapshot covers 147. The drift command correctly fails rather than silently accepting the mismatch.

The two missing snapshot operations are:

- `GET /api/v1/organizations/{organizationId}/billing/access`
- `PUT /api/v1/organizations/{organizationId}/billing/access/{userId}`

They correspond to `billing.access.list` and `billing.access.set` in `TerraScale.TypeScript/sdk-route-manifest.json`. Platform has matching billing-access endpoints, so the authoritative Documentation snapshot must be refreshed from the approved API source and reviewed before SDK publication can be considered contract-clean.

## Dependency and evidence

The authoritative dependency is `Terrascale.Documentation/public/openapi/server.openapi.json`, not an SDK-local approximation. The drift command records that snapshot's checkout provenance and last modifying commit, allowing the release workflow to diagnose a stale snapshot without substituting a mutable branch guess.

Observed command result: `npm run check:openapi-drift -- ../Terrascale.Documentation/public/openapi/server.openapi.json sdk-route-manifest.json` exited with drift at `147/149`. Until the snapshot contains both operations and the command succeeds, the remaining blocker is authoritative snapshot refresh.
