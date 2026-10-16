# Shared goal ledger history

This file keeps the superseded sections of the
[shared-goal acceptance ledger](shared-goal-acceptance-20260926.md). S0 moved
them here verbatim from ts-orchestrator `8ea61a7d` on 2026-10-01 so that no
evidence is lost. Every statement keeps its original date and scope: read
"current", "below" and "above" as of the date in each section, not as of
today. Do not edit or extend this file. Current status is in the index and in
the [gate](gates/) and [pipeline](pipeline/) files.

## Pre-handoff ts-infra record

**Later `ts-infra` ownership update:** The inventory, plan, PR, and cost details
below are from the 2026-09-27 pre-handoff snapshot. `ts-infra` main commit
`e347f13a313ebb2b9d0a0b631ba0aed56af65126` later removed the regional
Terraform definitions and workflow after the state-only handoff. Current
`ts-infra` manages four Email Delivery resources only. Regional networking,
IAM, bootstrap inputs, and controller A are operator-managed; after handoff,
`ts-orchestrator` forms B/C and manages ARM workload hosts and TerraBase. This
source update does not prove regional health or a live controller; see the
[manual regional bootstrap runbook](../region-bootstrap.md)
for the current procedure.

### Historical preliminary cost and inventory evidence (pre-handoff)

These figures and workflow artifacts record the earlier proposed regional
estate. They predate `ts-infra` main commit `e347f13a`, which removed the
regional source and workflow after the state-only handoff. They are retained
for provenance; do not use them as the current regional plan, admission, or
instructions for applying regional infrastructure.

The provisional estimate is **US$89.55/month**, leaving **US$10.45** under
the combined US$100/month testing-plus-preview cap. It covers five preview
instances at 1 OCPU / 6 GB plus the existing Forgejo VM (7 OCPU / 34 GB total),
450 GB block volumes (200 GB free allowance deducted), a 72-hour 1/6 GB
replacement and 100 GB of volumes, 10 GB Object Storage, 1 million extra
requests, 100 GB egress, a provisional 350 GB snapshot reserve, existing
Forgejo Object Storage, and a US$5 miscellaneous reserve. It uses the lower
Always Free documentation values (1,500 A1 OCPU-hours and 9,000 GB-hours); the
2026-09-23 price catalog lists higher values (3,000 and 18,000), while the
tenancy reports `is-free-tier: null`. The lower values still fit the estimate;
the $5 reserve and snapshot price are estimates, not verified line items. A separate full-month
1/6 GB stress host with 100 GB volumes would exceed the remaining margin. The estimate conservatively includes unrelated Forgejo object costs.

The provisional sanitized foundation plan is
[`ts-infra-foundation-plan-20260926.json`](ts-infra-foundation-plan-20260926.json),
SHA-256 `566700706440b8aa2141a9fd221525246aa563b8ec4c865d4ba1a85599cda3fc`;
it contains 24 creates, 0 updates/deletes, and no compute or data resources. Its effects digest is `77b397dd5828b3957668e08d4b1e6631089830a516574736823eb8438dc27518`. The
corrected apply workflow SHA-256 is
`17f6b751c646d0fb8af689bdd64e8dfc47d12536b34a94f24018d23be01b3c6a`; guard
test SHA-256 is
`c61f4ef8154530db30fc2e34524171709d23e580dfcbcbeb41436f19ceb6bb14`; guard
implementation SHA-256 is
`5ff65a58037ad659768592d6073f0c45638dc9bf5329a41d60365e467001f28d`. Earlier local workflow guard checks ran 7 tests and parsed both workflow YAML
files on their then-current source hashes; no retained test log is available. At this pre-handoff snapshot, PR #20 candidate
`c1cb2057fb0968bca2a8ddce3df77725c55e8b2e` was Draft/Pending and isolated-runner
task #55 was running. Its then-fresh informational admission has SHA-256
`c90f3db14e2792dbbd0a89c02f73c25727bcee5a8bfb97a106d79063328a4eee`, estimates
$89.55/month with $10.45 headroom, and expires at `2026-09-27T03:55:39Z`; refresh
inventory/admission before any effect. This plan and inventory are evidence only, not a deployed
preview or current permission to create resources.

