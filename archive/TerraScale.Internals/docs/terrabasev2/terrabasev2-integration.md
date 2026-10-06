# TerraBaseV2 integration contract (Platform side)

Status: **design / contract proposal** for W5-P (`TerraScale.Internals#41`),
2026-08-26. Nothing in this document is implemented; every "landed" statement
names the source that makes it landable. Implementation follows this
repository's own process through the proposed tickets in
[implementation-tickets.md](./implementation-tickets.md). This document
contains no secrets, credentials, or raw payloads.

## 1. Purpose and scope

TerraBaseV2 is the Rust re-implementation of the storage engine
(`TerraScale/TerraBaseV2`). Charter PD-2026-08-26-11 fixes its boundary:
TerraBaseV2 communicates strictly with the TerraScale backend, is local, and
carries no authentication or user-facing surface. The TerraScale Platform is
the **only** authentication/authorization layer; tenant onboarding,
confirmation, audit shipping, and secret handling stay Platform-side.

This contract specifies the Platform-side half of that boundary — what the
TerraScale backend supplies to a TerraBaseV2 deployment:

1. the **auth-context contract**: how authenticated customer identity and
   tenant context flow from Platform requests into TBEP dispatches;
2. the **tenant onboarding mapping**: Platform projects, databases,
   environments, and repositories onto engine tenant scopes;
3. the **typed operations surface**: which TerraBaseV2 typed operations the
   Platform exposes to SDKs and MCP, with confirmation semantics for
   destructive operations (server-ack-only per PD-2026-08-26-12);
4. the **deployment contract**: hosting and supervision of the local engine
   process and the C# API host, with UDS wiring per PD-2026-08-26-11.

Out of scope: engine-internal behavior, the TBEP wire encoding (SE-14 owns
it), the studio/CLI (TerraBaseV2 local operator tools), and anything the
engine-side W5-E adapter already lands (referenced here, never re-specified).

Vocabulary note: `CONTEXT.md` reserves "tenant" for the engine-side
`TenantId`/`TenantScope` vocabulary only. The Platform-side concept that maps
onto an engine tenant is the **virtual database** — a `(Database, Environment)`
pair (see `CONTEXT.md`: Database, Environment, Repository, Document).

## 2. Authority records

| Record | Clause used here |
| --- | --- |
| Charter PD-2026-08-26-11 D1 | Backend-only, local engine; C# host binds loopback/UDS; TBEP UDS binding is the required transport; no auth surface at the engine; tenant scoping stays engine-enforced from backend-supplied context; MCP exposure runs through the TerraScale backend only |
| Charter PD-2026-08-26-12 D2 | Server-ack mutations: clients drop optimistic patches; mutations await server acknowledgement |
| Charter PD-2026-08-26-12 D5 | W5 split: engine-side adapter (W5-E, landed) and Platform-side contracts (this document) |
| Charter PD-2026-08-26-13 D2/D3 | NATS is KV/config/discovery only, never a data store; engine emits content-free trigger events ("push the hint, pull the delta") |
| Charter PD-2026-08-26-07 D1–D3 | Agents are first-class principals; every capability reachable through typed, MCP-exposable operations; audit must distinguish agent actions (AI-01) |
| TerraBaseV2 ADR 0005 D-1/D-2 | Rust engine core; C# external surfaces; TBEP frames (operations, backbone subscriptions, sync delivery, topology/admin reads, supervision) over MessagePack, UDS same-host |
| TerraBaseV2 ADR 0007 D-1–D-4 | Schema-optional NoSQL; typed, versioned, tenant-scoped schemas enforced at the engine seam; migrations distinct from Logical Migration; typed-only exposure |
| TerraBaseV2 ADR 0008 D-1/D-3 | Sync engine is engine-native; external surfaces are transports and clients of the engine |
| TerraBaseV2 ADR 0011 | Sharding as owned ranges over the Platform-constructed bucket-range table; Platform drives resharding through typed engine operations; 2^20 buckets, at most 128 shards, 8,192-bucket initial allocation floor |

Source paths for the records above:
`/home/mariogk/Projects/TerraScale/specs/GOAL.md` (charter),
`TerraBaseV2/docs/adr/0005-workspace-stack-policy-and-engine-protocol.md`,
`.../0007-nosql-optional-schemas-and-migrations.md`,
`.../0008-native-sync-engine.md`, `.../0011-sharding-model.md` (read-only
main checkout of TerraBaseV2).

