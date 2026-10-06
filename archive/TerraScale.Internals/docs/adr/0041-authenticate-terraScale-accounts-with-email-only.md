# Authenticate TerraScale accounts with email only

Status: Accepted

Date: 2026-08-26

Owner: TerraScale Platform product and architecture owner

## Decision

A verified email address is the only sign-in credential for a TerraScale
account. Signing in means requesting a sign-in link (magic link) or one-time
code for an email address and proving possession of that mailbox; completing
that verification establishes the User identity and issues the normal session
tokens. TerraScale accounts have no passwords, no usernames, no Google or
GitHub external identities, no passkeys, and no MFA. Existing sign-in surfaces
that accept those credentials are removed from the TerraScale account product.

Account security stays session- and abuse-control-based:

- Sessions keep 15-minute access tokens, rotated 30-day refresh tokens, family
  revocation on refresh-token reuse, email re-verification, account
  suspension, and sign-out-everywhere (ADR-0015).
- Fresh authentication for sensitive billing, credential, deletion, and
  break-glass actions is a completed email sign-in verification no older than
  15 minutes.
- Signup and sign-in keep verified-email requirements, bot proof, throttling,
  velocity rules, enumeration-safe responses, and manual suspension
  (ADR-0012, ADR-0019). Link and code delivery is throttled by email, account,
  and IP.
- The security activity page keeps time, action, approximate location, client,
  and session with individual and global revocation (ADR-0018). Its events are
  email sign-ins, session creation and revocation, email changes, account
  suspension, and suspicious sign-ins.

## Scope boundary

This decision governs TerraScale accounts (the `User` identity). The
project-scoped Authentication product sold to customer projects keeps its own
mechanisms — including passwords, MFA, OAuth, SSO, and passkeys — for customer
application end users, and the `TerraScale.Authentication` storage layer keeps
owning that mechanism infrastructure.

## Superseded and amended rules

This decision supersedes ADR-0016 (recovery codes for MFA), ADR-0017 (modern
password rules), and ADR-0038 (username and stable external identities). It
amends ADR-0015, ADR-0018, and ADR-0019 where their wording presumes password,
provider, or MFA credentials: password reset and password change no longer
exist, fresh authentication is a completed email sign-in, and the throttled
security-sensitive endpoints are signup, login, email verification and sign-in
links, token, and payment verification.
