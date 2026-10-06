# Exploration: Deploy candidate retention

## Scope and checkout constraint

This is a read-only audit of the active, dirty candidate-retention slice in `TerraScale.Deploy`. The observed slice comprises the candidate-store command, retention implementation, and policy tests. The checkout was intentionally not modified, staged, committed, fetched, or otherwise reconciled. No Deploy files changed as part of this audit.

## Findings

1. **Promoted non-tip identities can be pruned.** Protection is derived from the current Git ref trees plus manually supplied trees. A promoted candidate that is no longer the tip tree of a retained ref has no durable promotion identity in the evaluated policy, and can become eligible after the retention period.
2. **Package and tree inputs can shape URLs.** The candidate package configuration is only checked for whitespace, and the tree input used for upload and download is not constrained to an immutable tree identifier before it is interpolated into a package URL. Path-shaped values can therefore change the request path rather than being rejected at the boundary.
3. **Final revalidation still has a delete race.** The policy re-reads an eligible version before deletion, but the delete request has no immutable version token, conditional precondition, or exclusive lease enforced by the registry. A change after that re-read can still be deleted.
4. **There is no real registry end-to-end evidence.** The added coverage is deterministic policy coverage. It does not demonstrate package listing, manifest and file metadata reads, path handling, or conditional deletion behavior against a safe Forgejo registry target.

## Safe ownership and next evidence

The Deploy candidate-retention owner should exclusively own the candidate-store command, retention implementation, and their focused tests until the slice is integrated. Preserve the unrelated dirty checkout state and do not run live registry actions without the required target-scoped lease and authorization.

Before admission, require evidence that:

- promoted candidate identities are retained independently of movable Git refs;
- package and tree values are allowlisted and URL path segments are escaped or rejected before any request;
- deletion is protected by a registry-supported immutable or conditional primitive, or an explicitly enforced exclusive lease that covers the final check and delete; and
- an environment-gated integration test runs the complete list, inspect, dry-run, confirmation, and deletion path against an isolated safe registry target, with redacted results.

These audit findings alone do not make the candidate-retention slice production-ready.
