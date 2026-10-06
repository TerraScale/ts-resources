# Human-agent parity exploration

Status: exploration evidence, not an implementation or a production-readiness claim.

Related records: [Dashboard and Platform exploration](exploration-dashboard-platform.md) and [MCP and SDK parity exploration](exploration-mcp-sdk-parity.md).

Snapshot note: the environment-deletion observation below is pre-implementation evidence. Dashboard commit [`7a35d3c`, Add Dashboard environment deletion flow](https://git.terrascale.tech/TerraScale/TerraScale.Internals/commit/7a35d3ca3173c84eb7b960338127a6321975ac2e) supplied the initial slice. Later hardening continued in [`8bd846f`, Harden Dashboard environment deletion confirmation](https://git.terrascale.tech/TerraScale/TerraScale.Internals/commit/8bd846f81756285aa856589069ffc9ebe0c8760a) and [`1019c8b`, Validate Dashboard environment deletion input](https://git.terrascale.tech/TerraScale/TerraScale.Internals/commit/1019c8b8601a5c24aa51adee1ee821a67ac2ee12). A P0 reviewer finding identified validation briefly placed in the wrong workflow by [`c90fdf5`, Preserve Dashboard environment deletion failures](https://git.terrascale.tech/TerraScale/TerraScale.Internals/commit/c90fdf5cd04da723c4d7d4a2e460883449b162f7); [`20bcb1a`, Fix Dashboard environment deletion validation placement](https://git.terrascale.tech/TerraScale/TerraScale.Internals/commit/20bcb1aa2c1375e8124e34e53282b72fca8482c9) corrected that placement. The [updated implementation record](https://git.terrascale.tech/TerraScale/TerraScale.Internals/src/commit/20bcb1aa2c1375e8124e34e53282b72fca8482c9/docs/implementation/2026-08-05-dashboard-environment-deletion.md) records the implementation. Closure requires final independent review: the focused affected-file compiler diagnostic was clean, global TypeScript diagnostics remain known unrelated findings, and live E2E remains inconclusive because AppHost startup did not complete. This is not a broader parity or production-readiness claim.

## Scope

Compare the current Dashboard and MCP workflows with public Platform capability and the typed TypeScript and .NET SDK surfaces.

## Evidence

- Dashboard composes TerraScale access through the typed SDK boundary.
- Public Platform and both typed SDKs support environment CRUD.
- At the time of this snapshot, Dashboard did not yet provide an environment-delete route or UI.
- MCP deliberately omits mutations, billing, and administration. Its plan-only backup handoff is the correct current scope.
- The .NET account and administration omission is declared scope D-008.
- The focused affected-file compiler diagnostic was clean. Global TypeScript diagnostics remain known unrelated findings, and live E2E is inconclusive because AppHost startup did not complete.

## Findings / decision

The actionable parity gap at snapshot time was human access to environment deletion, not a reason to broaden MCP. The Dashboard implementation and hardening sequence address that bounded gap, but the P0 validation-placement finding and its correction mean closure still requires final independent review. The clean focused diagnostic does not supersede the known unrelated global TypeScript diagnostics or the inconclusive live E2E. Preserve the MCP read and plan-only posture until a public mutation contract supplies confirmation, authorization, idempotency, and durable audit state. Treat D-008 as declared scope rather than an untracked SDK defect.

## Recommended bounded next slice

Run final independent review of the corrected placement in [`20bcb1a`](https://git.terrascale.tech/TerraScale/TerraScale.Internals/commit/20bcb1aa2c1375e8124e34e53282b72fca8482c9), then obtain conclusive live E2E evidence once AppHost startup is available. Keep global TypeScript findings separately classified as known unrelated work. Do not expand MCP in this slice.

## Validation / constraints

Verify that the Dashboard route uses no direct Platform, TerraBase, private RPC, special headers, or Dashboard-only public contract. Prove authorized deletion, tenant isolation, retries where the public contract permits them, and user-visible failure handling. Do not add MCP mutation, billing, administration, or credential tools in this slice.