This pre-handoff inventory and estimate do not authorize resource creation.
Current `ts-infra` automation is restricted to Email Delivery and cannot create
regional foundation or seed resources. Regional networking, IAM, bootstrap
inputs, and controller A are operator-managed under the
[manual regional bootstrap runbook](../region-bootstrap.md). No live regional
deployment is verified by this historical preflight.

## Historical checkpoint — 2026-09-29 02:54 UTC (superseded observations)

The current root [`GOAL.md`](../../../GOAL.md) is the sole goal authority for
this refresh (SHA-256
`99de61cbd4bd49a678d2d48b5cbc92297d93849746773229a80594ba7533d0a6`). The source identities and acceptance rows below retain their dated historical
scope; this checkpoint supersedes their *progress observations*, not their
receipts or stable IDs. **M0 and
D01–D15 remain unverified: 0/16 (0%).**

**Current cost authority is US$200/month combined for qualification and preview.** At the last R3 owner estimate of $90.27/month under its historical $100 plan, arithmetic headroom against the current ceiling is $109.73. Prior $100-plan admissions and dated $100 receipts retain their historical scope. Above $100 still requires a fresh signed active plan, inventory and admission for the selected fixture; no guest-image rebuild follows solely from the budget change. GRU and the A-only runbook handoff remain unchanged.

**Latest owner receipts.** TerraBase main `d2017ca9668a650ec490dff3f79bd51b75bb6466` passed CI #1012/run 11696: Fast 138 passed, 0 failed, 2 ignored, release and publish; [qualification](/home/mariogk/Projects/TerraScale/.qualification/terrabase-ci1012-d2017ca/qualification.json) SHA-256 `69ef5119a78ec1692d49f12447f66cdeb72ca09d8e42f135c05e779ef0e992e9` binds the retained binaries. Go main `db0231f1f2ee85cda8c087c8f9cb384147a7662d` CI #696/job 25225 failed test fixtures ([log](/tmp/ts-orchestrator-run-696.log) SHA-256 `e9b52655d56aa1aebaf030aadac18eef459fbc0346ab2c5ba17f3fce0a402cfa`); the seven-path test-only correction (patch SHA-256 `da675fa56748faa4179636824c8796a50963443b9889d62ea32e52c5fc7ccc39`) passed independent review, and the repository-wide race command passed locally against this base plus patch ([log](/tmp/ts-orch-ci696-full-race-r2.log) SHA-256 `6d6637ba4a2b53aa0ef5613f42e1588042b7fa2164dcdf0711d651fc28ea8c41`). Corrected main and matching Forgejo CI qualification are pending. R3 A and its boot volume are **TERMINATED**. The R3 attempt-1 intent was signed at 02:12:51.372 UTC and stored at 02:17:45.656 UTC, beyond its 61-second publication window; no HEAD exists, so that attempt cannot be recovered by the current API. Root selected fresh R4 `ts-preview-gru-20260929-r4` with StorageDomain prefix `r4-20260929`; signed R4 artifacts and rebaked image remain pending. The image builder requires the next corrected Go main SHA/tree with matching successful CI; Go37 is historical image evidence and cannot be rebaked from its tag. There are no live controllers or admitted workloads. M0 create-only passed, while both bounded `conmon` placement probes held and cleaned up exactly; no guest ran. D10 Complete implementation remains active. These owner-reported advances leave every formal gate open.

