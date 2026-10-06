# Adversarial reviews

Each major harness or TerraBase performance change gets a new immutable
`reviews/YYYY/MM/DD/<timestamp>-<change>/review.json` record from a reviewer who
did not implement the change.

The review must try to falsify the result: hidden errors or missing operations,
weaker durability or batching, stale indexes, timed setup work, harness/client
bottlenecks, incomparable allocation or memory categories, file-cache/mmap/GC
artifacts, biased order or statistics, environmental drift, races, corruption,
lost writes, tail regressions, unrelated workload regressions, dirty or mutable
source, secrets, unsafe exposure, and destructive cleanup.

Before committing any history, review, or baseline artifact, run
`dotnet tools/SanitizeHistory.cs --check`. It validates only the tracked safe
artifact allowlist (`history/**/result.json`, `history/**/failure.log`,
`reviews/**/review.json`, and `baselines/approved.json`); run it without
`--check` to redact those files in place. This protects current files and does
not remove data from historical Git objects.

For the dedicated KVM environment, also attack nonce replay, initial/final
attestation mutation, guest-writable evidence, shared or traversable 9p paths,
missing raw-evidence digest closure, incorrect or escaped QEMU/vCPU pinning,
per-vCPU schedstat attribution or non-monotonic samples, activity on QEMU-unused
SMT siblings, an isolation identity that overclaims external host visibility,
host IRQ/steal/virtual-frequency/TSC drift, explicit KVM thermal-unavailability
identity, rootless cgroupfs/slirp4netns identity with the slirp port handler and
image healthchecks disabled, QEMU swap despite
`MemorySwapMax=0`, DevHost isolation and restoration,
unsafe cache/snapshot storage, false allocation or FUA reporting, and
cleanup against a reused process ID or unowned path. Verify that the review
binds the tracked settings and OCI hashes, boot seed and both firmware inputs
are attested, SSH host keys are pinned before agent forwarding, every immutable
image is present before timing, controller work is isolated, the reviewed ext4
host source is attested, the raw file stays fully allocated, trim/discard stays
off, the root-created system service uses the intended CPU/NUMA policy,
delegated controllers, private runtime directory, and zero-swap limit, the
guest proves read-only evidence and isolated completion writes across the 9p seam, active-run
admission is atomic, and baseline manifests cannot be written before completed
valid host attestation. On a nested host, require proof of the launcher-visible
exclusive cpuset partition and scope claims to that KVM guest lane.
Confirm disposable run cleanup cannot remove immutable provisioned assets or
the compact committed evidence record.

Use `severity: "blocking"` for correctness, durability, comparison validity,
reproducibility, security, data loss, or a regression-gate violation. Major work
does not push or land until every blocking finding has `disposition:
"resolved"` and the review's top-level `disposition` is `"pass"`.
