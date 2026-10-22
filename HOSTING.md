# Current hosting and snapshot adaptations

As of 2026-10-22, TerraScale production hosting is OCI gru
(`sa-saopaulo-1`) under ts-orch (`ts-orchestrator`). Images use GHCR;
production secrets belong in OCI Vault and are delivered through instance
principal. Existing credential, security, cost and activation approvals apply.

ts-status remains on Cloudflare Workers + D1 and only monitors the public
HTTP API. ts-docs and ts-landing also remain on Cloudflare.

Copied documents are historical snapshots with local adaptations recorded in
`manifest.json`. Obsolete hosting instructions have been retired, without
claiming those historical deployments ran on OCI. Current requirements here
do not prove deployment health or complete secret-delivery automation.

For current implementation and known gaps, consult the tracked ts-orchestrator
`README.md`, `docs/secrets.md`, `docs/ts-auth-deployment.md` and
`deploy/m1/services/` in the production repository.