| Stable ID | Current owner and bounded evidence | Next qualifying result |
| --- | --- | --- |
| M0 | The independently accepted pinned Go `350a457588ced97ce47ed0cad58c77926357bde6` / TerraBase `1909dcd36c1f0e09189756d976891127312a2d19` source freeze remains [SHA-256](/tmp/ts-m0-repin-freeze-20260928.json) `fd391769e62ca533970fb3cdba501b05f6a75c1692e155c2d57152f1bff77902`; CI binary, kernel and 2 GiB rootfs provenance are pinned, but its wrapper has not built a fresh host test, packet or guest. `workspace_recovery` measured a read-only six-root cache union of 5,315,399,680 B across 83,648 unique inodes at 23:13 UTC, excluding 4,342 hardlink aliases. At that 23:13 UTC snapshot, 21,514,817,536 B `user.slice` usage needed 9,703,657,472 B reclaimed; even all union pages would leave a 4,388,257,792 B shortfall. A later read-only scan at 23:42 UTC found 0 resident bytes among 44 M0 image/output files totaling 82,597,537,016 logical bytes, with no detected readers. `user.slice` had fallen to 19,129,581,568 B, still 7,318,421,504 B above the 11,811,160,064 B admission threshold. Per-file dirty status remains unavailable; no cache advice or reclaim ran. An isolated M0v3 service-adapter/source candidate stages an 18 GiB child cap with +3 GiB reserve admission and 1 Hz actual reserve-floor monitoring; it has no frozen full receipt or live service/container/VM. V3r7 create-only passed ([cleanup](/tmp/ts-m0-runtime-ecbbe4b971b94a6f/no-guest-cleanup.json) SHA-256 `3e44410f14673ae12f33bbd3ece0f93d1a81addfda3c78e7349be6028c5bfb46`). Placement then held when `conmon` escaped the helper with cgroups enabled ([cleanup](/tmp/ts-m0-runtime-50522b610698404d/no-guest-cleanup.json) SHA-256 `e2a353cf0a760c0018c4f1874509001f7b5ddb25fab7caeafac1509a6a37bdeb`) and again with `--cgroups=no-conmon` ([cleanup](/tmp/ts-m0-runtime-31a56979cc124bf6/no-guest-cleanup.json) SHA-256 `1a292a262e97490ece18ec1e90c3649be71438488d4e74c6ea6e9e4f6e80de19`). Both cleanup receipts report no retained container, volume, service cgroup or guest; no joined write/read receipt exists. | Finish read-only Podman 5.8.7 diagnosis and independent review, then one bounded no-guest placement retry. Full M0 guest work remains held pending placement and safe admission. |
| D06 | The accepted [M1 fresh-fixture decision](/tmp/ts-m1-d06-fresh-fixture-decision-20260928.md) SHA-256 `15c94cb7b89c489f9267f53b8bd6ebc23e54546eb272055e48c1ce36f9253dee` chooses a newly qualified GRU fixture after Go `37cec40938bd9cac8e34168dde222c7739ccf125` R3/NATS diagnostic feedback: bootstrap A through the runbook, hand off B/C and two hosts to the orchestrator, then deploy first and distinct second TerraBase artifacts through signed desired state **within that same fixture**. D06 must prove data/member/volume continuity, failed-candidate health rejection and qualified rollback or forward recovery there. The old Go350 [management-binary bridge decision](/tmp/ts-go350-d06-management-upgrade-decision-20260928.md) SHA-256 `996b1b96167c87bea9b5875cb0be2222d02a2c62ce81b981c57b4fc33b733399` is a separate unimplemented self-update path, not an M1/D06 prerequisite; broader repeatable host-update remains open. The frozen D06 [source review](/tmp/ts-d06-managed-rollout-source-review-20260928.md) SHA-256 `0be87a0114ff7ac64c045078117e58337c789c6b6bf1711f39296aa8202771ff` is **HOLD**: committed R3 Held may fail seat CAS and never repair after restart; missing/stale/timed-out canary proof lacks a durable Held outcome. A superseding D06 correction [patch](/tmp/ts-d06-managed-rollout-correction-superseding-20260928.patch) SHA-256 `a47b9992409154b7334fd985364848d90a32c4c1c42d4e06a2109219c511706d` addresses both Held cases and passed independent narrow source review; the old HOLD remains historical. The combined D06+D10 candidate still needs trusted app/R3 regression, final integrated review and real rollout. R3 is terminated and fresh R4 is selected but not yet qualified. Diagnostic r2/r3 receipts, resource-owner cleanup and cost overlap remain distinct; no continuity across fixture replacement is claimed. | Complete trusted D06+D10 app/R3 tests, final integrated review and backup exclusion, then qualify a fresh ARM fixture, then run two signed TerraBase artifacts with data/identity continuity and failure/recovery evidence. |
| D09 | Corrected bounded document-core/HTTPS write fence remains on TerraBase main `817c63ca228f42fd4eaa593ef159de48fe5f553e`, CI #1006/run 11651 Fast 120 passed/2 ignored plus release/publish. The accepted [D09 HTTP subscription integration brief](/tmp/ts-d09-http-subscription-integration-brief-20260928.md) SHA-256 `dbf1e6a66264f2bfc06a4cb969ea304c97da47c3a17f69dd3a30c37e82a67a28` fixes the intended cursor/public error/whole-group contract and real caller checks; a D09-only ten-file HTTP candidate is frozen as [patch](/tmp/d09-http-subscription-source-20260928.patch) SHA-256 `eeb197eb48e7a968f24b3a56e28c70f41864e070861a629472a4b9982b888fa9` and [manifest](/tmp/d09-http-subscription-source-20260928.sha256) SHA-256 `d42d79d7e6ff8c9027d2b5307c31a1b78f5460f18a0ebbd33ec3de52833775c6`. Independent review accepted its production source and Scalar pagination correction; an isolated D09-on-9cf 12-file candidate ([patch](/tmp/d09-on-9cf-integration-20260928.patch) SHA-256 `08e146f335c9c735634d3380e84b2b5c0a08acdd360baf73b0909b5864e5ba37`; [manifest](/tmp/d09-on-9cf-integration-20260928.sha256) SHA-256 `8381285c1aa481dbb9380c2246498f0d6c83b8ae4814b1cbbaeb8ccce21e156e`) includes four bounded D08/D10 overlap resolutions. The owner reports final local Fast **136 passed/0 failed/2 ignored plus S3 host pass** with pinned `psql`; Clippy passed before its final test-only correction. Independent source review accepted all 12 file hashes; the local Scalar fixture subsequently passed per owner. The source-reviewed candidate is now integrated in TerraBase main `619df86d044d3ec2a3d020333556eaa46516beca` with a two-file CI readiness/CPU correction; composed signed-backup focused tests 6/6, standard Clippy and formatting passed. CI #1011 Fast failed 134/3/2 and publish was skipped; later TerraBase main `d2017ca9668a650ec490dff3f79bd51b75bb6466` passed CI #1012 Fast 138/0/2, release and publish (qualification SHA-256 `69ef5119a78ec1692d49f12447f66cdeb72ca09d8e42f135c05e779ef0e992e9`). The independent two-member cursor test remains a follow-on candidate; no packaged-process D10 hold composition or deployed two-member receipt exists. | Run real scoped snapshot/tail/resume, retention reset, slow-consumer and revoked-key cases through HTTPS on the deployed pair. |
| D10 | The independently accepted Go operation v3 [23-file patch](/tmp/ts-orch-d10-backup-operation-v3-20260928.patch) SHA-256 `e42c80b86907a40d319028eb5e8222342bf23cb0a31ecd6c33661e5f300eb3b8` has focused host tests and [review receipt](/tmp/ts-orch-d10-operation-independent-review-v3-20260928.md) SHA-256 `15d271e1978e7f7e5eadc039e9ae142ed7f4cad09d75a15cd600d0b32a505cda`; full Agent, process runner, mounted-volume and Rust held-restart guest remain open. Rust final [30-file manifest](/tmp/ts-d10-final-v3-30-file-manifest-20260928.json) SHA-256 `445071d271f58f968faa39fdafd2a532339d7976ce08d3a3d98c01e7d69538a4` and [evidence](/tmp/ts-d10-rust-v3-evidence-20260928.md) SHA-256 `16652f6bb5113c71434f2a85daf9591908bd5c5f9663607f16fefccff4e6f035` bind strict Clippy/build, signed process 3/3 serial and 3/3 parallel, closure 1/1 and separate owner/peer UIDs with peer credential read denial; independent source review accepted. These local slices do not prove Complete/publication, full Go Agent path, SQL/catalog equivalence, clean restore or PITR; native source frontier still qualifies only two roots/one remote inbox, not >2. The combined 646+D08+D10 40-file overlay patch SHA-256 `5b3c4a24c78beae4dac3d47fde3c17bcdbd9a14db5a2203d89b8a3b409a28360` received independent **source ACCEPT** ([review](/tmp/ts-d10-on-d08-d11-independent-source-review-20260928.md) SHA-256 `63960a2be30d28d4b9601c8780dcd7239c310dacccfcf6ea853affe61071bb88`). A final 43-file TerraBase integration [patch](/tmp/ts-d10-on-d08-d11-integration-final-20260928.patch) SHA-256 `1a599a8c1337885fdae9b0d9c2f3aaf900e5936975fe61f4018f18b735fdaa98` independently passed source review, local full Fast, locked Clippy and Scalar on main `9cf90fb58e4eaec1a4a381b4217d99f199bd6dec`; CI #1008 release passed but Fast failed 111/25/2 and publish was skipped; cause remains under diagnosis. TerraBase main `619df86d044d3ec2a3d020333556eaa46516beca` carries the reviewed D10 source plus D09/CI correction; composed focused signed-backup tests passed 6/6, while CI #1011 Fast later failed 134/3/2 and publish was skipped. The Go bridge predates the mandatory-verifier caller change, and no full Agent/Complete/restore runtime pass exists. The accepted [owner-only Complete proof decision](/tmp/ts-alpha-d10-complete-owner-proof-decision-20260928.md) SHA-256 `c23c5ec8c88be7f2b8157b2662a3a28acf0cec1936515937e093eced3a02cae0` requires owner catalog CAS/readback plus a leaf-signed publication receipt, with peer source-cut verification. The final [Complete implementation brief](/tmp/ts-alpha-d10-complete-publication-implementation-brief-20260928.md) SHA-256 `212f9e6d8bfc0fca9c30b2b7904dcf7de0081fe3121e5db0207d6d849e88a14d` and [decision note](/tmp/ts-alpha-d10-complete-publication-decisions-20260928.md) SHA-256 `7a52325a594a6dee3ac856edf9d7315fc216a3d13eddbf3f0e6914d2fd024ba7` passed independent source review. Replay requires a fully durable journal-linked candidate data file and signed envelope; otherwise recovery reports `capture_uncertain`, does not recapture, and uses a pre-publishing fenced all-member Abort. Implementation, publication wire, real caller, restore and PITR remain unproved. | Review/build integrated producer and consumer, run real packaged host/Agent backup and durable Complete/catalog with restart/partial-roster replay; then clean restore, post-restore write and PITR. |
| D14 | Scalar/OpenAPI source checks exist. The private [first-1909 browser runner](/tmp/ts-first1909-client-runner-20260928/README.md) SHA-256 `690d47cd368609964f5c115b12b445a61231837264eaed3ee106186f7f31052f` uses a Bastion forward and temporary browser/Node CA and hostname scope. Its local Chromium/Playwright fixture reached the correct hostname and rejected unknown CA and wrong host; independent review accepted the prepared runner. TerraBase 9cf local Scalar query fixture passed `[401,200]` (log SHA-256 `fe9f84b3901ef37d3e9b196b6ce8ad11b705ee0f86563994786c453b7080a459`). No deployed member listener, signed customer material, TLS-valid browser origin or live Scalar route result exists. | After managed pair and signed CA/client scope, admit exact runner script hashes and execute deployed `/docs`, `/openapi.json` and direct browser API examples with success/error responses and route/spec coverage. |
| D15 | The older same-guest harness finding is superseded by `ts-orchestrator` commit `1758532e`: `qualify.py`, `pressure.py`, `alpha_adapter.py`, `alpha_runner.py`, README, and `test_pressure.py` now distinguish dedicated controller and workload hosts. Existing tests cover role routing, distinct controller pin, controller probe without a host unit, and role-bound samples. The read-only [r2 ARM readiness packet](/tmp/ts-alpha-d15-r2-arm-runtime-readiness-20260928.md) SHA-256 `61bd2bb10c610ab7480c64cb6cc91e552ebb91ba2b6ac9c2c134f83ae661ba17` maps Go350/image #690 to configured management normal priority, weights, memory floors and role caps plus the exact after-handoff probe and bounded pressure sequence. The qualified Go37 r3 image remains historical and AVAILABLE, while R3 A and boot are TERMINATED. R4 image rebake is pending. The packet contains source policy, not effective guest settings; A/B/C and hosts have no runtime or pressure evidence yet. A truthful management hold is permitted, but it cannot turn a failed serving-path check into PASS. | Reuse the source-pinned role-aware probe on each exact qualified fresh-fixture controller/host guest after handoff, then run bounded CPU/memory/I/O, OOM and restart scenarios with before/during/after cgroup and data-path evidence. |

