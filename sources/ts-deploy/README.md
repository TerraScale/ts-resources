# ts-deploy

`ts-deploy` is a small C# helper CLI for three specific jobs: validating
version-1 delivery documents offline, announcing finished production
deployments on Discord once they are actually online, and inspecting — or
manipulating — Forgejo through the pinned `fj` CLI. It is built as one
self-contained binary from `src/TerraScale.Deploy/` with a focused test
project under `tests/TerraScale.Deploy.Tests/`.

It is deliberately not a workflow engine and not a deployer. Repository
workflows own their verification and release steps explicitly in their own
YAML. TerraScale.Orchestrator alone authorizes and performs production
rollout and rollback; this CLI never contacts cluster members, submits
delivery requests, or owns rollout state.

## Commands

All settings are explicit arguments; the client does not read a configuration
file.

- `ts-deploy validate (--request <path> | --request-json <json>) [--receipt <path> | --receipt-json <json>]`
  validates a delivery request and, when supplied, its matching receipt
  entirely offline.
- `ts-deploy notify (--request <path> | --request-json <json>)
  (--receipt <path> | --receipt-json <json>) --discord-webhook <url>
  [--discord-username <name>] [--discord-avatar-url <url>]
  [--health-url <url> | --skip-health-check]
  [--health-timeout <seconds>] [--health-interval <seconds>] [--health-region <region>]`
  sends the Discord production-ready notification for an existing receipt.
  Only a `succeeded` receipt targeting `production` notifies; everything else
  is skipped with a zero exit code. Production-ready notifications require
  `--health-url` pointing to the live `/readyz` endpoint, which must answer
  exactly HTTP 200 without redirects. Each invocation probes again with
  caching disabled, polling past connection errors and unsuccessful answers;
  waiting past the bound (default 300 seconds, polling every 5 seconds) fails
  without notifying. `--health-region` additionally requires exactly one
  `X-TerraBase-Region` response header value matching the supplied region.
  `--skip-health-check` is an explicit, logged opt-out for non-production
  targets only, cannot be combined with health options, and does not enable
  non-production notifications. Failed production receipts still skip without
  needing a health URL.
- `ts-deploy forgejo release-list --repo <owner/name>` lists releases,
  including drafts and prereleases.
- `ts-deploy forgejo release-view --repo <owner/name> --tag <tag>` reads one
  release by tag.
- `ts-deploy forgejo tag-commit --repo <owner/name> --tag <tag>` resolves a
  tag to its commit.
- `ts-deploy forgejo variables --repo <owner/name>` lists repository Actions
  variables.
- `ts-deploy help [command]` prints command help.

Forgejo operations run through the pinned `fj` CLI, which owns the host,
credential store, and output format; the CLI never speaks the Forgejo API.
The exposed Forgejo operations accept `--host`, `--repo owner/name`,
`--working-directory`, and `--json` where a structured result exists. The
`ForgejoProvider` additionally exposes the manipulation surface used by earlier
workflow lanes — idempotent release creation, release asset upload and download
with digest comparison, issue search, creation, labeling, commenting, and
closing, and workflow dispatch — so future lanes can drive Forgejo without
reassembling `fj` argument vectors. See `docs/adr/0004-forgejo-provider.md`.

## Repository workflow

`.forgejo/workflows/ci.yml` runs on pushes to `main` and manual dispatch. Its
`ci` job verifies the client directly:

```yaml
      - name: Restore .NET dependencies
        run: dotnet restore TerraScale.Deploy.slnx --nologo
      - name: Build the deployment client
        run: dotnet build TerraScale.Deploy.slnx --configuration Release --no-restore --nologo
      - name: Verify dependency audit failure handling
        run: dotnet run scripts/check-nuget-vulnerabilities.tests.cs -- --minimum-expected-tests 13
      - name: Fail closed on vulnerable NuGet packages
        run: dotnet run scripts/check-nuget-vulnerabilities.cs src/TerraScale.Deploy/TerraScale.Deploy.csproj tests/TerraScale.Deploy.Tests/TerraScale.Deploy.Tests.csproj
      - name: Check .NET formatting
        run: dotnet format style TerraScale.Deploy.slnx --verify-no-changes --no-restore
      - name: Run client tests
        run: >-
          dotnet run --project tests/TerraScale.Deploy.Tests/TerraScale.Deploy.Tests.csproj
          --configuration Release --no-build --no-restore --
          --minimum-expected-tests 1
```

The `release` job then publishes the Deploy CLI for linux/amd64 and
linux/arm64 with `dotnet publish` as self-contained single files. Each commit
becomes a `v<version>-dev.<commit>` Forgejo release carrying both binaries,
their metadata, and a manifest signed with `TS_DEPLOY_RELEASE_SIGNING_KEY_B64`
(checked against the `TS_DEPLOY_RELEASE_KEY_SHA256` variable); an existing
release for the tag is left untouched.

See:

- `docs/forgejo.md` (Forgejo Actions logs API)
- `docs/adr/README.md`
