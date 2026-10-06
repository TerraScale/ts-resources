# Qualify public alpha benchmark evidence

## Coordination record

- Owner: TerraBase benchmark baseline and release evidence, Forgejo issues #1
  and #2.
- Kind: source and validation.
- Scope: the stable .NET 10 benchmark project, launch-evidence schema, schema
  validator, variance and regression gates, CI self-test, tracked settings,
  candidate container recipe, and retained-result receipt.
- Baseline: `9dc54178150831b9609a2cd1d0e66d6ed012b227`, which added the initial
  launch-evidence validator while the project still targeted a .NET 11
  preview SDK.
- Dependencies: TerraBase source identity, an approved immutable container
  digest, the exclusive benchmark VM lane, and a separately retained raw
  measurement record.
- Evidence: locked restore, Release build, and
  `dotnet run -c Release --no-build -- validate-launch-evidence --self-test`
  pass locally. The self-test covers all required workloads and phases, the
  4 KiB document-size bands, exact measurement matrices, distinct raw-record
  digests recomputed from retained content, all latency-percentile variance,
  claim and threshold traceability, qualified-baseline coordinates and value
  binding, network-distance exclusion, no-performance-promise wording, a
  deliberate regression, and the tracked settings schema. The Release build
  completed with zero warnings and errors.
- Handoff: this checkout cannot produce a decision-grade baseline without the
  approved VM lane and an exact reviewed TerraBase image. No performance claim
  is made from the local schema fixture. The committed settings omit the
  retired preview candidate. An independent adversarial review is required
  before these major harness and schema changes may be pushed.

## Stable toolchain contract

The benchmark validator and harness target `net10.0`, pin SDK `10.0.302`, and
expect runtime patch `10.0.10`. Preview SDKs and `runtime-async` are not part of
the current production contract. Historical preview records remain available
for audit but cannot qualify as a current baseline.
