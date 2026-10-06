# ADR 0035: usage export integrity and authorization

Status: Accepted for the domain and application boundary. Runtime source,
authorizer, route composition, and reconciliation remain open.

Date: 2026-08-29

## Context

TerraBase is the authority for billable usage. The Database API must export
engine-minted facts without allowing a caller to select another scope, replay
an ambiguous continuation, bypass sequence integrity, or alter acknowledged
history. Dashboard owns pricing and invoicing, not this service.

## Decision

Usage export accepts a typed caller context and a typed scope containing tenant,
project, database, partition, and region. The service requires the action
`usage.export`, binds every caller resource field to the requested scope, and
asks an explicit authorizer before reading a segment source.

The domain keeps six fixed versioned meters. Segments are canonical, bounded,
checksummed, and immutable. Integer totals are decimal text. Corrections append
a segment referencing a matching base. Sequence intervals must be ordered,
non-overlapping, and gap-free per meter, version, scope, and replica epoch.
Continuation tokens are opaque, bounded, and must immediately follow the
previous sequence. Duplicate segment identities are accepted only when their
bytes match exactly.

The usage HTTP route remains unadvertised until a trusted source, authorizer,
caller-context accessor, and host composition exist. No telemetry or message
broker is a usage correctness source.

## Current implementation

- `src/database/domain/usage*.go` defines meters, segment encoding, checksums,
  and closed errors.
- `src/database/application/usage.go` binds authorization and validates
  ordering, identity, continuation, and scope.
- `src/database/api/usage.go` defines the typed HTTP projection, but the host
  does not register it.
- Domain, application, and API tests cover fixed meters, duplicate and
  reordered segments, ledger gaps, corrections, tampering, overflow, and
  authorization binding.

## Consequences

Export consumers can reconstruct usage from deterministic, append-only
segments. The API does not make a billing or availability claim until a real
engine source, authorization boundary, and reconciliation record exist.

## Open release work

TerraBase and Dashboard owners must provide the source, acknowledgement,
retention, reconciliation, and authorization contracts. The service owner must
then map the route and add end-to-end and outage tests.
