# TerraScale.Infrastructure (retired)

This repository previously held TerraScale production infrastructure as **OCI OKE + Flux/GitOps + Pulumi**.

That stack is **retired and removed**.

## Where production infrastructure lives now

| Concern | Owner |
|---------|--------|
| Control plane, scheduling, native GitOps, host agents, NATS, delivery | [`TerraScale.Orchestrator`](../TerraScale.Orchestrator) |
| Architecture and greenfield deployment posture | [`ORCHESTRATOR.md`](../TerraScale.Orchestrator/ORCHESTRATOR.md) |

Do not restore Kubernetes, Flux, OKE node pools, or GitOps YAML into this repository.
