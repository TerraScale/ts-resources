# Internals exploration

## Confirmed present

The reviewed `TerraScale.Internals/src` tree contains substantial product building blocks: Platform and Authentication services, onboarding and provisioning flows, billing integrations, backup endpoints and clients, user notifications, project monitoring and usage tests, and the Dashboard application. Dashboard-specific behavior is correctly owned in `Dashboard/TerraScale.Dashboard.Next`, while Platform is kept product-facing.

## Gaps for this delivery

No reviewed public product surface establishes managed database branches. Existing monitoring is useful but does not yet constitute deep customer observability across branch lineage, lifecycle operations, recovery evidence, and DR posture. No reviewed implementation or evidence proves customer-facing PITR workflows or recurring DR drills.

## Delivery implications

Build branch and recovery workflows as public Platform capabilities with durable public operation records. Dashboard should compose SDK calls into its own routes, views, and workflows, never move Dashboard behavior into Platform. Observability must expose customer-safe lineage, state, timestamps, actor, region, progress, retry, error classification, retention, and audit references, while keeping secrets and internal infrastructure details out of the contract.

## Evidence reviewed

- `TerraScale.Internals/src/Platform/TerraScale.Platform/Program.cs`
- Platform onboarding, monitoring, placement, notification, and backup test areas
- `TerraScale.Internals/src/Payments/TerraScale.Payments`
- `TerraScale.Internals/src/Dashboard/TerraScale.Dashboard.Next/AGENTS.md`

The Dashboard instructions independently confirm that Dashboard is an ordinary external user and must use typed public TypeScript SDK operations.
