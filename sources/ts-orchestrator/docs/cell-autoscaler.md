# TerraBase cell autoscaler

`internal/cellscale` runs a TerraBase cell without an operator. It reads the
pressure of every db node, then takes at most one bounded action per
evaluation:

- add a node (scale out);
- drain and remove a node (scale in);
- move a tenant between nodes (rebalance).

Every action and every refusal is journaled. `ts-orch cell-autoscaler` runs
the loop and is a dry run unless `--live` is given.

Status: tests use fakes. TerraBase does not
serve the pressure endpoint or the join, drain and move hooks yet.

## Cells, nodes and tenants

Names come from `internal/naming`. A cell is named `<region>-<index>`, for
example `gru-1`, and its db nodes are `<cell>-db-<n>`; the autoscaler uses
`n` from 1 to 64. A scale out takes the lowest free `n`; a scale in removes
the highest. The autoscaler only manages instances that carry the freeform
tags `ts-cell=<cell>` and `ts-role=db`, and it sets those tags on every node
it launches. An instance with a db node name but without those tags is
foreign, for example a placement seat (placement names its signed seat pair
`gru-1-db-1` and `gru-1-db-2`). Its name stays reserved, and the autoscaler
never counts, resizes or removes it. Launch refuses a name that a foreign
instance holds. If all 64 names are taken, scale out holds at capacity.

Tenants are organizations on a plan tier: `hobby`, `pro` or `enterprise`.
Moves take lower tiers first. Enterprise tenants have no limits, so they
move only when no hobby or pro tenant fits elsewhere.

## Node pressure contract

Every db node serves `GET /v1/node/pressure` and answers with one JSON object
of at most 64 KiB:

| Field | Meaning | Bounds |
| --- | --- | --- |
| `schema` | contract version | exactly 1 |
| `node` | the node's static name; must equal the node asked | `<cell>-db-<n>` |
| `state` | `joining`, `ready`, `draining` or `drained`; only `ready` serves and has caught up | one of the four |
| `sampled_at` | when the node measured the whole report, never when it was fetched | RFC 3339; at most 2 minutes old, at most 5 seconds ahead |
| `process_id` | opaque identity of this TerraBase process start; changes on every process restart/reboot and is never reused | 1–128 of `[A-Za-z0-9._:+-]` |
| `release` | the TerraBase build running; nodes that differ mean a rollout is in flight | 1–128 of `[A-Za-z0-9._:+-]` |
| `cpu_util`, `mem_util` | fractions of the node's current shape; the names match the host telemetry signals | [0, 1] |
| `disk_used_bytes`, `disk_total_bytes` | the data disk | 0 ≤ used ≤ total, total > 0 |
| `disk_iops`, `request_rate` | per second, over the node's last sampling interval | [0, 1e9] |
| `io_queue_depth` | mean in-flight I/O | [0, 1e9] |
| `p95_latency_ms` | client request latency | [0, 1e9] |
| `load` | the member status load block from [autoscale telemetry](autoscale-telemetry.md), unchanged: `connections`, `storage_bytes`, `replication_lag_seq`, `write_qps` | required, non-null; `memberstatus.DecodeLoad` and `Load.Validate` |
| `top_tenants` | at most 10 distinct organizations, by request rate; `cpu_share` is the tenant's fraction of the node's CPU time | org `[a-z0-9-]{1,64}`, plan tier, share in [0, 1]; duplicate orgs are rejected |

Every field except `top_tenants` is required and non-null, including every
counter in `load`. When a tenant entry is present, all four of its fields
are required. Explicit zero utilizations, rates and counters are valid;
omission never means zero.

A report that fails validation, is stale, names another node, or does not arrive
counts as an unreadable node. That holds the whole cell. `cellscale.HTTPSource` reads the contract. The tests use an in-memory fake
cell instead. Freshness is checked after the HTTP response completes, at the
decision, before each mutation and in readiness/drain waits. A cached `ready`
or `drained` report cannot complete a wait or authorize an action. Launch, join and drain completion require a sample measured after the request
began plus the allowed 5-second clock skew. Every valid observation advances that node's
sample floor, including unready states. Older readiness cannot overwrite a
newer unready report. Conflicting reports at the same timestamp hold until
strictly newer evidence arrives. A later process start with newer evidence
remains valid. Only confirmed no-effect resize rejections clear an uncertain resize refusal. Rejections can retry, reach the failure pause, and
recover after `Resume` without accepting uncertain restart readiness. After controller startup, all usable reports must be measured after startup
plus the same clock-skew margin, even with zero configured cooldown. This
rejects cached pre-start readiness when in-memory restart evidence is lost.

