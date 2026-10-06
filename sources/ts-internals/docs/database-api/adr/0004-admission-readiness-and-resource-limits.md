# ADR 0004: fail closed on readiness and bounded admission

Status: accepted boundary; implementation and calibration pending.

Date: 2026-08-29

## Decision

Readiness is true only when the configured engine, trust, workload identity,
authorization dependencies, and required public adapters are healthy. Missing
or partial production configuration keeps the instance out of service. The
service enforces configured request-body, response, frame, query, stream,
concurrency, queue, and deadline limits before allocating unbounded work.

Backpressure and typed overload responses protect the engine and other tenants
while Orchestrator adds capacity. Autoscaling is not the isolation boundary.
Cancellation drops abandoned engine work, and retries occur only for a
documented transient operation with a stable idempotency key.

## Verification

The engineering contract must record the limit and SLO values. Tests must
cover malformed and oversized input, slow consumers, concurrent callers,
cancellation, engine loss, stale readiness, recovery, and noisy-tenant
isolation.
