# CI and releases

GitHub Actions on GitHub-hosted runners only. Provision the pinned .NET SDK
in the job; the former dedicated builder runner is retired. This component
snapshot has no verified standalone GitHub repository, so consult the current
release inventory before adopting its example workflow names.

| Workflow | When | Jobs | Blocks merges/releases |
| --- | --- | --- | --- |
| `fast.yml` | push to `main` or of a `v*` tag, pull requests, manual | `fast` and `release` in parallel, then `publish` (pushes only) | yes |
| `slow.yml` | push to `main` (beside `fast.yml`), nightly 03:17 UTC, manual | `slow` | never |

- **fast**: `make restore` (locked mode), `make fmt-check`, `make build CONFIGURATION=Release`,
  `make test-fast CONFIGURATION=Release`.
- **release**: `scripts/ci/stage-release.sh` runs `make publish` for `linux-x64` and
  `linux-arm64` and stages `terrabase-linux-amd64` and `terrabase-linux-arm64`. Both must be
  ELF64 little-endian executables for their machine (`e_machine` x86-64 and aarch64). The amd64
  bytes are smoke-run: `/healthz` must report the csproj version, `/readyz` must be ready, and
  an unknown setting must exit with 2. The x86_64 runner cannot run the arm64 bytes, so the ELF
  header check is all they get before release.
  On a push to `main` or of a `v*` tag, `scripts/ci/release.sh draft` attaches those bytes and
  their checksums (`terrabase-linux-amd64`, `terrabase-linux-arm64` and a `.sha256` for each,
  verifiable with `sha256sum -c`) to a draft release whose notes list both SHA-256 sums:
  - `main`: prerelease `ci-<sha>-run-<run id>`;
  - tag `v<Version>`: release `<tag>` with notes generated from the first-parent history since
    the previous `v*` tag. The tag must match `<Version>` in the csproj and point at a commit on
    `main`; a semantic-version prerelease tag (`v1.2.0-rc.1`) stays a prerelease.
- **publish**: runs only after `fast` and `release` both pass, and publishes that draft
  (`scripts/ci/release.sh publish`). A draft is visible only to repository writers and
  GitHub release publication is gated by successful CI; an unpublished draft
  is not a release. Verify tag creation separately from release publication. A rerun replaces a leftover draft; a published release is never replaced.
  `scripts/ci/check-release.sh` proves this on every run first: it drives `release.sh` against
  a fake release API in a scratch repository.
- **slow**: `scripts/ci/check-reporter.sh` first proves that the failure reporter redacts and
  stays within its memory bound, then `make test-slow CONFIGURATION=Release` runs. A failure opens the issue "Slow test suite
  failed", or comments on it if it is already open (`scripts/ci/report-slow-failure.sh`).

Branch protection on `main` should require `Fast integration / fast` and
`Fast integration / release`.

## Speed

- `fast` and `release` run in parallel; `publish` only publishes the draft and never rebuilds.
- Use GitHub Actions caching keyed by the lockfile for NuGet downloads.
  Locked restore checks package hashes; do not rely on a persistent runner
  filesystem or let PR cache contents bypass integrity checks.
- `release` publishes only the server project (once per runtime); tests are built in `fast` alone.

## Requirements

- Restore `TerraScale.Endpoints` only from its verified current distribution
  source in the release inventory. The old package registry is retired; do not
  assume a GHCR container reference is a NuGet feed. Requalify the exact package
  and hash before changing a consuming dependency.
- GitHub releases use `GITHUB_TOKEN` with `contents: write` in the publication
  job; pull requests receive read-only permissions. Use `gh release` and
  `gh issue` for release and slow-suite failure reporting.
