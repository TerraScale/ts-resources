# ADR 0034: named atomic auth-storage boundary

Status: Accepted for the application boundary. The runtime adapter is blocked
on explicit TerraBase engine and terrabase-go operations.

Date: 2026-08-29

## Context

Better Auth needs a small set of security-sensitive storage operations. A
generic database route would allow arbitrary models, predicates, and scopes to
cross the public boundary. The caller's tenant, project, database, and
principal must come from an authenticated context, not request JSON or headers.

## Decision

Expose exactly three named server-only operations:

- `database.auth.insertUnique`;
- `database.auth.compareAndSwap`; and
- `database.auth.consumeOne`.

Each operation receives a typed request, a verified caller context, and an
`Idempotency-Key`. The typed store must commit atomically within that scope. A
retry with the same input returns the original result. Reusing a key with
different input conflicts. Races cannot produce two successful unique inserts
or two successful consumes. Validation enforces bounded identifiers, fields,
conditions, values, documents, and idempotency keys before storage is called.

The host's current `UnavailableAuthStorageStore` and unavailable caller-context
accessor are safe placeholders. They return failure, not an in-process storage
fallback, until a trusted adapter is composed.

## Engine and client contract gap

`terrascale.tech/terrabase-go` currently exposes document reads, writes,
deletes, readiness, and usage admission. It does not expose atomic equivalents
of `InsertUnique`, `CompareAndSwap`, or `ConsumeOne`. The Database API must
not emulate these operations with document read/write/delete calls. In
particular, read followed by delete cannot guarantee a single successful
consume under races or an unknown commit result.

TerraBase must add three explicit atomic RPCs and terrabase-go must expose
matching typed methods. Each call needs the immutable binding scope, a required
idempotency key, and one of four closed outcomes:

- `Applied`, with the committed value when the operation returns one;
- `Replayed`, with the original outcome for the same key and input;
- `Conflict`, including reuse of an idempotency key with different input; or
- `NotFound`.

`ConsumeOne` must select and remove one matching record in one atomic engine
commit. `InsertUnique` must enforce uniqueness in that same commit.
`CompareAndSwap` must evaluate its predicate and apply its update in that same
commit. A timeout or transport failure with unknown commit state remains an
unavailable response unless a retry retrieves the durable replay.

## Implementation references

- `src/database/domain/auth_storage.go` defines the typed context, mutation
  states, and bounds.
- `src/database/application/auth_storage.go` validates context, keeps the
  unavailable default, and maps unknown storage outcomes to unavailable.
- `src/database/api/auth_storage.go` maps only the three named routes.
- The auth-storage tests under `src/database/application` and
  `src/database/api` cover context, idempotency forwarding, validation, and
  the fail-closed defaults.

## Consequences

The boundary is narrow and safe to authorize. Better Auth cannot use this
surface until a real storage adapter and caller-context provider are registered
and tested under races and dependency failure.

## Open release work

The storage authority is TerraBase. Keep the host placeholder until its
protobuf service and terrabase-go implement the three atomic operations and
their durable replay outcomes. External caller-context integration remains
separate release work.
