# TerraBaseV2 integration — proposed implementation tickets

Status: **proposals only** for W5-P (`TerraScale.Internals#41`), 2026-08-26.
Companion to [terrabasev2-integration.md](./terrabasev2-integration.md).
These tickets are **not filed**; the mission process files and dispatches
them per this repository's tracker conventions (`docs/agents/issue-tracker.md`).
Bodies below are written in the tracker's issue format so they can be filed
verbatim. No ticket self-assigns into an existing lane; engine-side work
stays in TerraBaseV2's own waves.

Dependency order: TB2-P01 → TB2-P02 → {TB2-P03, TB2-P04} → {TB2-P05, TB2-P06,
TB2-P07} → TB2-P08. Every ticket's acceptance criteria demand red-then-green
tests at the public seam (`AGENTS.md` testing rules; TUnit, real local stack
where a stack is involved).

---

## TB2-P01 — TerraBaseV2 engine host client and configuration

> Part of W5-P (docs/terrabasev2/). Blocked by: none in this repository
> (consumes TerraBaseV2 SE-14/SE-08 artifacts as they land; must compile
> against their published contract).
>
> ## What it builds
> The Platform-side client slice that talks to a TerraBaseV2 C# API host:
> loopback HTTP client for typed operations, loopback SSE/WebSocket handling
> for subscription frames, host base-address configuration bound from
> configuration only, and typed result mapping onto `Result`/`Result<TValue>`
> with `TerraScaleErrorResponse`-compatible errors. No engine symbols, no
> TBEP, no direct engine-process access — the C# API host is the only
> gateway (contract section 3).
>
> ## Acceptance criteria
>
> - [ ] Red-then-green tests at the client seam: each typed operation maps
>       request/response and every refusal row of contract section 4.4 maps
>       to its typed Platform error (probe tests prove no generic/raw
>       passthrough exists).
> - [ ] Configuration binds host base addresses from configuration only;
>       no address, socket path, or credential is hard-coded.
> - [ ] Client surface is Dashboard-agnostic and reusable; no Dashboard
>       contract or header exists in it.
> - [ ] Deadline and cancellation derive from request timeouts for every
>       dispatch (never unbounded).
>
> ## Write scope
> A new Platform feature slice under
> `src/Platform/TerraScale.Platform/Features/Database/TerraBaseV2/` (client,
> options, typed error mapping) plus its tests.

## TB2-P02 — Auth-context resolution (principal vocabulary, tenant claims, credential markers)

> Part of W5-P. Blocked by: TB2-P01.
>
> ## What it builds
> The single Platform seam that turns an authenticated request into
> engine-bound caller evidence per contract section 4: the closed principal
> vocabulary (`user:{ULID}`, `key:{ULID}`, `service:{name}` with
> human/agent kind derivation), tenant-claim construction from the resolved
> virtual database (contract section 5.2, 92-byte bound validated), the
> non-secret dispatch marker (correlation identifier; never a credential),
> and credential-kind column mapping. Audit records written here carry
> principal kind.
>
> ## Acceptance criteria
>
> - [ ] Red-then-green tests: every caller class of contract section 4.3
>       resolves to the exact principal vocabulary entry, kind, and
>       credential-kind column; unknown/unauthenticated callers never
>       produce evidence.
> - [ ] Probe tests: no client input reaches the principal, tenant claim, or
>       credential kind; markers never contain credential material
>       (asserted by content inspection over the constructed evidence).
> - [ ] Cross-tenant evidence is unconstructible: a request authorized for
>       one virtual database cannot produce another database's tenant claim.
> - [ ] Principal strings are validated (non-empty, at most 128 bytes, no
>       control characters) and `service:{name}` names come from a
>       deployment-configured closed set.
>
> ## Write scope
> Auth-context resolver in the TerraBaseV2 slice + validators + tests.

## TB2-P03 — Tenant onboarding mapping and provisioner

