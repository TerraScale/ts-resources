# Database API production plan

Status: pre-production. Last reviewed: 2026-08-31.

The workspace [`../../GOAL.md`](../../GOAL.md) is authoritative. This plan
tracks the remaining work for the independently deployable ts-internals
Database API. Passing a local test or accepting an ADR does not prove that a
production deployment is ready.

## Mission and boundary

The Database API is the sole public gateway for database and reactive
operations. It exposes versioned HTTPS REST routes and the public reactive
MessagePack protocol. It calls private TerraBase operations only through the
official `terrascale.tech/terrabase-go` client.

The service owns public admission, resource limits, Dashboard authorization
integration, typed engine translation, public errors, retry behavior, and
usage contracts. It does not own Better Auth, organizations, projects,
billing, MCP, TerraBase storage, NATS, or provider placement. The dashboard
and `@terrascale/sdk` use the public contract. No caller receives direct TBEP,
a trusted-header shortcut, a local engine binding, or a raw request proxy.

## Current implementation

The host maps health, document CRUD, and three named Better Auth storage
operations. Document operations and readiness use `terrabase-go` over
protobuf/gRPC, HTTP/2, and TLS 1.3 mutual authentication. The adapter reuses
bounded placement transports and binds every operation to the admitted
principal, tenant, project, and database. Document mutations forward the ULID
idempotency key and usage-admission context.

The current client still exposes structured document values. The adapter
isolates that compatibility conversion, but this does not satisfy D-30.
TB-20/TB-21 must publish protobuf `bytes` fields and raw canonical JSON through
`terrabase-go`. The gateway must then delete the conversion, not add another
parse/serialize bridge. This blocks production.

Readiness fails closed when engine settings are incomplete and probes the real
engine when configuration is complete. Better Auth atomic storage remains
unavailable because the official client does not yet expose `InsertUnique`,
`CompareAndSwap`, or `ConsumeOne`. A usage endpoint and signed-grant verifier
exist as contracts but are not composed into the host. Public reactive routes
are not mapped.

## Production target

Every admitted region runs at least two disposable API instances. Deployment
supplies public endpoints, workload identity, gRPC endpoints, rotated trust,
and the fixed workspace routing configuration. Liveness remains independent;
readiness checks the real engine and required external authorities within a
bounded timeout.

Every route has a versioned schema, operation identity, security scope,
resource bounds, retry and idempotency rules, typed errors, tests, and generated
route-manifest parity. The gateway preserves the difference between a committed
mutation, an accepted operation, and an unavailable or indeterminate result.

Production verification covers authorization, tenant isolation, member and
region loss, reconnect, overload, cancellation, backup and restore, rolling
upgrade, rollback, and the seven-day soak required by the workspace goal.
Hermetic peers and local RF=1 runs remain diagnostics.

## Non-goals

- Dashboard identity, billing, MCP, or product workflows.
- Direct customer access to TBEP, TerraBase, NATS, storage, or providers.
- A generic HTTP proxy, arbitrary path, arbitrary header, or untyped JSON API.
- An API-owned SQLite or in-memory store, fake providers, or trusted local
  headers in the production composition. TerraBase's SQLite engine remains the
  storage authority.
- A fixed development listener port. Deployment supplies the endpoint.
- Claims about production durability or availability based on fixtures.

## Work register

| ID | Priority | Required outcome | Verification |
| --- | --- | --- | --- |
| DB-P0-01 | P0 | Publish the complete REST and reactive contracts with route ownership, OpenAPI, generated bindings, limits, errors, and compatibility rules. | Schema and route-manifest drift checks pass. |
| DB-P0-02 | P0 | Compose Dashboard authentication, signed grants, replay protection, scopes, and engine authorization context. | Live identity, revocation, wrong-scope, expiry, replay, and tenant-isolation tests pass. |
| DB-P0-03 | P0 | Replace unavailable auth-storage and usage ports with durable named operations. | Restart, concurrency, authorization, pagination, and duplicate-delivery tests pass. |
| DB-P0-04 | P0 | Implement bounded reactive WebSocket and HTTP fallback routes with snapshot, result updates, checkpoints, reset, reconnect, and slow-consumer closure. | Rust, Go, and TypeScript corpus plus live transport tests pass. |
| DB-P0-05 | P0 | Enforce readiness, admission, concurrency, body, query, stream, and TBEP limits. | Configuration, overload, cancellation, and shutdown tests pass. |
| DB-P0-06 | P0 | Complete private protobuf/gRPC through `terrabase-go`, including D-30 canonical document bytes, hostile-input handling, live mTLS, and N/N-1 compatibility. | Protobuf drift, client, live-peer, rollback, and invalid-input tests pass. |
| DB-P1-01 | P1 | Add database, query, index, schema, relationship, backup, PITR, restore, and placement operations as the engine publishes them. | Each operation covers success, denial, conflict, retry, cancellation, and partial outcomes. |
| DB-P1-02 | P1 | Add production metrics, traces, redacted audit facts, alerts, and incident-safe errors. | Secret scans, fault injection, alerts, and runbooks pass review. |
| DB-P1-03 | P1 | Qualify multi-instance deployment and recovery in GRU, SFO, and FRA. | Rotation, routing, member loss, region loss, restore, and rollback tests pass on the release candidate. |
| DB-P1-04 | P1 | Prove `@terrascale/sdk` parity for retry, cancellation, pagination, and reactive behavior. | Cross-repository manifest and conformance tests pass. |

## Delivery order

1. Fix route ownership, versioning, bounds, error taxonomy, and D-30. Keep
   unconfigured dependencies fail closed.
2. Land generated contracts and authorization ports, then implement named
   database and Better Auth storage operations.
3. Add reactive routes and runtime protection while `@terrascale/sdk` consumes
   the same manifests and test corpus.
4. Exercise real TerraBase, Dashboard authorization, rotated identity, and the
   production-shaped deployment.
5. Run failure, recovery, backup, restore, deletion, observability, and soak
   checks against one immutable candidate.
6. Promote only the image digest and configuration that passed every gate.

## Acceptance criteria

- The full Go verification set from the workspace goal passes.
- Every registered route appears in the owner-published schema and generated
  route manifest. The host advertises no schema-only route.
- Production startup rejects incomplete endpoint, engine, trust, identity,
  secret, or provider configuration.
- Authentication, authorization, isolation, idempotency, retry, cancellation,
  limits, typed errors, and secret redaction pass at the public boundary.
- TBEP valid, invalid, oversized, unknown-version, replay, cancellation, and
  reconnect cases pass against a real generated peer.
- Reactive snapshots, changes, checkpoints, reset, permission loss, region
  movement, and slow-consumer closure pass through `@terrascale/sdk`.
- Two instances per failure domain survive engine, member, region, identity,
  and control-plane faults within the accepted recovery window.

## Exit gates

The service remains pre-production until the current release candidate passes
the public-contract, security, engine, behavior, runtime, deployment, recovery,
and release gates in the workspace goal. Local fixtures cannot satisfy an
environment gate.
