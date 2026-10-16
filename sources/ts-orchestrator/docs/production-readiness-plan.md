# Production readiness plan

## Current workspace delivery scope

The [workspace GOAL](../../GOAL.md) is the current delivery authority and
supersedes earlier plan-only and AMD-only restrictions in this dated plan.
Current Go orchestration work belongs to `ts-orchestrator`; TerraBase is the
database service. The former `ts-deploy`-era guidance is historical. See the
[current orchestrator overview](../README.md).

The current regional bootstrap flow is the operator-run
[manual regional bootstrap](region-bootstrap.md): the operator provisions the
foundation and starts only controller A for one mapped cell; admitted A
provisions controller B/C, and `ts-orchestrator` owns managed workload hosts
and volumes after the cell-specific host-enrollment bundle is available. `ts-infra` manages shared Email Delivery only (four resource identities);
regional networking, IAM, and bootstrap inputs remain operator-prepared. The
OpenTofu seed candidate described later in this dated plan is historical and
is superseded for current operation by the runbook. The checked-in regional plan is populated for GRU. The host-enrollment public
bundle renderer accepts matching reviewed material for all three mappings;
the mapped CLI support and its tests are not evidence of a live deployment in
any cell.

Prioritize correct APIs and end-to-end integration, then an early deployed
preview before full product completion. Use the existing leaderless profile
for the first milestone; regional Raft remains a separate proposal. Combined recurring costs for
qualification testing and preview are capped at **US$200/month**, including
every required compute, storage, networking, object-storage, and retained
resource. Record the itemized estimate and resource inventory before creating
resources.

The selected preview topology is one regional R3 cell with three A1
controllers and two separate orchestrator-managed A1 TerraBase hosts. Its
control-plane claim is controller restart and recovery, not uninterrupted
management through controller loss. Confirm the combined cost estimate and
capacity before creating resources.

Benchmarks, comparative performance targets, performance tuning, and optional
model-assisted index advice are deferred until functional completion.
Correctness, authorization, durability, resource limits, and ordinary index
behavior remain in scope.

Protect the Go controller and embedded NATS management path with reserved CPU
and memory, workload CPU and memory caps, I/O weights, and OOM handling. The
orchestrator must use the highest normal scheduling priority supported by its
pinned host, without real-time scheduling guarantees. Verify pressure and
restart/recovery behavior against effective systemd/cgroup settings; host or
kernel failure remains a separate recovery case.

This authorization does not show that a preview has been deployed or that an
API scenario has passed. This production-readiness plan remains a dated audit, not deployment evidence.

## Objective and current decision

A placement is
serving only after the exact member identity, durable storage, local process,
and replication state have been independently verified.

**Status: NOT PRODUCTION READY.** This plan does not approve production use.
The bounded preview authorization in the workspace GOAL supersedes the former
plan-only restriction recorded below; it does not establish that preview
resources or a deployed artifact exist. At the `d5fc307` checkpoint, the Go
placement path could create a region-bound host and retained volume, then held
at `awaiting-runtime-contract`; later commits publish TerraBase desired state
and hold at `awaiting-healthy` without a serving claim. No production
acceptance gate below is closed.

This plan records a source and runtime audit, not an approval to deploy.

## Baseline and evidence boundaries

The accepted source checkpoint for this readiness pass is commit
`d5fc307f31ae825a664d99897a80a2219c058c3f` (tree
`647ffbcf601942d5bf4b15e558f1b457332f7168`). Later shared-tree changes are outside this checkpoint and are not covered by
the findings below. `AGENTS.md` is human-owned and is not an
implementation target.

Qualification results are revision- and scope-specific. The broad Go
suite/vet check recorded Go 1.27.1, `go test -count=1 ./...`, and `go vet ./...`
passing on its frozen pre-founder snapshot: archive base `93ca72c6` plus 13
overlays whose hashes match every tracked path changed through the preceding
`4c284550` enrollment checkpoint. It excludes untracked files and the nested
`third_party/nats-server` module, and does not cover the later founder commits.

