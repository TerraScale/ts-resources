---
title: TerraScale Data Processing Terms
description: Draft Public Alpha data-processing terms. Owner approval is pending.
draft: true
unlisted: true
seo:
  noindex: true
---

**Status: draft. Owner approval: pending.** These proposed terms require Brazilian counsel to approve the parties, roles, lawful bases, transfers, audit, liability, and exact legal timing. Those fields remain `LEGAL_TBD`.

The Customer determines the purpose and essential means of processing Customer content. TerraScale processes it under the Customer's instructions to host, route, replicate, query, export, and delete the configured Database service. Customer content stays in selected regions, while minimal Control metadata may be processed in TerraScale control regions.

Customer content is limited to the Public Alpha data boundary. Do not submit credentials, cryptographic keys, payment-card data, health records, government identifiers, children's data, unlawful content, or specially regulated workloads. Customer traffic requires TLS 1.2 or newer and data at rest uses qualified storage and key-management controls. Encryption does not replace authorization, tenant isolation, audit, incident response, or deletion controls.

Customers can export Projects as compressed packages with a manifest and one NDJSON file per Repository. After service, grace, export, and deletion periods, TerraScale removes Customer content unless law requires limited retention. Deletion receipts do not retain deleted content. The approved subprocessor, transfer, security schedule, audit, liability, and retention terms remain `LEGAL_TBD`.
