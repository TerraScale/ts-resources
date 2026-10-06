# MCP service hardening

## Scope

The read-only tools now convert public API, transport, timeout, cancellation, malformed-response, serialization, and unexpected failures into a small JSON error envelope. Process tests drain stderr continuously and verify that stderr cannot corrupt the JSON-RPC stdout stream.

## Contract and security decision

The MCP response exposes only a stable `error` category. A public API failure may additionally expose its numeric HTTP status and retry delay. Raw response bodies, exception messages, request IDs, headers, and credentials are never returned because those values are remote-controlled or may contain sensitive diagnostic data.

Installed `ModelContextProtocol` 2.0.0 supports `McpServerOptions.ServerInstructions`, tool titles, and explicit read-only, destructive, idempotent, and open-world annotations. TerraScale configures concise initialization instructions. All exposed tools are read-only, non-destructive, and closed-world. The backup-plan handoff is not idempotent because it asks the public API for a fresh expiring plan, but it returns only a safe projection and immediately discards the execution-capable token. These annotations are client guidance, not a security boundary: server implementation and public typed-SDK scope remain authoritative.

Static guidance resources advertise concise titles and `text/plain` MIME metadata. Prompts have titles and include inventory, usage-investigation, recovery planning, and backup approval handoff. The latter tells clients to display only the safe projection and direct the human to Dashboard or another genuine out-of-band approval authority; it never places a confirmation token in a prompt, resource, log, or chat summary. The generic recovery-review prompt declares no arguments and returns fixed read-only guidance; its tests verify the empty argument schema, stable content, and non-interpolation of hostile supplied arguments. The pinned SDK's handling of invalid prompt arguments is not asserted as a protocol-level validation mapping.

## Evidence

### P1 read-boundary hardening

All SDK response statuses pass through one local 64 KiB streaming HTTP
limit before typed deserialization or error parsing, then every projected collection is capped
at 100 items before projection. The same guard requires returned project and
requested child identifiers to match the fixed configuration and rejects a
safe projection exceeding 64 KiB with a categorical error. Bounds deny rather
than truncate, so partial data is never represented as complete. The guard returns
only `invalid_input`, `response_scope_invalid`,
`response_scope_unverifiable`, `response_limit_exceeded`, or
`response_too_large`; it never includes caller, SDK, or remote text.
Its size-limit sentinel is not a transport exception, so the typed SDK retry
policy makes exactly one request for both known-length and streaming oversize
responses, including non-success responses.

The current typed placement and restore-point models omit parent scope fields.
Those capabilities are not advertised rather than relying only on route
nesting. No endpoint, transport, selector, token, or executable operation was
added.

Organization-wide usage is not exposed: resolving a configured project’s
organization cannot make aggregate organization totals project-scoped, and the
public typed contract has no safe project-only replacement.

`McpProcessTests` covers validation, sanitized API errors, malformed payloads, concurrent stderr draining, and protocol/stderr isolation. It also uses a controlled loopback public-API response to prove that a JSON-RPC `notifications/cancelled` request produces no response for the cancelled ID and leaves the same stdio session usable. `ModelContextProtocol` suppresses cancelled-request results, so the read service’s internal `request_cancelled` category is intentionally not observable on stdio. The configured HTTP timeout remains observable and maps to exactly `request_timed_out`; its test rejects exception, credential, and raw-response leakage and is followed by a successful request. `BackupPlanHandoffAdmissionE2ETests` is discovery-time skipped unless `TERRASCALE_MCP_E2E_ENABLED=true` plus a valid session-bearing `TERRASCALE_BEARER_TOKEN`, public API base address, configured project, and approved fixture database ID are supplied. It proves the real public plan projection is scoped and that every old execution input is rejected because the execution tool is absent; optional revoked and expired bearer credentials prove expected denials when explicitly configured. It never starts AppHost or DevHost and never executes a backup.

## Backup approval handoff

`plan_database_backup` uses the reviewed typed public `TerraScale.DotNet` `Backups.PlanAsync` method only. It is limited to `TERRASCALE_PROJECT_ID`, verifies the returned project and database scope, and returns exactly action, database ID, request digest, and expiry. The Platform confirmation token is neither returned nor retained. There is no MCP execute tool, route, token cache, idempotency input, or automatic plan-to-execute bridge.

Platform confirmation tokens can authorize execution, but prompt text, MCP annotations, and an agent-observed human-approval boolean cannot provide a non-agent-controlled approval boundary. Stdio MCP therefore fails closed: it requires a visibly session-bearing bearer token for the scoped plan call, but the resulting token is discarded and execution must occur in Dashboard or another approved out-of-band authority. API-key authentication and opaque/non-session bearer tokens receive clear remediation instead of a bypass. The server still provides safe inspection of backup and restore-job metadata, but does not provide restore-point inspection, any mutation, TQL, raw documents, queues, billing, credentials, backup/restore configuration, restores, or admin operations.
