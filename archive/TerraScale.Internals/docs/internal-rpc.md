# Internal MagicOnion transport

TerraScale uses MagicOnion 7.10.2 for private communication between owned
backend processes. Public request/response Platform and Authentication APIs
remain versioned REST. Separately contracted public real-time APIs remain
versioned WebSocket or SSE endpoints. Dashboard, SDKs, the CLI, customers,
public health probes, TerraBase, NATS, and third-party integrations do not use
this private transport.

## Scope

| Caller | Service | RPC shape |
| --- | --- | --- |
| Platform | Authentication | Unary authentication storage command |
| Authentication | Platform | Unary incomplete Signup verification cleanup |
| Platform | Regional Platform | Unary queue replication and definition synchronization |
| Platform | Regional Platform | Raw duplex stream for a proxied public HTTP request and response |

Ordinary commands use C# MagicOnion interfaces and explicitly keyed
MessagePack contracts. Regional forwarding uses metadata frames followed by
bounded body chunks so an unbounded public request or response is never
buffered into one RPC message. There is no internal REST fallback or
dual-protocol migration path.

## Listeners and configuration

Platform and Authentication each bind a dedicated HTTP/2 listener from
`TerraScale:Kestrel:InternalRpcPort`. Middleware rejects gRPC traffic on public
listeners and rejects non-gRPC traffic on the internal listener. Internal
ports must not appear in ingress, public DNS, OpenAPI, Scalar, SDKs, or the
Dashboard.

Platform discovers its peers through:

```text
InternalRpc:AuthenticationEndpoint
InternalRpc:RegionalEndpoints:{region}
```

Authentication discovers the Platform in its current region through
`InternalRpc:RegionalEndpoints:{region}`. It uses that route only to remove an
incomplete Signup verification Customer before account deletion.

`InternalRpc:LocalPublicEndpoint` may identify the receiving Platform's local
public listener. When omitted, the receiver derives it from the configured
Kestrel URL.

AppHost allocates randomized, non-external internal ports. Production endpoint
allocation and discovery belong to TerraScale.Orchestrator.

## Security

Same-cell development may use isolated clear-text HTTP/2. Production and all
cross-region calls use Orchestrator-issued workload certificates:

- Platform clients present the Platform workload identity.
- Authentication clients present the Authentication workload identity.
- Authentication and Platform servers present their expected workload
  identities.
- Both sides validate the configured CA and exact SPIFFE URL identity.

Authentication listeners allow the Platform workload identity. Platform
listeners allow both Platform and Authentication through
`InternalRpc:AllowedClientIdentities`; the older single
`InternalRpc:ExpectedClientIdentity` setting remains a fallback.
Platform then authorizes each RPC operation against the caller certificate:
Authentication may call only incomplete Signup verification cleanup, while
regional queue and forwarding methods require the Platform identity. Insecure
development calls are accepted only from loopback.

Queue RPCs retain their signed timestamp, nonce, origin, target, placement
generation, payload hash, replay protection, and payload limits in addition to
transport identity. Logs include safe operation and region metadata only;
payloads, authorization values, credentials, and secrets are never logged.

## Behavior and failures

Authentication commands propagate cancellation, deadlines, trace context, and
an operation name. They are not retried automatically. Unavailable or expired
authentication RPCs map to public 503 responses; invalid or unexpected
contracts map to 500 responses.

Regional forwarding carries the original method, path, query, allowed
headers, and streamed body. The receiving Platform sends the request through
its own local public pipeline, preserving authentication, authorization,
routing, idempotency, metering, response status, headers, and response
streaming. A forwarding marker prevents a second regional hop. An unavailable
target maps to 503; an unexpected forwarding contract failure maps to 500.
Forwarded mutations are not retried.

Queue worker retry and durable outbox behavior are unchanged. Unary queue RPCs
preserve HMAC, replay, region, generation, timeout, payload-limit, and terminal
status semantics. Only the existing worker/outbox path retries transient
delivery.

Public readiness endpoints remain HTTP. Platform's readiness result includes
an Authentication RPC probe, so Platform is not ready when its required owner
is unavailable.
