# TerraScale.Infrastructure (retired)

This repository previously held a production infrastructure stack that is now
**retired and removed**.

## Where production infrastructure lives now

| Concern | Owner |
|---------|--------|
| Control plane, scheduling, native GitOps, host agents, NATS, delivery | [`TerraScale.Orchestrator`](../TerraScale.Orchestrator) |
| Architecture and greenfield deployment posture | [`ORCHESTRATOR.md`](../TerraScale.Orchestrator/ORCHESTRATOR.md) |

Do not restore Kubernetes, Flux, or GitOps YAML into this repository.
