# TerraScale Sync starting performance baseline

Status: exact source and image preserved; attested KVM timing runs pending.

No TerraBase hot-path change may begin until the attested KVM runs below pass.
Failed or environment-invalid checks are evidence, not baseline measurements.

## Exact starting source

| Item | Value |
| --- | --- |
| TerraBase commit | `e149ba4eccf22725313ee36900b2aa3aa3f07856` |
| Source branch | `bench/baseline-sync-20260726` |
| Isolated worktree | `/workspaces/TerraScale/TerraBase.Benchmark/.worktrees/baseline-sync-20260726` |
| Source state | clean; commit equals `origin/develop` at capture |
| Legacy capture harness | `a9e3650c50d33753613e1e0f28e29805a6585e7c` |
| Legacy harness review | `20260726T160523Z-9207e2f-adversarial` — pass before the KVM environment change |
| KVM harness review candidate | `59fbbb3d7212045c380f888bfd5d8764bf1a8ab1` |
| KVM environment review | exact-source re-review in progress |
| OCI image ID | `sha256:41458402507086af004951f180666439e7ee6459202587f30ccbdb40e48c2faa` |
| OCI manifest digest | `sha256:b2d1404a19c682f406c4238c89f5e2c28624bf002fc9fc6b652e1eeb9cb7601f` |
| Local immutable reference | `localhost/terrabase-sync-baseline@sha256:b2d1404a19c682f406c4238c89f5e2c28624bf002fc9fc6b652e1eeb9cb7601f` |
| Embedded revision | `e149ba4eccf22725313ee36900b2aa3aa3f07856` |

The exact-source Release publish was placed over the existing reviewed
TerraBase benchmark image runtime. A smoke start proved that the server banner
reported the captured commit. This validates artifact identity only; it is not a
latency or throughput result.

Machine-readable facts from the legacy invalid development-container capture
are preserved in `baseline-results/capture.json`. A separate KVM capture is
written only from an actual finalized guest result.

## Host

| Item | Value |
| --- | --- |
| Host | `mariogk-dev` |
| OS | Ubuntu 26.04 LTS |
| Kernel | `7.0.0-28-generic` |
| CPU | 2 × Intel Xeon E5-2660 v4, 28 physical / 56 logical cores |
| NUMA | node 0: CPUs `0-13,28-41`; node 1: CPUs `14-27,42-55` |
| Memory | 121 GiB |
| CPU governor | `performance` |
| Workspace storage | NVMe, btrfs |
| .NET SDK/runtime | 10.0.302 / 10.0.10 |
| Podman | 5.7.0 |

Decision-grade runs now use a disposable 24 GiB, 13-vCPU QEMU/KVM guest rather
than treating the development container as the benchmark host. Guest CPUs
`0-3` are clients, `4-5` are helpers, `6-11` are the server, and `12` is
housekeeping; QMP pins guest vCPU `0-12` to host CPU `0-12` before the VM
continues. QEMU emulator and I/O work stays on host CPUs `13,41`; launcher,
SSH, monitor, and run-preparation work stays on host CPUs `27,55`. The database
cgroup limit remains 8 GiB with no swap allowance.

The guest uses the existing host SSD through a fresh fully allocated raw data
disk: 1 GiB for tmpfs, test, self-test, and approval runs; 128 GiB only for
Persistent and Soak. QEMU exposes the disk as non-rotating virtio-scsi with
direct, uncached, write-through I/O and FUA; the guest mounts it at
`/var/lib/terrabase-benchmark`. A separate disposable root overlay prevents
state reuse. No additional NVMe device or host storage migration is required.

The launcher stops DevHost for every guest command, proves no process remains
in its cgroup, and restores its prior state during cleanup. A host monitor
covers the complete measurement interval and binds exact source, settings,
image, firmware, QEMU command, vCPU mapping, storage, thermal, interrupt, swap,
and DevHost state evidence to the guest result. The guest cannot publish a
decision-grade result until it signals completion and verifies the finalized
read-only host attestation.

The selected settings file is tracked and its SHA-256 plus the OCI archive
SHA-256 must appear in the exact-source review. Each run regenerates and
attests its cloud-init seed from reviewed input, verifies both OVMF templates,
authenticates the guest SSH host before forwarding the Forgejo agent, and
pre-pulls every immutable competitor/tracer digest before timing. The host
storage check binds `/var/tmp` to the reviewed non-rotating physical device,
keeps the NOCOW raw file fully allocated, and disables guest trim and QEMU
discard.

## Legacy invalid attempts

