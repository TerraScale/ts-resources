# Payment provider configuration

TerraScale supports Polar and Stripe behind the same public checkout, customer portal,
billing-account, invoice, webhook queue, and reconciliation flows. Polar is the default
for new billing accounts. Existing accounts continue through their recorded provider,
and a caller can select a catalog price belonging to either provider.

## Provider selection

Billing customers, payment methods, subscriptions, invoices, and provider history belong to
an Organization. TerraScale never creates an individual provider customer or collects a
payment method to verify a User. A Developer Organization becomes Active without provider
billing. A new paid Organization remains BillingPending until its initial checkout is
confirmed, and it cannot create Projects, Invitations, Application credentials, or billable
resources while pending.

An Organization Owner with Fresh authentication may start, resume, or cancel initial billing.
Only one unexpired checkout attempt may exist for an Organization and selected plan. Rejected
or cancelled attempts remain retryable for seven days. An upgrade from Developer keeps the
Organization Active with Developer limits until the provider confirms the paid plan.

Set the default provider with:

```text
Payments__Provider=polar
```

Accepted values are `polar` and `stripe`. Omitting the setting selects `polar`. To keep
Stripe as the default in an environment, set `Payments__Provider=stripe` explicitly.
Once an organization has provider billing state, checkout and portal operations continue
through that persisted provider unless an operator completes a supported migration.

Each paid plan can store both Polar product IDs and Stripe price IDs. The public pricing
response exposes `provider`, `monthlyPriceId`, and `annualPriceId` for the configured
provider, plus the provider-specific IDs for administration. A checkout request can use
the provider-neutral `planId` and `billingInterval`; an explicit Polar product ID, Stripe
price ID, or `provider` selects that real gateway when the organization has no persisted
provider state.

## Polar

Polar is **fixed-price only**. Each catalog product must include its allowlisted Polar product
price ID. TerraScale reads and verifies the complete Polar product before checkout and again
immediately after checkout creation; it never returns or persists a checkout known to select a
metered, usage, unknown, or mismatched product. Signed lifecycle payloads and reconciliation
snapshots must carry the exact verified price metadata, and TerraScale reads the complete
product immediately before durable lifecycle projection. A known invalid product dead-letters
the receipt or fails reconciliation rather than applying a provider amount. Local zero overage
rates are a secondary catalog guard, not proof of the provider product type.

TerraScale records operational usage, but it does not yet have the provider-attributed meter
ledger required to submit, reconcile, and audit usage charges. Do not configure Polar usage
products or non-zero operation/storage overages until that ledger is deployed and its provider
contract is added.

Configure the Platform workload with Orchestrator-managed secret file paths and URLs:

```text
Payments__Polar__AccessTokenFile
Payments__Polar__WebhookSecretFile
Payments__Polar__PreviousWebhookSecretFile
Payments__Polar__Enabled=true
Payments__Polar__CheckoutSuccessUrl
Payments__Polar__CheckoutReturnUrl
Payments__Polar__PaymentMethodVerificationReturnUrl
Payments__Polar__PortalReturnUrl
Payments__Polar__CatalogImmutabilityAdmission=true
```

`Payments__Polar__ApiBaseUrl` defaults to `https://api.polar.sh`, and
`Payments__Polar__WebhookToleranceSeconds` defaults to 300 seconds. Each secret file must
be a regular owner-private Unix file (no group/other permissions), contain one non-empty
secret (a final newline is ignored), and never be paired with the equivalent raw setting.
Raw secret settings are accepted only in explicit Development or Testing environments;
production fails startup for missing, ambiguous, or raw secrets whenever
`Payments__Polar__Enabled=true`. Polar must be explicitly enabled when it is the default
provider, and a disabled Polar gateway cannot be selected by an explicit provider, catalog
price, webhook, or reconciliation message. Enabled Polar also requires absolute HTTPS API,
checkout, and portal URLs without credentials or fragments.

`PaymentMethodVerificationReturnUrl` returns Organization card enrollment to the
onboarding flow. It falls back to `PortalReturnUrl` for existing deployments, while
new deployments should configure the dedicated URL so the ordinary billing portal can
keep its own return destination.

### Catalog immutability admission

Polar's public product documentation says billing cycle and pricing type cannot change after
creation, but a fixed price amount can change. Its public checkout API documents ordinary
checkout and product reads, not a conditional checkout/product version, ETag/If-Match contract,
or checkout cancellation operation. `CatalogImmutabilityAdmission=true` is therefore required
outside Development and Testing before a Polar-selected Platform can start. It is an explicit
operational admission, not an atomic provider lock.

