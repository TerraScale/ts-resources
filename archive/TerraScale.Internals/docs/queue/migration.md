# TerraScale Queue Migration Guide

Use TerraScale Queue for new async service workflows. Existing in-process background work should move behind `TerraScale.Queue` contracts before adding new broker-specific code.

## Payments

`TerraScale.Payments` owns the first queue integration:

| Workload | Queue |
| --- | --- |
| Payment webhooks | `payments.webhook` |
| Payment reconciliation | `payments.reconciliation` |
| Payment webhook DLQ | `payments.webhook.deadletter` |
| Payment reconciliation DLQ | `payments.reconciliation.deadletter` |

Feature code should use `PaymentQueueDispatcher` instead of publishing raw NATS messages or calling JetStream directly.
Webhook and reconciliation workers should use `PaymentQueueProcessor`, which wraps `QueueProcessor` with the payment retry policies and DLQ queues.
`TerraScale.Payments.Tests` proves the payment dispatcher, processor, acknowledgements, and webhook DLQ path against a real JetStream server.
Set `TERRASCALE_QUEUE_NATS_URL` to the running broker URL; for Aspire-managed NATS, use the connection string exposed by AppHost instead of a fixed localhost port:

```bash
dotnet test src/Payments/TerraScale.Payments.Tests/TerraScale.Payments.Tests.csproj
```

## Migration Steps

1. Define the queue or topic name in the feature project.
2. Add a typed message record for the payload.
3. Register `AddTerraScaleQueue` and the feature queueing extension.
4. Publish through `IQueueClient`, `IMessagePublisher`, or the feature dispatcher.
5. Consume with `QueueProcessor` or a feature-specific processor so retries, lock handling, and DLQ routing stay consistent.
6. Add an env-gated integration test that uses a real NATS JetStream instance.
7. Add CLI or operational docs for replay, retry, and DLQ handling.
8. Verify queue metrics, retry count, DLQ count, and consumer lag before enabling the workflow in production.

## Do Not Migrate To

- raw NATS subjects from feature code;
- ad hoc in-memory queues;
- mocked tests for queue behavior;
- bash-only queue management scripts;
- one-off storage tables that bypass the TerraScale Queue SDK.
