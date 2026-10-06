# State custody and recovery

Stop automatic applies when state publication or an apply is uncertain. Keep
production recovery in reviewed Forgejo Actions on `main`; never run a local
`tofu apply`/`destroy`, hand-edit production state, or roll back the `state`
branch to make the next apply pass.

## Passphrase custody

The current passphrase has two copies:

| Copy | Location | Purpose |
| --- | --- | --- |
| CI | Forgejo repository Actions secret `TF_STATE_PASSPHRASE` | Workflow supplies it as `TF_VAR_state_passphrase` |
| Operator backup | `~/.config/ts-infra/tf-state-passphrase` | Recovery if the Forgejo copy is lost |

Keep the backup outside Git with owner-only access (directory mode `0700`, file
mode `0600`). Do not put passphrases, decrypted state, SMTP passwords, or plan
contents in logs, artifacts, tickets, or PR comments. Record custody checks and
key versions without recording the key itself. A masked Forgejo secret is not
a readable backup in the web interface.

### Loss of a copy

1. Pause applies and establish which copy still exists. Treat possible exposure
   as compromise and follow the rotation procedure below.
2. **Forgejo copy lost:** the backup custodian restores
   `TF_STATE_PASSPHRASE` through Forgejo's secret settings using the exact backup
   value. Do not generate a new value: it cannot decrypt the existing state.
3. **Backup lost:** the repository secret administrator must arrange a reviewed,
   restricted CI procedure to transfer the surviving value directly to the
   custodian through a private channel, recreating the same backup location and
   permissions. The normal workflow has no secret-export command; never print
   the value or upload it as an artifact. If secure transfer is unavailable,
   keep applies paused until a reviewed rotation establishes a new backup.
4. Verify the restored copy through a reviewed CI decryption check of the exact
   current encrypted revision, reporting only success/failure. Confirm the
   backup exists and restrict access before resuming normal CI.
5. **Both copies lost:** encrypted snapshots and Git history cannot recover the
   passphrase. State is unrecoverable with this custody setup. Keep applies
   stopped; declare a separate infrastructure/state reconstruction incident
   rather than inventing empty state or applying an old snapshot.

### Rotation, including old Git history

Changing the Forgejo secret alone is not rotation: it makes the current state
unreadable. There is no rotation command in `scripts/state-store.cs` and the
current encryption configuration has no old-key fallback.

1. Pause automatic applies, resolve any outstanding reservation/recovery first,
   and record the exact `state` tip and its verified receipt. Preserve the old
   passphrase in two restricted, versioned copies; record their actual locations in a
   private operator record before replacing either current copy.
2. Review a CI-only OpenTofu encryption migration that can read using the old
   key and write using the new key. Prove it with synthetic fixtures first.
   Keep encryption enforced; the published envelope must satisfy the helper's
   `key_provider.pbkdf2.state_key` metadata contract. Use injected secrets, not
   literal key values in configuration. This requires reviewed migration code,
   not a normal workflow rerun.
3. In that reviewed CI procedure, re-encrypt the current state without changing
   resource identities or lineage, regressing the serial, or changing the
   provider lock. Publish the new encrypted bytes, matching digests, control,
   and a new receipt together as a child of the exact verified tip. Preserve
   existing receipts and stop if the remote tip changes.
4. Verify in CI that the new key decrypts the published revision and passes the
   email state gate. Update `TF_STATE_PASSPHRASE` and
   `~/.config/ts-infra/tf-state-passphrase` to the new value before resuming
   applies; remove temporary old-key access from CI after verification.
5. Retain old keys for snapshots encrypted with them, including immutable
   receipts and earlier `state` branch commits. Record which revisions need
   each key and verify an old snapshot privately in reviewed CI. Rotation does
   **not** re-encrypt old Git objects or revoke a leaked old key. If the old key
   was exposed, assess secrets in historical state (including the SMTP
   password); their rotation is a separate reviewed operation. Never rewrite
   history or discard the old key as an incidental part of this procedure.

## Publication protocol

The authoritative revision is the remote `refs/heads/state` tip, not the
source checkout or the last green workflow. It contains `terraform.tfstate`,
`.terraform.lock.hcl`, and `state-control.json`.

| Control phase | Meaning | Automatic apply |
| --- | --- | --- |
| `ready` | Completed success with matching receipt | Allowed after normal validation |
| `applying` | Exact revision reserved; result not yet recorded | Blocked |
| `recovery-required` | Recorded `failure`, `cancelled`, or `skipped` outcome | Blocked |

