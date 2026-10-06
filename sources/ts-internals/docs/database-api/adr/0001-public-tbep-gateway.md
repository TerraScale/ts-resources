# ADR 0001: sole public Database API and TBEP gateway

Status: Accepted boundary; implementation ongoing.

Date: 2026-08-29. Updated: 2026-08-31.

## Decision

`TerraScale.Database` is the independently deployable public database service
and the only customer-facing process allowed to call the private TerraBase
Engine Protocol (TBEP).

The service uses the official `terrascale.tech/terrabase-go` client. Private
TBEP is protobuf/gRPC over HTTP/2 with TLS 1.3 mutual authentication. Runtime
configuration supplies the engine endpoint, trust roots, client identity, and
server authority. The gateway binds each client to an immutable tenant,
project, database, and principal scope before it performs an operation.

Dashboard, SDKs, operators, and customers do not receive direct TerraBase,
TBEP, NATS, storage, local socket, or in-process engine access. The service
does not own Dashboard identity, billing, MCP, or database engine behavior.

## Consequences

Every public operation needs a typed application port, validation, error and
retry behavior, resource limits, and tests. Its engine operation must exist in
`terrabase-go`; the gateway must not recreate missing atomic behavior with a
sequence of lower-level document calls.

The public reactive protocol remains MessagePack over WebSocket, with the
specified HTTP fallback. It is separate from private TBEP.
