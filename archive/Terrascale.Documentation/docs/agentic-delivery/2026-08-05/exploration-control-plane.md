# Control-plane exploration

Status: planning and evidence record, not production-ready.

## Confirmed evidence

`TerraScale.Orchestrator` has fail-closed pure planners for topology, upgrades, recovery, backups, snapshots, storage, operations, authority, and reconciliation. It also has NATS, Forgejo, and native GitOps planning plus a DevHost RF=1 lab. Relevant evidence is `TerraScale.Orchestrator/docs/guides/production-readiness-audit-2026-08-04.md` and `TerraScale.Orchestrator/src/TerraScale.Orchestrator/ControlPlane`.

## Unmet production gates

The audited implementation lacks a TerraBase mTLS administrative adapter, application-consistent backup and object-store restore, a production GitOps apply path and artifact trust root, real containerd/systemd qualification, PKI/KMS/operator RBAC/audit, HA observability, and production network, DNS, and ingress qualification. The RF=1 lab is development evidence only.

## Delivery implication

Keep lifecycle planning separate from execution claims. Enable branch, restore, and DR automation only after persisted, fenced real-system intent, provider-truth recovery, qualified adapters, and retained recovery evidence. Public interfaces remain REST, with private MagicOnion restricted to TerraScale-owned backend processes on isolated mTLS listeners.
