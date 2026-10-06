# Operational readiness exploration

Status: exploration evidence, not an implementation or a production-readiness claim.

Related record: [Control-plane exploration](exploration-control-plane.md).

## Scope

Assess operational prerequisites for moving the Orchestrator beyond its current Phase 1 and development-lab status.

## Evidence

- Service health, OpenTelemetry, and internal mTLS building blocks exist.
- The Orchestrator remains Phase 1 and development-lab evidence.
- Production runtime, PKI, Vault, and NATS qualification are absent.
- There is no production deployment evidence, alert and runbook set, object-store recovery drill, or retained production operational evidence.

## Findings / decision

Do not infer production operational readiness from local health or internal transport components. The missing work spans runtime qualification, identity and secret management, messaging, deployment, recovery, and operational response evidence.

## Recommended bounded next slice

Define and test a production non-ingress internal RPC descriptor as the first narrow contract. It should make listener isolation, workload mTLS, allowed callers, and denial of public ingress explicit before broader runtime deployment work.

## Validation / constraints

Test that the descriptor accepts only the intended internal caller and rejects public ingress and untrusted identities. Keep public REST, WebSocket, and SSE contracts separate from private RPC. Do not expose RPC to Dashboard, SDKs, CLI, TerraBase, NATS, health probes, or third parties, and do not treat the descriptor test as PKI, Vault, NATS, deployment, alerting, or recovery-drill qualification.
