# Polar production-readiness exploration

Status: exploration evidence, not an implementation or a production-readiness claim.

Related record: [Billing, security, and Polar exploration](exploration-billing-security-polar.md).

## Scope

Assess the missing evidence between the existing Polar integration mechanics and a production billing deployment contract.

## Evidence

- Existing code has signature verification, receipts, ordering, reconciliation, and lifecycle handling.
- No Polar usage export or commercialization decision is recorded.
- Sandbox lifecycle evidence is incomplete, and no production workload deployment contract is established.
- Grace-period timing evidence is weak.

## Findings / decision

Do not make usage or commercialization claims yet. Decide fixed-price billing versus metered usage before designing or claiming usage export. The current code strength is not a substitute for an end-to-end, credential-gated sandbox lifecycle proof or a production workload contract.

## Recommended bounded next slice

Write a production Polar billing deployment contract, then add a credential-gated sandbox lifecycle test that covers the intended flow. The test must remain opt-in and separately injected from production identities.

## Validation / constraints

The contract should define deployment ownership, webhook verification and rotation, receipt and reconciliation retention, ordering, retry and DLQ behavior, grace timing, rollback, and operational alerting. The sandbox test should establish checkout, portal, subscription, webhook, and reconciliation behavior appropriate to the selected commercial model. Never record credentials, fixture identifiers, or a sandbox success claim in this evidence note.
