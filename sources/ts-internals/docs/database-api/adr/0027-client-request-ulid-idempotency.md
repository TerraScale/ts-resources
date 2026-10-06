# ADR 0027: client-request ULIDs for document mutation idempotency

Status: Accepted and implemented for document mutations.

Date: 2026-08-29

## Context

Network failure can occur after TerraBase commits a mutation and before the
client receives its response. Retrying with a new identity could commit twice.
The engine's write and delete frames already carry an operation identity and an
idempotency key.

## Decision

Every public document mutation requires `Idempotency-Key`. The API accepts only
the canonical 26-character uppercase Crockford Base32 ULID shape implemented
by `DocumentService`. One logical mutation must reuse the same value across
retries. The gateway sends the value both as the frame idempotency key and as
the operation identity. A committed response is valid only when the engine
response echoes that same identity. A mismatch is a protocol failure, not a
successful write.

The public operation maps remain named:

- create sends the `Absent` expected-version precondition;
- patch reads the current version, applies RFC 7396 merge patch, and sends an
  `Exact` expected-version precondition; and
- delete sends the `Any` expected-version precondition.

The engine owns durable replay records. The API does not invent a local commit
or claim success when the engine outcome is unknown.

## Verification

- `src/database/application/documents.go` validates the ULID and request bounds.
- `src/database/adapters/document_gateway.go` sends the identity through
  `terrabase-go` and checks the typed response.
- `src/database/application/documents_test.go`,
  `src/database/api/documents_write_test.go`, and
  `src/database/adapters/document_gateway_grpc_test.go` cover retries,
  preconditions, merge semantics, and gRPC mapping.

## Consequences

Clients need a stable request identity for each logical mutation. The API can
return a typed conflict or unavailable result without turning uncertain commit
state into a second write. This decision applies to document mutations only;
auth-storage idempotency has its own contract and usage export has checkpoint
identity.

## Open release work

`@terrascale/sdk` must expose the same retry rule. Contract and live-engine
tests must preserve the exact value through a retry.
