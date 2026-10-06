# MCP ticket audit

Audit date: 2026-08-20

## Issue #1

Mutation admission remains denied. The repository still lacks every required
gate in [the mutation admission policy](../../design/mcp-mutation-admission.md):
a public versioned mutation contract with tenant semantics, a genuine
non-agent approval authority, an atomically consumed token bound to project,
canonical payload, caller/session, and idempotency key, durable audit events,
and live success and denial evidence. No mutation implementation was added.

## Issue #2

TerraScale.DotNet commit `291d5753bd4eeae9aab8f9cce1d15c104a109a33` hardens
candidate-package digest checking, package-content scanning, and retry bounds.
It keeps live customer journey, tenant isolation, intended-feed download, and
publication as external release gates. It does not add a new MCP-safe typed
operation.

The MCP candidate now binds `docs/customer-api-parity.v1.json` to
`candidate-evidence.json` by SHA-256, inventory version, `/api/v1` compatibility,
and the `blocked-until-qualified` launch claim. Candidate verification rejects a
changed or missing parity inventory. The existing tool-contract digest, lock
hashes, SDK gitlink, SBOM, source revision, and per-artifact hashes remain
required.

## Issue #3

TerraScale.Internals commit `63cd7585f9f0ab0a30c5aa34f7ea5b3424cbfc663`
changes internal export receipts, usage-source evidence, billable delete units,
and customer-facing regional state. Those changes are not a released typed
TerraScale.DotNet contract and cannot be consumed through MCP. MCP therefore
does not add export, document, query, billing, or regional-placement tools, and
does not call internal or direct data-plane endpoints.

The live customer journey now requires an approved database fixture and covers
all approved read tools, both legacy array and page-v2 list paths, direct child
reads when fixtures provide child IDs, global routing, strict `gru`/`sfo`/`fra`
routing, and a cross-project tool-argument isolation probe. It remains an
environment-gated test. No live issuer, customer credential, expected-denial
fixture, exact published artifact, or externally controlled exclusive lane was
available during this audit.

## Release decision

The repository changes are safe for issues #2 and #3. The MCP launch claim stays
blocked until the external artifact publication, public API candidate digest,
live customer journey, tenant-isolation, routing, fault-redaction, and
deployment/ingress gates are independently evidenced.
