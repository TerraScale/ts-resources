# Active integration lease review

Date: 2026-08-07
Status: read-only review record for currently uncommitted checkout slices.

This report is not a production-readiness claim. It records bounded review findings from the active dirty paths named below. None of the three reviewed dirty checkouts, `TerraScale.Internals`, `TerraScale.Orchestrator`, or `TerraScale.Deploy`, was modified, staged, committed, fetched, reconciled, or validated by this review. The Documentation checkout containing this report was modified and committed separately. No secrets, credentials, endpoints, tenant data, or environment values are included.

## Internals: billing and deletion

**Owning repository:** `TerraScale.Internals`

**Active dirty-path limitation:** the observed slice is limited to the Platform billing and organization-deletion paths and one existing Aspire integration-test file:

- `src/Platform/TerraScale.Platform/Features/Billing/Services/PolarBillingService.cs`
- `src/Platform/TerraScale.Platform/Features/Billing/Services/StripeBillingAccountDocument.cs`
- `src/Platform/TerraScale.Platform/Features/Billing/Services/StripeBillingAccountStore.cs`
- `src/Platform/TerraScale.Platform/Features/Billing/Services/StripeBillingService.cs`
- `src/Platform/TerraScale.Platform/Features/Organizations/Endpoints/RequestOrganizationDeletionEndpoint.cs`
- `src/Platform/TerraScale.Platform/Features/Organizations/Services/OrganizationDeletionWorker.cs`
- `src/Platform/TerraScale.Platform.Tests/Billing/StripeBillingAspireAppHostIntegrationTests.cs`

The review did not establish behavior in any other billing, lifecycle, provider, persistence, or deployment path.

1. **A Polar checkout left in `creating` can strand operations.** `BeginPolarCheckoutAsync` persists a pending operation before the provider call, and the rejection path treats a pending operation as unresolved. The observed slice clears the fields on selected webhook handling, but does not itself prove a bounded reconciliation path when the provider call or process fails before a usable session is durably correlated.
2. **Deletion and expired-lease fences can be permanent.** The worker defers when the billing deletion fence is absent. The deletion fence blocks while an unresolved checkout lease or pending Polar operation exists. The observed expiry marker is not, by itself, proof that a failed release, interrupted deletion request, expired checkout lease, or abandoned pending operation reaches a bounded recoverable terminal state.

**Proposed owner/path scope, where grounded:** the active owner should retain the seven paths above, plus only focused billing/lifecycle tests needed to prove their contract. This report assigns no implementation change outside those paths.

**Required bounded proof before admission:**

- Fault-injection evidence for a Polar provider failure or interruption after `creating` is durable, showing a bounded reconciliation or release outcome and safe retry behavior.
- Deterministic expiry and restart evidence for checkout leases and deletion fences, including a failed metadata deletion request, worker interruption, and eventual terminal or explicitly recoverable state.
- Evidence must use isolated nonsecret inputs and confirm no checkout, webhook, or deletion writes are accepted after the relevant durable fence.

## Orchestrator: NATS protocol package migration

**Owning repository:** `TerraScale.Orchestrator`

**Active dirty-path limitation:** the current uncommitted slice is limited to:

- `src/TerraScale.Orchestrator/Development/NatsDevelopmentCluster.cs`
- `src/TerraScale.Orchestrator/Messaging/NatsOperationJournalProvisioner.cs`
- `src/TerraScale.Orchestrator/Messaging/NatsRuntime.cs`
- `src/TerraScale.Orchestrator/Messaging/NatsTopology.cs`

The active diff moves controller protocol-package reads from `CELL_BUNDLES` to `ORCH_PROTOCOL_PACKAGE`. The review did not modify or validate the still-stale tests, README, or delivery-evidence records that refer to `CELL_BUNDLES` for the protocol package.

