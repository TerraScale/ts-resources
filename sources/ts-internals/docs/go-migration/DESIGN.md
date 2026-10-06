# ts-internals Go architecture

Status: current. The workspace `GOAL.md` is authoritative.

## Runtime shape

`ts-internals` is one Go module with two binaries:

- `cmd/terrascale-database` runs the public Database API.
- `cmd/terrascale` runs the customer CLI.

The Database API remains one deployable service. Packages under
`src/database/` separate domain rules, application services, provider
adapters, and the HTTP composition root without creating extra services.

## Public HTTP boundary

The Database API uses Fiber v3. Route registration, middleware order, body
limits, cancellation, panic containment, and error projection all live in
`src/database/api`.

The customer contract is versioned REST under `/api/v1`, plus the bounded
MessagePack reactive protocol over WebSocket and its HTTP fallback. Public
document bodies remain canonical JSON bytes inside those envelopes. Handlers
must not decode a document body after TerraBase has canonicalized it.

Every public operation has a named route, typed request and response,
authorization scope, resource bound, idempotency rule, and stable error
mapping. The OpenAPI document and route manifest must agree with the routes
that Fiber registers.

## TerraBase boundary

`terrabase-go` is the only network client for TerraBase. It carries protobuf
TBEP over gRPC and HTTP/2 with TLS 1.3 mutual authentication. The Database API
uses named adapter methods and never exposes a raw private-protocol forwarder,
local engine binding, or caller-selected engine method.

The transport configuration is deployment supplied. Startup and readiness
fail closed when the endpoint, trust roots, client identity, or required
engine capabilities are missing.

## Package responsibilities

| Path | Responsibility |
| --- | --- |
| `src/core/` | Stable identifiers, errors, regions, redaction, and shared bounds. |
| `src/database/domain/` | Database API value types and ports. |
| `src/database/application/` | Authorization-aware use cases and readiness. |
| `src/database/adapters/` | `terrabase-go` translation and external integrations. |
| `src/database/api/` | Fiber composition, middleware, routes, and public encoding. |
| `src/database/testengine/` | Hermetic gRPC test engine used by integration tests. |
| `src/cli/` | CLI parsing, configuration, HTTP calls, and rendering. |

Dependencies point inward. API and adapter packages may depend on application
and domain packages. Domain packages do not import the host or transport.

## Safety rules

- Derive tenant, project, database, and authorization context from verified
  credentials and route identity. Never trust caller-selected scope headers.
- Pass `context.Context` through every dependency call and honor cancellation
  before mutations.
- Bound bodies, query work, reactive sessions, dependency calls, and result
  streams before allocating or dispatching.
- Keep credentials, document contents, private endpoints, and provider error
  bodies out of logs and public errors.
- Keep unavailable production dependencies fail closed. Test adapters must be
  explicitly composed and cannot become production defaults.

## Verification

Before a commit is integrated, run:

```bash
gofmt -l .
go vet ./...
go build ./...
go test ./...
go test -race ./...
```

`gofmt -l .` must print nothing. Live dependency tests remain opt-in and must
name their required environment variables.
