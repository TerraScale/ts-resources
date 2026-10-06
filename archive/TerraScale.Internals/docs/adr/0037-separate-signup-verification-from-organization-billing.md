---
status: superseded by ADR-0040
---

# Separate signup verification from Organization billing

Signup verification uses an embedded Polar payment method attached to an individual Customer linked to the User; TerraScale confirms the method server-side, never charges it, deletes it after reconciliation, and records historical Organization creation eligibility. Each User may create one Developer Organization, additional self-created Organizations start on a paid plan, and every Organization uses a separate Polar team Customer for billing. This supersedes only ADR-0012's constraint based on sharing one payment method across Users, which Polar cannot enforce without a card fingerprint; its other abuse controls remain in force.
