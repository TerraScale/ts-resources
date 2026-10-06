# TerraScale MCP

`terrascale-mcp` is a standards-compliant, read-only stdio [Model Context Protocol](https://modelcontextprotocol.io/) server for safe TerraScale discovery and backup-approval handoffs. It uses the official C# MCP SDK 2.0.0 and only the public TerraScale .NET SDK.

It exposes the public region catalog plus typed configured-project metadata, databases/environments, usage, latency, safe recovery inspection, and a scoped backup-plan handoff. It never executes mutations or exposes organization-wide usage, cross-project discovery, deletes, credentials, billing accounts/invoices/checkout/portals, queues, raw documents, backup policy/configuration, restores, admin actions, or TQL.

## Release-candidate installation

This repository currently produces release-candidate artifacts only; its CI does not create an external Forgejo release or publish a package. A candidate contains five `.mcpb` bundles, five standalone archives, `checksums.json`, `standalone-checksums.json`, a deterministic CycloneDX 1.6 `candidate-sbom.cdx.json`, and `candidate-evidence.json` for `win-x64`, `osx-arm64`, `osx-x64`, `linux-arm64`, and `linux-x64`. The contract and bundle distribution version is `0.1.0`; candidate evidence binds that version and the contract digest to the exact source revision, SDK/lock provenance, and per-artifact SHA-256 digests.

Install an approved platform `.mcpb` in a compatible desktop client, or unpack its matching standalone `.zip` and configure the contained `terrascale-mcp` executable as a stdio server. Verify its SHA-256 against the corresponding uppercase hexadecimal entry in `checksums.json` (`.mcpb`) or `standalone-checksums.json` (`.zip`):

```sh
sha256sum terrascale-linux-x64.mcpb
```

Use your platform's equivalent hashing command when `sha256sum` is unavailable. Artifacts are not signed by this repository today.

## Maintainer source build

Source builds require authenticated Forgejo access because the pinned SDK submodule is not publicly distributed:

```sh
git clone --recurse-submodules ssh://git@git.terrascale.tech/TerraScale/TerraScale.MCP.git
cd TerraScale.MCP
dotnet publish src/TerraScale.MCP -c Release -r linux-x64
```

The repository is pinned to stable .NET SDK `10.0.302` and target framework `net10.0`; use the checked-in `global.json` for source builds and tests.

Set the following in the MCP client's server environment. Supply exactly one credential; do not put credentials in chat or tool arguments.

| Variable | Required | Notes |
| --- | --- | --- |
| `TERRASCALE_API_BASE_ADDRESS` | Yes | Absolute public API HTTP(S) URL. |
| `TERRASCALE_PROJECT_ID` | Yes | Fixed scope for configured-project discovery, operations, recovery inspection, and usage tools. |
| `TERRASCALE_BEARER_TOKEN` | Exactly one | Public API bearer credential. Backup-plan handoffs additionally require its authenticated `session_id` claim. |
| `TERRASCALE_API_KEY` | Exactly one | Public project API key, instead of bearer token. It supports inspection tools only; backup-plan handoffs fail closed. |
| `TERRASCALE_ALLOW_INSECURE_LOOPBACK_HTTP` | No | Set exactly `true` only for a local loopback HTTP development API. All non-loopback APIs require HTTPS. |

For generic stdio MCP clients, configure the published `terrascale-mcp` executable as the command and pass this environment unchanged. Stdout is protocol-only; diagnostics go to stderr.

Copy [codex/config.toml.example](codex/config.toml.example) into Codex CLI configuration, changing the executable path and credential. Copy [claude-desktop/claude_desktop_config.json.example](claude-desktop/claude_desktop_config.json.example) into Claude Desktop's local configuration. The bundle input is [claude-desktop/manifest.json](claude-desktop/manifest.json). Generate per-platform `.mcpb` files with the built-in C# packager:

```sh
dotnet run --project tools/TerraScale.MCP.Bundle --
# or one RID:
dotnet run --project tools/TerraScale.MCP.Bundle -- linux-x64
```

The candidate packager supports only no argument (all targets), one supported RID, and `--verify`; it intentionally has no `--help` command. For release-candidate verification, use exactly:

```sh
dotnet run --project tools/TerraScale.MCP.Bundle -c Release -- --verify
```

Bundles are written to `artifacts/mcpb/terrascale-<rid>.mcpb`, with only `manifest.json` and the target binary under `server/`. Matching standalone executables are written to `artifacts/mcpb/terrascale-<rid>.zip`, containing only that target binary. Both checksum manifests are generated only for the complete five-platform set; a one-RID build removes stale manifests rather than representing a partial set as a release candidate. After clean-worktree admission, the packager runs `dotnet restore TerraScale.MCP.sln --locked-mode` before publishing; publish still uses `--no-restore`, so the SBOM comes from that locked resolved closure rather than a fresh unconstrained graph.
Run `dotnet run --project tools/TerraScale.MCP.Bundle -- --verify` before consuming an existing artifact set. It takes the same exclusive release lock without changing files and rejects missing, extra, duplicate, malformed, or mismatched artifacts; it also inspects every `.mcpb` manifest, binary entry point, platform mapping, standalone archive content, and exact executable hash pair for each RID. It also requires a byte-canonical CycloneDX 1.6 SBOM reconstructed separately for each candidate RID from `src/TerraScale.MCP/obj/project.assets.json`; each `net10.0/<rid>` target must match the effective lock closure formed from `net10.0` plus that RID's overlay in `src/TerraScale.MCP/packages.lock.json`. Target-qualified SBOM components and dependency graphs preserve RID-only packages and edges, alongside the pinned `TerraScale.DotNet` gitlink and recorded evidence hash/provenance. Unix executable entries must be regular `0755`; writable group or other permissions are rejected.

The SBOM is an unsigned candidate artifact and describes the resolved restore closure, not a full lock-file provenance attestation. The vendored SDK currently has no separately recorded dependency lock or release provenance in this candidate; signing and release publication remain follow-up work.

## Candidate CI action provenance

The Forgejo candidate workflow uses only fully qualified `data.forgejo.org` action sources, as recommended by Forgejo, pinned to immutable commits: `actions/checkout` v4.2.2 (`11bd71901bbe5b1630ceea73d27597364c9af683`), `actions/setup-dotnet` v4.3.1 (`67a3573c9a986a3f9c594539f4ab511d57bb3ce9`), and Forgejo's patched `forgejo/upload-artifact` v4 (`16871d9e8cfcf27ff31822cac382bbb5450f1e1e`). Review an upstream release and its source on `data.forgejo.org`, confirm Forgejo Runner compatibility, then update the version, SHA, workflow comment, and this list together; never use a floating tag or an unreviewed action source.

Claude Desktop's `Allow local HTTP development API` setting defaults to false. It only maps to `TERRASCALE_ALLOW_INSECURE_LOOPBACK_HTTP`; the server still rejects non-loopback HTTP endpoints.

## Separate MCP v2 HTTP host

The repository also contains an additive, independently published HTTP executable in
`src/TerraScale.MCP.Http`. It composes the transport-neutral surface from
`src/TerraScale.MCP.Core`, uses the official ASP.NET Core MCP transport with
`Stateless = true`, and maps one endpoint at `/mcp`. This host is separate from
`src/TerraScale.MCP`: it does not turn the stdio executable into a listener, does
not use the stdio credential variables, and does not change the stdio `.mcpb` or
standalone artifacts.

The HTTP host is a repository implementation, not a production deployment. Its
route, TLS termination, issuer, caller-client inventory, and ingress policy remain
deployment inputs owned by TerraScale.Orchestrator. Do not publish an endpoint until
that operational gate has been approved. The complete setup and wire examples are
in [the MCP v2 HTTP guide](docs/guides/2026-08-16-mcp-v2-http.md).

For source validation, the HTTP host can be published as its own output (for example):

```sh
dotnet publish src/TerraScale.MCP.Http -c Release -r linux-x64 --self-contained false -o artifacts/http/linux-x64
```

The HTTP release artifact, RID archives, checksums, SBOM, and provenance are
separate from the stdio `.mcpb`/standalone artifacts. To create and verify the
complete five-RID HTTP candidate, use:

```sh
dotnet run --project tools/TerraScale.MCP.Bundle -c Release -- --http
dotnet run --project tools/TerraScale.MCP.Bundle -c Release -- --http --verify
```

The HTTP archives and evidence are written under `artifacts/mcp-http/` as
`terrascale-mcp-http-<rid>.zip`, `checksums.json`, `candidate-sbom.cdx.json`, and
`candidate-evidence.json`. The direct `dotnet publish` command above is only a
source-build example. Candidate packaging requires the same clean-worktree and
locked-restore admission as the stdio packager.

### HTTP host environment reference

The HTTP process fails closed at startup unless all required values below are set.
`TERRASCALE_MCP_CONFIDENTIAL_CLIENT_ID` and
`TERRASCALE_MCP_CONFIDENTIAL_CLIENT_SECRET` identify the pre-registered MCP host
client used for RFC 7662 introspection and RFC 8693 token exchange. They are not
caller credentials. The process rejects `TERRASCALE_BEARER_TOKEN` and
`TERRASCALE_API_KEY`; never configure a shared operator credential for remote
callers.

| Variable | Required | Meaning |
| --- | --- | --- |
| `TERRASCALE_API_BASE_ADDRESS` | Yes | Absolute TerraScale public API base URI used by the typed SDK after token exchange. |
| `TERRASCALE_PROJECT_ID` | Yes | One fixed project scope; introspection must contain this exact `project_id`. |
| `TERRASCALE_MCP_ISSUER` | Yes | Exact authorization issuer URI; the introspection `iss` must match it. |
| `TERRASCALE_MCP_RESOURCE` | Yes | Exact MCP resource URI. It must be the canonical `<authority>/mcp` URI with no query. |
| `TERRASCALE_MCP_INTROSPECTION_ENDPOINT` | Yes | RFC 7662 token-introspection endpoint. |
| `TERRASCALE_MCP_TOKEN_ENDPOINT` | Yes | RFC 8693 token-exchange endpoint. |
| `TERRASCALE_MCP_CONFIDENTIAL_CLIENT_ID` | Yes | Pre-registered host client ID used for Basic client authentication to both OAuth endpoints. |
| `TERRASCALE_MCP_CONFIDENTIAL_CLIENT_SECRET` | Yes | Secret for that pre-registered host client; store it only in deployment secret management. |
| `TERRASCALE_MCP_REQUIRED_SCOPE` | Yes | One exact scope required on the caller token. |
| `TERRASCALE_MCP_ALLOWED_CLIENT_IDS` | Yes | Comma-separated pre-registered caller `client_id` allowlist. |
| `TERRASCALE_API_RESOURCE` | Yes | TerraScale API resource/audience requested during RFC 8693 exchange. |
| `TERRASCALE_API_SCOPE` | Yes | One exact TerraScale API scope requested during exchange. |
| `TERRASCALE_MCP_ALLOWED_ORIGINS` | No | Comma-separated normalized origin roots. A supplied request `Origin` must match one exactly; an absent `Origin` is allowed. |
| `TERRASCALE_MCP_ALLOW_INSECURE_LOOPBACK_HTTP` | No | The literal `true` enables HTTP only when the request peer and every configured endpoint are loopback. Default is HTTPS-only. |

The HTTP variable is intentionally `TERRASCALE_MCP_ALLOW_INSECURE_LOOPBACK_HTTP`;
the similarly named `TERRASCALE_ALLOW_INSECURE_LOOPBACK_HTTP` belongs only to the
stdio host. Do not substitute one for the other.

## MCP inventory

Tools (contract v1): `list_regions`, `get_configured_project`, `list_project_databases`, `get_project_database`, `list_database_environments`, `get_database_environment`, `get_project_usage`, `get_configured_project_latency`, `get_project_workload`, `get_project_usage_history`, `list_database_backups`, `get_database_backup`, `list_database_restore_jobs`, `get_database_restore_job`, `plan_database_backup`. Explicit page v2 tools: `list_project_databases_page_v2`, `list_database_environments_page_v2`, `list_database_backups_page_v2`, `list_database_restore_jobs_page_v2`.

The machine-readable [tool contract](docs/tool-contract.v1.json) records the exact runtime names, input schemas, safe output projections, configured scope, confirmation rule, and redacted error categories. A process test compares it with `tools/list` and fails on drift. Candidate evidence records the contract hash and supported `/api/v1` compatibility. Breaking contract changes require a new contract version and at least six months notice.

The [customer API parity inventory](docs/customer-api-parity.v1.json) classifies each customer capability family against the current public SDK and records the launch-claim gate. It makes the current fixed-project read subset explicit; organization, content, credential, billing, export, and other unqualified operations remain deferred. All MCP writes are denied until the [mutation-admission policy](docs/design/mcp-mutation-admission.md) has an approved non-agent-controlled authority, atomically consumed bound token, and durable audit contract.

Resources: `terrascale://v1/guidance/contract`, `terrascale://guidance/authentication`, `terrascale://guidance/safe-mutations`, `terrascale://guidance/operational-read-scope`, `terrascale://guidance/recovery-read-scope`, `terrascale://guidance/backup-approval-handoff`.

Prompts: `analyze-project-usage`, `review-operational-health`, `review-backup-recovery-readiness`, `inventory-configured-project`, `investigate-project-usage`, `plan-recovery-readiness`, `handoff-database-backup`.

Except for the globally public `list_regions` catalog, every tool call is rooted in `TERRASCALE_PROJECT_ID`. Child identifiers are accepted only for typed SDK routes nested under that configured project. Contract-v1 list tools retain their array responses. The explicit page v2 tools return `{ items, returned, truncated, nextSkip }`: `truncated` means the response reached its requested cap and may have more data; `nextSkip` is a nullable number, with `null` when there is no valid potentially-following offset. `list_regions` has no public paging route and fails closed rather than returning a partial catalog. `plan_database_backup` returns only action, database identity, digest, and expiry. It discards the opaque Platform confirmation token, retains no plan state, and has no execution route or tool. Show that safe projection to a human, then direct the human to Dashboard (or another genuine, out-of-band approval authority) to review and execute. A bearer token without an authenticated `session_id` claim, including API-key authentication, fails closed before a plan request. Tool annotations communicate intent but do not replace server-side scope enforcement. API errors are reduced to HTTP status and retry delay. Response bodies, API messages, request IDs, and credentials are never surfaced by this server. Requests use a fixed 30-second transport timeout. Recovery responses use safe projections that omit requesters, error messages, provider payloads/URLs, raw data, and credentials. Restore-point and regional-placement reads remain unavailable because their typed responses do not carry the parent scope needed for safe projection.

## Development

```sh
dotnet restore TerraScale.MCP.sln
dotnet build TerraScale.MCP.sln -m --no-restore
dotnet test TerraScale.MCP.sln --no-restore
```

The ordinary tests are deterministic and use loopback protocol fixtures only. The real public-API backup-handoff admission E2E is skipped unless all of `TERRASCALE_MCP_E2E_ENABLED=true`, `TERRASCALE_API_BASE_ADDRESS`, `TERRASCALE_PROJECT_ID`, `TERRASCALE_BEARER_TOKEN` (a valid session-bearing bearer credential), and `TERRASCALE_MCP_E2E_DATABASE_ID` are configured for an approved fixture. It verifies the scoped safe plan projection and that the absent execution tool cannot be called; it never executes a backup. Optional `TERRASCALE_MCP_E2E_REVOKED_BEARER_TOKEN` and `TERRASCALE_MCP_E2E_EXPIRED_BEARER_TOKEN` enable real expected-denial checks for those credentials.

`LiveReadScopeE2ETests` is a separate discovery-time-gated public-API evidence test. It starts two real MCP stdio processes and calls only `get_configured_project`, which uses typed `Projects.GetAsync` GET: one process receives the approved configured project and the other receives the protected configured expected-403 project with the same least-privilege bearer credential. It requires `TERRASCALE_MCP_E2E_ENABLED=true`, `TERRASCALE_API_BASE_ADDRESS`, `TERRASCALE_PROJECT_ID`, `TERRASCALE_BEARER_TOKEN`, and `TERRASCALE_MCP_E2E_EXPECTED_403_PROJECT_ID`. It checks the SafeProject projection and configured scope, the safe 403 error envelope, and no leakage of fixture credentials, API address, or expected-403 project ID to MCP responses/stdout/stderr. It performs exactly two fixed GETs and no writes.

The manually dispatched workflow keeps all fixture secrets on its one test step. It performs locked restore, Release build, and a deterministic self-test of its BCL XML verifier without fixture credentials before that step, then runs only the exact `ConfiguredProjectReadHasSafeProjectionAndConfiguredExpected403` test with `--no-build --no-restore` and a temporary TRX result. The verifier prohibits DTD/entity resolution, bounds the document, accepts the normal XML declaration before requiring the canonical TRX root/namespace, and requires the exact direct hierarchy `TestRun → Results → UnitTestResult` and `TestRun → ResultSummary → Counters`, with no misplaced descendants. Required result and counter attributes must be exactly one unqualified attribute for each required local name, with exact one-pass values. Its credential-free preflight and repeated test-step guard require a `refs/heads/develop` event and a checkout whose `git rev-parse HEAD` exactly equals fetched `origin/develop`. The protected `mcp-live-evidence` environment must also be configured by Forgejo administrators to allow only `develop`, so an arbitrary workflow ref cannot access fixture secrets. The workflow writes only commit, test selector, pass/fail, and timestamp after that exact pass.

The `mcp-live-fixture` runner label and fixed Forgejo concurrency are an external operator-controlled exclusive-lane prerequisite: the runner must be dedicated to a non-overlapping fixture lane. This workflow does not acquire or prove a cross-host lock. Without explicit external runner/environment evidence for that exclusive lane, any live result cannot be credited as release evidence; concurrent fixture or control-plane changes can make the check fail.

This configured expected-403 check does not establish that the expected-403 ID exists, that it is out of scope, or generic authorization behavior without independent external service evidence.

`LiveCustomerJourneyE2ETests` is a separate, stricter discovery-time-gated qualification lane. With `TERRASCALE_MCP_LIVE_JOURNEY_ENABLED=true`, it requires the global API address, strict `gru`, `sfo`, and `fra` API addresses, a configured project, an expected-403 project, a customer bearer credential, and an approved fixture database ID. It starts the published MCP process, exercises every approved read tool for the fixture (regions, project, databases, environments, recovery inspection, usage, latency, workload, and history), checks both legacy array and page-v2 list contracts, probes project reads through each strict endpoint, and runs a second process with the expected-403 project to check cross-process tenant isolation and redaction. It also supplies an ignored cross-project argument to a configured-project call to prove scope comes from server configuration, not tool arguments. Set `TERRASCALE_MCP_LIVE_JOURNEY_BACKUP_PLAN=true` only when the credential has the reviewed session claim and the fixture is approved for a read-only backup-plan handoff. The test never executes a mutation and never persists fixture values. Without the protected addresses, credential, expected-403 fixture, database fixture, and an externally controlled exclusive lane, this remains skipped and no live launch evidence is claimed.

The existing configured expected-403 check remains the narrow Forgejo-attested live evidence path. No E2E runs against an AppHost or DevHost.

## Future expansion contract

Stdio is the current delivery because it keeps the MCP session on the operator's machine and avoids publishing a public MCP workload or new ingress surface. No public HTTP MCP endpoint exists. Any future public HTTP workload requires a separate AppHost/Orchestrator/ingress admission and must not be inferred from these artifacts.

Add a tool, resource, prompt, HTTP transport, or OAuth only after TerraScale publishes a typed public API and SDK contract with authorization semantics, bounded input grammar, response sensitivity classification, and real API success/failure E2E coverage. Mutations remain denied until an actual non-agent-controlled approval authority can authorize and invoke them; tool annotations, prompts, and human-approval booleans are not that boundary.

The production mutation-admission gates and required server-enforced confirmation protocol are documented in [MCP mutation admission policy](docs/design/mcp-mutation-admission.md).
