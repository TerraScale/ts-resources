# SDK snapshot-reference fix record

## Change

Deploy commit `bd5ecec12efa857d098dfe12584c9a548eb3d06b` changes the SDK pipeline's Documentation snapshot ref from `main` to `develop`. The pipeline now defines the ref once and passes it to checkout bootstrap. Its targeted `GenericWorkflowCommandTests` assertion verifies the dry-run checks out `TerraScale/TerraScale.Documentation develop` and does not select `main`.

## Review and evidence

The recorded independent final review accepted the narrow implementation: it changes only snapshot selection and its dry-run test expectation, with no credentials, API bypasses, or contract mutation. The code-level evidence is the `SdkPipeline.cs` change and the corresponding `GenericWorkflowCommandTests.cs` assertions in the same commit. The later command outcomes are recorded in [validation evidence](validation-evidence.md).

The observed Deploy test command passed with three Docker-gated registry tests skipped, as recorded in [validation evidence](validation-evidence.md). It does not establish a successful SDK release validation. The TypeScript drift command currently fails at `147/149`, because the Documentation snapshot is missing the two billing-access operations. Snapshot regeneration, a passing drift check, and the normal repository test/build gates remain required.
