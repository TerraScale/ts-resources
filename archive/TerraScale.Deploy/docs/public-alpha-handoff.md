# Direct delivery handoff

This file is kept at its historical path so links in older checkouts do not
break. The supported handoff is the version-1 `DeliveryRequest` consumed by
`terrascale-deploy deploy`. One request is enough.

```json
{
  "schemaVersion": 1,
  "operationId": "client-generated-opaque-id",
  "source": {
    "repository": "TerraScale/TerraScale.Orchestrator",
    "commit": "40-hex-git-commit",
    "treeDigest": "sha256:..."
  },
  "artifact": {
    "digest": "sha256:...",
    "manifestDigest": "sha256:...",
    "kind": "service"
  },
  "target": {
    "service": "named-public-service",
    "environment": "development",
    "regions": ["gru"]
  },
  "configurationRevision": "sha256:...",
  "migrationRevision": null,
  "requestedBy": "authenticated-actor-id",
  "reason": "bounded-human-or-automation-reason"
}
```

The command accepts either an exact trusted artifact or a source identity that
it can build. It validates every digest and bounded text field before sending
the request. The request contains no secret.

The Orchestrator returns one `DeliveryReceipt` with the same operation ID,
source, target, and artifact digest. A successful receipt requires verified
provenance, passed health checks, and convergence. If mutation began and the
safe previous artifact exists, Orchestrator attempts rollback and reports
`rolled_back` only after rollback health checks pass. Deploy reports the
receipt without taking ownership of rollout state or provider credentials.
