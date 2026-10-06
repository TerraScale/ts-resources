# Durable environment deletion

Dashboard treats the typed SDK deletion result as complete only when both
`deleted` is `true` and `status` is `Completed`. A successful HTTP response with
`RetryScheduled` or `Requested` remains a pending deletion: the Dashboard
refetches environments, keeps a narrow `(databaseId, environmentId)` pending
key even when that refresh fails, returns stale `Active` data, or omits the
environment from a paged or partial list. It reports the retry time when
supplied, keeps the status and refresh action on that exact environment row,
and disables another delete action. That action performs a typed lookup of the
exact `(databaseId, environmentId)` target, updating only that row. The key
clears only after the typed delete operation returns its terminal completed
outcome or that typed target lookup returns `404` (the public API's completed
not-found representation); list data is not an authoritative terminal signal.
For a target already held in the Dashboard pending map, the typed lookup's
documented `409` / `TERRASCALE-1401` lifecycle conflict is retained as pending;
all other lookup failures remain errors. A terminal delete response removes
that exact target from any accompanying stale page list before the Dashboard
adopts it. Its immutable exact target ID then remains a session tombstone, so
later delayed or paged list responses cannot render it again; a new environment
with a different ID is unaffected. Pending entries retain their prior target
row and are overlaid into partial list results until the exact lookup completes,
so the target-specific refresh action remains available.

Terminal tombstones are bounded by broad-request generations, not by list
contents: after an exact terminal event, a tombstone remains until every broad
request that started on or before that event has settled. A later request may
not remove it merely because its page omits the target, since that omission is
not an authoritative complete-list proof. This bounds retained tombstones while
still preventing every pre-terminal delayed response from resurrecting a target.

The Dashboard route never turns browser input into a lifecycle success: typed
`404` and `409` responses remain errors at the route boundary. Only the client,
after finding the exact immutable target in its local pending map, classifies a
`404` as completed or `409` / `TERRASCALE-1401` as still pending. The default
`vp test run` state-machine test covers those classifications plus partial-list
overlay and delayed stale-list tombstones; the AppHost fault E2E remains the
separate live-stack proof.

Each pending key is scoped by its original `(projectId, databaseId, environmentId)`.
The exact-status route re-authorizes that project against the current session before
using the typed SDK client scoped to it. If Dashboard data has changed projects, old
pending entries stay dormant and cannot overlay the new project's list; a project
switch therefore cannot reinterpret a tenant-hidden `404` as deletion completion.

The Dashboard route returns `200` with `deletion.outcome: "completed"` only for
that terminal combination. It returns `202` with `deletion.outcome: "pending"`
for durable asynchronous work. A refresh failure is returned separately as
`refreshError`; it never changes a pending deletion into completion.

The test-only development AppHost supports retry-scheduled deletion responses,
a live `Deleting` refresh, and an independent one-shot Dashboard refresh fault.
The client guard deliberately preserves every pending key for each of those
response shapes.