### Full remaining scope mapped to the existing IDs

This is the open-work map from root `GOAL.md:119-205,210-249,271-337`,
not another gate count. Every group below remains **OPEN**; source, offline,
or CI preparation above does not verify the real caller and required
environment. Existing detailed rows and TerraBase child IDs carry the
individual executable checks and evidence references.

| Milestone and existing IDs | Remaining acceptance scope (all open) |
| --- | --- |
| **M0 — M0-01–M0-06** | Pin the Go/Rust/Turso source pair, effective Turso patch, lockfiles, runtime config, contract and artifact digests. Through the real host caller prove placement/tenant/database/shard/member/incarnation/authority identity; volume and mount identity, args and credential provisioning/reload; selected ACK profile, catch-up, admission and exact serving predicate; signed host observations versus native serving proof, rejecting stale reports; and safe stop/update with admitted and uncertain write outcomes. A clean checkout must build that pair and run automated `Controller.ApplyDesired` → `Agent.Run` → `processRunner` → authenticated Rust document write/read. |
| **M2 — D02–D03, D07-SQL-01–10, D08–D09, D14** | Complete supported document CRUD/upsert/transactions with invalid, unauthorized, retry, uncertain, restart and replica cases (**D02–D03**); indexed filters, projection, order and pagination, database/collection/schema/relationship provisioning, integrity and delete policy, including index lifecycle (**D08**). Real scoped `psql` must prove TLS, grants, isolated sessions, supported reads/DML/commit/rollback, atomic capture, replicated application and rejection of unsupported SQL before effects (**D07-SQL-01–10**). Reactive clients must prove snapshot/tail/resume, retention resync, bounded consumers and revocation (**D09**). Exercise administrative/lifecycle interfaces and consistent request/response shapes, auth, rotation/revocation and tenant isolation across the supported APIs (**D03, D07–D09**). Keep complete executable Scalar examples, direct browser requests and route/spec CI current for every exposed HTTP method/path (**D14**). |
| **Across M0–M3 — M0-01/M0-06, D01, D06, D10–D15** | Keep one repository-held runnable HTTPS client walkthrough that provisions, checks and removes its data; repeatable setup/build/deploy/smoke/diagnose/cleanup commands; truthful inspectable asynchronous operation IDs, states and retries. Promote immutable tested bytes through verified release admission, canary and health checks, with complete cache keys, safe CI concurrency/cancellation, first-class ARM artifacts and exact artifact-bound milestone receipts. Maintain this stable-ID checklist with owner, producer/consumer, supported config, expected result, executable check and evidence; record current inventory, recurring cost and cleanup. Performance tuning, model advice, and regional Raft remain explicit deferrals, not erased requirements. |

