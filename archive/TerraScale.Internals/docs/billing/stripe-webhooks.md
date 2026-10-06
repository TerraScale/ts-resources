# Stripe Webhook Registration Runbook

Stripe is the optional payment provider. Polar is the default; set
`Payments__Provider=stripe` to make Stripe the default for new billing accounts. Stripe
catalog price IDs can also select Stripe explicitly while Polar remains the environment
default.

TerraScale receives Stripe events at:

```text
POST https://api.terrascale.tech/api/v1/billing/stripe/webhook
```

The endpoint verifies `Stripe-Signature`, enqueues accepted events on
`payments.webhook`, and the API billing worker projects them into the
`TerraScale.Payments` database. Do not call billing projection code directly from Stripe
or from ad hoc scripts.

## Required Secrets

Production Platform workloads must receive these settings from
Orchestrator-managed secret material:

```text
Payments__Provider=stripe
Payments__Stripe__PublishableKey
Payments__Stripe__SecretKey
```

Stripe webhook endpoints also require `Payments__Stripe__WebhookSecret` after a
production Stripe webhook endpoint is created.
`Payments__Stripe__PreviousWebhookSecret` may temporarily hold the prior endpoint secret
during a coordinated rotation.

`Payments__Stripe__CheckoutSuccessUrl`, `Payments__Stripe__CheckoutCancelUrl`, and
`Payments__Stripe__PortalReturnUrl` must be trusted server-side runtime configuration.
Caller-supplied URLs and customer email fields are not used for redirects or billing
identity. Stripe Checkout enables automatic tax by default.

## Stripe Dashboard Setup

1. In Stripe Dashboard, open Developers -> Webhooks.
2. Add endpoint `https://api.terrascale.tech/api/v1/billing/stripe/webhook`.
3. Select events:
   - `checkout.session.completed`
   - `customer.subscription.created`
   - `customer.subscription.updated`
   - `customer.subscription.deleted`
   - `customer.subscription.trial_will_end`
   - `invoice.finalized`
   - `invoice.upcoming`
   - `invoice.updated`
   - `invoice.paid`
   - `invoice.payment_failed`
   - `invoice.voided`
   - `invoice.marked_uncollectible`
   - `charge.refunded`
4. Copy the endpoint signing secret into `Payments__Stripe__WebhookSecret`.
5. Keep Stripe API version pinned through `Payments__Stripe__ApiVersion` when production
   compatibility requires a fixed version.

## Local Verification

Local Aspire AppHost tests use signed payloads and the real TerraScale Queue path. Run:

```bash
dotnet test src/Platform/TerraScale.Platform.Tests/TerraScale.Platform.Tests.csproj --no-build --treenode-filter "/*/*/*/PaymentProviderRefundEvents_ProjectSharedInvoiceState" --minimum-expected-tests 1
```

The payment client form contract is covered by:

```bash
dotnet test src/Payments/TerraScale.Payments.Tests/TerraScale.Payments.Tests.csproj --no-restore
```

## Operations

- Accepted webhook events should appear on the `payments.webhook` queue until the
  `payments-webhook-processor` consumer acknowledges them.
- Poison messages should move to `payments.webhook.deadletter` after the configured retry
  policy.
- Permanent webhook receipts make processing and operator replay idempotent by provider
  event id; duplicate event ids should not create duplicate invoices or notifications.
- Inspect dead-lettered receipts with
  `GET /api/v1/admin/billing/webhooks/dead-lettered`, inspect one with
  `GET /api/v1/admin/billing/webhooks/stripe/{eventId}`, and replay a corrected
  dead-lettered event with
  `POST /api/v1/admin/billing/webhooks/stripe/{eventId}:replay` plus an
  `Idempotency-Key`.
- The Stripe reconciliation scheduler repairs subscription state only for Stripe-owned
  billing accounts.
- Monitor `terrascale.billing.webhooks` outcomes and the `payment_queues` readiness check.
  Do not publish raw NATS messages.
- For signing-secret rotation, deploy the old secret as
  `Payments__Stripe__PreviousWebhookSecret` and the new secret as
  `Payments__Stripe__WebhookSecret`, switch Stripe, confirm delivery, then remove the old
  value.
