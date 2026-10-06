# P0-02 OCI residual-inventory evidence receipt

Status: source-evidence receipt. The completed independent review is recorded in [the P0-02 independent-review integration record](./p0-02-independent-review.md). This receipt records source evidence only.

## Source and validation record

- Source repository: `TerraScale.Orchestrator` at commit `9d51bd401cc246d6565988150a49747abd77147a`.
- Source files: `docs/evidence/phase0/oci-residual-inventory.yaml` and `docs/guides/phase0-evidence.md`.
- Exact source validation: the evidence inventory is `incomplete-fail-closed`; its current observation states that the OCI CLI was unavailable on the Ubuntu host preflight and that no OCI API request was issued. The evidence records no cloud API mutation.

## Provenance and coverage

The current record is a host-only Ubuntu preflight. It lacked an OCI CLI and did not make an API call. It is distinct from the historical NixOS audit dated 2026-07-13, which observed OCI CLI 3.89.1. That historical observation does not establish OCI CLI availability on the current host.

The archived IAM region-subscription attempt is source-verified from initial evidence commit `1dff42c17b37a26f472f0987aa9e86b5f044ecf7` and redaction-hardened commit `ee72a8f3e3433aa8776ede2e3147815efdcd6881`. It failed authentication before any resource-category query.

The full open inventory surface remains not queried unless explicitly marked unverified: compute instances; block volumes and attachments; backups and volume backups; object-storage buckets; load balancers; public IPs; IAM; Vault/KMS; certificates; workloads; NATS; DNS zones and records; Vault-secret metadata/KMS; Kubernetes/Flux configuration and credential material; Flux webhooks and token metadata; NATS streams and durable consumers; networking; and seven-day cost. OKE and node pools are explicitly unverified. The canonical per-category source list is `docs/evidence/phase0/oci-residual-inventory.yaml` at the cited source commit.

## Safety boundary and limitations

Sensitive material, including secret values, private keys, kubeconfigs, webhook tokens, and NATS credentials, was not read or persisted. No cloud API mutation was performed or authorized.

This receipt is not a discovery, absence, ownership, cleanup, cost, production-gate, or Phase 0 exit claim. It does not establish resource availability, resource absence, ownership disposition, cleanup eligibility, cost status, or production readiness. Authenticated, scoped, read-only discovery and the required category-specific authority remain necessary before any such claim.
