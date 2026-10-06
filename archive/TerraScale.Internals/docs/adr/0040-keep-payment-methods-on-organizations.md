# Require Organization-owned payment verification during onboarding

Status: Accepted

Date: 2026-08-25

Owner: TerraScale Platform product, billing, and architecture owner

## Decision

Every new User receives one non-transferable Personal Organization. Payment methods, Polar Customer identity, subscriptions, trial eligibility, and billing history belong to an Organization and never directly to a User.

Every account must complete verified-card enrollment on its Personal Organization before normal product access. A Developer Organization creates no subscription or charge. Card reuse is a risk signal and does not reject enrollment by itself.

A User may own one Developer Organization. Membership in another User's Organization does not consume this allowance. Deletion, ownership changes, or membership changes do not reset trial eligibility or Developer allowance except through the explicit lifecycle rules implemented by the owning Platform modules.

Paid Organizations remain `BillingPending` until Polar confirms initial billing. The Organization keeps its selected paid plan pending and cannot create Projects, Invitations, Application credentials, or billable resources before confirmation. An active Developer Organization keeps Developer access while an upgrade is pending.

The onboarding journeys are:

- Developer: User, Personal Organization, verified-card enrollment, Project.
- Paid: User, Organization, Billing, Project.
- Invitation for a new User: User, Personal Organization, verified-card enrollment, Invitation.
- Invitation for a previously verified User: User, Invitation.

The first Project is part of self-registration onboarding. Database and Application credential creation remain optional Getting started tasks after onboarding.

Legacy User-level Signup verification approvals remain readable migration history. Migration moves incomplete payment progress to Organization-owned verified-card enrollment without creating new User-owned billing state. A retryable worker removes legacy individual Polar Customers without changing User access or deleting Organization Customers.

## Superseded rules

This decision supersedes ADR-0036, ADR-0037, and the earlier provider-free Developer wording previously recorded in ADR-0040. In particular:

- Developer onboarding is not provider-free.
- Invited new Users do not bypass Personal Organization card verification.
- Billing identity and payment methods never belong directly to a User.
- Card reuse alone does not deny onboarding.
- Identity, ownership, membership, and card changes do not reset paid-trial eligibility.

## Reconciliation matrix

| Issue | Reconciliation |
| --- | --- |
| #7 | Keep post-confirmation subscription lifecycle on Organizations. Remove provider-free Developer assumptions. |
| #23 | Coordinate the Personal Organization and verified-card journey across Platform, Authentication, SDK, Dashboard, and AppHost proof. |
| #25 | Retire User-owned Signup verification while migrating incomplete progress to Organization-owned card verification. |
| #27 | Require verified-card enrollment for Developer and paid Organization creation. Preserve Developer access during upgrades. |
| #28 | Persist and enforce the Developer, paid, and invitation journey shapes defined above. |
| #29 | Apply cleanup, audit, warning, and abandonment rules to Organization-owned billing and legacy migration. |
| #30 | Use Organization-owned verified-card enrollment as the abuse-prevention gate. Card reuse remains a risk signal. |

## Implementation order

1. Retire and migrate User-owned Signup verification in #25.
2. Persist and enforce the server-owned onboarding state in #28.
3. Complete Organization creation, billing admission, Project placement, and invitations in #27.
4. Publish matching typed TypeScript SDK operations.
5. Complete the Dashboard and Getting started journeys in #26.
6. Finish lifecycle cleanup, audit records, metrics, and race coverage in #29.
7. Re-run the complete public AppHost and browser journey before closing #23.

## Security and data handling

Card data stays inside Polar-hosted components. TerraScale stores only bounded provider references and non-sensitive state needed to resume or audit the journey. Passwords, tokens, checkout secrets, authorization headers, raw provider payloads, and card details must not appear in application state, logs, metrics, audit records, or test evidence.
