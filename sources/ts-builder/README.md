# ts-builder

Optional job container for GitHub Actions on GitHub-hosted runners only.
The old dedicated runner is retired. Built by the Nix flake as an OCI image.
This snapshot does not prove a current published image or GitHub repository;
verify the publishing workflow and digest in the current release inventory
before using the GHCR reference below.

**Registry: GHCR** — published as
`ghcr.io/terrascale/ts-builder:latest`

The image includes **Nix** (flakes, writable store, `initializeNixDatabase`)
so jobs can `nix build` inside ts-builder. When CI sets `HOMELAB_NIX_CACHE=1`
and the `HOMELAB_NIX_CACHE_*` substituter env, the `/usr/local/bin/nix`
wrapper adds those caches.

Rust 1.98.1 is the default for TerraBase and ts-auth; Rust 1.97.1 remains
installed for ts-rust. The default toolchain includes x86_64 GNU and musl and
ARM64 GNU targets, with matching cross linkers. TerraBase's `make build` also
uses the baked `make`, `protoc`, CMake, and native compilation tools. The image
includes `cargo-audit` and Playwright with Chromium so ts-auth jobs can use
them without installing tools during the job.

## Build

```bash
nix flake lock
nix flake show
nix fmt
nix flake check
nix build .#oci
skopeo inspect oci:./result:latest
nix run .#image.copyToPodman
podman run --rm ts-builder:latest nix --version
podman run --rm ts-builder:latest ts-builder-verify
```

`nix` in the image is enough to build other flakes (cache hits come from
`HOMELAB_NIX_CACHE_SUBSTITUTERS` when those env vars are set).

## Publish

CI on `main` runs `nix build .#oci` and `skopeo copy` to
`ghcr.io/terrascale/ts-builder:latest`.

GitHub-hosted jobs pull the pinned GHCR image when they start; no persistent
runner warm-up or host access is required.
