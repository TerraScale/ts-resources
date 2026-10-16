# Production-readiness checkpoint — 2026-09-26

**Status: NOT PRODUCTION READY.** This note records the accepted orchestrator
checkpoint `d5fc307f31ae825a664d99897a80a2219c058c3f`. It covers the Go
single-binary target, embedded regional NATS, managed placement, and the
founder bootstrap slice. It does not describe later shared-tree edits. The [production-readiness plan](production-readiness-plan.md)
contains the bounded canary inventory, conditional price arithmetic, cleanup
boundary, and remaining gates.

| Area | Verified at the stated scope | Still open |
| --- | --- | --- |
| Go verification | The Go 1.27.1 check recorded `go test -count=1 ./...` and `go vet ./...` passing for its frozen pre-founder snapshot. | The check predates the founder changes through `d5fc307`; it is not a full-suite or build qualification of this checkpoint. The nested `third_party/nats-server` module and ARM64 execution were not covered. |
| Embedded regional NATS | NATS server runs embedded in the Go process. The committed controller test covers three local controllers and controller loss. | That test supplies explicit routes; it does not demonstrate automatic region discovery, founder formation, or safe admission of new regional peers. |
| TerraBase lifecycle | Reconciliation can prepare a host and retained volume, then verify attachment. | Placement holds at `awaiting-runtime-contract`; guest mount identity, TerraBase launch, serving/catch-up evidence, durable drain, safe scale-in, and autoscaling remain open. |

The broad test result belongs to the predecessor
`4c284550310f5629976251d157047bc0282eb7be`, not this commit. The check used
archive base `93ca72c6dc0dac248ad7728fe36ca03513ca9877` plus 13 hash-verified
overlay files. Those are all tracked paths changed from `93ca72c6` through
`4c284550`, and the overlay manifest matched those files at `4c284550`; the
resulting tested source therefore corresponds to that predecessor checkpoint.
It records 21 root-module packages, verifies 1,194 snapshot file hashes, and
excludes untracked files and the nested NATS module. It does not cover commits
`0cc6ed`, `6eaf230`, or `d5fc307`.

Founder checks are narrower and separately recorded. The founder-core check
ran focused bootstrap package tests and vet from the `4c284550` source
baseline; that plan/ledger slice was later committed in
`0cc6ed525ac523060e6a813033f7e609224bd795`. The founder-selection check ran
package tests, a focused race run, and vet for the reader/floor files committed
in `6eaf230e1b78de393910c1196e4df9df6cd75a1a`.

The inspected `ts-infra` checkpoint is
`32bd267c0f64e74634667c113e13880c1147fd14`. Four
E4 VMs at 1 OCPU/6 GB calculate to `$0.136/hour`, or `$0.272` for two hours. The five-volume `$10.625/month` example assumes balanced 10 VPU/GB; the
current create/read-back path neither selects nor confirms that tier. These
are conditional list-price calculations, not a tenancy quote or approved
budget. No approved dollar ceiling is recorded.

Source identity for this checkpoint:

| File or evidence | Immutable source identity |
| --- | --- |
| Repository commit / tree (Git object IDs) | `d5fc307f31ae825a664d99897a80a2219c058c3f` / `647ffbcf601942d5bf4b15e558f1b457332f7168` |
| `internal/bootstrapstart/founder_selection.go` | `1ff2e1ed67179b8808a1fe055ac447bbc186bc3291ad3b1d4fd7dd4d3c81e55b` |
| `internal/bootstrapstart/founder_selection_floor.go` | `4371d5e5cfcef76343d3efb6198e6f55e4c17837705209a5b1f28cd072b0e864` |
| `internal/bootstrapstart/founder_oci.go` | `7db45af47da4744e0a5d7a7117a0fc4b5f54ab71eaaa20f4d485b30635f2c07a` |
| `internal/app/controller.go` | `714a17ba26c084373691bf70cd305e8ccae5c363b64090c0500bf56a78772ec4` |
| `internal/placement/controller.go` | `cdb73d7882a41686957a26c1aae5465796175a84e8920a1d42c5795b005e0434` |
| `ts-infra` revision (Git commit ID) | `32bd267c0f64e74634667c113e13880c1147fd14` |
| `ts-infra/infra.tfvars` | `f4f95c31a1e0b7c492e87666a6f338cfa49e8f67cac5e0af28c27b229064a315` |
| `ts-infra/variables.tf` | `904ed82cee92cb2309e2f0a7acfc2dca864b52121ad3f988978dc0c4ddeadfdb` |
| `ts-infra/orchestrator-bootstrap.tf` | `5500a3534c48cd22f9f0f89651bef7cfcf3daf0842edf6e7f3341d2069e61477` |