## 3. Trust and communication topology

```text
customer SDK (TS/.NET)   Dashboard Next   AI agent via MCP
        |                      |                |
        v                      v                v
TerraScale.MCP  ──>  TerraScale.Platform public API   <── the ONLY authenticated,
                     (versioned REST + WS/SSE,          customer-facing surface
                      JWT sessions + application
                      credentials, project capabilities)
                              |
                              | loopback HTTP only (typed operations, SSE/WS streams)
                              v
                     TerraBaseV2 C# API host (SE-08)
                              |
                              | TBEP over Unix-domain socket (required transport)
                              v
                     TerraBaseV2 engine process (Rust)
```

Rules:

- The Platform public API is the only surface published through ingress,
  public URLs, OpenAPI, Scalar, the SDKs, the CLI, and the Dashboard. The C#
  API host and the engine are **local-only**: loopback/UDS bind, no ingress,
  no public URL, no OpenAPI entry (PD-2026-08-26-11 D1; ADR 0005 D-2).
- TerraScale.MCP consumes Platform public operations like any other typed
  client; it never reaches the C# API host or the engine directly
  (PD-2026-08-26-11 D1 "MCP exposure runs through the TerraScale backend
  only"; AI-01 conformance target).
- The studio and the C# operator CLI (SE-13) are TerraBaseV2 local operator
  tools; they attach to the local engine/C# host without authentication gates
  and are never deployed as customer surfaces.
- No customer content crosses NATS: the engine's NATS use is KV, config
  sharing, and discovery only (PD-2026-08-26-13 D2).
- Region routing stays Platform-owned: global API endpoints route to the
  nearest healthy selected region; regional API endpoints keep strict
  affinity (see `CONTEXT.md`: Global API endpoint, Regional API endpoint).
  Engine instances are placed per regional cell; placement changes flow
  through `PlacementGeneration` convergence exactly as today.

## 4. Auth-context contract

### 4.1 What the Platform authenticates (before any engine involvement)

Every request is authenticated and authorized by the Platform exactly as
today: user sessions (JWT; `RequireActor()`/`EndpointActor`, whose identity is
a ULID `UserId` — `src/Core/TerraScale.Endpoints/Requests/EndpointActor.cs`)
or application credentials (`CONTEXT.md`: Application credential — a machine
identity with explicit project and product capabilities), checked against
project capabilities and, for repository access, the logical
`(LogicalDatabaseId, EnvironmentId)` coordinates
(`TerraScaleApiKeyScope.AllowsRepository`,
`src/Platform/TerraScale.Platform/Features/Database/TerraBase/Services/TerraScaleApiKeyScope.cs`).
Break-glass access resolves to a time-limited, audited scope
(`BreakGlassAuthorizationMiddleware`), never to standing membership.

Authorization decisions are made **only here**. Nothing downstream
re-authenticates: the C# API host and the engine are trusted local processes
(PD-2026-08-26-11 D1).

### 4.2 What crosses into the engine (the W5-E landed shapes)

The engine accepts an opaque `CallerContext` built from `CallerEvidence`
(`TerraBaseV2/src/adapters/protocol/mod.rs`): a `PrincipalId`, a `TenantId`
claim, and a `CredentialInput` carrying one closed credential kind
(`Bearer` | `ApiKey`). The engine-side Platform adapter derives the
engine-enforced scope as `TenantScope::from_parts(caller.tenant_claim(),
engine_identity)` — from backend-supplied context only — and denies any
request whose own tenant claim mismatches the derived scope
(`PlatformError::TenantDenied`), audited before any engine access
(`TerraBaseV2/src/adapters/platform/mod.rs`,
`enforce_tenant_isolation`/`TrustedAuthorizer::tenant_scope_for`). The engine
repeats tenant isolation on every snapshot, transaction, and query.

The Platform-side obligations this contract fixes:

1. **The Platform constructs the evidence.** No client input ever names a
   principal, tenant, or credential kind to the engine; all three fields are
   derived from the authenticated request and the resolved virtual database.
2. **No secret crosses the boundary.** PD-2026-08-26-11 means the engine
   verifies nothing, so the `CredentialInput` the backend supplies is a
   synthesized, non-secret dispatch marker (the dispatch correlation
   identifier), never the session token, API key, or any credential material.
   Its kind column records the principal class (below). This satisfies the
   engine-side invariant that no credential is read, accepted, or stored
   (`src/adapters/platform/mod.rs` module docs) and this repository's
   no-secrets rule.
3. **The tenant claim is the engine tenant of the resolved virtual database**
   (section 5), never a client-supplied string.

### 4.3 Principal vocabulary (human/agent distinguishability)

`PrincipalId` at the engine seam is a validated non-empty text with no kind
field (`PrincipalId::try_new`,
`TerraBaseV2/src/adapters/protocol/mod.rs`). AI-01 requires audit records to
carry principal kind (human/agent) without leaking credentials or document
bodies. This contract therefore fixes a **closed, canonical principal
vocabulary** constructed only by the Platform; the kind is derivable from the
prefix, so the engine audit skeleton (which records the principal verbatim)
becomes kind-distinguishable with no engine change:

| Platform caller | Engine `PrincipalId` | Kind | Credential kind column |
| --- | --- | --- | --- |
| Authenticated user session (Dashboard, CLI login, SDK, MCP session bound to a user) | `user:{ULID}` — the `EndpointActor.UserId` | human | `Bearer` |
| Application credential (machine identity; automation, non-interactive MCP agents) | `key:{ULID}` — the application credential's ULID | agent | `ApiKey` |
| TerraScale backend service (regional reconciler, provisioner, backup scheduler) | `service:{name}` — closed, deployment-configured name | agent | `ApiKey` |
| Break-glass access | `user:{ULID}` — the acting TerraScale Admin | human | `Bearer` |

Rules:

- The ULID inside `user:`/`key:` is the bare 26-character ULID; the prefix is
  a kind tag in the engine's wire vocabulary, not a prefixed resource ID.
  This mirrors the existing key vocabulary (`MetadataKeys` → `USER#{id}`).
- Principal strings are unique within and across kinds: user ULIDs and
  credential ULIDs are unique, and service names are a deployment-configured
  closed set. Duplicate principals across kinds are impossible by prefix.
- `service:{name}` names are bounded by Platform policy to at most 64
  characters; the Platform validates the full principal (non-empty, at most
  128 bytes, no control characters) before construction. The engine enforces
  only non-emptiness on principals today, so the bound is Platform-side.
- Break-glass distinguishes itself in the Platform's durable Audit record
  (the grant identifier, scope, reason, and approver), not by a special
  engine principal: at the engine seam a break-glass dispatch is the acting
  human principal, keeping the engine vocabulary closed.
- MCP agents acting with a user session are `user:` principals (human-driven
  tooling); agents acting with an application credential are `key:` principals
  (non-interactive). This is exactly the AI-01 audit distinction, derived
  without new wire fields.

### 4.4 Refusal vocabulary reserved for the Platform

The engine-side `PlatformError` enum keeps denial rows that are unreachable at
the trusted local seam and explicitly reserved for "the future Platform
side" (`TerraBaseV2/src/adapters/platform/mod.rs`):
`CallerDenied`, `PermissionDenied`, `Expired`, `ConfirmationRequired`,
`AuditFailure`, `SecretPolicyViolation`. This contract adopts that reserved
vocabulary for the Platform-side refusals, so one refusal vocabulary spans
the seam; the rows stay unreachable at the engine itself under
PD-2026-08-26-11 (the trusted local boundary performs none of these
denials):

| Platform decision | Engine vocabulary row | Platform public result |
| --- | --- | --- |
| Unauthenticated caller | `CallerDenied` | 401 via `TerraScaleErrorResponse` + TraceId |
| Capability/scope denied (`AllowsRepository` false, capability missing) | `PermissionDenied` | 403 |
| Stale confirmation token / expired evidence | `Expired` | 409 with resubmit guidance |
| Destructive operation without confirmation | `ConfirmationRequired` | 409 + confirmation token flow (section 6.3) |
| Audit write failed for an audited action | `AuditFailure` | fail closed for audited (destructive/onboarding) actions |
| Secret material detected in request fields that must never carry one | `SecretPolicyViolation` | 400 |

Tenant isolation failures surface as `TenantDenied` from the engine itself
(and map to 403 Platform-side); they are also Platform Audit records, because
a cross-tenant probe is a security action (section 4.5).

### 4.5 Audit lifecycle

Two audit planes, joined by identifiers, never by content:

- **Engine audit skeleton (landed, in-process):** one typed, content-free
  lifecycle event per dispatch — `Dispatched`, `Completed`,
  `Refused(reason)` — over five operation kinds and seven refusal categories,
  in a bounded journal of at most 1,024 events carrying only sequence, stage,
  operation kind, principal, tenant, and optional operation identity
  (`TerraBaseV2/src/adapters/platform/audit.rs`, `MAX_AUDIT_EVENTS`). It
  structurally cannot carry a document body, field, credential, or
  fingerprint. Durable shipping is explicitly deferred to the Platform side —
  this contract.
- **Platform Audit records (durable, this repository):** append-only,
  secret-redacted records per `CONTEXT.md` (Audit record), written for the
  security/membership/billing/credential/administrative/destructive subset —
  not for ordinary customer reads/writes, whose volume belongs to usage
  metering, not audit.

Platform obligations:

1. **Ship the skeleton for incidents, not as a stream.** The Platform reads
   the engine journal through the C# API host's topology/admin surface
   (TBEP admin reads) for diagnostics and incident support, correlated by
   principal/tenant/operation identity. It does not mirror the journal into
   durable storage wholesale.
2. **Write durable Audit records** for: tenant onboarding/offboarding,
   destructive-operation prepare and confirm, cross-tenant denial probes,
   break-glass grants, credential lifecycle, and backend-service destructive
   actions (restore, migration apply).
3. **Correlate by identity, not content.** Every mutating Platform dispatch
   records the engine `OperationId` in its Audit record and in structured
   logs; the engine journal event and the Platform Audit record join on
   (principal, tenant, operation id). Document bodies never appear on either
   side.
4. **Carry principal kind into Audit records** (human/agent, per the
   vocabulary above) — the AI-01 audit requirement, satisfied Platform-side
   while the engine skeleton stays content-free.

## 5. Tenant onboarding mapping

### 5.1 The mapping

TerraBaseV2 has a native tenant primitive the V1 TerraBase lacks: every
snapshot, transaction, and query is bound to a `TenantScope`
(`(TenantId, engine identity)`), storage keys documents by
`(tenant, collection, id)`, and backup manifests encode whole tenants. The
mapping uses it for the virtual-database boundary:

| Platform concept (`CONTEXT.md`) | TerraBaseV2 target | Notes |
| --- | --- | --- |
| Project | One engine database: the deployment unit of engine process + C# API host per regional cell | Replaces the V1 physical `proj-{projectId}` TerraBase database; topology per ADR 0011 (Platform-constructed bucket-range table, at most 128 shards, 8,192-bucket initial allocation floor) |
| Virtual database = `(Database, Environment)` | **Engine tenant** — one `TenantId` per pair | The isolation unit. Moves V1's application-enforced partition encoding into engine-enforced scoping |
| Repository (typed collection) | Engine `CollectionName` = the friendly collection name | No partition encoding: the tenant already carries `(Database, Environment)`. Storage keys documents by `(tenant, collection, id)`, so each repository is a distinct keyspace inside the engine-enforced tenant; friendly names stay public exactly as `RepositoryDefinitionDocument.Collection` is today |
| Document | Engine `DocumentId` = the bare 26-character ULID storage id | No prefixed, collection-prefixed, or path-shaped ids (both repositories' rule) |
| Platform service databases (`TerraScale.Authentication`, `TerraScale.Platform`, `TerraScale.Payments`, `TerraScale.Queue`) | Ordinary engine tenants under the configured platform project's engine database | Same rule, no special cases; customer authorization never resolves to them — only `service:` principals dispatch into them |
| Region selection | `Project.Regions` → per-cell engine placement, `PlacementGeneration` convergence | Unchanged; region selection is owned by `Project` |

### 5.2 Engine tenant identifier

```text
TenantId = "proj:" + projectId  + ":db:" + databaseId  + ":env:" + environmentId
```

with `projectId`/`databaseId`/`environmentId` the lowercased 26-character
ULIDs. Maximum length 92 bytes, within the engine's 255-byte identifier bound
(`TerraBaseV2/src/types.rs`, `validate_identifier_text`: non-empty, at most
255 bytes, no control characters, no leading/trailing whitespace). The
Platform validates well-formedness before the first dispatch and stores the
mapping alongside the `ProjectDatabase`/`ProjectDatabaseEnvironment` metadata
that owns it. The identifier is globally unique across engine databases,
which keeps backup manifests (whole-tenant encoded) and audit correlation
unambiguous.

This replaces V1's `RepositoryPartition.EncodePhysicalCollection`
(`ts.{logicalDatabaseId}.{environmentId}.{friendlyCollection}`,
`src/Platform/TerraScale.Platform/Features/Database/TerraBase/Documents/RepositoryPartition.cs`)
for TerraBaseV2-backed stores; the V1 seam remains for the V1 engine until
the cutover decision.

### 5.3 Reserved namespaces

Collection names and document fields follow the engine's reserved-namespace
enforcement (a W3-F prerequisite the charter tracks as an integrator
collision action). Platform-side, the repository/definition validators reject
reserved engine prefixes before onboarding, so an engine-side refusal never
meets customer input. The exact reserved list is pinned from the engine when
that enforcement lands; the contract requires only that the Platform fails
closed on unknown/reserved names rather than passing them through.

### 5.4 Onboarding lifecycle

1. **Project creation** — no engine resources (unchanged: lazy allocation).
2. **First storage-backed resource** — the V2 provisioner (proposed ticket
   TB2-P03) creates the engine database across the project's selected
   regional cells: engine process + C# API host per cell, Platform-constructed
   topology view, fail-closed when the cell cannot host the required
   members. Idempotent, like `ProjectDatabaseProvisioner.EnsureProjectDatabaseAsync`
   today.
3. **Logical database + environments** — metadata first, then the engine
   tenant mapping is recorded; the engine needs no create-tenant call (a
   tenant exists when first written — the current closed registry has no
   onboarding variant), so onboarding state is authoritative Platform-side.
   Authorization data (capabilities, credential scopes) must exist before the
   first dispatch into the tenant.
4. **Repository creation** — metadata + friendly-name validation; engine
   collections materialize on first use.
5. **Offboarding (environment, database, or project deletion)** — a
   destructive operation under section 6.3: prepare/confirm, server-ack-only,
   audited; the engine-side data deletion dispatches through typed operations
   as the BK/SM waves land them, and completes only on the acknowledged
   engine outcome. Backup retention obligations are evaluated before the
   deletion dispatch (restore must still be possible while a backup policy
   requires it).

## 6. Typed operations surface

### 6.1 Inventory (cross-checked)

"Registry today" is the closed `PublicOperation` set in
`TerraBaseV2/src/operations.rs` (exactly four variants: `DocumentRead`,
`DocumentWrite`, `Query`, `Family`) plus the TBEP frame classes ADR 0005 D-2
fixes (operations, backbone subscription streams, sync-delivery frames,
topology/admin reads, supervision frames). Waves are the filed TerraBaseV2
tickets (numbers below). Status: **landed** = in the registry today;
**wave** = filed ticket that adds it; **gap** = filed gap ticket.

| # | Platform public capability | Engine surface | Status / owner | Destructive |
| --- | --- | --- | --- | --- |
| 1 | Read one document | `PublicOperation::DocumentRead` | landed (registry) | no |
| 2 | Write one document (conditional mutation, `ExpectedVersion`) | `PublicOperation::DocumentWrite` (carries `ExpectedVersion`, stable `OperationId`, deadline, cancellation) | landed (registry); maps to ADR 0009 conditional document mutations | no |
| 3 | Query — typed | `PublicOperation::Query(QueryInput::Typed)` | landed (registry) | no |
| 4 | Query — V1-compatible text (RQL) | `PublicOperation::Query(QueryInput::V1Compatible)`, at most 16 KiB text (`MAX_QUERY_TEXT_BYTES`) | landed (registry); TQL-04 #35 owns RQL parity | no |
| 5 | Query — TQL | TQL operation form | wave: TQL-03 #34 (TQL across operation/host/CLI/studio/MCP) | no |
| 6 | Data families (counters, time-series, attachments, revisions, compare-exchange, identity) | `PublicOperation::Family(Read/Write)` | landed (registry); completion waves = the filed family gap set (#71–#78) | per family write |
| 7 | Session / unit-of-work semantics | typed session contract | gap: GAP-D01 #58 (decision-first) | no |
| 8 | Metadata / change-vector, conditional load | typed metadata operations | gap: GAP-D02 #59 | no |
| 9 | Patch operations | typed patch operations | gap: GAP-D07 #60 | no |
| 10 | Bulk insert | ingestion stream | gap: GAP-D10 #61 | no |
| 11 | Patch/delete by query | typed query-mutation operations | gap: GAP-Q10 #65 | **yes** (delete-by-query) |
| 12 | Includes | typed include contract | gap: GAP-Q07 #64 | no |
| 13 | Static index definitions, index lifecycle | typed index operations | gap: GAP-Q06 #63, GAP-Q18 #69; auto-index lifecycle IX-03 #39 | no |
| 14 | Collection schemas (declare, validate, version) | typed schema operations (tenant-scoped, engine write-path enforcement per ADR 0007 D-2) | wave: SM-04 #28 | no |
| 15 | Schema migrations (dry-run, apply, resume, evidence) | typed migration operations (idempotent, resumable; distinct from Logical Migration per ADR 0007 D-3) | wave: SM-03 #27 | **yes** (apply) |
| 16 | Subscriptions / live updates | TBEP backbone subscription streams surfaced as SSE/WebSocket (with PD-13 D3 content-free trigger events: push the hint, pull the delta) | wave: SE-03 (landed backbone) + SE-08 #11 host endpoints | no |
| 17 | Sync sessions (`terrascale.sync.v2`) | TBEP sync-delivery frames to the engine's delivery layer; native SDK clients (TS `TerraScale.TypeScript#11`, .NET `TerraScale.DotNet#9`), conformance kit SE-05 #7, wire SE-04 #6 | wave: SE-04/05/08/09/10; **server-ack-only** per PD-2026-08-26-12 D2 (no optimistic patches) | no |
| 18 | Backup, restore, export/import, logical migration | typed backup/restore/smuggler operations (agent-drivable per PD-2026-08-26-11 D2) | waves: BK-02 #43 (restore, Recovery Receipts), BK-03 #44 (smuggler + logical migration), BK-04 #45 (schedules/encryption/compression/retention); core BK-01 landed | **yes** (restore, import) |
| 19 | Placement / resharding | Platform-driven typed engine operations over the bucket-range table (ADR 0011 D3) | waves: SH-02..SH-04 (SH-03 #49 resharding) | **yes** (bucket migration) |
| 20 | Topology/admin reads, supervision | TBEP topology/admin reads + supervision frames | wave: SE-14 #10 (spec + engine server + C# client) | no |
| 21 | Vector search, presence/ephemeral, AI-era streams | typed operations at the query/sync seams | later rows: GAP-C2 #84, GAP-C3 #85, GAP-C4 #86 | no |
| 22 | Offline persistence (durable client stores) | sync-client capability | later row: GAP-C1 #83 | no |

Rules that hold across the whole surface:

- **Typed-only, closed-registry exposure.** The Platform composes only the
  engine's typed operations; there is no generic route, raw body, arbitrary
  SQL, or storage-handle operation anywhere in the public API (the registry
  is closed by construction — `TerraBaseV2/src/adapters/protocol/mod.rs`
  module docs). Every new engine operation lands through its wave and then
  through a Platform ticket in [implementation-tickets.md](./implementation-tickets.md).
- **MCP-exposable by construction.** Every capability above must be
  exposable through TerraScale.MCP under identical authorization, isolation,
  confirmation, and audit rules (PD-2026-08-26-07 D1; AI-01 #30). The
  Platform public API is the single surface both the SDKs and MCP consume.
- **Deadlines and cancellation travel with every operation.** The registry
  requires a bounded deadline and cancellation on every variant; the Platform
  derives them from request timeouts, never leaves them unbounded.
- **Stable operation identity on every mutation.** Writes carry a stable
  `OperationId` (idempotent retry identity — PD-2026-08-26-07 D2's
  idempotent-mutations requirement); the Platform generates it, records it in
  the Audit record, and returns it for resolution of uncertain outcomes.

### 6.2 Mutation acknowledgement (server-ack-only)

No Platform operation is optimistic. Mutations complete only on the engine's
acknowledged outcome: the public write path commits at
`LocalDurability::Synced`
(`TerraBaseV2/src/adapters/platform/engine_port.rs`,
`PUBLIC_WRITE_DURABILITY`), and the response is one of
`CommitOutcome::Committed` (ack), `CommitOutcome::Unknown` (durable state the
caller resolves by operation identity — surfaced as "pending, resolvable",
never as success), or a typed rejection. SDK sync clients follow the same
rule (PD-2026-08-26-12 D2: clients drop optimistic patches; mutations await
server acknowledgement).

### 6.3 Confirmation semantics for destructive operations

Destructive operations (marked **yes** above: environment/database/project
deletion, collection drop where exposed, delete-by-query, restore, import,
schema-migration apply, bucket migration) follow one flow, completable by
interactive **and** non-interactive callers (AI-01: confirmation flows an
agent can complete):

1. **Prepare** (typed operation, no side effects): the Platform validates
   authorization, computes the impact summary (counts, scopes, retention
   obligations), returns a single-use confirmation token with a bounded TTL,
   and writes the Audit record. `ConfirmationRequired` is the refusal for any
   attempt to skip it.
2. **Confirm** (typed operation): presents the token; the Platform re-checks
   authorization and TTL, then dispatches the destructive engine operations
   and acknowledges **only** on the engine's committed outcome
   (server-ack-only, section 6.2). `Expired` is the refusal for a stale
   token. Both calls are audited; tokens are single-use.
3. **Fresh authentication** applies where the Platform already requires it
   (deletion and credential actions — `CONTEXT.md`: Fresh authentication):
   human callers re-authenticate at confirm; application-credential callers
   satisfy the same bar by the scoped capability check plus the explicit
   confirm call — no interactive UI dependency.
4. **Agent drills** (PD-2026-08-26-11 D2): backup/export/import and
   migration flows must run end-to-end through these two calls with an
   application credential, joining AI-01's conformance evidence.

## 7. Deployment contract

### 7.1 Composition and supervision

- Per regional cell serving a project's engine database: one **TerraBaseV2
  engine process** and one **C# API host** (SE-08 #11), colocated on the same
  host. The host owns engine-process supervision per the SE-14 contract:
  engine loss produces truthful health, clean client errors, and recovery
  without orphaned state (SE-08 AC).
- The Platform backend owns the lifecycle above the host: it deploys,
  configures, health-checks, and converges engine databases per
  `PlacementGeneration`, exactly as regional reconcilers converge the V1
  store today. Placement/topology construction is Platform-owned per
  ADR 0011 (Platform-constructed, engine-validated bucket-range table);
  production engine databases use ADR 0011's topology limits and fail closed
  when a cell cannot host the required members.
- **Artifact ownership does not move.** The engine and C# host artifacts are
  built and published by the TerraBaseV2 repository; this repository's
  release plan selects only its Platform, Authentication, and Dashboard
  targets and must not add workflows or build steps for another repository's
  images (`AGENTS.md`). The Platform deployment consumes pinned,
  published TerraBaseV2 artifacts.
- Health stays truthful while starting (an `AGENTS.md` essential); host health
  reflects engine state, and Platform readiness gates on it.

### 7.2 UDS wiring (PD-2026-08-26-11 D1)

- The host↔engine link is TBEP over a **Unix-domain socket** — the required
  transport; QUIC remains deferred until a networked-engine need is recorded.
- One socket per engine instance, path per instance identity, filesystem
  permissions restricting the socket to the host process's user/group (the
  SE-14 security model owns the exact mode); the C# API host and the local
  operator CLI (SE-13 #12) are the only clients.
- The Platform↔host link is loopback HTTP (typed operations) plus loopback
  SSE/WebSocket for subscription and sync-session forwarding — never
  published through ingress, public URLs, OpenAPI, or SDKs.
- Unknown TBEP major versions fail closed on both sides (ADR 0005 D-2);
  Platform upgrades pin engine/host artifact versions together so the pair
  speaks one major version.

### 7.3 Observability

- Platform side keeps ZLogger console JSON + OpenTelemetry to Loki/Tempo/
  Grafana; the engine and host emit their own telemetry per TerraBaseV2
  policy. Dispatches carry the Platform trace/correlation identifier in the
  synthesized credential marker (section 4.2), so engine-side events join
  Platform traces without carrying customer content.
- Trigger events (PD-2026-08-26-13 D3) ride subscription frames and the
  host's SSE/WebSocket endpoints; clients pull the delta batch from their
  checkpoint. The Platform surfaces them on its public subscription
  contracts only — no operation/activity feed in the Dashboard beyond the
  bounded notification center (`AGENTS.md`).

### 7.4 Local development

The owner declined DevHost integration for now: V2 runs standalone
(charter ledger 2026-08-26). Until the owner records a cutover decision,
local development keeps the V1 stack through `TerraScale.AppHost`; the
Platform-side integration lands behind explicit configuration pointing at a
locally run TerraBaseV2 engine+host pair, and any AppHost wiring of V2 is a
gated ticket (TB2-P08), not a default.

## 8. Security and secrets

- No credential, token, cookie, key, connection string, or raw production
  payload appears in this contract, crosses the Platform→engine boundary
  (section 4.2), or lands in either audit plane (section 4.5).
- The engine and host run without authentication gates by design
  (PD-2026-08-26-11 D1); the security boundary is (a) the Platform's
  authenticated public surface, (b) loopback/UDS binding with filesystem
  permissions, and (c) engine-enforced tenant scoping from backend-supplied
  context only.
- Cross-tenant probes are denied at the engine before data access and are
  Platform Audit records (security action) with principal and tenant
  identifiers only.

## 9. Open decisions (parent-owned)

1. **Principal kind as a wire field vs prefix** — this contract derives kind
   from the closed prefix vocabulary (no engine change). If AI-01 conformance
   prefers an explicit kind field on the engine seam, that is an engine-side
   vocabulary extension and a superseding decision.
2. **Hot-path direct-TBEP option** — the Platform always routes through the
   C# API host (one supervision point, subscription/sync termination). If the
   SE-14 UDS-vs-QUIC measurement or SE-07/SE-15 budgets show the extra local
   hop matters, a Platform-embedded SE-14 C# client variant needs its own
   decision.
3. **Engine-side tenant admin operations** — onboarding is metadata-only
   Platform-side today because the registry has no tenant variant. If the
   engine adds tenant lifecycle operations (e.g. for explicit deletion
   evidence), the mapping here is unchanged; only the offboarding dispatch
   gains a typed engine operation.
4. **Reserved namespace list** — pinned from the engine when the W3-F
   reserved-namespace enforcement lands (an integrator collision action in
   the charter).

## 10. Source index

- `/home/mariogk/Projects/TerraScale/specs/GOAL.md` — charter: PD-2026-08-26-11
  D1, PD-2026-08-26-12 D2/D5, PD-2026-08-26-13 D2/D3, PD-2026-08-26-07,
  PD-2026-08-26-14 D1, W5 sections, risk ledger.
- `/home/mariogk/Projects/TerraScale/TerraBaseV2/docs/adr/0005-…md`,
  `0007-…md`, `0008-…md`, `0011-…md` — read-only main checkout.
- `/home/mariogk/Projects/TerraScale/TerraBaseV2/src/operations.rs` — the
  closed registry (4 variants), query input forms, 16 KiB text bound.
- `/home/mariogk/Projects/TerraScale/TerraBaseV2/src/types.rs` — identifier
  validation (255-byte bound), `TenantScope`.
- `/home/mariogk/Projects/TerraScale/TerraBaseV2/src/adapters/protocol/mod.rs`
  — `CallerEvidence`, `PrincipalId`, `CredentialKind`, closed-registry rule.
- `/home/mariogk/Projects/TerraScale/TerraBaseV2/src/adapters/platform/mod.rs`
  — `PlatformAdapter.dispatch`, `TenantScope` derivation, tenant isolation,
  reserved `PlatformError` rows.
- `/home/mariogk/Projects/TerraScale/TerraBaseV2/src/adapters/platform/audit.rs`
  — audit skeleton (stages, kinds, refusal categories, 1,024-event bound).
- `/home/mariogk/Projects/TerraScale/TerraBaseV2/src/adapters/platform/engine_port.rs`
  — `PUBLIC_WRITE_DURABILITY`, `CommitOutcome` mapping.
- This repository: `CONTEXT.md` (glossary), `AGENTS.md` (per-project
  database, transport rules, artifact ownership),
  `src/Core/TerraScale.Endpoints/Requests/EndpointActor.cs`,
  `src/Platform/TerraScale.Platform/Features/Database/TerraBase/Services/TerraScaleApiKeyScope.cs`,
  `src/Platform/TerraScale.Platform/Features/Database/TerraBase/Documents/RepositoryPartition.cs`,
  `docs/databases/virtual-databases.md` (V1 model this maps forward).
- Forgejo tracker (read-only): TerraBaseV2 #6, #10, #11, #12, #27, #28, #30,
  #34, #35, #39, #43, #44, #45, #49, #58..#86; TerraScale.TypeScript #11;
  TerraScale.DotNet #9.
