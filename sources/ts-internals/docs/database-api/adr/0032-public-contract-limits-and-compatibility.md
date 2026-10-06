# ADR 0032: named public operations and hard limits

Status: accepted boundary; implementation and numeric policy pending. The
current document and auth-storage slices implement only
part of this decision.

Date: 2026-08-29

## Context

The public edge has one origin, and the workspace goal requires one versioned
public database contract shared by official SDKs. Listener endpoints remain
deployment-supplied. An unbounded or generic route would let callers bypass
authorization, resource accounting, and protocol review. The current host has
document routes and Better Auth storage routes, while reactive and usage
surfaces are incomplete.

## Decision

The public API exposes named operations with typed request and response shapes,
stable error codes, explicit idempotency, and bounded values. Every operation
must have matching source documentation, focused tests, SDK behavior, and
conformance tests before it is advertised as supported.

Current configured defaults are 4 MiB for document request bodies, 16 MiB for
document responses, 256 concurrent requests, and 128 concurrent reactive
sessions. The validator bounds these values, but the current host consumes only
the document body and response bounds. Concurrency accounting and the reactive
surface are release work. Auth-storage applies its own 256 KiB document bound.
The 4 MiB document default is not launch policy: D-25 fixes the maximum
document size at 1 MiB, so the host, schema, SDK, and tests must converge on
that value before production.

The API must not add a raw proxy, arbitrary operation name, hidden fallback,
fixed listener port, or in-process engine path. SDK repositories own client
compatibility matrices. The public major, compatibility window, final limits
table, and limit-exhaustion errors are engineering contract gaps to record and
test before release.

## Current implementation

- `src/database/api/documents.go` maps named document operations and closed
  HTTP outcomes.
- `src/database/api/auth_storage.go` maps three named storage operations
  without an arbitrary operation field.
- `src/database/application/options.go` validates endpoint, protocol, and
  resource bounds; `src/database/api/config.go` loads them.
- API, application, and configuration tests cover the implemented bounds and
  outcomes.

## Consequences

Adding a route has a measurable review cost, but clients receive a contract
that can be checked before engine work starts. Until concurrency and reactive
limits are enforced, the corresponding configuration values must be described
as validated intent rather than active protection.

## Engineering release gaps

Record and test the public-major support window, one authoritative protocol
frame ceiling, exact limit-exhaustion errors, and reactive session semantics.
These values do not change the accepted boundary.
