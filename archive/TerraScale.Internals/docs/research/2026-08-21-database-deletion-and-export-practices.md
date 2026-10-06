# Database deletion and export practices

Research date: 2026-08-21

## Scope

This note supports product decisions for project export and delayed logical-database deletion. It distinguishes legal or standards requirements from recommended product policy. It is not legal advice; jurisdiction-specific retention schedules still require counsel and documented configuration.

## Recommendations

### Q11 — Authorize full-project exports narrowly

Allow full-project export to `Organization Owner` and `Project Owner` only. Do not grant it to application credentials, ordinary project members, or billing-only roles. Include billing receipts only when the caller separately has billing access (`Organization Owner` or billing manager). Require recent interactive authentication and create an audit record for request, completion, download, expiry, and revocation.

Why: a bulk export concentrates all tenant data and should follow least privilege. NIST SP 800-53 AC-6 requires only the access necessary for assigned tasks, while GDPR Articles 20 and 32 require portability where applicable and security appropriate to risk; neither requires broad role access.[^nist-ac6][^gdpr]

### Q12 — Generate asynchronously and distribute through a short-lived authenticated capability

Use an idempotent asynchronous export job. Encrypt the artifact at rest, bind it to the requesting tenant and authorized principals, expose status separately, and provide a single-purpose download capability with a maximum lifetime of 24 hours. Re-check authorization when issuing the link and at download time where the storage architecture permits it. Support explicit revocation, prevent caching, avoid logging the capability, and delete the artifact after expiry or a short documented grace period.

AWS documents large data exports as asynchronous jobs and S3 presigned URLs as bearer capabilities whose effective lifetime is constrained by both the requested expiry and the issuing credential; AWS also recommends restricting their use through policy conditions.[^dynamodb-export][^s3-presigned] The 24-hour value is therefore a TerraScale risk-based product limit, not a statutory rule.

### Q13 — Export one declared logical point in time

The export must represent one logical snapshot time across its manifest and NDJSON files. Record the snapshot timestamp, schema/export format version, included resource identifiers, and integrity hashes in the manifest. Changes committed after the snapshot belong to a later export. If a cross-resource consistent snapshot cannot be obtained, fail the job rather than silently combining different points in time.

Point-in-time exports are an established managed-database pattern: DynamoDB exports select any point in the point-in-time-recovery window and do not affect live capacity.[^dynamodb-export] PostgreSQL exported snapshots similarly exist to synchronize multiple sessions on exactly the same database state.[^postgres-snapshot] TerraScale should implement the equivalent at its own storage seam rather than exposing engine-specific details.

### Q14 — Resolve cancellation and deletion with an atomic state transition

Model deletion as a durable state machine such as `Active -> Scheduled -> Deleting -> Deleted`, with `Scheduled -> Active` for cancellation. At the deadline, the worker must atomically compare the persisted state/version and claim `Scheduled -> Deleting`. A cancellation succeeds only if it atomically changes `Scheduled -> Active` first. Once the worker has claimed `Deleting`, cancellation returns a stable conflict result and cannot resurrect the database. Repeated schedule and cancel requests are idempotent and audit every effective transition.

This is a system correctness policy rather than a rule imposed by GDPR. It applies the HTTP definition of idempotency—multiple identical requests have the same intended effect—and prevents a check-then-act race by making the competing transitions conditional and atomic.[^rfc9110-idempotency]

### Q15 — Retain only records backed by a documented purpose and schedule

Delete customer content after the seven-day grace period. Retain billing, security, and audit records only where a documented legal obligation, fraud/security need, or legal-claims purpose applies. Keep these records minimized and logically separated from customer content, restrict their use, and assign each record class a jurisdiction- and purpose-specific retention schedule. The product must fail closed against indefinite retention: absence of an approved schedule means no automatic expungement decision is invented in code and the policy gap is surfaced for governance.

GDPR Article 5(1)(e) requires personal data to be kept no longer than necessary, while Articles 5(2) and 24 require accountability. Article 17(3) provides limited exceptions to erasure, including legal obligations and legal claims; it does not authorize retaining everything indefinitely.[^gdpr] NIST SP 800-53 AU-11 likewise calls for retaining audit records for an organization-defined period consistent with policy and law.[^nist-au11]

### Q16 — Delete customer-controlled backups; expire shared service backups safely

At final deletion, revoke access and delete every backup, snapshot, or export that the customer can address or restore independently. Shared immutable disaster-recovery backups may age out under a documented, bounded operational retention period when selective erasure is not technically safe. During that interval, mark the logical database as deleted in authoritative metadata, prohibit ordinary restoration, keep backup access tightly restricted, and ensure any exceptional whole-system recovery reapplies the deletion tombstone before customer service resumes.

Google Cloud's official deletion lifecycle distinguishes active-system deletion from later backup-cycle deletion and states that backup media are overwritten on a bounded schedule; this supports delayed expiry for shared recovery media, not continued customer access.[^google-deletion] NIST SP 800-88 Rev. 1 requires media sanitization decisions to use clear, purge, or destroy methods according to confidentiality and reuse needs.[^nist-800-88] GDPR Article 17 still requires erasure without undue delay, so the operational backup window must be necessary, bounded, documented, protected, and excluded from normal processing.[^gdpr]

## Resulting product policy

1. Full-project export: `Organization Owner` or `Project Owner`; billing data requires its own billing permission.
2. Export delivery: asynchronous, idempotent, encrypted, audited, and revocable; authenticated download capability expires within 24 hours.
3. Export consistency: one declared logical snapshot or the job fails.
4. Deletion race: the first successful atomic transition wins; cancellation is unavailable after `Deleting` is claimed.
5. Retention: purpose-specific schedules configured by jurisdiction and data class; no blanket or indefinite preservation.
6. Backups: delete customer-restorable copies at final deletion; shared recovery copies expire under a bounded schedule and cannot restore a deleted logical database into service.

## Primary sources

[^gdpr]: European Union, [Regulation (EU) 2016/679 (GDPR), Articles 5, 17, 20, 24, and 32](https://eur-lex.europa.eu/eli/reg/2016/679/oj).
[^nist-ac6]: NIST, [SP 800-53 Rev. 5, control AC-6: Least Privilege](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).
[^nist-au11]: NIST, [SP 800-53 Rev. 5, control AU-11: Audit Record Retention](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).
[^dynamodb-export]: AWS, [DynamoDB data export to Amazon S3: How it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataExport.HowItWorks.html).
[^s3-presigned]: AWS, [Download and upload objects with presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html).
[^postgres-snapshot]: PostgreSQL Global Development Group, [`pg_export_snapshot`](https://www.postgresql.org/docs/current/functions-admin.html#FUNCTIONS-SNAPSHOT-SYNCHRONIZATION).
[^rfc9110-idempotency]: IETF, [RFC 9110, section 9.2.2: Idempotent Methods](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2).
[^google-deletion]: Google Cloud, [Data deletion on Google Cloud](https://cloud.google.com/docs/security/deletion).
[^nist-800-88]: NIST, [SP 800-88 Rev. 1: Guidelines for Media Sanitization](https://csrc.nist.gov/pubs/sp/800/88/r1/final).
