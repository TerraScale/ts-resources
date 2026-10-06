# Deploy discovery

The generic commands and `terrascale-deploy deploy --build` discover the
deployable application from the checkout. Discovery is deterministic and
fails with the matching names when a repository contains more than one
possible application.

## Order

1. Use an explicit `--project` or `--package-manifest` target.
2. Read `.terrascale/deploy.json` or `terrascale.deploy.json` when no target
   override was supplied.
3. Apply command-line overrides such as `--dockerfile` and
   `--image-repository`.
4. Scan C# projects and select executable, Web SDK, or Worker SDK projects
   that are not tests.
5. Pair a runtime project with its tests by project reference, then by name.
6. Scan package manifests with runtime or build scripts.
7. Match Dockerfiles to a package directory or service name. Pass
   `--dockerfile` for an unusual layout.
8. Discover sibling checkouts required by external C# project references and
   package `file:` dependencies.

If more than one application matches, pass `--service`, `--project`, or
`--package-manifest`. The error lists the names that need a choice.

## Commands

`restore`, `tests`, `build`, `publish-application`, `build-image`,
`push-images`, `publish-manifests`, and `deployment-notification` are generic
repository helpers. They discover the local toolchain instead of encoding a
repository path in workflow YAML. `deploy` composes source verification,
ordinary checks, artifact creation, and the version-1 delivery request.

Package apps use a local `./node_modules/.bin/vp` when present, then the
workspace `vp` runner. C# applications use `dotnet`. Repository-specific
commands belong in structured configuration so their arguments remain visible
and redacted by the same process runner.

Discovery never reads rollout state and never contacts a cluster. Orchestrator
owns authorization, rollout ordering, health, convergence, journaling, and
automatic rollback.

## Production image gate

Main-branch image publication requires the producing workflow to provide an
exact immutable candidate identity in `TERRASCALE_CANDIDATE_DIGEST` (the
`TERRASCALE_ARTIFACT_DIGEST` name is accepted as an equivalent input). The
value must be normalized as `sha256:` followed by 64 hexadecimal characters.
`source_sha` identifies the Git source only and is never used as an artifact
digest. The `prepare` step persists the candidate digest in `state.env`; the
`tests` step persists successful evidence bound to that same digest. Every
publish-capable step rejects missing, failed, stale, or mismatched evidence,
including retries and resumed invocations. A main-branch run must not use
`--skip-project-tests`; requesting that option invalidates any existing test
evidence before the request is rejected. Non-dry-run prepare, test, and
publish-capable phases share the workflow lock, so state and test evidence are
revalidated after lock acquisition before hooks or publication work run.

The producing workflow must also provide a trusted produced-artifact receipt
for non-SDK image publication through
`TERRASCALE_PRODUCED_ARTIFACT_RECEIPT` (or the equivalent
`TERRASCALE_ARTIFACT_RECEIPT`). The receipt is JSON with version `1` and these
fields: `artifactPath`, `artifactDigest`, `candidateDigest`, `eventName`,
`sourceRef`, `sourceSha`, `service`, `targetImage`, `profile`, and
`workflowStep` (`build-image`). The artifact path must resolve inside the
publish directory and the receipt must be inside the workflow state or publish
directory. Before publication, the CLI hashes the artifact bytes and checks the
receipt digest, candidate digest, source identity, service, target, publishing
profile, and producing workflow step. SDK container publishing writes this
receipt for its generated archive automatically; custom and Dockerfile builds
must write one before a later publication phase.

`TERRASCALE_CANDIDATE_ARTIFACT` and `TERRASCALE_CANDIDATE_MANIFEST` are not
publication authorization and are ignored by the publication gate. The
candidate digest remains the upstream immutable identity, while `source_sha`
identifies Git source; neither is substituted for a produced-artifact receipt.

Configured `beforeTestCommands`, `testCommands`, and `afterTestCommands`
receive the candidate and persisted workflow-state environment, including
`TERRASCALE_CANDIDATE_DIGEST`, `TERRASCALE_TESTS_PASSED`, and
`TERRASCALE_TESTS_PASSED_DIGEST`. An `afterTestCommands`-only configuration is
deliberately a valid production test gate: successful after-test commands write
durable evidence bound to the current candidate even when no project test is
discovered.
