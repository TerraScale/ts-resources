# ADR 0004: one Forgejo provider for releases and Actions reads

Status: Superseded 2026-10-28 by the GitHub workflow.

Use `gh` for releases, tags, Actions, and repository issues; see
[the current command reference](../forgejo.md). The dated decision below is
historical and must not be used as operational guidance.

Date: 2026-09-10

## Context

Workflows and the self-release lane each assembled their own `fj` argument
vectors and parsed `fj` output. `fj release view` renders only the release
header and body, so the self-release target check searched for a
`target_commitish` the pinned fj version never prints; an existing release could
therefore never be re-verified. `fj` also wraps human text in Unicode direction
isolates even under `--style minimal`, so ad-hoc string comparisons are
terminal-dependent.

## Decision

All Forgejo interaction lives in the C# `Forgejo` provider at
`src/TerraScale.Deploy/Forgejo/Forgejo.cs`. It runs `fj -H <host> --style
minimal`, normalizes output, centralizes "not found" handling, validates every
repository and tag before they reach an argument vector, and is the only place
that builds a Forgejo command line.

The current command surface is the flat `forgejo` read operations
`release-list`, `release-view`, `tag-commit`, and `variables`, with `--json` on
read paths. The provider additionally exposes write operations that no CLI
command wires up yet: idempotent release creation, release asset upload and
download, issue search, creation, labeling, commenting, and closing, and
workflow dispatch. It does not expose a second HTTP client.

Release target identity comes from `fj tag view`, not `fj release view`.

## Consequences

- Callers get release, tag, and Actions reads through the CLI, whose behavior
  is unit-tested with a process seam. The self-release lane in
  `.forgejo/workflows/ci.yml` still invokes `fj` directly.
- `fj` remains the only transport, so the credential store and host selection
  stay in one place. A future Forgejo API client is a new decision.

Implementation anchors:

- `src/TerraScale.Deploy/Forgejo/Forgejo.cs`
- `src/TerraScale.Deploy/Cli/Program.cs`
- `tests/TerraScale.Deploy.Tests/Forgejo/ForgejoProviderTests.cs`
- `docs/forgejo.md`