> Part of W5-P. Blocked by: TB2-P02.
>
> ## What it builds
> The V2 provisioner and mapping store per contract section 5:
> project→engine-database lifecycle (lazy, idempotent, fail-closed on
> placement), engine tenant records for `(Database, Environment)` pairs
> (`proj:{…}:db:{…}:env:{…}`), friendly-name validation with reserved
> namespace rejection, and Platform metadata as the authoritative onboarding
> state. Offboarding is destructive and only exposed through TB2-P05.
>
> ## Acceptance criteria
>
> - [ ] Red-then-green tests: onboarding records the exact tenant mapping,
>       rejects malformed/reserved names, and is idempotent; provisioning
>       fails closed when a regional cell cannot host the database.
> - [ ] Authorization data (capabilities, credential scopes) exists before
>       the first dispatch into a new tenant (ordering asserted by test).
> - [ ] The four platform service databases map as ordinary tenants under
>       the platform project; customer authorization never resolves to them
>       (probe test).
> - [ ] No engine-side assumptions beyond the landed registry: no
>       create-tenant dispatch exists.
>
> ## Write scope
> Provisioner, mapping records, validators in the TerraBaseV2 slice + tests.

## TB2-P04 — Public document and query operations

> Part of W5-P. Blocked by: TB2-P02 (TB2-P03 for tenant-scoped routes).
>
> ## What it builds
> The public REST surface for the landed registry rows (contract section 6.1,
> rows 1–6): document read, conditional write (`ExpectedVersion`, stable
> operation identity, server-ack-only with `CommitOutcome` surfacing),
> typed and V1-compatible text query (at most 16 KiB), and family read/write
> as the family waves land. Versioned routes through `TerraScale.Endpoints`
> with `RequireActor()`, result-to-HTTP via `ResultHttp`, matching typed SDK
> surface in `@terrascale/sdk`.
>
> ## Acceptance criteria
>
> - [ ] Red-then-green endpoint tests against the real local stack: each
>       operation crosses the public seam (authentication, capability,
>       `(LogicalDatabaseId, EnvironmentId)` scope) and maps to exactly one
>       registry variant.
> - [ ] Uncertain commit outcomes surface as pending/resolvable by operation
>       identity, never as success; conflicts and `ExpectedVersion`
>       mismatches map to the typed conditional-mutation errors (ADR 0009
>       alignment).
> - [ ] Query text over 16 KiB is refused with a typed validation error.
> - [ ] MCP exposability: every operation here is a typed operation with no
>       raw/generic escape (asserted by the same probe tests).
>
> ## Write scope
> Endpoint files (one per endpoint), validators, DTOs in the TerraBaseV2
> slice + tests + SDK surface additions.

## TB2-P05 — Destructive-operation confirmation flow

> Part of W5-P. Blocked by: TB2-P03, TB2-P04.
>
> ## What it builds
> The single prepare/confirm confirmation flow of contract section 6.3:
> impact summary, single-use bounded-TTL confirmation tokens, re-authorization
> at confirm, fresh authentication for human callers, agent-completable
> non-interactive path, server-ack-only completion, and Audit records for
> both calls. Applies to environment/database/project deletion, delete-by-query
> when it lands, restore/import, and schema-migration apply as those waves
> land.
>
> ## Acceptance criteria
>
> - [ ] Red-then-green tests: destructive calls without a token are refused
>       (`ConfirmationRequired`); tokens are single-use; stale tokens are
>       refused (`Expired`); prepare has no side effects (asserted).
> - [ ] An application credential completes prepare→confirm end-to-end with
>       no interactive dependency (agent drill, evidence recorded
>       secret-safe).
> - [ ] Acknowledgement happens only on the engine's committed outcome;
>       audit records for prepare and confirm carry principal kind and the
>       engine operation identity.
>
> ## Write scope
> Confirmation service, token model, endpoints, audit integration in the
> TerraBaseV2 slice + tests.

## TB2-P06 — Subscriptions and sync sessions exposure

