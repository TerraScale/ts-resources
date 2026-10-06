# Environment-deletion durability audit

Date: 2026-08-05
Status: reviewer evidence record. Implementation is underway and has not been validated.

## Scope

This read-only audit records the durability risk in environment deletion and its propagated deletion and cleanup paths. It covers the ordering between physical repository documents, indexes, and schema artifacts, and the repository-definition and environment metadata that represents the active environment. It also covers the database and project deletion routes that use the same path, plus restore cleanup.

This is not an implementation record or a statement that a durable deletion workflow is available.

## Evidence

The reviewer finding is that the current path removes physical repository documents, indexes, and schema before it removes the repository definition and environment metadata. The same ordering is propagated by database deletion, project deletion, and restore cleanup.

The audit was read-only. It records the observed ordering and its consequences, without using credentials, customer data, fixture identities, or environment-specific values.

## Finding and impact

If physical deletion succeeds and a later metadata operation fails, the repository definition and environment metadata can remain active even though the associated data has been erased. Consumers can then observe an active environment that cannot satisfy its represented state.

Because database deletion, project deletion, and restore cleanup route through the same path, the inconsistency is not limited to a direct environment delete. Retrying an incomplete request without a durable lifecycle marker also leaves no reliable basis for distinguishing a safe retry from a duplicate destructive action.

## Recommended state machine

Use a deterministic, leased deletion job as the sole executor of physical deletion.

1. Route environment, database, project, and restore-cleanup deletion requests through the same higher-level lifecycle entry point.
2. Atomically persist a `Deleting` marker and the deletion-job intent before physical repository work begins.
3. Have a leased worker perform physical document, index, and schema deletion idempotently. Retries must converge when prior attempts partially completed.
4. After physical work is confirmed complete, atomically finalize repository-definition and environment metadata removal with the corresponding audit record.
5. Treat lease expiry, worker interruption, and metadata-finalization failure as resumable job states. A later worker must resume from durable state rather than starting an unrelated deletion sequence.

The final metadata transition and audit write must be atomic with respect to the lifecycle decision, so no successful terminal deletion exists without immutable evidence and no active metadata remains after successful physical cleanup.

## Test plan

- Add a real TerraBase fault-injection test that fails after physical deletion and before final metadata and audit finalization.
- Verify that the pre-work `Deleting` marker is durable and that a leased retry resumes safely.
- Verify idempotence across repeated worker attempts for already deleted documents, indexes, and schema artifacts.
- Exercise direct environment deletion, database deletion, project deletion, and restore cleanup to prove they use the same higher-level lifecycle route.
- Verify the terminal state atomically removes active metadata and records the expected audit evidence.
- Run the test only with nonsecret, non-identifying test inputs. Do not include credentials or fixture identities in logs, assertions, commits, or this record.

## Constraints

- Keep the audit read-only until the implementation and real TerraBase fault-injection test are complete.
- Do not claim that the proposed state machine, worker, routing, or test is implemented or validated.
- Preserve existing tenant, authorization, and public-contract boundaries. This durability workflow must not create a bypass through direct data access or private customer-facing behavior.
- Keep deletion execution deterministic, idempotent, and recoverable from process failure. A request must not depend on ephemeral in-process state to reach a safe terminal result.
