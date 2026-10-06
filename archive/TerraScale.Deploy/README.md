# TerraScale.Deploy

Internal deployment and CI diagnostics tooling for TerraScale Forgejo Actions.

## Commands

- `terrascale-deploy forgejo failures`: inventory failed, running, and cancelled
  Forgejo action tasks across configured TerraScale repositories.
- `terrascale-deploy ci validate`: validate local workflow and repository
  policy assumptions before editing or dispatching CI.
- `terrascale-deploy ci public-alpha-handoff`: validate exact-candidate Public
  Alpha evidence and write the digest-bound Orchestrator handoff.
- `terrascale-deploy ci public-alpha-rollback`: write per-region rollback
  intents from a verified handoff and recorded progress. It never builds or
  changes traffic.
- `terrascale-deploy prepare`, `restore`, `tests`, `build`,
  `publish-application`, `build-image`, `push-images`, `publish-manifests`,
  and `deployment-notification`: run workflow-facing build and publication
  stages. TerraScale.Orchestrator owns production delivery and verification.
- `terrascale-deploy retention`: run generic artifact retention policies.
- `terrascale-deploy notify discord`: post a deployment notification.
- `terrascale-deploy sdk validate`: run shared SDK and Pages validation checks.

The CLI accepts explicit tokens through environment variables such as
`FORGEJO_TOKEN`, but it can also fall back to the locally authenticated `fj`
CLI for failure inventory when API credentials are not present.

## Release Discovery

The workflow-facing stage commands discover deployable projects dynamically.
They scan C# projects, solutions, test projects, package manifests,
Dockerfiles, project references, and package `file:` dependencies, then apply
any `.terrascale/deploy.json` overrides.

C# services use .NET SDK container publishing by default. Package apps and
other non-C# services use Dockerfile publishing.

See:

- `docs/deploy-discovery.md`
- `docs/deploy-configuration.md`
- `docs/container-publishing.md`
- `docs/release-versioning.md`
- `docs/public-alpha-handoff.md`
