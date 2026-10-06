# ts-atlas design — the metadata, auth, and API router edge Worker in full

## 1. Responsibilities and non-goals

`ts-atlas` serves Atlas discovery v1 on `atlas.terrascale.tech`:
`GET /v1/discovery`, `GET /v1/resolve`, `GET /v1/keys`, and the
orchestrator's ES256-signed `POST /v1/publish`. `GET /api/v1/regions` keeps
its pre-v1 catalog shape, projected from the topology, for ts-status. `GET /api/v1/auth/discovery`
remains for older auth clients; `regions[].auth` is the v1 replacement.
The Worker also serves the Scalar API reference at `/` and `/docs` and its
OpenAPI document at `/openapi.json`.

The same Worker proxies `auth.terrascale.tech` to configured `AUTH_ORIGINS`
and `api.terrascale.tech` to configured `API_ORIGINS` (§18). Auth has a cache
for anonymous public responses; API responses are not edge cached. SDK data
requests use the regional `api` URL returned by `/v1/resolve`.

Atlas does not validate customer API keys or JWTs, store customer data, or
proxy SDK data requests on their regional path. Atlas read routes never read
`Authorization`. The publish route verifies an orchestrator signature.
TerraBase handles tenant authorization. See [Atlas discovery v1](discovery-v1.md)
for the shared contract.

## 2. Hostnames and routes

| Hostname | Handled by | Purpose |
| --- | --- | --- |
| `atlas.terrascale.tech` | ts-atlas custom domain | Discovery v1, deprecated pre-v1 routes, API reference |
| `auth.terrascale.tech` | ts-atlas custom domain | Regional ts-auth reverse proxy |
| `api.terrascale.tech` | ts-atlas custom domain | Regional TerraBase reverse proxy |
| `<region>.api.terrascale.tech` | Regional TerraBase | SDK data path; Worker handles HTTP upgrade and exact HTTPS root redirect only |
| `<region>.auth.terrascale.tech` | Regional ts-auth | Auth proxy upstream |

