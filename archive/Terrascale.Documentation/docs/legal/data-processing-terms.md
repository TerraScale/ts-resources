# TerraScale Data Processing Terms

Status: draft
Owner approval: pending
Policy version: LEGAL_TBD_DPA_VERSION
Effective date: LEGAL_TBD_EFFECTIVE_DATE

These draft terms apply when TerraScale processes personal data in Customer content on a customer's behalf. Brazilian counsel must approve the controller, operator, transfer, audit, and liability language.

## Parties and roles

Customer legal name and address: LEGAL_TBD_CUSTOMER_FIELDS

TerraScale legal entity, registration, and address: LEGAL_TBD_ENTITY_FIELDS

The customer determines the purpose and essential means of processing Customer content. TerraScale processes that content under the customer's documented instructions and the service contract. Each party remains responsible for its separate account, employment, billing, security, and legal-compliance data.

## Processing details

- Subject matter: hosting, routing, replication, querying, export, and deletion of Customer content.
- Duration: the service term plus the documented grace, export, deletion, and legally required retention periods.
- Data subjects and personal-data categories: supplied by the customer within the Public Alpha data boundary.
- Purpose: provide the customer-configured Database service and related support and security work.

The customer must not submit credentials, cryptographic keys, payment-card data, health records, government identifiers, children's data, unlawful content, or specially regulated workloads during Public Alpha.

## Regions and Control metadata

TerraScale stores Customer content in the Database's selected regions. Adding or removing a region may copy, drain, repair, or delete content as part of actual placement work. TerraScale processes minimal Control metadata in its control regions. Control metadata includes account, authorization, resource-state, billing-reference, usage, monitoring, audit, security, support, and deletion-receipt data.

## Security

TerraScale requires TLS 1.2 or newer for customer traffic and uses qualified storage and key-management controls for data at rest. It applies tenant authorization, least-privilege access, audit records, monitoring, incident response, and tested deletion procedures. The approved technical and organizational measures need an evidence attachment: LEGAL_TBD_SECURITY_SCHEDULE.

## Subprocessors and transfers

TerraScale may use subprocessors needed to provide the service. The approved subprocessor list, notice and objection process, processing locations, and international-transfer safeguards are LEGAL_TBD_SUBPROCESSOR_TERMS.

## Assistance and incidents

TerraScale assists with data-subject requests, security investigations, impact assessments, and regulator inquiries to the extent relevant to its processing. It notifies affected Organization Owners after confirming a security incident and supplies known affected periods, data categories, mitigations, and customer actions. Contract timing must align with applicable law: LEGAL_TBD_INCIDENT_LEGAL_TIMING.

## Return and deletion

Customers can export Projects as compressed packages with a manifest and one NDJSON file per Repository. After the service and grace period, TerraScale deletes Customer content under the account-deletion schedule unless law requires limited retention. Deletion receipts do not retain deleted Customer content.

## Audit and liability

The evidence, certification, questionnaire, audit, cost, confidentiality, liability, and precedence terms require legal approval: LEGAL_TBD_AUDIT_AND_LIABILITY.