Set it only after restricting Polar product editing to a separate change-controlled role,
keeping the Platform token out of product-management workflows where Polar permissions permit,
and treating every catalog change as a new reviewed product/price rollout. Do not mutate a
catalog product in place. The preflight, post-checkout, and pre-projection reads detect a
known change but cannot close a mutation that happens between independent provider requests.
If that residual race is suspected, stop new checkouts, archive the affected product through
the approved provider change process, and inspect/dead-letter receipts before any replay.

Register this production webhook endpoint in Polar:

```text
POST https://api.terrascale.tech/api/v1/billing/polar/webhook
```

Subscribe it to checkout completion (`checkout.updated`), the subscription lifecycle events (`subscription.created`,
`subscription.updated`, `subscription.active`, `subscription.canceled`,
`subscription.uncanceled`, `subscription.revoked`, and `subscription.past_due`) and the
order lifecycle events (`order.created`, `order.updated`, `order.paid`, and
`order.refunded`). Store the endpoint secret in the file referenced by
`Payments__Polar__WebhookSecretFile`.

Polar webhooks follow Standard Webhooks. TerraScale requires `webhook-id`,
`webhook-timestamp`, and `webhook-signature`, verifies the HMAC-SHA256 signature over the
unaltered request bytes, rejects stale timestamps, and compares signatures in constant
time before enqueueing an event. Bodies are limited to 262,144 bytes by default through
`Payments__Polar__WebhookMaxBodyBytes` (valid range 1,024–1,048,576).

A signed Polar event cannot establish an organization binding from metadata alone. The
authenticated checkout flow first persists a pending session/product/price correlation;
only a successful `checkout.updated` for that exact, unexpired session consumes it and establishes the
customer, subscription, and product binding. Afterwards each lifecycle event and
reconciliation snapshot must exactly match the durable binding. Reordered order or
subscription events, duplicate/unrelated checkout sessions, and cross-organization customer
or subscription injection are dead-lettered without projection.

Only one pending Polar checkout correlation is retained per organization. A different checkout
request is rejected while that session is still unexpired (or while Polar supplied no expiry);
the same provider idempotency key returns the retained session instead of replacing it. This
keeps the original charged session consumable. Non-empty Polar customer and subscription IDs
are also claimed through provider-scoped TerraBase compare-exchange ownership before durable
projection. Those claims survive cancellation/revocation so delayed events and operator replay
remain fenced; they are released only when the owning billing account is deleted. A late
matching checkout is dead-lettered before a claim or billing projection is changed.

Disabled Polar also suppresses reconciliation scheduling, even when a token is present.

Creating a Polar checkout does not alter the billing account's active plan, amount, limits, or
entitlements. The requested product/price exists only in the pending checkout correlation and
provider metadata until a matching signed checkout or subscription lifecycle projection applies
the provider-verified plan. An expired or abandoned pending session therefore remains on the
current active plan. A newly created paid Organization has no active plan and remains
BillingPending until confirmation. A Developer upgrade remains Active on Developer limits.

Starter and Pro may grant one 30-day trial per Organization. TerraScale derives eligibility
from durable Organization billing history. Replacing a payment method does not restore trial
eligibility.

Compare-exchange ownership is acquired before the account projection. If a concurrent account
update rejects the event, or persistence fails before binding, only IDs newly acquired by that
attempt are released after checking the durable account state. Organization deletion first marks
the billing account as deleting and freezes its claim IDs. It retries claim cleanup until it can
write a terminal deleted tombstone, then removes organization metadata. Deleting and deleted
accounts reject webhook projection and cannot be recreated by an account-miss update.

## Stripe

Stripe remains fully supported. Configure it with `Payments__Provider=stripe` when it
should be the environment default, or leave Polar as the default and initiate checkout
with a Stripe catalog price. See [stripe-webhooks.md](stripe-webhooks.md) for the Stripe
secrets and endpoint registration.

## Hosted portal setup

TerraScale deliberately delegates saved payment methods, invoices, cancellations,
subscription upgrades and downgrades, seat changes, and provider proration to each
provider's hosted customer portal.

- In Polar, enable subscription changes and seat management in the customer portal and
  select the intended proration behavior.
