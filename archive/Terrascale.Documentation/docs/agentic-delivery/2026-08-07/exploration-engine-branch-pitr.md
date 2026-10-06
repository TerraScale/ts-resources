# Exploration: engine branches and point-in-time recovery

## Scope and evidence

This is an architecture exploration, not an implementation or live-validation claim. It is based on the checked-in TerraBase recovery and backup sources at `43085f63a3272da67d41a2362e094159aefdb765`, including `RecoveryPointManifest`, local restore discovery, and periodic snapshot backup paths.

## Current boundary

`RecoveryPointManifest` is a versioned, local archive-integrity selector. It records an ordered local archive set and digests after a successful local backup upload, then restore admission validates that selected set. It is not arbitrary-time PITR, a physical branch primitive, remote artifact support, or a control-plane feature.

Snapshot backup supplies a Voron-consistent backup and restore mechanism. Voron copy-on-write behavior supports storage and recovery mechanics, but does not establish durable branch identity, isolation, lifecycle, or routing. The checked-in engine has no durable recovery timeline, lineage graph, or cutover protocol.

## Production-required architecture

- A versioned recovery timeline that binds immutable artifact identities, ordering, timestamps, coverage, integrity metadata, retention state, and lineage to a source database.
- Cryptographic artifact and key references only. Key material must remain in an approved key-management boundary and never appear in manifests, events, logs, or public responses.
- An independent materializer that verifies the selected timeline and artifacts, reconstructs a target without mutating the source, and emits evidence of the resulting immutable recovery point.
- Versioned public branch and cutover state machines with explicit authorization, idempotency, cancellation, failure, readiness, and audit states. Cutover must use a separately authorized, reversible-or-compensated routing transition.
- A tenant-aware production control plane for tenancy, quota, placement, lifecycle, routing, policy, and audit. It is not an engine-local responsibility.

## Staged delivery and evidence gates

1. Define the recovery timeline and artifact-reference contracts, compatibility rules, retention model, and threat model. Gate on reviewed schema and key-reference-only invariants.
2. Build and test timeline capture and validation against real backup and restore boundaries. Gate on tamper, omission, ordering, encryption-reference, retention, and version-compatibility coverage.
3. Build an isolated materializer. Gate on repeatable restore drills, source non-mutation, data-consistency checks, cleanup, and fault recovery.
4. Add public branch lifecycle contracts and a tenant control-plane implementation. Gate on contract compatibility, tenant authorization and isolation, quotas, idempotency, auditability, and lifecycle integration evidence.
5. Add cutover orchestration only after branch readiness is proven. Gate on controlled traffic transition, rollback or compensation behavior, concurrent-operation handling, and an end-to-end recovery drill.

## Limitations and decision

The current engine evidence is sufficient only for local recovery-point selection and snapshot backup/restore mechanics. It does not prove arbitrary-time recovery, durable lineage, independent materialization, tenant isolation, branch lifecycle, cutover, routing, retention enforcement, or production readiness. Any future public capability must be introduced through a versioned control-plane contract and validated at each engine, control-plane, and customer boundary.
