# Plan: apply MCP `2026-07-28` stateless support to TerraScale.MCP

**Status:** repository implementation and deterministic validation complete; production rollout remains blocked on the Orchestrator hosting/authentication gate.<br>
**Owner:** TerraScale.MCP maintainers<br>
**Implementation base:** `develop` at `85d799463ce4d9f37d1374d21c4567829986ab22` with SDK gitlink `65c0fb57c808ccb95cd26729aa15e237039b1220`.<br>
**Related research:** [docs/research/2026-08-16-mcp-2026-07-28-stateless.md](docs/research/2026-08-16-mcp-2026-07-28-stateless.md)

**Architectural decision:** add an independently published `TerraScale.MCP.Http`
host beside the existing stdio host. The HTTP host is explicitly stateless on the
MCP `2026-07-28` path and uses configurable, fail-closed authentication. It does
not share the stdio operator credential, pass caller tokens through to TerraScale,
or add a session cache. Production issuer, resource, route, caller-client
allowlist, and ingress values remain deployment inputs; no concrete production
inventory or live issuer evidence is asserted by this plan.

## 1. Outcome

Add an approved, public remote MCP transport that speaks the MCP `2026-07-28` stateless protocol while preserving the current local stdio server as a separate delivery. The resulting system must remain a fixed-project, read-only TerraScale integration using only the released typed TerraScale .NET SDK and versioned public APIs.

The repository implementation is complete only when a remote request can be handled
by any healthy instance without MCP session affinity or an in-memory session store,
while authentication, project scope, safe projections, redacted errors, timeouts,
and stdio behavior remain intact. Production readiness additionally requires the
Orchestrator deployment gate and live authentication evidence, which are not present
in this repository.

## 2. Non-goals and hard boundaries

- Do not replace or weaken the existing stdio server.
- Do not expose Platform, Dashboard, TerraBase, internal RPC, private routes, generic SDK requests, or direct storage.
- Do not add writes, deletes, backup execution, restore execution, billing, credentials, identity, permission, queue, TQL, raw-document, or administrative tools.
- Do not treat `Mcp-Session-Id`, MRTR input, tool annotations, prompts, client UI, or a human-approval boolean as authorization.
- Do not make the remote server multi-project. Keep `TERRASCALE_PROJECT_ID` as the configured scope until a separate public product contract explicitly changes it.
- Do not add Cloudflare Workers, `McpAgent`, Durable Objects, or Cloudflare OAuth dependencies to this C# repository.
- Do not add a public ingress or production infrastructure configuration here. AppHost/Orchestrator admission is a separate, approved change.
- Do not adopt deprecated Roots, Sampling, Logging, Dynamic Client Registration, or HTTP+SSE for new behavior.

## 3. Current baseline

The current local executable is `src/TerraScale.MCP`; the additive HTTP executable is
`src/TerraScale.MCP.Http`:

- `Program.cs` configures `.WithStdioServerTransport()` and registers tools, resources, and prompts from the assembly.
- `ModelContextProtocol` is pinned to `2.0.0`; the project targets the pinned .NET 11 preview toolchain with warnings as errors.
- TerraScale API calls use the public typed SDK through `TerraScaleReadService` and `TerraScaleConfirmedBackupService`.
- Configuration supplies one environment credential and a fixed `TERRASCALE_PROJECT_ID`.
- Existing tests prove stdio protocol resilience, scope checks, safe projections, bounded responses, cancellation/timeout behavior, and stderr/stdout isolation.
- `src/TerraScale.MCP.Core` links the transport-neutral safe surface and typed client
  factory boundary without making stdio reference ASP.NET Core.
- `src/TerraScale.MCP.Http` configures the official ASP.NET Core transport with
  `Stateless = true`, maps `/mcp`, and maps protected-resource metadata plus
  liveness/readiness endpoints.
- HTTP configuration is separate from stdio and requires RFC 7662 introspection,
  RFC 8693 token exchange, a fixed project, a pre-registered caller-client
  allowlist, and explicit HTTPS/Origin policy. The exact variables are documented
  in [the HTTP guide](docs/guides/2026-08-16-mcp-v2-http.md).
- The current source has no production ingress configuration or MCP session store.

The clean baseline passed 76 deterministic tests with two credential-gated live
tests skipped. The integrated implementation passes locked restore, a warning-free
Release build, and 130 deterministic tests with those same two live tests skipped.
Release tooling additionally verifies the separate HTTP archive contract, checksum,
SBOM, provenance, and tamper boundary. Live public issuer/client and deployed-route
evidence remains unavailable.

## 4. Target architecture

### 4.1 Preserve stdio

Keep `src/TerraScale.MCP` as the local stdio entry point and keep its current client configuration and artifact packaging. Do not make HTTP mode selectable by an untrusted environment flag in the same binary; this could accidentally turn a local credential-bearing process into a listener.

