# Rotate refresh tokens and revoke their family

TerraScale issues 15-minute access tokens and rotated refresh tokens lasting 30 days. Refresh-token reuse, password reset, password change, account suspension, and “sign out everywhere” revoke the entire token family. Billing, credential, deletion, and break-glass actions also require fresh authentication rather than relying only on an existing session.

Dashboard implements platform account sessions through Better Auth. Database
API does not issue account sessions or accept session state as direct database
authority.
