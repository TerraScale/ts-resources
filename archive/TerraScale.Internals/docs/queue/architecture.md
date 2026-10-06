# TerraScale Queue Architecture

TerraScale Queue is the C# queue and messaging foundation for TerraScale services. It uses NATS JetStream for durable streams, pull consumers, explicit acknowledgements, replay, retention, duplicate detection, backpressure, and observability.

## Runtime Topology

`TerraScale.Orchestrator` owns the production product-NATS plane:

| Component | Purpose |
| --- | --- |
| Regional product-NATS cluster | Three independent NATS servers with JetStream R3 |
| Runtime configuration | Supplies the regional endpoint and workload-scoped credentials |
| TerraScale Queue | Provisions application streams and consumers through typed SDK contracts |
| Platform internal RPC | Replicates queue mutations and synchronizes definitions between selected regional cells |
| Host monitoring and NATS `$SYS` advisories | Feed NATS health and capacity into the telemetry pipeline |
| Grafana | Shows availability, message rates, streams, consumers, and storage |

## C# Layers

| Project | Responsibility |
| --- | --- |
| `TerraScale.Queue` | Public SDK contracts, NATS JetStream implementation, queue/topic/subscription models |
| `TerraScale.Queue.Tests` | Env-gated real JetStream integration tests |
| `TerraScale.Queue.Benchmarks` | Real JetStream benchmark harness for publish, receive/ack, retry, DLQ, batch, and fanout paths |
| `TerraScale.CLI` | Direct queue, topic, subscription, consumer, retry, DLQ, replay, metrics, and policy commands |
| `TerraScale.Payments` | Payment webhook and reconciliation queue dispatching |

## Queue Model

Work queues use one JetStream stream per TerraScale queue with work-queue retention and one durable consumer per worker group. Topics use interest retention and durable consumers as subscriptions. TerraScale owns the public queue names and maps them to JetStream stream and subject names.

Queue options cover retention, replicas, duplicate-detection window, message TTL, scheduled-message support, FIFO intent, partition count, retry policy, dead-letter settings, and lock settings. `QueueProcessor` applies retry and dead-letter policy for service workers while lower-level clients remain available for operational CLI flows and custom consumers.

Request/reply uses the same queue-name abstraction. The requester calls `IQueueClient.RequestAsync` with a `QueueMessage`; TerraScale resolves the configured tenant/namespace subject and waits on a NATS reply inbox. A durable JetStream consumer receives the request as a normal `QueueReceivedMessage` and responds through `QueueReceivedMessage.ReplyAsync`, so feature code never needs to construct a raw NATS subject.

`QueueProcessor` is the reusable worker runtime for service handlers. It provisions the queue, subscription, and DLQ when requested, receives batches with bounded concurrency, completes successfully handled messages, abandons failed messages with the configured exponential retry delay, and copies poison messages to the configured DLQ before acknowledging the source message.

## Delivery Guarantees

The default delivery model is at-least-once:

- publishers use JetStream publish acknowledgement before returning success;
- `Nats-Msg-Id` is set from the deduplication id, idempotency key, or message id;
- peek uses JetStream direct message reads by stream sequence and subject, so it does not create a consumer, lock messages, or increment delivery attempts;
- receivers use explicit ack;
- long-running handlers can renew the message lock through `QueueReceivedMessage.RenewLockAsync`, which maps to JetStream ack progress and extends the consumer `ack_wait` window;
- abandon uses JetStream NAK with an optional redelivery delay;
- `QueueProcessor` applies `RetryPolicy` and `DeadLetterOptions` so service code gets exponential retries, max delivery count enforcement, and DLQ routing without hand-coded broker logic;
- dead-letter CLI flow copies the message to a DLQ queue and completes the source message;
- replay flow copies DLQ messages back to a target queue;
- request/reply requests flow through the queue subject and responders reply on the NATS inbox attached to the received message.

Cross-region queue replication is separate from the public queue contract.
Each mutation is committed to a durable project outbox and delivered through a
signed unary MagicOnion command to each selected regional Platform. HMAC,
timestamp, nonce, replay, target-region, placement-generation, payload-limit,
and timeout validation remain mandatory. Only the existing worker/outbox path
retries transient delivery; the RPC client itself does not retry.

## Observability

TerraScale.Orchestrator owns production monitoring and Grafana provisioning. The SDK exposes OpenTelemetry-compatible diagnostics through `QueueDiagnostics.ActivitySourceName` and `QueueDiagnostics.MeterName`.

Application telemetry includes:

- spans for queue provisioning, subscription provisioning, publish, peek, receive, process, complete, abandon, and dead-letter operations;
- counters for published, duplicate, received, processed, retried, dead-lettered, acknowledged, and failed operations;
- histograms for publish duration and acknowledgement latency;
- CLI `queue metrics` and `consumer inspect` commands for live JetStream depth and consumer lag snapshots.

## Security And Tenancy

Queue isolation is tenant and namespace aware. `TerraScaleQueueOptions.TenantId` and `QueueNamespace` are folded into the JetStream subject prefix, so the same public queue name can exist in separate tenants or deployment namespaces without sharing streams or subjects. Service deployments should set these values through configuration or secret-backed environment variables instead of hard-coding them.

The SDK supports NATS token auth, username/password auth, TLS, and optional mTLS certificate files through `TerraScaleQueueOptions`. CLI operations can use the same settings through `--nats-token`, `--nats-username`, `--nats-password`, `--require-tls`, `--tls-ca-file`, `--tls-cert-file`, `--tls-key-file`, and `--tls-cert-bundle-file`.

Payload encryption is available through `TerraScaleQueueOptions.Encryption`. The built-in `AesGcmQueuePayloadProtector` encrypts message bodies with AES-GCM before publish, stores the key id, nonce, tag, and original content type as message headers, and decrypts on receive/peek when the configured key ring contains the referenced key id. Key material must come from Orchestrator-managed secret storage or a KMS-backed vault; it must not be committed to source or sample payloads.

Per-queue authorization is enforced before JetStream operations through `QueueAuthorizationOptions`. Services can require a tenant id and restrict queue names with allow and deny prefixes. The CLI exposes the same policy shape with repeated `--queue-allow-prefix` and `--queue-deny-prefix` flags.

Security extension points stay behind application services:

- `IQueuePayloadProtector` encrypts or decrypts message payloads before publish and after receive; services may use the built-in AES-GCM protector or override the interface with a KMS-backed implementation.
- `IQueueAuditSink` records queue operations with tenant, namespace, queue, consumer, message id, and success/failure state.
- Feature code should depend on typed dispatchers or `IQueueClient`; it should not construct raw NATS subjects or bypass these boundaries.
