# ts-infra

This repository manages shared OCI services with OpenTofu. Its managed service is
currently Email Delivery: the approved sender and domain, the domain DKIM key,
and one SMTP credential. Nonsecret inputs live in `infra.tfvars`.

Regional foundation, controller startup, and cell expansion follow the
[manual region bootstrap runbook](https://git.terrascale.tech/TerraScale/ts-orchestrator/src/branch/main/docs/region-bootstrap.md).
The existing GRU foundation is operated through the manual process. It is
outside this repository's OpenTofu state.

## Email Delivery

`email.tf` manages:

| Resource | Address |
| --- | --- |
| Sender | `oci_email_sender.sender["noreply@terrascale.tech"]` |
| Domain | `oci_email_email_domain.domain["terrascale.tech"]` |
| DKIM | `oci_email_dkim.dkim["terrascale.tech"]` |
| SMTP credential | `oci_identity_smtp_credential.email_delivery` |

The provider uses the tenancy home region. The SMTP password is a sensitive
OpenTofu output. It is held in encrypted state and must not be copied into
source control, logs, or PR comments. Renaming the credential resource rotates
its password.

## DNS for terrascale.tech

The Cloudflare zone is maintained manually. Publish the merged SPF TXT value
at `terrascale.tech`:

```text
v=spf1 include:_spf.purelymail.com include:mailgun.org include:rp.oracleemaildelivery.com ~all
```

Publish the OCI DKIM CNAME with Cloudflare proxying disabled:

```text
terrascale-tech-dkim._domainkey.terrascale.tech CNAME terrascale-tech-dkim.terrascale.tech.dkim.gru1.oracleemaildelivery.com
```

`dkim_dns_records` and `dkim_lifecycle_states` are OpenTofu outputs. OCI may
report `NEEDS_ATTENTION` until the CNAME resolves, then `ACTIVE` on its next
check. The current record can also be read with `oci email dkim get` using the
email domain and DKIM OCIDs.

## State and CI

Configuration lives on `main`. The encrypted `terraform.tfstate` and its
`state-control.json` live on the separate `state` branch. The Forgejo Actions
`ts-infra-state-sync` deploy key may push only that branch. OpenTofu encrypts
state with PBKDF2 and AES-GCM using the `TF_STATE_PASSPHRASE` Forgejo secret;
its backup is at `~/.config/ts-infra/tf-state-passphrase`. Losing both copies
makes the state unrecoverable.

`scripts/state-store.cs` reserves the exact state tip before an apply and
publishes the resulting encrypted state with an immutable receipt. A failed or
interrupted apply blocks the next automatic apply until a reviewed recovery.
Never run `tofu apply` or alter production state locally. PR checks have no OCI
or state credentials.

For passphrase custody, rotation, and failed-apply recovery, follow the
[state recovery runbook](docs/state-recovery.md).

The `main` push workflow restores the encrypted state, checks that it contains
exactly the four email resources and outputs above, and saves an OCI plan. Its
gate permits only `no-op` or in-place `update` actions on those same identities.
Creates, replacements, deletes, regional resources, and unexpected outputs
fail before reservation. The workflow applies the verified saved plan, then
publishes the encrypted state and receipt. A failed apply publishes its
observed state with phase `recovery-required` for a separate reviewed recovery.

The former regional foundation state was relinquished with OpenTofu
`removed` blocks using `destroy = false`. The handoff did not destroy its 24
OCI resources; one local propagation marker was removed from state. Previous
encrypted state snapshots and immutable receipts remain in the `state` branch's
Git history.
Changes to regional foundation or controller resources follow the manual
region bootstrap runbook linked above.

## Local checks

Run local builds at lower priority; CI builds use normal priority.

```sh
export TF_VAR_state_passphrase=test-only-state-passphrase-not-a-credential
nice -n 19 dotnet run scripts/state-store.tests.cs -- --minimum-expected-tests 28
nice -n 19 dotnet run scripts/state-recovery-drill.cs
nice -n 19 python3 -m unittest scripts/test_verify_email_plan.py
nice -n 19 tofu init -backend=false -lockfile=readonly
nice -n 19 tofu fmt -check -recursive
nice -n 19 tofu validate
```

The lock file pins the OCI provider. Local checks use a dummy state passphrase
and do not restore the production state branch.
