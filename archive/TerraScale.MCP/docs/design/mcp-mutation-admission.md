# MCP mutation admission policy

## Status

This production admission policy authorizes MCP implementations of typed public
operations after the operation satisfies every applicable gate in this
document. Admission remains deny by default per operation. Missing evidence for
one operation does not block unrelated typed operations that already satisfy
their gates.

## Non-negotiable admission gates

An admitted operation must use a versioned public capability through the typed
public TerraScale SDK. The User must authenticate through a distinct user-bound
MCP access key and select Organization, Project, and operation scopes. Future
Organizations and Projects are excluded by default. Every call must apply the
same live User authorization, role, scope, tenant-isolation, confirmation,
Audit, and secret-handling rules as the public operation. No private route,
generic HTTP escape hatch, direct storage access, reflection, or internal
transport is an alternative.

The public contract must also define a bounded input schema, response and
request sensitivity classification, an idempotency-key and retry posture, and
a durable audit event. Before release, a live public-API test must prove both a
successful request and an expected authorization or scope denial using the
same public contract.

MCP annotations, prompts, a `confirm=true` argument, and host-client UI are
useful guidance only. None replaces the public server's short-lived single-use
confirmation token or its live authorization checks.

## Required confirmation protocol

Every sensitive action must use a plan-to-confirm flow enforced by the public
server:

1. `plan` validates the bounded request and returns the exact canonical
   payload, target, impact, price where relevant, and a five-minute single-use
   confirmation token.
2. The User reviews and confirms the plan in the AI conversation. The AI then
   invokes the typed confirmation tool with the token and idempotency key.
3. `confirm` rechecks live authority and state before mutating and atomically
   consumes the token.

The server must bind the token to the authenticated User, MCP access key,
selected Organization and Project scope, operation scope, canonical payload,
current target state, price where relevant, idempotency key, and expiry. It
must reject expiry, replay, altered payload, target-state or price drift,
scope, caller, key, or idempotency-key mismatch. The Audit event must durably
record the operation, result, selected scope, authenticated actor, token
outcome, idempotency key, and correlation identifier without recording
credentials, one-time secrets, or confirmation tokens.

No Dashboard confirmation or separate fresh-authentication or step-up challenge
is required. A local cache, a client-generated session identifier, an MCP
annotation, prompt text, or a human-approval boolean cannot substitute for the
server-issued token and live rechecks.

## Operation classification and deferral

Each candidate operation requires a recorded destructive classification. A
missing classification is a denial.

| Candidate operation | Required classification | Admission now |
| --- | --- | --- |
| Create or start a bounded, reversible operation | Non-destructive or reversible write | Eligible after its typed contract, authorization, idempotency, Audit, and live evidence pass. |
| Change configuration, routing, policy, or capacity | Potentially service-affecting write | Eligible with exact impact, state, price where relevant, confirmation, rollback, and concurrency semantics. |
| Delete, purge, restore, overwrite, rotate, or revoke | Destructive or irreversible | Eligible with exact impact, recovery posture, confirmation, and replay-safe execution. |
| Billing, credentials, identities, permissions, queues, raw data, TQL, or customer administration | High-risk family | Eligible when typed and public, with the same live role, scope, confirmation, Audit, and secret rules as the authenticated User. |

## Admission record and release checklist

For each operation, the review record must identify the typed SDK method and
versioned public operation, Organization and Project scope proof, destructive
classification, bounded schema, sensitivity classification, authorization and
tenant semantics, idempotency and retry behavior, Audit-event contract, and
confirmation-token bindings when sensitive. Release evidence must include live
public success and expected authorization, tenant, scope, expiry, replay,
state-drift, and price-drift denials where applicable. Any failed, absent, or
unreviewed item keeps that operation denied.