Its launch request supplies the configured image,
shape, subnet, network security groups, and a host-node metadata field; it
does not install the binary, provide cloud-init, or distribute host identity
material. Managed placement explicitly stops before TerraBase serving. Host
configuration requires local key material, a pinned controller public key,
NATS settings, install root, and state root, but the repository has no
production host first-boot or enrollment delivery path. A separate controller
bootstrap admission path is present but unreviewed and unqualified in guests. The host runner writes
under the cgroup-v2 root and needs a qualified privilege and lifecycle
contract.

The Firecracker harness writes systemd units into temporary test guests. It
does not provide production image or unit assets. The active release workflow
builds static amd64 and arm64 binaries and prints checksums in job logs; it
does not retain, sign, or publish release assets. Controller JetStream data is
written under configured `store_dir`; no active durable-volume, backup,
restore, or quorum-recovery procedure is supplied.

The latest completed four-VM attempt is R6 at
`/tmp/ts4vm-20260925-r6/summary.json`: it passed initial guest execution and
host restart recovery, then failed the same-process renewal check after a
controller loss. It is partial recovery evidence, not uninterrupted
availability. The local R7 attempt exercising the production JWT/NTP path
failed before VM boot, so a guest rerun is pending; the recorded
arm64 artifact was cross-compiled and ELF-checked, not executed.

No existing
regional foundation can be assumed during rollout. The zero counts are a
point-in-time resource inventory, not a cost estimate. Quotas and total monthly
cost remain unknown; any future estimate must separate unit-priced resources
with explicit quantity and duration assumptions from unpriced services and
usage such as Vault, logging, and data transfer. The statement that a future
production apply would use the reviewed `ts-infra` workflow records the
assumption in this dated checkpoint. The current ownership boundary assigns
regional foundation and seed setup to the operator through controller A, then
same-cell peers to `ts-orchestrator`; `ts-infra` manages shared Email Delivery
only. Its approved state-only handoff subsequently completed without resource
additions, changes, or destruction; 25 regional state entries were removed,
and post-apply checks verified the four email resources. This state transition
does not establish regional resource health or a live controller. The regional
Terraform definitions and workflow were later removed from `ts-infra` main
commit `e347f13a313ebb2b9d0a0b631ba0aed56af65126`. See the
[manual regional bootstrap runbook](region-bootstrap.md).

## Historical GRU E4 canary proposal (superseded)

This section preserves the estimate and gates from the earlier E4 plan-only
proposal. Its E4 target, A1 exclusion, and separate-authorization statements
are historical and are superseded by the current workspace GOAL above. They do
not define the current preview target or its authorization. The
committed `ts-infra` defaults then had `oci_estate_enabled = false` and
`oci_seed_enabled = false`.

**Historical scope at that checkpoint: plan preparation only.** The current
preview authorization comes from the workspace GOAL. This old E4 proposal is
not a current operator runbook; the linked preview record and acceptance ledger
hold the current evidence and open prerequisites. Production remains **NOT
PRODUCTION READY**.

A1, SFO and FRA are excluded. A1 has cross-build and ELF evidence only;
its price rows below are comparison arithmetic, not this candidate. Normal TerraBase placement intent and reconciliation must remain inactive:
current placement has two fixed member seats per selected region and could
create a second host outside this four-VM inventory. The one-host run qualifies
control-plane and host boundaries, not normal placement or autoscaling.

The candidate resource inventory is four AMD64 E4 Flex VMs at 1 OCPU/6 GB
each, four 50 GB boot volumes, one protected 50 GB member-data volume, and one
private VCN with a private subnet. The five-volume count is a planning
assumption; the member-data volume is retained after the run, and boot-volume
disposition still needs an owner and decision.

There is no approved dollar ceiling.

It may
own only the exact canary foundation and seed, with an explicit controller
handoff and disposal policy; it must not reuse or destroy the protected
production seed. The existing `ts-infra` initial-controller validator accepts
only A1 and the seed has `prevent_destroy`; an E4 seed needs a reviewed canary
profile/validation path. OpenTofu and the orchestrator must never reconcile
the same resource concurrently. The two-hour target is not a hard runtime or
spend cap: a safety/ownership hold can leave compute billable beyond T+120. It does not bound the lifetime or cost of retained data, boot volumes,
ledger/HEAD or keys; each retained resource needs a named owner and retention
decision.

