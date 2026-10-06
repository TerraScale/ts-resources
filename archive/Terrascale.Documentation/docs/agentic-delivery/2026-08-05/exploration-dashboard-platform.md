# Dashboard and Platform exploration

Status: planning and evidence record, not production-ready.

## Confirmed evidence

Dashboard follows the SDK-only full-stack boundary. Existing public Platform APIs and Dashboard compositions cover databases and environments, backups and side-by-side restores, billing, authentication and administration, plus basic usage, latency, and audit signals.

## P0 gaps

There is no public branch lifecycle contract for source, TTL, merge, rebase, or promotion. Customer-facing database observability needs deeper lifecycle and recovery state, and authoritative lifecycle health and API, SDK, Dashboard parity evidence need strengthening. Backup and recovery also need focused Platform real-stack tests.

## Delivery implication

Build Dashboard workflow and view-model code locally on public typed SDK calls. Add a Dashboard-agnostic Platform capability only when it is suitable for every external customer. Customer-visible state should include safe lineage, timestamps, progress, errors, retention, and audit references without exposing internal topology or secrets.
