---
status: superseded by ADR-0041
---

# Use recovery codes for MFA recovery

TerraScale issues single-use recovery codes when a user enables MFA, shows them once, and stores only their hashes. A user may regenerate them after fresh authentication. Public Alpha supports TOTP, with passkeys added later. Support cannot bypass MFA without an audited identity-recovery process.