The eventual evidence owner should extend **this ledger's existing IDs** with
the root goal's owner, producer/consumer, supported configuration, expected
result, executable check and evidence reference. The
[TerraBase evidence ledger](../../../terrabase/docs/evidence-ledger.md)
already holds TerraBase requirement IDs; link its applicable entries instead
of creating a second checklist. The joined A-handoff/first-smoke receipt,
repository-held runnable HTTPS walkthrough, D14 browser operator, and D15 live
pressure operator still need explicit ownership after the signed A handoff.
The prepared smoke client remains under `/tmp` and is not that repository
walkthrough. Later section details are dated source evidence; none advances a
formal gate from this checkpoint.

## Source identity

The workspace root has no Git revision (`git rev-parse` fails because it is
not a repository). The source snapshot used for this ledger is:

| Source | Revision or SHA-256 | Worktree |
| --- | --- | --- |
| Workspace [`GOAL.md`](../../../GOAL.md) | `c9933171fba8c997a91ed48e4fae62f6d9f8932ee7d3b62aa6abd8c0c820291b` | Frozen by doc owner for this evidence snapshot |
| Root [`AGENTS.md`](../../../AGENTS.md) | `6d0e45ba183117ef522ab321831b28971d5b1a45575cab45314acdef2909653a` | Human-owned; unchanged |
| `ts-orchestrator` | HEAD `c845e6ca2c04f5cd435c9c3039d731f8a453ebfa` | Dirty |
| `terrabase` | HEAD `7930f774552034cbb5d5ad1cae2d1bd28d254ccd` | Dirty |
| `terrabase/crates/turso` | submodule `64b8ef5742fc18937f9c89806c81e3f6475dc7a3` | Dirty patch/worktree |
| M1 Go verification | commit `429edc2d51380f333aa6521bfd7d6b1fa23af574`, tree `38ce47f2c8e5f1def7f5c54339c23d6b53b019d9` | inventory SHA-256 `492696dd6d97236fb8954104b3f72e28b5a9dcf8b7eb1a4514af562dd3705285`; `make verify` result and log hashes are recorded in the M1 evidence refresh |
| Final Go candidate with authorized deletions | `.qualification/final-go-candidate/source-checkpoint-098a0df/checkpoint.json` SHA-256 `889ae53f4aaf872b2d51bb7b5bbd2769909cab119f7386f796b9a3d260bc95bb`; commit `098a0dfa38771c752f545ac3d2f09662da4c76a7`, tree `bbfab724a19b5f0d1753971d17e482694acb8190` | Inventory SHA-256 `29cf7e61d0d0370c8c4dd59dd489bdfe7580feea8f9a9e978f012ea26e83bcec`; exact authorized-deletion manifest SHA-256 `43af9b8fef1d2bca87d1a29e46860268fe2dfa2bf567a500b9ea48d1389b23cb`; all 396 paths absent; build/tests pending |
| M3 security UUID source | `.qualification/m3-material-security/source-checkpoint-fc3354a/checkpoint.json` SHA-256 `dc7e586a27a83ef77d081c3bf2f0a2ae0a5334cca813d7fb93d35704d48426be`; commit `fc3354a883613e0f9ba1a8ddcbe7b67a116a4378`, tree `a825fdd47e9c0bfa2b753c5e7e322d7bda044229` | Inventory SHA-256 `1e3d8a44daf588a62af573ae0209e28d2911da8c0c3610349861ea332becb968`; selective UUID compile fix; compile/tests and reviewed-boundary follow-up pending |