## Placement replica inventory

Before scale-in, the controller also reads `GET /v1/cell/replicas` from a
ready member. This is a complete, authoritative cell inventory, independent
of the top-tenants load list, with a 1 MiB response limit:

Every field is required and non-null; only an explicit `placements: []`
with `complete: true` means no placements. Each `(org, database, shard)`
appears once. Organizations use the pressure contract's identifier; database
identifiers are 1–128 characters from `[A-Za-z0-9._:+-]`, and shard IDs are
positive integers. `live_replicas` names distinct nodes of this cell that
currently serve a durable copy caught up to that shard's source frontier. Stopped, receiver-only, lagging and planned replicas are excluded. `members`
contains every owned node, including draining nodes and nodes with no live
placements.

The same 2-minute age and 5-second clock-skew limits apply. Scale-in has two
separate gates:

1. **Start drain:** the surviving cell stays at or above `nodes.min` and the
   replication factor, and every placement on the target has a ready
   destination with capacity. Replicas do not need to have moved yet.
2. **Terminate:** drain has finished and a fresh post-drain observation proves
   that **every** placement retains at least `replication_factor` live, ready
   copies excluding the target, with quorum. Copies on unreadable or lagging
   peers do not count. The controller polls this full gate until convergence or
   `ReadyTimeout`, refreshing peer pressure on every poll, before a final
   identity/lifecycle/evidence recheck. Drained-node recovery uses this same gate.

A missing, partial, stale or conflicting inventory holds the relevant gate.
Resizes also require this inventory: before every restart, actual surviving
replicas of every placement must retain quorum. Configured replication
factor alone cannot prove that a quiet database has enough copies. CPU/memory
growth uses scale-out when actual replica evidence makes restart unsafe.

Placement samples must also be measured after controller startup and the
latest membership/restart convergence, plus the full 5-second clock-skew
margin. Launch, join, drain, terminate and tenant moves fence prior inventory;
rolling resize waits for post-restart placement before continuing. State or
process changes and unreadable nodes also fence old placement evidence. A same-name replacement needs new placement evidence too. Stable
membership and listing-order changes do not keep advancing this fence. The controller tries other ready members when one inventory endpoint fails or
returns unusable evidence, including during convergence waits. A lower or
conflicting timestamp never becomes usable merely by asking another peer. Every accepted inventory advances a sample high-water mark; older snapshots
cannot replace newer under-replicated evidence. Contradictory placement sets
at the same timestamp hold until a strictly newer inventory arrives. Wire
ordering of the same placements and replica names does not create a conflict. Discarding mismatched membership preserves the highest prior inventory or
refusal timestamp; recovery requires inventory strictly after that bound.

A same-name replacement aborts the action,
including when its readiness and replica inventory are fresh. Scale-out adds
the ID returned by Launch; only the terminated target may disappear from the
expected membership. It invalidates affected cached pressure,
fences inventory and requires samples after discovery plus clock skew. Rechecks abort a shape change outside the controlled restart target, so
capacity decisions and later retries cannot use earlier utilization. A later
tick can observe fresh evidence and plan against the new cell. The incarnation is `process_id`
in the pressure contract and is never reused. One identity transition
invalidates the previous lifetime’s operational state atomically. Complete
inventory lists every owned member with the same identity; name-only or
predecessor inventory cannot authorize any action. Replacement evidence must
follow discovery plus the clock-skew margin. Retired identities and monotonic
time floors only refuse replay; they never supply readiness or progress. Convergence may wait through the controlled target's transition;
peers must stay running, and readiness cannot release a restart fence while
the target or a peer is stopped.

Destination fit uses the target node's whole measured load as a conservative
bound because inventory has no per-placement load sizes. CPU and memory are
converted to the destination's OCPU/GB shape; disk bytes use its disk capacity.
Projected CPU, memory, disk, IOPS, requests, queue and latency must fit the
configured targets. A missing replica needs an eligible peer that does not
already hold that shard; existing sufficient copies can receive transferred
workload. Bounding each destination by the whole source also covers multiple
placements assigned there, without relying on the top-tenants list.

TerraBase's drain hook must fence new placement onto the target, prepare
replacement copies on peers and preserve serving quorum throughout evacuation.
Replica migration remains TerraBase work. With RF=3 on four nodes, a target
holding one of three copies can start draining into the spare peer; termination
waits for three live, ready peer copies. RF=3 on three nodes never starts drain.

