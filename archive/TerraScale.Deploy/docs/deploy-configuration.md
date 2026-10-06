# Deploy configuration

`.terrascale/deploy.json` records facts that discovery cannot infer, such as a
service name, an image repository, or a command required by a repository. It
does not describe a release status or a prerequisite workflow.

```json
{
  "services": [
    {
      "name": "dashboard",
      "displayName": "Dashboard",
      "packageManifest": "src/Dashboard/package.json",
      "dockerfile": "deploy/Dashboard.Runtime.Dockerfile",
      "imageRepository": "terrascale-dashboard",
      "publishStrategy": "dockerfile",
      "testCommands": [
        {
          "description": "dashboard checks",
          "command": "./node_modules/.bin/vp",
          "arguments": ["run", "check"],
          "workingDirectory": "src/Dashboard"
        }
      ]
    }
  ]
}
```

The CLI accepts `dotnet-sdk`, `dockerfile`, and `custom` publish strategies.
C# services use SDK container publishing unless the descriptor selects a
Dockerfile. Package apps use their local package runner and Dockerfile.

Configured commands receive no credentials from the CLI. Secrets stay in the
existing secret store and are never copied into a request, receipt, log, or
artifact. Commands run once unless their `attempts` value explicitly permits
safe retries.

## Direct delivery

Create a version-1 `DeliveryRequest` and pass it to one command:

```bash
terrascale-deploy deploy \
  --request artifacts/delivery-request.json \
  --artifact artifacts/service.zip \
  --receipt artifacts/delivery-receipt.json
```

The request must identify its operation, source or exact artifact, target,
configuration, actor, and reason. An artifact path is checked against the
declared digest before the request leaves the machine. `--dry-run` validates
and prints the request without contacting Orchestrator.

To build from the exact source checkout, add `--build`. The CLI verifies the
commit and tree identity, restores dependencies, runs the discovered tests,
builds the application, and creates an immutable local artifact digest before
submitting the request. Deploy does not own production rollout state, cluster
credentials, or provider mutations.

The receipt is the only result a caller needs. It reports `succeeded`,
`failed`, or `rolled_back`, with the operation ID, source, artifact digest,
provenance, health checks, rollback result, audit ID, and a bounded remediation
when an operation fails.
