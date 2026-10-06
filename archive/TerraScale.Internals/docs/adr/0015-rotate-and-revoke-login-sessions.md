# Rotate refresh tokens and revoke their family

TerraScale issues 15-minute access tokens and rotated refresh tokens lasting 30 days. Refresh-token reuse, password reset, password change, account suspension, and “sign out everywhere” revoke the entire token family. Billing, credential, deletion, and break-glass actions also require fresh authentication rather than relying only on an existing session.

_Amended by [ADR-0041](0041-authenticate-terraScale-accounts-with-email-only.md): password reset and password change no longer exist; email re-verification, account suspension, and sign-out-everywhere revoke the family, and fresh authentication is a completed email sign-in verification no older than 15 minutes._
