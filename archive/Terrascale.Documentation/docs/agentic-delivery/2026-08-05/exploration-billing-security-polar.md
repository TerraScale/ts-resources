# Billing, security, and Polar exploration

Status: planning and evidence record, not production-ready.

## Confirmed evidence

Current code supports Polar checkout, portal, subscription lookup, standard HMAC webhook verification with secret rotation and time tolerance, replay storage, queue and DLQ handling, local usage metering, public billing endpoints, and Dashboard SDK composition. The current live sandbox test needs both a sandbox token and a product ID and tests checkout only.

There is no Polar usage-event API or outbox. Decide and implement either fixed-only billing or metered usage export before billing claims expand. The `StripePaymentReconciliationConsumer` name is shared dispatch, so it is naming and test debt, not a confirmed functional gap.

## Required evidence

Add a sandbox product and webhook runbook plus opt-in tests for checkout, portal, subscription, webhook, reconciliation, and usage. Keep payment testing separate from live payment identities. Secrets belong only in owner-readable environment or secret injection and must never appear in reports or source.
