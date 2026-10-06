# Implementation: MCP reproducibility

## Delivered commits

MCP delivery commits: `165053f`, `c33d715`, and `349ce2e`.

## Improvements

- The CI SDK is exact.
- Parent restore is locked and its locks are committed.
- Candidate evidence is deterministic.
- Evidence artifacts and lock hashes are recorded.
- Checks require the current source revision, SDK version, and a clean worktree, including submodules and untracked files.

## Residuals

The following remain unclosed exactly:

- signed immutable releases
- protected live public API success/denial lane
- full vendored SDK dependency-closure provenance

These changes strengthen reproducibility evidence. They do not independently qualify a production control plane or establish full-product validation.