`restore` verifies control and receipt before writing encrypted state privately
to the CI workspace. `reserve` checks the exact restored tip, source SHA, state
bytes, and provider lock, then publishes an `applying` child commit before any
apply. `finish` publishes the observed encrypted state, control, and receipt
atomically. It requires the same lineage, a serial at least as large as the
reserved state's, and an unchanged lock. Equal serials are permitted; a failed
apply may still have changed infrastructure or advanced state.

Receipts live at `recovery/<run>-<attempt>-<nonce>/` with `terraform.tfstate`,
`.terraform.lock.hcl`, and `metadata.json`. Metadata binds the full session
(`run`, `attempt`, `nonce`, `source`, `base`, `reservation`, `readOnly`, and
schema version), outcome, and state/lock SHA-256 digests. `ready` requires a
`success` receipt; `recovery-required` requires a non-success receipt. Archived
state and lock must byte-match the canonical files. A reservation in
`applying` has no final receipt yet.

Publication uses an exact expected-tip lease and a single-parent child commit;
it cannot overwrite a concurrent revision. A lost push acknowledgement is
checked by fetching the remote tip. An exact receipt retry is idempotent,
including when a later run has advanced state; it does not replace that later
state. Conflicting receipt contents are rejected.

## Failed-apply recovery runbook

### 1. Freeze and preserve evidence

Stop dispatching/rerunning applies and have the operator pause automatic apply
execution. Confirm no apply is still running before any recovery write. Record
the failed workflow URL, source SHA, run/attempt, reservation and published SHAs
from the fixed diagnostics. Record where failure occurred: before reservation,
during apply, or during publication.

If the isolated runner still exists, have its custodian preserve encrypted
working state and session evidence privately before disposal. The normal
cleanup removes the saved plan, session JSON, and SSH files; it does not upload
recovery artifacts. Do not assume a cancelled/lost runner's files are available,
or copy decrypted state into an incident record.

### 2. Inspect the exact remote revision in reviewed CI

Use a reviewed diagnostic workflow with `restore --read-only` and its own
private session path. This option exists in `scripts/state-store.cs`, but is
not wired as a recovery job in `.forgejo/workflows/infra.yml`. It remains a CI
operation and cannot reserve or publish. It accepts valid `applying` and
`recovery-required` control; malformed metadata, digest mismatches, and missing
or mismatched completed receipts still fail closed.

Run this step in that reviewed Forgejo CI job after checking out the exact
source and configuring the existing trusted SSH access to the state remote:

```sh
set -eu
umask 077
dotnet run scripts/state-store.cs restore --read-only \
  --session "$RUNNER_TEMP/ts-infra-recovery-session.json"
```

Use real CI identities; do not impersonate CI by setting these locally:

| Environment | Value |
| --- | --- |
| `GITHUB_ACTIONS` | Forgejo-provided `true` |
| `GITHUB_RUN_ID`, `GITHUB_RUN_ATTEMPT` | Current numeric run/attempt; attempt defaults to `1` |
| `SOURCE_SHA` | Exact reviewed source SHA (`${{ forgejo.sha }}`), equal to checkout `HEAD` |
| `GITHUB_EVENT_NAME`, `GITHUB_REF` | Use reviewed `workflow_dispatch` on `refs/heads/main`; these are enforced for writes |
| `RUNNER_TEMP` | Runner's private writable temporary directory for the session |

The restore needs authenticated Git access, not the passphrase. Inject
`TF_VAR_state_passphrase` from `TF_STATE_PASSPHRASE` only into the subsequent
decryption/validation steps. Keep the session private and remove it during
cleanup. This read-only session cannot be reused for a recovery write.

Verify SHA-256 over the actual encrypted state and lock bytes against control
and, for completed phases, receipt metadata. Verify session identity, outcome,
archived byte equality, and the reservation's single parent matching `base`.
Compare final envelope lineage and serial with the reservation: same lineage,
nondecreasing serial, unchanged lock. The helper checks envelope structure,
not decryption; use enforced OpenTofu AES-GCM decryption in CI and
`scripts/verify-email-plan.py state` to verify the four email identities and
expected outputs without printing state.

### 3. Classify publication before choosing a recovery

| Observation | Required action |
| --- | --- |
| Failed before reservation; remote is valid `ready` | Fix the pre-apply failure and use a fresh normal CI plan after review |
| Remote has the exact completed receipt despite publication error | Treat publication as landed; `ready` can resume after verification, while `recovery-required` stays blocked |
| Remote remains `applying` | Result is unresolved; preserve the original session and observed encrypted working state if available |
| Completed control has missing/mismatched receipt or digests | Stop; investigate corruption and preserve evidence, including existing receipt history |
| Remote changed concurrently | Review the newer revision; never overwrite it with the failed run's candidate |

