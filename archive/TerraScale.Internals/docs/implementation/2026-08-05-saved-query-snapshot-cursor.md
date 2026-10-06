# Saved-query v3 snapshot cursor remediation

## Scope

`/api/v3/projects/{projectId}/saved-queries` remains additive. The v1 array
and v2 `skip`/`take` contracts are unchanged.

The v3 `take` query parameter defaults to 100 when omitted and accepts only
integer values from 1 through 500 when supplied. Out-of-range, negative,
zero, overflow, malformed, or repeated values return the standard validation
error (HTTP 400) before a saved-query snapshot query is attempted; they never
become a service-unavailable response.

## Collection revision collision handling

Every saved-query mutation commits both the query and its per-project
collection revision atomically. Within a Platform process, a fixed-size
per-project mutation stripe serializes the hot collection document without
unbounded lock growth. Across Platform processes, the repository reloads and
retries the complete transaction at most twelve times with capped jittered
backoff after an optimistic concurrency collision. This preserves each
successful mutation and advances the collection revision, so a previously
issued v3 cursor cannot be used after the write.

The v2 conditional update only retries when TerraBase identifies the
collection document as the conflicted document. A conflict on the target
saved-query document still returns `TERRASCALE-1401`; collection contention
cannot be reported as a stale target revision.

## Behavioral evidence

`SavedQueryV3_SnapshotPaginationIsStableAndRejectsUnsafeCursors`
exercises the AppHost API with 105 tied `UpdatedAt` values and verifies every
item is returned once across pages. It verifies that v1 create/update/delete
and a v2 target update invalidate a prior cursor, and that tampered, expired,
cross-project, and unauthenticated cursors are rejected without exposing the
cursor or a TerraBase change vector.

`SavedQueryCollectionRevision_RetriesIndependentMutations` uses the real
TerraBase repository and crypto seam from the AppHost fixture. It concurrently
performs v1 creates, a v1 update, a v1 delete, and a v2 conditional update,
then verifies success, deletion, the v2 update, and snapshot invalidation.

`SavedQueryCollectionRevision_DeterministicallyRetriesV2CollectionConflictsAndBoundsExhaustion`
uses the same real TerraBase boundary. Its per-repository, normally-null
pre-commit test aid causes a v1 write to advance the collection after the v2
transaction has read it. This forces the v2 transaction's collection conflict,
asserts its successful second commit attempt, proves a stale target revision
still has the target-stale error, and proves twelve forced collection conflicts
return the distinct collection-reload error. The aid is only a transaction
ordering hook; it neither replaces TerraBase nor changes production behavior.

`SavedQueryV3_TakeIsBoundedBeforeSnapshotQueries` seeds 101 saved queries at
the real TerraBase boundary, then reads the public v3 endpoint without a
`take` parameter and proves the returned page has 100 items and a cursor. It
also accepts the inclusive `1` and `500` bounds and proves every supplied
invalid form returns HTTP 400: an empty supplied parameter, zero, negative, over-bound, `Int32.MaxValue`,
true integer parse overflow (`2147483648`), alphabetic/decimal malformed
input, and a repeated `take` parameter. This is deliberately an AppHost
request-contract test: a supplied invalid `take` must be rejected as 400 and
cannot be allowed to become a 503 snapshot-query failure.

## Saved-query ownership manifest

This is a path-based manifest, not a contiguous commit-range claim. `git show
--name-only` confirms the following saved-query snapshot/cursor commits and
their owned paths:

- `bf442cc` — `docs/product/openapi/server.openapi.json`; saved-query
  metadata models/services/repository; `ListProjectSavedQueriesV2Endpoint.cs`;
  and the saved-query AppHost/OpenAPI contract tests.
- `da84047` — that OpenAPI file and saved-query AppHost/OpenAPI tests;
  `CoreMetadataV3EndpointGroup.cs`; v2/v3 saved-query endpoints; and
  `ProjectSavedQuerySnapshotPageResponse.cs`.
- `39df350` and `ed755be` — this implementation report, the saved-query
  AppHost test, and `TerraBaseCoreMetadataRepository.cs`.
- `abef5bc` and `9a2d381` — only the saved-query OpenAPI document/test
  contract paths.
- `28cf651` — this report, the OpenAPI document and test, the saved-query
  AppHost test, metadata service/repository, and the v3 endpoint.

The history deliberately has interleaved commits that are outside this saved-
query manifest. In particular `8deba33`, `621988e`, `7aeaddd`, `0f7fe57`, and
`d8836eb` are environment-deletion work (their `git show --name-only` file
lists are database/environment deletion tests, services, AppHost, and Dashboard
database UI paths). `6143704` is Dashboard saved-query flow work, not Platform
snapshot/cursor work. Pending Dashboard saved-query edits are not included in
Platform saved-query commits.

## Residual gate

The AppHost tests require the serialized Aspire topology and use the focused
TUnit filter. On 2026-08-05, immediately before this continuation's validation,
`/tmp/terrascale-orchestrator-validation-mariogk.lock` was present while no
ready TerraScale AppHost process was running. That external Orchestrator
validation lease is a pre-execution blocker, so the AppHost test was not
started and no real-stack result is claimed. The exact command to run after the
lease is released and a topology is available is:

```text
dotnet test --project src/Platform/TerraScale.Platform.Tests/TerraScale.Platform.Tests.csproj --no-build --no-restore --no-progress --fail-fast -- --treenode-filter "/*/*/ProjectSavedQueriesAspireAppHostIntegrationTests/*"
```

A project build alone does not establish real-stack success. Re-run that
focused command after the shared topology is available.

The non-AppHost OpenAPI snapshot class was repaired in `9a2d381`: `nextCursor`
is correctly asserted as the nullable string union in the checked-in document.
In this continuation, the test project built with zero warnings/errors and the
exact `OpenApiSnapshotContractTests.ServerSnapshot_DocumentsConditionalProjectSavedQueryV2`
filter passed. The AppHost saved-query behavioral suite remains unresolved due
to the pre-execution shared-topology gate above.
