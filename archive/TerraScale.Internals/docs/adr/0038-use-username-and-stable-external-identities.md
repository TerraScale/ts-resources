---
status: superseded by ADR-0041
---

# Use Username and stable External identities

A password-backed User has one globally unique, case-insensitive Username as an alternative to email sign-in. Google and GitHub identities link by stable provider and subject identifiers, with verified email used only for the first link. Fresh authentication accepts password, Google, GitHub, passkey, or MFA proof no older than 15 minutes instead of depending on an MFA-specific claim.