The gate-specific rows of this table moved to their gate and pipeline files:
M0 candidate, lock, cgroup-attempt and diagnostic-packet rows to
[M0](gates/m0.md); material provenance correction B and the M1 Go
diagnostic-test pin to [D03](gates/d03.md); the M1 corrected TerraBase source
inventory to [D04](gates/d04.md); crash-test source history, the M1 Rust
process-test pin and the Clippy PR #144 correction to [D05](gates/d05.md);
the D07, D08, D09, D10, D11 and D14 rows to their gate files; and the builder
PR #11 and published builder rows to [P4](pipeline/p4.md).

Sanitized foundation plan
[`ts-infra-foundation-plan-20260926.json`](ts-infra-foundation-plan-20260926.json)
has SHA-256 `566700706440b8aa2141a9fd221525246aa563b8ec4c865d4ba1a85599cda3fc`;
it is provisional review evidence, not an apply receipt.

The D15 input hashes that followed here moved to [D15](gates/d15.md).

These selected hashes identify individual working-tree files from the earlier
source snapshot; they are not a substitute for the locked M0 pair above. The `ts-builder` runner image has since been published separately; see the M0 evidence refresh below. The lock-bound TerraBase
runtime evidence is SHA-256
`0fdd980f51e18a593c345a778f37b840ce2a3e7466d7890aba7736b34f445b65`. An
appended copy is preserved separately at
`.qualification/shared-m0/evidence/runtime-evidence-d9d11e1-appended-20260926.txt`
(SHA-256 `fe355dc6d076ad671d2f34d434768cdf3d40b6baa3cdce93a0450b77cbcc9d53`);
the repair record is
`.qualification/shared-m0/evidence/runtime-evidence-d9d11e1-repair-20260926.txt`
(SHA-256 `791d7581d461bf945ed84a2ff49e509123623d9a73eb06b5dbf76d5f9d649ef4`). The build operator confirmed the appended content was source-inventory
confirmation, restored the original lock-bound bytes, and left the candidate
lock and running packet unchanged. Current M1 corrected source at `a30a6c6`
has no fresh compile or runtime receipt; the earlier `9d80e7f` compile check
is pre-correction. Any later source or configuration change invalidates only
evidence bound to those changed inputs; refresh those identities before use. During preparation the operational docs changed to add the $100 cap, D15, the
five-instance R3 ARM topology, and the fixed 16-gate reporting denominator;
the root Goal and qualification status were rehashed after those edits. Historical cleanup was confirmed intentional. No historical files were
restored. No build, test, deployment, or external mutation was run as part of
this ledger refresh; independent gate results are recorded under M0-02 and
D15.

