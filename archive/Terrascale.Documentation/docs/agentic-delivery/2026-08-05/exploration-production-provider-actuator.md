# Provider actuator readiness exploration

Status: exploration evidence, not an implementation or a production-readiness claim.

Related record: [Control-plane exploration](exploration-control-plane.md).

## Scope

Assess the smallest evidence-bearing path from pure control-plane planning to a provider-side node-create proof. This record covers the provider actuator boundary only, not a production deployment.

## Evidence

- `OperationEngine` and `ProviderOwnershipEngine` are pure engines.
- The current boundary has no durable journal store or codec, CAS append, runtime coordinator, signed `HandoffReceipt`, Pulumi verifier.
- The local `develop` checkout was ahead of `origin` during the exploration and a validation lease was held. That state is not execution evidence.

## Findings / decision

Do not claim provider execution readiness. A pure plan cannot establish durable ownership, replay safety, provider truth, or verifiable handoff. The required sequence is a durable journal and signed handoff before any provider call, followed by independently checked provider evidence.

## Recommended bounded next slice

Implement a minimal durable operation journal with codec and compare-and-swap append, a signed `HandoffReceipt`, and a runtime coordinator. Exercise it against a fake `CreateNode` adapter.

## Validation / constraints

Prove append conflict handling, idempotent retry, receipt-signature verification, and refusal to execute without a valid handoff. Retain only redacted evidence. Do not reuse CI runner code as an actuator, expose private transport, publish provider credentials, or call the disposable proof production readiness.
