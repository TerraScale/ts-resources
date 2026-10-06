# ADR 0025: private TBEP gateway boundary

Status: Accepted. Transport cutover is staged for document operations and
readiness; raw document bytes remain blocked upstream.

Date: 2026-08-29. Updated: 2026-08-31 for workspace decision D-02.

## Context

The public API must not expose TerraBase storage, a private protocol, or an
arbitrary operation forwarder. The engine link carries tenant and workload
identity, so transport shortcuts change the security boundary.

## Decision

The Database API calls TerraBase only through named operations in
`terrascale.tech/terrabase-go`. The gateway:

- uses protobuf/gRPC over HTTP/2 with TLS 1.3, custom trust roots, server-name
  verification, and a client certificate;
- resolves an opaque placement to its endpoint and shares one gRPC transport
  per immutable placement;
- binds one immutable `terrabase-go` client per operation to the complete
  tenant, project, database, and principal scope;
- forwards idempotency and usage-admission identities on mutations;
- maps typed gRPC and TBEP failures to closed application outcomes;
- closes each shared transport when the API host stops, which invalidates its
  bound clients; and
- exposes typed application ports, never a raw proxy, local TBEP socket, or
  in-process engine binding.

The repository does not own generated TBEP bindings or a second wire codec.
TerraBase owns the protobuf service, and `terrabase-go` is the only network
client. The public reactive MessagePack protocol remains a separate customer
contract.

## Current implementation

`src/database/adapters/document_gateway.go` maps document read, write, delete,
and readiness calls to `terrabase-go`. The API and adapter tests exercise the
real authenticated gRPC path, typed failures, idempotent replay, usage
admission, tenant isolation, transport reuse, and lifecycle shutdown.

The pinned `terrabase-go` version still exposes structured document values.
The compatibility conversion is isolated in
`src/database/adapters/document_value_compat.go`, but it does not satisfy
workspace decision D-30. TB-20/TB-21 must publish protobuf `bytes` fields and
a raw canonical JSON client API. The gateway must delete the conversion when
that API exists, not add another parse/serialize bridge. This blocks
production.

The live workflow runs the integration-tagged adapter test against a protected
TerraBase member over mTLS gRPC. Missing engine operations remain fail-closed.
In particular, the Better Auth atomic storage calls cannot be built from
document operations; ADR 0034 records the required TerraBase and
`terrabase-go` work.

## Consequences

Adding an engine-backed public operation requires a matching typed
`terrabase-go` method and an adapter mapping. A scripted engine is useful for
failure cases, but production readiness still depends on the live engine,
deployment identity, and topology checks in the workspace goal.
