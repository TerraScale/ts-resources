# TerraBase benchmark

TerraBase.Benchmark runs repeatable workloads against TerraBase and comparison
products. Each history record contains a redacted benchmark receipt. A receipt
answers what ran, which exact source and image were measured, whether workload
correctness and durability checks passed, and whether the evidence is valid
for a performance claim.

The harness never authorizes deployment, promotes an image, or makes a delivery
decision. `compare` reports statistical differences as a regression report.
Regression output names the affected workload and a next action. It does not
block a separate direct deployment command.

## Run the checks

The local receipt check is deterministic and does not start a database or write
canonical history:

```text
dotnet run -- receipt-self-test
```

The launcher safety check is also local and does not write benchmark history:

```text
dotnet tools/BenchmarkVm.cs --self-test
```

The launcher always creates the same VM shape: 8 single-threaded vCPUs and 8
GiB of guest RAM. This is a hard limit shared by every profile, and cannot be
changed through settings or CLI arguments.

Run history-producing commands through the launcher. The launcher provides the
isolated VM, fixed CPU and storage allocation, host attestation, and cleanup
boundary. Do not run timing workloads on the development host.

```text
dotnet tools/BenchmarkVm.cs provision

dotnet tools/BenchmarkVm.cs run \
  --oci-archive .artifacts/benchmark-vm/images/terrabase-exact-source.docker.tar \
  -- benchmark --profile smoke --products terrabase,ravendb,postgresql

dotnet tools/BenchmarkVm.cs run \
  --oci-archive .artifacts/benchmark-vm/images/terrabase-exact-source.docker.tar \
  -- compare --profile standard --subject terrabase --reference ravendb

dotnet tools/BenchmarkVm.cs cleanup --run-id <run-id>
```

The `--subject` and `--reference` names describe a statistical comparison.

## Receipts and regression reports

The receipt schema is `terrascale.benchmark-receipt/v1`. It contains the run
ID, harness commit, TerraBase source identity, product identities, workload
inputs, retained sample rows, correctness and durability facts, and a digest
of the evidence snapshot. Source commits are full 40-character Git commits and
container identities are immutable `sha256:` references.

The regression schema is `terrascale.benchmark-regression/v1`. It records paired
statistics, confidence intervals, metrics whose measured verdict is
`regressed`, and remediation text. A regression is evidence, not an outage or
deployment denial. Incomplete, failed, or invalid runs retain diagnostics in
history but are excluded from performance claims and comparisons.

History output is redacted before persistence. Private source paths, host paths,
credentials, tokens, connection strings, and workload secrets must not appear
in receipts, logs, or committed artifacts. `sanitize-history --check` reports
artifacts that need redaction.

## Profiles

`smoke` is a short directional run. `standard` exercises the full fixed
workload matrix. `persistent` uses the configured 128 GiB ext4 data image and
checks durable acknowledgements. `soak` runs the mixed workload for a sustained
period. Strict evidence checks are selected by the profile's
`strictEvidence` setting. They protect measurement quality.

## Workload and safety rules

The runner keeps the workload correctness, durability, response validation,
paired statistical comparison, exact source identity, host attestation, and
evidence-integrity checks. A failed check changes the receipt status to
`invalid` or `failed` and records a reason. It never turns an invalid result
into a claim.

Use the tracked settings file and the exact TerraBase source commit selected by
that file. Do not build, restore packages, pull images, or use a second storage
device during a measured VM run. Reuse the configured ext4 host volume and run
`cleanup` when a disposable run is finished.

## Container image

`images/Containerfile.runtime` is the TerraBase runtime image
recipe. It runs the server as the unprivileged `terrabase` user, keeps
settings writable only by that user, and copies a prebuilt exact-source payload.
It does not restore packages or fetch dependencies during image construction.
