# Provisioning and recovery parity readiness

Status: implementation substrate exists; production qualification does not.

## Evidence present

Project provisioning has a concrete, fail-closed implementation. [ProjectDatabaseProvisioner](../../../../TerraScale.Internals/src/Platform/TerraScale.Platform/Features/Projects/Services/ProjectDatabaseProvisioner.cs) creates or heals a project physical database, requires the configured topology floor outside explicitly reduced development topology, and does not silently recreate a missing ready database. The public backup confirmation flow has an [AppHost integration test](../../../../TerraScale.Internals/src/Platform/TerraScale.Platform.Tests/Database/DatabaseBackupConfirmationAspireAppHostIntegrationTests.cs), and the Platform contains typed backup, restore-point, restore-job, reconciliation, and side-by-side restore code under [`Features/Backups`](../../../../TerraScale.Internals/src/Platform/TerraScale.Platform/Features/Backups/).

This is source and local-AppHost evidence. It is not production storage, provider, or recovery qualification.

## Not delivered

Do not describe any of the following as available:

- database branches or clones, including branch lifecycle and TTL cleanup;
- PITR semantics, recovery-point retention guarantees, promotion, or merge behavior;
- production side-by-side restore and cutover;
- clean-room disaster-recovery evidence, or committed RPO and RTO values.

The current platform API/SDK backup and restore surface remains meaningful for its stated contract. It cannot be relabeled as branching or PITR. The Orchestrator's audited gap list separately confirms that application-consistent object backup/restore and retained-volume recovery have not reached real-system qualification. See its [production-readiness audit](../../../../TerraScale.Orchestrator/docs/guides/production-readiness-audit-2026-08-04.md).

## Required parity path

First qualify the production recovery substrate: application-consistent backup, object-store restore, provider-truth recovery, and clean-room drills against an agreed RPO/RTO. Then publish a distinct versioned public lifecycle contract for create-from-source or restore-point, candidate validation, explicit promotion or cutover, deletion, lineage, TTL, idempotency, authorization, audit, and meter attribution. Add SDK, Dashboard composition, and optional read-only MCP projections only after that contract is proved.

## Evidence provenance

All local evidence below was read with `git show` from immutable trees, not from sibling working trees. The provisioner, backup implementation directory, AppHost test, and public snapshot are from `TerraScale.Internals` commit `5ba9722953871fc46384d48e52e8660612b93c34`. The current public artifact is `docs/product/openapi/server.openapi.json`, SHA-256 `ee71b5998353a4a8559e3197e572c513e82a577bda60858514a4b532001a351a`; it contains project-database create and backup plan, execute, restore-point, and restore paths. The artifact's last modifying commit is `9e9d3851742335869186747a09389143f749aff7`.

The .NET SDK evidence is `TerraScale.DotNet` commit `0286964d559fff314ced3269357ee1c4f8d5546b`: package version `0.1.0` in `src/TerraScale.DotNet/TerraScale.DotNet.csproj`, and `TerraScaleBackupsClient.cs` SHA-256 `2d6c40daddb40bad135c93969b531ef2264ed1a1892417eed4f04fde2c98f872`. The production-gap comparison is `TerraScale.Orchestrator` commit `85a162ca45258361ccdb303ce0d5b1047ce59f7e`, `docs/guides/production-readiness-audit-2026-08-04.md`.
