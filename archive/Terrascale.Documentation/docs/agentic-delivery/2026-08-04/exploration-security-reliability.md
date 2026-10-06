# Security and reliability exploration

## Confirmed production blockers

The Orchestrator production-readiness audit blocks deployment on unqualified real OCI compute, storage, runtime, NATS, PKI, restore, and DR adapters. Local development evidence and pure state-machine tests do not establish production recovery, availability, or destructive-operation safety.

Internals review identified these delivery risks:

- Rate limiting trusts unvalidated `X-Forwarded-For` behavior, which can let an untrusted client influence its apparent address.
- Kestrel request-body bounds and minimum request data rate are disabled or unbounded, leaving resource-exhaustion exposure.
- Actual RPO/RTO targets and successful restore-drill evidence remain unresolved.
- Project-deleted audit records are mutable, weakening forensic integrity.
- Internal gRPC message sizes are unbounded, risking memory pressure across a private boundary.

## Positive controls to preserve

Public keys are scoped, provider webhooks are signed, and the internal-RPC design specifies isolated non-ingress listeners with workload mTLS. Preserve these controls while making their runtime enforcement and operational evidence production-qualified. Internal RPC remains unavailable to Dashboard, SDKs, CLI, MCP, customers, and third parties.

## Remediation and test gates

| Finding | Required remediation | Acceptance evidence |
| --- | --- | --- |
| Forwarded client address | Trust forwarded headers only from a configured, authenticated proxy boundary; otherwise use the direct peer address. | Integration tests prove spoofed client headers cannot evade per-identity or per-address limits. |
| Request exhaustion | Set endpoint-appropriate body limits, header limits, request timeouts, and minimum data rates; apply streaming exceptions narrowly. | Slowloris, oversized-body, and legitimate streaming tests show bounded resource use and correct status codes. |
| Recovery uncertainty | Approve measurable RPO/RTO, retention, and recovery-workspace objectives, then automate restore and regional DR drills. | Signed drill record includes source, target, elapsed recovery, recovered consistency checks, owner, and result. |
| Mutable deletion audit | Make deletion audit entries append-only and link corrections or redactions as new records. | Authorization and tamper tests prove actors cannot alter historical deletion facts. |
| Internal gRPC size | Set explicit request and response message ceilings, validate payload sizes before allocation, and paginate or stream approved large reads. | Boundary tests reject oversized payloads and demonstrate normal operations within the published limits. |
| Control-plane qualification | Implement and qualify real OCI, storage, runtime, NATS, PKI, backup/restore, and DR adapters. | Environment-specific, retained evidence proves fencing, recovery, mTLS identity, fault handling, and restore behavior. |

No security or reliability claim should be promoted from this exploration until the corresponding gate has reproducible evidence.