> Part of W5-P. Blocked by: TB2-P04. Engine-side dependencies: SE-08 #11
> host endpoints, SE-04 #6 wire protocol.
>
> ## What it builds
> Public SSE/WebSocket subscription endpoints and sync-session exposure per
> contract sections 6.1 rows 16–17: forwarded backbone streams with content-
> free trigger events (push the hint, pull the delta), checkpoint/resume on
> reconnect, bounded queues with counted drops surfaced, and
> `terrascale.sync.v2` session relay for native SDK clients
> (server-ack-only; no optimistic patches).
>
> ## Acceptance criteria
>
> - [ ] Red-then-green tests: cross-tenant subscription refused and audited;
>       checkpoint/resume works across reconnect; drops are surfaced, not
>       hidden.
> - [ ] Trigger events carry no document data (content-free asserted).
> - [ ] Sync mutations acknowledge server-side only; SDK-facing contract
>       documents the removal of optimistic patches (PD-2026-08-26-12 D2).
>
> ## Write scope
> SSE/WS endpoints, session relay, streaming DTOs in the TerraBaseV2 slice +
> tests + SDK surface.

## TB2-P07 — Audit correlation and durable audit records

> Part of W5-P. Blocked by: TB2-P02 (rides every dispatch; lands with
> TB2-P04/P05 usage).
>
> ## What it builds
> The durable audit half of contract section 4.5: Audit records for tenant
> onboarding/offboarding, destructive prepare/confirm, cross-tenant denial
> probes, break-glass grants, and backend-service destructive actions;
> engine `OperationId` correlation in records and structured logs; principal
> kind on every record; the incident-read path over the host's topology/admin
> surface.
>
> ## Acceptance criteria
>
> - [ ] Red-then-green tests: every audited action writes a record carrying
>       principal kind, tenant, and operation identity; records never
>       contain document bodies or credentials (content inspection).
> - [ ] An engine journal event joins its Platform Audit record by
>       (principal, tenant, operation id) in a test.
> - [ ] Audit write failure fails closed for audited actions
>       (`AuditFailure` row).
>
> ## Write scope
> Audit writer, correlation, incident-read endpoint in the TerraBaseV2 slice
> + tests.

## TB2-P08 — Deployment wiring and health integration

> Part of W5-P. Blocked by: TB2-P01..P07 (ships last); gated on the owner's
> V2 cutover decision for any AppHost integration.
>
> ## What it builds
> The deployment contract of section 7 as code: engine+host pair registration
> per regional cell with pinned TerraBaseV2-published artifacts (this
> repository never builds them), host health integration with truthful
> starting states, `PlacementGeneration` convergence for engine databases,
> and explicitly-configured local V2 pairing (V2 runs standalone until the
> owner records the cutover; no default AppHost wiring).
>
> ## Acceptance criteria
>
> - [ ] No workflow, script, or build step builds or publishes TerraBaseV2
>       images (probe test/lane check).
> - [ ] Health remains truthful while starting; engine loss produces clean
>       typed client errors and recovery without orphaned state (real-stack
>       test).
> - [ ] Local development keeps the V1 stack by default; V2 pairing is
>       opt-in through configuration only.
>
> ## Write scope
> Deployment composition, health wiring, placement convergence in Platform
> slices + tests; no CI/workflow changes beyond this repository's own
> targets.

---

## Adjacent-repo follow-ups (recorded, not filed here)

- TerraScale.TypeScript / TerraScale.DotNet: SDK operations for each
  Platform surface above, and the native sync clients (already filed:
  `TerraScale.TypeScript#11` = SE-09, `TerraScale.DotNet#9` = SE-10) with
  server-ack-only semantics.
- TerraScale.MCP: MCP surface additions track the Platform operations as
  they land (AI-01 #30 owns the conformance suite; Platform tickets keep
  every operation MCP-exposable).
- TerraBaseV2: any engine-side vocabulary needs this contract's open
  decisions resolve (section 9) — principal kind field, tenant lifecycle
  operations, reserved namespace list.
