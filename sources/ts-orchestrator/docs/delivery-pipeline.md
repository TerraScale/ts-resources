# Delivery pipeline

Every stage finds its input from the previous
stage's retained record by source revision; nothing is copied by hand except
the signing and authorization decisions policy requires.

## Stages

### 1. Orchestrator CI (`.github/workflows/ci.yml`)

Runs on every push to `main` or `develop` except documentation-only changes
(`docs/**`, `**/*.md`). A newer push cancels a running check of the same
branch; on `main` the newest revision contains every older one and is the
candidate. The run stays one job because `ts-orch release` admission requires
exactly one job in the qualifying run, so parallelism is inside it:
`make ci-verify` runs gofmt, `go vet`, all native Go driver contracts, the sharded race
tests (`scripts/ci/racetest/race-test.sh`) and the static release build at once. The
job then retains both binaries and `qualification.json` (the completion
marker) on `ci-<sha>-run-<id>`. On `main` its last step dispatches
`image.yml` for the same revision, so the image job never holds a builder
slot while the checks run. Pull requests run the fast test tier (`-short`)
and skip the admission client; pushes run every tier (CONTRIBUTING.md).

### 2. TerraBase CI (`terrabase/.github/workflows/fast.yml`)

`fast` (format, Clippy, Fast suite) and `release` (static x86_64 and ARM64
build, smoke run under qemu) run in parallel. On `main`, `release` retains
the exact bytes it tested on `ci-<sha>-run-<id>`; `publish` reads them back
once Fast passes, checks them against the release job's manifest, uploads
`qualification.json` and never rebuilds. It then pins the release in this
repository's `deploy/image/image-inputs.json` through
`scripts/ci/pin-terrabase.sh`, adapted to open a ready-for-review GitHub PR.
Its exact latest head must pass CI after
rebasing on current main. Merge it directly when green; publication then runs
stage 1 and images the new pin.

### 3. Image (`.github/workflows/image.yml`, `deploy/image/`)

`build-image.sh` checks out the named revision and reads every other input
from `deploy/image/image-inputs.json`: the base QCOW2 retained once on
`image-base-noble-arm64-20260926` and verified against Ubuntu's signed
checksums, the trust root and timesyncd config under `deploy/image/inputs`,
the priority profile, and the TerraBase pin (re-derived from its release to
prove it). It finds the orchestrator binary from the successful `ci.yml` run
for the revision, verifies the manifest, run detail and log marker, and
builds a deployment-neutral image with `build-offline.sh` (trust roots only;
identity, anchor and enrollment arrive in launch metadata). The release
`image-<sha>-run-<id>-attempt-<n>` holds the QCOW2, guest kernel,
`SHA256SUMS` and `image-qualification.json`. Automatic builds queue rather
than cancel each other, so a running build always finishes. After preparing
its tools, an automatic build waits for its revision's `ci.yml` run and skips
itself if that run fails or is cancelled, or once a newer main revision has
passed `ci.yml` (`scripts/ci/image-superseded.sh`). `make image SOURCE=<sha>` runs the same
build on a developer machine from the same retained release.

### 4. Promotion (`ts-orch image promote`)

`--dry-run`
runs every read-only gate without importing or signing.

### 5. Rollout

TerraBase binary updates do not need a new image: they
roll out through the managed update path and signed desired state.

## Operator commands

To rebuild a named revision in CI, run the "Qualified GRU ARM64 image"
workflow on `main` from the GitHub Actions page with `source_revision` set;
it needs no other input. `--sign-binary --signing-key leaf.pem` also signs the
binary receipt when the candidate's CI release has none. Local builds are
promoted with `--image-dir`.

## What is automated

| Step | Trigger | Manual input |
| --- | --- | --- |
| Orchestrator checks, binaries, qualification | push to `main` | none |
| Image build and retention | start of `ci.yml` on `main`, built once it passes | none (optional dispatch of a named revision) |
| TerraBase checks, tested-bytes publication | push to TerraBase `main` | none |
| TerraBase pin bump into the image inputs | end of TerraBase `publish` | `TS_PIN_BUMP_TOKEN` secret (decision 2) |
| Local image build | `make image SOURCE=<sha>` | revision |

## Measured (Forgejo runs, 2026-09-29)

| Stage | Before | After |
| --- | --- | --- |
| Orchestrator `ci.yml` | 7m56s warm (run 705), 13–17 min cold | 1m55s–4m32s (runs 717, 719, 725, 727, 729) |
| CI → image handoff | 5 values copied into a manual dispatch | none: `ci.yml` dispatches `image.yml` as it ends |
| Image job | 27–40 min (runs 698, 702) | 6m22s (run 728), 8m30s with a cold base cache (run 726) |
| Image tool setup | about 16 min (fj build, then nixpkgs tools with libguestfs built from source) | 31 s from pinned store paths in `/cache/nix` (10m31s once, to fill the cache) |
| Appliance launches per image | 7 under TCG, about 70 s each | 2 |
| Push → retained image | 45–60 min with hand-copied inputs | about 8½ min, plus any wait for the previous image build |
| TerraBase `main` → published release | about 17 min, published bytes rebuilt (run 1018) | 7m14s, the tested bytes (run 1020) |
| Local image build (KVM) | not available | 1m48s (`make image`) |
| Promotion dry run | about 25 hand-run commands | 1m11s, one command |

## Open decisions

2. **Cross-repository pin bump token.** The Actions token cannot write to
   another repository. Use a narrowly scoped GitHub App installation token
   or fine-grained token with contents and PR write permissions for the target
   repository, stored as a GitHub Actions secret. Open a ready-for-review PR
   for the pin update; never bypass its CI gate or assign the retired reviewer.
3. **Image job capacity.** Use GitHub-hosted runners only. Choose supported
   architecture and virtualization capabilities; do not reintroduce private
   runners to obtain `/dev/kvm`. Retained timings above are historical.
4. **Builder image tools.** The image tools come from the pinned nixpkgs
   revision with a lockfile-keyed GitHub Actions cache. Do not depend on a
   persistent runner filesystem or manual runner image refreshes.
