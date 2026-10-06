# TerraScale Queue Usage

## Local JetStream

Start the local broker through `TerraScale.AppHost` or the slim
`TerraScale.Nats.AppHost` test host. Use the Aspire-provided NATS connection string
instead of assuming a fixed localhost port.

```bash
dotnet run --project src/Hosting/TerraScale.AppHost/TerraScale.AppHost.csproj
```

## SDK

```csharp
services.AddTerraScaleQueue(options =>
{
    options.NatsUrl = "nats://nats.nats.svc.cluster.local:4222";
    options.SubjectPrefix = "terrascale.queue";
    options.TenantId = "tenant_01";
    options.QueueNamespace = "production";
    options.RequireTls = true;
    options.TlsCaFile = "/var/run/secrets/terrascale-queue/ca.crt";
    options.Authorization.RequireTenantId = true;
    options.Authorization.AllowedQueuePrefixes = ["payments."];
    options.Encryption.Enabled = true;
    options.Encryption.CurrentKeyId = "production-active";
    options.Encryption.Keys["production-active"] =
        configuration["TerraScale:Queue:Encryption:Keys:production-active"]!;
});

services.AddOpenTelemetry()
    .WithTracing(tracing => tracing.AddSource(QueueDiagnostics.ActivitySourceName))
    .WithMetrics(metrics => metrics.AddMeter(QueueDiagnostics.MeterName));
```

```csharp
await queue.EnsureQueueAsync(new QueueDefinition("payments.webhook")
{
    Retention = TimeSpan.FromDays(14),
    Replicas = 3,
});

await queue.PublishAsync(
    "payments.webhook",
    new PaymentWebhookQueueMessage("evt_invoice_paid", "invoice.paid", "{}", "t=1760000000,v1=test"));

var pending = await queue.PeekAsync(new QueuePeekRequest("payments.webhook")
{
    MaxMessages = 10,
});

await foreach (var message in queue.ReceiveAsync(new QueueReceiveRequest("payments.webhook", "payments-worker")))
{
    var payload = message.ReadBody<PaymentWebhookQueueMessage>();
    await message.RenewLockAsync();
    await message.CompleteAsync();
}
```

## Processing With Retries And DLQ

```csharp
await processor.RunAsync(
    new QueueProcessingOptions(
        new QueueDefinition("payments.webhook")
        {
            Options = new QueueOptions
            {
                RetryPolicy = new RetryPolicy
                {
                    MaxDeliveryCount = 5,
                    InitialBackoff = TimeSpan.FromSeconds(15),
                    MaxBackoff = TimeSpan.FromMinutes(5),
                },
                DeadLetter = new DeadLetterOptions
                {
                    Enabled = true,
                    QueueName = "payments.webhook.deadletter",
                    MaxDeliveryCount = 5,
                },
            },
        },
        new QueueConsumerDefinition("payments.webhook", "payments-worker")
        {
            MaxBatchSize = 32,
            MaxDeliveryAttempts = 5,
            DeadLetterQueueName = "payments.webhook.deadletter",
        }),
    async (message, cancellationToken) =>
    {
        var payload = message.ReadBody<PaymentWebhookQueueMessage>();
        await ProcessWebhookAsync(payload, cancellationToken);
    },
    cancellationToken);
```

## Request/Reply

```csharp
var quote = await queue.RequestAsync<PaymentQuoteRequest, PaymentQuoteReply>(
    "payments.quote",
    new PaymentQuoteRequest(2500, "usd"),
    new QueueRequestOptions
    {
        CorrelationId = Ulid.NewUlid().ToString(),
        Timeout = TimeSpan.FromSeconds(10),
    });
```

```csharp
await foreach (var request in queue.ReceiveAsync(new QueueReceiveRequest("payments.quote", "payments-quote-worker")))
{
    var payload = request.ReadBody<PaymentQuoteRequest>();
    await request.ReplyAsync(
        System.Text.Json.JsonSerializer.SerializeToUtf8Bytes(new PaymentQuoteReply(true)),
        "application/json");
    await request.CompleteAsync();
}
```

## CLI

```bash
terrascale queue create payments.webhook --nats-url "$TERRASCALE_QUEUE_NATS_URL"
terrascale subscription create payments.webhook payments-worker --nats-url "$TERRASCALE_QUEUE_NATS_URL"
terrascale queue send payments.webhook --data '{"event":"invoice.paid"}' --content-type application/json --nats-url "$TERRASCALE_QUEUE_NATS_URL"
terrascale queue peek payments.webhook --max-messages 10 --nats-url "$TERRASCALE_QUEUE_NATS_URL"
terrascale queue receive payments.webhook --consumer payments-worker --max-messages 10 --nats-url "$TERRASCALE_QUEUE_NATS_URL"
terrascale queue metrics payments.webhook --nats-url "$TERRASCALE_QUEUE_NATS_URL"
```

`TERRASCALE_QUEUE_NATS_URL` can replace repeated `--nats-url` flags.

Security and tenancy flags map directly to `TerraScaleQueueOptions`:

```bash
terrascale queue create payments.webhook \
  --tenant-id tenant_01 \
  --queue-namespace production \
  --nats-url tls://nats.nats.svc.cluster.local:4222 \
  --nats-token "$TERRASCALE_QUEUE_NATS_TOKEN" \
  --require-tls \
  --tls-ca-file /var/run/secrets/terrascale-queue/ca.crt \
  --queue-allow-prefix payments.
```

The same values can come from environment variables: `TERRASCALE_QUEUE_TENANT_ID`, `TERRASCALE_QUEUE_NAMESPACE`, `TERRASCALE_QUEUE_NATS_TOKEN`, `TERRASCALE_QUEUE_NATS_USERNAME`, `TERRASCALE_QUEUE_NATS_PASSWORD`, `TERRASCALE_QUEUE_REQUIRE_TLS`, `TERRASCALE_QUEUE_TLS_CA_FILE`, `TERRASCALE_QUEUE_TLS_CERT_FILE`, `TERRASCALE_QUEUE_TLS_KEY_FILE`, and comma-separated `TERRASCALE_QUEUE_ALLOW_PREFIXES` or `TERRASCALE_QUEUE_DENY_PREFIXES`.

Encryption keys should come from secret-backed configuration. With the built-in AES-GCM protector, set `TerraScale:Queue:Encryption:Enabled=true`, `CurrentKeyId`, and one or more base64-encoded keys under `TerraScale:Queue:Encryption:Keys:{keyId}`. Environment variables use the standard double-underscore form, for example `TerraScale__Queue__Encryption__Keys__production-active`.

## Tests And Benchmarks

```bash
dotnet test src/Core/TerraScale.Queue.Tests/TerraScale.Queue.Tests.csproj
dotnet run --project src/Core/TerraScale.Queue.Benchmarks/TerraScale.Queue.Benchmarks.csproj -- --nats-url "$TERRASCALE_QUEUE_NATS_URL" --messages 10000 --batch-size 100 --scenario all
```

Benchmark scenarios are `core`, `retry`, `dlq`, `fanout`, or `all`. The fanout scenario also accepts `--fanout-subscriptions`.