Immediately before a load-driven drain, the controller repeats the projected
pressure check with current metrics across all seven signals. Recovery of an
already draining node and explicit above-max correction retain their existing
safety rails. Before a tenant move, its current top-tenant report and the
destination's current CPU/request capacity must still authorize the move;
CPU accounting uses the source and destination's current OCPU sizes.

## TerraBase hooks

TerraBase does the work; the autoscaler only orders the steps and waits for
the node's reported `state`. The hooks are `POST` requests to the node's base
URL, and both `200` and `202` count as accepted:

| Hook | Called on | Done when |
| --- | --- | --- |
| `/v1/node/join` | the new node, once it answers its pressure endpoint | the node reports `ready` |
| `/v1/node/drain` | the node being removed, after destination-fit and cell-floor checks | fresh `drained` report and a fresh complete inventory proving every placement's surviving replicas; only then is it terminated |
| `/v1/tenants/<org>/move` with `{"to": "<node>", "expected": <source identity>, "expected_target": <destination identity>}` | the tenant's current node | the call returns (moves are hook only) |

Each receiver must atomically verify this
precondition before effects and reject a changed identity (for example HTTP
409). A move also verifies `expected_target` at its destination; the source
and destination must retain those identities throughout the move. These
preconditions close the replacement window between a controller read and a
name-routed POST. The TerraBase hook implementation remains an integration
prerequisite.

Mutation hooks reject redirects, including with a supplied HTTP client, so
a redirect to a successful page cannot count as an accepted action.

Restrict these endpoints to the NetBird mesh. The autoscaler sends no
credentials. Join must be idempotent: a failed or interrupted join can be
retried while the owned node reports `joining`.

## How it decides

A signal's pressure is its value divided by the policy target for one node,
so 1 means full. The seven signals are CPU, memory, disk used, IOPS, request
rate, I/O queue depth and p95 latency. The cell's pressure for a signal is
the mean over its nodes. A node's pressure is its largest signal.

The checks run in this order; the first match decides:

1. Hold if the autoscaler is paused, a rollout is in flight, any node is
   unreadable, or any ready node's `load.replication_lag_seq` exceeds
   `max_replication_lag_seq`. If exactly one owned node reports `joining`,
   retry its join without launching another instance; if it reports
   `draining` or `drained`, wait for the drain and finish its termination.
   This recovery skips the sustain window, passes all rails, and requires
   every peer to be ready on the same release. Otherwise an unready cell holds.
2. Restore the bounds: below `nodes.min`, scale out at the largest observed
   shape only when the budget also reserves minimum-sized launches for every
   remaining missing node; otherwise launch at the minimum shape. If even
   those launches cannot fit, propose the largest affordable corrective
   downsize that preserves the full reserve. Per-node pressure, replica
   quorum, cooldown, rate and dry-run rails still apply; unsafe recovery holds.
   If no safe correction leaves the full reserve affordable, launch holds
   even when the next minimum-sized node alone would fit.
   Rolling resizes reduce the most expensive nodes first, so mixed shapes
   cannot temporarily exceed the larger of the original and final run rates.
   Every mutation recheck requires capacity to match the original action
   plan; only a completed controlled resize updates its target's expectation.
   Resize completion repeats this check after the final inventory wait;
   scale-out completion repeats it after post-join readiness convergence.
   Above `nodes.max`, scale in. If node shapes differ (for example after an
   interrupted resize), converge to the largest shape when its cost passes
   the budget rail; otherwise continue evaluating load on the mixed cell.
   Bounds and affordable shape corrections skip the sustain window.
3. **Cell pressure ≥ 1.** If CPU or memory leads and the shape can grow,
   resize up one `step_ocpus`. A bigger shape relieves every node at once,
   while new nodes only help after tenants move to them. Otherwise scale out.
   At `nodes.max`, resize if the shape can still grow. Storage pressure (disk
   used, IOPS, I/O queue depth) belongs to the volume, so it never resizes.
   If nothing works, hold with `at-capacity`.

