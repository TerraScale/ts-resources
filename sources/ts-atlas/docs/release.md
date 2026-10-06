## Signed release attestation

Each `ts-atlas` release publishes only the deterministic
`ts-atlas-edge-contract-v1.tar` archive, its `.metadata.json`, the signed
`ts-atlas-release-manifest.json`, its detached
`ts-atlas-release-manifest.sig`, and `ts-atlas-release-public.pem`. The
manifest binds the source commit, byte count, and SHA-256 digest of the
contract bundle. Normalized tar metadata makes the archive reproducible.

The Forgejo release job requires the managed
`TS_ATLAS_RELEASE_SIGNING_KEY_B64` secret and the trusted
`TS_ATLAS_RELEASE_KEY_SHA256` fingerprint before publication. Consumers can
verify the signature, expected source revision, trusted key, and artifact bytes
with:

```bash
node scripts/verify-release-attestation.mjs \
  ts-atlas-release-manifest.json \
  ts-atlas-release-manifest.sig \
  ts-atlas-release-public.pem \
  ./release-assets "$EXPECTED_COMMIT" "$TRUSTED_KEY_SHA256"
```

`TRUSTED_KEY_SHA256` is the lowercase SHA-256 of the approved public key's DER
SubjectPublicKeyInfo encoding. Record it in the release inventory and get
release-owner approval before the first production publication. Obtain it from
the independently approved key inventory, never from the release being
verified. Set the protected repository variable `TS_ATLAS_RELEASE_KEY_SHA256`
to that value for CI. `EXPECTED_COMMIT` must come from the reviewed release
request. Key rotation requires a reviewed inventory and variable update
alongside managed signing-key provisioning.

The archive is covered by the same signed manifest. SDK CI can stage the exact
edge bundle through `EDGE_CONTRACT_SOURCE` after downloading the immutable
release asset. A signature proves possession of the configured release key and
integrity of the manifest; it does not replace protected review or independent
key custody.
