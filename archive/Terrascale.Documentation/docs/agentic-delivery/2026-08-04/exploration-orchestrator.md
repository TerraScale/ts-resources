# Orchestrator exploration

## Confirmed state

The Orchestrator has a substantial pure decision core, development lab, typed lifecycle planning, and a detailed production-readiness audit. The audit explicitly says it is not ready for a first production deployment.

Missing qualification includes real OCI compute and block-volume actuation, production runtime and systemd/containerd integration, real NATS provisioning and credential lifecycle, TerraBase administrative and object-store restore adapters, HA telemetry, and recovery evidence. Its local RF=1 development topology is useful regional-development evidence only.

## Delivery implications

Branch, restore, and DR claims must remain disabled until the control plane can execute and observe them with fenced, persisted intent and production-qualified adapters. Prioritize NATS identity and permissions, OCI and storage truth recovery, runtime actuation, TerraBase administrative integration, and production telemetry before broad lifecycle automation.

Keep public listeners REST. MagicOnion remains private to TerraScale-owned backend processes, on isolated non-ingress ports with production workload mTLS. It is not an SDK, CLI, Dashboard, MCP, or customer transport.

## Evidence reviewed

- `TerraScale.Orchestrator/docs/guides/production-readiness-audit-2026-08-04.md`
- `TerraScale.Orchestrator/README.md`
- `TerraScale.Orchestrator/AGENTS.md`
