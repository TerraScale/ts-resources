# ts-atlas — TerraScale edge Worker

This Cloudflare Worker serves Atlas discovery on `atlas.terrascale.tech` and
regional reverse proxies on `auth.terrascale.tech` and `api.terrascale.tech`.
Atlas serves `GET /v1/discovery`, `GET /v1/resolve`, `GET /v1/keys`, and the
orchestrator's signed `POST /v1/publish`. `GET /api/v1/regions` keeps its
pre-v1 catalog shape, projected from the topology, for ts-status. `GET /api/v1/auth/discovery`
remains for older auth clients; new clients use `regions[].auth`.
The API reference is at `/`, `/docs`, and `/openapi.json`.

## Atlas discovery v1

Atlas ranks published regions for the client, resolves a project's region,
and signs a 600 s session pin. The orchestrator publishes topology and
project placements. Production TerraBase holds the authoritative documents;
KV and isolate memory hold cached copies. See [the v1 contract](docs/discovery-v1.md)
for request and response shapes, storage, and failure behavior.

| Route | Purpose | Auth |
| --- | --- | --- |
| `GET /v1/discovery[?fresh=1]` | Every region ranked for this client, the closest usable one, the service catalog | none |
| `GET /v1/resolve?project=<id>[&database=<name>][&fresh=1]` | The project's region and a signed session pin | none |
| `GET /v1/keys` | JWKS that verifies session pins | none |
| `POST /v1/publish` | The orchestrator's signed write of regions and placements | ES256 signature |
| `GET /api/v1/regions` | Deprecated: the pre-v1 catalog shape (`code`, `hosts`, `available`, ISO `updated`) projected from the topology, until ts-status and the SDKs move | none |
| `GET /api/v1/auth/discovery` | Deprecated: use `regions[].auth` | none |

### Consuming Atlas from other repositories

- **SDKs (TS-507):** Default to `https://atlas.terrascale.tech`, resolve per
  project and optional database, verify the pin using `/v1/keys`, and send
  `X-TerraScale-Region-Pin: <region>` to the returned `api`. Re-resolve with
  `fresh=1` on pin expiry, `421`, or redirect. Use discovery's `closest` for
  project-less calls. A configured static endpoint bypasses Atlas.
- **TerraBase (TS-499):** Use the published region id for `--region` and
  answer `421` with `X-TerraBase-Region` for a mismatched pin.
- **ts-orchestrator (TS-506):** Probe each region's `/readyz`, publish topology
  and placements through `/v1/publish`, and increase each document's `updated`.
- **Dashboard, status, docs, and CLI:** Read regions and the service catalog
  from `/v1/discovery` and validate the response against the JSON Schema.

On the auth hostname, the Worker selects a configured `AUTH_ORIGINS` entry by
client distance. Failed origins are ejected for 10 s. Safe reads can fail over;
mutations go once to an origin whose `/readyz` recently answered `200`.
Anonymous public GETs can use the edge cache. The proxy forwards cookies,
redirects, and credential headers to the origin, after removing hop-by-hop
headers. Auth routing does not depend on TerraBase region health.

On the API hostname, the Worker ranks configured `API_ORIGINS` by
`X-TerraScale-Region-Rtt`, then client distance, then region code; ejected
origins sort last. It does not read Atlas KV or cache TerraBase responses.
Safe reads can fail over. Mutations go once to an origin whose public
`/readyz` answered `200`. `GET /` and `HEAD /` redirect to `/v1/docs` with
the query string preserved; every other path is forwarded unchanged. The
exact regional root `https://<region>.api.terrascale.tech/` redirects to
`/v1/docs` without contacting the origin. Other regional HTTPS paths go
straight to TerraBase.

Publishing requires `ATLAS_STORE_URL`, the `ATLAS_STORE_KEY` secret, and
`PUBLISH_KEYS` containing the orchestrator's public ES256 keys. Pin signing
requires the `PIN_SIGNING_KEY` secret. `POST /v1/publish` writes each document
to TerraBase with a conditional write before updating its KV copy. Atlas
reads serve a cached copy when TerraBase is unavailable; without any copy,
discovery answers `503 discovery_unavailable`. The v1 contract gives the
signature format and retry rules. `STALE_AFTER_S` controls when published
region health becomes unknown (default 60 s).