4. **One node ≥ 1 but the cell below 1.** This happens with a noisy tenant,
   or with a new node that joined empty.
   - Move a tenant of the hot node to the coolest ready peer that fits it: hobby
     first, then pro, then enterprise, the largest first within a tier. A
     tenant fits if that node's CPU and request pressure stay below 1. It must
     also have positive attributed demand in a hot CPU or request signal;
     the fresh pre-move check repeats this eligibility check.
   - If no eligible tenant fits, but one would fit on an empty node, scale out. Convert
     tenant CPU demand from the source's OCPUs to the proposed node's OCPUs.
   - Otherwise resize up, unless the hot node's leading signal is storage.
5. **Scale in.** Remove a node when the cell's largest signal, multiplied by
   n/(n−1), stays at or below `scale_down_below`. The cell never drops below
   `nodes.min` or the replication factor.
6. **Resize down** one step when every node's projected CPU and memory
   pressure at the smaller shape stay at or below `scale_down_below`.
7. Otherwise hold with `within-band`.

Resize steps must change OCPUs or memory by at least 0.001, matching the
shape comparison tolerance. A step clipped at a bound below both tolerances
is skipped; hot cells use horizontal growth when possible instead.

The gap between 1 and `scale_down_below` is the hysteresis band. A
load-driven action must be wanted on every evaluation for
`sustain_up_seconds` (actions that add capacity or move load) or
`sustain_down_seconds` (actions that remove capacity). A spike shorter than
that never acts.

## Safety rails

