# Validation evidence

Date: 2026-08-04

This record contains reproducible command outcomes only. It excludes credentials, raw configuration, and remote URLs.

## Documentation content claims

Command:

```text
npm run content:claims
```

Outcome: exit `0`; `public content claim validation passed`.

## C# MCP v0.1.0 source validation

The following results were recorded from `TerraScale.Mcp` release source commit `17d4bfa`. They contain no credentials, raw configuration, or remote URLs.

```text
dotnet restore TerraScale.Mcp.sln
dotnet build TerraScale.Mcp.sln -m --no-restore
dotnet test TerraScale.Mcp.sln --no-restore
dotnet build TerraScale.Mcp.sln -c Release -m --no-restore
dotnet test TerraScale.Mcp.sln -c Release --no-restore
```

Outcomes: restore passed; the Debug build passed with zero warnings and zero errors; the Debug test run passed 25 of 25 tests; the Release build passed with zero warnings and zero errors; and the Release test run passed 25 of 25 tests. These source test runs did not exercise environment-gated live public API calls, so they are not evidence of live public API access.

### C# MCP package validation

```text
dotnet run --project tools/TerraScale.Mcp.Bundle --
dotnet run --project tools/TerraScale.Mcp.Bundle -- --verify
unzip -t artifacts/mcpb/terrascale-win-x64.mcpb
unzip -t artifacts/mcpb/terrascale-osx-arm64.mcpb
unzip -t artifacts/mcpb/terrascale-osx-x64.mcpb
unzip -t artifacts/mcpb/terrascale-linux-x64.mcpb
jq 'type == "object" and length == 4 and all(.[]; test("^[0-9A-F]{64}$"))' artifacts/mcpb/checksums.json
```

Outcomes: the bundle command produced the complete four-bundle set; strict `--verify` passed; each named `.mcpb` passed `unzip -t`; and `jq` confirmed the checksum manifest is an object of length four with every checksum matching `^[0-9A-F]{64}$`.

The authenticated Forgejo release is [TerraScale MCP v0.1.0](https://git.terrascale.tech/TerraScale/TerraScaleMcp/releases/tag/v0.1.0). Its remote annotated tag `v0.1.0` resolves to tag object `0d2fb560...`, while release source remains `17d4bfa`; the attached product assets are exactly `checksums.json` and the four bundles above. Forgejo creates source archives automatically.

## Deploy SDK pipeline tests

Command:

```text
dotnet test tests/TerraScale.Deploy.Cli.Tests/TerraScale.Deploy.Cli.Tests.csproj --configuration Release --no-restore
```

Outcome: passed. Three Docker-gated registry recovery tests were skipped because a running Docker daemon with the required local registry and image was unavailable:

- `RealRegistryRecoveryRetriesEachTagWithoutSerializingPlatforms`
- `RealStoppedRegistryCancellationDoesNotStartAnotherAttempt`
- `RealStoppedRegistryExhaustionReportsTagAttemptsAndProcessFailure`

The skips are environment gates, not passing Docker integration evidence.

## Ordinary push attempts

Commands:

```text
git push origin develop
```

Outcome for both the Documentation and Deploy repositories: exit `1`; Forgejo rejected the ordinary non-force update because `develop` is protected. No force push or protection bypass was attempted.
