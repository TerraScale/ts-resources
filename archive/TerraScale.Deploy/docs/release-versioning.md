# Delivery identity

Deployments bind an operation to the exact source and artifact that the
caller selected. The source commit and tree digest identify the checkout. The
artifact and manifest digests identify the bytes. Configuration and migration
revisions identify the inputs that can change runtime behavior.

Use the version-1 request document with one command:

```bash
terrascale-deploy deploy --request artifacts/delivery-request.json
```

When the request includes `artifact`, the caller supplies the exact trusted
artifact. When it includes only `source`, `terrascale-deploy deploy --build`
restores, tests, builds, and produces the artifact before delivery. A source
or artifact is required. The two cannot silently substitute one another.

The receipt keeps the same identity and records provenance, health,
convergence, rollback, and audit information. A failed or incomplete health
check cannot become a successful receipt. Error codes and remediation text
are bounded so automation can act on them without parsing private logs.

Deploy publishes only through the approved artifact-store and Orchestrator
interfaces configured by the owning environment. It does not create a second
rollout protocol, keep production state, calculate a version from tags, or
hold cluster credentials.

Forgejo workflow checks and benchmark reports remain ordinary engineering
evidence. They do not grant permission to deliver an artifact.
