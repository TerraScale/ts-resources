# Orchestrator production readiness

Status: Phase 1 decision core and development-lab evidence only. It is not production-ready.

## What the evidence supports

The Orchestrator contains fail-closed planners and journals for control-plane decisions, plus a three-region RF=1 development lab. Its [repository rules](../../../../TerraScale.Orchestrator/AGENTS.md) explicitly say RF=1 results are regional-development evidence, not production quorum, host-failure tolerance, cloud, destructive-storage, or ARM qualification. The [production-readiness audit](../../../../TerraScale.Orchestrator/docs/guides/production-readiness-audit-2026-08-04.md) records the same limit.

Safe disabled gates are valuable: for example, the runtime rejects plaintext or anonymous control-NATS configuration, and unsigned GitOps material receives no apply authority. Those denials reduce risk. They are not evidence that a production deployment, ingress, identity lifecycle, or recovery path exists.

## Production gates still missing

- KMS, PKI/Vault, account bootstrap, revocation, and production workload identity qualification.
- A real R3 regional runtime, provider actuators with persisted intent and provider-truth recovery, and qualified systemd/containerd, storage, and TerraBase administrative boundaries.
- Production ingress and private RPC listener policy with workload mTLS and peer identity enforcement. Public REST, WebSocket, and SSE remain separate from private MagicOnion.
- Application-consistent object backup, object-store and retained-volume recovery, clean-room DR, operational observability, alerts, and retained runbook evidence.
- The L4 OCI/ARM destructive boundary lane, including provider APIs, block storage, load balancer, KMS/Vault, and recovery tests.

The source-level R3 journal requirement in [NatsOperationJournalStore](../../../../TerraScale.Orchestrator/src/TerraScale.Orchestrator/Messaging/NatsOperationJournalStore.cs) and the development PKI in [DevelopmentPki](../../../../TerraScale.Orchestrator/src/TerraScale.Orchestrator/Development/DevelopmentPki.cs) are building blocks, not completed versions of those gates.

## Decision

Keep production actuators, public ingress, destructive automation, and production-ready claims disabled until each required real boundary has independently qualified evidence. Do not translate a safe default or pure-test result into an operational SLO or availability claim.

## Evidence provenance

All local evidence below was read with `git show` from the immutable `TerraScale.Orchestrator` tree at `85a162ca45258361ccdb303ce0d5b1047ce59f7e`, not from its working tree. The RF=1 limitation and private-RPC requirements are in `AGENTS.md`; the audited unmet gates are in `docs/guides/production-readiness-audit-2026-08-04.md`; and the source-level journal check is in `src/TerraScale.Orchestrator/Messaging/NatsOperationJournalStore.cs`. The development-only certificate material referenced above is `src/TerraScale.Orchestrator/Development/DevelopmentPki.cs` at the same tree.