- Design and failure modes: [docs/design.md](docs/design.md)
- Signed edge contract release: [docs/release.md](docs/release.md)

## Layout

```text
src/
  index.ts             Host gate, proxies, Atlas routes
  api-docs.ts          Scalar reference and OpenAPI document
  discovery.ts         GET /v1/discovery, /v1/resolve, /v1/keys
  contract.ts          topology and placement validation
  store.ts             TerraBase authority, KV and isolate caches
  pin.ts               session pins and publisher signatures
  publish.ts           POST /v1/publish
  regional-proxy.ts    auth and API proxies; auth discovery
  edge-cache.ts        public auth response cache
  isolate-cache.ts     bounded isolate memory cache
  geo.ts               locations and great-circle distance
  headers.ts           client location and RTT inputs
  analytics.ts         Analytics Engine rows
  cors.ts              Atlas CORS and preflights
  error.ts             typed error envelope
  env.ts               bindings, vars, secrets, dev mode
contracts/v1/
  atlas-discovery.schema.json  Atlas discovery JSON Schema
  openapi.json         Worker OpenAPI contract
docs/discovery-v1.md   Atlas discovery v1 contract
scripts/terrabase.mjs  pinned TerraBase integration runner
scripts/terrabase-release.json  the pinned TerraBase release (tag, asset, SHA-256)
test/
  discovery.test.ts    discovery, resolve, keys
  publish.test.ts      signed publishing and validation
  regional-proxy.test.ts  auth and API routing
  analytics.test.ts    route and hostname dimensions
  prod.test.ts         production Host gate and route surface
  terrabase/storage.test.ts  real TerraBase storage integration
wrangler.toml          routes, bindings, origin maps
vitest.config.ts       workerd dev-mode tests and throwaway keys
vitest.prod.config.ts  workerd production-mode tests
vitest.terrabase.config.ts  plain Node TerraBase lane
```

## Local development

`npm run dev` starts `wrangler dev --env dev --port 7000`. `DEV_ORIGINS`
enables dev mode, and `AUTH_ORIGINS` and `API_ORIGINS` select loopback proxy
origins. Local publishing needs `PUBLISH_KEYS`, `ATLAS_STORE_URL`,
`ATLAS_STORE_KEY`, and a local TerraBase. Resolving needs
`PIN_SIGNING_KEY`.

## Benchmark

`npm run bench` measures Worker latency against simulated regional auth
origins. `--root <checkout>` compares another checkout with the same harness;
`--only <scenario>` runs one route. An Atlas route runs only when the checkout
declares it in `contracts/v1/route-source.json`; a declared route that answers
anything unexpected, 404 included, fails the run.

## Verification set

```bash
nice -n 19 npm ci
nice -n 19 npm run test:config
nice -n 19 npm run typecheck
nice -n 19 npm test
nice -n 19 npm run test:terrabase
nice -n 19 npm exec -- wrangler deploy --dry-run
nice -n 19 npm run test:attestation
```

CI runs these checks at normal CPU priority. The TerraBase lane runs the
real pinned release binary through `scripts/terrabase.mjs`.

Production uses custom domains for Atlas, auth, and the API router.
`AUTH_ORIGINS` and `API_ORIGINS` list the regional upstreams. The deployment
controller provisions regional DNS; Wrangler provisions the Worker domains
and the narrow regional redirect routes. `npm run deploy:production` checks
the production config before deploying, and refuses it until `wrangler.toml`
sets `ATLAS_STORE_URL` and `PUBLISH_KEYS`. The orchestrator publishes through
`POST /v1/publish`. Until TS-506 lands and the store, publisher, and pin
secrets are provisioned, `/v1/discovery` answers `503` because no topology
copy exists.

Language: TypeScript. On `main`, CI publishes the signed edge contract bundle
([docs/release.md](docs/release.md)).
