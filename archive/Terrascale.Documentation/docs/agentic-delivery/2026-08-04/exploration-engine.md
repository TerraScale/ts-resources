# Engine exploration

## Confirmed capabilities

TerraBase contains periodic backup, restore, restore-point, and replication implementation and tests. These are engine primitives suitable for a managed recovery system.

## Boundary and gap

The reviewed engine source has no native managed-branch lifecycle. A customer branch requires product-level intent, source selection, isolated placement, lifecycle controls, quotas, retention, authorization, operation history, and deletion semantics. It cannot be represented merely as a backup folder or an engine-side restore command.

## Delivery direction

Use TerraBase backup and restore primitives behind an explicit managed recovery workspace and branch state machine. First support restore validation in isolation. Then add branch creation from an approved snapshot or point-in-time source, read/write isolation, expiry, promotion or merge policy where applicable, and auditable teardown. Replication and restore topology must be validated under the production control plane rather than inferred from local tests.

## Evidence reviewed

- `TerraBase/src/TerraBase.Server/Web/System/BackupDatabaseHandler.cs`
- periodic backup and restore namespaces under `TerraBase/src/TerraBase.Server`
- replication and backup test coverage under `TerraBase/test`