Atlas routes and their methods are listed in [the v1 contract](discovery-v1.md#routes).
On the atlas host, other paths answer `404`; wrong methods on known routes
answer `405`. The deployment controller provisions regional DNS. Wrangler
provisions the three Worker custom domains and narrow regional API routes.

## 3. Inputs available to the Worker

`request.cf` coordinates locate the client; the continent gives a fallback
location. Without a location, discovery preserves publication order within
each health group. `X-TerraScale-Client-Loc` is accepted only when `request.cf`
is absent, for service-binding callers. `X-TerraScale-Debug-Loc` works only in
dev mode. `X-TerraScale-Region-Rtt` affects the API proxy's ranking (§18),
not Atlas discovery's ranking.

The orchestrator publishes one topology and project placements through
`POST /v1/publish`. The authoritative documents live in TerraBase. `REGIONS`
KV key `topology` and `PLACEMENT` KV keys `project:<id>` hold
`{at, version, doc}` copies. Isolate memory holds reads for 5 s. §6 covers
the read path and [the v1 contract](discovery-v1.md#storage) defines the
documents.

`ATLAS_STORE_URL` is the TerraBase database URL;
`ATLAS_STORE_KEY` is its secret API key. `PUBLISH_KEYS` contains up to four
public P-256 publisher keys; `PIN_SIGNING_KEY` is the private P-256 pin key.
`STALE_AFTER_S` defaults to 60. `DEV_ORIGINS` enables development mode;
`AUTH_ORIGINS` and `API_ORIGINS` configure the proxies. `VERSION` identifies
the deployed release. Production origin maps must contain the expected HTTPS
regional hosts; dev maps may use loopback origins.

## 4. Request flow

```text
fetch(request):
  unknown production Host                    → 421 misdirected_request
  auth.terrascale.tech                       → auth proxy (§18)
  api.terrascale.tech GET/HEAD /             → 302 /v1/docs, preserving query
  api.terrascale.tech otherwise              → API proxy (§18)
  atlas /, /docs, /openapi.json GET          → Scalar or OpenAPI document
  atlas /v1/discovery GET                    → ranked topology and services (§5)
  atlas /api/v1/regions GET                  → same discovery response (§5)
  atlas /v1/resolve GET                      → placement and signed pin (§5)
  atlas /v1/keys GET                         → pin verification JWKS (§16)
  atlas /api/v1/auth/discovery GET           → configured auth origins by distance
  atlas /v1/publish POST                     → verify, validate, publish (§17)
  known route with wrong method             → 405 method_not_allowed
  Atlas read route OPTIONS                   → local CORS preflight, 204 or 403
  other atlas path or method                 → 404 not_found
```

The read routes send `Cache-Control: no-store`, except `/v1/keys`, which
sends `public, max-age=300`. Errors have `{error:{code,message,fix}}`.
Atlas does not forward discovery calls to a member. Safe proxy reads can
fail over; proxy mutations go to one ready origin (§18).

## 5. Discovery and resolve

`GET /v1/discovery` ranks published regions by health (`ok`, `unknown`,
`down`), client distance, then publication order. `closest` is the first
region that is not down. Health becomes `unknown` when the topology is older
than `STALE_AFTER_S`; a stale health verdict does not hide a region.
Deprecated `GET /api/v1/regions` projects the topology into the pre-v1
catalog shape: `regions[].code` (the API host's first label uppercased),
`name`, `country`, `latitude`, `longitude`, `available` (health `ok`), `hosts`
(code to API host), and an ISO `updated`, with `private, max-age=60`. A
topology in which two regions would share a code answers
`503 region_catalog_unavailable` rather than an ambiguous catalog.

`GET /v1/resolve?project=<id>[&database=<name>][&fresh=1]` reads the project
placement. A database override wins over the project default. An unplaced
project uses the closest usable region; a placed region stays selected even
when down. The response includes its API and auth origins, placement state,
health, and a signed 600 s pin. Malformed parameters answer `400
invalid_project` or `400 invalid_database`. A missing topology or placement
copy when TerraBase is unavailable answers `503 discovery_unavailable`; no
usable region answers `503 no_eligible_region`. See [the v1 contract](discovery-v1.md)
for the response fields and examples.

## 6. Storage

Published topology and placements are authoritative in production TerraBase:
organization `terrascale-internal`, project `atlas`, database `atlas`,
collection `atlas`. Each key maps to a deterministic lowercase UUID.
Publishing checks `updated`, writes with `If-Match` on the current version
(or `If-None-Match: *` for a new document), and retries a `412` conflict up
to four attempts. KV is updated only after TerraBase accepts the write.

Reads use 5 s isolate memory, then the KV copies named in §3, then
TerraBase. A KV copy younger than 60 s is served directly. `fresh=1` accepts
only a copy younger than 5 s before reading TerraBase. The TerraBase request
times out after 2.5 s. If it fails, Atlas serves its last cached copy with
`stale: true`; with no copy it answers `503`. KV has no conditional writes,
so TerraBase refresh bounds a raced KV copy to 60 s on normal reads and 5 s
on fresh reads. See [storage in the v1 contract](discovery-v1.md#storage).

## 7. Placement changes

The orchestrator publishes project placements through `/v1/publish` with
monotonic `updated` timestamps. Atlas does not infer or move placement.
A placed region stays in `/v1/resolve` even if its health is down.

An SDK re-resolves with `fresh=1` when its 600 s pin expires, TerraBase
answers `421` with `X-TerraBase-Region`, or the request is redirected.
Normal KV copies are bounded by 60 s; a fresh resolve rechecks after 5 s.
A still-valid pin can be used while Atlas is unreachable.

## 8. Failure modes

| Failure | Behaviour |
| --- | --- |
| TerraBase unavailable or times out after 2.5 s | Serve a cached topology or placement with `stale: true`; without a copy, `503 discovery_unavailable`. |
| Topology older than `STALE_AFTER_S` | Show every region's health as `unknown`; retain placement. |
| No usable region or placed region absent from topology | `503 no_eligible_region`. |
| Pin signing key missing | `503 pin_unavailable` on resolve and keys. |
| Store or publisher keys missing | `503 publish_disabled`; a failed store write answers `502 store_unavailable`. |
| Proxy origin fails | Eject it for 10 s; safe reads try another origin, mutations are not retried (§18). |

## 9. Security

- `ATLAS_STORE_KEY` and `PIN_SIGNING_KEY` are secrets. `PUBLISH_KEYS` holds
  public keys; `ATLAS_STORE_URL` and `STALE_AFTER_S` are vars. Atlas read
  routes never inspect `Authorization`.
- `/v1/publish` checks an ES256 signature over the exact body with
  `X-Atlas-Timestamp` and `X-Atlas-Signature`. The timestamp must be within
  300 s. Bodies are limited to 128 KiB and 64 placements; the whole request
  is validated before any write.
- Published production URLs must be HTTPS under `terrascale.tech`, without
  credentials, port, query, or fragment. API and auth URLs are bare origins.
  Dev mode also accepts loopback URLs.
- The auth and API proxies forward credentials to their origins without
  logging them. Auth caches only anonymous public GET responses. API never
  caches tenant responses. Atlas CORS applies only to Atlas routes.
- The production Host gate rejects other hosts with `421`.

## 10. Observability

Workers Analytics Engine (`ANALYTICS`, dataset `proxy_decisions`) records one
row per request. Reasons are `discovery`, `resolve`, `keys`,
`auth-discovery`, `publish`, `docs`, `auth-proxy`, `auth-cache`, `api-proxy`,
`host`, and `not-found`. `auth-cache` means an auth response came from the
edge cache. Rows include colo, serving region, status, elapsed time, and a
bounded host label (`atlas|auth|api|gru|sfo|fra|dashboard|other`), and
`kv_hit`: for discovery and resolve, whether the answer needed no TerraBase
read (`X-TerraScale-Cache: HIT`). The old reactive sync.api Snippet was
removed.

## 11. Local development (`terrascale dev`)

`npm run dev` runs `wrangler dev --env dev --port 7000`. `DEV_ORIGINS`
enables dev mode and permits loopback URLs in published topology.
`AUTH_ORIGINS` and `API_ORIGINS` point the proxies to local services.
Local publishing needs `PUBLISH_KEYS`, `ATLAS_STORE_URL`, `ATLAS_STORE_KEY`,
and a local TerraBase. Resolving needs `PIN_SIGNING_KEY`; a missing key
returns `503 pin_unavailable`. The dev KV bindings cache published documents.
`X-TerraScale-Debug-Loc` is honored only when dev mode is active.

## 12. Tests

- `test/discovery.test.ts`, `test/publish.test.ts`,
  `test/regional-proxy.test.ts`, and `test/analytics.test.ts` run in workerd
  through `vitest.config.ts`. That config enables dev mode and generates
  throwaway publisher and pin keys.
- `test/prod.test.ts` runs in workerd through `vitest.prod.config.ts`, with
  production Host gating and without `DEV_ORIGINS`.
- `test/terrabase/storage.test.ts` runs through
  `vitest.terrabase.config.ts` in plain Node. `npm run test:terrabase`
  starts the real pinned TerraBase release binary through
  `scripts/terrabase.mjs`; it does not use a fake server.
- `bench/worker/bench.mjs` (`npm run bench`, outside CI) measures Worker
  latency against simulated regional auth origins.

## 13. Deployment

`npm run deploy:production` runs the production config gate
(`scripts/validate-production-config.mjs`) and then `wrangler deploy`. The
gate refuses a `dev`/`test`/`local` `VERSION`, placeholder or duplicate KV
namespace IDs, a missing `ANALYTICS` → `proxy_decisions` binding, a missing
or non-HTTPS-regional `AUTH_ORIGINS` or `API_ORIGINS` map, and any service
binding. The custom domains, the production `REGIONS`/`PLACEMENT` namespace
IDs, and the analytics dataset are checked into `wrangler.toml`; Wrangler
provisions the three custom domains and their proxied DNS with the deploy.
The orchestrator owns everything else in the zone, including the regional
auth and TerraBase API host records. This Worker
declares no service bindings and dispatches to nothing. CI validates the
bundle with `wrangler deploy --dry-run` but does not deploy.

## 15. Phase 2 — edge cache (D-55, M2-4)

Not built. Constraints recorded so the design is not re-litigated:
only public-rule collections with cache enabled participate; private reads
(`Cache-Control: private`) are never cached; invalidation must arrive within
one group-commit wave; the signal is batched **per database per wave** and
must fit the KV write budget or use Cache API purge instead — the M2-4 issue
chooses with measurements, not opinions.

## 16. Session pins

`GET /v1/resolve` signs a compact ES256 JWS with `iss`, `project`, optional
`database`, `region`, `api`, `iat`, and `exp`. The pin lasts 600 s. Its `kid`
is the RFC 7638 thumbprint of the public key; `GET /v1/keys` serves the
verification JWKS with `Cache-Control: public, max-age=300`. An SDK verifies
the pin, sends `X-TerraScale-Region-Pin: <region>` to TerraBase, and fetches
keys again on an unknown `kid`. Key rotation means resolving again. See
[session pins in the v1 contract](discovery-v1.md#session-pins).

## 17. Publishing

`POST /v1/publish` accepts `{topology?, placements?}` from the orchestrator.
It verifies `X-Atlas-Timestamp` and `X-Atlas-Signature` against up to four
public ES256 keys in `PUBLISH_KEYS`. The signature covers
`atlas-publish-v1\n<timestamp>\n<body>`. The timestamp skew limit is 300 s;
the request body limit is 128 KiB and the placement limit is 64 per request.
Malformed or expired signature headers are refused before the body is read,
and a body that has not arrived within 10 s answers `408 body_timeout`.
Validation finishes before writing, and the topology must list the
`terrabase`, `auth`, `dashboard`, `status`, and `docs` services. An older
`updated`, or a different document with the same `updated`, is `stale`, so a
replayed signed body cannot roll a newer one back; the identical document is
an idempotent write. `updated` may be at most 300 s ahead of the Worker clock
(`400 future_updated`), so a future-dated document cannot block later
corrections. TerraBase accepts each conditional write before
KV is updated. Earlier documents may have landed if a later write fails, so
`502 store_unavailable` calls for retrying the request. See
[publishing in the v1 contract](discovery-v1.md#publishing-ts-orchestrator-ts-506).

## 18. Regional reverse proxies (`auth.` and `api.terrascale.tech`)

One proxy (`src/regional-proxy.ts`) serves both hostnames from separate
configured origin maps. Auth uses `AUTH_ORIGINS` and can cache anonymous
public GET responses; API uses `API_ORIGINS` and never edge caches TerraBase
answers. The proxies forward `X-TerraScale-Auth-Region` or
`X-TerraScale-Api-Region` to the selected origin. Responses carry
`X-TerraScale-Route-Mode` and `X-TerraScale-Serving-Region`.

The auth proxy ranks origins by client distance and region code. The API
proxy ranks its configured origins by measured `X-TerraScale-Region-Rtt`,
then client distance using the launch coordinates, then region code.
Neither proxy reads Atlas KV topology or placement. An origin ejected by a
network error, header timeout, `502`/`503`/`504`, or Cloudflare
`520`–`526`/`530` sorts last for 10 s. An expired ejection restores its
normal rank. A missing or invalid origin map answers `503
<host>_proxy_unconfigured`.

Safe `GET`, `HEAD`, and `OPTIONS` requests try ranked origins in turn. Each
attempt except the last has a 5 s response-header deadline. Mutations go
once to the first origin with a recent public `/readyz` `200` (TerraBase's
public readiness route, terrabase#16). A readiness result younger than 5 s
is reused; one younger than 30 s is reused while a background probe runs.
Older or ejected origins are probed before a mutation, with a 1.5 s timeout.
No ready origin answers `503 <host>_no_ready_replica`. When every attempt
fails, the proxy answers `502 <host>_upstream_unavailable`; a final
Cloudflare origin error is a typed `502` for the API proxy.

On `api.terrascale.tech`, `GET /` and `HEAD /` return a local `302` to
`/v1/docs`, preserving the query. Every path is forwarded unchanged; the
Rust-era fallback between `/docs` and `/v1/docs` is gone, because no C#
TerraBase build serves `/docs`. The exact regional root
`https://<region>.api.terrascale.tech/` redirects to `/v1/docs` without
contacting the origin. The regional HTTP wildcard redirects to HTTPS with
`301`; other regional HTTPS requests go straight to TerraBase.

The Worker strips hop-by-hop headers, sets forwarded host, protocol, client
IP, and region, and passes other request and response headers through.
Auth caches only anonymous GET `200` responses marked public with a positive
lifetime, no cookie, and no `Vary` except `Accept-Encoding`. Its isolate
memory cache sits in front of the colo Cache API. API responses are tenant
data and are never stored at the edge.
