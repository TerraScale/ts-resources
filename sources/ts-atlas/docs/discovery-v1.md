# Atlas discovery v1

Atlas (`https://atlas.terrascale.tech`) is TerraScale's region-discovery
layer. It tells an SDK which region is closest, where a project's database
lives, and which region to pin for the session. It also lists every
TerraScale service. SDKs, TerraBase, ts-orchestrator, and every other
TerraScale project build on this contract.

Machine-readable form: [`contracts/v1/atlas-discovery.schema.json`](../contracts/v1/atlas-discovery.schema.json)
(JSON Schema 2020-12) and [`contracts/v1/openapi.json`](../contracts/v1/openapi.json)
(OpenAPI 3.1, the same definitions under `components.schemas`). Both ship in
the signed edge contract release ([release.md](release.md)).

## Routes

| Route | Purpose | Auth |
| --- | --- | --- |
| `GET /v1/discovery[?fresh=1]` | Every region ranked for this client, the closest usable one, the service catalog | none |
| `GET /v1/resolve?project=<id>[&database=<name>][&fresh=1]` | The project's region and a signed session pin | none |
| `GET /v1/keys` | JWKS that verifies session pins | none |
| `POST /v1/publish` | The orchestrator's signed write of regions and placements | ES256 signature |
| `GET /api/v1/regions` | Deprecated: the pre-v1 catalog shape (`code`, `hosts`, `available`, ISO `updated`) projected from the topology, until ts-status and the SDKs move | none |
| `GET /api/v1/auth/discovery` | Deprecated: use `regions[].auth` | none |

Read routes answer `Cache-Control: no-store` (`/v1/keys`: `public,
max-age=300`), wildcard CORS, and local `OPTIONS` preflights. Discovery and
resolve add `X-TerraScale-Cache: HIT` when no TerraBase read was needed
(isolate memory or KV), else `MISS`. Errors use the envelope
`{"error":{"code","message","fix"}}`.

### `GET /v1/discovery`

```json
{
  "v": 1,
  "updated": 1791159807,
  "stale": false,
  "closest": "gru-1",
  "regions": [
    { "id": "gru-1", "name": "São Paulo", "country": "BR", "lat": -23.43, "lon": -46.47,
      "api": "https://gru.api.terrascale.tech", "auth": "https://gru.auth.terrascale.tech",
      "health": "ok", "distanceKm": 12 }
  ],
  "services": [
    { "id": "terrabase", "name": "TerraBase", "url": "https://api.terrascale.tech", "health": "https://api.terrascale.tech/readyz" },
    { "id": "status", "name": "Status", "url": "https://status.terrascale.tech" }
  ]
}
```

- **Region id** is TerraBase's `--region` setting (`gru-1`): a lowercase
  letter, then lowercase letters, digits, or hyphens, at most 63, no trailing
  hyphen.
- **Ranking**: `health` `ok`, then `unknown`, then `down`; within each, the
  great-circle distance from the client's Cloudflare location (`request.cf`
  coordinates, else its continent); then publication order. `distanceKm` is
  `null` without a location.
- **Health** is the orchestrator's last `GET <api>/readyz` verdict. Once the
  topology is older than `STALE_AFTER_S` (60 s), every region is `unknown`:
  a stale verdict never marks a region down.
