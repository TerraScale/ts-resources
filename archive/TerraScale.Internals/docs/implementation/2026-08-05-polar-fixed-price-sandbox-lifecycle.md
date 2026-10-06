# Polar fixed-price sandbox lifecycle proof

## Product boundary

Polar is fixed-price-only until TerraScale has a provider-attributed meter ledger. The
catalog includes an allowlisted Polar product-price ID for each plan interval. Checkout reads
the complete product before and immediately after creation, and lifecycle projection reads it
immediately before its durable update. TerraScale accepts only the exact allowlisted price when
Polar reports a recurring fixed amount equal to the catalog amount/currency and no sibling is
metered or usage-priced. Signed lifecycle payloads and reconciliation snapshots must carry the
same product-price ID and fixed-price metadata. A known metered, usage, unknown, or mismatched
product is dead-lettered or causes reconciliation to fail rather than applying a provider
amount. Local zero overage rates remain a secondary catalog guard; they are not evidence of the
provider product type.

Polar's published API documentation does not offer a conditional product/checkout version,
ETag/If-Match, or checkout-cancellation primitive. Production startup therefore requires
`Payments__Polar__CatalogImmutabilityAdmission=true` after the catalog is placed under the
operational controls in [payment-providers.md](../billing/payment-providers.md#catalog-immutability-admission).
The flag is an attestation, not a claim that independent provider GETs eliminate the residual
between-request race.

This is deliberately fail-closed. TerraScale's operational metering records product usage,
but it is not a ledger that can be attributed to a Polar customer/product/period and then
reconciled against provider invoices. Adding a Polar usage product, an overage rate, or a
usage event submission path is blocked until that ledger and its audit/reconciliation
contract exist.

## Credential-gated contract probe

The focused Payments test contains the non-destructive provider API probe. It runs only when
all three settings are present:

```text
TERRASCALE_POLAR_SANDBOX_RUN_LIFECYCLE_CONTRACTS=true
TERRASCALE_POLAR_SANDBOX_ACCESS_TOKEN_FILE=/absolute/path/to/isolated-polar-sandbox-token
TERRASCALE_POLAR_SANDBOX_PRODUCT_ID=<fixed-price-sandbox-product-id>
```

Use a disposable, owner-private regular file containing a sandbox-only token and a dedicated
fixed-price sandbox product. Do not point the file setting at a production secret, do not
export the token itself, and do not capture test output containing request headers. The guard
does not read the token while deciding whether to skip; the token is read only by the bounded
owner-private file reader after the test has opted in.

Run the probe with:

```bash
dotnet test --project src/Payments/TerraScale.Payments.Tests/TerraScale.Payments.Tests.csproj --no-progress --fail-fast -- --treenode-filter "/*/*/PolarSandboxIntegrationTests/*"
```

It creates a hosted checkout using an idempotency key and validates a subscription read only
when the checkout response already carries a subscription ID. It does not complete checkout,
create a portal session, or mutate a subscription. A portal session requires a separately
provisioned disposable customer after checkout completion. The suite is skipped when any
guard is missing, so ordinary deterministic test runs cannot contact Polar.

## Real-boundary lifecycle runbook

1. Deploy an isolated Platform/AppHost sandbox environment with the sandbox API base URL,
   dedicated file-backed access token and webhook secret, fixed-price product catalog ID,
   publicly reachable HTTPS webhook URL, queue processor, payments database, and data
   protection key persistence. Do not use production URLs, products, queues, or key rings.
2. Run the credential-gated probe above. Save only redacted test result and correlation IDs.
3. Complete the created checkout manually with Polar's documented sandbox payment method,
   then use its resulting disposable customer to create and validate a portal session.
   Confirm the provider delivers its signed lifecycle webhook to the actual
   `/api/v1/billing/polar/webhook` endpoint and that the durable receipt becomes projected.
4. Deliver the same signed event again, then deliver an earlier signed event of the same
   lifecycle. Confirm receipt deduplication and ordering preserve the latest account state.
   The AppHost suite is designed to prove raw signed ingress, queue projection, duplicate/
   ordering handling, invoice/refund projection, and lifecycle status transitions without a
   provider call. It is not executed evidence until its result is recorded below.
5. In the sandbox portal, exercise cancellation, a failed/overdue payment when Polar's
   sandbox supports it, grace-period access, recovery, and refund. For every supported
   provider action, retain redacted provider event IDs plus the matching receipt, account,
   invoice, and reconciliation result. If Polar does not expose a safe public sandbox action
   for a state, record it as provider-limited rather than claiming coverage.
6. Trigger reconciliation only after a subscription exists. Confirm the client snapshot and
   persisted account agree on fixed product, status, period, amount, and currency. A metered
   or unknown product must dead-letter/fail reconciliation instead of changing entitlements.

## Evidence limits and deployment handoff

Payment webhook replay stores an encrypted message only for a dead-lettered receipt and only
up to 30 days; projected messages clear their protected payload immediately. The existing
code checks expiry when an administrator requests replay, but this slice does not provide a
30-day elapsed-time/restart proof or a physical expiry-sweep proof. Treat retention and
cleanup behavior as unverified operational evidence until a deployed environment demonstrates
restart recovery, expiry enforcement, and the selected retention/purge mechanism.

`TerraScale.Orchestrator` must supply the production deployment prerequisites: isolated
secret-file mounts and permissions, durable data-protection keys, a non-ingress internal RPC
layout, public HTTPS ingress only for the signed webhook endpoint, queue/worker availability,
reconciliation scheduling, monitoring/alerts for dead letters and stale reconciliations, and
an auditable retention/expiry sweep policy. This repository does not own or deploy those
resources.

## Service/persistence ordering proof

`PolarReconciliation_DoesNotSuppressDelayedPaidOrRefundInvoiceProjection` uses the real
`PaymentBillingService`, `PolarBillingService`, `PaymentWebhookEventStore`, billing account
store, metadata service, and TerraBase fixture. It persists `order.created`, reconciles the
subscription, then persists delayed `order.paid` and `order.refunded` messages. The assertion
checks that the invoice's own provider-event cursor advances through open, paid, and refunded
states while the payment-status cursor remains untouched by reconciliation. Polar's
subscription HTTP response is the only deterministic transport seam.

This is a service/persistence proof, not raw HTTP ingress proof: the real signed-webhook
endpoint, queue worker, and AppHost topology still require a completed AppHost run before
they can be represented as executed evidence.

`PolarMixedProduct_DeadLettersWebhookAndRejectsReconciliationWithoutProjection` drives the
real `PaymentBillingService` and persistent webhook receipt store with a deterministic typed
Polar transport. The mixed-product checkout cases now invoke the actual
`PaymentBillingService.CreateCheckoutSessionAsync` workflow, proving a known mixed product has
no checkout POST and that its checkout lease is released; a product that becomes mixed after
checkout creation is not returned or persisted; and a known mixed lifecycle event
is durably marked `dead_lettered` without invoice/subscription projection before reconciliation
also fails. `PolarProductReadFailure_RetriesThenDeadLettersAndReplaysAfterProviderRecovery`
proves a provider product-read failure is durably `retrying` before final delivery, becomes an
operator-replayable dead letter on final delivery, and projects after recovery. These tests
make no external Polar or sandbox call.

## Validation recorded for this slice

`TerraScale.Payments.Tests` passed with 44 tests and 2 deliberately skipped credential-gated
sandbox tests. Both Platform and Payments test projects built with zero warnings/errors, and
the focused fixed-price policy test passed. The focused service/persistence ordering, mixed
product/dead-letter, product-read-retry, and earlier raw-AppHost lifecycle tests initialized
the shared AppHost topology but emitted no test result after five minutes; each owned process
tree was stopped and cleaned up. The tests are retained, but their AppHost/fixture execution
and raw ingress proof remain inconclusive. No complete isolated sandbox configuration was
present or used, and no Polar credential or external product/subscription was inspected or
changed.
The lifecycle proof also fences the account identity: checkout creates only a pending durable
session/product/price correlation. A successful signed `checkout.updated` must consume that
exact session before the customer, subscription, and product binding exists. Reordered order
or subscription events and later cross-organization customer/subscription values are
dead-lettered without rebinding. A transient provider product-read error is `retrying` before
the queue's final delivery; the final failed delivery changes the protected receipt to
`dead_lettered`, so an operator replay can project it after the provider recovers.

A pending correlation is never overwritten by a second checkout: another request is rejected
until Polar's supplied expiry, or indefinitely when no expiry is present; an identical provider
idempotency key returns the retained session. A matching checkout delivered after its durable
expiry is dead-lettered before claims or billing projection. Customer and subscription ownership
is a provider-scoped TerraBase compare-exchange claim made before projection. Canceled/revoked
accounts retain their claims for delayed lifecycle events and replay; deletion freezes the claim
IDs, retries cleanup, and writes a deleted account tombstone before organization metadata is
removed. The tombstone fences concurrent webhooks and account-miss updates. Disabled Polar does
not enqueue reconciliation work, open an existing customer's portal, or process queued
reconciliation messages even if a token is configured.

Pending checkout state does not change the active plan, amount, or entitlement limits; the
requested price is applied only by matching signed lifecycle projection. Newly acquired
compare-exchange claims are compensated after a rejected/raced projection or persistence
failure when no durable account binding owns them. Organization deletion performs the same
retryable account cleanup before metadata deletion.

## Source-side qualification gate and redacted evidence

The Payments test project now has a source-side, fail-closed qualification boundary. The
existing `PolarSandboxIntegrationTests` test is deliberately named and treated as an initial
catalog/idempotent-checkout probe: it reads the fixed-price catalog, creates a checkout, and
replays the same idempotency key. It does **not** complete a signed checkout or exercise the
remaining lifecycle. It records every required scenario as `passed`, `failed`, `provider_limited`,
or `not_run`; a run with any `not_run` scenario emits `run_status: incomplete` and fails the
qualification command. A skipped no-credential local run cannot produce qualified evidence.
Consequently, this source change is not evidence that Polar payment lifecycle qualification is
complete.

The live boundary accepts only the following non-secret settings. The token is never accepted
from an environment variable; the preflight opens the access-token path only for descriptor
validation and does not read its contents. The bounded owner-private reader is used only after
the opted-in preflight passes.

```bash
set -eu
export TERRASCALE_POLAR_SANDBOX_RUN_LIFECYCLE_CONTRACTS=true
export TERRASCALE_POLAR_SANDBOX_ACCESS_TOKEN_FILE=/run/terrascale/polar/lease-qualification-01/access-token
export TERRASCALE_POLAR_SANDBOX_PRODUCT_ID=<fixed-price-sandbox-product-id>
export TERRASCALE_POLAR_SANDBOX_API_BASE_URL=https://sandbox-api.polar.sh
export TERRASCALE_POLAR_SANDBOX_CHECKOUT_SUCCESS_URL=https://<isolated-qualification-host>/checkout/success
export TERRASCALE_POLAR_SANDBOX_CHECKOUT_RETURN_URL=https://<isolated-qualification-host>/checkout/return
export TERRASCALE_POLAR_SANDBOX_WEBHOOK_URL=https://<isolated-qualification-host>/api/v1/billing/polar/webhook
export TERRASCALE_POLAR_SANDBOX_EVIDENCE_PATH=/var/lib/terrascale/polar-qualification/lease-qualification-01.json
export TERRASCALE_POLAR_SANDBOX_CLEANUP_DISPOSITION=delete-after-run
export TERRASCALE_POLAR_SANDBOX_LEASE_ID=lease-qualification-01
export TERRASCALE_POLAR_SANDBOX_SOURCE_REVISION="$(git -C /workspaces/TerraScale/TerraScale.Internals rev-parse HEAD)"
export TERRASCALE_WORKSPACE_ROOT=/workspaces/TerraScale
install -d -m 700 /var/lib/terrascale/polar-qualification
test "$(stat -c '%a' "$TERRASCALE_POLAR_SANDBOX_ACCESS_TOKEN_FILE")" = 600

dotnet test \
  --project src/Payments/TerraScale.Payments.Tests/TerraScale.Payments.Tests.csproj \
  --no-progress --fail-fast -- \
  --treenode-filter "/*/*/PolarSandboxIntegrationTests/*"
```

The source revision must be the full 40-character Git commit. The evidence directory must be
outside `/workspaces/TerraScale` and every product repository,
must have owner-private ancestors, and must not already contain the target file. The writer
uses a same-directory temporary file, owner-private mode, flush-to-disk, and an atomic no-replace
rename; an existing regular file or symlink is never overwritten. Evidence contains only the
source revision, the fixed `polar-sandbox` classification, allowlisted scenario/status and UTC
timestamps, SHA-256 provider-identifier fingerprints, cleanup state/lease identifier, and
bounded provider-limited action codes. It never stores a token path/value, bearer header,
webhook secret, raw payload, card/customer data, full URL/query, or exception text.

Before this command, the billing owner must hold the sandbox account lease identified by the
safe lease ID above. The lease must cover one disposable organization/customer and any
subscription/order resources created by the run, with authority to delete or revoke them. For
the full matrix, acquire an exclusive `AspireTopologyLease` for the isolated AppHost topology
(Platform, queue worker, payments database, data-protection keys, and HTTPS webhook ingress)
before starting the topology; release it after the run and record whether cleanup completed.
The token file is a sandbox-only owner-private mount. The webhook secret belongs in the isolated
AppHost runtime secret store and is never exported to this test or copied into evidence.

The source probe cannot return success while the matrix is incomplete. This packet intentionally
does not provide a manual evidence-edit path: the evidence file is immutable and the current
source runner remains an initial probe. A future bounded executable lifecycle runner must emit a
new evidence file through the same allowlisted writer after the human-provided boundary exists;
until that runner is implemented, the remaining signed checkout, subscription create/update/active,
duplicate/out-of-order, provider-supported `past_due` and recovery, cancellation/revocation,
paid/refund, reconciliation, protected DLQ/replay, and cleanup/disposition scenarios remain
unqualified. If a future runner finds that Polar does not expose a safe sandbox action, it must
mark that scenario `provider_limited` with a bounded action code; never mark it green or infer it
from a local test.

## Resumable bounded lifecycle runner

`PolarSandboxQualificationLifecycleTests` is a separate, explicitly opted-in runner for the
HN-002 owner workflow; it is not part of an ordinary developer test run. In addition to the
initial-probe inputs, the billing owner supplies owner-private regular files for the Platform
administrator session and the one-action-per-invocation input, plus an owner-private journal
path outside the repository/workspace, isolated Platform HTTPS origin, disposable organization,
and plan ID. The runner accepts these settings only through the following names:

```text
TERRASCALE_POLAR_SANDBOX_JOURNAL_PATH
TERRASCALE_POLAR_SANDBOX_ACTION_FILE
TERRASCALE_POLAR_SANDBOX_PLATFORM_API_BASE_URL
TERRASCALE_POLAR_SANDBOX_ADMIN_SESSION_FILE
TERRASCALE_POLAR_SANDBOX_ORGANIZATION_ID
TERRASCALE_POLAR_SANDBOX_PLAN_ID
```

The journal is append-only JSONL, held with an exclusive file lock for the full invocation.
It is never auto-broken after a stale process: a second runner must fail closed. Each record
binds the exact full source revision and lease ID, chains a SHA-256 record hash to the prior
record, and uses monotonic states. Resume rejects a partial final line, hash tampering,
reordering, schema mismatch, source mismatch, or lease mismatch. It contains only fixed state
and action codes, timestamps, scenario status, and SHA-256 fingerprints of provider/session/
subscription/webhook identifiers. It never records raw action input, paths, bearer/admin
sessions, URLs, provider payloads, provider secrets, or exception text.

The action file is an owner-private, non-symlink JSON object. Its allowed actions are bounded:
`checkout_completed` (with a subscription ID), `duplicate_order_observed` (with a webhook event
ID), `past_due_recovered`, `subscription_cancelled`, `order_refunded`, `dead_letter_replayed`
(with a webhook event ID), and `cleanup_completed`. The runner pauses rather than inferring a
provider-hosted checkout, duplicate/order delivery, failure/recovery, cancellation, refund,
DLQ/replay, or cleanup action. Polar access is limited to catalog and subscription reads;
TerraScale account, invoice, checkout, webhook receipt, dead-letter, and replay observations
use typed public .NET SDK billing/administration APIs.

After cleanup, terminal evidence is committed through the existing immutable writer exactly
once. It cannot qualify the current implementation: the runner records
`reconciliation_public_capability_missing` as a provider-limited reconciliation scenario and
emits incomplete evidence. There is no manual green override. This remains blocked until the
producer exposes a Dashboard-agnostic public reconciliation trigger/status capability and the
typed .NET SDK exposes the matching contract; then the producer must land compatibly before a
runner update can remove this bounded blocker.

Scan the finished evidence without printing its contents or values:

```bash
if rg -n -i --pcre2 'access[_-]?token|bearer|webhook[_-]?secret|raw[_-]?payload|card|customer|https?://|\?|exception' \
  "$TERRASCALE_POLAR_SANDBOX_EVIDENCE_PATH" >/dev/null; then
  echo 'Polar evidence secret-safety scan failed' >&2
  exit 1
fi
```

This gate remains dependent on HN-002: a billing owner must provide the isolated Polar Sandbox
product, webhook registration, least-privilege credential, disposable account lease, and safe
provider actions. No credential, external product, customer, subscription, webhook, or cloud
resource was inspected or changed while implementing or testing this source boundary.