When the original invocation still has its exact session and state, a reviewed
retry of **only** `finish` can publish against the unchanged reservation or
recognize an identical receipt. Preserve the actual outcome. The CLI binds the
session to run, attempt, and source: a new job attempt cannot simply reuse it.
Do not rerun `apply`, relabel failure as success, or assume a whole-workflow
rerun can repair publication.

### 4. Review reconciliation and the recovery write

Compare observed encrypted state, reservation, receipts, and actual resource
identities in reviewed CI. A failed apply may have partly succeeded; the
pre-apply snapshot is evidence, not a rollback candidate. If runner state or a
receipt is missing, establish current provider reality through reviewed CI
before constructing recovered state. Never lower the serial, change lineage,
or fabricate a receipt to hide uncertainty.

Have the human reviewer approve the exact recovery input revision, evidence,
resource identities, reconciliation plan, and intended publication. The
existing helper exposes only `restore`, `reserve`, and `finish`: **there is no
unlock, recovery-complete, or administrative reset command**. Standard
`workflow_dispatch` uses the same blocked restore path.

Use the explicit recovery-completion transition in the fixture-only
[drill](../scripts/state-recovery-drill.cs) as the template for an
incident-specific, human-reviewed CI procedure:

1. Pin the approved current remote tip and verify its evidence. Validate the
   reconciled encrypted state against it: same lineage, nondecreasing serial,
   unchanged lock, and the four approved email identities.
2. Create a fresh attributable recovery session with that tip as `base`, the
   reviewed source SHA, current CI run/attempt, a fresh nonce, and
   `readOnly = false`. Preserve the failed receipt byte-for-byte; never relabel
   its outcome or reuse the read-only diagnostic session.
3. Use `StateStore.Commit` to create an `applying` reservation as a single-parent
   child of the approved tip, containing the verified reconciled encrypted
   state, unchanged lock, and their matching digests. Validate it with
   `StateStore.Inspect(..., readOnly: true)`
   and publish it with `StateStore.PublishCommit(expectedTip, reservation)`.
   Record that reservation SHA in the fresh session. This explicit reviewed
   transition must not be exposed as an automatic bypass of `Reserve`.
4. Place the verified reconciled encrypted state and unchanged lock in the CI
   workspace, then use `StateStore.Finish(recoverySession, "success")`. It checks
   lineage, serial, lock, session, and exact reservation before atomically
   publishing canonical state, `ready` control, and a new matching immutable
   receipt. Verify the remote result. If the tip changes or evidence is
   insufficient, stop and review again; an interrupted recovery stays blocked.

The drill performs this transition only on synthetic state in its temporary
remote. Review its session construction and checks when adapting it to the
approved incident; it is not a production unlock command. Keep ordinary
applies paused until reviewed CI reconciliation and verification succeed.

### 5. Verify and resume

In CI, restore the published revision through the normal validation path.
Confirm `ready`, matching digests and receipt, successful decryption, and the
email state gate. Save and review a fresh plan against that exact state; retain
the normal no-create/no-replace/no-delete gate. Record the recovery source/run
and state revision in the incident, then allow normal CI execution again.
Discard the failed run's saved plan; never reuse a stale plan or force-push an
older state revision.

## Local recovery drill

From the repository root:

```sh
nice -n 19 dotnet run scripts/state-recovery-drill.cs
```

The drill reuses the StateStore library with synthetic fixtures, an isolated
temporary Git `state` branch, and OpenTofu local state encryption. It needs
Git, .NET, Python3, and OpenTofu; it does not need production secrets. `PATH`
must resolve installed binaries that work with a private `HOME`. If a local
runtime manager uses shims that depend on user configuration, put its installed
Python and .NET binary directories first on `PATH` for this command. Both CI
workflows run it before production credentials are configured. It never restores the
live state branch or runs apply/destroy. Its runnable self-checks cover
exact-revision canonical and archived state decryption, re-encryption with
unchanged lineage and serial, receipt/digest verification, wrong-key and
ciphertext-tamper rejection, and reviewed recovery that preserves the original
failure receipt. Private temporary data is removed on exit.

One deadline covers each subprocess and its input/output pipes. Regression
fixtures check cleanup when a parent exits before a descendant closes those
pipes, input writes block, or output exceeds its limit. Negative checks require
the expected policy/integrity error or encryption diagnostic; unrelated tool
failures cannot satisfy them, and captured diagnostics are never printed.

Passing checks the fixture recovery scenarios, not production decryption or
resource reality; a live recovery still requires the reviewed CI procedure
above.