- **`closest`** is the first region that is not `down`, or `null`.
- **`stale: true`** means TerraBase was unavailable and Atlas served its last
  cached copy (see [Storage](#storage)).
- `503 discovery_unavailable`: no copy exists and TerraBase is unavailable.

### `GET /v1/resolve`

```json
{
  "v": 1, "project": "01a10971-047d-7de5-a99e-6430003b8ccd", "database": "orders",
  "region": "gru-1", "api": "https://gru.api.terrascale.tech", "auth": "https://gru.auth.terrascale.tech",
  "health": "ok", "placement": "known", "stale": false,
  "pin": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii4uLiJ9.eyJpc3MiOi4uLn0.c2ln",
  "expires": 1791160407
}
```

- `project` is the TerraBase project id (the `{project}` of
  `/v1/projects/{project}/databases/{database}/…`); `database` is optional.
- A database override in the placement wins over the project default.
- An unplaced project gets the closest usable region with `placement:
  "unknown"`.
- A placed region is returned even when it is `down`, because the data
  lives there.
- Atlas never guesses. If it cannot read the placement (no cached copy and
  TerraBase down), it answers `503 discovery_unavailable`. A placed region
  missing from the topology answers `503 no_eligible_region`.
- `400 invalid_project` or `invalid_database` for malformed parameters.
- `503 pin_unavailable` when no signing key is configured.

### Session pins

`pin` is a compact JWS (RFC 7515), `alg: ES256` (ECDSA P-256, SHA-256, raw
`r||s`), with `kid` in its header. Every SDK runtime verifies ES256 with its
standard library. Claims:

```json
{ "iss": "atlas.terrascale.tech", "project": "…", "database": "orders",
  "region": "gru-1", "api": "https://gru.api.terrascale.tech",
  "iat": 1791159807, "exp": 1791160407 }
```

The pin lives 600 s. An SDK session:

1. Calls `GET /v1/resolve` and verifies `pin` against `GET /v1/keys`
   (cache the JWKS; re-fetch it on an unknown `kid`).
2. Sends every TerraBase request to `api` with
   `X-TerraScale-Region-Pin: <region>` (TerraBase TS-499). TerraBase answers
   `421` and its own `X-TerraBase-Region` when the node is in another region.
3. Re-resolves with `fresh=1` when `exp` passes, on a `421`, or on a
   redirect. `fresh=1` makes Atlas re-read TerraBase unless its copy is
   younger than 5 s.
4. Keeps using a still-valid pin if Atlas is unreachable. A static endpoint
   override (configuration, never a hardcoded host) bypasses Atlas entirely.

`kid` is the RFC 7638 thumbprint of the public key. A rotated key makes old
pins unverifiable, which only means resolving again.

## Publishing (ts-orchestrator, TS-506)

`POST /v1/publish` with:

- `X-Atlas-Timestamp: <unix seconds>`, within 300 s of the Worker clock.
- `X-Atlas-Signature: <base64url raw r||s>`, the ES256 signature over the
  UTF-8 bytes of `"atlas-publish-v1\n" + <timestamp> + "\n" + <body>`, made
  with a private key whose public JWK is in `PUBLISH_KEYS`.
- Body `{ "topology"?: Topology, "placements"?: Placement[] }` (at most
  128 KiB, enforced while reading, and 64 placements, one per project).
  Missing, malformed, or expired signature headers are refused before the
  body is read, and the body must arrive within 10 s (`408 body_timeout`).
  Placements are written eight at a time; the report keeps input order.

```json
{
  "topology": {
    "v": 1, "updated": 1791159807,
    "regions": [{ "id": "gru-1", "name": "São Paulo", "country": "BR", "lat": -23.43, "lon": -46.47,
                  "api": "https://gru.api.terrascale.tech", "auth": "https://gru.auth.terrascale.tech", "ok": true }],
    "services": [
      { "id": "terrabase", "name": "TerraBase", "url": "https://api.terrascale.tech", "health": "https://api.terrascale.tech/readyz" },
      { "id": "auth", "name": "ts-auth", "url": "https://auth.terrascale.tech", "health": "https://auth.terrascale.tech/readyz" },
      { "id": "dashboard", "name": "Dashboard", "url": "https://dash.terrascale.tech" },
      { "id": "status", "name": "Status", "url": "https://status.terrascale.tech" },
      { "id": "docs", "name": "Docs", "url": "https://docs.terrascale.tech" }
    ]
  },
  "placements": [
    { "v": 1, "project": "01a10971-047d-7de5-a99e-6430003b8ccd", "region": "gru-1",
      "databases": { "orders": "gru-1" }, "updated": 1791159807 }
  ]
}
```

- The topology is one document: all regions (1..64) and all services
  (0..32), each with unique ids. Publish it whole, every ~10 s and on every
  health transition. `ok` is the region's `GET <api>/readyz` result.
- Every URL must be HTTPS on `terrascale.tech` or a subdomain, without
  credentials, port, query, or fragment. `api` and `auth` are bare origins.
  In development (`DEV_ORIGINS` set) loopback URLs are also accepted.
- The service catalog must carry `terrabase`, `auth`, `dashboard`,
  `status`, and `docs` (a topology without one is `400 invalid_topology`);
  add others, such as `atlas`, freely.
- The whole request is validated before anything is written: any `400`
  means nothing landed.
- Publishes are monotonic per document on `updated` (unix seconds). An older
  `updated`, or a different document with the same `updated`, reports
  `stale` and is not written, so a replayed signed body can never roll a
  newer one back. The identical document is an idempotent replay. Bump
  `updated` for every change, including two changes within one second.
  `updated` may not be more than 300 s ahead of the Worker clock
  (`400 future_updated`), so a future-dated document can never block later
  corrections.
- Response: `{ "topology": "updated"|"stale"|"skipped", "placements": [{ "project", "result": "updated"|"stale" }] }`.
- Errors: `401 invalid_signature`, `400 invalid_*`/`empty_publish`/`future_updated`,
  `408 body_timeout`,
  `413 payload_too_large`, `502 store_unavailable` (TerraBase did not take
  a write; earlier documents may have landed, so retry the request), and
  `503 publish_disabled`.

## Storage

Per Ouroboros, the authoritative copy of every published document lives in
production TerraBase: organization `terrascale-internal`, project `atlas`,
database `atlas`, collection `atlas`. Each document is stored under a
lowercase UUID derived from SHA-256 of `atlas:<key>` (keys `topology` and
`project:<project id>`). The first publish creates the collection.

- **Writes** read the current document and its version, check
  monotonicity, and write with `If-Match: "<version>"` (or `If-None-Match: *`
  when none exists). A `412` means another writer, in any isolate, got there
  first; the publish re-reads and re-checks, up to four times. TerraBase
  therefore orders every writer, which closes the cross-isolate race of the
  old KV-only ingest. After TerraBase accepts the write, isolate memory is
  invalidated and KV is refreshed with `waitUntil`; the cache write does not
  delay the publish response.
- **Reads** go isolate memory (5 s) → KV (`REGIONS` key `topology`,
  `PLACEMENT` key `project:<id>`, each `{at, version, doc}`) → TerraBase. A KV
  copy younger than 60 s is served as is; an older one, or one stamped in
  the future, is refreshed from TerraBase and written back to KV. "Not
  published" is cached too.
- **Stale but available**: when TerraBase errors or times out (2.5 s), Atlas
  serves its last copy with `stale: true`. With no copy it answers `503`.
- **Bound**: KV has no compare-and-swap, so a slow writer can leave an older
  copy in KV. Readers replace it from TerraBase within 60 s; `fresh=1` within
  5 s. Isolate memory never extends either bound: a remembered copy that has
  aged past it is read again.

## Configuration

| Name | Kind | Meaning |
| --- | --- | --- |
| `ATLAS_STORE_URL` | var | `https://<host>/v1/projects/<atlas project id>/databases/atlas`. Static configuration: Atlas cannot discover its own store. |
| `ATLAS_STORE_KEY` | secret | `tb_` API key with `documents:read` and `documents:write`, narrowed to the atlas project |
| `PUBLISH_KEYS` | var | JWKS of the orchestrator's P-256 public keys (at most four, for rotation) |
| `PIN_SIGNING_KEY` | secret | Private P-256 JWK that signs pins; its public part is served by `/v1/keys` |
| `STALE_AFTER_S` | var | Topology age after which health is `unknown` (default 60) |

Missing configuration fails closed: no `PUBLISH_KEYS` or store means
`503 publish_disabled`, no signing key means `503 pin_unavailable`, and no
store means reads serve KV copies only. The production deploy gate
(`npm run deploy:production`) refuses a `wrangler.toml` without a valid
`ATLAS_STORE_URL` and `PUBLISH_KEYS` (public P-256 keys only); the two
secrets are provisioned separately.

## Consuming Atlas from other repositories

- **SDKs (TS-507)**: a resolver with a static override. Default base
  `https://atlas.terrascale.tech`; call `/v1/resolve` per project/database,
  pin as above, and fall back to `closest` from `/v1/discovery` for
  project-less calls. Never hardcode `gru.api.terrascale.tech` or any other
  regional host.
- **TerraBase**: run with `--region=<region id>` exactly as published here,
  and reject a mismatched `X-TerraScale-Region-Pin` with `421` (TS-499).
- **ts-orchestrator (TS-506)**: probe each region's `/readyz`, publish the
  topology and placements with `POST /v1/publish`, and keep `updated`
  monotonic.
- **Everything else** (dashboard, status, docs, CLI): read the service
  catalog and regions from `/v1/discovery`; validate responses with the JSON
  Schema.
