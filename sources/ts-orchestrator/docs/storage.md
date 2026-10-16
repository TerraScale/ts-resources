# Storage

`internal/storage` owns retained-volume policy for TerraBase members.

| Package | Purpose |
|---|---|
| `storage/lifecycle` | Pure volume state machine with deadlines and `stuck`/`held` phases. Placement uses it to hold an attachment stuck ATTACHING (default 10 minutes) with a remediation instead of waiting forever. |
| `storage/hostvolume` | Host-side primitives for the root volume initializer: hardened mount flags, ext4/xfs format commands, online grow. |
| `storage/capacity` | statfs collector, the TTL'd `TS_STORAGE_USAGE` KV bucket, and pressure signals for placement and autoscaling. |

## Mounts

Managed volumes are mounted `nosuid,nodev,noexec,noatime`. ext4 volumes also
use `errors=remount-ro`. The initializer reads the per-mount flags back
before it completes the volume layout. TerraBase runs from the managed runtime
root, not from the volume. The volume holds only `data/`, `replication/` and
the claim file, so it needs no exec, set-id or device nodes. A mount made by
an older initializer is bind-remounted with the hardened flags the next time
the initializer touches it, including a mount that has the three security
flags but lacks `noatime`. This is best effort and failures are logged.

A signed `xfs` pin is formatted with `mkfs.xfs -m uuid=<pin>`, which needs
`xfsprogs` on the host image.

## Opt-in features

Every feature below is off by default.

| Setting | Effect | Prerequisite |
|---|---|---|
| placement `auto_grow_volumes` | Grows a retained volume created under a smaller resource profile through the journaled `Fleet.ResizeRetainedVolume` (grow-only). | None. |
| controller `storage_capacity.enabled` | Each controller publishes its boot root and JetStream StoreDir usage. The unused JetStream max-store reservation counts as used, and it is also subtracted from the node's boot headroom when the StoreDir is on the boot filesystem. Pressure is logged, and critical pressure is logged as an error. | None. |
| placement `reattach_on_host_loss` | A replacement host attempt takes over its lost predecessor's retained volume (see Reattach on host loss). | The lost-member replacement itself needs a `LostMemberEvidence` source. Roll every controller to this version first (new durable field). |

## Resize and ownership

A `volume-resize` operation is keyed by volume, target size and attempt. Attempt 1 keeps the original `<volume>/<size>` key; later attempts use
`<volume>/<size>/attempt-<n>`, up to 8. Its intent records the predecessor
size and ETag. One If-Match `UpdateVolume` changes both the size and the
`terrascale-volume-size-gib` tag. The confirmed result advances the volume
ownership record by CAS. If that ownership record is lost, it is rebuilt
from the confirmed create plus a confirmed attempt of the resize.

A new attempt starts only when the previous attempt of the same target never
confirmed, the volume is still below the target, and its ETag no longer
matches the attempt's If-Match ETag, so that request can never land as
journaled. Before attempts existed, such a same-size retry held with
`ErrStaleETag` (#133, finding 11583 item 2). With the ETag unchanged an
unknown attempt is retried on its own key, as before. A volume whose ETag
moves under all 8 attempts holds with `ErrStaleETag`.

## Reattach on host loss

With placement `reattach_on_host_loss`, a replacement host attempt (whose
member state records `previous_instance_id`) does not attach its retained
volume directly. Each placement tick runs one `failover.Reattacher` step:

2. Detach a live attachment of the old instance through
   `Fleet.DetachFencedAttachment`: a journaled `volume-detach` (same key as
   the evidence-driven detach of that attachment fence) whose fence is
   re-read after the authority guard, right before the effect. A detach
   that does not reach DETACHED within the settle window is recorded
   Unknown; terminal discovery treats a detach whose exact attachment is
   now DETACHED or gone as settled.
4. Attach to the replacement with `AllowDetachedHistory`: DETACHED records
   no longer hold the attach. Any other live attachment still holds it, and
   a live attachment on an unrelated instance holds the reattach for an
   operator.

Each step is guarded against the tick's authority epoch and bound to it
(`Reattacher.ExpectedEpoch`), so member state read under one epoch never
drives a detach or attach under a later one.

`InspectVolumeInitialization` admits a volume with DETACHED attachment
history only when that permit names exactly the pinned attachment, workload
and replacement instance, and the pinned attachment is the only live one.
It then answers without format authority: the replacement mounts the
existing filesystem and never formats it. A replacement whose volume was
never formatted therefore fails closed at initialization.

Each fenced detach, replacement attach and mount permit is recorded in the
decision journal (`volume_reattached`, rule
`storage.reattach_on_host_loss`).

## Follow-ups

- Host-side usage of managed mounts: hosts may publish only their
  observation subject. Carry usage in `memberstatus`, republish it from the
  controller, feed `SignalSource` and `NodeHeadroomBytes` into placement
  instead of the configured `DiskBytes`, and cordon on critical JetStream
  pressure.
- A per-member desired volume size and a signed grow request to the host
  initializer, so a live member's filesystem grows without waiting for the
  next initializer run.
