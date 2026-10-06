# Durable environment deletion contract sync

Date: 2026-08-05
Status: documentation contract synchronization. This is not runtime proof.

## Source

The server OpenAPI snapshot was synchronized from TerraScale.Internals commit `95a2551e8d62a5469ffb3d43004b015c79690160` (`Close durable environment deletion bypasses`), using `docs/product/openapi/server.openapi.json`. The checked-out source artifact matched that revision at synchronization time.

## Public contract recorded

- `EnvironmentStatus` includes `Deleting`.
- `DELETE /api/v1/projects/{projectId}/databases/{databaseId}/environments/{environmentId}` returns `DeletedProjectDatabaseEnvironmentResponse`, which exposes optional `operationId`, `status`, and nullable `retryAt` fields in addition to `deleted`.
- Completion requires both `deleted: true` and `status: "Completed"`. `deleted: false`, `status: "RetryScheduled"`, or an absent `status` is not a completion result. `retryAt` is a scheduled retry time, not completion proof. The durable fields remain optional in OpenAPI for additive compatibility, although Platform currently returns `status`.
- The snapshot does not publish a separate public operation-status endpoint. Documentation does not suggest private routes, direct data access, or generic SDK request bypasses.

## SDK drift evidence

The TypeScript SDK at commit `ae0a0e5536ba32a3abc81e0ef213ead16073d9ea` exports `Deleting`, `EnvironmentDeletionStatus`, and the optional `operationId`, `status`, and `retryAt` response fields for `client.databases.deleteEnvironment`. Its typed status includes `Completed`, `Requested`, and `RetryScheduled`.

The C# SDK at commit `ea834af3cb04884311e6eb9deb53fd512060c69b` exposes `Environments.DeleteAsync` and nullable `OperationId`, `Status`, and `RetryAt` fields on `TerraScaleDeletedProjectDatabaseEnvironment`; its public guidance requires `Deleted` and `Status == "Completed"`. Both SDK guides retain the typed public boundary. This record does not claim a runtime deletion test or service deployment.