- In Stripe, enable payment-method updates, invoice history, cancellation, plan switching,
  and quantity changes in the customer portal configuration and select the intended
  proration behavior.

Configure every TerraScale catalog plan and interval as an allowed portal product before
shipping it. Validate both portals in provider sandboxes after any catalog or portal
configuration change.

## Operations

Both providers enqueue verified events on `payments.webhook` and reconciliation work on
`payments.reconciliation`. Queue messages carry a provider field, use provider-scoped
deduplication keys, and move invalid lifecycle projections to the payment webhook dead
letter queue after bounded retries. A permanent provider/event receipt records deliveries,
projection attempts, conflicts, ordering cursors, terminal state, and an encrypted,
time-limited replay payload. Reconciliation schedulers query only accounts owned by their
provider.

Never switch an organization by rewriting its persisted provider. An active subscription
must be managed through its existing provider portal; webhook projection rejects a
second provider while the other provider has a subscription.

Monitor the `terrascale.billing.webhooks` counter by `payment.provider`,
`payment.event_type`, and `payment.outcome`. Alert on sustained dead-letter, failure,
conflict, or stale-event outcomes. The `payment_queues` readiness check reports webhook
and reconciliation backlog, redelivery, and dead-letter counts; missing queues or
processors fail readiness and retained dead letters degrade it.

Platform administrators can inspect receipts through:

```text
GET  /api/v1/admin/billing/webhooks/dead-lettered
GET  /api/v1/admin/billing/webhooks/{provider}/{eventId}
POST /api/v1/admin/billing/webhooks/{provider}/{eventId}:replay
```

The admin endpoints require a current verified TerraScale user with the
`terrascale_admin` global role. Replay additionally requires a fresh verified session
and an `Idempotency-Key`; only dead-lettered receipts with an available protected payload
can be replayed. Replays record the authenticated user and session. Never publish raw
payment messages to NATS.

For an incident, first confirm provider delivery and the configured signing secret, then
inspect the permanent receipt and application trace. Correct the configuration or
referenced catalog/account data before replaying the dead-lettered receipt. Subscription
reconciliation can repair provider snapshots; use receipt replay for invoice, refund, and
other event-only projections.

Rotate a signing secret without an acceptance gap by placing the old value in the file
referenced by `PreviousWebhookSecretFile`, deploying the new value through
`WebhookSecretFile`, switching the provider endpoint to the new secret, confirming signed
deliveries, and then removing the previous value. TerraScale verifies both during the
overlap and never logs either value.

## Local verification

AppHost uses Stripe as its safe default and explicitly disables Polar so routine local startup
does not require a valid Polar admission. DevHost uses the configured provider and the same
provider clients as production.
Configure sandbox/test credentials, webhook secrets, product or price IDs, and optional
API base URLs through the `Payments__Polar__*` or `Payments__Stripe__*` settings above.
DevHost forwards those settings from its systemd environment to every Platform workload;
AppHost forwards them from its process environment. Neither runtime starts a payment
emulator.

Focused client and webhook-signature tests use test-local HTTP stubs and run with:

```bash
dotnet test src/Payments/TerraScale.Payments.Tests/TerraScale.Payments.Tests.csproj --no-restore
```

The AppHost integration suite is designed to cover signed webhook queueing, ordering, replay,
subscription projection, refunds, shared invoice state, and customer notification without
calling an external provider. Treat those as executed evidence only after a completed suite
result is recorded in the lifecycle implementation report. Credential-gated tests create
hosted checkout sessions in the Stripe and Polar sandboxes. The Polar lifecycle probe runs
only when all of these are set:

```text
TERRASCALE_POLAR_SANDBOX_RUN_LIFECYCLE_CONTRACTS=true
TERRASCALE_POLAR_SANDBOX_ACCESS_TOKEN_FILE=/absolute/path/to/isolated-polar-sandbox-token
TERRASCALE_POLAR_SANDBOX_PRODUCT_ID=<fixed-price-sandbox-product-id>
```

The access-token file must be a dedicated owner-private sandbox credential, never a
production credential file. The test only reads that named file through the bounded secret
reader and never logs its contents. It creates a hosted checkout and retrieves a subscription
only if Polar returns one without completing payment; it does not create, cancel, pay, refund,
or mutate a provider subscription. Portal proof requires a separately provisioned disposable
customer after checkout completion. See the lifecycle runbook before performing that proof.