Every action passes all of these. A refused action is held, and it acts as
soon as the rail clears. The hold carries the refused action (`held` in the
command's output, an alternative in the journal):

| Rail | Rule |
| --- | --- |
| quorum | Drain begins only with enough surviving cell nodes and a destination that fits every target placement. Termination requires drain completion and fresh proof of the full replication factor and quorum on live, ready survivors for every database/shard. A rolling resize needs both `n−1` and `replication_factor−1` to be at least `replication_factor/2+1`. Factors 1 and 2 cannot restart safely without replica preparation even when the cell has spare nodes. |
| recheck | An action waits minutes, so the controller observes the cell again right before each step that changes it: launch, join, drain, terminate, each node's restart and each move. It stops the action if the members changed, if any peer is not `ready` or lags beyond `max_replication_lag_seq`, or if a rollout started (by release skew or the gate). The joining node's release must match its peers. Before a terminate, the target must still report `drained` and every peer must serve. Before each restart, every shrinking resource must still fit each node's latest pressure at `scale_down_below`. `ReadyTimeout` reaches each polled request; a result arriving after the deadline cannot complete the wait. |
| rollout | Hold while nodes report different releases, or while the rollout gate reports a rollout in flight. A gate that fails or answers anything but `{"in_flight": true\|false}` fails the tick. `--live` refuses to start without `--rollout-gate`. |
| cooldown | `cooldown_seconds` after any action before the next action that adds CPU or memory capacity or moves load. `scale_down_cooldown_seconds` before the next action that removes capacity. A controller start counts as an action. |
| rate | At most `max_actions_per_hour` actions, counting a full rolling resize as one. |
| budget | An action that raises the cell's monthly run rate above `monthly_budget` is refused. The run rate is nodes × (OCPUs × `ocpu_hour` + GB × `memory_gb_hour`) × 730 + `node_monthly`. Scale downs always pass. Validation rejects a policy whose floor (`nodes.min` at `min_ocpus`) exceeds the budget. |
| audit | A decision that cannot be written to the audit stream stops `run` before the action's first effect. |

## Audit and undo

The decision journal (actor `cellscale`, subject `cell/<cell>`) records the
following. `ts-orch cell-autoscaler run` writes every decision to stderr as
one JSON line, with all its signals and attributes:

- every action, as `in_progress` and then as `succeeded` or `failed` linked
  to it;
- every new hold reason, once per change;
- every pause.

Membership recovery carries `recovery=true` in the action and journal. A
joining instance is already billed, so its recovery adds no projected cost.

Each action carries the cell's pressure signals, its monthly cost after the
action, and an `undo` attribute holding the reverse action as JSON:

| Action | Undo |
| --- | --- |
| scale out | scale in of that node |
| resize | resize back to the previous shape |
| rebalance | move the tenant back |
| scale in | none: its data was drained, so scale out a fresh node instead |

The launch journal is a cell/region-scoped file at
`/var/lib/ts-orch/cell-autoscaler/<hash>/launches.json`. It retains at most 64
names and 8 MiB, including frozen cloud-init input; protect it as a secret.
Each replacement fsyncs the private temporary file, atomically renames it and
fsyncs the containing directory. Accepted instance IDs and reconciliation
changes are persisted too. A failed save blocks subsequent mutations and
reconciliation on that cloud until restart; inspect the journal first.
Live SDK clouds refuse mutation until this persistence is configured.

A new launch generation whose initial call contains only confirmed no-effect
rejections releases its intent durably before a corrected launch can proceed.
An earlier ambiguous SDK attempt, replayed/restored intent, accepted instance
ID or conflicting response retains the fence. Failure to save the release
latches the same reconciliation and mutation block.

An uncertain launch may replay only until 23 hours after its original intent.
Expiry, missing List results, a 404 and changed policy never authorize a fresh
token. A new generation requires the known instance ID to be positively
`TERMINATED`, or a terminated instance tagged with that generation's exact
`ts-launch-token`. Expired unresolved launches require operator reconciliation.
Keep the durable journal across reboots, runner restarts and upgrades; do not
replace a lost journal with an empty one. This local journal and flock require
one runner per cell on a shared persistent state/lock namespace.

## Command

`check` prints `lock_file`, `launch_journal` and `initial_launch_journal`.
Before starting a runner, an administrator must provision the root-owned lock
directory/file and durable state parent. The per-cell state directory and
journal belong to the runner UID with modes 0700 and 0600. Create pristine
state only for a cell that has never issued a launch through this autoscaler;
never reset existing state. Provisioning example (not run by the controller):

```sh
report=$(ts-orch cell-autoscaler check --config cell.json)
lock_file=$(printf '%s' "$report" | jq -r .lock_file)
sudo install -d -o root -g root -m 0755 /run/lock/ts-orch-cell-autoscaler
sudo sh -c 'umask 022; set -C; : > "$1"' sh "$lock_file"
runner=ts-orch
journal=$(printf '%s' "$report" | jq -r .launch_journal)
sudo install -d -o root -g root -m 0755 /var/lib/ts-orch /var/lib/ts-orch/cell-autoscaler
sudo install -d -o "$runner" -g "$runner" -m 0700 "$(dirname "$journal")"
printf '%s' "$report" | jq -c .initial_launch_journal |
  sudo -u "$runner" sh -c 'umask 077; set -C; cat > "$1"' sh "$journal"
```

The creation commands refuse existing files. Re-provision the runtime lock
file after reboot before restarting the runner; preserve the durable journal. Configuration files must contain exactly one JSON
value; trailing whitespace is accepted, appended values or malformed data
are rejected by both `check` and `run`.

`endpoint` must be a non-opaque HTTP(S) URL with a hostname and `{node}`.

The rollout gate is a `GET` URL that answers `{"in_flight": true}` or
`{"in_flight": false}`. Point it at whatever owns TerraBase rollouts for the
cell. It requires one bounded JSON object and rejects duplicate or unknown
fields, null values, and trailing data. The file is read with unknown fields
rejected. The loop prints each tick's
action to stdout and errors to stderr. The pause and the decision memory live
in the process; a restart starts with a fresh cooldown.

## Preflight

They:

- check that the shape is offered and flexible in every occupied AD and the
  launch AD, and that the policy's OCPU and memory ladder fits each domain's
  limits. Only the launch AD uses the template image compatibility filter;

The JSON report includes each checked quota's domain, available headroom and
required growth; an omitted domain identifies a regional quota.

`TestOCIReadOnlyAgainstRealAPI` runs `List` and `Preflight` against a real
tenancy with the DEFAULT profile, through a guard that fails the test on
any launch, update or terminate.

`TS_CELLSCALE_OCI_AD`, `_IMAGE` and `_SUBNET` are optional. It then expects exactly that subnet
problem.

## Limits

- Tenants are chosen for a move by request rate and CPU share, the only
  per-tenant loads in the contract. A node that is hot on disk, IOPS or
  latency may need several moves.
- All nodes of a cell share one shape ladder. Shape convergence also moves a
  node whose memory differs from `memory_gb_per_ocpu` back onto the ladder.
- An unreadable node or multiple unfinished membership transitions hold the
  cell (`cell-not-settled`) until repaired. One readable unfinished join or
  drain is retried; repeated failed recovery attempts pause and alert. The
  autoscaler does not terminate a node it could not join.
- The command runs beside the regional controller rather than inside it.
  `Config.Rollouts` is the seam for the regional rollout store once the
  controller hosts it. Inside the controller, the host telemetry
  `hostload.Aggregator` (see [autoscale telemetry](autoscale-telemetry.md))
  already carries CPU, memory, disk and the load block per node and could
  back a `Source`.