## Status rules and milestone snapshot

The status rules and the 16-gate denominator from this section are in the
[index](shared-goal-acceptance-20260926.md). The dated milestone snapshot and
critical path were:

| Milestone | Status | Current gate |
| --- | --- | --- |
| M2 — complete supported APIs | **IN PROGRESS** | Source checkpoints are frozen for D07 V2 SQL (`d1d3be9`), D08 indexed query/schema/relationship work plus restart correction (`e16db2e`), and D09 reactive delivery/reset-cursor correction (`fd4154b`). D07/D09 Cargo and process runs remain pending; D08 retains startup-cost risk and has no Cargo/Fast run. No M2 top-level gate is verified. |

The single ordered critical path is: freeze candidate and signed fixture;
verify release admission and retained artifacts; settle and implement the
selected two-member S3 acknowledgment/serving contract; qualify the ARM host
image and exact R3 five-instance cost/inventory; then run D01–D06, D14, and D15
on those artifacts. M2/M3 work remains recorded below and must not silently
become an M1 prerequisite.

## M1 Go verification refresh

**M1 Go verification refresh (2026-09-27).** On source `429edc2d51380f333aa6521bfd7d6b1fa23af574` / tree `38ce47f2c8e5f1def7f5c54339c23d6b53b019d9` (inventory SHA-256 `492696dd6d97236fb8954104b3f72e28b5a9dcf8b7eb1a4514af562dd3705285`), `make verify` passed ordinary Go tests, vet, race checks, and three Firecracker-related Python suites. `.qualification/m1-go-checkpoint-429edc2/verification-result.txt` SHA-256 is `03e9612bc10ee93ca89a0fd750adb2b8aec31262d78d812a355ff7414a0240dc`; `.qualification/m1-go-checkpoint-429edc2/verify-capped-4g.log` SHA-256 is `018a9ba6637df12b01cda3474d106d13cbe4974d75d43909592a6ac1d2bde438`. Two sudo-dependent checks were skipped.

