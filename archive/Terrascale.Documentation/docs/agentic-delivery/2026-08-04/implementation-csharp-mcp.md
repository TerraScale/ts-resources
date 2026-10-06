# C# MCP delivery record

Date: 2026-08-04
Release source: `TerraScale.Mcp` commit `17d4bfa`, tag `v0.1.0`

## Delivered product and boundary

`/workspaces/TerraScale/TerraScale.Mcp` is the dedicated C# standard-input/output MCP product. The release source is `17d4bfa`, which includes the complete implementation and fixes made after the initial implementation commit. The initial commit is historical evidence only, not the release source.

This follows the workspace language strategy: C# is the default for TerraScale-owned MCP servers. First-class public SDK parity does not require a TypeScript MCP implementation. The TypeScript MCP was removed in commit `57b7083`.

The server is a read-only external adapter over the public typed `TerraScale.DotNet` SDK, pinned as its only source dependency at submodule commit `48d8a0e`. It does not use Platform, TerraBase, internal RPC, direct generic HTTP, mutations, TQL, raw documents, or private product paths.

## Released surface

The release exposes 12 typed read-only MCP tools, two resources, and two prompts. Repository listing was removed because the corresponding SDK endpoint is unbounded. The remaining surface covers bounded public read operations for regions, projects, database metadata, repository and schema details, and project usage. It excludes all write or administrative actions, credentials, billing, queues, backup and restore operations, raw documents, and TQL.

## Security, reliability, and packaging

The final implementation requires HTTPS for public endpoints, except for an explicit loopback-development HTTP opt-in. It rejects URL userinfo, disables redirects, redacts errors, keeps stdout exclusively for the MCP protocol, and has process-level Release testing.

Release packaging is staged, deterministic, and integrity-guarded: it bundles the exact expected artifact set, produces a checksum manifest only for a complete valid set, validates that set exactly, and performs strict verification rather than accepting extras or missing files. An interrupted or incomplete set has no valid checksum manifest. Review findings were resolved across transport security, dependency isolation, deterministic packaging, HTTP-client reliability, and real-process protocol coverage.

## Final validation evidence

An independent final review after `17d4bfa` reported a clean result. Root validation recorded:

- Debug and Release test runs: 25 tests each.
- Strict all-RID bundling and four ZIP integrity checks.
- Full checksum-manifest regex validation for exactly four bundles.

The exact commands and outcomes are retained in [validation evidence](validation-evidence.md#c-mcp-v010-source-validation). These results validate the product boundary, process behavior, and release artifacts. They are not evidence that the wider TerraScale DBaaS is production-ready or that a real customer public endpoint was exercised.

## Release evidence

The authenticated Forgejo release is [TerraScale MCP v0.1.0](https://git.terrascale.tech/TerraScale/TerraScaleMcp/releases/tag/v0.1.0). Its annotated tag `v0.1.0` resolves remotely to tag object `0d2fb560...`; the release source commit remains `17d4bfa`.

Post-release README corrections in `TerraScale.Mcp` commits `39539f5` and `6f50b7c` removed stale planned-release wording and precisely identify the five required installation artifacts: `checksums.json`, `terrascale-win-x64.mcpb`, `terrascale-osx-arm64.mcpb`, `terrascale-osx-x64.mcpb`, and `terrascale-linux-x64.mcpb`. Forgejo additionally provides automatic `source.zip` and `source.tar.gz` archives; they are not installation artifacts.

## Remaining system blockers

This MCP release does not deliver the full TerraScale DBaaS. Remaining external or system blockers include the dirty and behind Internals checkout with security findings, Orchestrator production-readiness and DR work, OpenAPI SDK drift, and Polar sandbox-product plus webhook-secret configuration and real checkout tests.
