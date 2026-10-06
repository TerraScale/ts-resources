# Orchestrator production composition audit

Status: the Orchestrator is a strong fail-closed decision and validation core, with RF=1 development-harness evidence. It is not a composed production runtime and public `CreateNode` remains unavailable.

## Current evidence and decision

The implemented core includes control-plane planners, journals, validation gates, and an authoritative `CreateNode` journal building block. Its RF=1 development lab is useful regional-development evidence. It does not demonstrate a production quorum, host-failure tolerance, provider operation, or cloud qualification. Safe denials for anonymous or plaintext control-NATS and unsigned GitOps material remain denials, not evidence of deployment.

Do not enable a public `CreateNode` endpoint, Dashboard workflow, or agent tool until an authenticated, authoritative composition can execute it end to end and return durable, independently recoverable operation state. An agent must enter through the same versioned public contract and typed SDK as every customer, with scoped authority, explicit confirmation, idempotency, and immutable audit evidence. It must never receive private NATS, MagicOnion, direct TerraBase, or privileged Dashboard access.

## Qualification ledger

| Area | Implemented evidence | Code-completable next work | External qualification still required |
| --- | --- | --- | --- |
| Control-plane decisions | Fail-closed planners, validation, journal abstractions, and RF=1 development harness. | Compose the existing private journal and coordinator behind disabled-by-default configuration. | R3/R5 runtime behavior, failure evidence, and production enablement approval. |
| Provisioning and host lifecycle | No enabled provider actuator or authoritative production composition. | Provider-neutral adapter contract, persisted intent, idempotency, provider-truth readback, compensation, and host checks. | Approved account, quota, network, capacity, systemd/containerd, storage, and safe cleanup proof. |
| Backup and DR | Decision models and recovery-oriented building blocks only. | Backup/recovery orchestration hooks, probes, and crash/recovery scenarios. | Application-consistent backup, object-store and retained-volume restore, clean-room drill, agreed RPO/RTO, and owner acceptance. |
| Observability | Development and source-level telemetry foundations only. | Bounded telemetry, exporters, dashboards-as-code, alerts, and operational probes. | Regional metrics, logs, traces, alert delivery, outage exercise, and retained on-call evidence. |
| Identity and deployment | Development PKI and fail-closed NATS/GitOps validation. | Runtime options validation, key/receipt/recovery services, signed reply verification, and restricted mutation authority. | KMS/Vault, PKI, account bootstrap, revocation, workload mTLS, and production GitOps trust. |
| Agent admission | MCP remains read-only and public lifecycle mutation admission is not delivered. | Public contract and SDK support only after the capability exists, then prepare-confirm-execute and audit tests. | Genuine non-agent-controlled approval authority and live public-boundary authorization evidence. |

No row above authorizes an OCI claim, an R3 claim, or a production-readiness claim. Repository work can supply code and test harnesses; security, platform operations, SRE, and TerraBase owners must qualify their real boundaries and approve enablement.

## Next minimal slice: `ProductionCreateNodeComposition`

Keep the scope to composition, not provider creation or public exposure:

1. Add explicit disabled-by-default production composition options, requiring validated private NATS identity, journal stream/account identifiers, key and receipt dependencies, and a named runtime mode. Missing, malformed, anonymous, or plaintext configuration must fail closed at startup.
2. In `Program` and runtime configuration, compose the private `NatsCreateNodeOperationJournal`, key lifecycle, signed handoff and recovery lookup, restricted mutation client, and reply verification. Because `CreateNodeCoordinator` requires a non-null `ICreateNodeProvider`, either defer its construction until an approved enabled adapter exists, or inject an explicitly non-mutating, fail-closed disabled provider whose only result is an audited unavailable outcome. Do not register a public route in this slice.
3. Add control-plane composition tests that prove disabled default, invalid configuration denial, duplicate replay, forged reply denial, key or receipt absence, CAS conflict, and restart recovery. Tests must assert that no provider mutation occurs.

The exit condition is a reviewed, secret-free, disabled composition with reproducible tests. Production capability remains unavailable until a reviewed enabled provider and authenticated journal dependencies are present. This is not a node creation, provider integration, production deployment, OCI exercise, or R3 qualification.

## Evidence provenance

This audit consolidates the immutable Orchestrator `develop` evidence already recorded on 2026-08-05 at `e27e4c9f4ca729e9790b063665ae90d608059d26`: `Program.cs`, `Messaging/NatsRuntime.cs`, `Messaging/NatsOperationJournalStore.cs`, `ControlPlane/Operations/NatsCreateNodeOperationJournal.cs`, `Development/DevelopmentPki.cs`, `docs/guides/nats-journal-production-prerequisites.md`, and `docs/guides/production-readiness-audit-2026-08-04.md`. Related admission and recovery boundaries are recorded in this directory's MCP mutation and provisioning/recovery readiness records. No credentials, production hosts, or unsupported availability claims are included.