## M2 — supported API backlog

TerraBase is the workspace GOAL's database producer. The canonical detailed
database requirement/decision tracking remains
[`terrabase/docs/evidence-ledger.md`](../../../terrabase/docs/evidence-ledger.md);
this shared ledger maps product acceptance to real callers. API names below are
stable ledger IDs; their source and verification state is recorded in each row.

The D07, D08 and D09 rows of this section moved to [D07](gates/d07.md),
[D08](gates/d08.md) and [D09](gates/d09.md).

## Verification commands and evidence policy

No build, test, Git, Forgejo, deployment, or external action was run for this
ledger refresh. Its local Markdown link and table-shape check passed with seven
local link targets and no missing targets; `sha256sum` verified the recorded
source and evidence identities. Known repository entrypoints for the later
candidate are:

```bash
cd ts-orchestrator && make test
cd terrabase && make fmt-check
cd terrabase && make test-fast
cd terrabase && make test-slow
```

TerraBase keeps exactly Fast and Slow integration suites; Fast is release
critical and Slow remains independent. Use `fj` for Forgejo status/logs as
required by the repository. No reproducible M1 deploy command has yet been identified. The
M1 browser check must use the live preview, and resource-pressure evidence must
name the exact ARM image, service/cgroup settings, load profile, outcomes and
recovery receipts. Retain raw reports by immutable candidate digest; refresh
file hashes and relevant ledger rows whenever the shared worktree changes.

