# Environment-deletion write-fence exploration

Date: 2026-08-05

Status: design evidence and implementation underway. This proposal is not validated runtime behavior, persistence proof, or a production-readiness claim.

## Problem

The existing deletion checkpoint gate can reject work that starts after a checkpoint is observed, but it cannot invalidate a writer already in flight. A mutation can pass the checkpoint, continue toward its physical project database write, and commit after deletion begins. This leaves a race between lifecycle deletion and ordinary environment mutations.

The lifecycle marker described in the [environment-deletion durability audit](review-environment-deletion-durability.md) remains necessary for durable deletion and recovery. It is not by itself a physical-write fence for concurrent writers.

## Proposed durable fence

Maintain one permanent fence record in the physical project database for every environment. The record is not removed during deletion. Its state is:

- `Active`, with a current generation and operation identifier.
- `Deleting`, with the deletion operation identifier that sealed it and the generation that was active when sealing began.

Deletion must atomically compare and exchange this record from `Active` to `Deleting` before environment metadata is changed to `Deleting` and before any physical cleanup is allowed. The compare-exchange must reject a conflicting deletion operation and preserve the winning operation identifier for deterministic retry and diagnosis.

Each environment mutation must include an atomic compare-exchange assertion of the expected `Active` state, generation, and operation identifier in its clusterwide `SaveChanges` transaction. A successful commit is therefore coupled to a still-active fence, rather than relying on a prior in-process checkpoint read. A stale mutation that reached its commit point after the deletion seal must fail and return through the normal retry or conflict handling path. It must not recreate or modify environment data.

An environment create path must recheck the same fence after its checkpoint and immediately before its clusterwide commit. This covers a create that began while the environment was active but crosses the deletion seal before it writes.

The permanent `Deleting` record is a tombstone. It must remain after physical cleanup and metadata finalization so delayed writers and retried creates continue to fail instead of treating an absent record as permission to recreate state. Any future, explicitly designed environment identity reuse must allocate a new generation under a separately authorized lifecycle operation; it must not silently overwrite this tombstone.

## Required ordering

1. Resolve the environment fence in the physical project database.
2. Compare-exchange `Active` to `Deleting` with the deletion generation and operation identifier.
3. Persist the lifecycle metadata transition to `Deleting` only after the seal succeeds.
4. Perform idempotent physical cleanup and metadata finalization through the durable deletion workflow.
5. Retain the `Deleting` tombstone after finalization.

If a metadata transition fails after the seal, recovery must continue from the durable deletion operation and must not reopen the fence. If sealing fails because a different deletion operation already owns the fence, the caller must converge on that recorded operation rather than beginning competing destructive work.

## Proof plan

The implementation needs real concurrent-boundary tests, not mocked or fake persistence:

- Use a test barrier to pause a mutation after its initial checkpoint and before the clusterwide `SaveChanges` compare-exchange assertion. Seal deletion, then release the mutation and prove that the stale commit fails and writes no environment data.
- Use the same barrier pattern for create: start create, pass its checkpoint, seal deletion, release it, and prove the post-checkpoint recheck plus commit assertion rejects the create.
- Exercise deletion while concurrent write and create attempts are blocked, then verify the fence is `Deleting`, carries the winning generation and operation identifier, and remains as a tombstone after deletion finalization.
- Retry stale mutation, create, and deletion requests to prove that they converge on the fence state and do not recreate data or start a second deletion operation.

These tests must use a real clusterwide persistence boundary. The current live test environment does not yet provide the required barrier and concurrent write/create-delete execution proof. Until that limitation is removed and the tests pass, this record must not be cited as validation that the race is closed.

## Tradeoffs

Every environment mutation adds a clusterwide compare-exchange condition, increasing write-path coordination and contention relative to a checkpoint-only read. During deletion, availability for that environment intentionally changes: new writes and creates fail rather than waiting indefinitely or racing cleanup. The permanent tombstone also consumes retained metadata and requires an explicit identity-reuse policy.

These costs are deliberate. They trade a small steady-state write coordination cost and a clear deletion-time rejection mode for a durable, database-enforced guarantee that an already-started writer cannot commit after deletion has been sealed.

## Constraints

- Do not substitute in-memory flags, mocked stores, or fake persistence for the physical project-database compare-exchange and clusterwide transaction.
- Do not publish this internal design as a public API contract or imply a new customer-visible endpoint, SDK method, or Dashboard-specific behavior.
- Preserve tenant, authorization, and public-contract boundaries throughout the implementation and test harness.
- Keep test data nonsecret and non-identifying. Do not record credentials, fixture identities, internal hostnames, or environment values in this evidence.
