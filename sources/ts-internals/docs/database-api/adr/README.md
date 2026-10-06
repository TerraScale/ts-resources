# Database API ADR index

The workspace [`GOAL.md`](../../../GOAL.md) is authoritative. These records
explain boundaries that remain useful to the Database API implementation.

| ADR | Status | Decision |
| --- | --- | --- |
| [0001](0001-public-tbep-gateway.md) | Accepted boundary; implementation ongoing | The service is the sole public database service and customer-facing TBEP gateway. |
| [0002](0002-grant-authorization-and-tenant-isolation.md) | Accepted boundary; implementation pending | Dashboard grants, live scopes, replay protection, and engine contexts protect every request. |
| [0003](0003-reactive-public-contract.md) | Accepted boundary; implementation pending | Database owns bounded public reactive results; the TypeScript SDK owns launch-client compatibility. |
| [0004](0004-admission-readiness-and-resource-limits.md) | Accepted boundary; implementation pending | Readiness and bounded admission fail closed and protect the service before autoscaling. |
| [0025](0025-private-tbep-gateway-boundary.md) | Staged for document operations and readiness | Private TBEP uses the official `terrabase-go` protobuf/gRPC client over TLS 1.3 mTLS; raw canonical document bytes remain blocked upstream. |
| [0027](0027-client-request-ulid-idempotency.md) | Accepted for document mutations | Client-request ULIDs bind retries to engine receipts and preconditions. |
| [0032](0032-public-contract-limits-and-compatibility.md) | Accepted boundary; implementation and numeric policy pending | Named operations, stable outcomes, and hard limits are required before support. |
| [0033](0033-production-slos-topology-and-operability.md) | Accepted production gate; deployment checks pending | Deployment, security, recovery, and operability gate production. |
| [0034](0034-auth-storage-named-atomic-boundary.md) | Accepted boundary; engine operations pending | Better Auth storage stays three named typed atomic operations and remains fail-closed. |
| [0035](0035-usage-export-integrity-and-authorization.md) | Accepted boundary; source pending | Usage export is checksummed, bounded, engine-minted, and authorization-bound. |
| [0036](0036-authorization-and-admission-composition.md) | Accepted boundary; implementation pending | Verified caller context and bounded admission precede product operations. |

An ADR does not override the workspace goal or prove that an implementation or
environment test has passed.
