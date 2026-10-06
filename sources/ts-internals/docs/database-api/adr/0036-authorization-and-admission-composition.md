# ADR 0036: authorization and admission composition

Status: accepted boundary; implementation pending.

Date: 2026-08-29

## Context

The repository contains a grant verifier and several typed authorization
ports, but `DatabaseApiComposition` currently registers neither the verifier
nor an external signature, replay, caller-context, or admission provider. The
service also validates concurrency-limit configuration without consuming those
limits. Treating these seams as complete would create a security and resource
control gap.

## Decision

Every product operation must pass through a host-composed authorization and
admission boundary before it reaches a gateway or storage port. The boundary
must obtain caller identity from the authenticated transport, verify a
short-lived audience- and resource-bound grant where the workspace contract
requires one, consume replay state, enforce policy generation and key identity,
and attach only an opaque verified context to application services.

Admission must enforce configured request and reactive-session limits before
unbounded work begins. It must distinguish invalid input, authorization
denial, resource exhaustion, dependency unavailability, and cancellation using
stable public outcomes. It must not infer membership, extend expiry, fall back
to a local authority, or accept a raw token in a typed application port.

Dashboard owns Better Auth and grants. TerraBase owns the engine-side
authorization and health contracts. Orchestrator owns routing, topology,
workload identity, and observability operations. The Database API owns the
public route and admission boundary. Exact limits, timeouts, queue budgets,
and error values remain engineering contract gaps to record and test.

## Current implementation

- `src/database/application/grants.go` implements claim, key, lifetime, and
  replay checks; its tests cover accepted, rejected, replayed, and unavailable
  dependency outcomes.
- `src/database/api/composition.go` composes the request-admission limit and
  records the remaining authorization seams.
- `src/database/application/options.go` defines the configured limits.

## Consequences

The service remains fail-closed while no trusted provider is configured. The
host cannot claim customer authorization, admission protection, or production
readiness from the verifier's unit tests alone.

## Remaining work

Implement the authenticated caller contract, grant verification and key
rotation integration, replay store, admission semantics, stable error mapping,
and observability requirements under the established ownership boundaries.
The integration tests must pass before the host maps routes that depend on
these authorities.
