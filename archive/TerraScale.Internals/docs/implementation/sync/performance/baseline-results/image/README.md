# Exact-source baseline image recipe

The image identity in `../capture.json` is preserved legacy capture evidence.
Decision-grade runs import the reviewed OCI archive
`.artifacts/benchmark-vm/images/terrabase-sync-baseline.oci`, whose required
SHA-256 is
`3f0b99b5f90f9abfddce7c54cd2d9838baf7fe84b4d3186f417f9eadd55b639e`.
The archive contains the exact starting TerraBase image ID
`sha256:41458402507086af004951f180666439e7ee6459202587f30ccbdb40e48c2faa`.

Create a disposable checkout at the exact commit, stamp only its build metadata,
publish Release, and build from the pinned runtime base:

```bash
git clone --no-local /workspaces/TerraScale/TerraBase /tmp/terrabase-sync-image-source
git -C /tmp/terrabase-sync-image-source checkout --detach e149ba4eccf22725313ee36900b2aa3aa3f07856

dotnet StampVersion.cs \
  /tmp/terrabase-sync-image-source/src/TerraBase.Client/Properties/VersionInfo.cs \
  e149ba4eccf22725313ee36900b2aa3aa3f07856

dotnet publish \
  /tmp/terrabase-sync-image-source/src/TerraBase.Server/TerraBase.Server.csproj \
  --configuration Release \
  --output server

podman build \
  --file Containerfile \
  --tag localhost/terrabase-sync-baseline:e149ba4eccf \
  .
```

Run those commands from this directory. Use a fresh disposable source directory
and empty `server` output each time. The rebuild must report the expected commit
through TerraBase’s build-version endpoint before it is admitted to a benchmark
settings file. Refer to the resulting immutable image ID or manifest digest,
never the mutable tag.

The original capture used this Containerfile shape and pinned parent image.
Export the rebuilt image into one OCI archive, subject the archive and exact
harness source to independent review, and update the launcher pin when its
digest changes. A different archive digest is a new input even when OCI
timestamps are the only suspected cause; it is never admitted as silently
equivalent.

Run the reviewed archive only through the dedicated launcher:

```text
dotnet tools/BenchmarkVm.cs run \
  --oci-archive .artifacts/benchmark-vm/images/terrabase-sync-baseline.oci \
  --review reviews/YYYY/MM/DD/<review>/review.json \
  --settings benchmarksettings.json \
  -- <harness-command>
```

The launcher verifies the archive digest before starting QEMU and binds it into
both phases of the host attestation. The reviewed
`benchmarksettings.json` SHA-256 is
`de7f8692d904ea46db858b9a663697aa37d4e6cca22287be5a38a02ff0f4caa9`;
changing it requires a new exact-source review.
