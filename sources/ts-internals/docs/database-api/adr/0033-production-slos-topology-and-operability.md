# ADR 0033: production gates for the Database API

Status: accepted production gate; implementation in progress.

Date: 2026-08-29. Updated: 2026-08-31.

## Decision

The Database API is not production-ready until all of the following hold:

- every launch region runs at least two disposable API instances with no
  instance-owned customer or routing state;
- deployment supplies HTTPS endpoints, workload identity, gRPC endpoints,
  trust roots, and certificate rotation;
- readiness checks the real engine within a bounded timeout while liveness
  remains independent;
- request admission authenticates and authorizes every operation, rejects
  replay, and keeps secrets out of logs and errors;
- request bodies, dependency calls, reactive sessions, result streams, and
  shutdown are bounded and cancelable;
- real TerraBase, restart, rolling-upgrade, dependency-outage, restore, and
  rollback tests pass; and
- the service meets the workspace latency, availability, recovery, paging,
  and seven-day soak requirements.

This ADR sets production gates. It does not invent numeric SLOs,
ports, regions, certificate authorities, alert thresholds, or retention values
that the repository does not contain.

Orchestrator owns routing, topology, workload identity, service supervision,
and observability operations. The Database API owns its public routes,
application admission, private client configuration, and health behavior.
Listener endpoints remain deployment-supplied.

## Current checks

Current repository checks include configuration validator tests, health
endpoint tests, local mTLS gRPC fixtures through the official `terrabase-go`
client, typed grant unit tests, and a protected live-engine workflow. These do
not qualify a deployed production topology or close the D-30 raw document-byte
gap.

## Consequences

The service remains fail closed while a required dependency is absent. The
full local Go verification set is required before integration. Production
sign-off also requires the environment-gated tests and operational runbooks
named by the workspace goal.
