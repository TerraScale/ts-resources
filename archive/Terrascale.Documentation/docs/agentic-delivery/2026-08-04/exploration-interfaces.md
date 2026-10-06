# Interfaces exploration

## Confirmed public-client split

The TypeScript client constructs first-class clients for onboarding, organizations, databases, queues, repositories, backups, usage, billing, audit, notifications, security, and other product workflows. This is the practical parity surface used by Dashboard.

The .NET `TerraScaleClient` deliberately focuses on database, repository, project, region, queue, environment, usage, key, backup, billing, notification, and sync operations. It does not expose the user and organization onboarding workflow shape present in the TypeScript client. This asymmetry is intentional and must be documented as a client-audience decision, not silently filled with private calls.

## Contract requirements

New branch, recovery-workspace, operation-status, and audit capabilities need versioned public REST contracts and typed methods in every client promised parity. Define capability discovery so a caller can distinguish unavailable, unauthorized, disabled, and terminal operation states without guessing from UI behavior.

Every mutating request needs an idempotency key, operation identifier, state transitions, error code, correlation identifier, and safe retry semantics. Public clients must never carry Dashboard-only headers, organization bypasses, direct database connections, or internal RPC knowledge.

## Evidence reviewed

- `TerraScale.TypeScript/src/client.ts`, including `onboarding`, `organizations`, `backups`, `usage`, `audit`, and `security` clients.
- `TerraScale.DotNet/src/TerraScale.DotNet/TerraScaleClient.cs`, whose constructor exposes the intentionally narrower client set.
