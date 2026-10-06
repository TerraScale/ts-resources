# ADR 0002: verify live grants before issuing an engine context

Status: accepted boundary; host composition pending.

Date: 2026-08-29

## Context

The API sits between Dashboard identity and a private engine. A static service
credential or client-supplied tenant fields would let a stale or compromised
caller cross Project or Database scope. The checked-in verifier already models
signature, resource, action, policy-generation, lifetime, key, and replay
checks, but its external authorities are not composed by the host.

## Decision

Dashboard owns Better Auth and grant issuance. Each request receives a
short-lived, audience-bound grant from that authority. The Database API
verifies the signature, resource and action binding, policy generation,
expiry, key status, replay state, and the caller User/Organization/Project
scope before it issues a bounded engine context. The context is never returned
to the caller and cannot authorize a different Database, Partition, or
operation.

Denial, expiry, replay, missing authority, and provider failure fail closed and
produce the required redacted audit fact. Credential rotation has an overlap
window and explicit revocation behavior. No client header, Project ID, prompt,
or local configuration replaces live authorization.

## Verification

`src/database/application/grants.go` contains the fail-closed verifier and
`src/database/application/grants_test.go` covers its local outcomes. Host
composition remains open. Live success and denial, cross-tenant denial,
revocation, replay, clock-boundary, key-rotation, reconnect, audit-redaction,
and engine-context invalidation tests must pass through the public route before
production.