### 4.2 Separate HTTP host (implemented in the repository)

The repository contains the dedicated executable project `src/TerraScale.MCP.Http`
and transport-neutral project `src/TerraScale.MCP.Core` in the same solution. They:

1. Reference the shared typed SDK and the safe TerraScale MCP tool/resource/prompt implementations through an intentionally reviewed composition boundary.
2. Use the official `ModelContextProtocol.AspNetCore` package at the SDK version compatible with the pinned `ModelContextProtocol` 2.0.0 line; update lock files with locked restore.
3. Configure the HTTP transport explicitly with `Stateless = true` and map one MCP endpoint at `/mcp`.
4. Construct an isolated MCP server/registration context per request (the SDK’s stateless factory pattern), without an MCP session cache or per-session execution context.
5. Keep service state request-safe. Singleton services are permitted only after review proves they contain no caller, project, request, or transport state; otherwise use scoped/transient lifetimes.
6. Keep the HTTP host’s authentication and configuration separate from the stdio environment-token model. A remote caller must authenticate through an approved public authentication boundary; the server must not use one operator bearer token for all remote callers.

The ownership boundary is explicit: stdio remains free of ASP.NET Core/public-listener
dependencies, while HTTP composes the shared safe surface through Core.

### 4.3 Modern protocol behavior

The host relies on the official SDK for the wire implementation. Real child-process
tests prove the following at the HTTP boundary:

- Modern requests use `MCP-Protocol-Version: 2026-07-28`.
- `Mcp-Method` and `Mcp-Name` are present when required and match the JSON-RPC body; mismatches fail closed.
- `server/discover` works without an `initialize` handshake.
- No `Mcp-Session-Id` is minted, required, stored, or echoed on the modern path.
- A request returns one JSON result or a request-scoped SSE result stream; a later request can land on another process.
- Legacy compatibility, if required by an approved client inventory, is stateless compatibility only. Do not add a stateful legacy route unless a separate decision accepts its session, drain, and replay costs.

### 4.4 Authentication, authorization, and scope

The implemented HTTP host fails closed with configuration supplied by the approved
deployment contract. The request pipeline must:

1. Require HTTPS outside explicitly approved local development loopback.
2. Validate `Origin` when present and reject invalid origins to prevent DNS-rebinding attacks.
3. Validate the authorization issuer and issuer-bound credentials.
4. Validate the MCP resource/audience of the access token.
5. Derive the authenticated caller from the trusted auth boundary, never from `_meta`, a tool argument, or a client-generated handle.
6. Enforce the configured `TERRASCALE_PROJECT_ID` on every SDK read and verify returned parent/child scope before projection.
7. Return only the documented safe error envelope. Never return token claims, raw headers, exception text, request IDs, response bodies, or provider payloads.

The implementation uses RFC 7662 introspection and RFC 8693 token exchange with a
pre-registered confidential host client plus a deployment-configured allowlist of
pre-registered caller client IDs. It does not implement CIMD or Dynamic Client
Registration. The concrete issuer, resource, endpoint, client inventory, and route
values remain deployment inputs.

### 4.5 Application state and long-running work

The first HTTP release should expose only the existing request/response read surface and the existing read-only backup-plan handoff. It should not implement MRTR, Tasks, or client-visible state handles unless a product workflow specifically requires them.

If a later workflow needs continuity:

- Mint a typed, short-lived handle server-side.
- Bind it to authenticated caller, configured project, operation, canonical payload digest, expiry, and idempotency key as applicable.
- Store durable state in an approved product-owned store or workflow.
- Validate and consume the handle server-side; never trust client-supplied approval or authorization fields.

If a later workflow needs elicitation, use MRTR (`input_required` and a retried request) only after the operation’s independent approval authority and audit protocol have been approved. MRTR is not an admission boundary.

## 5. Implementation phases

### Phase 0 — decision and evidence baseline

**Status:** architectural decision and repository evidence complete; production
admission is pending.

**Deliverables**

- Confirm product approval for a remote MCP endpoint and its intended clients.
- Name the owning host/ingress repository and the public authentication authority.
- Produce the compatibility matrix below with concrete client versions.
- Run and record the current suite and package/SDK provenance from a clean `develop` checkout.

**Evidence and gap**

The approved repository decision is additive separate hosting with configurable,
fail-closed authentication. The HTTP guide records the RFC 7662/RFC 8693 contract,
pre-registered caller-client requirement, and exact configuration surface. The
concrete production issuer, route, client inventory, and live authorization fixture
are still deployment inputs; their absence blocks production, not repository-level
implementation or deterministic testing.

### Phase 1 — host and package skeleton

**Status:** repository implementation and deterministic artifact validation complete.
Production artifact admission remains separate.

