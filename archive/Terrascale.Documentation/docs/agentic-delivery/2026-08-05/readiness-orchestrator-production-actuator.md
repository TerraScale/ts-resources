# Orchestrator production actuator readiness

Status: the private NATS journal-writer substrate and authoritative `CreateNode` journal implementation are code building blocks. The production composition, provider adapter, and operational qualification authority are intentionally absent. This is not an enabled `CreateNode` capability.

## Exact boundary

NATS is a substrate for durable, private control-plane coordination. It is not a provider actuator. A real production `CreateNode` requires all of the following in one reviewed composition: an R3/R5-qualified `ORCH_OPERATIONS` store; `NatsCreateNodeOperationJournal`; key, receipt, recovery-lookup, and invocation-capability services; restricted mutation authority and reply verification; `CreateNodeCoordinator`; and an explicitly enabled, separately reviewed provider adapter.

The current production-prerequisites guide expressly says the composition root does not create an enabled journal, coordinator, or provider. Local RF=1, pure-decision, development PKI, CI runner, or a successful NATS unit/integration test cannot substitute for that composition or for a provider-side node creation.

## Readiness ledger

| Work item | Owner | Code-completable in repository | Requires external qualification authority |
| --- | --- | --- | --- |
| Compose private journal, key lifecycle, signed handoff/recovery lookup, mutation client, coordinator, and disabled-by-default feature gate | Orchestrator | Yes. Preserve fail-closed startup and do not wire a provider by default. | No production enablement without owner-approved NATS identity and key material. |
| Provider adapter with persisted intent, idempotency token, provider-truth readback, compensation, and receipt binding | Orchestrator | Yes, subject to a reviewed provider-neutral interface. | Disposable and then approved-account execution, quota/network confirmation, billing review, and resource cleanup proof. |
| Regional NATS accounts, ACLs, NKeys, mTLS identities, server host configuration, and rotation/revocation | Security and platform operations | No. The repository correctly contains no production credential artifact. | Named security/operator authority creates, stores, rotates, and attests to the external configuration. |
| Three-server regional availability and failure behavior | SRE/operator authority with Orchestrator support | Test harness and probes are code-completable. | Real R3 or approved R5 deployment, one-member-loss, partition, writer failover, and outage evidence. RF=1 is development-only. |
| Host/runtime, storage, ingress, and private RPC controls | Orchestrator plus platform operations | Declarative plans, checks, and probes are code-completable. | Provider, KMS/Vault, systemd/containerd, load-balancer, network, and workload-mTLS qualification. |
| Backup/restore, retained-volume recovery, and DR | TerraBase, Orchestrator, SRE/operator authority | Planners, orchestration hooks, and test scenarios are code-completable. | Application-consistent object backup, object-store restore, clean-room drill, agreed RPO/RTO, and operator acceptance. |
| HA telemetry and operations | Orchestrator plus SRE/operator authority | Bounded telemetry models, exporters, dashboards-as-code, and alert policies are code-completable. | HA metrics/log/trace/Grafana deployment, encrypted regional spool, Alertmanager and OTLP outage drill, and retained on-call evidence. |

## Implementation sequence and gates

1. Orchestrator implements the composition root behind an explicit disabled default, with tests for missing keys, invalid handoff, forged reply, CAS conflict, duplicate replay, and crash recovery. Gate: source tests and a secret-free configuration review.
2. Orchestrator implements one provider adapter only after an interface and destructive-boundary review. Gate: a disposable account proof that verifies created resource identity through an independent provider-truth read and destroys it safely.
3. Security and platform operations supply production NATS, PKI/KMS, account, and network artifacts outside this repository. Gate: a targeted three-server TLS and ACL exercise proving controller denial of KV/stream destructive mutations, reply isolation, rotation, and failover.
4. SRE, TerraBase, and Orchestrator run the complete provider-backed `CreateNode` crash/recovery and recovery/DR drills. Gate: retained, independently reviewable evidence and explicit production enablement approval.

## Authority boundary

Repository maintainers can complete code and test harnesses. They cannot manufacture production authority by committing credentials, provisioning a cloud account without authorization, or treating test-only evidence as an operational acceptance. Security owns identities and revocation; cloud/platform operations own account, network, and capacity authorization; SRE owns production reliability acceptance; TerraBase owners approve database recovery behavior. The final enablement decision belongs to the designated production operator, not to a code merge.

## Evidence provenance

Read-only inspection on 2026-08-05 used Orchestrator `develop` at `e27e4c9f4ca729e9790b063665ae90d608059d26`. Evidence includes `docs/guides/nats-journal-production-prerequisites.md` at that commit, `docs/guides/production-readiness-audit-2026-08-04.md`, `src/TerraScale.Orchestrator/ControlPlane/Operations/NatsCreateNodeOperationJournal.cs`, `src/TerraScale.Orchestrator/Messaging/NatsOperationJournalStore.cs`, and the runtime composition in `Program.cs` and `Messaging/NatsRuntime.cs`. The prerequisite guide is intentionally explicit that its substrate does not compose an enabled journal, coordinator, or provider. No secrets or production host details are included here.
