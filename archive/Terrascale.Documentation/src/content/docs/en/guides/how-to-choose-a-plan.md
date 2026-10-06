---
title: How to choose a plan
description: Choose among Developer, Starter, Pro, and unavailable Enterprise using the Public Alpha catalog.
sidebar:
  order: 12
---

Use this guide with the public plan list at `GET /api/v1/pricing/plans`. The catalog below is the Public Alpha contract. The API response is authoritative if the published catalog changes. Every User receives one non-transferable Personal Organization, and its payment method, Polar Customer identity, subscriptions, trials, billing history, Projects, and memberships belong to that Organization, not directly to the User.

## Target onboarding choice

The target self-registration flow starts with identity and email verification already counted as one completed step, then provisions the first Organization, Project, and logical Database and verifies a payment card for signup abuse control. Card verification creates no charge, subscription, paid trial, or automatic renewal. The User then chooses either no paid plan and no automatic renewal, retaining the Developer allowance, or Starter or Pro with monthly automatic renewal and an eligible first 30 days at no charge. In onboarding copy, "no paid plan" is the customer-facing choice and Developer is the internal free entitlement. Invited-user onboarding remains separate. This target is not yet released and is tracked in [TerraScale.Internals issue 30](https://git.terrascale.tech/TerraScale/TerraScale.Internals/issues/30).

## Quick picker

| Plan | Price and availability | Best when |
| --- | --- | --- |
| `Developer` | $0, non-expiring | You are exploring TerraScale or building a prototype within the Developer limits. |
| `Starter` | $5 monthly | You need a small paid allowance and support target. |
| `Pro` | $25 monthly | You need larger project, storage, and operation-unit allowances. |
| `Enterprise` | $500 monthly support base plus metered usage, unavailable during Public Alpha | You need a contract plan after Enterprise terms are approved. |

## Limits that usually decide

- **Projects and databases**: Developer allows 1 Project and 3 Databases. Starter allows 5 Projects and 10 Databases. Pro allows 25 Projects and 50 Databases.
- **Storage**: Developer allows 1 GB across selected regions. Starter allows 5 GB. Pro allows 50 GB.
- **Operation units**: Developer allows 10,000 per month. Starter allows 1,000,000. Pro allows 10,000,000.
- **Members**: Developer allows 3 members. Starter allows 5. Pro allows 25.
- **Regions**: all available plans can select São Paulo, San Francisco, and Falkenstein.

## Practical advice

1. Start on **Developer** while you validate authentication, repositories, TQL, and queue workflows.
2. Choose **Starter** when the Developer allowances no longer fit.
3. Choose **Pro** when you need the larger allowances or one-business-day support target.
4. Treat **Enterprise** as unavailable until its contract and usage rates are approved.

When a hard allowance is reached, new billable work is rejected. Reads, project export, deletion, and work that reduces usage remain available. The monthly operation-unit allowance resets at the start of the next calendar month.

An eligible paid Organization receives its first 30 days at no charge after an Organization Owner explicitly selects Starter or Pro and accepts monthly automatic renewal. Signup card verification alone does not start this period. Trial eligibility survives changes to the card, owner, or membership and cannot be restored by changing those identities. Cancellation stops renewal at the end of the paid period. An unresolved renewal receives seven days of payment retries with normal access, followed by a 30-day read-only grace period. Payment during either period restores the prior plan and data access. The read-only period permits reads, usage reduction, deletion, and export while blocking new billable work. At its end, TerraScale purges Customer content and customer-restorable copies, retaining only minimal Organization, billing, security, Audit, and deletion-receipt records required by policy. The empty Organization may later reactivate, but purged data cannot return, and an unpaid Organization is not downgraded into Developer.

Voluntary User deletion is separate from failed-payment handling. It starts a seven-day cancellable window, immediately revokes sessions, stops charges, and preserves export throughout the seven-day cancellable window. Completion deletes the Personal Organization, memberships, and Customer content, retaining only legally required records and a deletion receipt. A complete Project export is a compressed, versioned ZIP package with a versioned manifest, integrity hashes, and one newline-delimited JSON file per Repository (NDJSON). It includes Database, Environment, Repository, Document, index, and version metadata, excludes credential secrets, and is not a backup or Database snapshot. Delivery is an authenticated, revocable download available for 24 hours or a short-lived customer-provided AWS S3 presigned destination. TerraScale never stores the customer's AWS access keys.

## Support

Developer receives documentation and best-effort email support. Starter targets a response within two business days. Pro targets a response within one business day. These targets are not resolution guarantees or an uptime SLA. Enterprise support is unavailable during Public Alpha.

Plan prices do not vary by selected region. Operation-unit metering uses the started 4 KiB contract documented in [Pricing](/reference/pricing/).

## Next steps

- [Plans reference](/reference/plans/)
- [Billing](/reference/billing/)
- [Getting started](/guides/getting-started/)