The storage candidate is four 50 GB boot volumes and one 50 GB retained data
volume. Price arithmetic below assumes the balanced 10 VPU/GB tier, but this
is not a selected or requested tier: the Go volume-create request sets size and
does not set performance, and the volume read-back mapping does not expose the
performance tier. Set and read back the intended tier in a separately reviewed
path before treating that price as the canary estimate. The seed boot profile
is already 50 GB; other exact launch and volume settings still need review. The protected member-data volume remains retained; every preserved
boot volume needs a named owner and retention decision.

The network candidate is one reviewed private GRU VCN/subnet in the selected
AD, with private east-west NATS and health traffic. Prove
effective route, NSG and security-list rules for Compute, Object Storage,
Vault/Secrets, instance-principal federation/Identity, IMDS and the required
NATS ports. The current `ts-infra` NSG chiefly defines private ingress; it
does not prove all of that egress. No public IP, Internet gateway, default NAT
or cross-region route belongs in this run. A service gateway does not provide
arbitrary public OS patch/artifact or operator endpoints. Stage signed artifacts in the pinned offline image and separately review the
private operator path; the GRU path is the
[operator gateway](region-bootstrap.md#operator-gateway-peering). Guest clocks must pass the production `adjtimex`
predicate (`TIME_OK`, no `STA_UNSYNC` or `STA_CLOCKERR`, maxerror at most
250 ms), and actual service reachability must be demonstrated before workload
admission.

Therefore the existing
configuration supplies no reviewed GRU CIDRs, subnet key, service-gateway
service ID/CIDR, or NSG rules for this run. Exact network IDs and effective
routes remain lookup and review gates; do not infer them from the candidate
diagram or from the provider's region defaults.

The signed placement profile carries OCPU and memory dimensions through the
launch request. The test uses a 2-OCPU/12-GB fixture; it is not a live launch. Recheck
the proposed 1-OCPU/6-GB E4 dimensions on all four actual instances before
workload admission. A shape name, unit test, or quota arithmetic alone does
not prove the launched VM size.

The following public PAYG list-price snapshot was captured on
2026-09-25T18:12:17Z. This is neither a tenancy quote nor
an all-in estimate. The table's 30-day arithmetic covers only compute and the
five-volume scenario; its A1 rows are excluded from the concrete E4 canary. The block-volume performance rows use the balanced 10 VPU/GB rate only as an
illustrative assumption; the current Go create/read-back path neither selects
nor confirms that tier.

| Candidate line item | SKU and rate | 30-day calculation |
| --- | --- | --- |
| E4 compute: OCPU | `B93113`, $0.025/OCPU-hour | 4 × 1 × 720 × $0.025 = $72.00 |
| E4 compute: memory | `B93114`, $0.0015/GB-hour | 4 × 6 × 720 × $0.0015 = $25.92 |
| E4 compute subtotal | E4 branch only | $97.92; $0.136/hour for four VMs |
| A1 compute: OCPU | `B93297`, $0.01/OCPU-hour after the first 3,000 monthly OCPU-hours | 4 × 1 × 720 × $0.01 = $28.80 list-tier amount |
| A1 compute: memory | `B93298`, $0.0015/GB-hour after the first 18,000 monthly GB-hours | 4 × 6 × 720 × $0.0015 = $25.92 list-tier amount |
| A1 compute subtotal | A1 branch only | $54.72 list-tier amount; $0.076/hour for four VMs |
| Block-volume capacity | `B91961`, $0.0255/GB-month | 250 × $0.0255 = $6.375/month |
| Assumed balanced performance | `B91962`, $0.0017/VPU-GB-month × assumed 10 VPU/GB | 250 × $0.017 = $4.25/month, if read-back confirms this tier |
| Five-volume scenario | Capacity plus assumed balanced performance | $10.625/month, conditional on that tier |
| E4 priced scenario | E4 compute plus assumed five-volume tier | $108.545 for 30 full days, not an approved estimate |
| A1 priced subtotal | A1 list-tier compute plus volume scenario | $65.345 for 30 full days |

The A1 branch consumes 2,880 OCPU-hours and 17,280 GB-hours in 30 days. Both
fall below the stated 3,000 OCPU-hour and 18,000 GB-hour free ranges only if
those ranges are entirely unused by the rest of the tenancy. The A1 priced
subtotal therefore remains $65.345; $10.625 is only the compute-free scenario,
not a promised price. These historical subtotals are not an all-in preview
estimate and do not establish that an A1 deployment fits the current
$200/month combined testing-and-preview cap. Recalculate with the current
tenancy inventory and all required charges.

For the E4 canary, four VMs cost 4 × (1 × $0.025 + 6 × $0.0015) = $0.136 per
hour at these list rates, or **$0.272 for the planned two active hours**. A
safety hold that extends billable VM time increases this compute charge. Under
the unverified balanced-tier assumption, capacity and performance cost
$0.0425/GB-month: five 50 GB volumes exposed for a full month would be
**$10.625**, while the retained 50 GB data volume alone would continue at
**$2.125/month** if boot deletion were separately approved and performed via a
separately reviewed path. The hypothetical
two-hour charge if **all five** volumes were deleted then is about $0.029514,
but that is not the current preserve behavior in the Go provider and cannot be
used as a run cost. At the time of this proposal, no dollar ceiling was
recorded and a prior draft's **$50 first-billing-period example was unapproved
and illustrative only**: under the two-hour compute scenario, $0.272 plus a
full month of five volumes at that assumed tier leaves $39.103 before every
other itemized charge. That arithmetic is not an all-in estimate for the
current authorized $200/month combined testing-and-preview recurring-cost cap,
and a safety hold can extend
billable compute beyond the planned duration. Image/Object Storage, network/transfer, logs, Vault and continued retention
must be priced with named owners before any authorization.

Other known list rates are recorded without inventing workload quantities:
Object Storage Standard `B91628` is free for the first 10 GB, then $0.0255 per
GB-month; requests `B91627` are free for the first 50,000, then $0.0034 per
10,000 requests-month. Logging `B92593` is free for the first 10 GB, then
$0.05 per GB-month. Monitoring ingestion `B90925` is free for the first 500M
datapoints, then $0.0025 per million; retrieval `B90926` is free for the first
1B, then $0.0015 per million. Software Vault key versions `B92092` are free;
HSM key versions are free for the first 20, then $0.5334 per key-version-month.
No dedicated or private Vault tier is selected. Private Vault `B90328` is
$3.724/hour; dedicated KMS `B99597` is $1.75 per HSM-partition-hour with a
three-partition minimum. Those are unselected alternatives, not part of the
priced subtotal.

The public catalog showing no
gateway SKU is not a zero-cost guarantee. A later estimate must show priced
quantities and durations separately from these unknowns; it must not label
the priced subtotals a total monthly bill.

| Exclusive candidate | AD-scoped quota proposal |
| --- | --- |
| E4 / AMD64 | `compute-core standard-e4-core-count=4`; `compute-memory standard-e4-memory-count=24` |
| Five 50 GB volumes | `block-storage total-storage-gb=250` |
| One private GRU VCN | Regional `vcn vcn-count=1` |

Use `where request.ad=<actual-AD>` only after confirming the target AD in the
selected tenancy. Compute and block-storage quotas are AD-scoped; VCN quota is
regional. These quotas constrain resource count/capacity, do not cap cost,
VM lifetime, or role count, and do not reserve capacity. A 2026-09-20 read-only
quota snapshot reported 249 A1 cores, 1,662 GB A1 memory, and 61,340 GB
block storage available in GRU AD-1; it is stale planning evidence and the A1
limits say nothing about E4 availability or capacity.

The following sequence was written for the historical E4 canary. For the
current preview, follow the workspace GOAL's resource-ownership boundaries and
recorded cost/inventory prerequisite; the root GOAL supplies the preview
authorization. Decisions, inventory, state isolation, cost and stop ownership
still precede resource creation. Image/ledger checks that require created
resources block seed launch, and live network/clock checks block workload
admission. A passed check does not substitute for these prerequisites.

2. The pinned base and custom image, signer/delegation, root-signed manifest,
   first-boot delivery, production NTP, and the image receipt consumer are
   verified on the exact source and image. The signed manifest policy is now
   bounded to 365 days, defaults to 30 days, allows one minute clock skew, and
   requires at least 24 hours of current remaining validity for mutation. The
   image receipt and delegation wire are carried publicly in the root-signed
   manifest after image import and remain bound by its exact envelope digest.
4. A separate read-only bucket auditor, authorized only for `BUCKET_READ`,
   checks `GetBucket`, `ListRetentionRules`, and `GetRetentionRule` in the
   pinned region. It verifies a private, exact-KMS, nonversioned, locked-WORM
   immutable ledger bucket and a separate private, exact-KMS, versioned CAS
   `HEAD` bucket without WORM retention. Conditional writes alone are not
   WORM. The minimum lock/retention duration must be explicitly selected by
   the decision owner; the runtime must not guess or inspect bucket policy.
7. The offline CLI, focused receipt tests, production broker/JWT/clock gate,
   and no-live-secret/image delivery paths pass review. R6's static-TLS
   fixture is not evidence for active JWT/ClockCheck or production NTP; R7's
   JWT/NTP attempt failed before VM boot and has no guest outcome.

At the historical proposal checkpoint, none of the commands below had been
executed; this was a future sequence for that E4 candidate.

2. Review the separate canary root/state, exact Flex dimensions, selected AD
   and pinned image, five volume sizes/tiers and boot disposition, private
   routes and service/NTP/operator reachability, run duration, itemized cost,
   owners and stop automation. Keep A1, SFO, FRA and production `ts-infra`
   state/resources out of this run.
4. Prove exact seed identity and 1-OCPU/6-GB launch dimensions on each VM,
   current image receipt, private networking, synchronized clock, broker
   authorization, and bootstrap-ledger properties before workload admission.
   No local `tofu apply`, manual ownership transfer, or overlapping
   `ts-infra`/orchestrator reconciliation is allowed.

The qualification operator who creates a resource owns its stop and cleanup. At T+90 minutes, stop new creates and begin the controlled stop. Target T+105 minutes to stop test workloads and capture fresh, identity-bound
writer-stop proof or evidence that no writer was admitted; absent that proof,
hold detach and termination for explicit reconciliation. Target T+120 minutes to
detach the protected data volume only after writer-stop, host stop/unmount and
exact attachment checks, and re-observe its detached state. Terminate only the
four exact run-owned VMs when those safety
conditions hold, then verify their terminal states and inventory of preserved
boot/data volumes, immutable ledger, CAS `HEAD`, and any other retained items. Termination alone does not delete the boot or data volumes. Otherwise record each preserved boot
volume and its owner. These milestones do not
authorize unsafe detach, termination, or deletion when proof is missing. A
safety/ownership hold may extend billable compute beyond T+120; the named owner
must track and resolve the resulting charges. There is no approved spend cap. The T+90/T+105/T+120 milestones are targets, not an implemented expiry timer or
spend cutoff. Before any separately authorized execution, review and test a
run-scoped enforcement and operator-response plan that blocks new creates by
T+90, starts the controlled stop by T+105, and defines escalation when safety
evidence prevents detach or termination. No such enforcement path is qualified here;
because a safety hold can keep compute billable, the two-hour target is not a
hard runtime or spend cap.

## Latest local qualification limits (2026-09-25)

R6 is the latest completed four-VM run. Its clean source revision was
`10970344f53afe246b787177c1f439aa9efb2620`, with Go source manifest
`11dc97ca8af8c106179630ae8d590d871595603109d0982eb8bbc7e0fb07da77` and
harness hash `b166c78851c9b7e7204aa9d38d6330801065d341d4eeb4199eeccc6618cd58f3`.
It reached initial v1 execution, host reboot recovery and 2/3 controller
readiness, then failed the 25-second same-process host-session renewal check.
The operator `hosts` attempts timed out; the required current session, report,
and unchanged process proof was not obtained. R6 therefore did not reach v2
deployment, signed-expiry fencing or rollback. Its `cleanup_errors` were empty.
Evidence: `/tmp/ts4vm-20260925-r6/summary.json` and
`logs/nats-live-diagnostics.jsonl`. The post-run parser correction narrows
renewal evidence to the verified guest log format. The later leader-read fix
addresses a diagnostic direct-KV read that took the 2-second timeout while
the equivalent leader read took about 6 ms. Neither correction retroactively
passes R6 or proves its 25-second renewal requirement.

The older R5 attempt is preserved at `/tmp/ts4vm-20260925-r5/summary.json`.
Both R5 and R6 used static TLS and manual pre-start guest clock setting, so
neither tests production JWT admission or the kernel NTP predicate. The
accepted R7 harness at commit `a54c8b1` instead builds the frozen JWT fixture
and a probe calling the production `KernelClockProbe.Measure()` predicate,
starts bridge-only Chrony with a real selected upstream, waits for guest
timesyncd before releasing services, and tests pinned c1 admission closure
and recovery. Its clean detached source and four static binary builds are
recorded under `/tmp/ts-orch-r7-qualification-a54c8b1` and
`/tmp/ts-orch-r7-qualification-binaries-a54c8b1`. The R7 attempt **FAILED
BEFORE VM BOOT** at host Chrony readiness: root `chronyd` refused its command
socket beneath the user-owned run directory, although it selected a real
upstream. The bridge UDP listener was configured, but the `chronyc` readiness
probe could not connect and the harness never reached listener observation.
Evidence is
`/tmp/ts-orch-r7-qualification-run-20260925T160720Z/summary.json` and
`logs/chronyd.log`. The shared-tree harness now creates a root-owned mode-0700
socket directory under `/run`; its 33 focused tests and a pinned Chrony 4.8
foreground no-NTP-port socket probe passed. This fix has not been used for an
R7 guest rerun. The four-guest result remains **PENDING**; build, fixture,
bridge and socket tests do not substitute for guest evidence.

The corrected local JWT R3 tests now exercise the signed operator
`broker-claim-apply` caller and real TLS-first broker bridge. Both focused
tests passed: `TestRunControllerOperatorBrokerClaimApply` covers the CLI/caller,
and `TestBrokerGateR3TicketRevocationAndOfflineFence` covers the gate/fence
directly; see `/tmp/ts-broker-jwt-r3-final-caller-focused.log`. These tests resolve the earlier helper-only and invalid-fence-floor review
findings in their local scope.

A separate one-guest Unix-socket member-status attempt **FAILED**: systemd
recorded `ts-member-boundary.service` exiting status 1 after 5.745 seconds.
The Rust result and Go marker were not captured because the service wrote to
`ttyS0` while serial-getty also ran. The outer 240-second watcher saw no exit
marker; this is a monitor/output failure, not evidence that the service kept
running for 240 seconds or that the member boundary passed. See
`/tmp/ts-member-boundary-vmrun-20260925T1220Z/attempt-outcome.txt` and
`guest-systemd.journal`.

The later delegated one-guest attempt **FAILED** with a captured and verified
systemd journal. The guest reached the `/supervisor` service subgroup, reported
the expected `0x1e1` effective and bounding capability mask, and showed a
5 GiB service `MemoryMax`. During native runner `Apply`, the Go execution
helper logged `epollwait on fd 5 failed with 9` (`EBADF`) and
`fatal error: runtime: netpoll failed`; the runner reported that the native
target exited before verification. The Rust test failed;
`ts-member-boundary.service` exited status 101, while Firecracker exited 0. The role
`memory.max`, workload capability drop and Unix-socket member-status checks
were not verified. The cause remains under runtime investigation; this is no
member-status or production-readiness pass. Journal extraction and verification
worked; the Firecracker process, socket, mount and loop attachment were quiescent after
cleanup, with the guest image retained for forensics. Evidence is
`/tmp/ts-member-boundary-vmrun-delegated-20260925T1659Z/summary.json`,
`guest-systemd-unit.log`, and `runtime-evidence.sha256` (SHA-256
`ebc56d0e7c4707ca04e02b50444ee5e087b93becfbd6eca7decc67aa21e12e78`).
The full systemd main-process-death boundary remains open. This guest failure
is separate from R7's pre-VM Chrony failure. Commit `3aef6fba` later changed
native helper FD preservation, but it has no guest requalification result.

## Proposed trust and bootstrap contract

These are the planner's preferred interfaces for implementation and
qualification. They are design inputs, not accepted production behavior.

3. Cloud-init contains only role and public signed-manifest references. It
   carries no private key, Vault secret, NATS seed, or installer credential.
   The image's trusted binary verifies the receipt; a network download is
   never trusted to verify itself.
5. **Historical proposal, superseded for current operation.** The earlier
   two-phase `ts-infra` proposal put foundation and seed creation in OpenTofu
   and is replaced by the operator-run [regional bootstrap
   runbook](region-bootstrap.md). At its recorded candidate (`ts-infra`
   `3fff4df2d3f92c0343cd11c633fc0ba36a82f3e8`, draft PR #16), no apply had run
   and both gates were false. Regional source/state migration still requires
   its own reviewed, non-destructive plan identifying the exact resources;
   this historical proposal does not show that migration has completed.
   Disabling future ledger archiving does not restore records already archived.
6. TerraBase admission should use native v2 ULID database/member identities,
   numeric shard and incarnation values, and reject legacy v1 labels without
   an alias shim. This remains blocked on a frozen TerraBase producer
   contract; later mutable producer source includes an outbound sender and
   `AppliedAck`, but current-source real-peer acceptance, serving proof and
   durable drain semantics are still missing.

## Production-readiness gates

No production gate in this table is **CLOSED**. Evidence must be collected
from the exact code and image being qualified; a design document or isolated
unit test does not close an integration gate. The current M0/M1 delivery gates
are tracked separately in the [shared-goal acceptance ledger](evidence/shared-goal-acceptance-20260926.md).

| Gate / ownership | Required implementation and acceptance evidence | State |
| --- | --- | --- |
| Host runtime contract — host image/runtime slice, `internal/host/**` | Qualify the exact pinned kernel and image for writable cgroup v2, execution, cancellation, restart recovery, and safe child cleanup. Define the service user, cgroup delegation, state/install directory ownership, read/write mounts, stop timeout, and restart policy. Prove workload privilege boundaries before accepting untrusted workloads; a native process and a startup probe alone are not a tenant sandbox. | IN PROGRESS; the earlier 8/8 native security run covered nested-supervisor death and child cleanup, but full systemd main-process death and writable-cgroup guest qualification remain OPEN. The earlier one-guest Unix-socket attempt exited status 1 without a captured application result; the later delegated attempt captured a verified journal but failed during native Apply with a Go netpoll fatal error before role and Unix-socket verification. The cause is under runtime investigation. Root-to-service credential handoff has source but its real privileged subprocess and restart caller still require review and qualification. The delegated supervisor leaf reached guest startup, but native workload verification failed. R7 failed before VM boot, so JWT/NTP host evidence still needs a rerun. |

## Production-readiness follow-on

The API-first preview sequence and M0/M1 exit criteria are defined in the
[workspace GOAL](../../GOAL.md#5-delivery-sequence) and tracked in the
[shared-goal acceptance ledger](evidence/shared-goal-acceptance-20260926.md).
After that milestone, close the production gates above: signed release and
pinned-image qualification, host enrollment and runtime recovery, durable
TerraBase serving and drain evidence, safe scale-in, backup and restore, and
regional failure testing. Regional Raft remains a separate proposal and is not
a prerequisite for the first preview.

The first bounded deployment target is now the workspace GOAL's API-first,
low-cost ARM64 preview with both services and the existing leaderless profile. The E4 control-plane-only canary above is historical and is not the current
target. A preview result does
not imply production readiness.

## Unresolved authority decisions

- Provision the offline release signer, publish its trust anchor into the
  image, and decide signer rotation and revocation behavior. A missing signer
  key cannot be replaced by an unsigned build or test key.
- Qualify the immutable pre-quorum ledger bucket, conditional-write and
  retention behavior, KMS authority, Vault path/version policy, and the
  operator-A to Go-controller identity/authority handoff. The current boundary
  keeps regional foundation and the first seed with the operator until explicit
  handoff, then assigns same-cell B/C to `ts-orchestrator`. The completed
  `ts-infra` state-only handoff is a separate state operation; it does not
  establish regional resource health, a live controller, or the required
  operator-to-orchestrator identity, authority, and inventory handoff. Source
  cleanup is separate. See the
  [manual regional bootstrap runbook](region-bootstrap.md).
- Freeze TerraBase v2 identity, readiness, replication, drain, and writer-stop
  contracts with its producer team.
- Set availability targets for controller loss and host session loss, replica
  floor, scale policy, RPO, RTO, and backup retention. Apply the authorized
  preview cap to recurring preview resources; define production limits
  separately.

Until those decisions and the acceptance ledger are complete, this document
must not be read as an operating runbook or a production approval.