1. **Controller startup can fail under stale permissions.** The controller ACL construction changes most protocol-package permissions to `OBJ_ORCH_PROTOCOL_PACKAGE` and `$O.ORCH_PROTOCOL_PACKAGE`, while stale `CELL_BUNDLES` subjects remain in the development permission construction. A deployment whose credential policy or rendered permissions has not been migrated consistently can deny the new object-store read and prevent controller startup.
2. **Tests, docs, and evidence are stale.** The observed test and documentation references still describe the protocol package as residing in `CELL_BUNDLES`. They cannot demonstrate the new controller permissions, object-store configuration, or startup path without synchronized updates and rerun evidence.
3. **The hard migration has no old-store fallback.** Runtime startup opens only `ORCH_PROTOCOL_PACKAGE`, and provisioner seeding writes only there. This is a hard cutover, not compatibility behavior. Existing cells must therefore be provisioned and validated in order before a controller that only reads the new store is allowed to start.

**Proposed owner/path scope, where grounded:** the owner should retain the four active messaging and development paths, then separately claim the directly referenced NATS security and journal tests plus the NATS README, guide, and delivery evidence that still name the protocol-package store. No production infrastructure mutation is proposed by this report.

**Required ordered provision and validation gate:**

1. Provision and exact-config validate `ORCH_PROTOCOL_PACKAGE`, then seed and byte-validate the canonical package under infrastructure authority.
2. Render and credential-test controller permissions against the new store, including a successful startup/read and denied mutation access.
3. Update and run the stale focused tests, documentation, and delivery evidence against that behavior.
4. Only then permit controllers with the hard-cutover runtime; retain an explicit rollback or recovery decision rather than inferring an old-store fallback.

The required evidence is a controlled NATS integration run with redacted identities and no credentials or internal endpoint values.

## Deploy: candidate retention

**Owning repository:** `TerraScale.Deploy`

**Active dirty-path limitation:** the observed uncommitted slice is limited to:

- `src/TerraScale.Deploy.Cli/Ci/CiRefactorCommands.cs`
- `src/TerraScale.Deploy.Cli/Ci/CandidateRetention.cs`
- `tests/TerraScale.Deploy.Cli.Tests/Ci/CandidateRetentionPolicyTests.cs`

The retention tests are deterministic policy tests using an in-memory store. This review did not run a registry, fetch the dirty checkout, or alter its paths.

1. **Promoted candidate authority is missing.** Protection is computed from current referenced Git trees and supplied protected trees. A candidate promoted from a tree that is no longer a retained ref tip has no durable promoted authority in the observed retention policy and can become eligible.
2. **The reviewed-plan and deletion sequence races.** The command reviews a dry-run hash, then runs the policy again; the policy re-reads a candidate before an unconditional registry delete. A candidate can change after plan review or after revalidation. With no registry conditional-delete primitive, immutable version token, or exclusive lease that covers final check and delete, this is an unresolved TOCTOU risk.
3. **Package and tree segments are unsafe at the command boundary.** Package configuration is accepted without a constrained package-segment allowlist, and upload/download tree input is interpolated into package URLs without first proving the immutable tree shape at that boundary. Escaping alone is not evidence that path-shaped input is rejected.
4. **Provider end-to-end proof is missing.** The fake-store tests do not prove Forgejo package listing, metadata and file inspection, URL-segment handling, reviewed-plan behavior, or fail-closed deletion against an isolated registry target.

**Proposed owner/path scope, where grounded:** the active owner should retain the three paths above. Any provider-integration harness or environment-gated test requires a separately claimed isolated registry target and exclusive lease.

**Required tests and evidence before admission:**

- Demonstrate durable promoted-candidate authority independent of mutable ref tips, including retention after ref movement.
- Demonstrate that package and tree inputs are constrained to safe immutable identifiers before URL construction, with rejected path-shaped and encoded-segment inputs.
- Demonstrate an exclusive, time-bounded delete lease or a provider conditional immutable deletion primitive that covers reviewed-plan revalidation through delete, and fail closed if it cannot be obtained.
- Run an environment-gated end-to-end test against an isolated safe Forgejo registry target through list, inspect, dry run, reviewed confirmation, race handling, and deletion. Record only redacted results and release the shared-target lease afterward.

## Handoff boundary

This file is the only artifact created by this review. It is a redacted finding record, not remediation, validation evidence, an ownership lease, or authorization to change any product checkout.
