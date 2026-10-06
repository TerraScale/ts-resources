# ADR 0003: bounded public reactive results

Status: accepted boundary; implementation in progress.

Date: 2026-08-29. Updated: 2026-08-31.

## Decision

The Database API owns the versioned public WebSocket route and the HTTP
fallback. Both carry the generated bounded MessagePack envelope. Canonical
JSON document bodies ride inside frames as opaque bytes.

A session subscribes to typed TQL result views and receives authorized
snapshots, inserts, updates, patches, removals, moves, or resets. Checkpoints
are opaque authorized-view positions. They are not TerraBase replication
vectors or client-owned CRDT state. `@terrascale/sdk` owns the launch client.

Realtime delivery is the fast path. Resume and snapshot bootstrap are the
correctness path. The service reauthorizes after reconnect, permission change,
region movement, or grant expiry. It removes data after access loss and closes
slow or oversized sessions with typed bounded errors.

## Verification

The generated schema, Rust and TypeScript vectors, limits, tenant isolation,
history expiry, duplicate and reordered delivery, reconnect, cancellation,
and slow-consumer tests must pass before the route is advertised.
