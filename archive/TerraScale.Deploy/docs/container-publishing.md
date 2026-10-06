# Container Publishing

TerraScale.Deploy supports two container publishing strategies.

## C# Services

C# runtime services prefer .NET SDK container publishing:

```xml
<Project>
  <PropertyGroup>
    <ContainerRepository>terrascale-service</ContainerRepository>
    <ContainerImageTags>v1.2.3;main-latest;latest</ContainerImageTags>
    <ContainerRuntimeIdentifiers>linux-x64;linux-arm64</ContainerRuntimeIdentifiers>
    <RuntimeIdentifiers>linux-x64;linux-arm64</RuntimeIdentifiers>
    <ContainerImageFormat>OCI</ContainerImageFormat>
    <ContainerArchiveOutputPath>/artifacts/sdk-containers/terrascale-service.tar</ContainerArchiveOutputPath>
    <ErrorOnDuplicatePublishOutputFiles>false</ErrorOnDuplicatePublishOutputFiles>
  </PropertyGroup>
</Project>
```

```bash
dotnet publish src/Service/TerraScale.Service.csproj \
  --configuration Release \
  /t:PublishContainer \
  -p:CustomAfterMicrosoftCommonTargets=/tmp/terrascale-container-publish.targets
```

The .NET SDK can publish without a Dockerfile and can produce a
multi-architecture OCI image index when multiple container runtime identifiers
are supplied. TerraScale.Deploy always writes that exact image index to the
deterministic `<publish-root>/sdk-containers/<image-repository>.tar` archive
during `build-image`; this phase does not authenticate to or mutate a registry.
An authorized `push-images` phase then uploads the archive to the primary
computed registry repository with `skopeo copy --all --preserve-digests`, once
for the release tag and once for each configured latest alias. The source selector is
`oci-archive:<absolute-archive-path>:<tag>` because the pinned SDK emits one
top-level OCI descriptor per `ContainerImageTags` value and stores the bare tag
in `org.opencontainers.image.ref.name`. `--all` preserves the nested
`linux/amd64` and `linux/arm64` manifests.

The generic deploy phases write this temporary targets file for C# services.
Prefer that CLI path over hand-written publish commands in workflows, because
semicolon-delimited MSBuild list properties are fragile when passed as raw
command-line properties.

Reference: <https://learn.microsoft.com/en-us/dotnet/core/containers/sdk-publish>

Use MSBuild container properties for image behavior:

- `ContainerRepository`
- `ContainerArchiveOutputPath`
- `ContainerImageTags`
- `ContainerRuntimeIdentifiers`
- `ContainerBaseImage`
- `ContainerPort`
- `ContainerEnvironmentVariable`
- `ContainerUser`

The SDK writes a plain OCI tar archive, so the CLI names this output `*.tar`.
Dry-run `push-images` prints the deterministic, credential-free `skopeo` command
vectors without requiring the archive or registry credentials. A non-dry-run
authorized push fails clearly when `build-image` did not produce the archive.

## Dockerfile Services

Use Dockerfile publishing for non-C# apps, for example Dashboard Next/Node.js,
or for C# services that truly need container build steps the .NET
SDK cannot express. The .NET SDK container pipeline cannot emulate Dockerfile
`RUN` commands, so those cases need either a custom base image or Dockerfile
strategy.

Dockerfile services use the deploy CLI buildx flow:

1. Publish app output.
2. Build architecture-specific tags.
3. Push architecture-specific tags.
4. Create multi-architecture manifests.

Package apps build from their standalone publish output. Dockerfile-only
services build from `dockerContext`, which defaults to the repository root when
declared in `.terrascale/deploy.json`.

## Custom Services

Use `publishStrategy: "custom"` only when the image build cannot be represented
by the SDK container publisher or a normal Dockerfile context, for example a
repository that must assemble product-specific tarballs before image creation.
The workflow should still call generic `terrascale-deploy` phases such as
`restore`, `tests`, `build-image`, `push-images`, and `publish-manifests`; the profile then
supplies phase commands such as `buildImageCommands`, `pushImageCommands`, and
`publishManifestsCommands` so release state, coloring, and Forgejo release
creation stay centralized.

## Workflow Shape

Forgejo workflows should install `TerraScale.Deploy.Cli`, then invoke generic
CLI capabilities. The CLI owns checkout, sibling checkout discovery, release
metadata, tests, container publication, and Discord notification.
TerraScale.Orchestrator consumes published immutable artifacts and owns
production delivery, health verification, and rollback.

```bash
terrascale-deploy prepare --checkout
terrascale-deploy restore
terrascale-deploy tests
terrascale-deploy build
terrascale-deploy publish-application
terrascale-deploy build-image
terrascale-deploy push-images
terrascale-deploy publish-manifests
terrascale-deploy deployment-notification
```

Split workflows should still use generic verbs:

```bash
terrascale-deploy prepare --checkout
terrascale-deploy restore
terrascale-deploy tests
terrascale-deploy build
terrascale-deploy publish-application
terrascale-deploy build-image
terrascale-deploy push-images
terrascale-deploy publish-manifests
terrascale-deploy deployment-notification
```

Do not add repository-specific CLI commands for workflow steps. Repository
differences belong in project discovery and `.terrascale/deploy.json`.
