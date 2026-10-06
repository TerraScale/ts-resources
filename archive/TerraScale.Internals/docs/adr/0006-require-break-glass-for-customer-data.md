# Require break-glass access for customer documents

TerraScale Admin authority does not grant standing access to customer documents. Support or incident access requires MFA, an approved reason, narrow organization and project scope, a short expiry, a complete audit record, and customer notification unless law prohibits it. The grant expires automatically and never creates customer organization or project membership.

_Amended by [ADR-0041](0041-authenticate-terraScale-accounts-with-email-only.md): TerraScale accounts have no MFA; the fresh-identity requirement is a completed email sign-in verification no older than 15 minutes. All other controls are unchanged._