**Owned paths**

- `src/TerraScale.MCP.Http/**`
- `TerraScale.MCP.sln`
- `Directory.Build.props` only if a shared setting is genuinely required
- HTTP project package lock

**Work**

- Add the HTTP executable and official ASP.NET Core MCP transport package.
- Register `Stateless = true` explicitly and map `/mcp`.
- Add a health/readiness shape that does not expose project metadata, credentials, or internal diagnostics.
- Compose the existing safe service surface without exposing a generic request escape hatch.
- Keep HTTP logging off stdout and configure bounded, redacted diagnostics.

**Evidence and gap**

The solution includes `TerraScale.MCP.Core` and `TerraScale.MCP.Http`; the HTTP host
sets `Stateless = true`, maps `/mcp`, and maps metadata/health endpoints. Real
process tests prove startup and modern discovery. Four self-contained HTTP RID
archives, checksums, CycloneDX SBOM, and candidate provenance are independently
generated and verified outside the stdio `.mcpb` artifacts.

### Phase 2 — request pipeline and safe projections

**Status:** complete for repository implementation and deterministic validation.

**Owned paths**

- HTTP host middleware/auth composition
- Shared MCP service files only where a transport-neutral hardening fix is required
- New HTTP-specific configuration and authorization tests

**Implemented behavior and remaining gate**

- Trusted RFC 7662 authentication and issuer/audience/resource/client/scope/project
  validation are implemented, followed by caller-bound RFC 8693 exchange.
- `Origin` and HTTPS enforcement include the explicit all-loopback development
  exception.
- The official transport is configured for stateless modern protocol handling and
  the host does not maintain an MCP session store.
- Existing scope checks, bounded input, response limits, safe projections, redacted
  errors, and 30-second SDK timeout behavior remain composed through Core.
- `plan_database_backup` remains a read-only handoff; the exchanged token and any
  execution-capable Platform token are not exposed, and no execute route exists.

**Gate evidence**

Deterministic configuration, authentication, exchange, real-process, shared safety,
and stdio regression tests prove unauthorized, wrong-audience, wrong-project,
invalid-origin, invalid-header, malformed-body, timeout, cancellation, and
oversized-response behavior fails closed without sensitive leakage.

### Phase 3 — modern protocol and compatibility tests

**Status:** deterministic implementation and protocol-boundary evidence complete.
No live issuer/client or deployed-route evidence is available.

**Owned paths**

- `tests/TerraScale.MCP.Tests/**` for deterministic tests
- `tests/TerraScale.MCP.TestChild/**` only if a child process is needed for HTTP/stdio isolation

**Work**

Add deterministic process or in-process HTTP tests for:

- `server/discover` and a tool call without `initialize`/`initialized`.
- No `Mcp-Session-Id` creation, requirement, storage, or echo.
- Correct `MCP-Protocol-Version`, `Mcp-Method`, and `Mcp-Name` behavior.
- Header/body mismatch rejection.
- Independent requests handled by two server instances with no sticky routing or shared MCP session state.
- Safe handling of JSON responses and request-scoped SSE responses.
- Deterministic list ordering and cache metadata where exposed by the SDK.
- Per-request trace metadata handling without leaking trace data in projections or errors.
- Authentication issuer/audience/resource and configured-project denial cases.
- Cancellation, client disconnect, retry, and timeout behavior.
- Existing stdio protocol behavior and stderr/stdout isolation after the solution gains a second host.

Do not use mocks, fakes, or stubs to bypass the TerraScale API boundary. Environment-gated live tests may use approved public API fixtures and redacted identifiers only.

### Phase 4 — staged rollout and operations

**Status:** not started; blocked on the Orchestrator deployment/ingress gate and
concrete production issuer/client/route inputs.

**Work**

- Deploy only through the approved AppHost/Orchestrator path; do not add production ingress here.
- Start with a private/allow-listed route and an explicit client cohort.
- Observe request method/name, status, latency, retry, auth-denial, and scope-denial metrics without logging credentials, raw payloads, or sensitive tool arguments.
- Verify horizontal routing across at least two instances.
- If legacy clients are approved, run the compatibility path beside the modern path, track active sessions, and define a drain/removal date within the deprecation window.
- Retain the stdio artifact and configuration as the rollback path.

**Rollback**

Disable the HTTP route at the owning ingress/host, revoke the remote client registration or audience, and keep the stdio release available. Do not roll back by reintroducing a hidden session cache or enabling mutation behavior.

## 6. Compatibility matrix