Two harness self-test records were created before any hot-path change:

| Run | Result | Reason |
| --- | --- | --- |
| `20260726T140241Z-self-test` | failed | runner lacked the required pre-CLR NUMA bind |
| `20260726T140258Z-self-test` | failed | self-test helper-registration race |

The second run used the required NUMA launch policy. Its environment probe also
correctly marked the host invalid because:

- median background CPU was 6.95%, above the 5% limit;
- load average 5.91 exceeded the committed threshold;
- another TerraBase workload was running;
- the current runner cgroup does not delegate cpuset.

The active `terrascale-devhost.service` owned the competing TerraBase, Platform,
Authentication, Dashboard, NATS, and controller processes during these
attempts. The KVM launcher supersedes the old bare-container assumption: it
stops DevHost, proves its cgroup quiescent, and restores its prior state for
every guest command. Raw attempt references remain recorded in
`baseline-results/attempts.json`.

## Fixed benchmark configuration

The existing first-party realistic harness is the authority for HTTP/database
measurements. Its fixed starting profiles are:

| Profile | Seed | Operations | Samples | Concurrency | Storage |
| --- | ---: | ---: | ---: | --- | --- |
| smoke | 20,000 | 20,000 | 3 | 16 | tmpfs |
| standard | 100,000 | 100,000 | 10 | 1, 16, 64 | tmpfs |
| persistent | 100,000 | 100,000 | 10 | 1, 16, 64 | isolated raw guest disk on host SSD |
| soak | 1,000,000 | 10,000,000 or 30 min | 1 | 64 | isolated raw guest disk on host SSD |

Timed setup excludes container start, database creation, seeding, index
creation, warmup, and result serialization. Existing measurements include
throughput, p50/p95/p99, CPU, allocations, GC, working set, network bytes,
storage IO, durable sync evidence, restart durability, and environment drift.

## Required starting matrix

Before TerraBase commit/query hot paths change, preserve decision-grade results
for:

- single-document read;
- partition/prefix read;
- indexed range and empty indexed range;
- insert, update, delete, and acknowledged commit;
- batch write;
- concurrent read, write, and mixed workloads;
- replication apply;
- query/result serialization;
- Platform-to-TerraBase request latency.

The reviewed first-party realistic harness covers single read, equality query,
partition read, indexed and empty indexed ranges, insert, update, delete, batch
write, mixed concurrency, durability, network, allocations, GC, and storage.
Replication apply and serialization stay in their existing first-party
benchmark projects.

BenchmarkDotNet remains the microbenchmark authority inside TerraBase for
in-process primitives. The starting micro set will reuse existing Voron table
read/insert, transaction-merger, blittable serialization, and hashing
benchmarks. New Sync primitive benchmarks are added only after their production
types exist, so benchmark-only duplicate algorithms cannot drift from the
implementation.

Persisted samples include mean and maximum latency plus runtime monitor-lock
contentions per successful operation. Storage amplification is calculated from
physical cgroup IO bytes divided by acknowledged logical payload bytes.

## Noise and gates

Noise is established from at least two independent valid Standard runs and the
per-case sample distributions. The threshold for stable microbenchmarks is the
greater of 3% or twice measured noise. The threshold for p95/p99 integration
latency is the greater of 5% or twice measured noise.

Every post-change run uses the same source-derived image strategy, hardware,
CPU/NUMA sets, datasets, warmup, samples, operation sequences, and measurement
windows. Required comparison variants are:

1. original TerraBase;
2. modified TerraBase with Sync disabled;
3. modified TerraBase with durable Sync enabled and zero subscribers;
4. modified TerraBase with active subscribers;
5. modified TerraBase under heavy invalidation.

No failed or environment-invalid record is used to approve a regression.

## Baseline completion checklist

- [x] isolated exact-commit worktree
- [x] clean source identity recorded
- [x] exact-source immutable OCI image built and smoke-started
- [x] hardware/runtime/configuration captured
- [x] required realistic-harness probes implemented
- [x] corrected KVM candidate passes locked build, 20 safe launcher checks, and 121 isolated harness checks (`20260726T201733Z`)
- [ ] corrected KVM environment change independently reviewed
- [ ] harness self-test passes in the attested KVM environment
- [ ] two independent valid Standard runs
- [ ] valid Persistent run
- [ ] required operation-extension baseline
- [ ] existing request-latency baseline
- [ ] microbenchmark raw exports
- [ ] calculated noise floor
- [ ] baseline review and approval

Until every unchecked item needed by a touched hot path is complete, the
performance gate remains closed.
