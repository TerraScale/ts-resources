# TerraBase integration

Status: current. The workspace `GOAL.md` and TerraBase's published protobuf
contract are authoritative.

## Supported path

```text
customer application or dashboard
        |
        | @terrascale/sdk
        | HTTPS REST or reactive MessagePack
        v
ts-internals Database API
        |
        | terrabase-go protobuf/gRPC over HTTP/2 with TLS 1.3 mTLS
        v
TerraBase Members
```

Private TBEP follows the workspace goal and TerraBase ADR 0025. This repository
uses `terrascale.tech/terrabase-go`, the only network client, and owns no second
wire codec or generated private bindings. The adapter reuses bounded placement
transports, creates an immutable client for each complete principal, tenant,
project, and database scope, and forwards mutation idempotency and usage
admission identities. Public reactive WebSocket MessagePack is a separate
protocol.

The pinned client still exposes structured document values. That temporary
compatibility conversion is isolated in the adapter but does not satisfy D-30.
TB-20/TB-21 must publish raw canonical JSON bytes through protobuf and
`terrabase-go` before production. The gateway must delete the conversion when
that API exists, not add another parse/serialize bridge.

Better Auth atomic storage also remains fail-closed. The official client does
not yet expose `InsertUnique`, `CompareAndSwap`, or `ConsumeOne`, and the
gateway must not approximate them with document calls.

## Client ownership

`terrabase-go` owns generated protobuf bindings, connection setup, request
encoding, response decoding, and typed engine errors. This repository owns
the adapters that map public Database API operations to those client methods.
It must not check in a second generated client or implement another wire
codec.

The adapter boundary is closed and typed. Adding a public operation requires a
corresponding `terrabase-go` method, a bounded application port, explicit
error mapping, and tests on both sides of the adapter.

## Identity and authorization

The dashboard owns account identity, organizations, projects, billing, and
entitlements. The Database API verifies the caller, derives the database
scope, applies public admission policy, and sends a typed authorization
context to TerraBase.

TerraBase enforces database and collection actions, query predicates, field
projection, schema operations, reactive dependencies, and reconnect
filtering. Caller JSON, query text, and headers cannot override the verified
tenant, project, or database scope.

## Documents and reactive results

TerraBase parses and canonicalizes a document once at write time. The
canonical JSON body then remains opaque bytes through storage, TBEP, HTTP
responses, replication, and reactive frames. The gateway derives ETags and
metering from typed metadata without decoding the body.

The public reactive protocol uses MessagePack for subscription identity,
revisions, and patch structure. Canonical JSON document bytes ride inside the
frame unchanged. One encoded update may be fanned out to all authorized
subscribers of the same query.

## Placement and durability

Launch regions are GRU, SFO, and FRA. A database selects one to three regions.
TerraBase owns member placement state, cross-region replication, conflict
resolution, and repair. The Database API exposes typed placement and health
operations without naming physical members or transport details.

`RegionalDurable` waits for the local RF=2 copy. `GlobalDurable` requires at
least two active regions and fails closed when that condition cannot be met.
Backups and PITR are separate from replication and use Litestream-managed
Object Storage streams.

## Failure behavior

- Startup rejects incomplete engine endpoint, trust, or identity settings.
- Readiness probes the configured engine within a bounded timeout.
- Transport ambiguity is never reported as a confirmed failed mutation.
- Cancellation and deadlines propagate to `terrabase-go`.
- Private provider or engine details never enter customer error bodies.
- Test engines and fixtures cannot be selected by production configuration.

The repository verification set covers adapter behavior and a hermetic gRPC
engine. Environment-gated live tests cover real certificates and a deployed
TerraBase endpoint.