| Contract surface | Producer | Consumer(s) | Landing order | Compatibility validation |
| --- | --- | --- | --- | --- |
| MCP `2026-07-28` stateless HTTP `/mcp` | New `TerraScale.MCP.Http` host plus official C# SDK transport | Approved remote MCP clients and the auth/ingress boundary | Auth/route contract, then producer, then client enablement | Modern discovery, header/body consistency, no-session behavior, independent-instance routing, auth/scope denial tests |
| Existing stdio MCP contract | Existing `src/TerraScale.MCP` host | Codex, Claude Desktop, and generic stdio clients | Preserve first; HTTP lands additively | Existing process/protocol suite remains green; artifact manifests/config examples unchanged unless explicitly versioned |
| TerraScale public typed SDK reads | Existing TerraScale API/SDK contract | Both MCP hosts | No contract change; verify released SDK first | Typed compile boundary, scope verification, safe projection/error tests, live read evidence where approved |
| Caller authentication and API token exchange | Approved public auth authority plus configured HTTP host (RFC 7662/RFC 8693) | HTTP host, ingress, remote clients, TerraScale API | Pre-register host/caller clients and publish issuer/resource metadata, then host, then clients | Issuer, resource/audience, client allowlist, scope/project, expiry, invalid-origin, unauthorized, and exchanged-token evidence |
| Separate HTTP release artifact | MCP bundle tool and `TerraScale.MCP.Http` | Orchestrator deployment pipeline | Build/verify HTTP archives independently after source/package validation | Four RID archives, checksums, CycloneDX SBOM, candidate evidence, and no HTTP payload in stdio artifacts |
| Optional legacy HTTP compatibility | New HTTP host/SDK compatibility path | Named legacy clients only | Modern path first; legacy only if approved | No stateful session dependency unless separately approved; client inventory and drain evidence |

## 7. Validation and release gates

Before handoff, all of the following must be recorded with redacted evidence:

1. Exact source commit, package lock, SDK gitlink revision, target framework, and HTTP artifact hash.
2. Locked restore, solution build, all deterministic tests, and release-artifact verification.
3. Modern MCP protocol evidence for discovery, tool/resource/prompt dispatch, headers, no-session behavior, and independent-instance routing.
4. Authentication evidence for valid caller, invalid issuer, wrong audience/resource, expired/revoked credential, and missing credential.
5. Scope-denial evidence for the configured project and a protected expected-403 project; no project IDs or credentials in output.
6. Security evidence for Origin/DNS-rebinding protection, HTTPS enforcement, bounded requests/responses, safe errors, and no stdout contamination.
7. Live public-API success/failure evidence for only the approved read routes, with an exclusive fixture lane where required.
8. Confirmation that no mutation tool, execution route, token cache, raw API escape hatch, internal RPC, or unapproved infrastructure changed.
9. Deployment/ingress owner, route status, client cohort, lease cleanup, rollback path, and push state for every affected repository.

## 8. Suggested file change set

The implementation should stay within this bounded set unless a gate explicitly expands it:

- `src/TerraScale.MCP.Http/**` — new stateless HTTP host and transport composition.
- `src/TerraScale.MCP/TerraScale*.cs` — only transport-neutral safety/configuration changes proven necessary for both hosts.
- `tests/TerraScale.MCP.Tests/**` — deterministic HTTP, auth, header, routing, and regression tests.
- `tests/TerraScale.MCP.TestChild/**` — process fixtures only when required to prove isolation.
- `TerraScale.MCP.sln` and HTTP package lock — solution/package registration.
- `tools/TerraScale.MCP.Bundle/**` — separate HTTP RID archives, checksums, SBOM,
  and candidate provenance; never place the HTTP executable inside a stdio bundle.
- `README.md` and `docs/guides/**` — only after the implementation and release evidence exist; document the separate HTTP setup and preserve the stdio warning.
- `PLAN_MCP_V2.md` — update phase status and evidence links as work lands.

Do not modify `TerraScale.Orchestrator`, `TerraScale.Internals`, retired infrastructure stubs, or SDK contract repositories as part of this plan without a new cross-repository compatibility decision.

## 9. Done definition

The plan is complete when the new HTTP host is explicitly stateless on the `2026-07-28` path, horizontally routable without MCP session affinity, authenticated and project-scoped on every request, covered by deterministic and approved live evidence, and independently releasable from the existing stdio binary. The current read-only/mutation-deny policy, safe projection rules, and transport boundaries must remain unchanged.

## References

- [MCP `2026-07-28` stateless research](docs/research/2026-08-16-mcp-2026-07-28-stateless.md)
- [Cloudflare — The next generation of MCP](https://blog.cloudflare.com/mcp-v2/)
- [MCP — The `2026-07-28` specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
- [MCP C# SDK — Stateless and stateful mode](https://csharp.sdk.modelcontextprotocol.io/v2/concepts/stateless/stateless.html)
- [MCP C# SDK — Transports](https://csharp.sdk.modelcontextprotocol.io/v2/concepts/transports/transports.html)
- [MCP C# SDK v2 announcement](https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/)
