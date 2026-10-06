# Registration clickwrap requirements

Status: draft
Owner approval: pending
Policy version: LEGAL_TBD_CLICKWRAP_VERSION

The Dashboard must not activate clickwrap or complete registration until Mario approves the customer policies and the legal publication gate passes.

## Active policy set

The registration server owns an active required-policy set. Each entry has a stable policy key, immutable version, publication time, canonical URL, and content digest. Replacing text creates a new version. It never edits an accepted version in place.

## Affirmative acceptance

The form displays each required policy and its active version before payment verification. Required controls start unchecked. Registration rejects a missing, stale, or unknown policy version. A general continuation click, a preselected control, or mere use of the site is not acceptance.

## Acceptance record

For each required version, the server records:

- the policy key, immutable version, URL, and content digest;
- affirmative acceptance;
- the authenticated or pending user identifier;
- the organization identifier when the policy applies to an organization;
- acceptance time;
- request evidence sufficient to investigate disputes without storing credentials or full Customer content.

The server writes the acceptance record before completing registration or payment verification. Retries are idempotent. Audit access is restricted and retention follows the approved legal schedule.

## Approval

Mario's final approval record must name every active version and its digest. Approval date and evidence location: LEGAL_TBD_OWNER_APPROVAL_RECORD.
