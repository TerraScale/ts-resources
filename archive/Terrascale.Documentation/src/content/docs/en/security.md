---
title: Coordinated security disclosure
description: How to report a TerraScale vulnerability and what response to expect.
sidebar:
  hidden: true
---

Report suspected vulnerabilities privately to [security@terrascale.tech](mailto:security@terrascale.tech). Include the affected public product or URL, impact, reproducible steps, and any request identifiers that do not contain secrets. Do not include credentials, personal data, or unrelated Customer content.

The canonical machine-readable contact is [security.txt](https://docs.terrascale.tech/.well-known/security.txt).

## Our response

TerraScale targets acknowledgement within two business days. The acknowledgement confirms receipt and gives a contact for follow-up. Triage, remediation, disclosure timing, and customer notice depend on impact and verified scope.

TerraScale has no funded bug bounty program during Public Alpha. This policy does not promise payment or a reward.

## Research boundaries

Use accounts and data you own or have permission to test. Stop if testing could access another customer's data, degrade the service, trigger destructive work, or affect availability. Do not use denial-of-service traffic, social engineering, credential theft, physical attacks, or automated scanning that ignores rate limits.

Good-faith research that follows these boundaries should be reported through the contact above. Legal safe-harbor wording still requires owner and counsel approval before it can become a contractual promise.

## Security statements

Customer traffic requires TLS 1.2 or newer. Customer data at rest uses qualified encryption at rest through storage and key-management controls. TerraScale names algorithms only after production evidence covers every relevant path. Encryption does not replace authorization, tenant isolation, recovery, or deletion controls.

Customer content remains in the Database's selected regions. Minimal Control metadata for accounts, authorization, billing references, resource state, monitoring, audit, security, support, and deletion receipts may be processed in TerraScale control regions.

## Security incidents

After confirming that an incident affected a customer organization, TerraScale emails its Organization Owners. The notice identifies the known affected period and data categories, current mitigations, and any customer action. Scope and cause may still be under investigation. See [service status and incident communication](/about/status-and-incidents/).

The checked-in contact and policy links are publication inputs, not proof of external reachability. An authorized release check must load `https://docs.terrascale.tech/en/security/` and `https://docs.terrascale.tech/.well-known/security.txt`, confirm the status page, and exercise the Organization Owner notification path before registration opens.
