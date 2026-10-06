# Durable environment deletion

## Admission and recovery

Deletion admission is one TerraBase cluster-wide metadata transaction: it stores the
deterministic `(projectId, databaseId, environmentId)` job and changes the live
environment from `Active` to `Deleting` together. `Deleting` is immediately
non-writable. A duplicate request returns the same job; if a previously persisted
non-completed job is discovered with an `Active` environment, the same transaction
repairs the environment to `Deleting` before returning it.

The job begins in `Admission`. A leased worker first seals the physical partition with
the compare-exchange deletion fence, then records `Cleanup`, removes the partition's
repositories, and atomically removes the `Deleting` environment while completing the
job and writing one deterministic audit event. Retry before the physical seal remains
in `Admission`; retry after it remains in `Cleanup`. The missing-physical-database path
also moves through `Cleanup`, removes only metadata/repository definitions, and cannot
later recreate the deleted environment.

This is deliberately not a cross-database transaction. Metadata admission prevents
new normal mutations before their native side effects. The later physical
compare-exchange fence invalidates a physical write already in flight when admission
committed, before cleanup can remove its partition. Internal cleanup carries the
matching deletion permit and is the only path allowed through the physical fence.

## Mutation guards

Repository create, document writes, and repository maintenance all check durable
environment metadata for `Active` before proceeding; document saves also include the
physical compare-exchange fence in their cluster transaction. Reads retain their
existing rejection once the physical fence is present. No guarantee is made for raw
TerraBase/RQL access that bypasses Platform's repository seam.

## Response contract

The delete response has `deleted: true` only after metadata finalization. It exposes
`operationId`, `status`, and nullable `retryAt`; a durable pending retry returns
`deleted: false` and `RetryScheduled`. `EnvironmentStatus` includes `Deleting`.

## Real-stack proof and validation

`ProjectDatabaseEnvironmentDelete_AdmissionRejectsMutationsBeforePhysicalFenceAndRecovers`
uses the local AppHost and real TerraBase. Its Development-only, header-scoped barrier
pauses a deletion only after atomic metadata admission and before the physical fence.
The test observes the durable `Requested/Admission` job and `Deleting` environment,
proves no physical fence exists yet, verifies public document and repository creation
both reject, releases the bounded barrier, and verifies one cleanup/completion audit.
The barrier is enabled only by the existing AppHost test switch and times out after 20
seconds; it is not persistence or a production control path.

`dotnet build -m src/Platform/TerraScale.Platform/TerraScale.Platform.csproj --no-restore`
and `dotnet build -m src/Platform/TerraScale.Platform.Tests/TerraScale.Platform.Tests.csproj --no-restore`
passed after this change. The exclusive AppHost test result is recorded with its exact
command when run; no live pass is claimed before then.
