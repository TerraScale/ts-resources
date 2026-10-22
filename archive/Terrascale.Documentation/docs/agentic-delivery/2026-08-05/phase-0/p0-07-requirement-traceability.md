Warning: truncated output (original token count: 139368)
Total output lines: 3151

# P0-07 requirement traceability baseline

Status: open. This is a fail-closed planning baseline. It does not assert implementation, acceptance, production readiness, or P0 acceptance.

Retired cloud records and clauses have been removed from this archived snapshot; remaining ContentLocator values may be shortened.

## Snapshot and record contract

SnapshotDigest: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9`.

The snapshot is the reviewed `/workspaces/TerraScale/GOAL.md` content on 2026-08-05. A SourceAnchor is deliberately only the snapshot digest followed by real, verbatim GOAL headings. RequirementID and ContentLocator are separate so an anchor never invents a leaf slug for a list item or table cell. ContentLocator is the exact source text used to find the atomic requirement and is re-reviewed when the GOAL changes.

PhaseHeading reference format: `PhaseHeading[level=3; number=N; title=T]` is a structured reference to a real GOAL Phase heading. `level`, `number`, and `title` are separate source components. PhaseHeadingPunctuationNormalization: the GOAL delimiter is encoded as `U+2014` and omitted from the structural reference, so the reference is not presented as a verbatim source heading.

Every governing record below has the same required fields. `gap` is the only unfinished value. `N/A` is permitted only in this exact form: `N/A[story;approving-authority;safe-alternative;validation-evidence]`. This baseline contains no N/A decisions. `Evidence:gap` is never acceptance evidence. A future Work value is a stable work ID; its exact contract is defined in the Work contracts section and cannot be closed by a plan, static scan, route inventory, or mocked test.

## Navigation pointers

### REQ-OBJ-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Objective`

RequirementID: `REQ-OBJ-01`

ContentLocator: `Finish **TerraScale, powered by TerraBase**, as a production-ready Database-as-a-Service for human developers and AI agents.`

Navigation: The objective is decomposed into `REQ-OBJ-SERVICE-01`, `REQ-OBJ-QUALITY-01`, and `REQ-OBJ-NOT-MVP-01` in the scoped atomic records. This pointer is not governing authority.

### REQ-ID-EMAIL-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`

RequirementID: `REQ-ID-EMAIL-01`

ContentLocator: `Email/password registration, confirmation, single-use resendable confirmation links, login`

RequirementText: Provide email/password registration, confirmation, single-use resendable confirmation links, and login.

Owner: Platform identity lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Self identity; no account enumeration.

AT: Planned artifact: email/password registration confirmation and login isolation real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Account takeover or confirmation replay.

N/A: gap

Work: `FW-ID-01`

### REQ-ID-REGISTER-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-REGISTER-01`
RequirementText: Provide email/password registration.
ContentLocator: `Email/password registration`
Owner: Platform identity owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Unauthenticated registration with abuse protection.
AT: Planned artifact: email/password registration and abuse-protection AppHost scenario receipt in `FW-ID-01`; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Account-creation abuse.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-CONFIRM-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-CONFIRM-01`
RequirementText: Provide email confirmation.
ContentLocator: `- Email/password registration, confirmation, single-use resendable confirmation links, login, password recovery that avoids account enumeration, and password changes that invalidate all sessions.`

SourcePosition: Structural disambiguator only, not source text: `confirmation segment`.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Possession of the verified email address.
AT: Planned artifact: verified-email confirmation AppHost scenario receipt in `FW-ID-01`; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unverified account activation.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-CONFIRM-RESEND-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-CONFIRM-RESEND-01`
RequirementText: Confirmation links are single-use and resendable.
ContentLocator: `- Email/password registration, confirmation, single-use resendable confirmation links, login, password recovery that avoids account enumeration, and password changes that invalidate all sessions.`

SourcePosition: Structural disambiguator only, not source text: `single-use resendable confirmation-links segment`.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Link replay prevention and self-service resend rate limiting.
AT: Planned artifact: single-use confirmation-link replay and resend-rate-limit scenario receipt in `FW-ID-01`; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Confirmation-token replay.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-LOGIN-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-LOGIN-01`
RequirementText: Provide login.
ContentLocator: `- Email/password registration, confirmation, single-use resendable confirmation links, login, password recovery that avoids account enumeration, and password changes that invalidate all sessions.`

SourcePosition: Structural disambiguator only, not source text: `login segment`.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Credential verification with secure session issuance.
AT: Planned artifact: credential-verification and secure-session-issuance AppHost scenario receipt in `FW-ID-01`; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Authentication bypass.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-RECOVERY-NONENUM-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-RECOVERY-NONENUM-01`
ContentLocator: `- Email/password registration, confirmation, single-use resendable confirmation links, login, password recovery that avoids account enumeration, and password changes that invalidate all sessions.`
RequirementText: Password recovery that avoids account enumeration.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Recovery requests reveal no account-existence state.
AT: Planned artifact: password-recovery account-enumeration denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Account enumeration enables targeted account takeover.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-PASSWORD-INVALIDATE-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-PASSWORD-INVALIDATE-01`
RequirementText: A password change invalidates all sessions.
ContentLocator: `- Email/password registration, confirmation, single-use resendable confirmation links, login, password recovery that avoids account enumeration, and password changes that invalidate all sessions.`

SourcePosition: Structural disambiguator only, not source text: `password-change session-invalidation segment`.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: N/A[SP-ACCOUNT;product security authority;no streaming contract;real AppHost evidence]
.NET: N/A[SP-ACCOUNT;SDK architecture authority;Dashboard account flow;real AppHost evidence]
TS: N/A[SP-ACCOUNT;SDK architecture authority;Dashboard account flow;real AppHost evidence]
Dashboard: gap
MCP: N/A[SP-ACCOUNT;product security authority;human account recovery flow;real AppHost evidence]
Auth: Reauthenticated self identity.
AT: Planned artifact: password-change session-invalidation AppHost scenario receipt in `FW-ID-01`; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Compromised session remains usable after password change.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-OIDC-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`

RequirementID: `REQ-ID-OIDC-01`

ContentLocator: `- Google and GitHub login linked to an existing account by verified email; MFA enrollment, challenge, recovery, re-authentication to disable MFA, and secure session management.`

SourcePosition: Structural disambiguator only, not source text: `Google verified-email linking segment`.

RequirementText: Link Google login to an existing account only through verified email.

Owner: Platform identity lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Verified identity binding and anti-account-linking-confusion controls.

AT: Planned artifact: verified-email Google account-linking authorization-denial evidence; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: OIDC account-linking takeover.

N/A: gap

Work: `FW-ID-01`

### REQ-ID-GITHUB-LINK-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-GITHUB-LINK-01`
RequirementText: Link GitHub login to an existing account by verified email.
ContentLocator: `- Google and GitHub login linked to an existing account by verified email; MFA enrollment, challenge, recovery, re-authentication to disable MFA, and secure session management.`

SourcePosition: Structural disambiguator only, not source text: `GitHub verified-email linking segment`.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: N/A[SP-ACCOUNT;product security authority;no streaming contract;real AppHost evidence]
.NET: N/A[SP-ACCOUNT;SDK architecture authority;Dashboard identity flow;real AppHost evidence]
TS: N/A[SP-ACCOUNT;SDK architecture authority;Dashboard identity flow;real AppHost evidence]
Dashboard: gap
MCP: N/A[SP-ACCOUNT;product security authority;human OAuth flow;real AppHost evidence]
Auth: Verified-email identity binding.
AT: Planned artifact: GitHub verified-email account-linking AppHost scenario receipt in `FW-ID-01`; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: OAuth account-linking takeover.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-MFA-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`

RequirementID: `REQ-ID-MFA-01`

ContentLocator: `- Google and GitHub login linked to an existing account by verified email; MFA enrollment, challenge, recovery, re-authentication to disable MFA, and secure session management.`

SourcePosition: Structural disambiguator only, not source text: `MFA enrollment segment`.

RequirementText: Provide MFA enrollment.

Owner: Platform identity lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Self identity, MFA challenge, and recent reauthentication.

AT: Planned artifact: MFA enrollment binding and unenrolled-user denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: MFA bypass or irrecoverable account lockout.

N/A: gap

Work: `FW-ID-01`

### REQ-ID-MFA-CHALLENGE-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-MFA-CHALLENGE-01`
ContentLocator: `- Google and GitHub login linked to an existing account by verified email; MFA enrollment, challenge, recovery, re-authentication to disable MFA, and secure session management.`
RequirementText: MFA challenge.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Enrolled account holder must satisfy the MFA challenge before session issuance.
AT: Planned artifact: MFA challenge session-issuance denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: MFA challenge bypass permits account takeover.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-MFA-RECOVERY-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-MFA-RECOVERY-01`
ContentLocator: `- Google and GitHub login linked to an existing account by verified email; MFA enrollment, challenge, recovery, re-authentication to disable MFA, and secure session management.`
RequirementText: MFA recovery.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: MFA recovery proves self identity without silently weakening the MFA policy.
AT: Planned artifact: MFA recovery proof and unauthorized-recovery denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Recovery bypasses MFA or permanently locks out the account holder.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-MFA-DISABLE-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-MFA-DISABLE-01`
RequirementText: Disabling MFA requires re-authentication.
ContentLocator: `- Google and GitHub login linked to an existing account by verified email; MFA enrollment, challenge, recovery, re-authentication to disable MFA, and secure session management.`

SourcePosition: Structural disambiguator only, not source text: `re-authentication to disable MFA segment`.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: N/A[SP-ACCOUNT;product security authority;no streaming contract;real AppHost evidence]
.NET: N/A[SP-ACCOUNT;SDK architecture authority;Dashboard security flow;real AppHost evidence]
TS: N/A[SP-ACCOUNT;SDK architecture authority;Dashboard security flow;real AppHost evidence]
Dashboard: gap
MCP: N/A[SP-ACCOUNT;product security authority;human MFA security flow;real AppHost evidence]
Auth: Fresh re-authentication by the account holder.
AT: Planned artifact: MFA-disable fresh-reauthentication AppHost scenario receipt in `FW-ID-01`; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: MFA is disabled after session theft.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-PASSKEY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`

RequirementID: `REQ-ID-PASSKEY-01`

ContentLocator: `MFA/passkeys/recovery`

RequirementText: Deliver and prove passkeys where supported, including recovery behavior.

Owner: Platform identity lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Registered credential bound to self identity; recovery cannot weaken MFA.

AT: Planned artifact: passkey unsupported-device fallback and recovery real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Credential loss or phishing-resistant authentication regression.

N/A: gap

Work: `FW-ID-01`

### REQ-ID-SESSION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`

RequirementID: `REQ-ID-SESSION-01`

ContentLocator: `- Google and GitHub login linked to an existing account by verified email; MFA enrollment, challenge, recovery, re-authentication to disable MFA, and secure session management.`

SourcePosition: Structural disambiguator only, not source text: `secure session-management segment`.

RequirementText: Provide secure session management.

Owner: Platform identity lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Self identity, device binding, revocation, trusted-IP policy.

AT: Planned artifact: secure-session inspection and cross-user revocation denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Uncontrolled persistent sessions.

N/A: gap

Work: `FW-ID-01`

### REQ-ID-PROFILE-NAME-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-PROFILE-NAME-01`
ContentLocator: `- Profile management for name, phone, email-change verification, password, providers, MFA, sessions, and audit/security events.`
RequirementText: Profile management for name.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Authenticated self identity may manage only its own name.
AT: Planned artifact: self-profile name update and cross-user authorization denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: One account changes another account's identity data.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-PROFILE-PHONE-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-PROFILE-PHONE-01`
ContentLocator: `- Profile management for name, phone, email-change verification, password, providers, MFA, sessions, and audit/security events.`
RequirementText: Profile management for phone.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Authenticated self identity may manage only its own phone.
AT: Planned artifact: self-profile phone update and cross-user authorization denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unverified or cross-account contact data changes.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-EMAIL-CHANGE-VERIFY-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-EMAIL-CHANGE-VERIFY-01`
ContentLocator: `- Profile management for name, phone, email-change verification, password, providers, MFA, sessions, and audit/security events.`
RequirementText: Profile management for email-change verification.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Authenticated self identity and possession of the replacement email address.
AT: Planned artifact: replacement-email possession verification and replay denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unverified email replacement causes account takeover.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-PROFILE-PASSWORD-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-PROFILE-PASSWORD-01`
ContentLocator: `- Profile management for name, phone, email-change verification, password, providers, MFA, sessions, and audit/security events.`
RequirementText: Profile management for password.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Reauthenticated self identity manages its password.
AT: Planned artifact: reauthenticated password change and session invalidation real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Password change enables account takeover or leaves a compromised credential active.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-PROFILE-PROVIDERS-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-PROFILE-PROVIDERS-01`
ContentLocator: `- Profile management for name, phone, email-change verification, password, providers, MFA, sessions, and audit/security events.`
RequirementText: Profile management for providers.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Authenticated self identity manages only its own linked providers.
AT: Planned artifact: linked-provider self-management and cross-user authorization denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unauthorized provider linking or unlinking causes account takeover.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-PROFILE-MFA-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-PROFILE-MFA-01`
ContentLocator: `- Profile management for name, phone, email-change verification, password, providers, MFA, sessions, and audit/security events.`
RequirementText: Profile management for MFA.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Authenticated self identity manages MFA with challenge and reauthentication controls.
AT: Planned artifact: profile MFA management with challenge and reauthentication real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: MFA state is changed without the account holder's authorization.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-PROFILE-SESSIONS-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-PROFILE-SESSIONS-01`
ContentLocator: `- Profile management for name, phone, email-change verification, password, providers, MFA, sessions, and audit/security events.`
RequirementText: Profile management for sessions.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Authenticated self identity can inspect and revoke only its own sessions.
AT: Planned artifact: self-session listing and foreign-session revocation denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Session information disclosure or unauthorized session revocation.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-PROFILE-AUDIT-EVENTS-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-PROFILE-AUDIT-EVENTS-01`
ContentLocator: `- Profile management for name, phone, email-change verification, password, providers, MFA, sessions, and audit/security events.`
RequirementText: Profile management for audit events.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Authenticated self identity accesses only audit events it is authorized to view.
AT: Planned artifact: self security-audit event visibility and cross-user tenant-denial evidence; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Audit-event disclosure, omission, or tampering obscures account activity.
N/A: gap
Work: `FW-ID-01`

### REQ-ID-PROFILE-SECURITY-EVENTS-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ID-PROFILE-SECURITY-EVENTS-01`
ContentLocator: `- Profile management for name, phone, email-change verification, password, providers, MFA, sessions, and audit/security events.`
RequirementText: Profile management for security events.
Owner: Platform identity owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Authenticated self identity accesses only security events it is authorized to view.
AT: Planned artifact: self security-event visibility and cross-user tenant-denial evidence; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Security-event disclosure or suppression delays incident response.
N/A: gap
Work: `FW-ID-01`

### REQ-ONB-COMPLETE-ACCOUNT-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ONB-COMPLETE-ACCOUNT-01`
ContentLocator: `- Resumable onboarding that requires complete account information, provider-hosted payment-method collection and validation, optional MFA enrollment, first organization, region/backup-region selection, and first project before the user reaches the project dashboard.`
RequirementText: Complete account information.
Owner: Platform onboarding owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Authenticated self identity completes only its own account information.
AT: Planned artifact: confirmed-account onboarding completion and incomplete-account denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Incomplete account state reaches later onboarding steps.
N/A: gap
Work: `FW-ID-01`

### REQ-ONB-PAYMENT-COLLECTION-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ONB-PAYMENT-COLLECTION-01`
ContentLocator: `- Resumable onboarding that requires complete account information, provider-hosted payment-method collection and validation, optional MFA enrollment, first organization, region/backup-region selection, and first project before the user reaches the project dashboard.`
RequirementText: Provider-hosted payment-method collection.
Owner: Platform onboarding owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Authenticated self identity uses only the approved provider-hosted payment collection flow.
AT: Planned artifact: onboarding payment-method collection isolation real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Payment data bypasses the provider-hosted collection boundary.
N/A: gap
Work: `FW-ID-01`

### REQ-ONB-PAYMENT-VALIDATION-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ONB-PAYMENT-VALIDATION-01`
ContentLocator: `- Resumable onboarding that requires complete account information, provider-hosted payment-method collection and validation, optional MFA enrollment, first organization, region/backup-region selection, and first project before the user reaches the project dashboard.`
RequirementText: Payment-method validation.
Owner: Platform onboarding owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Authenticated self identity proceeds only after provider payment-method validation.
AT: Planned artifact: onboarding payment-method validation failure evidence; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: An invalid payment method permits unapproved service access.
N/A: gap
Work: `FW-ID-01`

### REQ-ONB-OPTIONAL-MFA-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ONB-OPTIONAL-MFA-01`
ContentLocator: `- Resumable onboarding that requires complete account information, provider-hosted payment-method collection and validation, optional MFA enrollment, first organization, region/backup-region selection, and first project before the user reaches the project dashboard.`
RequirementText: Optional MFA enrollment.
Owner: Platform onboarding owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Authenticated self identity may elect MFA enrollment without bypassing its controls.
AT: Planned artifact: optional onboarding MFA enrollment and skip-path real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Optional enrollment is misrepresented as completed or bypasses MFA safeguards.
N/A: gap
Work: `FW-ID-01`

### REQ-ONB-FIRST-ORG-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ONB-FIRST-ORG-01`
ContentLocator: `- Resumable onboarding that requires complete account information, provider-hosted payment-method collection and validation, optional MFA enrollment, first organization, region/backup-region selection, and first project before the user reaches the project dashboard.`
RequirementText: First organization.
Owner: Platform onboarding owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Authenticated self identity creates its first organization under organization-owner authority.
AT: Planned artifact: first-organization creation and cross-user tenant-denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: First organization is absent, inaccessible, or created in the wrong tenant.
N/A: gap
Work: `FW-ID-01`

### REQ-ONB-PRIMARY-REGION-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ONB-PRIMARY-REGION-01`
ContentLocator: `- Resumable onboarding that requires complete account information, provider-hosted payment-method collection and validation, optional MFA enrollment, first organization, region/backup-region selection, and first project before the user reaches the project dashboard.`
RequirementText: Region selection.
Owner: Platform onboarding owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Organization owner selects a primary region for the first project.
AT: Planned artifact: onboarding primary-region selection and invalid-region denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: First project has no valid primary region.
N/A: gap
Work: `FW-ID-01`

### REQ-ONB-BACKUP-REGION-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ONB-BACKUP-REGION-01`
ContentLocator: `- Resumable onboarding that requires complete account information, provider-hosted payment-method collection and validation, optional MFA enrollment, first organization, region/backup-region selection, and first project before the user reaches the project dashboard.`
RequirementText: Backup-region selection.
Owner: Platform onboarding owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Organization owner selects the backup region for the first project.
AT: Planned artifact: onboarding backup-region selection and same-region denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: First project has no valid backup region.
N/A: gap
Work: `FW-ID-01`

### REQ-ONB-FIRST-PROJECT-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ONB-FIRST-PROJECT-01`
ContentLocator: `- Resumable onboarding that requires complete account information, provider-hosted payment-method collection and validation, optional MFA enrollment, first organization, region/backup-region selection, and first project before the user reaches the project dashboard.`
RequirementText: First project.
Owner: Platform onboarding owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Organization owner creates the first project in the accessible organization.
AT: Planned artifact: first-project creation with organization tenant isolation real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Dashboard entry has no initialized project context.
N/A: gap
Work: `FW-ID-01`

### REQ-ONB-DASHBOARD-GATE-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ONB-DASHBOARD-GATE-01`
ContentLocator: `- Resumable onboarding that requires complete account information, provider-hosted payment-method collection and validation, optional MFA enrollment, first organization, region/backup-region selection, and first project before the user reaches the project dashboard.`
RequirementText: First project before the user reaches the project dashboard.
Owner: Platform onboarding owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Dashboard access requires completion of each mandatory onboarding prerequisite.
AT: Planned artifact: Dashboard onboarding-completion gate authorization-denial evidence; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Incomplete onboarding reaches a project dashboard.
N/A: gap
Work: `FW-ID-01`

### REQ-ONB-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`

RequirementID: `REQ-ONB-01`

ContentLocator: `- Resumable onboarding that requires complete account information, provider-hosted payment-method collection and validation, optional MFA enrollment, first organization, region/backup-region selection, and first project before the user reaches the project dashboard.`

SourcePosition: Structural disambiguator only, not source text: `resumable onboarding segment`.

RequirementText: Make onboarding resumable.

Owner: Platform onboarding lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Self identity and organization-owner authority after organization creation.

AT: Planned artifact: end-to-end onboarding completion and incomplete-state denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Incomplete tenant initialization or payment data handling.

N/A: gap

Work: `FW-ID-01`

### REQ-ONB-ROUTE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`

RequirementID: `REQ-ONB-ROUTE-01`

ContentLocator: `- Correct routing after login: incomplete onboarding continues onboarding; otherwise restore the last accessible organization or require a valid replacement selection.`

SourcePosition: Structural disambiguator only, not source text: `incomplete-onboarding routing segment`.

RequirementText: After login, incomplete onboarding continues onboarding.

Owner: Dashboard and Platform onboarding leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Accessible organization only; denied or removed context cannot be restored.

AT: Planned artifact: onboarding route selection and cross-organization tenant-denial evidence; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Wrong-tenant dashboard context.

N/A: gap

Work: `FW-ID-01`

### REQ-ONB-ROUTE-RESTORE-ORG-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ONB-ROUTE-RESTORE-ORG-01`
ContentLocator: `- Correct routing after login: incomplete onboarding continues onboarding; otherwise restore the last accessible organization or require a valid replacement selection.`
RequirementText: Restore the last accessible organization after login.
Owner: Dashboard and Platform onboarding owners
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Only an organization that remains accessible to the authenticated user may be restored.
AT: Planned artifact: onboarding restore-organization route and stale-state denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Login restores an inaccessible or wrong-tenant organization.
N/A: gap
Work: `FW-ID-01`

### REQ-ONB-ROUTE-REPLACEMENT-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 1. Identity, account, and onboarding`
RequirementID: `REQ-ONB-ROUTE-REPLACEMENT-01`
ContentLocator: `- Correct routing after login: incomplete onboarding continues onboarding; otherwise restore the last accessible organization or require a valid replacement selection.`
RequirementText: Require a valid replacement selection after login.
Owner: Dashboard and Platform onboarding owners
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Authenticated user can select only an organization to which it has current access.
AT: Planned artifact: onboarding replacement-organization route and tenant-denial evidence; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Missing or invalid replacement selection opens the wrong tenant context.
N/A: gap
Work: `FW-ID-01`

### REQ-ORG-CREATE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-ORG-CREATE-01`

ContentLocator: `Organization creation`

RequirementText: Organization creation.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization creation authority.

AT: Planned artifact: organization creation and cross-organization tenant-denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Tenant creation abuse.

N/A: gap

Work: `FW-AUTH-01`

### REQ-ORG-SELECTION-PERSIST-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-ORG-SELECTION-PERSIST-01`

ContentLocator: `selection persistence`

RequirementText: Selection persistence.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Only currently accessible organization.

AT: Planned artifact: organization selection persistence and foreign-organization tenant-denial evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Inaccessible tenant restore.

N/A: gap

Work: `FW-AUTH-01`

### REQ-ORG-SETTINGS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-ORG-SETTINGS-01`

ContentLocator: `settings`

RequirementText: Organization settings.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner authority.

AT: Planned artifact: organization-settings update and non-owner authorization-denial evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unauthorized configuration.

N/A: gap

Work: `FW-AUTH-01`

### REQ-ORG-DELETE-SAFEGUARDS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-ORG-DELETE-SAFEGUARDS-01`

ContentLocator: `deletion safeguards`

RequirementText: Deletion safeguards.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner with safeguards.

AT: Planned artifact: organization deletion safeguard authorization-denial and dependent-resource evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unsafe tenant deletion.

N/A: gap

Work: `FW-AUTH-01`

### REQ-ORG-LAST-OWNER-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-ORG-LAST-OWNER-01`

ContentLocator: `a guarantee that each organization retains at least one Organization Owner`

RequirementText: Each organization retains at least one Organization Owner.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Last Organization Owner cannot be removed or demoted.

AT: Planned artifact: last-organization-owner removal denial evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Tenant lockout.

N/A: gap

Work: `FW-AUTH-01`

### REQ-INVITE-PENDING-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-INVITE-PENDING-01`

ContentLocator: `pending`

RequirementText: Invitations have pending state.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Inviter authority.

AT: Planned artifact: pending organization invitation visibility and foreign-organization tenant-denial evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Untracked invitation state.

N/A: gap

Work: `FW-AUTH-01`

### REQ-INVITE-ACCEPTED-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-INVITE-ACCEPTED-01`

ContentLocator: `accepted`

RequirementText: Invitations have accepted state.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Acceptance is organization-bound.

AT: Planned artifact: invitation acceptance membership grant and cross-organization tenant-denial evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Wrong-tenant membership.

N/A: gap

Work: `FW-AUTH-01`

### REQ-INVITE-DECLINED-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-INVITE-DECLINED-01`

ContentLocator: `declined`

RequirementText: Invitations have declined state.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Only invitee declines.

AT: Planned artifact: invitation decline state transition and later-acceptance denial evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Invitation state spoofing.

N/A: gap

Work: `FW-AUTH-01`

### REQ-INVITE-EXPIRED-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-INVITE-EXPIRED-01`

ContentLocator: `expired`

RequirementText: Invitations have expired state.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Expired invitations cannot grant membership.

AT: Planned artifact: expired invitation acceptance denial evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Expired-invite replay.

N/A: gap

Work: `FW-AUTH-01`

### REQ-INVITE-RESEND-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-INVITE-RESEND-01`

ContentLocator: `- Invitations with pending/accepted/declined/expired state, resend/cancel behavior, duplicate protection, and acceptance that grants organization membership but not implicit project access.`

SourcePosition: Structural disambiguator only, not source text: `resend/cancel behavior segment`.

RequirementText: Invitations support resend behavior.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Inviter authority.

AT: Planned artifact: invitation resend rotation and old-link replay denial evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Invitation replay.

N/A: gap

Work: `FW-AUTH-01`

### REQ-INVITE-CANCEL-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-INVITE-CANCEL-01`

ContentLocator: `cancel behavior`

RequirementText: Invitations support cancel behavior.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Canceled invitations cannot be accepted.

AT: Planned artifact: invitation cancellation and canceled-link acceptance denial evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Canceled invitation grants access.

N/A: gap

Work: `FW-AUTH-01`

### REQ-INVITE-DUPLICATE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-INVITE-DUPLICATE-01`

ContentLocator: `duplicate protection`

RequirementText: Invitations have duplicate protection.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Unique active invitation.

AT: Planned artifact: duplicate invitation prevention evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Duplicate membership.

N/A: gap

Work: `FW-AUTH-01`

### REQ-INVITE-ACCEPT-NO-PROJECT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-INVITE-ACCEPT-NO-PROJECT-01`

ContentLocator: `acceptance that grants organization membership but not implicit project access`

RequirementText: Invitation acceptance grants organization membership but not implicit project access.

Owner: Platform projects lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Accepted member has no project grant.

AT: Planned artifact: invitation acceptance without implicit project access evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Implicit project privilege.

N/A: gap

Work: `FW-AUTH-01`

### REQ-MEMBERSHIP-LIST-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-MEMBERSHIP-LIST-01`

ContentLocator: `Membership listing`

RequirementText: Membership listing.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization-scoped authority.

AT: Planned artifact: organization membership listing and cross-organization tenant-denial evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Membership disclosure.

N/A: gap

Work: `FW-AUTH-01`

### REQ-MEMBERSHIP-ROLES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-MEMBERSHIP-ROLES-01`

ContentLocator: `roles`

RequirementText: Membership roles.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Actor authority ceiling.

AT: Planned artifact: membership role change and unauthorized role-change denial evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unauthorized role elevation.

N/A: gap

Work: `FW-AUTH-01`

### REQ-MEMBERSHIP-REMOVE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-MEMBERSHIP-REMOVE-01`

ContentLocator: `removal`

RequirementText: Membership removal.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized remover; owner invariant applies.

AT: Planned artifact: membership removal and immediate project-access revocation evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unauthorized removal.

N/A: gap

Work: `FW-AUTH-01`

### REQ-MEMBERSHIP-DEPART-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-MEMBERSHIP-DEPART-01`

ContentLocator: `voluntary departure`

RequirementText: Voluntary departure.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Self membership; owner invariant applies.

AT: Planned artifact: self-departure last-owner safeguard denial evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Orphaned organization.

N/A: gap

Work: `FW-AUTH-01`

### REQ-MEMBERSHIP-IMMEDIATE-REVOKE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-MEMBERSHIP-IMMEDIATE-REVOKE-01`

ContentLocator: `immediate revocation`

RequirementText: Membership changes provide immediate revocation.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Revoked authority denied immediately.

AT: Planned artifact: immediate membership role-revocation authorization evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Stale access.

N/A: gap

Work: `FW-AUTH-01`

### REQ-MEMBERSHIP-IMMUTABLE-AUDIT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-MEMBERSHIP-IMMUTABLE-AUDIT-01`

ContentLocator: `immutable audit trails for all access changes`

RequirementText: All access changes have immutable audit trails.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Tenant-scoped immutable audit.

AT: Planned artifact: immutable membership-change audit evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Audit loss.

N/A: gap

Work: `FW-AUTH-01`

### REQ-PROJECT-CREATE-MANAGE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PROJECT-CREATE-MANAGE-01`

ContentLocator: `Project creation and management`

RequirementText: Project creation and management.

Owner: Platform projects lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner or delegated authority.

AT: Planned artifact: project creation and cross-organization tenant-denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-PROJ-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unauthorized project action.

N/A: gap

Work: `FW-PROJ-02`

### REQ-PROJECT-UNIQUE-NAME-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PROJECT-UNIQUE-NAME-01`

ContentLocator: `unique names per organization`

RequirementText: Projects have unique names per organization.

Owner: Platform projects lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization-scoped uniqueness.

AT: Planned artifact: same-organization duplicate project-name denial and cross-organization allowance evidence; Work contract: `FW-PROJ-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Ambiguous project identity.

N/A: gap

Work: `FW-PROJ-02`

### REQ-PROJECT-PRIMARY-REGIONS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PROJECT-PRIMARY-REGIONS-01`

ContentLocator: `one-or-more primary regions`

RequirementText: Projects have one or more primary regions.

Owner: Platform projects lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Validated placement authority.

AT: Planned artifact: project primary-region selection validation evidence; Work contract: `FW-PROJ-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Invalid primary placement.

N/A: gap

Work: `FW-PROJ-02`

### REQ-PROJECT-ONE-BACKUP-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PROJECT-ONE-BACKUP-01`

ContentLocator: `exactly one backup region`

RequirementText: Projects have exactly one backup region.

Owner: Platform projects lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Validated backup placement.

AT: Planned artifact: exactly-one backup-region constraint denial evidence; Work contract: `FW-PROJ-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Ambiguous backup.

N/A: gap

Work: `FW-PROJ-02`

### REQ-PROJECT-SAFE-REGION-CHANGE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PROJECT-SAFE-REGION-CHANGE-01`

ContentLocator: `safe region-change constraints`

RequirementText: Projects enforce safe region-change constraints.

Owner: Platform projects lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Safe transition authority.

AT: Planned artifact: safe region-change rollback and unsafe-change denial evidence; Work contract: `FW-PROJ-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unsafe regional transition.

N/A: gap

Work: `FW-PROJ-02`

### REQ-PROJECT-EXPLICIT-DELETE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PROJECT-EXPLICIT-DELETE-01`

ContentLocator: `explicit deletion`

RequirementText: Projects require explicit deletion.

Owner: Platform projects lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized explicit deletion.

AT: Planned artifact: explicit project deletion confirmation and unauthorized-deletion denial evidence; Work contract: `FW-PROJ-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Accidental deletion.

N/A: gap

Work: `FW-PROJ-02`

### REQ-PROJECT-OWNER-INVARIANT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PROJECT-OWNER-INVARIANT-01`

ContentLocator: `at least one Project Owner`

RequirementText: Each project retains at least one Project Owner.

Owner: Platform projects lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Last Project Owner cannot be removed or demoted.

AT: Planned artifact: last-project-owner removal denial evidence; Work contract: `FW-PROJ-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Project lockout.

N/A: gap

Work: `FW-PROJ-02`

### REQ-RBAC-ORG-OWNER-ALL-PROJECTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-RBAC-ORG-OWNER-ALL-PROJECTS-01`

ContentLocator: `Organization Owners have organization-wide project access`

RequirementText: Organization Owners have organization-wide project access.

Owner: Platform projects lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner in its organization.

AT: Planned artifact: organization-owner all-project authorization evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Missing or cross-tenant access.

N/A: gap

Work: `FW-AUTH-01`

### REQ-RBAC-PROJECT-OWNER-OWN-ONLY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-RBAC-PROJECT-OWNER-OWN-ONLY-01`

ContentLocator: `Project Owners administer only their projects`

RequirementText: Project Owners administer only their projects.

Owner: Platform projects lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project Owner assigned-project boundary.

AT: Planned artifact: project-owner foreign-project authorization-denial evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Cross-project administration.

N/A: gap

Work: `FW-AUTH-01`

### REQ-RBAC-MEMBER-EXPLICIT-GRANT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-RBAC-MEMBER-EXPLICIT-GRANT-01`

ContentLocator: `Members receive only explicitly granted project access`

RequirementText: Members receive only explicitly granted project access.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Explicit project grant required.

AT: Planned artifact: member explicit-project-grant and ungranted-project denial evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Implicit access.

N/A: gap

Work: `FW-AUTH-01`

### REQ-RBAC-NO-ESCALATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-RBAC-NO-ESCALATION-01`

ContentLocator: `No user can grant privilege above their authority`

RequirementText: No user can grant privilege above their authority.

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Actor authority is maximum grant.

AT: Planned artifact: above-authority role-grant denial evidence; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Privilege escalation.

N/A: gap

Work: `FW-AUTH-01`

### REQ-ADMIN-DISTINCT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-ADMIN-DISTINCT-01`

ContentLocator: `A distinct, audited TerraScale Admin role`

RequirementText: A distinct TerraScale Admin role exists.

Owner: Platform Admin lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Platform admin distinct from customer roles.

AT: Planned artifact: distinct TerraScale Admin role and customer-organization tenant-denial evidence; Work contract: `FW-ADMIN-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Authority conflation.

N/A: gap

Work: `FW-ADMIN-04`

### REQ-ADMIN-AUDITED-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-ADMIN-AUDITED-01`

ContentLocator: `audited TerraScale Admin role`

RequirementText: TerraScale Admin activity is audited.

Owner: Platform Admin lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Immutable attributable admin audit.

AT: Planned artifact: mandatory TerraScale Admin activity audit evidence; Work contract: `FW-ADMIN-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unauditable operations.

N/A: gap

Work: `FW-ADMIN-04`

### REQ-ADMIN-NO-SILENT-MEMBERSHIP-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-ADMIN-NO-SILENT-MEMBERSHIP-01`

ContentLocator: `never silently represented as customer-organization membership`

RequirementText: TerraScale Admin is never silently represented as customer-organization membership.

Owner: Platform Admin lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Admin cannot imply customer membership.

AT: Planned artifact: TerraScale Admin non-membership representation denial evidence; Work contract: `FW-ADMIN-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Silent tenant access.

N/A: gap

Work: `FW-ADMIN-04`

### REQ-PRODUCT-DATABASE-PROJECT-SCOPED-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-DATABASE-PROJECT-SCOPED-01`

ContentLocator: `project-scoped databases`

RequirementText: Databases are project-scoped.

Owner: Platform projects lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project access and tenant isolation.

AT: Planned artifact: project-scoped database access and cross-project tenant-denial evidence; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Database cross-project access.

N/A: gap

Work: `FW-DB-02`

### REQ-PRODUCT-QUEUE-SUPPORTED-TYPE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-QUEUE-SUPPORTED-TYPE-01`

ContentLocator: `queues with explicit supported type`

RequirementText: Queues have an explicit supported type.

Owner: Platform products lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project access and tenant isolation.

AT: Planned artifact: supported queue-type validation denial evidence; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unsupported queue semantics.

N/A: gap

Work: `FW-DB-02`

### REQ-PRODUCT-QUEUE-PROVISIONING-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-QUEUE-PROVISIONING-01`

ContentLocator: `provisioning`

RequirementText: Queues support provisioning.

Owner: Platform products lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project provisioning authority.

AT: Planned artifact: queue provisioning and cross-project tenant-denial real two-user/two-org AppHost scenario receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unauthorized provisioning.

N/A: gap

Work: `FW-DB-02`

### REQ-PRODUCT-QUEUE-PUBLISH-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-QUEUE-PUBLISH-01`

ContentLocator: `publish`

RequirementText: Queues support publish lifecycle.

Owner: Platform products lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Explicit project publish grant.

AT: Planned artifact: queue publish authorization and cross-project tenant-denial evidence; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unauthorized publication.

N/A: gap

Work: `FW-DB-02`

### REQ-PRODUCT-QUEUE-CONSUME-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-QUEUE-CONSUME-01`

ContentLocator: `consume`

RequirementText: Queues support consume lifecycle.

Owner: Platform products lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Explicit project consume grant.

AT: Planned artifact: queue consume authorization and cross-project tenant-denial evidence; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unauthorized consumption.

N/A: gap

Work: `FW-DB-02`

### REQ-PRODUCT-QUEUE-DEAD-LETTER-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-QUEUE-DEAD-LETTER-01`

ContentLocator: `dead-letter lifecycle`

RequirementText: Queues support dead-letter lifecycle.

Owner: Platform products lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Tenant-safe dead-letter authority.

AT: Planned artifact: queue dead-letter lifecycle authorization evidence; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dead-letter leakage.

N/A: gap

Work: `FW-DB-02`

### REQ-PRODUCT-QUEUE-OBSERVABILITY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-QUEUE-OBSERVABILITY-01`

ContentLocator: `tenant-safe observability`

RequirementText: Queues provide tenant-safe observability.

Owner: Platform products lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized project observability.

AT: Planned artifact: queue tenant-safe observability cross-project denial evidence; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Observability leakage.

N/A: gap

Work: `FW-DB-02`

### REQ-PRODUCT-AUTH-INDEPENDENT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-AUTH-INDEPENDENT-01`

ContentLocator: `an independent, ready-to-integrate Authentication product configuration`

RequirementText: Authentication has an independent, ready-to-integrate product configuration.

Owner: Platform products lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project access and tenant isolation.

AT: Planned artifact: independent Authentication product configuration isolation evidence; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Product coupling.

N/A: gap

Work: `FW-DB-02`

### REQ-PRODUCT-AUTH-USERS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-AUTH-USERS-01`

ContentLocator: `with users`

RequirementText: Authentication product configuration includes users.

Owner: Platform products lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized project access.

AT: Planned artifact: Authentication product users cross-project tenant-denial evidence; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: User leakage.

N/A: gap

Work: `FW-DB-02`

### REQ-PRODUCT-AUTH-SESSIONS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-AUTH-SESSIONS-01`

ContentLocator: `sessions`

RequirementText: Authentication product configuration includes sessions.

Owner: Platform products lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized project access.

AT: Planned artifact: Authentication product sessions cross-project tenant-denial evidence; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Session leakage.

N/A: gap

Work: `FW-DB-02`

### REQ-PRODUCT-AUTH-PROVIDERS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-AUTH-PROVIDERS-01`

ContentLocator: `providers`

RequirementText: Authentication product configuration includes providers.

Owner: Platform products lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized project access.

AT: Planned artifact: Authentication product providers cross-project tenant-denial evidence; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Provider exposure.

N/A: gap

Work: `FW-DB-02`

### REQ-PRODUCT-AUTH-SAFE-DISABLE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-AUTH-SAFE-DISABLE-01`

ContentLocator: `safe disable/impact handling`

RequirementText: Authentication product configuration has safe disable and impact handling.

Owner: Platform products lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized lifecycle with impact safeguards.

AT: Planned artifact: Authentication safe-disable impact handling and rollback evidence; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unsafe disablement.

N/A: gap

Work: `FW-DB-02`

### REQ-PRODUCT-SHARED-ACCESS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-SHARED-ACCESS-01`

ContentLocator: `project access`

RequirementText: Each product follows the same project access rules.

Owner: Platform products lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized project boundary.

AT: Planned artifact: shared product project-access authorization and tenant-denial evidence; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Inconsistent access.

N/A: gap

Work: `FW-DB-02`

### REQ-PRODUCT-SHARED-AUDIT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-SHARED-AUDIT-01`

ContentLocator: `audit`

RequirementText: Each product follows the same audit rules.

Owner: Platform products lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized project audit boundary.

AT: Planned artifact: shared product audit isolation evidence; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Inconsistent audit.

N/A: gap

Work: `FW-DB-02`

### REQ-PRODUCT-SHARED-REGIONAL-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-SHARED-REGIONAL-01`

ContentLocator: `regional`

RequirementText: Each product follows the same regional rules.

Owner: Platform products lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized project regional boundary.

AT: Planned artifact: shared product regional constraint and rollback evidence; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Inconsistent regional rules.

N/A: gap

Work: `FW-DB-02`

### REQ-PRODUCT-SHARED-QUOTA-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-SHARED-QUOTA-01`

ContentLocator: `quota`

RequirementText: Each product follows the same quota rules.

Owner: Platform products lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized project quota boundary.

AT: Planned artifact: shared product quota enforcement authorization evidence; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Inconsistent quota enforcement.

N/A: gap

Work: `FW-DB-02`

### REQ-PRODUCT-SHARED-LIFECYCLE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-SHARED-LIFECYCLE-01`

ContentLocator: `lifecycle`

RequirementText: Each product follows the same lifecycle rules.

Owner: Platform products lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized project lifecycle boundary.

AT: Planned artifact: shared product lifecycle authorization and tenant-denial evidence; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Inconsistent lifecycle.

N/A: gap

Work: `FW-DB-02`

### REQ-PRODUCT-SHARED-DELETION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 2. Organizations, projects, and access control`

RequirementID: `REQ-PRODUCT-SHARED-DELETION-01`

ContentLocator: `deletion`

RequirementText: Each product follows the same deletion rules.

Owner: Platform products lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized project deletion boundary.

AT: Planned artifact: shared product deletion confirmation and tenant-denial evidence; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Inconsistent deletion.

N/A: gap

Work: `FW-DB-02`

### REQ-DB-CREATE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-CREATE-01`

ContentLocator: `Project-scoped database creation`

RequirementText: Create a database scoped to exactly one authorized project.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project authorization and idempotent creation.

AT: Planned artifact: database creation and cross-project tenant-denial AppHost scenario receipt; Work contract: `FW-DB-PROVISION-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unauthorized or duplicate database creation.

N/A: gap

Work: `FW-DB-PROVISION-02`

### REQ-DB-NAME-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-NAME-01`

ContentLocator: `naming`

RequirementText: Assign and enforce the database naming model.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project authorization and tenant-unique naming.

AT: Planned artifact: database-name validation and duplicate-name denial evidence; Work contract: `FW-DB-PROVISION-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Name collision or cross-tenant disclosure.

N/A: gap

Work: `FW-DB-PROVISION-02`

### REQ-DB-CONFIG-REGION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-CONFIG-REGION-01`

ContentLocator: `configuration derived from project regions`

RequirementText: Derive database configuration from the project's primary regions.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project placement authorization.

AT: Planned artifact: database primary-region validation and cross-project tenant-denial evidence; Work contract: `FW-DB-PROVISION-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Database placement outside authorized regions.

N/A: gap

Work: `FW-DB-PROVISION-02`

### REQ-DB-CONFIG-BACKUP-REGION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-CONFIG-BACKUP-REGION-01`

ContentLocator: `backup region`

RequirementText: Derive database configuration from the project's exactly one backup region.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project placement authorization.

AT: Planned artifact: database backup-region constraint denial evidence; Work contract: `FW-DB-PROVISION-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Backup placement outside the approved recovery region.

N/A: gap

Work: `FW-DB-PROVISION-02`

### REQ-DB-PROVISIONING-PROGRESS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-PROVISIONING-PROGRESS-01`

ContentLocator: `provisioning progress`

RequirementText: Expose truthful provisioning progress for an authorized project database.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project access; progress contains no secrets.

AT: Planned artifact: database provisioning progress and retry-state AppHost scenario receipt; Work contract: `FW-DB-PROVISION-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Misleading progress or tenant information leakage.

N/A: gap

Work: `FW-DB-PROVISION-02`

### REQ-DB-READINESS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-READINESS-01`

ContentLocator: `readiness`

RequirementText: Expose truthful database readiness before use.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project access; readiness contains no secrets.

AT: Planned artifact: database readiness gate and premature-access denial evidence; Work contract: `FW-DB-PROVISION-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Use before the database is ready.

N/A: gap

Work: `FW-DB-PROVISION-02`

### REQ-DB-ENDPOINTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-ENDPOINTS-01`

ContentLocator: `connection endpoints`

RequirementText: Provide authorized, tenant-safe database connection endpoints.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project access; redact internal routing detail.

AT: Planned artifact: database endpoint visibility and cross-project tenant-denial evidence; Work contract: `FW-DB-PROVISION-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Endpoint disclosure or cross-tenant routing.

N/A: gap

Work: `FW-DB-PROVISION-02`

### REQ-DB-CREDENTIALS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-CREDENTIALS-01`

ContentLocator: `credentials`

RequirementText: Issue database credentials only through the supported secure lifecycle.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized credential issuance with secret redaction.

AT: Planned artifact: database credential issuance and secret-redaction evidence; Work contract: `FW-DB-CREDENTIAL-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Secret disclosure or unauthorized database access.

N/A: gap

Work: `FW-DB-CREDENTIAL-02`

### REQ-DB-ACCESS-CONTROLS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-ACCESS-CONTROLS-01`

ContentLocator: `access controls`

RequirementText: Enforce database access controls for every data-plane connection.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Least-privilege project database authorization.

AT: Planned artifact: database access-control authorization and tenant-denial evidence; Work contract: `FW-DB-SECURITY-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unauthorized data-plane access.

N/A: gap

Work: `FW-DB-SECURITY-02`

### REQ-DB-ROTATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-ROTATION-01`

ContentLocator: `rotation`

RequirementText: Rotate database credentials safely and audit the rotation.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized secret rotation with non-replayable issuance.

AT: Planned artifact: database credential rotation with prior-secret revocation and redaction evidence; Work contract: `FW-DB-CREDENTIAL-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Stale or exposed credentials remain usable.

N/A: gap

Work: `FW-DB-CREDENTIAL-02`

### REQ-DB-SAFE-REMOVAL-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-SAFE-REMOVAL-01`

ContentLocator: `safe removal`

RequirementText: Remove a project database through the safe destructive lifecycle.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project owner confirmation, retention disclosure, and audit.

AT: Planned artifact: database removal confirmation and unauthorized-deletion denial evidence; Work contract: `FW-DB-PROVISION-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Accidental irreversible database removal.

N/A: gap

Work: `FW-DB-PROVISION-02`

### REQ-DB-STATUS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-STATUS-01`

ContentLocator: `status`

RequirementText: Provide database lifecycle status.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project access and tenant-safe status.

AT: Planned artifact: database status visibility and cross-project tenant-denial evidence; Work contract: `FW-DB-OPERATE-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Incorrect status drives unsafe action.

N/A: gap

Work: `FW-DB-OPERATE-02`

### REQ-DB-EVENTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-EVENTS-01`

ContentLocator: `events`

RequirementText: Provide database lifecycle events.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project access and tenant-safe event redaction.

AT: Planned artifact: database lifecycle-event audit isolation evidence; Work contract: `FW-DB-OPERATE-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Event leakage or missed lifecycle transition.

N/A: gap

Work: `FW-DB-OPERATE-02`

### REQ-DB-SCALE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-SCALE-01`

ContentLocator: `- Production-grade lifecycle controls: status and events, scale/configuration changes, maintenance behavior, quotas, limits, backups, retention, recovery drills, point-in-time restore, cloning/branching, promotion/merge semantics where applicable, and deletion/retention controls.`

SourcePosition: Structural disambiguator only, not source text: `scale/configuration changes segment`.

RequirementText: Support authorized database scale changes.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project owner authorization and impact control.

AT: Planned artifact: database scale operation retry and failed-change rollback evidence; Work contract: `FW-DB-OPERATE-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unsafe capacity change.

N/A: gap

Work: `FW-DB-OPERATE-02`

### REQ-DB-CONFIG-CHANGE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-CONFIG-CHANGE-01`

ContentLocator: `configuration changes`

RequirementText: Support authorized database configuration changes.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project owner authorization and validated configuration.

AT: Planned artifact: database configuration-change validation and retry evidence; Work contract: `FW-DB-OPERATE-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unsafe configuration mutation.

N/A: gap

Work: `FW-DB-OPERATE-02`

### REQ-DB-MAINTENANCE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-MAINTENANCE-01`

ContentLocator: `maintenance behavior`

RequirementText: Define and operate customer-safe maintenance behavior.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized maintenance control and tenant-safe notification.

AT: Planned artifact: database maintenance scheduling and retry-safe interruption evidence; Work contract: `FW-DB-OPERATE-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unannounced or unsafe maintenance impact.

N/A: gap

Work: `FW-DB-OPERATE-02`

### REQ-DB-QUOTAS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-QUOTAS-01`

ContentLocator: `quotas`

RequirementText: Apply database quotas.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project authorization and tenant-isolated quota accounting.

AT: Planned artifact: database quota enforcement and rate-denial evidence; Work contract: `FW-DB-OPERATE-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Quota bypass or cross-tenant accounting.

N/A: gap

Work: `FW-DB-OPERATE-02`

### REQ-DB-LIMITS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-LIMITS-01`

ContentLocator: `limits`

RequirementText: Apply database limits.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project authorization and tenant-isolated limit enforcement.

AT: Planned artifact: database service-limit denial and audit evidence; Work contract: `FW-DB-OPERATE-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Limit bypass or denial of service.

N/A: gap

Work: `FW-DB-OPERATE-02`

### REQ-DB-BACKUPS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-BACKUPS-01`

ContentLocator: `backups`

RequirementText: Create and manage supported database backups.

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project recovery authorization and encrypted backup scope.

AT: Planned artifact: database backup completion and cross-project recovery denial evidence; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Backup loss or unauthorized restoration.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-DB-RETENTION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-RETENTION-01`

ContentLocator: `retention`

RequirementText: Enforce database backup and data retention policy.

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized policy changes and retention audit.

AT: Planned artifact: database backup-retention enforcement evidence; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Retention violation or premature data loss.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-DB-RECOVERY-DRILLS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-RECOVERY-DRILLS-01`

ContentLocator: `recovery drills`

RequirementText: Perform and evidence database recovery drills.

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Controlled recovery authority and isolated drill data.

AT: Planned artifact: destructive recovery drill RPO-RTO evidence; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Untested recovery procedure.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-DB-PITR-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-PITR-01`

ContentLocator: `point-in-time restore`

RequirementText: Restore a database to a supported point in time.

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Explicit recovery authorization, target confirmation, and audit.

AT: Planned artifact: point-in-time recovery RPO evidence; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Incorrect or unauthorized point-in-time recovery.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-DB-CLONING-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-CLONING-01`

ContentLocator: `cloning`

RequirementText: Create a supported database clone.

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project authorization, target isolation, and secret rotation.

AT: Planned artifact: database clone isolation and cross-project tenant-denial evidence; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Clone leaks tenant data or credentials.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-DB-BRANCHING-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-BRANCHING-01`

ContentLocator: `branching`

RequirementText: Create and manage a supported database branch.

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project authorization, branch isolation, and audit.

AT: Planned artifact: database branch creation and isolation evidence; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Branch leaks or mutates production data.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-DB-PROMOTION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-PROMOTION-01`

ContentLocator: `- Production-grade lifecycle controls: status and events, scale/configuration changes, maintenance behavior, quotas, limits, backups, retention, recovery drills, point-in-time restore, cloning/branching, promotion/merge semantics where applicable, and deletion/retention controls.`

SourcePosition: Structural disambiguator only, not source text: `promotion/merge semantics segment`.

RequirementText: Define and enforce supported database promotion semantics where applicable.

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized promotion with target and impact confirmation.

AT: Planned artifact: database branch promotion authorization and rollback evidence; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unsafe promotion or unsupported semantic claim.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-DB-MERGE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-MERGE-01`

ContentLocator: `merge semantics where applicable`

RequirementText: Define and enforce supported database merge semantics where applicable.

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized merge with conflict and impact control.

AT: Planned artifact: database branch merge conflict and rollback evidence; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unsafe merge or unsupported semantic claim.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-DB-DELETION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-DELETION-01`

ContentLocator: `- Production-grade lifecycle controls: status and events, scale/configuration changes, maintenance behavior, quotas, limits, backups, retention, recovery drills, point-in-time restore, cloning/branching, promotion/merge semantics where applicable, and deletion/retention controls.`

SourcePosition: Structural disambiguator only, not source text: `deletion/retention controls segment`.

RequirementText: Provide explicit database deletion controls.

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Project owner confirmation, retention disclosure, and audit.

AT: Planned artifact: destructive database deletion confirmation and recovery-window evidence; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Accidental destructive deletion.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-DB-DELETION-RETENTION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-DELETION-RETENTION-01`

ContentLocator: `deletion/retention controls`

RequirementText: Apply retention controls to deleted databases.

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized retention policy and recovery-window disclosure.

AT: Planned artifact: deleted-database retention expiry and recovery denial evidence; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Deletion violates retention or recovery commitments.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-DB-SEC-AUTHENTICATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-SEC-AUTHENTICATION-01`

ContentLocator: `authentication`

RequirementText: Authenticate database data-plane and control-plane callers.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Strong caller and workload authentication.

AT: Planned artifact: database authentication failure denial evidence; Work contract: `FW-DB-SECURITY-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unauthenticated access.

N/A: gap

Work: `FW-DB-SECURITY-02`

### REQ-DB-SEC-AUTHORIZATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-SEC-AUTHORIZATION-01`

ContentLocator: `authorization`

RequirementText: Authorize database data-plane and control-plane operations.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Least-privilege authorization at every operation.

AT: Planned artifact: database authorization denial and audit evidence; Work contract: `FW-DB-SECURITY-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Privilege escalation.

N/A: gap

Work: `FW-DB-SECURITY-02`

### REQ-DB-SEC-TENANCY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-SEC-TENANCY-01`

ContentLocator: `tenancy isolation`

RequirementText: Isolate every tenant in database data-plane and control-plane operation.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Tenant boundary enforcement and denial evidence.

AT: Planned artifact: database cross-tenant access denial evidence; Work contract: `FW-DB-SECURITY-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Cross-tenant data exposure.

N/A: gap

Work: `FW-DB-SECURITY-02`

### REQ-DB-SEC-TRANSIT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-SEC-TRANSIT-01`

ContentLocator: `encryption in transit`

RequirementText: Encrypt database traffic in transit.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authenticated encrypted transport.

AT: Planned artifact: database encrypted-transit enforcement evidence; Work contract: `FW-DB-SECURITY-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Traffic interception or downgrade.

N/A: gap

Work: `FW-DB-SECURITY-02`

### REQ-DB-SEC-REST-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-SEC-REST-01`

ContentLocator: `- Data-plane and control-plane security: authentication, authorization, tenancy isolation, encryption in transit and at rest, secret handling, rate limits, idempotency, audit logs, secure defaults, and abuse/failure protection.`

SourcePosition: Structural disambiguator only, not source text: `encryption at rest segment`.

RequirementText: Encrypt database data at rest.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized key and storage protection.

AT: Planned artifact: database encrypted-at-rest key-access denial evidence; Work contract: `FW-DB-SECURITY-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Storage disclosure.

N/A: gap

Work: `FW-DB-SECURITY-02`

### REQ-DB-SEC-SECRETS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-SEC-SECRETS-01`

ContentLocator: `secret handling`

RequirementText: Handle database secrets without source, log, response, or cross-tenant leakage.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Least-privilege secret access and redaction.

AT: Planned artifact: database secret redaction in logs and diagnostics evidence; Work contract: `FW-DB-SECURITY-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Secret leakage.

N/A: gap

Work: `FW-DB-SECURITY-02`

### REQ-DB-SEC-RATE-LIMITS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-SEC-RATE-LIMITS-01`

ContentLocator: `rate limits`

RequirementText: Apply database product rate limits.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Tenant-safe abuse control.

AT: Planned artifact: database rate-limit denial and audit evidence; Work contract: `FW-DB-SECURITY-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Abuse exhausts shared capacity.

N/A: gap

Work: `FW-DB-SECURITY-02`

### REQ-DB-SEC-IDEMPOTENCY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-SEC-IDEMPOTENCY-01`

ContentLocator: `idempotency`

RequirementText: Provide idempotency for supported database mutations.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized idempotency keys bound to caller and target.

AT: Planned artifact: database idempotent retry replay evidence; Work contract: `FW-DB-SECURITY-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Duplicate mutation on retry.

N/A: gap

Work: `FW-DB-SECURITY-02`

### REQ-DB-SEC-AUDIT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-SEC-AUDIT-01`

ContentLocator: `audit logs`

RequirementText: Record immutable, tenant-safe database security and lifecycle audit logs.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized audit visibility and tamper-resistant retention.

AT: Planned artifact: database privileged-operation immutable audit evidence; Work contract: `FW-DB-SECURITY-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unauditable security-relevant action.

N/A: gap

Work: `FW-DB-SECURITY-02`

### REQ-DB-SEC-DEFAULTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-SEC-DEFAULTS-01`

ContentLocator: `secure defaults`

RequirementText: Use secure database product defaults.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: No insecure opt-out without explicit authorized policy.

AT: Planned artifact: database secure-default configuration evidence; Work contract: `FW-DB-SECURITY-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Insecure default deployment.

N/A: gap

Work: `FW-DB-SECURITY-02`

### REQ-DB-SEC-ABUSE-FAILURE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-SEC-ABUSE-FAILURE-01`

ContentLocator: `abuse/failure protection`

RequirementText: Protect database workflows from abuse and failure.

Owner: Platform database lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Least privilege, bounded retries, and safe failure behavior.

AT: Planned artifact: database abuse-control failure denial and audit evidence; Work contract: `FW-DB-SECURITY-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Abuse or failure cascades into data loss.

N/A: gap

Work: `FW-DB-SECURITY-02`

### REQ-DB-REST-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-REST-01`

ContentLocator: `Public versioned REST APIs`

RequirementText: Expose the database product through public versioned REST APIs.

Owner: Platform and SDK contract leads

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and versioned tenant scope.

AT: Planned artifact: database versioned REST contract boundary evidence; Work contract: `FW-DB-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unversioned or private public contract.

N/A: gap

Work: `FW-DB-CONTRACT-01`

### REQ-DB-DOTNET-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-DOTNET-01`

ContentLocator: `- Public versioned REST APIs and first-class .NET and TypeScript SDK parity. Do not expose generic request escape hatches, private routes/contracts, direct TerraBase access, special Dashboard headers, or service-internal shortcuts.`

SourcePosition: Structural disambiguator only, not source text: `first-class .NET SDK parity segment`.

RequirementText: Provide first-class typed .NET SDK parity for database product operations.

Owner: Platform and SDK contract leads

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Same public authorization and tenant scope as REST.

AT: Planned artifact: database .NET typed SDK contract boundary evidence; Work contract: `FW-DB-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: SDK capability drift.

N/A: gap

Work: `FW-DB-CONTRACT-01`

### REQ-DB-TYPESCRIPT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-TYPESCRIPT-01`

ContentLocator: `- Public versioned REST APIs and first-class .NET and TypeScript SDK parity. Do not expose generic request escape hatches, private routes/contracts, direct TerraBase access, special Dashboard headers, or service-internal shortcuts.`

SourcePosition: Structural disambiguator only, not source text: `first-class TypeScript SDK parity segment`.

RequirementText: Provide first-class typed TypeScript SDK parity for database product operations.

Owner: Platform and SDK contract leads

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Same public authorization and tenant scope as REST.

AT: Planned artifact: database TypeScript typed SDK contract boundary evidence; Work contract: `FW-DB-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: SDK capability drift.

N/A: gap

Work: `FW-DB-CONTRACT-01`

### REQ-DB-NO-GENERIC-ESCAPE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-NO-GENERIC-ESCAPE-01`

ContentLocator: `Do not expose generic request escape hatches`

RequirementText: Do not expose a generic request escape hatch for the database product.

Owner: Platform and SDK contract leads

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Typed public contract only.

AT: Planned artifact: database generic-request escape-hatch denial evidence; Work contract: `FW-DB-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unreviewed request bypass.

N/A: gap

Work: `FW-DB-CONTRACT-01`

### REQ-DB-NO-PRIVATE-ROUTES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-NO-PRIVATE-ROUTES-01`

ContentLocator: `private routes/contracts`

RequirementText: Do not expose private database routes or contracts to customers.

Owner: Platform and SDK contract leads

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public-contract boundary enforcement.

AT: Planned artifact: database private-route access denial evidence; Work contract: `FW-DB-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Private contract exposure.

N/A: gap

Work: `FW-DB-CONTRACT-01`

### REQ-DB-NO-DIRECT-TERRABASE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-NO-DIRECT-TERRABASE-01`

ContentLocator: `direct TerraBase access`

RequirementText: Do not expose direct TerraBase access to database-product customers or clients.

Owner: Platform and SDK contract leads

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Control-plane authorization and data-plane credential boundary.

AT: Planned artifact: database direct-TerraBase access denial evidence; Work contract: `FW-DB-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Control-plane or engine bypass.

N/A: gap

Work: `FW-DB-CONTRACT-01`

### REQ-DB-NO-DASHBOARD-HEADERS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-NO-DASHBOARD-HEADERS-01`

ContentLocator: `special Dashboard headers`

RequirementText: Do not use special Dashboard headers for database-product access.

Owner: Platform and SDK contract leads

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Dashboard uses the same public customer authorization.

AT: Planned artifact: database Dashboard-specific header denial evidence; Work contract: `FW-DB-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Privileged Dashboard bypass.

N/A: gap

Work: `FW-DB-CONTRACT-01`

### REQ-DB-NO-INTERNAL-SHORTCUTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-NO-INTERNAL-SHORTCUTS-01`

ContentLocator: `service-internal shortcuts`

RequirementText: Do not expose service-internal shortcuts for database-product access.

Owner: Platform and SDK contract leads

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public contract boundary and workload-only internal transport.

AT: Planned artifact: database internal-transport shortcut denial evidence; Work contract: `FW-DB-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Internal service bypass.

N/A: gap

Work: `FW-DB-CONTRACT-01`

### REQ-DB-LOCAL-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-LOCAL-01`

ContentLocator: `- Clear local development, CI, integration, migration, upgrade, rollback, and customer troubleshooting workflows.`

SourcePosition: Structural disambiguator only, not source text: `local development workflow segment`.

RequirementText: Document and support a clear local database-product development workflow.

Owner: Developer experience lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Local secrets remain ignored and non-production.

AT: Planned artifact: fresh developer local database workflow AppHost scenario receipt; Work contract: `FW-DB-DEVELOPER-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unsafe or irreproducible local setup.

N/A: gap

Work: `FW-DB-DEVELOPER-02`

### REQ-DB-CI-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-CI-01`

ContentLocator: `- Clear local development, CI, integration, migration, upgrade, rollback, and customer troubleshooting workflows.`

SourcePosition: Structural disambiguator only, not source text: `CI workflow segment`.

RequirementText: Document and support database-product CI workflows.

Owner: Developer experience lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: CI secrets, isolation, and provenance controls.

AT: Planned artifact: fresh database CI workflow AppHost scenario receipt; Work contract: `FW-DB-DEVELOPER-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unreliable or insecure CI validation.

N/A: gap

Work: `FW-DB-DEVELOPER-02`

### REQ-DB-INTEGRATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-INTEGRATION-01`

ContentLocator: `- Clear local development, CI, integration, migration, upgrade, rollback, and customer troubleshooting workflows.`

SourcePosition: Structural disambiguator only, not source text: `integration workflow segment`.

RequirementText: Document and support database-product integration workflows.

Owner: Developer experience lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public-contract integration scope and tenant isolation.

AT: Planned artifact: database real integration boundary workflow evidence; Work contract: `FW-DB-DEVELOPER-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Integration drift or unsafe connection.

N/A: gap

Work: `FW-DB-DEVELOPER-02`

### REQ-DB-MIGRATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-MIGRATION-01`

ContentLocator: `- Clear local development, CI, integration, migration, upgrade, rollback, and customer troubleshooting workflows.`

SourcePosition: Structural disambiguator only, not source text: `migration workflow segment`.

RequirementText: Document and support database-product migration workflows.

Owner: Developer experience lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized migration and compatibility control.

AT: Planned artifact: database migration retry and rollback evidence; Work contract: `FW-DB-DEVELOPER-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Migration loss or incompatibility.

N/A: gap

Work: `FW-DB-DEVELOPER-02`

### REQ-DB-UPGRADE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-UPGRADE-01`

ContentLocator: `- Clear local development, CI, integration, migration, upgrade, rollback, and customer troubleshooting workflows.`

SourcePosition: Structural disambiguator only, not source text: `upgrade workflow segment`.

RequirementText: Document and support database-product upgrade workflows.

Owner: Developer experience lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized upgrade planning and compatibility control.

AT: Planned artifact: database upgrade compatibility and rollback evidence; Work contract: `FW-DB-DEVELOPER-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Upgrade outage or data incompatibility.

N/A: gap

Work: `FW-DB-DEVELOPER-02`

### REQ-DB-ROLLBACK-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-ROLLBACK-01`

ContentLocator: `- Clear local development, CI, integration, migration, upgrade, rollback, and customer troubleshooting workflows.`

SourcePosition: Structural disambiguator only, not source text: `rollback workflow segment`.

RequirementText: Document and support database-product rollback workflows.

Owner: Developer experience lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized rollback and recovery safeguards.

AT: Planned artifact: database deployment rollback recovery evidence; Work contract: `FW-DB-DEVELOPER-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Rollback data loss or outage.

N/A: gap

Work: `FW-DB-DEVELOPER-02`

### REQ-DB-TROUBLESHOOTING-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 3. Database service and developer workflow`

RequirementID: `REQ-DB-TROUBLESHOOTING-01`

ContentLocator: `customer troubleshooting workflows`

RequirementText: Document clear, customer-safe database troubleshooting workflows.

Owner: Developer experience lead

Life: gap

REST: gap

Stream: N/A[database product lifecycle;API architecture authority;versioned REST or approved streaming only where a public streaming contract is selected;real-boundary scenario evidence]

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized sanitized diagnostics only.

AT: Planned artifact: database troubleshooting diagnostic redaction evidence; Work contract: `FW-DB-DEVELOPER-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Customer receives unsafe or insufficient diagnostics.

N/A: gap

Work: `FW-DB-DEVELOPER-02`

### REQ-TRANSPORT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Definition of Done`

RequirementID: `REQ-TRANSPORT-01`

ContentLocator: Public APIs are versioned REST, public streaming uses the approved WebSocket/SSE contracts, and private MagicOnion RPC is used only by TerraScale-owned backend processes on isolated paths; production and all cross-region RPC use workload mTLS as specified in `TerraScale.Internals/docs/internal-rpc.md`.

RequirementText: Public APIs are versioned REST, public streaming uses the approved WebSocket/SSE contracts, and private MagicOnion RPC is used only by TerraScale-owned backend processes on isolated paths; production and all cross-region RPC use workload mTLS as specified in `TerraScale.Internals/docs/internal-rpc.md`.

Owner: Platform and Orchestrator architecture leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public caller authorization; private workload mTLS; no customer private RPC consumption.

AT: Planned artifact: transport 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Internal transport exposure.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-DASH-ROUTE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-ROUTE-01`

ContentLocator: - Keep every Dashboard-specific route, handler, server action, workflow, view model, and persistence choice in `TerraScale.Dashboard.Next` under `TerraScale.Internals/src/Dashboard/TerraScale.Dashboard.Next`.

SourcePosition: Structural disambiguator only, not source text: `route segment`.

RequirementText: Dashboard-specific routes stay under the Dashboard root.

Owner: Dashboard lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard-owned route boundary and cross-tenant denial evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard route leaks into Platform.

N/A: gap

Work: `FW-DASH-06`

### REQ-DASH-HANDLER-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-HANDLER-01`

ContentLocator: - Keep every Dashboard-specific route, handler, server action, workflow, view model, and persistence choice in `TerraScale.Dashboard.Next` under `TerraScale.Internals/src/Dashboard/TerraScale.Dashboard.Next`.

SourcePosition: Structural disambiguator only, not source text: `handler segment`.

RequirementText: Dashboard-specific handlers stay under the Dashboard root.

Owner: Dashboard lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard-owned route-handler typed SDK boundary evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard handler leaks into Platform.

N/A: gap

Work: `FW-DASH-06`

### REQ-DASH-SERVER-ACTION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-SERVER-ACTION-01`

ContentLocator: - Keep every Dashboard-specific route, handler, server action, workflow, view model, and persistence choice in `TerraScale.Dashboard.Next` under `TerraScale.Internals/src/Dashboard/TerraScale.Dashboard.Next`.

SourcePosition: Structural disambiguator only, not source text: `server-action segment`.

RequirementText: Dashboard-specific server actions stay under the Dashboard root.

Owner: Dashboard lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard server-action typed SDK authorization evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard server action leaks into Platform.

N/A: gap

Work: `FW-DASH-06`

### REQ-DASH-WORKFLOW-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-WORKFLOW-01`

ContentLocator: - Keep every Dashboard-specific route, handler, server action, workflow, view model, and persistence choice in `TerraScale.Dashboard.Next` under `TerraScale.Internals/src/Dashboard/TerraScale.Dashboard.Next`.

SourcePosition: Structural disambiguator only, not source text: `workflow segment`.

RequirementText: Dashboard-specific workflows stay under the Dashboard root.

Owner: Dashboard lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard workflow composition through typed SDK evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard workflow leaks into Platform.

N/A: gap

Work: `FW-DASH-06`

### REQ-DASH-VIEW-MODEL-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-VIEW-MODEL-01`

ContentLocator: - Keep every Dashboard-specific route, handler, server action, workflow, view model, and persistence choice in `TerraScale.Dashboard.Next` under `TerraScale.Internals/src/Dashboard/TerraScale.Dashboard.Next`.

SourcePosition: Structural disambiguator only, not source text: `view-model segment`.

RequirementText: Dashboard-specific view models stay under the Dashboard root.

Owner: Dashboard lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard view-model tenant-isolation evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard view model leaks into Platform.

N/A: gap

Work: `FW-DASH-06`

### REQ-DASH-PERSISTENCE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-PERSISTENCE-01`

ContentLocator: - Keep every Dashboard-specific route, handler, server action, workflow, view model, and persistence choice in `TerraScale.Dashboard.Next` under `TerraScale.Internals/src/Dashboard/TerraScale.Dashboard.Next`.

SourcePosition: Structural disambiguator only, not source text: `persistence-choice segment`.

RequirementText: Dashboard-only persistence stays under the Dashboard root.

Owner: Dashboard lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard-only persistence boundary evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard persistence leaks into Platform.

N/A: gap

Work: `FW-DASH-06`

### REQ-DASH-TYPED-SDK-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-TYPED-SDK-01`

ContentLocator: - Dashboard server code uses typed `@terrascale/sdk` APIs; browser code uses same-origin Dashboard-owned routes only. `TerraScale.Platform` stays reusable and contains no Dashboard feature slice, Dashboard route, DTO, service, option, auth, notification, or business logic.

SourcePosition: Structural disambiguator only, not source text: `typed-sdk-server segment`.

RequirementText: Dashboard server code reaches TerraScale through typed public SDK APIs.

Owner: Dashboard lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard typed SDK-only public-contract boundary evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard bypasses public contracts.

N/A: gap

Work: `FW-DASH-06`

### REQ-DASH-BROWSER-SAME-ORIGIN-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-BROWSER-SAME-ORIGIN-01`

ContentLocator: - Dashboard server code uses typed `@terrascale/sdk` APIs; browser code uses same-origin Dashboard-owned routes only. `TerraScale.Platform` stays reusable and contains no Dashboard feature slice, Dashboard route, DTO, service, option, auth, notification, or business logic.

SourcePosition: Structural disambiguator only, not source text: `browser-same-origin segment`.

RequirementText: Browser code calls only same-origin Dashboard-owned routes.

Owner: Dashboard lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard browser same-origin handler boundary evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Browser directly calls TerraScale.

N/A: gap

Work: `FW-DASH-06`

### REQ-PLATFORM-NO-DASH-FEATURE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-PLATFORM-NO-DASH-FEATURE-01`

ContentLocator: - Dashboard server code uses typed `@terrascale/sdk` APIs; browser code uses same-origin Dashboard-owned routes only. `TerraScale.Platform` stays reusable and contains no Dashboard feature slice, Dashboard route, DTO, service, option, auth, notification, or business logic.

SourcePosition: Structural disambiguator only, not source text: `no-feature-slice segment`.

RequirementText: Platform contains no Dashboard feature slice.

Owner: Platform architecture lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Platform Dashboard-feature ownership denial evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard feature logic enters Platform.

N/A: gap

Work: `FW-DASH-06`

### REQ-PLATFORM-NO-DASH-ROUTE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-PLATFORM-NO-DASH-ROUTE-01`

ContentLocator: - Dashboard server code uses typed `@terrascale/sdk` APIs; browser code uses same-origin Dashboard-owned routes only. `TerraScale.Platform` stays reusable and contains no Dashboard feature slice, Dashboard route, DTO, service, option, auth, notification, or business logic.

SourcePosition: Structural disambiguator only, not source text: `no-dashboard-route segment`.

RequirementText: Platform contains no Dashboard route.

Owner: Platform architecture lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Platform Dashboard-route ownership denial evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard route enters Platform.

N/A: gap

Work: `FW-DASH-06`

### REQ-PLATFORM-NO-DASH-DTO-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-PLATFORM-NO-DASH-DTO-01`

ContentLocator: - Dashboard server code uses typed `@terrascale/sdk` APIs; browser code uses same-origin Dashboard-owned routes only. `TerraScale.Platform` stays reusable and contains no Dashboard feature slice, Dashboard route, DTO, service, option, auth, notification, or business logic.

SourcePosition: Structural disambiguator only, not source text: `no-dashboard-dto segment`.

RequirementText: Platform contains no Dashboard DTO.

Owner: Platform architecture lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Platform Dashboard DTO ownership denial evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard DTO enters Platform.

N/A: gap

Work: `FW-DASH-06`

### REQ-PLATFORM-NO-DASH-SERVICE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-PLATFORM-NO-DASH-SERVICE-01`

ContentLocator: - Dashboard server code uses typed `@terrascale/sdk` APIs; browser code uses same-origin Dashboard-owned routes only. `TerraScale.Platform` stays reusable and contains no Dashboard feature slice, Dashboard route, DTO, service, option, auth, notification, or business logic.

SourcePosition: Structural disambiguator only, not source text: `no-dashboard-service segment`.

RequirementText: Platform contains no Dashboard service.

Owner: Platform architecture lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Platform Dashboard service ownership denial evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard service enters Platform.

N/A: gap

Work: `FW-DASH-06`

### REQ-PLATFORM-NO-DASH-OPTION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-PLATFORM-NO-DASH-OPTION-01`

ContentLocator: - Dashboard server code uses typed `@terrascale/sdk` APIs; browser code uses same-origin Dashboard-owned routes only. `TerraScale.Platform` stays reusable and contains no Dashboard feature slice, Dashboard route, DTO, service, option, auth, notification, or business logic.

SourcePosition: Structural disambiguator only, not source text: `no-dashboard-option segment`.

RequirementText: Platform contains no Dashboard option.

Owner: Platform architecture lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Platform Dashboard option ownership denial evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard option enters Platform.

N/A: gap

Work: `FW-DASH-06`

### REQ-PLATFORM-NO-DASH-AUTH-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-PLATFORM-NO-DASH-AUTH-01`

ContentLocator: - Dashboard server code uses typed `@terrascale/sdk` APIs; browser code uses same-origin Dashboard-owned routes only. `TerraScale.Platform` stays reusable and contains no Dashboard feature slice, Dashboard route, DTO, service, option, auth, notification, or business logic.

SourcePosition: Structural disambiguator only, not source text: `no-dashboard-auth segment`.

RequirementText: Platform contains no Dashboard-specific authentication logic.

Owner: Platform security lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Platform Dashboard-specific authentication denial evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard-specific authentication bypasses public controls.

N/A: gap

Work: `FW-DASH-06`

### REQ-PLATFORM-NO-DASH-NOTIFICATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-PLATFORM-NO-DASH-NOTIFICATION-01`

ContentLocator: - Dashboard server code uses typed `@terrascale/sdk` APIs; browser code uses same-origin Dashboard-owned routes only. `TerraScale.Platform` stays reusable and contains no Dashboard feature slice, Dashboard route, DTO, service, option, auth, notification, or business logic.

SourcePosition: Structural disambiguator only, not source text: `no-dashboard-notification segment`.

RequirementText: Platform contains no Dashboard-specific notification logic.

Owner: Platform architecture lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Platform Dashboard-specific notification ownership denial evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard notification logic enters Platform.

N/A: gap

Work: `FW-DASH-06`

### REQ-PLATFORM-NO-DASH-BUSINESS-LOGIC-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-PLATFORM-NO-DASH-BUSINESS-LOGIC-01`

ContentLocator: - Dashboard server code uses typed `@terrascale/sdk` APIs; browser code uses same-origin Dashboard-owned routes only. `TerraScale.Platform` stays reusable and contains no Dashboard feature slice, Dashboard route, DTO, service, option, auth, notification, or business logic.

SourcePosition: Structural disambiguator only, not source text: `no-dashboard-business-logic segment`.

RequirementText: Platform contains no Dashboard business logic.

Owner: Platform architecture lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Platform Dashboard business-logic ownership denial evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard business logic enters Platform.

N/A: gap

Work: `FW-DASH-06`

### REQ-MONITOR-OVERVIEW-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-MONITOR-OVERVIEW-01`

ContentLocator: - Project overview, continuously refreshed region availability, region and user-to-nearest-region latency, resource usage (storage, database operations, egress), historical periods and retention disclosure, and project-scoped alerts.

SourcePosition: Structural disambiguator only, not source text: `project-overview segment`.

RequirementText: Provide a project overview.

Owner: Dashboard observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard monitoring overview cross-tenant denial evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Project context is unclear or cross-tenant.

N/A: gap

Work: `FW-DASH-06`

### REQ-MONITOR-REGION-AVAILABILITY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-MONITOR-REGION-AVAILABILITY-01`

ContentLocator: - Project overview, continuously refreshed region availability, region and user-to-nearest-region latency, resource usage (storage, database operations, egress), historical periods and retention disclosure, and project-scoped alerts.

SourcePosition: Structural disambiguator only, not source text: `region-availability segment`.

RequirementText: Continuously refresh region availability.

Owner: Dashboard observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: regional availability partial-data disclosure evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Stale or misleading region availability.

N/A: gap

Work: `FW-DASH-06`

### REQ-MONITOR-REGION-LATENCY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-MONITOR-REGION-LATENCY-01`

ContentLocator: - Project overview, continuously refreshed region availability, region and user-to-nearest-region latency, resource usage (storage, database operations, egress), historical periods and retention disclosure, and project-scoped alerts.

SourcePosition: Structural disambiguator only, not source text: `region-latency segment`.

RequirementText: Show region latency.

Owner: Dashboard observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: regional latency partial-data and unit evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Misleading region latency.

N/A: gap

Work: `FW-DASH-06`

### REQ-MONITOR-NEAREST-REGION-LATENCY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-MONITOR-NEAREST-REGION-LATENCY-01`

ContentLocator: - Project overview, continuously refreshed region availability, region and user-to-nearest-region latency, resource usage (storage, database operations, egress), historical periods and retention disclosure, and project-scoped alerts.

SourcePosition: Structural disambiguator only, not source text: `nearest-region-latency segment`.

RequirementText: Show user-to-nearest-region latency.

Owner: Dashboard observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: nearest-region latency partial-data disclosure evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Misleading nearest-region latency.

N/A: gap

Work: `FW-DASH-06`

### REQ-MONITOR-STORAGE-USAGE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-MONITOR-STORAGE-USAGE-01`

ContentLocator: - Project overview, continuously refreshed region availability, region and user-to-nearest-region latency, resource usage (storage, database operations, egress), historical periods and retention disclosure, and project-scoped alerts.

SourcePosition: Structural disambiguator only, not source text: `storage-usage segment`.

RequirementText: Show storage resource usage.

Owner: Dashboard observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: storage-usage partial-data and unit evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Misleading storage usage.

N/A: gap

Work: `FW-DASH-06`

### REQ-MONITOR-DATABASE-OPERATIONS-USAGE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-MONITOR-DATABASE-OPERATIONS-USAGE-01`

ContentLocator: - Project overview, continuously refreshed region availability, region and user-to-nearest-region latency, resource usage (storage, database operations, egress), historical periods and retention disclosure, and project-scoped alerts.

SourcePosition: Structural disambiguator only, not source text: `database-operations-usage segment`.

RequirementText: Show database operations resource usage.

Owner: Dashboard observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: database-operation usage partial-data and unit evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Misleading database-operations usage.

N/A: gap

Work: `FW-DASH-06`

### REQ-MONITOR-EGRESS-USAGE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-MONITOR-EGRESS-USAGE-01`

ContentLocator: - Project overview, continuously refreshed region availability, region and user-to-nearest-region latency, resource usage (storage, database operations, egress), historical periods and retention disclosure, and project-scoped alerts.

SourcePosition: Structural disambiguator only, not source text: `egress-usage segment`.

RequirementText: Show egress resource usage.

Owner: Dashboard observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: egress-usage partial-data and unit evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Misleading egress usage.

N/A: gap

Work: `FW-DASH-06`

### REQ-MONITOR-HISTORICAL-PERIODS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-MONITOR-HISTORICAL-PERIODS-01`

ContentLocator: - Project overview, continuously refreshed region availability, region and user-to-nearest-region latency, resource usage (storage, database operations, egress), historical periods and retention disclosure, and project-scoped alerts.

SourcePosition: Structural disambiguator only, not source text: `historical-periods segment`.

RequirementText: Show historical periods.

Owner: Dashboard observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: monitoring historical-period selection evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Historical context is unavailable.

N/A: gap

Work: `FW-DASH-06`

### REQ-MONITOR-RETENTION-DISCLOSURE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-MONITOR-RETENTION-DISCLOSURE-01`

ContentLocator: - Project overview, continuously refreshed region availability, region and user-to-nearest-region latency, resource usage (storage, database operations, egress), historical periods and retention disclosure, and project-scoped alerts.

SourcePosition: Structural disambiguator only, not source text: `retention-disclosure segment`.

RequirementText: Disclose metric retention.

Owner: Dashboard observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: monitoring retention disclosure evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Retention is undisclosed.

N/A: gap

Work: `FW-DASH-06`

### REQ-MONITOR-PROJECT-ALERTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-MONITOR-PROJECT-ALERTS-01`

ContentLocator: - Project overview, continuously refreshed region availability, region and user-to-nearest-region latency, resource usage (storage, database operations, egress), historical periods and retention disclosure, and project-scoped alerts.

SourcePosition: Structural disambiguator only, not source text: `project-scoped-alerts segment`.

RequirementText: Provide project-scoped alerts.

Owner: Dashboard observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: project alert notification and cross-tenant denial evidence; Work contract: `FW-OBS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Alert crosses project boundary or is missed.

N/A: gap

Work: `FW-OBS-06`

### REQ-DASH-UX-ACCESSIBLE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-UX-ACCESSIBLE-01`

ContentLocator: - Accessible, responsive, comprehensible UX with clear active organization/project context, empty/loading/error states, no internal error leakage, and consistent units and metric reference periods.

SourcePosition: Structural disambiguator only, not source text: `accessible segment`.

RequirementText: Provide accessible UX.

Owner: Dashboard experience lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard accessible interaction-state evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard is inaccessible.

N/A: gap

Work: `FW-DASH-06`

### REQ-DASH-UX-RESPONSIVE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-UX-RESPONSIVE-01`

ContentLocator: - Accessible, responsive, comprehensible UX with clear active organization/project context, empty/loading/error states, no internal error leakage, and consistent units and metric reference periods.

SourcePosition: Structural disambiguator only, not source text: `responsive segment`.

RequirementText: Provide responsive UX.

Owner: Dashboard experience lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard responsive accessible layout-state evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard is unusable on supported viewports.

N/A: gap

Work: `FW-DASH-06`

### REQ-DASH-UX-COMPREHENSIBLE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-UX-COMPREHENSIBLE-01`

ContentLocator: - Accessible, responsive, comprehensible UX with clear active organization/project context, empty/loading/error states, no internal error leakage, and consistent units and metric reference periods.

SourcePosition: Structural disambiguator only, not source text: `comprehensible segment`.

RequirementText: Provide comprehensible UX.

Owner: Dashboard experience lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard comprehensible accessible-label evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard state is misunderstood.

N/A: gap

Work: `FW-DASH-06`

### REQ-DASH-UX-ACTIVE-ORG-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-UX-ACTIVE-ORG-01`

ContentLocator: - Accessible, responsive, comprehensible UX with clear active organization/project context, empty/loading/error states, no internal error leakage, and consistent units and metric reference periods.

SourcePosition: Structural disambiguator only, not source text: `active-organization-context segment`.

RequirementText: Show clear active organization context.

Owner: Dashboard experience lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard active-organization cross-tenant denial evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Action occurs in an unclear organization context.

N/A: gap

Work: `FW-DASH-06`

### REQ-DASH-UX-ACTIVE-PROJECT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-UX-ACTIVE-PROJECT-01`

ContentLocator: - Accessible, responsive, comprehensible UX with clear active organization/project context, empty/loading/error states, no internal error leakage, and consistent units and metric reference periods.

SourcePosition: Structural disambiguator only, not source text: `active-project-context segment`.

RequirementText: Show clear active project context.

Owner: Dashboard experience lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard active-project cross-tenant denial evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Action occurs in an unclear project context.

N/A: gap

Work: `FW-DASH-06`

### REQ-DASH-UX-EMPTY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-UX-EMPTY-01`

ContentLocator: - Accessible, responsive, comprehensible UX with clear active organization/project context, empty/loading/error states, no internal error leakage, and consistent units and metric reference periods.

SourcePosition: Structural disambiguator only, not source text: `empty-state segment`.

RequirementText: Provide an empty state.

Owner: Dashboard experience lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard empty-state accessibility evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Empty monitoring state is unclear.

N/A: gap

Work: `FW-DASH-06`

### REQ-DASH-UX-LOADING-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-UX-LOADING-01`

ContentLocator: - Accessible, responsive, comprehensible UX with clear active organization/project context, empty/loading/error states, no internal error leakage, and consistent units and metric reference periods.

SourcePosition: Structural disambiguator only, not source text: `loading-state segment`.

RequirementText: Provide a loading state.

Owner: Dashboard experience lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard loading-state accessibility evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Loading monitoring state is unclear.

N/A: gap

Work: `FW-DASH-06`

### REQ-DASH-UX-ERROR-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-UX-ERROR-01`

ContentLocator: - Accessible, responsive, comprehensible UX with clear active organization/project context, empty/loading/error states, no internal error leakage, and consistent units and metric reference periods.

SourcePosition: Structural disambiguator only, not source text: `error-state segment`.

RequirementText: Provide an error state.

Owner: Dashboard experience lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard error partial-data accessibility evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Monitoring failure has no usable error state.

N/A: gap

Work: `FW-DASH-06`

### REQ-DASH-UX-NO-INTERNAL-ERROR-LEAK-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-UX-NO-INTERNAL-ERROR-LEAK-01`

ContentLocator: - Accessible, responsive, comprehensible UX with clear active organization/project context, empty/loading/error states, no internal error leakage, and consistent units and metric reference periods.

SourcePosition: Structural disambiguator only, not source text: `no-internal-error-leakage segment`.

RequirementText: Do not leak internal errors in the Dashboard.

Owner: Dashboard security lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard internal-error redaction evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Internal error details leak to customers.

N/A: gap

Work: `FW-DASH-06`

### REQ-DASH-UX-CONSISTENT-UNITS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-UX-CONSISTENT-UNITS-01`

ContentLocator: - Accessible, responsive, comprehensible UX with clear active organization/project context, empty/loading/error states, no internal error leakage, and consistent units and metric reference periods.

SourcePosition: Structural disambiguator only, not source text: `consistent-units segment`.

RequirementText: Use consistent units.

Owner: Dashboard experience lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard metric-unit consistency evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Metric units are inconsistent.

N/A: gap

Work: `FW-DASH-06`

### REQ-DASH-UX-METRIC-REFERENCE-PERIODS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-DASH-UX-METRIC-REFERENCE-PERIODS-01`

ContentLocator: - Accessible, responsive, comprehensible UX with clear active organization/project context, empty/loading/error states, no internal error leakage, and consistent units and metric reference periods.

SourcePosition: Structural disambiguator only, not source text: `metric-reference-periods segment`.

RequirementText: Use consistent metric reference periods.

Owner: Dashboard experience lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: Dashboard metric reference-period evidence; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Metric reference period is unclear.

N/A: gap

Work: `FW-DASH-06`

### REQ-OBS-OTEL-TRACES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-OBS-OTEL-TRACES-01`

ContentLocator: - OpenTelemetry-based traces, metrics, structured ZLogger logs, dashboards, alerting, SLOs/SLIs, auditability, runbooks, and support diagnostics. Partial metric-source failures must degrade gracefully.

SourcePosition: Structural disambiguator only, not source text: `otel-traces segment`.

RequirementText: Provide OpenTelemetry-based traces.

Owner: Orchestrator observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: OpenTelemetry trace correlation and partial-failure evidence; Work contract: `FW-OBS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Trace gap blocks diagnosis.

N/A: gap

Work: `FW-OBS-06`

### REQ-OBS-OTEL-METRICS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-OBS-OTEL-METRICS-01`

ContentLocator: - OpenTelemetry-based traces, metrics, structured ZLogger logs, dashboards, alerting, SLOs/SLIs, auditability, runbooks, and support diagnostics. Partial metric-source failures must degrade gracefully.

SourcePosition: Structural disambiguator only, not source text: `otel-metrics segment`.

RequirementText: Provide OpenTelemetry-based metrics.

Owner: Orchestrator observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: OpenTelemetry metric unit and partial-data evidence; Work contract: `FW-OBS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Metric gap blocks diagnosis.

N/A: gap

Work: `FW-OBS-06`

### REQ-OBS-ZLOGGER-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-OBS-ZLOGGER-01`

ContentLocator: - OpenTelemetry-based traces, metrics, structured ZLogger logs, dashboards, alerting, SLOs/SLIs, auditability, runbooks, and support diagnostics. Partial metric-source failures must degrade gracefully.

SourcePosition: Structural disambiguator only, not source text: `zlogger-logs segment`.

RequirementText: Provide structured ZLogger logs.

Owner: Orchestrator observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: ZLogger structured diagnostic redaction evidence; Work contract: `FW-OBS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Log gap blocks diagnosis.

N/A: gap

Work: `FW-OBS-06`

### REQ-OBS-DASHBOARDS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-OBS-DASHBOARDS-01`

ContentLocator: - OpenTelemetry-based traces, metrics, structured ZLogger logs, dashboards, alerting, SLOs/SLIs, auditability, runbooks, and support diagnostics. Partial metric-source failures must degrade gracefully.

SourcePosition: Structural disambiguator only, not source text: `operational-dashboards segment`.

RequirementText: Provide operational dashboards.

Owner: Orchestrator observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: operational dashboard partial-data disclosure evidence; Work contract: `FW-OBS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Operators lack operational visibility.

N/A: gap

Work: `FW-OBS-06`

### REQ-OBS-ALERTING-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-OBS-ALERTING-01`

ContentLocator: - OpenTelemetry-based traces, metrics, structured ZLogger logs, dashboards, alerting, SLOs/SLIs, auditability, runbooks, and support diagnostics. Partial metric-source failures must degrade gracefully.

SourcePosition: Structural disambiguator only, not source text: `alerting segment`.

RequirementText: Provide alerting.

Owner: Orchestrator observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: alert delivery and degradation notification evidence; Work contract: `FW-OBS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Outage alert is missed.

N/A: gap

Work: `FW-OBS-06`

### REQ-OBS-SLO-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-OBS-SLO-01`

ContentLocator: - OpenTelemetry-based traces, metrics, structured ZLogger logs, dashboards, alerting, SLOs/SLIs, auditability, runbooks, and support diagnostics. Partial metric-source failures must degrade gracefully.

SourcePosition: Structural disambiguator only, not source text: `slos segment`.

RequirementText: Define service-level objectives.

Owner: Orchestrator observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: SLO breach measurement and degradation evidence; Work contract: `FW-OBS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: No objective reliability target.

N/A: gap

Work: `FW-OBS-06`

### REQ-OBS-SLI-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-OBS-SLI-01`

ContentLocator: - OpenTelemetry-based traces, metrics, structured ZLogger logs, dashboards, alerting, SLOs/SLIs, auditability, runbooks, and support diagnostics. Partial metric-source failures must degrade gracefully.

SourcePosition: Structural disambiguator only, not source text: `slis segment`.

RequirementText: Define service-level indicators.

Owner: Orchestrator observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: SLI calculation and partial-signal evidence; Work contract: `FW-OBS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: No reliability measurement.

N/A: gap

Work: `FW-OBS-06`

### REQ-OBS-AUDITABILITY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-OBS-AUDITABILITY-01`

ContentLocator: - OpenTelemetry-based traces, metrics, structured ZLogger logs, dashboards, alerting, SLOs/SLIs, auditability, runbooks, and support diagnostics. Partial metric-source failures must degrade gracefully.

SourcePosition: Structural disambiguator only, not source text: `auditability segment`.

RequirementText: Provide auditability.

Owner: Orchestrator observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: observability audit tenant-isolation evidence; Work contract: `FW-OBS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Operations cannot be audited.

N/A: gap

Work: `FW-OBS-06`

### REQ-OBS-RUNBOOKS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-OBS-RUNBOOKS-01`

ContentLocator: - OpenTelemetry-based traces, metrics, structured ZLogger logs, dashboards, alerting, SLOs/SLIs, auditability, runbooks, and support diagnostics. Partial metric-source failures must degrade gracefully.

SourcePosition: Structural disambiguator only, not source text: `runbooks segment`.

RequirementText: Provide runbooks.

Owner: Orchestrator observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: runbook escalation and degraded-signal evidence; Work contract: `FW-OBS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Incident response is inconsistent.

N/A: gap

Work: `FW-OBS-06`

### REQ-OBS-SUPPORT-DIAGNOSTICS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-OBS-SUPPORT-DIAGNOSTICS-01`

ContentLocator: - OpenTelemetry-based traces, metrics, structured ZLogger logs, dashboards, alerting, SLOs/SLIs, auditability, runbooks, and support diagnostics. Partial metric-source failures must degrade gracefully.

SourcePosition: Structural disambiguator only, not source text: `support-diagnostics segment`.

RequirementText: Provide tenant-safe support diagnostics.

Owner: Support diagnostics lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: support diagnostic tenant-denial and redaction evidence; Work contract: `FW-OBS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Support diagnosis leaks tenant data.

N/A: gap

Work: `FW-OBS-06`

### REQ-OBS-PARTIAL-METRIC-DEGRADATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 4. Dashboard, observability, and notifications`

RequirementID: `REQ-OBS-PARTIAL-METRIC-DEGRADATION-01`

ContentLocator: - OpenTelemetry-based traces, metrics, structured ZLogger logs, dashboards, alerting, SLOs/SLIs, auditability, runbooks, and support diagnostics. Partial metric-source failures must degrade gracefully.

SourcePosition: Structural disambiguator only, not source text: `partial-metric-source-degradation segment`.

RequirementText: Degrade gracefully when a partial metric source fails.

Owner: Orchestrator observability lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public customer authorization and tenant isolation; no privileged Dashboard bypass.

AT: Planned artifact: partial metric degradation notice and Dashboard fallback evidence; Work contract: `FW-OBS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A partial metric failure becomes misleading or disruptive.

N/A: gap

Work: `FW-OBS-06`

### REQ-BILLING-PLAN-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-PLAN-01`

ContentLocator: `- Plans, trials, subscriptions, upgrades with proration where applicable, next-cycle downgrades, cancellation/reactivation, entitlement enforcement, restricted-access states, and clear incompatibility warnings.`

RequirementText: Provide organization-scoped plans.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox plan 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-TRIAL-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-TRIAL-01`

ContentLocator: `- Plans, trials, subscriptions, upgrades with proration where applicable, next-cycle downgrades, cancellation/reactivation, entitlement enforcement, restricted-access states, and clear incompatibility warnings.`

RequirementText: Provide organization-scoped trials.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox trial 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-SUBSCRIPTION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-SUBSCRIPTION-01`

ContentLocator: `- Plans, trials, subscriptions, upgrades with proration where applicable, next-cycle downgrades, cancellation/reactivation, entitlement enforcement, restricted-access states, and clear incompatibility warnings.`

RequirementText: Provide organization-scoped subscriptions.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox subscription 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-UPGRADE-PRORATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-UPGRADE-PRORATION-01`

ContentLocator: `- Plans, trials, subscriptions, upgrades with proration where applicable, next-cycle downgrades, cancellation/reactivation, entitlement enforcement, restricted-access states, and clear incompatibility warnings.`

RequirementText: Apply proration where applicable to an upgrade.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox upgrade proration 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-DOWNGRADE-NEXT-CYCLE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-DOWNGRADE-NEXT-CYCLE-01`

ContentLocator: `- Plans, trials, subscriptions, upgrades with proration where applicable, next-cycle downgrades, cancellation/reactivation, entitlement enforcement, restricted-access states, and clear incompatibility warnings.`

RequirementText: Schedule a downgrade for the next billing cycle.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox downgrade next cycle 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-CANCELLATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-CANCELLATION-01`

ContentLocator: `- Plans, trials, subscriptions, upgrades with proration where applicable, next-cycle downgrades, cancellation/reactivation, entitlement enforcement, restricted-access states, and clear incompatibility warnings.`

RequirementText: Support subscription cancellation.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox cancellation 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-REACTIVATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-REACTIVATION-01`

ContentLocator: `- Plans, trials, subscriptions, upgrades with proration where applicable, next-cycle downgrades, cancellation/reactivation, entitlement enforcement, restricted-access states, and clear incompatibility warnings.`

RequirementText: Support subscription reactivation.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox reactivation 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-ENTITLEMENT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-ENTITLEMENT-01`

ContentLocator: `- Plans, trials, subscriptions, upgrades with proration where applicable, next-cycle downgrades, cancellation/reactivation, entitlement enforcement, restricted-access states, and clear incompatibility warnings.`

RequirementText: Enforce billing entitlements.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox entitlement 01 entitlement authorization evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-RESTRICTED-ACCESS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-RESTRICTED-ACCESS-01`

ContentLocator: `- Plans, trials, subscriptions, upgrades with proration where applicable, next-cycle downgrades, cancellation/reactivation, entitlement enforcement, restricted-access states, and clear incompatibility warnings.`

RequirementText: Provide restricted-access states.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox restricted access 01 entitlement authorization evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-INCOMPATIBILITY-WARNING-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-INCOMPATIBILITY-WARNING-01`

ContentLocator: `- Plans, trials, subscriptions, upgrades with proration where applicable, next-cycle downgrades, cancellation/reactivation, entitlement enforcement, restricted-access states, and clear incompatibility warnings.`

RequirementText: Present clear incompatibility warnings.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox incompatibility warning 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-HOSTED-PAYMENT-METHODS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-HOSTED-PAYMENT-METHODS-01`

ContentLocator: `- Provider-hosted payment methods; TerraScale never stores sensitive card data. Support primary-method management, payment history, invoices/receipts, webhook verification, idempotent processing, retries, reconciliation, and customer-visible payment status.`

RequirementText: Use provider-hosted payment methods.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox hosted payment methods 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-NO-CARD-STORAGE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-NO-CARD-STORAGE-01`

ContentLocator: `- Provider-hosted payment methods; TerraScale never stores sensitive card data. Support primary-method management, payment history, invoices/receipts, webhook verification, idempotent processing, retries, reconciliation, and customer-visible payment status.`

RequirementText: TerraScale never stores sensitive card data.

Owner: Platform security lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Only verified provider events may mutate organization billing state; no TerraScale role may access sensitive card data.

AT: Planned artifact: Polar sandbox no-card-storage redaction and retrieval-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Sensitive payment data exposure or unverified provider state change.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-PRIMARY-METHOD-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-PRIMARY-METHOD-01`

ContentLocator: `- Provider-hosted payment methods; TerraScale never stores sensitive card data. Support primary-method management, payment history, invoices/receipts, webhook verification, idempotent processing, retries, reconciliation, and customer-visible payment status.`

RequirementText: Support primary-method management.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox primary method 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-PAYMENT-HISTORY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-PAYMENT-HISTORY-01`

ContentLocator: `- Provider-hosted payment methods; TerraScale never stores sensitive card data. Support primary-method management, payment history, invoices/receipts, webhook verification, idempotent processing, retries, reconciliation, and customer-visible payment status.`

RequirementText: Provide payment history.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox payment history 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-INVOICES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-INVOICES-01`

ContentLocator: `- Provider-hosted payment methods; TerraScale never stores sensitive card data. Support primary-method management, payment history, invoices/receipts, webhook verification, idempotent processing, retries, reconciliation, and customer-visible payment status.`

RequirementText: Provide invoices.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox invoices 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-RECEIPTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-RECEIPTS-01`

ContentLocator: `- Provider-hosted payment methods; TerraScale never stores sensitive card data. Support primary-method management, payment history, invoices/receipts, webhook verification, idempotent processing, retries, reconciliation, and customer-visible payment status.`

RequirementText: Provide receipts.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox receipts 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-WEBHOOK-VERIFICATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-WEBHOOK-VERIFICATION-01`

ContentLocator: `- Provider-hosted payment methods; TerraScale never stores sensitive card data. Support primary-method management, payment history, invoices/receipts, webhook verification, idempotent processing, retries, reconciliation, and customer-visible payment status.`

RequirementText: Verify payment-provider webhooks.

Owner: Platform security lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Only verified provider events may mutate organization billing state; no TerraScale role may access sensitive card data.

AT: Planned artifact: Polar sandbox webhook webhook verification 01 signature, retry, and reconciliation evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Sensitive payment data exposure or unverified provider state change.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-WEBHOOK-IDEMPOTENCY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-WEBHOOK-IDEMPOTENCY-01`

ContentLocator: `- Provider-hosted payment methods; TerraScale never stores sensitive card data. Support primary-method management, payment history, invoices/receipts, webhook verification, idempotent processing, retries, reconciliation, and customer-visible payment status.`

RequirementText: Process payment-provider webhooks idempotently.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox webhook webhook idempotency 01 signature, retry, and reconciliation evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-PAYMENT-RETRIES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-PAYMENT-RETRIES-01`

ContentLocator: `- Provider-hosted payment methods; TerraScale never stores sensitive card data. Support primary-method management, payment history, invoices/receipts, webhook verification, idempotent processing, retries, reconciliation, and customer-visible payment status.`

RequirementText: Retry payment processing safely.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox payment retries 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-RECONCILIATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-RECONCILIATION-01`

ContentLocator: `- Provider-hosted payment methods; TerraScale never stores sensitive card data. Support primary-method management, payment history, invoices/receipts, webhook verification, idempotent processing, retries, reconciliation, and customer-visible payment status.`

RequirementText: Reconcile provider payment state with TerraScale billing state.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox payment reconciliation discrepancy evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-PAYMENT-STATUS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-PAYMENT-STATUS-01`

ContentLocator: `- Provider-hosted payment methods; TerraScale never stores sensitive card data. Support primary-method management, payment history, invoices/receipts, webhook verification, idempotent processing, retries, reconciliation, and customer-visible payment status.`

RequirementText: Provide customer-visible payment status.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox payment status 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial harm, incorrect entitlement, or cross-organization disclosure.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-USAGE-STORAGE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-USAGE-STORAGE-01`

ContentLocator: `- Accurate, continuously ingested, auditable usage for storage, database operations, and egress; organization totals, project breakdowns, included allowances, provisional values, overages, and plan-limit indicators.`

RequirementText: Provide accurate, continuously ingested, auditable storage usage.

Owner: Platform metering lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox usage storage 01 metered-usage reconciliation evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Usage, allowance, or limit information is inaccurate, stale, unauditable, or cross-tenant.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-USAGE-DB-OPERATIONS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-USAGE-DB-OPERATIONS-01`

ContentLocator: `- Accurate, continuously ingested, auditable usage for storage, database operations, and egress; organization totals, project breakdowns, included allowances, provisional values, overages, and plan-limit indicators.`

RequirementText: Provide accurate, continuously ingested, auditable database-operations usage.

Owner: Platform metering lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox usage db operations 01 metered-usage reconciliation evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Usage, allowance, or limit information is inaccurate, stale, unauditable, or cross-tenant.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-USAGE-EGRESS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-USAGE-EGRESS-01`

ContentLocator: `- Accurate, continuously ingested, auditable usage for storage, database operations, and egress; organization totals, project breakdowns, included allowances, provisional values, overages, and plan-limit indicators.`

RequirementText: Provide accurate, continuously ingested, auditable egress usage.

Owner: Platform metering lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox usage egress 01 metered-usage reconciliation evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Usage, allowance, or limit information is inaccurate, stale, unauditable, or cross-tenant.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-USAGE-ORG-TOTALS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-USAGE-ORG-TOTALS-01`

ContentLocator: `- Accurate, continuously ingested, auditable usage for storage, database operations, and egress; organization totals, project breakdowns, included allowances, provisional values, overages, and plan-limit indicators.`

RequirementText: Provide organization usage totals.

Owner: Platform metering lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox usage org totals 01 metered-usage reconciliation evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Usage, allowance, or limit information is inaccurate, stale, unauditable, or cross-tenant.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-USAGE-PROJECT-BREAKDOWNS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-USAGE-PROJECT-BREAKDOWNS-01`

ContentLocator: `- Accurate, continuously ingested, auditable usage for storage, database operations, and egress; organization totals, project breakdowns, included allowances, provisional values, overages, and plan-limit indicators.`

RequirementText: Provide project usage breakdowns.

Owner: Platform metering lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox usage project breakdowns 01 metered-usage reconciliation evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Usage, allowance, or limit information is inaccurate, stale, unauditable, or cross-tenant.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-USAGE-ALLOWANCES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-USAGE-ALLOWANCES-01`

ContentLocator: `- Accurate, continuously ingested, auditable usage for storage, database operations, and egress; organization totals, project breakdowns, included allowances, provisional values, overages, and plan-limit indicators.`

RequirementText: Provide included usage allowances.

Owner: Platform metering lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox usage allowances 01 metered-usage reconciliation evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Usage, allowance, or limit information is inaccurate, stale, unauditable, or cross-tenant.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-USAGE-PROVISIONAL-VALUES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-USAGE-PROVISIONAL-VALUES-01`

ContentLocator: `- Accurate, continuously ingested, auditable usage for storage, database operations, and egress; organization totals, project breakdowns, included allowances, provisional values, overages, and plan-limit indicators.`

RequirementText: Identify provisional usage values.

Owner: Platform metering lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox usage provisional values 01 metered-usage reconciliation evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Usage, allowance, or limit information is inaccurate, stale, unauditable, or cross-tenant.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-USAGE-OVERAGES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-USAGE-OVERAGES-01`

ContentLocator: `- Accurate, continuously ingested, auditable usage for storage, database operations, and egress; organization totals, project breakdowns, included allowances, provisional values, overages, and plan-limit indicators.`

RequirementText: Calculate and expose usage overages.

Owner: Platform metering lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox usage overages 01 metered-usage reconciliation evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Usage, allowance, or limit information is inaccurate, stale, unauditable, or cross-tenant.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-USAGE-PLAN-LIMITS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-USAGE-PLAN-LIMITS-01`

ContentLocator: `- Accurate, continuously ingested, auditable usage for storage, database operations, and egress; organization totals, project breakdowns, included allowances, provisional values, overages, and plan-limit indicators.`

RequirementText: Provide plan-limit indicators.

Owner: Platform metering lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization Owner and authorized financial role; cross-organization denial.

AT: Planned artifact: Polar sandbox usage plan limits 01 metered-usage reconciliation evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Usage, allowance, or limit information is inaccurate, stale, unauditable, or cross-tenant.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-NOTICE-PAYMENT-FAILURE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-NOTICE-PAYMENT-FAILURE-01`

ContentLocator: `- Mandatory organization-owner communications for payment failures, charges, renewal, limits, and overages; optional preferences cannot disable security or required billing notices.`

RequirementText: Send mandatory organization-owner communications for payment failures.

Owner: Platform notifications lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Required-notice policy targets organization owners and overrides optional preferences.

AT: Planned artifact: Polar sandbox notice payment failure 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A mandatory organization-owner notice is missed or suppressed.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-NOTICE-CHARGE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-NOTICE-CHARGE-01`

ContentLocator: `- Mandatory organization-owner communications for payment failures, charges, renewal, limits, and overages; optional preferences cannot disable security or required billing notices.`

RequirementText: Send mandatory organization-owner communications for charges.

Owner: Platform notifications lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Required-notice policy targets organization owners and overrides optional preferences.

AT: Planned artifact: Polar sandbox notice charge 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A mandatory organization-owner notice is missed or suppressed.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-NOTICE-RENEWAL-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-NOTICE-RENEWAL-01`

ContentLocator: `- Mandatory organization-owner communications for payment failures, charges, renewal, limits, and overages; optional preferences cannot disable security or required billing notices.`

RequirementText: Send mandatory organization-owner communications for renewal.

Owner: Platform notifications lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Required-notice policy targets organization owners and overrides optional preferences.

AT: Planned artifact: Polar sandbox notice renewal 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A mandatory organization-owner notice is missed or suppressed.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-NOTICE-LIMIT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-NOTICE-LIMIT-01`

ContentLocator: `- Mandatory organization-owner communications for payment failures, charges, renewal, limits, and overages; optional preferences cannot disable security or required billing notices.`

RequirementText: Send mandatory organization-owner communications for limits.

Owner: Platform notifications lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Required-notice policy targets organization owners and overrides optional preferences.

AT: Planned artifact: Polar sandbox notice limit 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A mandatory organization-owner notice is missed or suppressed.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-NOTICE-OVERAGE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-NOTICE-OVERAGE-01`

ContentLocator: `- Mandatory organization-owner communications for payment failures, charges, renewal, limits, and overages; optional preferences cannot disable security or required billing notices.`

RequirementText: Send mandatory organization-owner communications for overages.

Owner: Platform notifications lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Required-notice policy targets organization owners and overrides optional preferences.

AT: Planned artifact: Polar sandbox notice overage 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A mandatory organization-owner notice is missed or suppressed.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-NOTICE-PREFERENCE-BOUNDARY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-NOTICE-PREFERENCE-BOUNDARY-01`

ContentLocator: `- Mandatory organization-owner communications for payment failures, charges, renewal, limits, and overages; optional preferences cannot disable security or required billing notices.`

RequirementText: Prevent optional preferences from disabling security or required billing notices.

Owner: Platform notifications lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Required-notice policy targets organization owners and overrides optional preferences.

AT: Planned artifact: Polar sandbox notice preference boundary 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A mandatory organization-owner notice is missed or suppressed.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-POLAR-SUBSCRIBE-SUCCESS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-POLAR-SUBSCRIBE-SUCCESS-01`

ContentLocator: `- Real Polar Sandbox test scenarios for successful and failed subscriptions, payment-method updates, renewal, cancellation/reactivation, metered usage, overages, webhook retries/out-of-order events, duplicate events, receipt access, and reconciliation.`

RequirementText: Run a real Polar Sandbox scenario for a successful subscription.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Polar Sandbox authorization, organization scope, provider verification where applicable, and redacted credentials.

AT: Planned artifact: Polar sandbox polar subscribe success 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: The named real provider-boundary scenario is absent, unsafe, or unreconciled.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-POLAR-SUBSCRIBE-FAILURE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-POLAR-SUBSCRIBE-FAILURE-01`

ContentLocator: `- Real Polar Sandbox test scenarios for successful and failed subscriptions, payment-method updates, renewal, cancellation/reactivation, metered usage, overages, webhook retries/out-of-order events, duplicate events, receipt access, and reconciliation.`

RequirementText: Run a real Polar Sandbox scenario for a failed subscription.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Polar Sandbox authorization, organization scope, provider verification where applicable, and redacted credentials.

AT: Planned artifact: Polar sandbox polar subscribe failure 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: The named real provider-boundary scenario is absent, unsafe, or unreconciled.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-POLAR-METHOD-UPDATE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-POLAR-METHOD-UPDATE-01`

ContentLocator: `- Real Polar Sandbox test scenarios for successful and failed subscriptions, payment-method updates, renewal, cancellation/reactivation, metered usage, overages, webhook retries/out-of-order events, duplicate events, receipt access, and reconciliation.`

RequirementText: Run a real Polar Sandbox scenario for a payment-method update.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Polar Sandbox authorization, organization scope, provider verification where applicable, and redacted credentials.

AT: Planned artifact: Polar sandbox polar method update 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: The named real provider-boundary scenario is absent, unsafe, or unreconciled.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-POLAR-RENEWAL-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-POLAR-RENEWAL-01`

ContentLocator: `- Real Polar Sandbox test scenarios for successful and failed subscriptions, payment-method updates, renewal, cancellation/reactivation, metered usage, overages, webhook retries/out-of-order events, duplicate events, receipt access, and reconciliation.`

RequirementText: Run a real Polar Sandbox scenario for renewal.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Polar Sandbox authorization, organization scope, provider verification where applicable, and redacted credentials.

AT: Planned artifact: Polar sandbox polar renewal 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: The named real provider-boundary scenario is absent, unsafe, or unreconciled.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-POLAR-CANCELLATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-POLAR-CANCELLATION-01`

ContentLocator: `- Real Polar Sandbox test scenarios for successful and failed subscriptions, payment-method updates, renewal, cancellation/reactivation, metered usage, overages, webhook retries/out-of-order events, duplicate events, receipt access, and reconciliation.`

RequirementText: Run a real Polar Sandbox scenario for cancellation.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Polar Sandbox authorization, organization scope, provider verification where applicable, and redacted credentials.

AT: Planned artifact: Polar sandbox polar cancellation 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: The named real provider-boundary scenario is absent, unsafe, or unreconciled.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-POLAR-REACTIVATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-POLAR-REACTIVATION-01`

ContentLocator: `- Real Polar Sandbox test scenarios for successful and failed subscriptions, payment-method updates, renewal, cancellation/reactivation, metered usage, overages, webhook retries/out-of-order events, duplicate events, receipt access, and reconciliation.`

RequirementText: Run a real Polar Sandbox scenario for reactivation.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Polar Sandbox authorization, organization scope, provider verification where applicable, and redacted credentials.

AT: Planned artifact: Polar sandbox polar reactivation 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: The named real provider-boundary scenario is absent, unsafe, or unreconciled.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-POLAR-METERED-USAGE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-POLAR-METERED-USAGE-01`

ContentLocator: `- Real Polar Sandbox test scenarios for successful and failed subscriptions, payment-method updates, renewal, cancellation/reactivation, metered usage, overages, webhook retries/out-of-order events, duplicate events, receipt access, and reconciliation.`

RequirementText: Run a real Polar Sandbox scenario for metered usage.

Owner: Platform metering lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Polar Sandbox authorization, organization scope, provider verification where applicable, and redacted credentials.

AT: Planned artifact: Polar sandbox polar metered usage 01 metered-usage reconciliation evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: The named real provider-boundary scenario is absent, unsafe, or unreconciled.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-POLAR-OVERAGES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-POLAR-OVERAGES-01`

ContentLocator: `- Real Polar Sandbox test scenarios for successful and failed subscriptions, payment-method updates, renewal, cancellation/reactivation, metered usage, overages, webhook retries/out-of-order events, duplicate events, receipt access, and reconciliation.`

RequirementText: Run a real Polar Sandbox scenario for overages.

Owner: Platform metering lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Polar Sandbox authorization, organization scope, provider verification where applicable, and redacted credentials.

AT: Planned artifact: Polar sandbox polar overages 01 metered-usage reconciliation evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: The named real provider-boundary scenario is absent, unsafe, or unreconciled.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-POLAR-WEBHOOK-RETRY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-POLAR-WEBHOOK-RETRY-01`

ContentLocator: `- Real Polar Sandbox test scenarios for successful and failed subscriptions, payment-method updates, renewal, cancellation/reactivation, metered usage, overages, webhook retries/out-of-order events, duplicate events, receipt access, and reconciliation.`

RequirementText: Run a real Polar Sandbox scenario for webhook retries.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Polar Sandbox authorization, organization scope, provider verification where applicable, and redacted credentials.

AT: Planned artifact: Polar sandbox webhook webhook retry 01 signature, retry, and reconciliation evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: The named real provider-boundary scenario is absent, unsafe, or unreconciled.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-POLAR-WEBHOOK-OUT-OF-ORDER-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-POLAR-WEBHOOK-OUT-OF-ORDER-01`

ContentLocator: `- Real Polar Sandbox test scenarios for successful and failed subscriptions, payment-method updates, renewal, cancellation/reactivation, metered usage, overages, webhook retries/out-of-order events, duplicate events, receipt access, and reconciliation.`

RequirementText: Run a real Polar Sandbox scenario for out-of-order webhook events.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Polar Sandbox authorization, organization scope, provider verification where applicable, and redacted credentials.

AT: Planned artifact: Polar sandbox webhook webhook out of order 01 signature, retry, and reconciliation evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: The named real provider-boundary scenario is absent, unsafe, or unreconciled.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-POLAR-WEBHOOK-DUPLICATE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-POLAR-WEBHOOK-DUPLICATE-01`

ContentLocator: `- Real Polar Sandbox test scenarios for successful and failed subscriptions, payment-method updates, renewal, cancellation/reactivation, metered usage, overages, webhook retries/out-of-order events, duplicate events, receipt access, and reconciliation.`

RequirementText: Run a real Polar Sandbox scenario for duplicate webhook events.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Polar Sandbox authorization, organization scope, provider verification where applicable, and redacted credentials.

AT: Planned artifact: Polar sandbox webhook webhook duplicate 01 signature, retry, and reconciliation evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: The named real provider-boundary scenario is absent, unsafe, or unreconciled.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-POLAR-RECEIPT-ACCESS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-POLAR-RECEIPT-ACCESS-01`

ContentLocator: `- Real Polar Sandbox test scenarios for successful and failed subscriptions, payment-method updates, renewal, cancellation/reactivation, metered usage, overages, webhook retries/out-of-order events, duplicate events, receipt access, and reconciliation.`

RequirementText: Run a real Polar Sandbox scenario for receipt access.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Polar Sandbox authorization, organization scope, provider verification where applicable, and redacted credentials.

AT: Planned artifact: Polar sandbox polar receipt access 01 subscription and tenant-denial evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: The named real provider-boundary scenario is absent, unsafe, or unreconciled.

N/A: gap

Work: `FW-BILL-04`

### REQ-BILLING-POLAR-RECONCILIATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 5. Billing, payments, and usage`

RequirementID: `REQ-BILLING-POLAR-RECONCILIATION-01`

ContentLocator: `- Real Polar Sandbox test scenarios for successful and failed subscriptions, payment-method updates, renewal, cancellation/reactivation, metered usage, overages, webhook retries/out-of-order events, duplicate events, receipt access, and reconciliation.`

RequirementText: Run a real Polar Sandbox scenario for reconciliation.

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Polar Sandbox authorization, organization scope, provider verification where applicable, and redacted credentials.

AT: Planned artifact: Polar sandbox payment reconciliation discrepancy evidence; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: The named real provider-boundary scenario is absent, unsafe, or unreconciled.

N/A: gap

Work: `FW-BILL-04`

### REQ-MCP-TOOLS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 6. AI-agent product surface`

RequirementID: `REQ-MCP-TOOLS-01`

ContentLocator: `- Clear capability-oriented tools for identity context, organization/project selection, database lifecycle, operations, backups/recovery, observability, usage/billing, alerts, and supported administration.`

RequirementText: Deliver clear capability-oriented MCP tools for identity context, organization and project selection, database lifecycle, operations, backups and recovery, observability, usage and billing, alerts, and supported administration.

Owner: MCP lead

Life: gap

REST: `AT-SP09.API-SDK`; Evidence: gap

Stream: N/A[agent capability inventory;API architecture authority;public REST or an approved public stream is selected per capability;per-capability integration evidence]

.NET: `AT-SP09.API-SDK`; Evidence: gap

TS: `AT-SP09.API-SDK`; Evidence: gap

Dashboard: `AT-SP09.DASH`; Evidence: gap

MCP: `AT-SP09.MCP`; Evidence: gap

Auth: Least-privilege public authorization, tenant scope, bounded output, and idempotency for each consequential tool.

AT: Planned artifact: typed public MCP tools 01 metadata, confirmation, retry, and tenant-denial evidence; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: An absent, over-broad, or internally backed tool can deny parity or create a privilege escalation path.

N/A: gap

Work: `FW-MCP-05`

### REQ-MCP-DISCOVERABILITY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 6. AI-agent product surface`

RequirementID: `REQ-MCP-DISCOVERABILITY-01`

ContentLocator: `- Discoverable resources, prompts, instructions, schemas, examples, error/recovery guidance, pagination/filtering conventions, idempotency behavior, and least-privilege authorization.`

RequirementText: Make MCP resources, prompts, instructions, schemas, examples, error and recovery guidance, pagination and filtering conventions, idempotency behavior, and least-privilege authorization discoverable.

Owner: MCP lead

Life: gap

REST: `AT-SP09.API-SDK`; Evidence: gap

Stream: N/A[agent discovery metadata;API architecture authority;metadata describes the selected public REST or stream contract;metadata and contract integration evidence]

.NET: `AT-SP09.API-SDK`; Evidence: gap

TS: `AT-SP09.API-SDK`; Evidence: gap

Dashboard: `AT-SP09.DASH`; Evidence: gap

MCP: `AT-SP09.MCP`; Evidence: gap

Auth: Discoverability must not disclose ungranted capabilities; examples, pagination, filters, errors, recovery, and idempotency must preserve least privilege.

AT: Planned artifact: typed public MCP discoverability 01 metadata, confirmation, retry, and tenant-denial evidence; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Incomplete metadata or unsafe examples produce agent misuse, hidden behavior, or authorization leakage.

N/A: gap

Work: `FW-MCP-05`

### REQ-MCP-WORKFLOWS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 6. AI-agent product surface`

RequirementID: `REQ-MCP-WORKFLOWS-01`

ContentLocator: `- Agent-friendly workflows for onboarding, project/database provisioning, incident inspection, restore drills, and billing/usage investigation, with confirmation for destructive or financially consequential operations.`

RequirementText: Provide agent-friendly onboarding, project and database provisioning, incident-inspection, restore-drill, and billing and usage-investigation workflows. Require confirmation for destructive or financially consequential operations.

Owner: MCP lead

Life: gap

REST: `AT-SP09.API-SDK`; Evidence: gap

Stream: N/A[agent workflow;API architecture authority;public REST or approved public stream is selected per workflow step;workflow integration evidence]

.NET: `AT-SP09.API-SDK`; Evidence: gap

TS: `AT-SP09.API-SDK`; Evidence: gap

Dashboard: `AT-SP09.DASH`; Evidence: gap

MCP: `AT-SP09.MCP`; Evidence: gap

Auth: Tenant-scoped authorization, explicit confirmation before destructive or financially consequential operations, audit, and idempotency where a mutation is retried.

AT: Planned artifact: typed public MCP workflows 01 metadata, confirmation, retry, and tenant-denial evidence; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A workflow may bypass confirmation, lose recovery context, or produce an unsafe financial or destructive outcome.

N/A: gap

Work: `FW-MCP-05`

### REQ-MCP-EQUIVALENCE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 6. AI-agent product surface`

RequirementID: `REQ-MCP-EQUIVALENCE-01`

ContentLocator: `- Capability equivalence with the dashboard for every customer action. Maintain a Dashboard-to-public-API/SDK-to-MCP capability matrix that maps each action to its human flow, public contract, agent tool/resource/prompt, required confirmation behavior, and automated equivalence coverage. A security-sensitive interaction may require stronger agent confirmation or a safe alternative flow, but it may not create a privileged Dashboard-only capability or reduce the customer's underlying agent-accessible capability.`

RequirementText: Maintain per-customer-action Dashboard-to-public-API, typed SDK, and MCP equivalence records with human flow, public contract, tool, resource or prompt, confirmation, automated coverage, stronger-confirmation and safe-alternative decisions. Do not create privileged Dashboard-only capability or reduce the underlying agent-accessible customer capability.

Owner: MCP lead

Life: gap

REST: `AT-SP09.API-SDK`; Evidence: gap

Stream: N/A[capability-equivalence matrix;API architecture authority;the matrix records the selected public REST or stream contract for each action;per-action equivalence evidence]

.NET: `AT-SP09.API-SDK`; Evidence: gap

TS: `AT-SP09.API-SDK`; Evidence: gap

Dashboard: `AT-SP09.DASH`; Evidence: gap

MCP: `AT-SP09.MCP`; Evidence: gap

Auth: Security-sensitive actions may strengthen agent confirmation or use an approved safe alternative, never a privileged Dashboard-only path.

AT: Planned artifact: typed public MCP equivalence 01 metadata, confirmation, retry, and tenant-denial evidence; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Matrix drift could grant Dashboard privilege, leave an agent without a safe equivalent, or represent untested parity as complete.

N/A: gap

Work: `FW-MCP-05`

### REQ-MCP-BOUNDARY-TESTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 6. AI-agent product surface`

RequirementID: `REQ-MCP-BOUNDARY-TESTS-01`

ContentLocator: `- Contract, integration, security, and usability tests for the MCP server; no private control-plane transport, privileged header, direct database access, or hidden agent-only escape hatch.`

RequirementText: Prove the MCP server with contract, integration, security, and usability tests. Prohibit private control-plane transport, privileged headers, direct database access, and hidden agent-only escape hatches.

Owner: MCP lead

Life: gap

REST: `AT-SP09.API-SDK`; Evidence: gap

Stream: N/A[MCP boundary test;API architecture authority;only public REST or approved public streaming contracts are exercised;real-boundary test evidence]

.NET: `AT-SP09.API-SDK`; Evidence: gap

TS: `AT-SP09.API-SDK`; Evidence: gap

Dashboard: `AT-SP09.DASH`; Evidence: gap

MCP: `AT-SP09.MCP`; Evidence: gap

Auth: Public customer authorization and tenant boundaries only. No private transport, privileged header, direct database credential, or agent-only bypass.

AT: Planned artifact: typed public MCP boundary tests 01 metadata, confirmation, retry, and tenant-denial evidence; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Private or direct access can conceal a boundary violation and invalidate customer-equivalence evidence.

N/A: gap

Work: `FW-MCP-05`

### REQ-ADMIN-OIDC-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`

RequirementID: `REQ-ADMIN-OIDC-01`

ContentLocator: `TerraScale Admin surface separately from customer membership, with OIDC/RBAC, break-glass controls, least privilege, mandatory audit, and safe support diagnostics.`

RequirementText: Deliver a TerraScale Admin surface separate from customer membership with OIDC, RBAC, break-glass controls, least privilege, mandatory audit, and safe support diagnostics.

Owner: Platform administration lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Separately audited operator identity, OIDC, RBAC, break-glass expiration, and least privilege.

AT: Planned artifact: TerraScale Admin OIDC break-glass authorization and mandatory-audit evidence; Work contract: `FW-ADMIN-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Staff abuse, hidden customer membership, or diagnostic data exposure.

N/A: gap

Work: `FW-ADMIN-04`

### REQ-ADMIN-RETENTION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Requirement Traceability > ### Required Acceptance Scenario Packs`

RequirementID: `REQ-ADMIN-RETENTION-01`

ContentLocator: `data retention/export/delete behavior, secret handling, security event response, and legal/claim approval boundaries.`

RequirementText: Define and prove data retention, export, delete, secret handling, security-event response, and legal or claim approval behavior.

Owner: Security and documentation claims leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Authorized subject or operator only; legal approval boundary; immutable security-event audit.

AT: Planned artifact: admin retention 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-CLAIM-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Privacy, secret, legal, or incident-response failure.

N/A: gap

Work: `FW-CLAIM-06`

### REQ-GATE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Delivery Gates`

RequirementID: `REQ-GATE-01`

ContentLocator: `Discovery gate`

RequirementText: Satisfy the Discovery, Contract, Feature, Quality, Security, Operations, and Release gates before declaring completion.

Owner: Release integration lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Release authority and independent review.

AT: Planned artifact: gate 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-QUALITY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Release without complete evidence.

N/A: gap

Work: `FW-QUALITY-06`

### REQ-CONSTRAINT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Non-Negotiable Constraints`

RequirementID: `REQ-CONSTRAINT-01`

ContentLocator: `Keep customer-facing public contracts and AI-agent capability parity secure; Dashboard is an ordinary SDK customer, never a privileged bypass.`

RequirementText: Preserve secure public contracts and agent parity; the Dashboard is an ordinary SDK customer. Destructive, billing, authorization, subscription, and production infrastructure actions are confirmation, audit, and idempotency sensitive.

Owner: Product integration lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public contract authorization, confirmation, audit, and idempotency.

AT: Planned artifact: constraint 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-QUALITY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Security boundary weakening to advance work.

N/A: gap

Work: `FW-QUALITY-06`

### REQ-EQR-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Requirement Traceability > ### Evidence Quality Rules`

RequirementID: `REQ-EQR-01`

ContentLocator: `A mocked unit test can support deterministic protocol/state-machine behavior but cannot close`

RequirementText: A mocked seam may support deterministic protocol or state-machine behavior but cannot close customer, data-plane, payment-provider, deployment, recovery, or tenant-isolation requirements.

Owner: Verification lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: eqr 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-QUALITY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: False closure evidence.

N/A: gap

Work: `FW-QUALITY-06`

### REQ-EQR-02

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Requirement Traceability > ### Evidence Quality Rules`

RequirementID: `REQ-EQR-02`

ContentLocator: `A plan, static scan, code review, unchecked dashboard control, or existing route cannot substitute`

RequirementText: A plan, static scan, code review, unchecked Dashboard control, or existing route cannot substitute for a required live integration or end-to-end result.

Owner: Verification lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: eqr 02 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-QUALITY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Static evidence represented as live proof.

N/A: gap

Work: `FW-QUALITY-06`

### REQ-EQR-03

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Requirement Traceability > ### Evidence Quality Rules`

RequirementID: `REQ-EQR-03`

ContentLocator: `Every production claim has a dated evidence link`

RequirementText: Every production claim needs dated evidence, expiry or revalidation interval, accountable owner, environment, input digest, result, and residual risk.

Owner: Documentation claims lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Claim approval authority.

AT: Planned artifact: eqr 03 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-CLAIM-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unsupported public commitment.

N/A: gap

Work: `FW-CLAIM-06`

### REQ-EQR-04

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Requirement Traceability > ### Evidence Quality Rules`

RequirementID: `REQ-EQR-04`

ContentLocator: `Restore, failover, billing, security, release, and destructive-action evidence includes the tested failure path and recovery outcome`

RequirementText: Evidence for restore, failover, billing, security, release, and destructive actions includes a tested failure path and recovery outcome.

Owner: Verification lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: eqr 04 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-QUALITY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Happy-path-only recovery assertion.

N/A: gap

Work: `FW-QUALITY-06`

### REQ-EQR-05

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Requirement Traceability > ### Evidence Quality Rules`

RequirementID: `REQ-EQR-05`

ContentLocator: `A requirement marked non-applicable must state why`

RequirementText: Non-applicability must state the affected story, approving authority, safe alternative, and validation evidence; it cannot conceal unfinished capability.

Owner: Product integration lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Approval authority.

AT: Planned artifact: eqr 05 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-QUALITY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unexplained coverage hole.

N/A: gap

Work: `FW-QUALITY-06`

### REQ-P1-ROADMAP-CONTRACT-OPENAPI-INVENTORY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-CONTRACT-OPENAPI-INVENTORY-01`

RequirementText: Make the versioned Platform OpenAPI and operation inventory authoritative.

ContentLocator: `Make versioned Platform OpenAPI and operation inventory authoritative.`

Owner: Platform API lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization contract openapi inventory 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: The authoritative public API inventory omits or misstates an operation.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P1-ROADMAP-CONTRACT-SDK-DECISION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-CONTRACT-SDK-DECISION-01`

RequirementText: Record an architecture decision before expanding either SDK.

ContentLocator: `Before expanding either SDK, record an architecture decision`

Owner: Platform API lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization contract sdk decision 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: SDK expansion proceeds without an approved public-contract decision.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P1-ROADMAP-CONTRACT-OPERATION-CLASSIFICATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-CONTRACT-OPERATION-CLASSIFICATION-01`

RequirementText: Classify every public operation as SDK-supported or deliberately browser-/MCP-only.

ContentLocator: `classifies every public operation as SDK-supported or deliberately browser-/MCP-only`

Owner: Platform API lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization contract operation classification 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A public operation has an ambiguous or unsupported consumer classification.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P1-ROADMAP-CONTRACT-SDK-SCOPE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-CONTRACT-SDK-SCOPE-01`

RequirementText: Reconcile the operation classification with each SDK repository's scope rules.

ContentLocator: `reconcile that decision with each SDK repository's scope rules`

Owner: SDK architecture lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization contract sdk scope 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: An SDK exposes operations outside its approved scope.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P1-ROADMAP-CONTRACT-SAFE-ALTERNATIVE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-CONTRACT-SAFE-ALTERNATIVE-01`

RequirementText: Require an approved safe alternative for every non-SDK operation.

ContentLocator: `approved safe alternative`

Owner: SDK architecture lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization contract safe alternative 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A non-SDK operation leaves customers without a safe supported path.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P1-ROADMAP-CONTRACT-MATRIX-ENTRY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-CONTRACT-MATRIX-ENTRY-01`

RequirementText: Require a matrix entry for every non-SDK operation.

ContentLocator: `matrix entry for every non-SDK operation`

Owner: SDK architecture lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization contract matrix entry 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A non-SDK operation lacks traceable classification.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P1-ROADMAP-CONTRACT-MATCHING-INVENTORIES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-CONTRACT-MATCHING-INVENTORIES-01`

RequirementText: Generate or validate matching TypeScript, .NET, and MCP inventories.

ContentLocator: `matching TypeScript, .NET, and MCP inventories`

Owner: Platform API and SDK leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization contract matching inventories 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Consumer inventories drift from the authoritative operation inventory.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P1-ROADMAP-CONTRACT-AUTH-CLASSIFICATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-CONTRACT-AUTH-CLASSIFICATION-01`

RequirementText: Generate or validate authorization classification for every endpoint.

ContentLocator: `auth classification`

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization contract auth classification 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: An endpoint authorization requirement is unclassified.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P1-ROADMAP-CONTRACT-TENANT-SCOPE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-CONTRACT-TENANT-SCOPE-01`

RequirementText: Generate or validate tenant scope for every endpoint.

ContentLocator: `tenant scope`

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization contract tenant scope 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: An endpoint permits ambiguous tenant scope.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P1-ROADMAP-CONTRACT-IDEMPOTENCY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-CONTRACT-IDEMPOTENCY-01`

RequirementText: Generate or validate idempotency behavior for every endpoint.

ContentLocator: `idempotency behavior`

Owner: Platform API lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization contract idempotency 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: An endpoint retry outcome is undefined.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P1-ROADMAP-CONTRACT-COMPATIBILITY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-CONTRACT-COMPATIBILITY-01`

RequirementText: Generate or validate compatibility and deprecation status for every endpoint.

ContentLocator: `compatibility/deprecation status`

Owner: Platform API lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization contract compatibility 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A contract change breaks a supported consumer without compatibility status.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P1-ROADMAP-CONTRACT-DOCUMENTATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-CONTRACT-DOCUMENTATION-01`

RequirementText: Generate or validate a documentation reference for every endpoint.

ContentLocator: `documentation reference for every endpoint`

Owner: Platform API lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization contract documentation 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A public endpoint lacks a traceable documentation reference.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P1-ROADMAP-IDENTITY-SIGNUP-VERIFY-RESEND-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-IDENTITY-SIGNUP-VERIFY-RESEND-01`

RequirementText: Deliver and prove signup, verification, and resend.

ContentLocator: `signup/verification/resend`

Owner: Platform identity lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization identity signup verify resend 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Account onboarding cannot complete reliably.

N/A: gap

Work: `FW-ID-01`

### REQ-P1-ROADMAP-IDENTITY-PASSWORD-OAUTH-LOGIN-LINK-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-IDENTITY-PASSWORD-OAUTH-LOGIN-LINK-01`

RequirementText: Deliver and prove password and OAuth login and linking.

ContentLocator: `password/OAuth login/linking`

Owner: Platform identity lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization identity password oauth login link 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Login or account linking permits account takeover or blocks valid access.

N/A: gap

Work: `FW-ID-01`

### REQ-P1-ROADMAP-IDENTITY-RECOVERY-NONENUM-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-IDENTITY-RECOVERY-NONENUM-01`

RequirementText: Deliver and prove enumeration-safe recovery.

ContentLocator: `enumeration-safe recovery`

Owner: Platform identity lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization identity recovery nonenum 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Recovery reveals account existence.

N/A: gap

Work: `FW-ID-01`

### REQ-P1-ROADMAP-IDENTITY-MFA-PASSKEY-RECOVERY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-IDENTITY-MFA-PASSKEY-RECOVERY-01`

RequirementText: Deliver and prove MFA, passkeys, and recovery.

ContentLocator: `MFA/passkeys/recovery`

Owner: Platform identity lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization identity mfa passkey recovery 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: High-assurance identity controls fail or recovery bypasses them.

N/A: gap

Work: `FW-ID-01`

### REQ-P1-ROADMAP-IDENTITY-SESSION-DEVICE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-IDENTITY-SESSION-DEVICE-01`

RequirementText: Deliver and prove session and device control.

ContentLocator: `session/device control`

Owner: Platform identity lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization identity session device 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Session or device controls retain unauthorized access.

N/A: gap

Work: `FW-ID-01`

### REQ-P1-ROADMAP-IDENTITY-TRUSTED-IP-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-IDENTITY-TRUSTED-IP-01`

RequirementText: Deliver and prove trusted-IP behavior where supported.

ContentLocator: `trusted-IP behavior where supported`

Owner: Platform identity lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization identity trusted ip 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Trusted-IP handling grants or blocks access incorrectly.

N/A: gap

Work: `FW-ID-01`

### REQ-P1-ROADMAP-IDENTITY-PROFILE-EMAIL-PASSWORD-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-IDENTITY-PROFILE-EMAIL-PASSWORD-01`

RequirementText: Deliver and prove profile, email, and password change.

ContentLocator: `profile/email/password change`

Owner: Platform identity lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization identity profile email password 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Account changes bypass required identity controls.

N/A: gap

Work: `FW-ID-01`

### REQ-P1-ROADMAP-IDENTITY-REAUTH-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-IDENTITY-REAUTH-01`

RequirementText: Deliver and prove re-authentication.

ContentLocator: `re-authentication`

Owner: Platform identity lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization identity reauth 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Sensitive account changes proceed without required re-authentication.

N/A: gap

Work: `FW-ID-01`

### REQ-P1-ROADMAP-IDENTITY-AUDIT-EVENTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-IDENTITY-AUDIT-EVENTS-01`

RequirementText: Deliver and prove account and security audit events.

ContentLocator: `audit events`

Owner: Platform identity lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization identity audit events 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Security-relevant account activity is not auditable.

N/A: gap

Work: `FW-ID-01`

### REQ-P1-ROADMAP-AUTHZ-SELECTION-PERSISTENCE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-AUTHZ-SELECTION-PERSISTENCE-01`

RequirementText: Deliver and prove authorization selection persistence.

ContentLocator: `selection persistence`

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization authz selection persistence 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Persisted selection crosses an organization or project boundary.

N/A: gap

Work: `FW-AUTH-01`

### REQ-P1-ROADMAP-AUTHZ-OWNER-INVARIANTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-AUTHZ-OWNER-INVARIANTS-01`

RequirementText: Deliver and prove owner invariants.

ContentLocator: `owner invariants`

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization authz owner invariants 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Organization ownership can be lost or escalated incorrectly.

N/A: gap

Work: `FW-AUTH-01`

### REQ-P1-ROADMAP-AUTHZ-INVITATIONS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-AUTHZ-INVITATIONS-01`

RequirementText: Deliver and prove invitations.

ContentLocator: `invitations`

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization authz invitations 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Invitation flows grant unintended access.

N/A: gap

Work: `FW-AUTH-01`

### REQ-P1-ROADMAP-AUTHZ-MEMBERSHIP-CHANGES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-AUTHZ-MEMBERSHIP-CHANGES-01`

RequirementText: Deliver and prove membership role changes, removal, and leave.

ContentLocator: `membership role changes/removal/leave`

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization authz membership changes 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Membership transitions leave incorrect role or access state.

N/A: gap

Work: `FW-AUTH-01`

### REQ-P1-ROADMAP-AUTHZ-PROJECT-ACCESS-OWNERSHIP-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-AUTHZ-PROJECT-ACCESS-OWNERSHIP-01`

RequirementText: Deliver and prove project access and ownership.

ContentLocator: `project access/ownership`

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization authz project access ownership 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Project access or ownership crosses the intended boundary.

N/A: gap

Work: `FW-AUTH-01`

### REQ-P1-ROADMAP-AUTHZ-CROSS-DENIAL-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-AUTHZ-CROSS-DENIAL-01`

RequirementText: Deliver and prove cross-organization and cross-project denial.

ContentLocator: `cross-organization/project denial`

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization authz cross denial 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A customer crosses organization or project authorization boundaries.

N/A: gap

Work: `FW-AUTH-01`

### REQ-P1-ROADMAP-AUTHZ-IMMEDIATE-REVOCATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-ROADMAP-AUTHZ-IMMEDIATE-REVOCATION-01`

RequirementText: Deliver and prove immediate permission revocation.

ContentLocator: `immediate permission revocation`

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 1 identity and organization authz immediate revocation 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Revoked permissions remain usable.

N/A: gap

Work: `FW-AUTH-01`

### REQ-P2-ROADMAP-ORCH-PROVISION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-ORCH-PROVISION-01`

RequirementText: Implement Orchestrator-owned reconciled instance provision lifecycle.

ContentLocator: `provision`

Owner: Platform database and Orchestrator lifecycle leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product orch provision 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-PROVISION-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Provisioning lacks reconciled lifecycle control.

N/A: gap

Work: `FW-DB-PROVISION-02`

### REQ-P2-ROADMAP-ORCH-CONFIGURE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-ORCH-CONFIGURE-01`

RequirementText: Implement Orchestrator-owned reconciled instance configuration lifecycle.

ContentLocator: `configure`

Owner: Platform database and Orchestrator lifecycle leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product orch configure 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-PROVISION-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Configuration diverges from requested managed state.

N/A: gap

Work: `FW-DB-PROVISION-02`

### REQ-P2-ROADMAP-ORCH-ENDPOINT-ROUTING-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-ORCH-ENDPOINT-ROUTING-01`

RequirementText: Implement Orchestrator-owned reconciled endpoint and routing lifecycle.

ContentLocator: `endpoint/routing`

Owner: Platform database and Orchestrator lifecycle leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product orch endpoint routing 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-PROVISION-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Endpoints or routing expose the wrong customer instance.

N/A: gap

Work: `FW-DB-PROVISION-02`

### REQ-P2-ROADMAP-ORCH-HEALTH-READINESS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-ORCH-HEALTH-READINESS-01`

RequirementText: Implement Orchestrator-owned reconciled health and readiness lifecycle.

ContentLocator: `health/readiness`

Owner: Platform database and Orchestrator lifecycle leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product orch health readiness 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-PROVISION-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Readiness is reported before a managed instance is usable.

N/A: gap

Work: `FW-DB-PROVISION-02`

### REQ-P2-ROADMAP-ORCH-RESIZE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-ORCH-RESIZE-01`

RequirementText: Implement Orchestrator-owned reconciled resize lifecycle.

ContentLocator: `resize`

Owner: Platform database and Orchestrator lifecycle leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product orch resize 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-OPERATE-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Resize requests produce unsafe or unreconciled capacity state.

N/A: gap

Work: `FW-DB-OPERATE-02`

### REQ-P2-ROADMAP-ORCH-MAINTENANCE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-ORCH-MAINTENANCE-01`

RequirementText: Implement Orchestrator-owned reconciled maintenance lifecycle.

ContentLocator: `maintenance`

Owner: Platform database and Orchestrator lifecycle leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product orch maintenance 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-OPERATE-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Maintenance changes are not safely controlled or communicated.

N/A: gap

Work: `FW-DB-OPERATE-02`

### REQ-P2-ROADMAP-ORCH-SUSPEND-RESTRICT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-ORCH-SUSPEND-RESTRICT-01`

RequirementText: Implement Orchestrator-owned reconciled suspend and restrict lifecycle.

ContentLocator: `suspend/restrict`

Owner: Platform database and Orchestrator lifecycle leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product orch suspend restrict 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-OPERATE-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Suspension or restriction leaves unauthorized access.

N/A: gap

Work: `FW-DB-OPERATE-02`

### REQ-P2-ROADMAP-ORCH-CREDENTIAL-ISSUANCE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-ORCH-CREDENTIAL-ISSUANCE-01`

RequirementText: Implement reconciled credential issuance.

ContentLocator: `credential issuance`

Owner: Platform database and security leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product orch credential issuance 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-CREDENTIAL-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Credential issuance bypasses managed lifecycle controls.

N/A: gap

Work: `FW-DB-CREDENTIAL-02`

### REQ-P2-ROADMAP-ORCH-CREDENTIAL-ROTATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-ORCH-CREDENTIAL-ROTATION-01`

RequirementText: Implement reconciled credential rotation.

ContentLocator: `rotation`

Owner: Platform database and security leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product orch credential rotation 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-CREDENTIAL-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Credential rotation leaves unsafe active credentials.

N/A: gap

Work: `FW-DB-CREDENTIAL-02`

### REQ-P2-ROADMAP-ORCH-CREDENTIAL-REVOCATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-ORCH-CREDENTIAL-REVOCATION-01`

RequirementText: Implement reconciled credential revocation.

ContentLocator: `revocation`

Owner: Platform database and security leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product orch credential revocation 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-CREDENTIAL-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Revoked credentials remain usable.

N/A: gap

Work: `FW-DB-CREDENTIAL-02`

### REQ-P2-ROADMAP-ORCH-QUOTA-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-ORCH-QUOTA-01`

RequirementText: Implement reconciled quota lifecycle.

ContentLocator: `quota`

Owner: Platform database and Orchestrator lifecycle leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product orch quota 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-OPERATE-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Quota enforcement is bypassed or inconsistent.

N/A: gap

Work: `FW-DB-OPERATE-02`

### REQ-P2-ROADMAP-ORCH-SAFE-DELETION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-ORCH-SAFE-DELETION-01`

RequirementText: Implement reconciled safe deletion lifecycle.

ContentLocator: `safe deletion`

Owner: Platform database and Orchestrator lifecycle leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product orch safe deletion 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-PROVISION-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Deletion is unsafe or incomplete.

N/A: gap

Work: `FW-DB-PROVISION-02`

### REQ-P2-ROADMAP-ORCH-DURABLE-IDEMPOTENCY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-ORCH-DURABLE-IDEMPOTENCY-01`

RequirementText: Implement durable idempotent state transitions.

ContentLocator: `durable idempotent state transitions`

Owner: Platform database and Orchestrator lifecycle leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product orch durable idempotency 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-PROVISION-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Retries create divergent lifecycle state.

N/A: gap

Work: `FW-DB-PROVISION-02`

### REQ-P2-ROADMAP-TERRABASE-TOPOLOGY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-TERRABASE-TOPOLOGY-01`

RequirementText: Convert TerraBase topology into an explicit supported managed contract.

ContentLocator: `topology`

Owner: TerraBase and Platform database leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product terrabase topology 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-PROVISION-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Managed topology behavior is unsupported or ambiguous.

N/A: gap

Work: `FW-DB-PROVISION-02`

### REQ-P2-ROADMAP-TERRABASE-REGION-PLACEMENT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-TERRABASE-REGION-PLACEMENT-01`

RequirementText: Convert TerraBase region placement into an explicit supported managed contract.

ContentLocator: `region placement`

Owner: TerraBase and Platform database leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product terrabase region placement 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-PROVISION-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Placement violates the selected managed contract.

N/A: gap

Work: `FW-DB-PROVISION-02`

### REQ-P2-ROADMAP-TERRABASE-BRANCH-CLONE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-TERRABASE-BRANCH-CLONE-01`

RequirementText: Convert TerraBase branch and clone semantics into explicit supported managed contracts.

ContentLocator: `branch/clone semantics`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product terrabase branch clone 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Branch or clone behavior is represented without supported semantics.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-P2-ROADMAP-TERRABASE-BACKUP-SCHEDULING-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-TERRABASE-BACKUP-SCHEDULING-01`

RequirementText: Convert TerraBase backup scheduling into an explicit supported managed contract.

ContentLocator: `backup scheduling`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product terrabase backup scheduling 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Backups run without an auditable supported schedule.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-P2-ROADMAP-TERRABASE-ENCRYPTED-RETENTION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-TERRABASE-ENCRYPTED-RETENTION-01`

RequirementText: Convert TerraBase encrypted retention and immutability into explicit supported managed contracts.

ContentLocator: `encrypted retention/immutability`

Owner: TerraBase recovery and security leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product terrabase encrypted retention 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Retention or immutability fails to protect stored recovery data.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-P2-ROADMAP-TERRABASE-CONTINUOUS-LOG-PITR-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-TERRABASE-CONTINUOUS-LOG-PITR-01`

RequirementText: Convert TerraBase continuous-log and PITR behavior where supported into an explicit managed contract.

ContentLocator: `continuous-log/PITR where supported`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product terrabase continuous log pitr 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Continuous-log or PITR behavior is claimed without supported semantics.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-P2-ROADMAP-TERRABASE-RESTORE-NEW-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-TERRABASE-RESTORE-NEW-01`

RequirementText: Convert TerraBase restore-to-new-instance behavior into an explicit supported managed contract.

ContentLocator: `restore-to-new instance`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product terrabase restore new 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Restore overwrites or exposes the wrong managed instance.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-P2-ROADMAP-TERRABASE-VALIDATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-TERRABASE-VALIDATION-01`

RequirementText: Convert TerraBase recovery validation into an explicit supported managed contract.

ContentLocator: `validation`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product terrabase validation 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Recovery completion is not validated.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-P2-ROADMAP-TERRABASE-CUTOVER-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-TERRABASE-CUTOVER-01`

RequirementText: Convert TerraBase recovery cutover into an explicit supported managed contract.

ContentLocator: `cutover`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product terrabase cutover 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Recovery cutover leaves customers on inconsistent state.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-P2-ROADMAP-TERRABASE-ROLLBACK-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-TERRABASE-ROLLBACK-01`

RequirementText: Convert TerraBase recovery rollback into an explicit supported managed contract.

ContentLocator: `rollback`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product terrabase rollback 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Recovery cannot safely return from a failed cutover.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-P2-ROADMAP-TERRABASE-CUSTOMER-RECOVERY-STATE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-TERRABASE-CUSTOMER-RECOVERY-STATE-01`

RequirementText: Convert auditable customer recovery state into an explicit supported managed contract.

ContentLocator: `auditable customer recovery state`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product terrabase customer recovery state 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Customer recovery state is not auditable.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-P2-ROADMAP-PUBLIC-DATABASE-DATA-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-PUBLIC-DATABASE-DATA-01`

RequirementText: Complete database data operations through public consumer interfaces.

ContentLocator: `database data`

Owner: Platform database lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product public database data 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Database data operations bypass public tenant controls.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-PUBLIC-API-KEY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-PUBLIC-API-KEY-01`

RequirementText: Complete API-key operations through public consumer interfaces.

ContentLocator: `API-key`

Owner: Platform database and security leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product public api key 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-SECURITY-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: API-key operations expose or misuse credentials.

N/A: gap

Work: `FW-DB-SECURITY-02`

### REQ-P2-ROADMAP-PUBLIC-ENVIRONMENT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-PUBLIC-ENVIRONMENT-01`

RequirementText: Complete environment operations through public consumer interfaces.

ContentLocator: `environment operations`

Owner: Platform database lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product public environment 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Environment operations cross customer boundaries.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-PUBLIC-QUEUES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-PUBLIC-QUEUES-01`

RequirementText: Complete queue operations through public consumer interfaces.

ContentLocator: `queues`

Owner: Platform database lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product public queues 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Queue operations lack supported public behavior.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-PUBLIC-AUTHENTICATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-PUBLIC-AUTHENTICATION-01`

RequirementText: Complete project Authentication product workflows through public consumer interfaces.

ContentLocator: `project Authentication product workflows`

Owner: Platform Authentication lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product public authentication 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Authentication workflows lack supported customer isolation.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-PUBLIC-PUBLIC-CONTRACTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-PUBLIC-PUBLIC-CONTRACTS-01`

RequirementText: Complete the listed product workflows through public contracts.

ContentLocator: `through public contracts`

Owner: Platform API lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product public public contracts 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Customer workflows use non-public or unversioned contracts.

N/A: gap

Work: `FW-DB-CONTRACT-01`

### REQ-P2-ROADMAP-PUBLIC-TYPED-SDKS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-PUBLIC-TYPED-SDKS-01`

RequirementText: Complete the listed product workflows through typed SDKs.

ContentLocator: `typed SDKs`

Owner: SDK architecture lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product public typed sdks 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Customer workflows require untyped SDK access.

N/A: gap

Work: `FW-DB-CONTRACT-01`

### REQ-P2-ROADMAP-PUBLIC-DASHBOARD-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-PUBLIC-DASHBOARD-01`

RequirementText: Complete the listed product workflows through the Dashboard.

ContentLocator: `Dashboard`

Owner: Dashboard lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product public dashboard 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard workflows bypass the public customer boundary.

N/A: gap

Work: `FW-DASH-06`

### REQ-P2-ROADMAP-PUBLIC-AUTHORIZED-MCP-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-PUBLIC-AUTHORIZED-MCP-01`

RequirementText: Complete the listed product workflows through authorized MCP workflows.

ContentLocator: `authorized MCP workflows`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product public authorized mcp 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: MCP workflows exceed customer authorization.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-PUBLIC-OWNER-ISOLATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-PUBLIC-OWNER-ISOLATION-01`

RequirementText: Validate owner isolation on a real stack.

ContentLocator: `owner/member/project isolation`

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product public owner isolation 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Owner access is not isolated.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-PUBLIC-RETRIES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-PUBLIC-RETRIES-01`

RequirementText: Validate retries on a real stack.

ContentLocator: `retries`

Owner: Platform database lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product public retries 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Retry behavior is not validated against the real stack.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-PUBLIC-PARTIAL-FAILURE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-PUBLIC-PARTIAL-FAILURE-01`

RequirementText: Validate partial failure on a real stack.

ContentLocator: `partial failure`

Owner: Platform database lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product public partial failure 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Partial failures leave unsafe lifecycle state.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-PUBLIC-CANCELLATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-PUBLIC-CANCELLATION-01`

RequirementText: Validate cancellation on a real stack.

ContentLocator: `cancellation`

Owner: Platform database lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product public cancellation 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Cancellation leaves an unsafe in-progress operation.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-PUBLIC-LIFECYCLE-CLEANUP-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-PUBLIC-LIFECYCLE-CLEANUP-01`

RequirementText: Validate lifecycle cleanup on a real stack.

ContentLocator: `lifecycle cleanup`

Owner: Platform database lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product public lifecycle cleanup 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Lifecycle cleanup leaves customer resources or data behind.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-PUBLIC-REAL-STACK-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-PUBLIC-REAL-STACK-01`

RequirementText: Validate the listed workflows on a real stack.

ContentLocator: `on a real stack`

Owner: Platform database lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product public real stack 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Workflow evidence does not exercise a real product boundary.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-EXIT-CREATE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-EXIT-CREATE-01`

RequirementText: Produce public E2E evidence for create.

ContentLocator: `create/use/rotate/backup/restore/delete`

Owner: Platform database lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product exit create 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Create lacks public end-to-end evidence.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-EXIT-USE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-EXIT-USE-01`

RequirementText: Produce public E2E evidence for use.

ContentLocator: `use/rotate/backup/restore/delete`

Owner: Platform database lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product exit use 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Use lacks public end-to-end evidence.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-EXIT-ROTATE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-EXIT-ROTATE-01`

RequirementText: Produce public E2E evidence for rotate.

ContentLocator: `rotate/backup/restore/delete`

Owner: Platform database and security leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product exit rotate 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-CREDENTIAL-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Rotation lacks public end-to-end evidence.

N/A: gap

Work: `FW-DB-CREDENTIAL-02`

### REQ-P2-ROADMAP-EXIT-BACKUP-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-EXIT-BACKUP-01`

RequirementText: Produce public E2E evidence for backup.

ContentLocator: `backup/restore/delete`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product exit backup 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Backup lacks public end-to-end evidence.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-P2-ROADMAP-EXIT-RESTORE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-EXIT-RESTORE-01`

RequirementText: Produce public E2E evidence for restore.

ContentLocator: `restore/delete`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product exit restore 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Restore lacks public end-to-end evidence.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-P2-ROADMAP-EXIT-DELETE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-EXIT-DELETE-01`

RequirementText: Produce public E2E evidence for delete.

ContentLocator: `delete`

Owner: Platform database lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product exit delete 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Delete lacks public end-to-end evidence.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-EXIT-QUEUE-PUBLISH-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-EXIT-QUEUE-PUBLISH-01`

RequirementText: Produce public E2E evidence for queue publish.

ContentLocator: `queue publish`

Owner: Platform database lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product exit queue publish 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Queue publish lacks public end-to-end evidence.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-EXIT-QUEUE-CONSUME-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-EXIT-QUEUE-CONSUME-01`

RequirementText: Produce public E2E evidence for queue consume.

ContentLocator: `queue publish/consume`

Owner: Platform database lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product exit queue consume 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Queue consume lacks public end-to-end evidence.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-EXIT-QUEUE-DEAD-LETTER-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-EXIT-QUEUE-DEAD-LETTER-01`

RequirementText: Produce public E2E evidence for queue dead-letter.

ContentLocator: `queue publish/consume/dead-letter`

Owner: Platform database lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product exit queue dead letter 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Queue dead-letter handling lacks public end-to-end evidence.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-EXIT-AUTH-ENABLE-DISABLE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-EXIT-AUTH-ENABLE-DISABLE-01`

RequirementText: Produce public E2E evidence for Authentication enable and disable impact.

ContentLocator: `Authentication enable/disable impact`

Owner: Platform Authentication lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product exit auth enable disable 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Authentication enable or disable impact lacks public evidence.

N/A: gap

Work: `FW-DB-02`

### REQ-P2-ROADMAP-EXIT-CUSTOMER-SAFE-AUDIT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-EXIT-CUSTOMER-SAFE-AUDIT-01`

RequirementText: Produce public E2E evidence for customer-safe audit history.

ContentLocator: `customer-safe audit history`

Owner: Platform security lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product exit customer safe audit 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-SECURITY-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Audit history exposes unsafe customer information.

N/A: gap

Work: `FW-DB-SECURITY-02`

### REQ-P2-ROADMAP-EXIT-NO-ENDPOINT-LEAK-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-EXIT-NO-ENDPOINT-LEAK-01`

RequirementText: Produce public E2E evidence of no leaked endpoint data.

ContentLocator: `no leaked endpoint/credential/tenant data`

Owner: Platform security lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product exit no endpoint leak 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-SECURITY-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Endpoint data leaks across customer boundaries.

N/A: gap

Work: `FW-DB-SECURITY-02`

### REQ-P2-ROADMAP-EXIT-NO-CREDENTIAL-LEAK-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-EXIT-NO-CREDENTIAL-LEAK-01`

RequirementText: Produce public E2E evidence of no leaked credential data.

ContentLocator: `endpoint/credential/tenant data`

Owner: Platform security lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product exit no credential leak 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-SECURITY-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Credential data leaks across customer boundaries.

N/A: gap

Work: `FW-DB-SECURITY-02`

### REQ-P2-ROADMAP-EXIT-NO-TENANT-LEAK-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-ROADMAP-EXIT-NO-TENANT-LEAK-01`

RequirementText: Produce public E2E evidence of no leaked tenant data.

ContentLocator: `credential/tenant data`

Owner: Platform security lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 2 public database product exit no tenant leak 01 lifecycle, credential, queue, Authentication, audit, and no-leak receipt; Work contract: `FW-DB-SECURITY-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Tenant data leaks across customer boundaries.

N/A: gap

Work: `FW-DB-SECURITY-02`

### REQ-P3-ROADMAP-HOST-BOOTSTRAP-ROLLBACK-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-HOST-BOOTSTRAP-ROLLBACK-01`

RequirementText: Deliver signed A/B bootstrap and rollback.

ContentLocator: `signed A/B bootstrap and rollback`

Owner: Orchestrator runtime lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary host bootstrap rollback 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Bootstrap or rollback lacks signed recovery control.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-HOST-PID1-SYSTEMD-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-HOST-PID1-SYSTEMD-01`

RequirementText: Deliver the PID-1 and systemd boundary.

ContentLocator: `PID-1/systemd boundary`

Owner: Orchestrator runtime lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary host pid1 systemd 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Workloads run without a controlled host-process boundary.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-HOST-CONTAINERD-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-HOST-CONTAINERD-01`

RequirementText: Deliver a live containerd client.

ContentLocator: `live containerd client`

Owner: Orchestrator runtime lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary host containerd 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Runtime state is not reconciled through the live container runtime.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-HOST-ROLE-ISOLATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-HOST-ROLE-ISOLATION-01`

RequirementText: Deliver workload role isolation.

ContentLocator: `workload role isolation`

Owner: Orchestrator runtime lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary host role isolation 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Workload roles can cross their intended privileges.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-HOST-SCHEDULING-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-HOST-SCHEDULING-01`

RequirementText: Deliver scheduling, discovery, rollout, drain, and anti-affinity.

ContentLocator: `scheduling/discovery/rollout/drain/anti-affinity`

Owner: Orchestrator runtime lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary host scheduling 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Workload placement or transition is unsafe.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-HOST-PROVIDER-TRUTH-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-HOST-PROVIDER-TRUTH-01`

RequirementText: Deliver provider-truth reconciliation.

ContentLocator: `provider-truth reconciliation`

Owner: Orchestrator runtime lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary host provider truth 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Recorded and provider state diverge.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-TERRABASE-CERTIFICATES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-TERRABASE-CERTIFICATES-01`

RequirementText: Deliver certificate issuance and rotation.

ContentLocator: `certificate issuance and rotation`

Owner: TerraBase and Orchestrator runtime leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary terrabase certificates 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Certificate lifecycle leaves invalid or exposed trust material.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-TERRABASE-STORAGE-EXPANSION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-TERRABASE-STORAGE-EXPANSION-01`

RequirementText: Deliver storage, device, and filesystem expansion.

ContentLocator: `storage/device/filesystem expansion`

Owner: TerraBase and Orchestrator runtime leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary terrabase storage expansion 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Storage expansion leaves unavailable or inconsistent state.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-TERRABASE-TOPOLOGY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-TERRABASE-TOPOLOGY-01`

RequirementText: Deliver topology changes.

ContentLocator: `topology changes`

Owner: TerraBase and Orchestrator runtime leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary terrabase topology 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Topology changes violate the multi-member recovery contract.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-TERRABASE-HEALTH-QUORUM-FENCING-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-TERRABASE-HEALTH-QUORUM-FENCING-01`

RequirementText: Deliver health, quorum, and fencing.

ContentLocator: `health/quorum/fencing`

Owner: TerraBase and Orchestrator runtime leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary terrabase health quorum fencing 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Quorum loss or fencing failure allows unsafe membership.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-TERRABASE-REPLICATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-TERRABASE-REPLICATION-01`

RequirementText: Deliver replication.

ContentLocator: `replication`

Owner: TerraBase and Orchestrator runtime leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary terrabase replication 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Replication does not meet the managed recovery contract.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-TERRABASE-FAILOVER-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-TERRABASE-FAILOVER-01`

RequirementText: Deliver failover.

ContentLocator: `failover`

Owner: TerraBase and Orchestrator runtime leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary terrabase failover 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Failover leaves unavailable or split service state.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-TERRABASE-REPAIR-REBALANCE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-TERRABASE-REPAIR-REBALANCE-01`

RequirementText: Deliver repair and rebalance.

ContentLocator: `repair/rebalance`

Owner: TerraBase and Orchestrator runtime leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary terrabase repair rebalance 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Repair or rebalance fails to restore safe membership.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-TERRABASE-REGIONAL-FAILOVER-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-TERRABASE-REGIONAL-FAILOVER-01`

RequirementText: Deliver regional failover.

ContentLocator: `regional failover`

Owner: TerraBase and Orchestrator runtime leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary terrabase regional failover 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Regional failover lacks recovery evidence.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-TERRABASE-RESTORE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-TERRABASE-RESTORE-01`

RequirementText: Deliver restore controllers.

ContentLocator: `restore`

Owner: TerraBase and Orchestrator runtime leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary terrabase restore 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Restore controller behavior is not safely orchestrated.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-P3-ROADMAP-TERRABASE-UPGRADE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-TERRABASE-UPGRADE-01`

RequirementText: Deliver upgrade controllers.

ContentLocator: `upgrade`

Owner: TerraBase and Orchestrator runtime leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary terrabase upgrade 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Upgrade controller behavior threatens availability or recovery.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-TERRABASE-SCALE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-TERRABASE-SCALE-01`

RequirementText: Deliver scale controllers.

ContentLocator: `scale controllers`

Owner: TerraBase and Orchestrator runtime leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary terrabase scale 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Scale control leaves unsafe capacity or membership state.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-RECOVERY-BACKUP-PITR-DR-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-RECOVERY-BACKUP-PITR-DR-01`

RequirementText: Validate backup, PITR, and DR objectives.

ContentLocator: `backup/PITR/DR objectives`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary recovery backup pitr dr 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Recovery objectives are not validated.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-P3-ROADMAP-RECOVERY-RESTORE-DRILLS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-RECOVERY-RESTORE-DRILLS-01`

RequirementText: Validate automated restore drills.

ContentLocator: `automated restore drills`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary recovery restore drills 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Restore cannot be repeated automatically.

N/A: gap

Work: `FW-DB-RESILIENCE-03`

### REQ-P3-ROADMAP-RECOVERY-FAILURE-EXPERIMENTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-RECOVERY-FAILURE-EXPERIMENTS-01`

RequirementText: Validate zone, controller, host, volume, and region failure experiments.

ContentLocator: `zone/controller/host/volume/region failure experiments`

Owner: TerraBase recovery and Orchestrator runtime leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary recovery failure experiments 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A failure domain lacks recovery validation.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-RECOVERY-RPO-RTO-MEASUREMENTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-RECOVERY-RPO-RTO-MEASUREMENTS-01`

RequirementText: Validate RPO and RTO measurements.

ContentLocator: `RPO/RTO measurements`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary recovery rpo rto measurements 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Recovery objectives are unmeasured.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-RECOVERY-CLEAN-ROOM-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-RECOVERY-CLEAN-ROOM-01`

RequirementText: Validate clean-room recovery.

ContentLocator: `clean-room recovery`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary recovery clean room 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Recovery proof depends on contaminated environment state.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-RECOVERY-CUSTOMER-RUNBOOK-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-RECOVERY-CUSTOMER-RUNBOOK-01`

RequirementText: Validate customer runbooks.

ContentLocator: `customer and operator runbooks`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary recovery customer runbook 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Customers lack a recovery procedure.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-RECOVERY-EVIDENCE-RETENTION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-RECOVERY-EVIDENCE-RETENTION-01`

RequirementText: Validate evidence retention.

ContentLocator: `evidence retention`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary recovery evidence retention 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Recovery evidence cannot be independently reviewed.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-EXIT-R3-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-EXIT-R3-01`

RequirementText: Produce R3 production-boundary tests.

ContentLocator: `R3/L3/L4 production-boundary tests`

Owner: Orchestrator recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary exit r3 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: R3 behavior lacks production-boundary evidence.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-EXIT-L3-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-EXIT-L3-01`

RequirementText: Produce L3 production-boundary tests.

ContentLocator: `L3/L4 production-boundary tests`

Owner: Orchestrator recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary exit l3 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: L3 behavior lacks production-boundary evidence.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-EXIT-L4-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-EXIT-L4-01`

RequirementText: Produce L4 production-boundary tests.

ContentLocator: `L4 production-boundary tests`

Owner: Orchestrator recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary exit l4 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: L4 behavior lacks production-boundary evidence.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-EXIT-DESTRUCTIVE-RECOVERY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-EXIT-DESTRUCTIVE-RECOVERY-01`

RequirementText: Produce destructive recovery proof.

ContentLocator: `destructive recovery proof`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary exit destructive recovery 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Recovery is asserted without destructive proof.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-EXIT-APPROVED-RPO-RTO-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-EXIT-APPROVED-RPO-RTO-01`

RequirementText: Produce measured RPO and RTO within approved SLOs.

ContentLocator: `measured RPO/RTO within approved SLOs`

Owner: TerraBase recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary exit approved rpo rto 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Measured recovery does not meet approved objectives.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-EXIT-SURVIVAL-BUNDLE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-EXIT-SURVIVAL-BUNDLE-01`

RequirementText: Produce a signed survival bundle.

ContentLocator: `signed survival bundle`

Owner: Orchestrator recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary exit survival bundle 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Survival evidence lacks signed provenance.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-EXIT-NO-RF1-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-EXIT-NO-RF1-01`

RequirementText: Prove no reliance on local RF=1 assumptions.

ContentLocator: `no reliance on local RF=1`

Owner: Orchestrator recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary exit no rf1 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Recovery depends on local RF=1 assumptions.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-EXIT-NO-DEV-PKI-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-EXIT-NO-DEV-PKI-01`

RequirementText: Prove no reliance on development PKI assumptions.

ContentLocator: `dev PKI`

Owner: Orchestrator recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary exit no dev pki 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Recovery depends on development PKI assumptions.

N/A: gap

Work: `FW-REC-03`

### REQ-P3-ROADMAP-EXIT-NO-LAB-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-ROADMAP-EXIT-NO-LAB-01`

RequirementText: Prove no reliance on lab assumptions.

ContentLocator: `lab assumptions`

Owner: Orchestrator recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Phase 3 production boundary exit no lab 01 recovery, RPO-RTO, survival, no-RF1, no-dev-PKI, and no-lab receipt; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Recovery depends on lab assumptions.

N/A: gap

Work: `FW-REC-03`

### REQ-P4-ROADMAP-BILL-PLANS-ENTITLEMENTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-BILL-PLANS-ENTITLEMENTS-01`

RequirementText: Complete organization-scoped plans and entitlements.

ContentLocator: `organization-scoped plans, entitlements`

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox bill plans entitlements 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Billing plans or entitlements cross organization boundaries.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-BILL-TRIAL-RESTRICTED-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-BILL-TRIAL-RESTRICTED-01`

RequirementText: Complete trial and restricted state.

ContentLocator: `trial/restricted state`

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox bill trial restricted 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Trial or restricted state is not enforced.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-BILL-TRANSITIONS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-BILL-TRANSITIONS-01`

RequirementText: Complete upgrades, downgrades, cancellation, and reactivation.

ContentLocator: `upgrades/downgrades, cancellation/reactivation`

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox bill transitions 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Subscription transitions produce inconsistent entitlement state.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-BILL-PAYMENT-METHODS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-BILL-PAYMENT-METHODS-01`

RequirementText: Complete provider-hosted payment methods.

ContentLocator: `provider-hosted payment methods`

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox bill payment methods 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Payment methods bypass the approved provider-hosted flow.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-BILL-INVOICES-RECEIPTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-BILL-INVOICES-RECEIPTS-01`

RequirementText: Complete invoices and receipts.

ContentLocator: `invoices/receipts`

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox bill invoices receipts 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Customer billing records are incomplete or inaccessible.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-BILL-USAGE-OVERAGES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-BILL-USAGE-OVERAGES-01`

RequirementText: Complete usage aggregation and overages.

ContentLocator: `usage aggregation/overages`

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox bill usage overages 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Usage or overage calculations are inconsistent.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-BILL-AUDIT-RECONCILIATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-BILL-AUDIT-RECONCILIATION-01`

RequirementText: Complete financial audit and reconciliation.

ContentLocator: `financial audit/reconciliation`

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox bill audit reconciliation 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial events cannot be reconciled.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-SECRET-APPROVED-IMPORT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-SECRET-APPROVED-IMPORT-01`

RequirementText: Configure the supplied Polar Sandbox credential only after authorized operator import into an approved secret manager or ignored local runtime secret.

ContentLocator: `approved secret manager or ignored local runtime secret after an authorized operator imports it`

Owner: Platform billing security lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox secret approved import 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A Polar credential is imported outside an approved secret boundary.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-SECRET-NO-SECRET-DISCLOSURE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-SECRET-NO-SECRET-DISCLOSURE-01`

RequirementText: Do not repeat, export, log, commit, fixture, or place the supplied credential in documentation.

ContentLocator: `Do not repeat, export, log, commit, fixture, or place the value in documentation.`

Owner: Platform billing security lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox secret no secret disclosure 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A supplied billing secret is disclosed.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-SECRET-REDACTED-REFERENCES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-SECRET-REDACTED-REFERENCES-01`

RequirementText: Record only redacted secret references and sandbox scenario results.

ContentLocator: `Record only redacted secret references and sandbox scenario results.`

Owner: Platform billing security lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox secret redacted references 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Billing evidence contains raw secret material.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-POLAR-CHECKOUT-PAYMENT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-POLAR-CHECKOUT-PAYMENT-01`

RequirementText: Execute initial checkout and payment validation or update.

ContentLocator: `initial checkout, payment validation/update`

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox polar checkout payment 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Checkout or payment updates lack real sandbox evidence.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-POLAR-APPROVAL-SUBSCRIPTION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-POLAR-APPROVAL-SUBSCRIPTION-01`

RequirementText: Execute approval, failure, subscription transition, and renewal flows.

ContentLocator: `approval/failure, subscription transition, renewal`

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox polar approval subscription 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Subscription state transitions are not validated against Polar.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-POLAR-CANCELLATION-USAGE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-POLAR-CANCELLATION-USAGE-01`

RequirementText: Execute cancellation, reactivation, usage, and overage flows.

ContentLocator: `cancellation/reactivation, usage/overage`

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox polar cancellation usage 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Cancellation or usage changes leave inconsistent billing state.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-POLAR-WEBHOOKS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-POLAR-WEBHOOKS-01`

RequirementText: Execute webhook signature, idempotency, retry, and out-of-order handling.

ContentLocator: `webhook signature/idempotency/retry/out-of-order handling`

Owner: Platform billing security lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox polar webhooks 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Webhook handling accepts forged, duplicate, or unordered events unsafely.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-POLAR-RECEIPT-PORTAL-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-POLAR-RECEIPT-PORTAL-01`

RequirementText: Execute receipt and portal access flows.

ContentLocator: `receipt/portal access`

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox polar receipt portal 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Customers cannot safely access billing records.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-POLAR-RECONCILIATION-NOTICE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-POLAR-RECONCILIATION-NOTICE-01`

RequirementText: Execute reconciliation and notification preference flows.

ContentLocator: `reconciliation, notification preference`

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox polar reconciliation notice 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Billing records or communications are not reconciled.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-POLAR-ROLE-TENANT-DENIAL-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-POLAR-ROLE-TENANT-DENIAL-01`

RequirementText: Execute role and tenant denial flows.

ContentLocator: `role/tenant denial`

Owner: Platform billing security lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox polar role tenant denial 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Billing access crosses role or tenant boundaries.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-ADMIN-SEPARATE-SURFACE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-ADMIN-SEPARATE-SURFACE-01`

RequirementText: Deliver the audited TerraScale Admin surface separately from customer membership.

ContentLocator: `audited TerraScale Admin surface separately from customer membership`

Owner: Platform Admin lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox admin separate surface 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-ADMIN-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Administrative access is conflated with customer membership.

N/A: gap

Work: `FW-ADMIN-04`

### REQ-P4-ROADMAP-ADMIN-OIDC-RBAC-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-ADMIN-OIDC-RBAC-01`

RequirementText: Deliver Admin OIDC and RBAC.

ContentLocator: `OIDC/RBAC`

Owner: Platform Admin lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox admin oidc rbac 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-ADMIN-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Admin authentication or roles are insufficiently controlled.

N/A: gap

Work: `FW-ADMIN-04`

### REQ-P4-ROADMAP-ADMIN-BREAK-GLASS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-ADMIN-BREAK-GLASS-01`

RequirementText: Deliver Admin break-glass controls.

ContentLocator: `break-glass controls`

Owner: Platform Admin lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox admin break glass 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-ADMIN-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Emergency access lacks control or auditability.

N/A: gap

Work: `FW-ADMIN-04`

### REQ-P4-ROADMAP-ADMIN-LEAST-PRIVILEGE-AUDIT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-ADMIN-LEAST-PRIVILEGE-AUDIT-01`

RequirementText: Deliver least privilege and mandatory audit.

ContentLocator: `least privilege, mandatory audit`

Owner: Platform Admin lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox admin least privilege audit 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-ADMIN-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Admin activity exceeds least privilege or is unaudited.

N/A: gap

Work: `FW-ADMIN-04`

### REQ-P4-ROADMAP-ADMIN-SAFE-DIAGNOSTICS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-ADMIN-SAFE-DIAGNOSTICS-01`

RequirementText: Deliver safe support diagnostics.

ContentLocator: `safe support diagnostics`

Owner: Platform Admin lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox admin safe diagnostics 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-ADMIN-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Support diagnostics expose unsafe customer data.

N/A: gap

Work: `FW-ADMIN-04`

### REQ-P4-ROADMAP-EXIT-SANDBOX-RECONCILIATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-EXIT-SANDBOX-RECONCILIATION-01`

RequirementText: Produce a sandbox report and reconciled provider events.

ContentLocator: `sandbox report and reconciled provider events`

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox exit sandbox reconciliation 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Sandbox billing events are not reconciled.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-EXIT-OWNER-NONOWNER-CROSSORG-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-EXIT-OWNER-NONOWNER-CROSSORG-01`

RequirementText: Produce owner, non-owner, and cross-organization E2E proof.

ContentLocator: `owner/non-owner/cross-org E2E proof`

Owner: Platform billing security lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox exit owner nonowner crossorg 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Billing authorization lacks real boundary proof.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-EXIT-NO-PAYMENT-DATA-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-EXIT-NO-PAYMENT-DATA-01`

RequirementText: Produce evidence of no sensitive payment data in TerraScale.

ContentLocator: `no sensitive payment data in TerraScale`

Owner: Platform billing security lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox exit no payment data 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Sensitive payment data is retained by TerraScale.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-EXIT-ENTITLEMENTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-EXIT-ENTITLEMENTS-01`

RequirementText: Produce enforced entitlements evidence.

ContentLocator: `enforced entitlements`

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox exit entitlements 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Entitlements are not enforced.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-EXIT-COMMUNICATIONS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-EXIT-COMMUNICATIONS-01`

RequirementText: Produce mandatory billing and security communications evidence.

ContentLocator: `mandatory billing/security communications`

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox exit communications 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Required billing or security communications are omitted.

N/A: gap

Work: `FW-BILL-04`

### REQ-P4-ROADMAP-EXIT-RUNBOOK-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-ROADMAP-EXIT-RUNBOOK-01`

RequirementText: Produce an operations runbook.

ContentLocator: `operations runbook`

Owner: Platform billing lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar sandbox exit runbook 01 reconciliation, owner and no-owner, cross-organization denial, no-payment-data, entitlement, notice, and runbook receipt; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Billing operations lack a recovery procedure.

N/A: gap

Work: `FW-BILL-04`

### REQ-P5-ROADMAP-SDK-PARITY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-SDK-PARITY-01`

RequirementText: Close .NET and TypeScript SDK parity for every approved public operation.

ContentLocator: `.NET/TypeScript SDK parity for every approved public operation`

Owner: SDK architecture lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity sdk parity 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: SDK parity is incomplete.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P5-ROADMAP-SDK-CI-INVENTORY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-SDK-CI-INVENTORY-01`

RequirementText: Use the shared contract inventory as a CI failure gate.

ContentLocator: `shared contract inventory as a CI failure gate`

Owner: SDK architecture lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity sdk ci inventory 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Contract drift is not detected in CI.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P5-ROADMAP-SDK-ERROR-REDACTION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-SDK-ERROR-REDACTION-01`

RequirementText: Fix unsafe raw error exposure.

ContentLocator: `unsafe raw error exposure`

Owner: SDK architecture lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity sdk error redaction 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: SDK errors expose unsafe detail.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P5-ROADMAP-SDK-IDEMPOTENCY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-SDK-IDEMPOTENCY-01`

RequirementText: Ensure idempotency spans POST, PATCH, PUT, and DELETE when permitted.

ContentLocator: `idempotency spans POST, PATCH, PUT, and DELETE when the contract permits them`

Owner: SDK architecture lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity sdk idempotency 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Supported mutations lack safe retry semantics.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P5-ROADMAP-MCP-CAPABILITY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-MCP-CAPABILITY-01`

RequirementText: Evolve MCP into capability-complete agent workflows.

ContentLocator: `capability-complete agent workflows`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity mcp capability 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Agent workflows lack required customer capability.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-MCP-SAFETY-TIERS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-MCP-SAFETY-TIERS-01`

RequirementText: Evolve MCP in incremental safety tiers.

ContentLocator: `incremental safety tiers`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity mcp safety tiers 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: MCP capability expands without safety controls.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-MCP-PUBLIC-API-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-MCP-PUBLIC-API-01`

RequirementText: Require a public Platform API before each MCP addition.

ContentLocator: `Each addition first has a public Platform API`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity mcp public api 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: An MCP tool depends on a private API.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-MCP-TYPED-SDK-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-MCP-TYPED-SDK-01`

RequirementText: Require a typed SDK method before each MCP addition.

ContentLocator: `typed SDK method`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity mcp typed sdk 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: An MCP tool bypasses typed SDK parity.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-MCP-AUTH-TENANT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-MCP-AUTH-TENANT-01`

RequirementText: Require authorization and tenant-isolation evidence.

ContentLocator: `authorization and tenant-isolation evidence`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity mcp auth tenant 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: An MCP tool crosses authorization or tenant boundaries.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-MCP-CONFIRM-IMPACT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-MCP-CONFIRM-IMPACT-01`

RequirementText: Require confirmation and impact design.

ContentLocator: `confirmation/impact design`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity mcp confirm impact 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: An MCP mutation lacks safe confirmation.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-MCP-DASH-EQUIVALENT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-MCP-DASH-EQUIVALENT-01`

RequirementText: Require a human Dashboard equivalent.

ContentLocator: `human Dashboard equivalent`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity mcp dash equivalent 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: MCP adds a privileged agent-only capability.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-DISCOVERY-BOUNDED-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-DISCOVERY-BOUNDED-01`

RequirementText: Add missing bounded discovery flows.

ContentLocator: `missing bounded discovery flows`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity discovery bounded 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Discovery is unbounded.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-DISCOVERY-REPOSITORY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-DISCOVERY-REPOSITORY-01`

RequirementText: Begin repository listing only after a typed public contract exists.

ContentLocator: `repository listing only after a typed public contract exists`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity discovery repository 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Repository discovery uses an untyped or private path.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-FORBID-GENERIC-TRANSPORT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-FORBID-GENERIC-TRANSPORT-01`

RequirementText: Do not add generic transport tools.

ContentLocator: `generic transport`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity forbid generic transport 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Generic transport bypasses bounded contracts.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-FORBID-RAW-SECRET-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-FORBID-RAW-SECRET-01`

RequirementText: Do not add raw-secret tools.

ContentLocator: `raw-secret`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity forbid raw secret 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: MCP exposes raw secrets.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-FORBID-RAW-DOCUMENT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-FORBID-RAW-DOCUMENT-01`

RequirementText: Do not add raw-document tools.

ContentLocator: `raw-document`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity forbid raw document 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: MCP exposes raw documents.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-FORBID-ARBITRARY-QUERY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-FORBID-ARBITRARY-QUERY-01`

RequirementText: Do not add arbitrary-query tools.

ContentLocator: `arbitrary-query`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity forbid arbitrary query 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: MCP enables arbitrary queries.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-FORBID-INTERNAL-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-FORBID-INTERNAL-01`

RequirementText: Do not add internal tools.

ContentLocator: `internal`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity forbid internal 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: MCP exposes internal capability.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-FORBID-BILLING-ADMIN-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-FORBID-BILLING-ADMIN-01`

RequirementText: Do not add billing-admin tools without dedicated safety design and evidence.

ContentLocator: `billing-admin`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity forbid billing admin 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: MCP exposes billing administration unsafely.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-FORBID-DESTRUCTIVE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-FORBID-DESTRUCTIVE-01`

RequirementText: Do not add destructive tools without dedicated safety design and evidence.

ContentLocator: `destructive tools without the dedicated safety design and evidence required above`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity forbid destructive 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: MCP enables destructive action without proof.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-DOCS-ONBOARDING-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-DOCS-ONBOARDING-01`

RequirementText: Publish runnable SDK/MCP onboarding.

ContentLocator: `runnable SDK/MCP onboarding`

Owner: Developer experience lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity docs onboarding 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-DB-DEVELOPER-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Developers cannot start SDK or MCP integration.

N/A: gap

Work: `FW-DB-DEVELOPER-02`

### REQ-P5-ROADMAP-DOCS-REFERENCES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-DOCS-REFERENCES-01`

RequirementText: Publish tool, resource, and prompt references.

ContentLocator: `tool/resource/prompt references`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity docs references 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: MCP interfaces lack reference documentation.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-DOCS-COMPATIBILITY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-DOCS-COMPATIBILITY-01`

RequirementText: Publish version compatibility and migration/deprecation guidance.

ContentLocator: `version compatibility, migration/deprecation guidance`

Owner: SDK architecture lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity docs compatibility 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Consumers cannot upgrade safely.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P5-ROADMAP-DOCS-RECOVERY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-DOCS-RECOVERY-01`

RequirementText: Publish error/recovery recipes and local E2E setup.

ContentLocator: `error/recovery recipes, local E2E setup`

Owner: Developer experience lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity docs recovery 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-DB-DEVELOPER-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Developers cannot diagnose or reproduce integrations.

N/A: gap

Work: `FW-DB-DEVELOPER-02`

### REQ-P5-ROADMAP-DOCS-AGENT-EXAMPLES-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-DOCS-AGENT-EXAMPLES-01`

RequirementText: Publish agent-safe examples.

ContentLocator: `agent-safe examples`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity docs agent examples 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Examples teach unsafe agent behavior.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-EXIT-CAPABILITY-MATRIX-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-EXIT-CAPABILITY-MATRIX-01`

RequirementText: Produce the current Dashboard-to-public-API/SDK-to-MCP capability matrix.

ContentLocator: `current Dashboard-to-public-API/SDK-to-MCP capability matrix`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity exit capability matrix 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Capability parity is not traceable.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-EXIT-PARITY-REPORT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-EXIT-PARITY-REPORT-01`

RequirementText: Produce the complete public contract parity report.

ContentLocator: `complete public contract parity report`

Owner: SDK architecture lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity exit parity report 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Public contract parity is incomplete.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P5-ROADMAP-EXIT-REAL-TESTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-EXIT-REAL-TESTS-01`

RequirementText: Produce real success, failure, and cross-tenant tests per operation and tool.

ContentLocator: `real success/failure/cross-tenant tests per operation/tool`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity exit real tests 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Tools lack real-boundary proof.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-EXIT-PROVENANCE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-EXIT-PROVENANCE-01`

RequirementText: Produce signed MCP artifacts and provenance.

ContentLocator: `signed MCP artifacts/provenance`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity exit provenance 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: MCP artifact provenance is unverified.

N/A: gap

Work: `FW-MCP-05`

### REQ-P5-ROADMAP-EXIT-USABILITY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-ROADMAP-EXIT-USABILITY-01`

RequirementText: Produce independent agent-usability review.

ContentLocator: `independent agent-usability review`

Owner: MCP lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: SDK parity exit usability 01 error-redaction, idempotency, safe MCP discovery, forbidden-tool, provenance, and usability receipt; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Agent usability is not independently assessed.

N/A: gap

Work: `FW-MCP-05`

### REQ-P6-ROADMAP-OBS-HA-STACK-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-OBS-HA-STACK-01`
RequirementText: Build the HA metrics, logs, traces, and alerting stack.
ContentLocator: `HA metrics/logs/traces/alerting stack`
Owner: Observability lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE obs ha stack 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-OBS-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: HA observability is incomplete.
N/A: gap
Work: `FW-OBS-06`

### REQ-P6-ROADMAP-OBS-SAFETY-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-OBS-SAFETY-01`
RequirementText: Build bounded-cardinality labels, tenant-safe support queries, and encrypted regional buffering.
ContentLocator: `bounded-cardinality labels, tenant-safe support queries, encrypted regional buffering`
Owner: Observability lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE obs safety 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-OBS-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Observability leaks tenant data or grows without bound.
N/A: gap
Work: `FW-OBS-06`

### REQ-P6-ROADMAP-OBS-ALERTS-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-OBS-ALERTS-01`
RequirementText: Build dashboards, SLI/SLO/error-budget alerts, and tested incident escalation.
ContentLocator: `dashboards, SLI/SLO/error-budget alerts, and tested incident escalation`
Owner: Observability lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE obs alerts 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-OBS-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Alerts or escalation are untested.
N/A: gap
Work: `FW-OBS-06`

### REQ-P6-ROADMAP-DELIVERY-GITOPS-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-DELIVERY-GITOPS-01`
RequirementText: Complete native GitOps deployment apply, drift, prune, health, and rollback.
ContentLocator: `native GitOps deployment apply/drift/prune/health/rollback`
Owner: Release engineering lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE delivery gitops 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-DELIVERY-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Deployment reconciliation or rollback is unsafe.
N/A: gap
Work: `FW-DELIVERY-06`

### REQ-P6-ROADMAP-DELIVERY-PROVENANCE-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-DELIVERY-PROVENANCE-01`
RequirementText: Complete trusted artifact chain with SBOM, provenance, and signing.
ContentLocator: `trusted artifact chain with SBOM/provenance/signing`
Owner: Release engineering lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE delivery provenance 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-DELIVERY-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Artifacts lack trusted provenance.
N/A: gap
Work: `FW-DELIVERY-06`

### REQ-P6-ROADMAP-DELIVERY-CREDENTIALS-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-DELIVERY-CREDENTIALS-01`
RequirementText: Complete evidence-gated credentials.
ContentLocator: `evidence-gated credentials`
Owner: Release engineering lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE delivery credentials 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-DELIVERY-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Credentials are used without evidence gates.
N/A: gap
Work: `FW-DELIVERY-06`

### REQ-P6-ROADMAP-DELIVERY-ROLLOUT-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-DELIVERY-ROLLOUT-01`
RequirementText: Complete staged SFO to FRA to GRU live rollout and rollback.
ContentLocator: `staged SFO → FRA → GRU live rollout/rollback`
Owner: Release engineering lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE delivery rollout 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-DELIVERY-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Regional rollout lacks safe rollback.
N/A: gap
Work: `FW-DELIVERY-06`

### REQ-P6-ROADMAP-DELIVERY-GREENFIELD-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-DELIVERY-GREENFIELD-01`
RequirementText: Complete clean-room nine-seed greenfield rehearsal.
ContentLocator: `clean-room nine-seed greenfield rehearsal`
Owner: Release engineering lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE delivery greenfield 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-DELIVERY-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Greenfield delivery cannot be reproduced.
N/A: gap
Work: `FW-DELIVERY-06`

### REQ-P6-ROADMAP-DOCS-AUDIENCES-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-DOCS-AUDIENCES-01`
RequirementText: Publish customer, admin, and operator documentation.
ContentLocator: `complete customer/admin/operator documentation set`
Owner: Documentation lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE docs audiences 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-DOCS-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Required documentation audiences are omitted.
N/A: gap
Work: `FW-DOCS-06`

### REQ-P6-ROADMAP-DOCS-PRODUCT-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-DOCS-PRODUCT-01`
RequirementText: Publish onboarding, public API/SDK/MCP, service limits/regions, and database lifecycle documentation.
ContentLocator: `onboarding; public API/SDK/MCP; service limits/regions; database lifecycle`
Owner: Documentation lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE docs product 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-DOCS-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Product documentation is incomplete.
N/A: gap
Work: `FW-DOCS-06`

### REQ-P6-ROADMAP-DOCS-RECOVERY-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-DOCS-RECOVERY-01`
RequirementText: Publish backup, PITR, restore, and DR documentation.
ContentLocator: `backup/PITR/restore/DR`
Owner: Documentation lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE docs recovery 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-DOCS-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Recovery documentation is incomplete.
N/A: gap
Work: `FW-DOCS-06`

### REQ-P6-ROADMAP-DOCS-SECURITY-BILLING-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-DOCS-SECURITY-BILLING-01`
RequirementText: Publish security, privacy, billing, usage, failures, and reconciliation documentation.
ContentLocator: `security/shared responsibility/privacy/retention; billing/usage/failures/reconciliation`
Owner: Documentation lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE docs security billing 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-DOCS-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Security or billing guidance is incomplete.
N/A: gap
Work: `FW-DOCS-06`

### REQ-P6-ROADMAP-DOCS-OPERATIONS-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-DOCS-OPERATIONS-01`
RequirementText: Publish support, status, incident, SLO, capacity, deployment, rollback, contributor, and release guides.
ContentLocator: `support/status/incident process; SLO/capacity; deployment/rollback; contributor/release guides`
Owner: Documentation lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE docs operations 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-DOCS-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Operational guidance is incomplete.
N/A: gap
Work: `FW-DOCS-06`

### REQ-P6-ROADMAP-QUALITY-GATES-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-QUALITY-GATES-01`
RequirementText: Enforce source-contract drift, claim registry, localization parity, runnable examples, accessibility, link/style/spell, freshness, and update proof.
ContentLocator: `source-contract drift, claim registry validation, EN/ES/PT-BR parity, runnable examples, accessibility, link/style/spell checks, freshness review, and release-note/update proof`
Owner: Documentation lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE quality gates 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-DOCS-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Documentation quality gates are incomplete.
N/A: gap
Work: `FW-DOCS-06`

### REQ-P6-ROADMAP-QUALITY-PROMOTION-CI-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-QUALITY-PROMOTION-CI-01`
RequirementText: Require promotion CI to rerun all relevant checks.
ContentLocator: `Promotion CI must rerun all relevant checks`
Owner: Release engineering lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE quality promotion ci 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-DELIVERY-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Promotion bypasses required checks.
N/A: gap
Work: `FW-DELIVERY-06`

### REQ-P6-ROADMAP-ADMISSION-RINGS-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-ADMISSION-RINGS-01`
RequirementText: Run internal dogfood, design-partner validation, invited early access, and self-service production availability.
ContentLocator: `internal dogfood, design-partner validation, invited early access, and self-service production availability`
Owner: Product admission lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE admission rings 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-OPS-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Customer admission rings are not evidence-gated.
N/A: gap
Work: `FW-OPS-06`

### REQ-P6-ROADMAP-ADMISSION-CONTROLS-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-ADMISSION-CONTROLS-01`
RequirementText: Require support capacity, limits, abuse controls, billing entitlement, status, rollback criteria, and supported-capability statement per ring.
ContentLocator: `Each ring has explicit support/on-call capacity, service limits, rate/abuse controls, billing entitlement, status communication, rollback/exit criteria, and a published statement of supported capability`
Owner: Product admission lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE admission controls 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-OPS-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Admission rings lack operational controls.
N/A: gap
Work: `FW-OPS-06`

### REQ-P6-ROADMAP-ADMISSION-NO-BYPASS-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-ADMISSION-NO-BYPASS-01`
RequirementText: Forbid manual customer or agent bypass.
ContentLocator: `no manual customer or agent bypass may substitute for these controls`
Owner: Product admission lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE admission no bypass 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-OPS-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Manual bypass weakens admission controls.
N/A: gap
Work: `FW-OPS-06`

### REQ-P6-ROADMAP-EXIT-SOAK-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-EXIT-SOAK-01`
RequirementText: Produce seven-day production-like soak evidence with database load, recovery, cost, billing, security, and outage tests.
ContentLocator: `seven-day production-like soak with database load, backup/recovery, cost, billing, security, and outage tests`
Owner: SRE lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE exit soak 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-OPS-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Production readiness lacks soak evidence.
N/A: gap
Work: `FW-OPS-06`

### REQ-P6-ROADMAP-EXIT-DEFAULT-DENY-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-EXIT-DEFAULT-DENY-01`
RequirementText: Keep public ingress default-deny until signed readiness approval.
ContentLocator: `public ingress remains default-deny until signed readiness approval`
Owner: SRE lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE exit default deny 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-OPS-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Public ingress opens before readiness approval.
N/A: gap
Work: `FW-OPS-06`

### REQ-P6-ROADMAP-EXIT-CLAIMS-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`
RequirementID: `REQ-P6-ROADMAP-EXIT-CLAIMS-01`
RequirementText: Match customer and public claims to the capability registry exactly.
ContentLocator: `customer/public claims match the capability registry exactly`
Owner: Documentation claims lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: HA SRE exit claims 01 native GitOps provenance, staged rollout, greenfield documentation, admission, seven-day soak, default-deny, signed readiness, and claim-registry receipt; Work contract: `FW-CLAIM-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Public claims exceed supported capability.
N/A: gap
Work: `FW-CLAIM-06`


### REQ-CROSS-GATE-MAINTENANCE-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Delivery Gates`
RequirementID: `REQ-CROSS-GATE-MAINTENANCE-01`
RequirementText: Maintain and satisfy delivery gates before declaring completion.
ContentLocator: `orchestrator must maintain and satisfy these gates before declaring completion`
Owner: Delivery governance lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross gate maintenance 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-QUALITY-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `FW-QUALITY-06`

### REQ-CROSS-GATE-DISCOVERY-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Delivery Gates`
RequirementID: `REQ-CROSS-GATE-DISCOVERY-01`
RequirementText: Review discovery architecture, gaps, ownership, dependencies, threat model, and plan.
ContentLocator: `current architecture map, gap matrix against this goal, ownership map, dependency graph, threat model, and prioritized delivery plan are reviewed`
Owner: Delivery governance lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross gate discovery 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `P0-12`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `P0-12`

### REQ-CROSS-GATE-CONTRACT-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Delivery Gates`
RequirementID: `REQ-CROSS-GATE-CONTRACT-01`
RequirementText: Document, version, validate, and protect public contracts.
ContentLocator: `public API, SDK, MCP, auth, tenancy, billing, and observability contracts are documented, versioned, validated, and free of Dashboard/internal-transport leakage`
Owner: Platform API lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross gate contract 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-CONTRACT-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `FW-CONTRACT-01`

### REQ-CROSS-GATE-FEATURE-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Delivery Gates`
RequirementID: `REQ-CROSS-GATE-FEATURE-01`
RequirementText: Provide traceable acceptance coverage or accepted non-applicability.
ContentLocator: `complete coverage or an explicitly justified, accepted non-applicability`
Owner: Delivery governance lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross gate feature 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `P0-12`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `P0-12`

### REQ-CROSS-GATE-QUALITY-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Delivery Gates`
RequirementID: `REQ-CROSS-GATE-QUALITY-01`
RequirementText: Pass compilation through applicable documentation checks.
ContentLocator: `compilation, lint/format checks, unit/protocol tests, real integration/end-to-end tests, compatibility tests, accessibility checks, load/soak/failure tests where applicable, and documentation checks pass`
Owner: Release-quality lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross gate quality 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-QUALITY-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `FW-QUALITY-06`

### REQ-CROSS-GATE-SECURITY-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Delivery Gates`
RequirementID: `REQ-CROSS-GATE-SECURITY-01`
RequirementText: Pass security gate controls.
ContentLocator: `authentication/authorization/tenant-isolation tests, secret scans, dependency/supply-chain checks, threat-model actions, webhook verification, audit coverage, and destructive-action safeguards pass`
Owner: Security lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross gate security 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-SEC-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `FW-SEC-06`

### REQ-CROSS-GATE-OPERATIONS-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Delivery Gates`
RequirementID: `REQ-CROSS-GATE-OPERATIONS-01`
RequirementText: Complete operations gate evidence.
ContentLocator: `deployment/rollback, monitoring/alerting, SLOs, backups, restore/PITR drill, incident/runbook, capacity, and disaster-recovery evidence are complete`
Owner: SRE lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross gate operations 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-OPS-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `FW-OPS-06`

### REQ-CROSS-GATE-RELEASE-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Delivery Gates`
RequirementID: `REQ-CROSS-GATE-RELEASE-01`
RequirementText: Build, test, review, and promote an immutable multi-repository release candidate manifest.
ContentLocator: `signed immutable multi-repository release manifest identifies the exact commit SHA, artifact digest, OpenAPI/SDK/MCP contract version, configuration-schema version, and evidence links for every affected repository`
Owner: Release engineering lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross gate release 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-DELIVERY-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `FW-DELIVERY-06`

### REQ-CROSS-CONSTRAINT-DECISIONS-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Non-Negotiable Constraints`
RequirementID: `REQ-CROSS-CONSTRAINT-DECISIONS-01`
RequirementText: Make proactive evidence-based decisions and escalate material changes only.
ContentLocator: `Make proactive, evidence-based decisions within this goal`
Owner: Delivery governance lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross constraint decisions 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `P0-12`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `P0-12`

### REQ-CROSS-CONSTRAINT-PLATFORM-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Non-Negotiable Constraints`
RequirementID: `REQ-CROSS-CONSTRAINT-PLATFORM-01`
RequirementText: Prefer existing capabilities and C# defaults while retaining mandated runtimes.
ContentLocator: `Prefer existing TerraScale capabilities and standard platform facilities`
Owner: Architecture lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross constraint platform 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-ADR-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `FW-ADR-06`

### REQ-CROSS-CONSTRAINT-CSHARP-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Non-Negotiable Constraints`
RequirementID: `REQ-CROSS-CONSTRAINT-CSHARP-01`
RequirementText: Use mandated C# serialization, nullable, logging, and telemetry defaults.
ContentLocator: `Use `System.Text.Json`, nullable reference types, warnings-as-errors`
Owner: Platform architecture lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross constraint csharp 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-CONTRACT-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `FW-CONTRACT-01`

### REQ-CROSS-CONSTRAINT-PUBLIC-PARITY-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Non-Negotiable Constraints`
RequirementID: `REQ-CROSS-CONSTRAINT-PUBLIC-PARITY-01`
RequirementText: Keep public contracts and AI parity secure without Dashboard bypass.
ContentLocator: `Dashboard is an ordinary SDK customer, never a privileged bypass`
Owner: Platform security lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross constraint public parity 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-DASH-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `FW-DASH-06`

### REQ-CROSS-CONSTRAINT-SENSITIVE-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Non-Negotiable Constraints`
RequirementID: `REQ-CROSS-CONSTRAINT-SENSITIVE-01`
RequirementText: Treat sensitive operations as confirmation, audit, and idempotency-sensitive.
ContentLocator: `confirmation-, audit-, and idempotency-sensitive workflows`
Owner: Security lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross constraint sensitive 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-SEC-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `FW-SEC-06`

### REQ-CROSS-CONSTRAINT-NO-WEAKENING-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Non-Negotiable Constraints`
RequirementID: `REQ-CROSS-CONSTRAINT-NO-WEAKENING-01`
RequirementText: Do not weaken tests, security boundaries, or production controls.
ContentLocator: `A green test suite without the real required behavior does not meet this goal`
Owner: Release-quality lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross constraint no weakening 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-QUALITY-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `FW-QUALITY-06`

### REQ-CROSS-TRACE-NORMATIVE-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Requirement Traceability`
RequirementID: `REQ-CROSS-TRACE-NORMATIVE-01`
RequirementText: Convert every normative story, rule, and exception into traceable testable acceptance.
ContentLocator: `convert every story, business rule, and exception into a traceable backlog item and testable acceptance criterion`
Owner: Delivery governance lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross trace normative 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `P0-12`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `P0-12`

### REQ-CROSS-TRACE-MATRIX-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Requirement Traceability`
RequirementID: `REQ-CROSS-TRACE-MATRIX-01`
RequirementText: Maintain reviewable traceability and capability matrices with no unexplained gap.
ContentLocator: `matrix and the Dashboard-to-public-API/SDK-to-MCP capability matrix are current, independently reviewed, and show no unexplained gap`
Owner: Delivery governance lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross trace matrix 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `P0-12`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `P0-12`

### REQ-CROSS-EVIDENCE-NO-MOCK-CLOSURE-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ### Evidence Quality Rules`
RequirementID: `REQ-CROSS-EVIDENCE-NO-MOCK-CLOSURE-01`
RequirementText: Do not close real-boundary requirements with mocked unit tests alone.
ContentLocator: `cannot close a customer, data-plane, payment-provider, deployment, recovery, or tenant-isolation requirement by itself`
Owner: Evidence-quality lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross evidence no mock closure 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-QUALITY-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `FW-QUALITY-06`

### REQ-CROSS-EVIDENCE-NO-SUBSTITUTE-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ### Evidence Quality Rules`
RequirementID: `REQ-CROSS-EVIDENCE-NO-SUBSTITUTE-01`
RequirementText: Do not substitute plans or static checks for live boundary results.
ContentLocator: `cannot substitute for a live integration/end-to-end result at the required boundary`
Owner: Evidence-quality lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross evidence no substitute 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-QUALITY-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `FW-QUALITY-06`

### REQ-CROSS-EVIDENCE-CLAIM-METADATA-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ### Evidence Quality Rules`
RequirementID: `REQ-CROSS-EVIDENCE-CLAIM-METADATA-01`
RequirementText: Require complete dated production-claim evidence metadata.
ContentLocator: `dated evidence link, expiry/revalidation interval, accountable owner, environment, input version/digest, result, and residual-risk statement`
Owner: Evidence-quality lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross evidence claim metadata 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-CLAIM-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `FW-CLAIM-06`

### REQ-CROSS-EVIDENCE-FAILURE-RECOVERY-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ### Evidence Quality Rules`
RequirementID: `REQ-CROSS-EVIDENCE-FAILURE-RECOVERY-01`
RequirementText: Include failure path and recovery outcome in sensitive evidence.
ContentLocator: `tested failure path and recovery outcome`
Owner: Evidence-quality lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross evidence failure recovery 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-QUALITY-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `FW-QUALITY-06`

### REQ-CROSS-EVIDENCE-NONAPPLICABLE-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ### Evidence Quality Rules`
RequirementID: `REQ-CROSS-EVIDENCE-NONAPPLICABLE-01`
RequirementText: Require justified, approved safe alternative for non-applicable requirements.
ContentLocator: `may not conceal an unfinished capability`
Owner: Evidence-quality lead
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: gap
AT: Planned artifact: cross evidence nonapplicable 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-QUALITY-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unresolved cross-cutting control.
N/A: gap
Work: `FW-QUALITY-06`


### REQ-SCENARIO-ACCOUNT-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Requirement Traceability > ### Required Acceptance Scenario Packs`
RequirementID: `REQ-SCENARIO-ACCOUNT-01`
RequirementText: Governing Account and security scope: Login, confirmation/resend, OAuth linking, password recovery non-enumeration, MFA enrollment/challenge/recovery/disable, passkeys where supported, profile change verification, password/session revocation, onboarding routing, and last-valid-organization restoration.
ContentLocator: `| Account and security | Login, confirmation/resend, OAuth linking, password recovery non-enumeration, MFA enrollment/challenge/recovery/disable, passkeys where supported, profile change verification, password/session revocation, onboarding routing, and last-valid-organization restoration. |`
Owner: Scenario-pack owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Scope-specific authorization and tenant isolation.
AT: Planned artifact: scenario account 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Scenario scope remains unproven.
N/A: gap
Work: `FW-ID-01`

### REQ-SCENARIO-ORGANIZATION-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Requirement Traceability > ### Required Acceptance Scenario Packs`
RequirementID: `REQ-SCENARIO-ORGANIZATION-01`
RequirementText: Governing Organization and membership scope: Organization creation/selection/management/deletion safeguards; invitation state/resend/cancel/accept/decline/expiry; owner/member role management; last-owner prevention; removal/leave and immediate project-access revocation.
ContentLocator: `| Organization and membership | Organization creation/selection/management/deletion safeguards; invitation state/resend/cancel/accept/decline/expiry; owner/member role management; last-owner prevention; removal/leave and immediate project-access revocation. |`
Owner: Scenario-pack owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Scope-specific authorization and tenant isolation.
AT: Planned artifact: scenario organization 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-AUTH-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Scenario scope remains unproven.
N/A: gap
Work: `FW-AUTH-01`

### REQ-SCENARIO-ONBOARDING-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Requirement Traceability > ### Required Acceptance Scenario Packs`
RequirementID: `REQ-SCENARIO-ONBOARDING-01`
RequirementText: Governing Onboarding and first value scope: Resumable account completion, provider-hosted payment method/validation, optional MFA, first organization, first project with primary and single backup region, active context, and dashboard landing.
ContentLocator: `| Onboarding and first value | Resumable account completion, provider-hosted payment method/validation, optional MFA, first organization, first project with primary and single backup region, active context, and dashboard landing. |`
Owner: Scenario-pack owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Scope-specific authorization and tenant isolation.
AT: Planned artifact: scenario onboarding 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-ID-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Scenario scope remains unproven.
N/A: gap
Work: `FW-ID-01`

### REQ-SCENARIO-PROJECTS-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Requirement Traceability > ### Required Acceptance Scenario Packs`
RequirementID: `REQ-SCENARIO-PROJECTS-01`
RequirementText: Governing Projects, products, and access scope: Project uniqueness/regions/backup/management/deletion; database provisioning and lifecycle; queue creation/type/use; Authentication enablement; project members/owners; organization/project role inheritance and isolation.
ContentLocator: `| Projects, products, and access | Project uniqueness/regions/backup/management/deletion; database provisioning and lifecycle; queue creation/type/use; Authentication enablement; project members/owners; organization/project role inheritance and isolation. |`
Owner: Scenario-pack owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Scope-specific authorization and tenant isolation.
AT: Planned artifact: scenario projects 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-DB-02`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Scenario scope remains unproven.
N/A: gap
Work: `FW-DB-02`

### REQ-SCENARIO-RESILIENCE-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Requirement Traceability > ### Required Acceptance Scenario Packs`
RequirementID: `REQ-SCENARIO-RESILIENCE-01`
RequirementText: Governing Database resilience scope: Credentials/endpoints/rotation, backup policy, restore points, PITR where supported, restore-to-new instance, validation/cutover/rollback, branch/clone semantics, failure/retry, retention/deletion, incident audit, measured RPO/RTO, and customer/operator recovery paths.
ContentLocator: `| Database resilience | Credentials/endpoints/rotation, backup policy, restore points, PITR where supported, restore-to-new instance, validation/cutover/rollback, branch/clone semantics, failure/retry, retention/deletion, incident audit, measured RPO/RTO, and customer/operator recovery paths. |`
Owner: Scenario-pack owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Scope-specific authorization and tenant isolation.
AT: Planned artifact: scenario resilience 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Scenario scope remains unproven.
N/A: gap
Work: `FW-DB-RESILIENCE-03`

### REQ-SCENARIO-MONITORING-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Requirement Traceability > ### Required Acceptance Scenario Packs`
RequirementID: `REQ-SCENARIO-MONITORING-01`
RequirementText: Governing Monitoring and alerts scope: Project overview, region state/backup indicator, latency and user-location fallback, usage/history periods/retention, partial metric-source degradation, alert severity/dismissal, and tenant-safe dashboard/stream updates.
ContentLocator: `| Monitoring and alerts | Project overview, region state/backup indicator, latency and user-location fallback, usage/history periods/retention, partial metric-source degradation, alert severity/dismissal, and tenant-safe dashboard/stream updates. |`
Owner: Scenario-pack owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Scope-specific authorization and tenant isolation.
AT: Planned artifact: scenario monitoring 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-OBS-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Scenario scope remains unproven.
N/A: gap
Work: `FW-OBS-06`

### REQ-SCENARIO-BILLING-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Requirement Traceability > ### Required Acceptance Scenario Packs`
RequirementID: `REQ-SCENARIO-BILLING-01`
RequirementText: Governing Billing and usage scope: Subscription/trial/restricted access, plan transition semantics, payment-method rules, history/receipts, organization/project usage and limits/overage, Polar Sandbox event matrix, mandatory notices, preference boundaries, reconciliation, and financial-role denial.
ContentLocator: `| Billing and usage | Subscription/trial/restricted access, plan transition semantics, payment-method rules, history/receipts, organization/project usage and limits/overage, Polar Sandbox event matrix, mandatory notices, preference boundaries, reconciliation, and financial-role denial. |`
Owner: Scenario-pack owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Scope-specific authorization and tenant isolation.
AT: Planned artifact: scenario billing 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-BILL-04`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Scenario scope remains unproven.
N/A: gap
Work: `FW-BILL-04`

### REQ-SCENARIO-ADMIN-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Requirement Traceability > ### Required Acceptance Scenario Packs`
RequirementID: `REQ-SCENARIO-ADMIN-01`
RequirementText: Governing Administration and compliance scope: TerraScale Admin isolation from customer membership, OIDC/RBAC/break-glass/audit, support diagnostics, data retention/export/delete behavior, secret handling, security event response, and legal/claim approval boundaries.
ContentLocator: `| Administration and compliance | TerraScale Admin isolation from customer membership, OIDC/RBAC/break-glass/audit, support diagnostics, data retention/export/delete behavior, secret handling, security event response, and legal/claim approval boundaries. |`
Owner: Scenario-pack owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Scope-specific authorization and tenant isolation.
AT: Planned artifact: scenario admin 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-ADMIN-04`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Scenario scope remains unproven.
N/A: gap
Work: `FW-ADMIN-04`

### REQ-SCENARIO-AGENT-01
SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Requirement Traceability > ### Required Acceptance Scenario Packs`
RequirementID: `REQ-SCENARIO-AGENT-01`
RequirementText: Governing AI-agent and SDK parity scope: Every approved human outcome mapped to public API, TypeScript, .NET, and MCP or to a reviewed safe public alternative; typed-only transport, bounded outputs, redaction, confirmation, idempotency, pagination, version compatibility, and real cross-tenant denial proof.
ContentLocator: `| AI-agent and SDK parity | Every approved human outcome mapped to public API, TypeScript, .NET, and MCP or to a reviewed safe public alternative; typed-only transport, bounded outputs, redaction, confirmation, idempotency, pagination, version compatibility, and real cross-tenant denial proof. |`
Owner: Scenario-pack owner
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Scope-specific authorization and tenant isolation.
AT: Planned artifact: scenario agent 01 specific gate-review, coverage-audit, real-boundary negative-proof, scenario receipt, and claim-review artifact; Work contract: `FW-MCP-05`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Scenario scope remains unproven.
N/A: gap
Work: `FW-MCP-05`


## Phase exit-evidence records

### REQ-P1-EXIT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-EXIT-01`

RequirementText: Produce real two-user, two-organization AppHost integration coverage for success, 401/403, race/idempotency, session invalidation, and authority invariants, plus API/SDK drift, Dashboard typed-SDK structural, and accessible browser-flow gates.

ContentLocator: `Exit evidence: real two-user/two-organization AppHost integration matrix covering success, 401/403, race/idempotency, session invalidation, and all authority invariants; API/SDK drift gate; Dashboard typed-SDK structural gate; accessible Dashboard browser flows.`

Owner: Platform identity and authorization leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Two-user, two-organization authorization and tenant denial.

AT: Planned artifact: Phase 1 two-user, two-organization AppHost exit-evidence matrix and API/SDK, typed-SDK, and accessible-browser gate receipt in `FW-ID-01`; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Authorization or tenancy regression accepted without a real AppHost boundary.

N/A: gap

Work: `FW-ID-01`

### REQ-P1-EXIT-SUCCESS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-EXIT-SUCCESS-01`

RequirementText: Produce real AppHost integration evidence of successful two-user, two-organization behavior.

ContentLocator: `real two-user/two-organization AppHost integration matrix covering success`

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Two distinct users and organizations execute only their authorized successful flows.

AT: Planned artifact: Phase 1 identity and organization success 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A single-user or single-organization test masks tenant-boundary defects.

N/A: gap

Work: `FW-AUTH-01`

### REQ-P1-EXIT-DENIAL-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-EXIT-DENIAL-01`

RequirementText: Produce real AppHost integration evidence of 401 and 403 denials.

ContentLocator: `401/403`

Owner: Platform authorization lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Unauthenticated and unauthorized callers are denied without crossing organization boundaries.

AT: Planned artifact: Phase 1 identity and organization denial 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Authentication or authorization failures expose protected tenant data.

N/A: gap

Work: `FW-AUTH-01`

### REQ-P1-EXIT-RACE-IDEMPOTENCY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-EXIT-RACE-IDEMPOTENCY-01`

RequirementText: Produce real AppHost integration evidence for race and idempotency behavior.

ContentLocator: `race/idempotency`

Owner: Platform identity lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Retried or concurrent authorized requests preserve identity and tenant scope.

AT: Planned artifact: Phase 1 identity and organization race idempotency 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Concurrent or retried requests create duplicate or unauthorized state changes.

N/A: gap

Work: `FW-ID-01`

### REQ-P1-EXIT-SESSION-AUTHORITY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-EXIT-SESSION-AUTHORITY-01`

RequirementText: Produce real AppHost integration evidence for session invalidation and all authority invariants.

ContentLocator: `session invalidation, and all authority invariants`

Owner: Platform identity and authorization leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Invalidated sessions and every authority invariant deny access immediately when required.

AT: Planned artifact: Phase 1 identity and organization session authority 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-ID-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Revoked sessions or changed authority remain effective.

N/A: gap

Work: `FW-ID-01`

### REQ-P1-EXIT-OPENAPI-DRIFT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-EXIT-OPENAPI-DRIFT-01`

RequirementText: Produce an OpenAPI and SDK drift gate.

ContentLocator: `API/SDK drift gate`

Owner: Platform API lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public contract authorization classifications remain aligned with the published inventory.

AT: Planned artifact: Phase 1 identity and organization openapi drift 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Published API contracts and SDK behavior diverge.

N/A: gap

Work: `FW-CONTRACT-01`

### REQ-P1-EXIT-TYPED-SDK-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-EXIT-TYPED-SDK-01`

RequirementText: Produce a Dashboard typed-SDK structural gate.

ContentLocator: `Dashboard typed-SDK structural gate`

Owner: Dashboard boundary lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Dashboard uses the same typed public customer contract and authorization boundary as external customers.

AT: Planned artifact: Phase 1 identity and organization typed sdk 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Dashboard code bypasses typed public contracts or customer authorization.

N/A: gap

Work: `FW-DASH-06`

### REQ-P1-EXIT-A11Y-BROWSER-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=1; title=Public contracts, identity, and tenant foundations]`

RequirementID: `REQ-P1-EXIT-A11Y-BROWSER-01`

RequirementText: Produce accessible Dashboard browser-flow gates.

ContentLocator: `accessible Dashboard browser flows`

Owner: Dashboard accessibility lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Accessible customer browser flows preserve ordinary public authorization and tenant isolation.

AT: Planned artifact: Phase 1 identity and organization a11y browser 01 real AppHost two-user/two-org success, denial, retry, session, accessibility, and drift receipt; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: A required Dashboard flow is inaccessible or loses authorization context.

N/A: gap

Work: `FW-DASH-06`

### REQ-P2-EXIT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=2; title=Managed database, project products, and customer operations]`

RequirementID: `REQ-P2-EXIT-01`

RequirementText: Produce public E2E evidence for create, use, rotate, backup, restore, delete, queue publish/consume/dead-letter, Authentication enable/disable impact, customer-safe audit history, and no leaked endpoint, credential, or tenant data.

ContentLocator: `Exit evidence: public E2E scenario pack for create/use/rotate/backup/restore/delete, queue publish/consume/dead-letter, Authentication enable/disable impact, customer-safe audit history, and no leaked endpoint/credential/tenant data.`

Owner: Platform database and Orchestrator lifecycle leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Owner, member, and project isolation.

AT: Planned artifact: Phase 2 public lifecycle and queue E2E scenario-pack receipt with Authentication impact and redaction review in `FW-DB-02`; Work contract: `FW-DB-02`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Data, credential, or tenant disclosure during lifecycle operations.

N/A: gap

Work: `FW-DB-02`

### REQ-P3-EXIT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=3; title=Real regional runtime, high availability, and recovery]`

RequirementID: `REQ-P3-EXIT-01`

RequirementText: Produce R3/L3/L4 production-boundary tests, destructive recovery proof, measured RPO/RTO within approved SLOs, a signed survival bundle, and no reliance on local RF=1, development PKI, or lab assumptions.

ContentLocator: `Exit evidence: R3/L3/L4 production-boundary tests, destructive recovery proof, measured RPO/RTO within approved SLOs, signed survival bundle, and no reliance on local RF=1/dev PKI/lab assumptions.`

Owner: Orchestrator recovery lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Operator recovery authority and audit.

AT: Planned artifact: Phase 3 R3/L3/L4 recovery, measured RPO/RTO, and signed-survival-bundle exit receipt in `FW-REC-03`; Work contract: `FW-REC-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unsupported durability or recovery claim.

N/A: gap

Work: `FW-REC-03`

### REQ-P4-EXIT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=4; title=Billing, usage, notifications, and governed administration]`

RequirementID: `REQ-P4-EXIT-01`

RequirementText: Produce a sandbox report with reconciled provider events, owner/non-owner/cross-organization E2E proof, no sensitive payment data in TerraScale, enforced entitlements, mandatory billing/security communications, and an operations runbook.

ContentLocator: `Exit evidence: sandbox report and reconciled provider events, owner/non-owner/cross-org E2E proof, no sensitive payment data in TerraScale, enforced entitlements, mandatory billing/security communications, and operations runbook.`

Owner: Billing and administration leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Organization-owner, financial-role, and operator authorization.

AT: Planned artifact: Phase 4 sandbox reconciliation, entitlement, communication, and billing-operations exit receipt in `FW-BILL-04`; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Financial loss, data exposure, or ungoverned administration.

N/A: gap

Work: `FW-BILL-04`

### REQ-P5-EXIT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=5; title=Full AI-agent parity and developer experience]`

RequirementID: `REQ-P5-EXIT-01`

RequirementText: Maintain a current Dashboard-to-public-API/SDK-to-MCP capability matrix, a complete public-contract parity report, real success/failure/cross-tenant tests per operation or tool, signed MCP artifacts/provenance, and independent agent-usability review.

ContentLocator: `Exit evidence: current Dashboard-to-public-API/SDK-to-MCP capability matrix, complete public contract parity report, real success/failure/cross-tenant tests per operation/tool, signed MCP artifacts/provenance, and independent agent-usability review.`

Owner: MCP product lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Customer tenant authorization and destructive-action confirmation.

AT: Planned artifact: Phase 5 Dashboard-to-public-contract-to-MCP parity matrix, provenance, and agent-usability exit receipt in `FW-MCP-05`; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Agent-only privilege or unsafe tool behavior.

N/A: gap

Work: `FW-MCP-05`

### REQ-P6-EXIT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=6; title=Operability, release, documentation, and launch proof]`

RequirementID: `REQ-P6-EXIT-01`

RequirementText: Produce a seven-day production-like soak spanning database load, backup/recovery, cost, billing, security, and outage tests; retain default-deny public ingress until signed readiness approval; and match customer/public claims exactly to the capability registry.

ContentLocator: `Exit evidence: seven-day production-like soak with database load, backup/recovery, cost, billing, security, and outage tests; public ingress remains default-deny until signed readiness approval; customer/public claims match the capability registry exactly.`

Owner: Release, SRE, and documentation claims leads

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Signed readiness authority; ingress remains default-deny.

AT: Planned artifact: Phase 6 seven-day production-like soak, default-deny readiness, and capability-registry claim-alignment exit receipt in `FW-OBS-06`; Work contract: `FW-OBS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Launch with unproven reliability or inaccurate claims.

N/A: gap

Work: `FW-OBS-06`

## Scope 7 atomic governing records

These records replace the missing broad Scope 7 navigation entry. Each ContentLocator is literal text from Scope 7, while the shared SourceAnchor uses only its real GOAL heading chain. This section is a planning baseline: every Evidence and Claim remains a gap, and it does not assert P0-07 acceptance.

### REQ-S7-SEC-THREAT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-SEC-THREAT-01`

RequirementText: Maintain a threat model for the production service and use it to drive mitigations and review.

ContentLocator: `Threat modeling`

Owner: Security engineering lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-SEC-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-SEC-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-SEC-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-SEC-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-SEC-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-SEC-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: signed security-control threat 01 evidence receipt; Work contract: `FW-SEC-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Undiscovered abuse or trust-boundary risk.

N/A: gap

Work: `FW-SEC-06`

### REQ-S7-SEC-SDLC-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-SEC-SDLC-01`

RequirementText: Operate a secure SDLC with SAST and DAST controls appropriate to the production service.

ContentLocator: `secure SDLC`

Owner: Security engineering lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-SEC-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-SEC-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-SEC-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-SEC-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-SEC-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-SEC-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: signed security-control sdlc 01 evidence receipt; Work contract: `FW-SEC-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Vulnerabilities reach release undetected.

N/A: gap

Work: `FW-SEC-06`

### REQ-S7-SEC-SUPPLY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-SEC-SUPPLY-01`

RequirementText: Scan dependencies and container images as supply-chain controls before release.

ContentLocator: `dependency and supply-chain controls`

Owner: Security engineering lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-SEC-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-SEC-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-SEC-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-SEC-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-SEC-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-SEC-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: signed security-control supply 01 evidence receipt; Work contract: `FW-SEC-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Known vulnerable dependency or image is released.

N/A: gap

Work: `FW-SEC-06`

### REQ-S7-SEC-SECRETS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-SEC-SECRETS-01`

RequirementText: Manage secrets through approved, auditable secret-management controls.

ContentLocator: `secrets management`

Owner: Security engineering lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-SEC-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-SEC-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-SEC-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-SEC-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-SEC-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-SEC-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: signed security-control secrets 01 evidence receipt; Work contract: `FW-SEC-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Secret exposure or unauthorized secret use.

N/A: gap

Work: `FW-SEC-06`

### REQ-S7-SEC-VULN-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-SEC-VULN-01`

RequirementText: Perform vulnerability review, risk-based patching, and tracked vulnerability response.

ContentLocator: `vulnerability response`

Owner: Security engineering lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-SEC-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-SEC-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-SEC-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-SEC-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-SEC-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-SEC-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: signed security-control vuln 01 evidence receipt; Work contract: `FW-SEC-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Known vulnerability remains exploitable.

N/A: gap

Work: `FW-SEC-06`

### REQ-S7-SEC-AUDIT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-SEC-AUDIT-01`

RequirementText: Produce audit logging for security-relevant actions and retain reviewable evidence.

ContentLocator: `audit logging`

Owner: Security engineering lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-SEC-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-SEC-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-SEC-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-SEC-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-SEC-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-SEC-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: signed security-control audit 01 evidence receipt; Work contract: `FW-SEC-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Security events cannot be investigated.

N/A: gap

Work: `FW-SEC-06`

### REQ-S7-SEC-PRIVACY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-SEC-PRIVACY-01`

RequirementText: Define and apply privacy and retention policies to production data and operational evidence.

ContentLocator: `privacy/retention policies`

Owner: Privacy and security lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-SEC-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-SEC-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-SEC-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-SEC-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-SEC-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-SEC-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: signed security-control privacy 01 evidence receipt; Work contract: `FW-SEC-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Privacy breach or unlawful retention.

N/A: gap

Work: `FW-SEC-06`

### REQ-S7-SEC-ACCESS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-SEC-ACCESS-01`

RequirementText: Perform regular access reviews and remove inappropriate access.

ContentLocator: `regular access review`

Owner: Security engineering lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-SEC-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-SEC-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-SEC-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-SEC-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-SEC-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-SEC-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: signed security-control access 01 evidence receipt; Work contract: `FW-SEC-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Excessive or stale access persists.

N/A: gap

Work: `FW-SEC-06`

### REQ-S7-SEC-PROVENANCE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-SEC-PROVENANCE-01`

RequirementText: Publish SBOM and provenance for supported release artifacts as a supply-chain control.

ContentLocator: `SBOM/provenance where supported.`

Owner: Release security lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-SEC-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-SEC-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-SEC-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-SEC-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-SEC-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-SEC-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: signed security-control provenance 01 evidence receipt; Work contract: `FW-SEC-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Artifact origin or dependency inventory is unverifiable.

N/A: gap

Work: `FW-SEC-06`

### REQ-S7-OPS-HA-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-OPS-HA-01`

RequirementText: Design high availability across explicit failure domains.

ContentLocator: `HA/failure-domain design`

Owner: SRE and runtime lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-OPS-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-OPS-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-OPS-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-OPS-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-OPS-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-OPS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: HA chaos and disaster-recovery ha 01 evidence receipt; Work contract: `FW-OPS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Single failure domain causes avoidable outage.

N/A: gap

Work: `FW-OPS-06`

### REQ-S7-OPS-CAPACITY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-OPS-CAPACITY-01`

RequirementText: Maintain capacity plans based on service demand and failure margins.

ContentLocator: `capacity planning`

Owner: SRE and runtime lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-OPS-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-OPS-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-OPS-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-OPS-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-OPS-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-OPS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: HA chaos and disaster-recovery capacity 01 evidence receipt; Work contract: `FW-OPS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Capacity exhaustion degrades service.

N/A: gap

Work: `FW-OPS-06`

### REQ-S7-OPS-LOAD-SOAK-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-OPS-LOAD-SOAK-01`

RequirementText: Run load and soak tests against the defined production-like scenario.

ContentLocator: `load and soak testing`

Owner: SRE and performance lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-OPS-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-OPS-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-OPS-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-OPS-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-OPS-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-OPS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: HA chaos and disaster-recovery load soak 01 evidence receipt; Work contract: `FW-OPS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Performance or leak failure emerges only in production.

N/A: gap

Work: `FW-OPS-06`

### REQ-S7-OPS-CHAOS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-OPS-CHAOS-01`

RequirementText: Run chaos and failure tests for the defined service failure modes.

ContentLocator: `chaos/failure testing`

Owner: SRE and runtime lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-OPS-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-OPS-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-OPS-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-OPS-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-OPS-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-OPS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: HA chaos and disaster-recovery chaos 01 evidence receipt; Work contract: `FW-OPS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Failure handling remains unproven.

N/A: gap

Work: `FW-OPS-06`

### REQ-S7-OPS-RECOVERY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-OPS-RECOVERY-01`

RequirementText: Verify backups and recovery through real recovery scenarios.

ContentLocator: `backup and recovery verification`

Owner: Recovery lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-OPS-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-OPS-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-OPS-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-OPS-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-OPS-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-OPS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: HA chaos and disaster-recovery recovery 01 evidence receipt; Work contract: `FW-OPS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Backups cannot restore required service state.

N/A: gap

Work: `FW-OPS-06`

### REQ-S7-OPS-INCIDENT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-OPS-INCIDENT-01`

RequirementText: Maintain and exercise incident response procedures.

ContentLocator: `incident response`

Owner: Incident management lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-OPS-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-OPS-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-OPS-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-OPS-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-OPS-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-OPS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: HA chaos and disaster-recovery incident 01 evidence receipt; Work contract: `FW-OPS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Incident response is delayed or inconsistent.

N/A: gap

Work: `FW-OPS-06`

### REQ-S7-OPS-ESCALATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-OPS-ESCALATION-01`

RequirementText: Define and exercise operational escalation paths.

ContentLocator: `escalation`

Owner: Incident management lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-OPS-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-OPS-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-OPS-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-OPS-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-OPS-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-OPS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: HA chaos and disaster-recovery escalation 01 evidence receipt; Work contract: `FW-OPS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unowned incident stalls without escalation.

N/A: gap

Work: `FW-OPS-06`

### REQ-S7-OPS-OWNERSHIP-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-OPS-OWNERSHIP-01`

RequirementText: Assign operational ownership for production services and controls.

ContentLocator: `operational ownership`

Owner: Operations lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-OPS-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-OPS-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-OPS-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-OPS-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-OPS-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-OPS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: HA chaos and disaster-recovery ownership 01 evidence receipt; Work contract: `FW-OPS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Production responsibility is ambiguous.

N/A: gap

Work: `FW-OPS-06`

### REQ-S7-OPS-SLO-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-OPS-SLO-01`

RequirementText: Approve and operate an SLO and error-budget policy.

ContentLocator: `SLO/error-budget policy`

Owner: SRE lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-OPS-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-OPS-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-OPS-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-OPS-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-OPS-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-OPS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: HA chaos and disaster-recovery slo 01 evidence receipt; Work contract: `FW-OPS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Reliability tradeoffs lack a governed decision rule.

N/A: gap

Work: `FW-OPS-06`

### REQ-S7-OPS-DR-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-OPS-DR-01`

RequirementText: Conduct disaster-recovery exercises and retain their evidence.

ContentLocator: `disaster-recovery exercises`

Owner: Recovery lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-OPS-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-OPS-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-OPS-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-OPS-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-OPS-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-OPS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: HA chaos and disaster-recovery dr 01 evidence receipt; Work contract: `FW-OPS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Disaster recovery is an untested claim.

N/A: gap

Work: `FW-OPS-06`

### REQ-S7-DELIVERY-BUILD-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DELIVERY-BUILD-01`

RequirementText: Produce reproducible builds for release artifacts.

ContentLocator: `Reproducible builds`

Owner: Release engineering lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-DELIVERY-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-DELIVERY-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-DELIVERY-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-DELIVERY-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-DELIVERY-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-DELIVERY-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: reproducible delivery build 01 evidence receipt; Work contract: `FW-DELIVERY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Release cannot be reproduced or attributed.

N/A: gap

Work: `FW-DELIVERY-06`

### REQ-S7-DELIVERY-TEST-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DELIVERY-TEST-01`

RequirementText: Run the required release tests in the delivery pipeline.

ContentLocator: `tests`

Owner: Release engineering lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-DELIVERY-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-DELIVERY-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-DELIVERY-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-DELIVERY-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-DELIVERY-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-DELIVERY-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: reproducible delivery test 01 evidence receipt; Work contract: `FW-DELIVERY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Untested artifact is promoted.

N/A: gap

Work: `FW-DELIVERY-06`

### REQ-S7-DELIVERY-MIGRATION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DELIVERY-MIGRATION-01`

RequirementText: Deliver and rehearse compatible migrations with recovery or rollback.

ContentLocator: `migrations`

Owner: Release engineering lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-DELIVERY-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-DELIVERY-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-DELIVERY-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-DELIVERY-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-DELIVERY-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-DELIVERY-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: reproducible delivery migration 01 evidence receipt; Work contract: `FW-DELIVERY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Migration corrupts or strands production state.

N/A: gap

Work: `FW-DELIVERY-06`

### REQ-S7-DELIVERY-DEPLOY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DELIVERY-DEPLOY-01`

RequirementText: Use a governed deployment process for production changes.

ContentLocator: `deployment`

Owner: Release engineering lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-DELIVERY-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-DELIVERY-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-DELIVERY-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-DELIVERY-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-DELIVERY-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-DELIVERY-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: reproducible delivery deploy 01 evidence receipt; Work contract: `FW-DELIVERY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Uncontrolled deployment changes production.

N/A: gap

Work: `FW-DELIVERY-06`

### REQ-S7-DELIVERY-PROGRESSIVE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DELIVERY-PROGRESSIVE-01`

RequirementText: Use progressive delivery where the approved architecture supports it.

ContentLocator: `progressive delivery`

Owner: Release engineering lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-DELIVERY-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-DELIVERY-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-DELIVERY-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-DELIVERY-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-DELIVERY-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-DELIVERY-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: reproducible delivery progressive 01 evidence receipt; Work contract: `FW-DELIVERY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Wide rollout amplifies a defective change.

N/A: gap

Work: `FW-DELIVERY-06`

### REQ-S7-DELIVERY-ROLLBACK-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DELIVERY-ROLLBACK-01`

RequirementText: Provide tested rollback for releasable changes.

ContentLocator: `rollback`

Owner: Release engineering lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-DELIVERY-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-DELIVERY-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-DELIVERY-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-DELIVERY-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-DELIVERY-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-DELIVERY-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: reproducible delivery rollback 01 evidence receipt; Work contract: `FW-DELIVERY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Failed release cannot be safely reversed.

N/A: gap

Work: `FW-DELIVERY-06`

### REQ-S7-DELIVERY-PROMOTION-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DELIVERY-PROMOTION-01`

RequirementText: Promote environments through controlled, evidenced gates.

ContentLocator: `environment promotion`

Owner: Release engineering lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-DELIVERY-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-DELIVERY-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-DELIVERY-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-DELIVERY-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-DELIVERY-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-DELIVERY-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: reproducible delivery promotion 01 evidence receipt; Work contract: `FW-DELIVERY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unqualified artifact reaches production.

N/A: gap

Work: `FW-DELIVERY-06`

### REQ-S7-DELIVERY-CONFIG-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DELIVERY-CONFIG-01`

RequirementText: Manage release configuration with reviewable, environment-scoped controls.

ContentLocator: `configuration management`

Owner: Release engineering lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-DELIVERY-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-DELIVERY-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-DELIVERY-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-DELIVERY-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-DELIVERY-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-DELIVERY-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: reproducible delivery config 01 evidence receipt; Work contract: `FW-DELIVERY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Configuration drift or unsafe secret exposure.

N/A: gap

Work: `FW-DELIVERY-06`

### REQ-S7-DELIVERY-IAC-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DELIVERY-IAC-01`

RequirementText: Manage production infrastructure as code in TerraScale.Orchestrator.

ContentLocator: `infrastructure as code`

Owner: Orchestrator infrastructure lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-DELIVERY-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-DELIVERY-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-DELIVERY-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-DELIVERY-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-DELIVERY-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-DELIVERY-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: reproducible delivery iac 01 evidence receipt; Work contract: `FW-DELIVERY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unreviewed or retired-stub infrastructure mutation.

N/A: gap

Work: `FW-DELIVERY-06`

### REQ-S7-DELIVERY-ARTIFACT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DELIVERY-ARTIFACT-01`

RequirementText: Retain identifiable release artifacts for each promoted release.

ContentLocator: `release artifacts`

Owner: Release engineering lead

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-DELIVERY-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-DELIVERY-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-DELIVERY-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-DELIVERY-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-DELIVERY-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-DELIVERY-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: reproducible delivery artifact 01 evidence receipt; Work contract: `FW-DELIVERY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Release provenance and rollback target are unavailable.

N/A: gap

Work: `FW-DELIVERY-06`

### REQ-S7-ADR-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-ADR-01`

RequirementText: Maintain architecture decision records for material production decisions.

ContentLocator: `Architecture decision records`

Owner: Architecture steward

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-ADR-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-ADR-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-ADR-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-ADR-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-ADR-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-ADR-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: ADR architectural-fit 01 decision receipt; Work contract: `FW-ADR-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Material architecture decision is unreviewable.

N/A: gap

Work: `FW-ADR-06`

### REQ-S7-ADR-VERCEL-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-ADR-VERCEL-01`

RequirementText: Analyze relevant Vercel patterns and adopt only those fitting TerraScale constraints.

ContentLocator: `Vercel`

Owner: Architecture steward

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-ADR-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-ADR-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-ADR-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-ADR-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-ADR-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-ADR-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: ADR architectural-fit vercel 01 decision receipt; Work contract: `FW-ADR-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Inapplicable external pattern is adopted.

N/A: gap

Work: `FW-ADR-06`

### REQ-S7-ADR-ARCHIVED-HOSTING-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-ADR-ARCHIVED-HOSTING-01`

RequirementText: Archived hosting-provider pattern analysis; this local adaptation retires the provider-specific requirement.

ContentLocator: Retired hosting-provider source; see manifest adaptation note.

Owner: Architecture steward

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-ADR-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-ADR-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-ADR-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-ADR-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-ADR-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-ADR-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: archived hosting-provider architectural-fit decision receipt; Work contract: `FW-ADR-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Inapplicable external pattern is adopted.

N/A: gap

Work: `FW-ADR-06`

### REQ-S7-ADR-TURSO-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-ADR-TURSO-01`

RequirementText: Analyze relevant Turso patterns and adopt only those fitting TerraScale constraints.

ContentLocator: `Turso`

Owner: Architecture steward

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-ADR-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-ADR-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-ADR-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-ADR-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-ADR-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-ADR-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: ADR architectural-fit turso 01 decision receipt; Work contract: `FW-ADR-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Inapplicable external pattern is adopted.

N/A: gap

Work: `FW-ADR-06`

### REQ-S7-ADR-NEON-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-ADR-NEON-01`

RequirementText: Analyze relevant Neon patterns and adopt only those fitting TerraScale constraints.

ContentLocator: `Neon`

Owner: Architecture steward

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-ADR-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-ADR-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-ADR-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-ADR-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-ADR-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-ADR-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: ADR architectural-fit neon 01 decision receipt; Work contract: `FW-ADR-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Inapplicable external pattern is adopted.

N/A: gap

Work: `FW-ADR-06`

### REQ-S7-ADR-FIT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-ADR-FIT-01`

RequirementText: Record architectural fit against TerraScale product, architecture, compliance, and operational constraints before adopting an external pattern.

ContentLocator: `Adopt only patterns that fit TerraScale's product, architecture, compliance, and operational constraints.`

Owner: Architecture steward

Life: gap

REST: N/A[production engineering control;API architecture authority;no customer REST contract;FW-ADR-06 real-boundary evidence]

Stream: N/A[production engineering control;API architecture authority;no streaming contract;FW-ADR-06 real-boundary evidence]

.NET: N/A[production engineering control;SDK architecture authority;no typed .NET SDK surface;FW-ADR-06 real-boundary evidence]

TS: N/A[production engineering control;SDK architecture authority;no typed TypeScript SDK surface;FW-ADR-06 real-boundary evidence]

Dashboard: N/A[production engineering control;Dashboard boundary authority;no Dashboard-specific workflow;FW-ADR-06 real-boundary evidence]

MCP: N/A[production engineering control;MCP architecture authority;no MCP tool or resource;FW-ADR-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: ADR architectural-fit fit 01 decision receipt; Work contract: `FW-ADR-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: External pattern conflicts with TerraScale constraints.

N/A: gap

Work: `FW-ADR-06`

### REQ-S7-DOCS-CUSTOMER-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DOCS-CUSTOMER-01`

RequirementText: Provide documentation for customers.

ContentLocator: `customers`

Owner: Documentation lead

Life: gap

REST: N/A[documentation audience;API architecture authority;documentation does not add a REST contract;FW-DOCS-06 real-boundary evidence]

Stream: N/A[documentation audience;API architecture authority;documentation does not add streaming;FW-DOCS-06 real-boundary evidence]

.NET: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

TS: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

Dashboard: N/A[documentation audience;Dashboard boundary authority;documentation is not a Dashboard feature;FW-DOCS-06 real-boundary evidence]

MCP: N/A[documentation audience;MCP architecture authority;documentation does not itself add a tool;FW-DOCS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: audience-specific customer 01 documentation receipt; Work contract: `FW-DOCS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Customers cannot safely use the service.

N/A: gap

Work: `FW-DOCS-06`

### REQ-S7-DOCS-SDK-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DOCS-SDK-01`

RequirementText: Provide documentation for SDK users.

ContentLocator: `SDK users`

Owner: Developer experience lead

Life: gap

REST: N/A[documentation audience;API architecture authority;documentation does not add a REST contract;FW-DOCS-06 real-boundary evidence]

Stream: N/A[documentation audience;API architecture authority;documentation does not add streaming;FW-DOCS-06 real-boundary evidence]

.NET: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

TS: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

Dashboard: N/A[documentation audience;Dashboard boundary authority;documentation is not a Dashboard feature;FW-DOCS-06 real-boundary evidence]

MCP: N/A[documentation audience;MCP architecture authority;documentation does not itself add a tool;FW-DOCS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: audience-specific sdk 01 documentation receipt; Work contract: `FW-DOCS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: SDK integration is error-prone or unsupported.

N/A: gap

Work: `FW-DOCS-06`

### REQ-S7-DOCS-API-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DOCS-API-01`

RequirementText: Provide documentation for API and MCP consumers, including safe agent use and recovery guidance.

ContentLocator: `API/MCP consumers`

Owner: Developer experience and MCP leads

Life: gap

REST: N/A[documentation audience;API architecture authority;documentation does not add a REST contract;FW-DOCS-06 real-boundary evidence]

Stream: N/A[documentation audience;API architecture authority;documentation does not add streaming;FW-DOCS-06 real-boundary evidence]

.NET: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

TS: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

Dashboard: N/A[documentation audience;Dashboard boundary authority;documentation is not a Dashboard feature;FW-DOCS-06 real-boundary evidence]

MCP: N/A[documentation audience;MCP architecture authority;documentation does not itself add a tool;FW-DOCS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: audience-specific api 01 documentation receipt; Work contract: `FW-DOCS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: API or agent consumers lack safe public-contract and recovery guidance.

N/A: gap

Work: `FW-DOCS-06`

### REQ-S7-DOCS-OPERATOR-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DOCS-OPERATOR-01`

RequirementText: Provide documentation for operators.

ContentLocator: `operators`

Owner: Operations documentation lead

Life: gap

REST: N/A[documentation audience;API architecture authority;documentation does not add a REST contract;FW-DOCS-06 real-boundary evidence]

Stream: N/A[documentation audience;API architecture authority;documentation does not add streaming;FW-DOCS-06 real-boundary evidence]

.NET: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

TS: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

Dashboard: N/A[documentation audience;Dashboard boundary authority;documentation is not a Dashboard feature;FW-DOCS-06 real-boundary evidence]

MCP: N/A[documentation audience;MCP architecture authority;documentation does not itself add a tool;FW-DOCS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: audience-specific operator 01 documentation receipt; Work contract: `FW-DOCS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Operators cannot run the service safely.

N/A: gap

Work: `FW-DOCS-06`

### REQ-S7-DOCS-SECURITY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DOCS-SECURITY-01`

RequirementText: Provide documentation for security reviewers and responders.

ContentLocator: `security`

Owner: Security documentation lead

Life: gap

REST: N/A[documentation audience;API architecture authority;documentation does not add a REST contract;FW-DOCS-06 real-boundary evidence]

Stream: N/A[documentation audience;API architecture authority;documentation does not add streaming;FW-DOCS-06 real-boundary evidence]

.NET: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

TS: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

Dashboard: N/A[documentation audience;Dashboard boundary authority;documentation is not a Dashboard feature;FW-DOCS-06 real-boundary evidence]

MCP: N/A[documentation audience;MCP architecture authority;documentation does not itself add a tool;FW-DOCS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: audience-specific security 01 documentation receipt; Work contract: `FW-DOCS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Security controls and response are not actionable.

N/A: gap

Work: `FW-DOCS-06`

### REQ-S7-DOCS-BILLING-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DOCS-BILLING-01`

RequirementText: Provide documentation for billing workflows.

ContentLocator: `billing`

Owner: Billing documentation lead

Life: gap

REST: N/A[documentation audience;API architecture authority;documentation does not add a REST contract;FW-DOCS-06 real-boundary evidence]

Stream: N/A[documentation audience;API architecture authority;documentation does not add streaming;FW-DOCS-06 real-boundary evidence]

.NET: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

TS: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

Dashboard: N/A[documentation audience;Dashboard boundary authority;documentation is not a Dashboard feature;FW-DOCS-06 real-boundary evidence]

MCP: N/A[documentation audience;MCP architecture authority;documentation does not itself add a tool;FW-DOCS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: audience-specific billing 01 documentation receipt; Work contract: `FW-DOCS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Billing workflow is misoperated.

N/A: gap

Work: `FW-DOCS-06`

### REQ-S7-DOCS-SUPPORT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DOCS-SUPPORT-01`

RequirementText: Provide documentation for support workflows.

ContentLocator: `support`

Owner: Support documentation lead

Life: gap

REST: N/A[documentation audience;API architecture authority;documentation does not add a REST contract;FW-DOCS-06 real-boundary evidence]

Stream: N/A[documentation audience;API architecture authority;documentation does not add streaming;FW-DOCS-06 real-boundary evidence]

.NET: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

TS: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

Dashboard: N/A[documentation audience;Dashboard boundary authority;documentation is not a Dashboard feature;FW-DOCS-06 real-boundary evidence]

MCP: N/A[documentation audience;MCP architecture authority;documentation does not itself add a tool;FW-DOCS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: audience-specific support 01 documentation receipt; Work contract: `FW-DOCS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Support cannot diagnose or assist safely.

N/A: gap

Work: `FW-DOCS-06`

### REQ-S7-DOCS-ONCALL-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DOCS-ONCALL-01`

RequirementText: Provide documentation for on-call response.

ContentLocator: `on-call response`

Owner: Operations documentation lead

Life: gap

REST: N/A[documentation audience;API architecture authority;documentation does not add a REST contract;FW-DOCS-06 real-boundary evidence]

Stream: N/A[documentation audience;API architecture authority;documentation does not add streaming;FW-DOCS-06 real-boundary evidence]

.NET: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

TS: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

Dashboard: N/A[documentation audience;Dashboard boundary authority;documentation is not a Dashboard feature;FW-DOCS-06 real-boundary evidence]

MCP: N/A[documentation audience;MCP architecture authority;documentation does not itself add a tool;FW-DOCS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: audience-specific oncall 01 documentation receipt; Work contract: `FW-DOCS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: On-call responder lacks an actionable incident guide.

N/A: gap

Work: `FW-DOCS-06`

### REQ-S7-DOCS-RECOVERY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DOCS-RECOVERY-01`

RequirementText: Provide documentation for recovery procedures.

ContentLocator: `recovery`

Owner: Recovery documentation lead

Life: gap

REST: N/A[documentation audience;API architecture authority;documentation does not add a REST contract;FW-DOCS-06 real-boundary evidence]

Stream: N/A[documentation audience;API architecture authority;documentation does not add streaming;FW-DOCS-06 real-boundary evidence]

.NET: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

TS: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

Dashboard: N/A[documentation audience;Dashboard boundary authority;documentation is not a Dashboard feature;FW-DOCS-06 real-boundary evidence]

MCP: N/A[documentation audience;MCP architecture authority;documentation does not itself add a tool;FW-DOCS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: audience-specific recovery 01 documentation receipt; Work contract: `FW-DOCS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Recovery is performed incorrectly or too slowly.

N/A: gap

Work: `FW-DOCS-06`

### REQ-S7-DOCS-RELEASE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DOCS-RELEASE-01`

RequirementText: Provide documentation for release procedures.

ContentLocator: `release`

Owner: Release documentation lead

Life: gap

REST: N/A[documentation audience;API architecture authority;documentation does not add a REST contract;FW-DOCS-06 real-boundary evidence]

Stream: N/A[documentation audience;API architecture authority;documentation does not add streaming;FW-DOCS-06 real-boundary evidence]

.NET: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

TS: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

Dashboard: N/A[documentation audience;Dashboard boundary authority;documentation is not a Dashboard feature;FW-DOCS-06 real-boundary evidence]

MCP: N/A[documentation audience;MCP architecture authority;documentation does not itself add a tool;FW-DOCS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: audience-specific release 01 documentation receipt; Work contract: `FW-DOCS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Release process is inconsistent.

N/A: gap

Work: `FW-DOCS-06`

### REQ-S7-DOCS-CONTRIBUTOR-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Product Scope > ### 7. Production engineering`

RequirementID: `REQ-S7-DOCS-CONTRIBUTOR-01`

RequirementText: Provide documentation for local contributors and developers.

ContentLocator: `local contributors`

Owner: Developer experience lead

Life: gap

REST: N/A[documentation audience;API architecture authority;documentation does not add a REST contract;FW-DOCS-06 real-boundary evidence]

Stream: N/A[documentation audience;API architecture authority;documentation does not add streaming;FW-DOCS-06 real-boundary evidence]

.NET: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

TS: N/A[documentation audience;SDK architecture authority;documentation is not an SDK surface;FW-DOCS-06 real-boundary evidence]

Dashboard: N/A[documentation audience;Dashboard boundary authority;documentation is not a Dashboard feature;FW-DOCS-06 real-boundary evidence]

MCP: N/A[documentation audience;MCP architecture authority;documentation does not itself add a tool;FW-DOCS-06 real-boundary evidence]

Auth: Named production-control owner with least-privilege access and audit.

AT: Planned artifact: audience-specific contributor 01 documentation receipt; Work contract: `FW-DOCS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Contributor workflow is irreproducible.

N/A: gap

Work: `FW-DOCS-06`


## P0 control-board records

The `REQ-P0-*` records retain the complete control-board task contracts while the governing Phase 0 atoms following `REQ-P0-RECEIPT-01` split the roadmap, validator, receipt rule, and scheduling obligations into literal source locations. Neither set asserts P0 acceptance.

### P0 control-board summary, non-governing navigation only

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`

The individual records below are governing. The task names occur in a GOAL table, so their common SourceAnchor is the actual parent heading and each ContentLocator identifies the exact table-cell text without inventing an anchor leaf.

### REQ-P0-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`

RequirementID: `REQ-P0-01`

ContentLocator: `| P0-01 | **Decision register normalization.**`

RequirementText: Normalize the decision register under P0-01 exclusive ownership and objective exit evidence.

Owner: Integration and contract steward

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Coordinator lease and named owner authority.

AT: Planned artifact: P0 decision packet and digest graph validation receipt; Work contract: `P0-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unresolved controlling decision.

N/A: gap

Work: `P0-01`

### REQ-P0-01V

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`

RequirementID: `REQ-P0-01V`

ContentLocator: `| P0-01V | **Decision/readiness invariant validator.**`

RequirementText: Build and rerun the fail-closed P0-01 decision and readiness invariant validator against final P0-01 digests.

Owner: Verification lane

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Read-only P0-01 access and verification lease.

AT: Planned artifact: validator positive and adversarial results for unknown, duplicate, empty, cyclic, self-alias, dependency-cycle, malformed/missing, and invalid-reference classes; Work contract: `P0-01V`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Malformed or cyclic readiness graph accepted.

N/A: gap

Work: `P0-01V`

### REQ-P0-03

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`

RequirementID: `REQ-P0-03`

ContentLocator: `| P0-03 | **Descriptor inventory and retired-workaround ledger.**`

RequirementText: Complete the descriptor inventory and retired-workaround ledger with native replacement gates.

Owner: Cross-repository cleanup lane

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Repository read authority.

AT: Planned artifact: descriptor and workaround retirement-ledger receipt; Work contract: `P0-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Retired workaround treated as production contract.

N/A: gap

Work: `P0-03`

### REQ-P0-04A

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`

RequirementID: `REQ-P0-04A`

ContentLocator: `| P0-04A | **Public provider/TCO and region research.**`

RequirementText: Complete public provider, TCO, and region research without entering an ARM64 lab or asserting a performance baseline.

Owner: Cloud research lane

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Public-source and read-only billing authority.

AT: Planned artifact: price and region comparison receipt with source date and currency; Work contract: `P0-04A`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unsupported provider or cost claim.

N/A: gap

Work: `P0-04A`

### REQ-P0-04B

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`

RequirementID: `REQ-P0-04B`

ContentLocator: `| P0-04B | **ARM64/TerraBase storage benchmark inputs.**`

RequirementText: Capture ARM64 storage benchmark inputs only on the positively owned isolated lab target with exclusive CPU allocation.

Owner: Benchmark lane

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Lab ownership and exclusive CPU allocation authority.

AT: Planned artifact: ARM64 benchmark manifest with target identity, CPU isolation, method, timestamp, and digest receipt; Work contract: `P0-04B`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Invalid benchmark baseline.

N/A: gap

Work: `P0-04B`

### REQ-P0-05

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`

RequirementID: `REQ-P0-05`

ContentLocator: `| P0-05 | **Measurable SLO approval and ADR tranche.**`

RequirementText: Approve measurable SLO inputs and the listed ADR tranche with authority and residual risk.

Owner: Integration and contract steward

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Product, operations, security, and legal authority.

AT: Planned artifact: ADR and SLO numeric-target approval receipt; Work contract: `P0-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unapproved measurable control input.

N/A: gap

Work: `P0-05`

### REQ-P0-06

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`

RequirementID: `REQ-P0-06`

ContentLocator: `| P0-06 | **Credential-gated evidence tooling and bounded RF=1 lab qualification.**`

RequirementText: Qualify credential-gated evidence tooling and bounded RF=1 lab evidence without claiming R3 or production qualification.

Owner: Verification lane

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: CI administrator and signing-identity authority.

AT: Planned artifact: toolchain attestation with exact-tree provenance and RF=1 receipt; Work contract: `P0-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Lab evidence represented as production evidence.

N/A: gap

Work: `P0-06`

### REQ-P0-07

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`

RequirementID: `REQ-P0-07`

ContentLocator: `| P0-07 | **Normative requirements and future-work traceability.**`

RequirementText: Produce the P0-07 sole report with every GOAL atom, stable heading-plus-requirement anchor, all required interfaces, authorization, tests, evidence, claim, owner, and complete later-work contract.

Owner: Product integration lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Accountable-owner assignment authority and independent reviewer.

AT: Planned artifact: trace matrix task-ID and gap-completeness independent-review receipt; Work contract: `P0-07`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: `docs/agentic-delivery/2026-08-05/phase-0/p0-07-requirement-traceability.md`

Runbook: gap

Risk: Missing normative atom or unjustified gap.

N/A: gap

Work: `P0-07`

### REQ-P0-08

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`

RequirementID: `REQ-P0-08`

ContentLocator: `| P0-08 | **Authoritative public-contract inventory and snapshot provenance.**`

RequirementText: Record the authoritative versioned `/api/v1` inventory, Platform provenance, auth, idempotency, sensitivity, tenant scope, and the 149-versus-147 discrepancy without source mutation.

Owner: Platform-contract investigator

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: API architecture steward.

AT: Planned artifact: public-contract inventory and private-transport exclusion receipt; Work contract: `P0-08`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: `docs/agentic-delivery/2026-08-05/phase-0/p0-08-platform-openapi-inventory.md`

Runbook: gap

Risk: Public contract drift or private RPC exposure.

N/A: gap

Work: `P0-08`

### REQ-P0-09

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`

RequirementID: `REQ-P0-09`

ContentLocator: `| P0-09 | **SDK support classification and parity evidence.**`

RequirementText: Classify every public operation for .NET and TypeScript support or explicit safe alternative with typed mapping and real success, failure, and cross-tenant evidence.

Owner: SDK-classification investigator

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: SDK architecture decision authority.

AT: Planned artifact: OpenAPI and typed SDK success, failure, cross-tenant, and safe-alternative receipt; Work contract: `P0-09`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: `docs/agentic-delivery/2026-08-05/phase-0/p0-09-sdk-contract-classification.md`

Runbook: gap

Risk: Unsupported typed operation represented as parity.

N/A: gap

Work: `P0-09`

### REQ-P0-10

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`

RequirementID: `REQ-P0-10`

ContentLocator: `| P0-10 | **MCP safety/capability and Dashboard external-consumer proof.**`

RequirementText: Map each Dashboard action to public API, typed SDK, and MCP or safe alternative; prove no private, direct, generic, raw-fetch, special-header, or direct-TerraBase bypass and prove representative live two-tenant behavior.

Owner: Boundary and MCP investigator

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Product security mutation and confirmation authority.

AT: Planned artifact: static boundary and live AppHost two-tenant receipt; Work contract: `P0-10`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: `docs/agentic-delivery/2026-08-05/phase-0/p0-10-dashboard-mcp-boundary-proof.md`

Runbook: gap

Risk: Dashboard bypass or unsafe MCP capability.

N/A: gap

Work: `P0-10`

### REQ-P0-11

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`

RequirementID: `REQ-P0-11`

ContentLocator: `| P0-11 | **Capability/status and documentation-claim governance.**`

RequirementText: Link every public claim to a capability, exact evidence or commit, owner, review date, lifecycle, and required approval; block unresolved production-marketing contradiction and unsupported claims.

Owner: Documentation-claims investigator

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Product, commercial, and legal approval authority.

AT: Planned artifact: claim register capability, evidence, owner, review-date, lifecycle, and approval receipt; Work contract: `P0-11`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: `docs/agentic-delivery/2026-08-05/phase-0/p0-11-public-claim-governance.md`

Runbook: gap

Risk: Unauthorized commitment.

N/A: gap

Work: `P0-11`

### REQ-P0-12

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`

RequirementID: `REQ-P0-12`

ContentLocator: `| P0-12 | **Register and validate every later-phase work package.**`

RequirementText: Validate every later-phase requirement for task, owner, exact scope, predecessor, risk, real-boundary validation, exit evidence, acyclic prerequisites, no unleased overlap, and cross-repository order and compatibility.

Owner: Root integration coordinator

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Register-validation authority.

AT: Planned artifact: trace matrix independent review, fail-closed validation, and immutable-index receipt; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: `docs/agentic-delivery/2026-08-05/phase-0/p0-12-work-package-register-validation.md`

Runbook: gap

Risk: Missing later work or overlapping ownership.

N/A: gap

Work: `P0-12`

### REQ-P0-RECEIPT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Report and Cross-Repository Integration Receipts`

RequirementID: `REQ-P0-RECEIPT-01`

ContentLocator: `Every control-board task has an exclusive Markdown report.`

RequirementText: Evidence-repository work is reviewed and validated first; the Documentation report follows and records exact commit or digest, command results, inputs, residual risk, and compatibility result. P0-07 is independently reviewed for task-ID and gap completeness before P0-12 imports it.

Owner: Product integration lead

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: Exclusive path lease and independent review.

AT: Planned artifact: trace matrix independent review, fail-closed validation, and immutable-index receipt; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Report substituted for underlying evidence.

N/A: gap

Work: `P0-12`

## Governing Phase 0 atomic records

Status: open. These are planning atoms only. They do not assert implementation, acceptance, production readiness, or P0 acceptance. Customer surfaces are irrelevant to Phase 0 control work and use the required N/A form, never an implied product decision.

### REQ-P0-ROADMAP-PARALLEL-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`
RequirementID: `REQ-P0-ROADMAP-PARALLEL-01`
RequirementText: Permit parallel workstreams only after dependencies and ownership are explicit.
ContentLocator: `Workstreams may proceed in parallel only after their dependencies and ownership are explicit.`
Owner: Root integration coordinator
Life: gap
REST: N/A[Phase 0 delivery governance;API architecture authority;no public REST contract;independent P0 receipt review]
Stream: N/A[Phase 0 delivery governance;API architecture authority;no public streaming contract;independent P0 receipt review]
.NET: N/A[Phase 0 delivery governance;SDK architecture authority;no SDK surface;independent P0 receipt review]
TS: N/A[Phase 0 delivery governance;SDK architecture authority;no SDK surface;independent P0 receipt review]
Dashboard: N/A[Phase 0 delivery governance;Dashboard boundary authority;no Dashboard feature;independent P0 receipt review]
MCP: N/A[Phase 0 delivery governance;MCP architecture authority;no MCP tool;independent P0 receipt review]
Auth: Coordinator grants an exclusive path lease only after explicit dependency and ownership review.
AT: Planned artifact: trace matrix independent review, fail-closed validation, and immutable-index receipt; Work contract: `P0-12`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Concurrent writers overlap or start on unapproved assumptions.
N/A: gap
Work: `P0-12`

### REQ-P0-ROADMAP-EVIDENCE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap`
RequirementID: `REQ-P0-ROADMAP-EVIDENCE-01`
RequirementText: Require specified evidence and Delivery Gates, not code completion alone, for later-phase sign-off.
ContentLocator: `A later phase cannot be signed off by code completion alone; it requires the specified evidence and the Delivery Gates below.`
Owner: Root integration coordinator
Life: gap
REST: N/A[Phase 0 delivery governance;API architecture authority;no public REST contract;independent gate review]
Stream: N/A[Phase 0 delivery governance;API architecture authority;no public streaming contract;independent gate review]
.NET: N/A[Phase 0 delivery governance;SDK architecture authority;no SDK surface;independent gate review]
TS: N/A[Phase 0 delivery governance;SDK architecture authority;no SDK surface;independent gate review]
Dashboard: N/A[Phase 0 delivery governance;Dashboard boundary authority;no Dashboard feature;independent gate review]
MCP: N/A[Phase 0 delivery governance;MCP architecture authority;no MCP tool;independent gate review]
Auth: Delivery-gate authority.
AT: Planned artifact: trace matrix independent review, fail-closed validation, and immutable-index receipt; Work contract: `P0-12`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Code completion is misrepresented as release evidence.
N/A: gap
Work: `P0-12`

### REQ-P0-BASELINE-ARTIFACTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=0; title=Production truth, decisions, and measurable baselines]`
RequirementID: `REQ-P0-BASELINE-ARTIFACTS-01`
RequirementText: Produce the authoritative architecture map, service/data-flow diagrams, inventory, requirement traceability matrix, capability/status registry, threat model, data classification, and dependency graph.
ContentLocator: `- Produce the authoritative architecture map, service/data-flow diagrams, inventory, requirement traceability matrix, capability/status registry, threat model, data classification, and dependency graph.`
Owner: Product integration lead
Life: gap
REST: N/A[Phase 0 planning artifacts;API architecture authority;no public REST contract;independent artifact review]
Stream: N/A[Phase 0 planning artifacts;API architecture authority;no public streaming contract;independent artifact review]
.NET: N/A[Phase 0 planning artifacts;SDK architecture authority;no SDK surface;independent artifact review]
TS: N/A[Phase 0 planning artifacts;SDK architecture authority;no SDK surface;independent artifact review]
Dashboard: N/A[Phase 0 planning artifacts;Dashboard boundary authority;no Dashboard feature;independent artifact review]
MCP: N/A[Phase 0 planning artifacts;MCP architecture authority;no MCP tool;independent artifact review]
Auth: Named architecture, security, data, and integration owners.
AT: Planned artifact: P0 decision packet and digest graph validation receipt; Work contract: `P0-07`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Planning relies on unknown architecture, data, or dependency truth.
N/A: gap
Work: `P0-07`

### REQ-P0-ORCHESTRATOR-INPUTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=0; title=Production truth, decisions, and measurable baselines]`
RequirementID: `REQ-P0-ORCHESTRATOR-INPUTS-01`
RequirementText: Close the cost and storage model; approved RPO/RTO, backup retention, security-token TTL, density, audit-retention, survival-window SLOs; provider residual inventory; supply-chain pins/mirrors/signing; ARM64 qualification; DNS, VPN, IdP, regional mirror, and NATS dual-plane decisions.
ContentLocator: `- Close Orchestrator Phase-0 inputs: cost and storage model; approved RPO/RTO, backup retention, security-token TTL, density, audit-retention, and survival-window SLOs; provider residual inventory; selected supply-chain pins/mirrors/signing; ARM64 qualification; DNS, VPN, IdP, regional mirror, and NATS dual-plane decisions.`
Owner: Integration and contract steward
Life: gap
REST: N/A[Orchestrator Phase 0 inputs;API architecture authority;no public REST contract;approved ADR and receipt]
Stream: N/A[Orchestrator Phase 0 inputs;API architecture authority;no public streaming contract;approved ADR and receipt]
.NET: N/A[Orchestrator Phase 0 inputs;SDK architecture authority;no SDK surface;approved ADR and receipt]
TS: N/A[Orchestrator Phase 0 inputs;SDK architecture authority;no SDK surface;approved ADR and receipt]
Dashboard: N/A[Orchestrator Phase 0 inputs;Dashboard boundary authority;no Dashboard feature;approved ADR and receipt]
MCP: N/A[Orchestrator Phase 0 inputs;MCP architecture authority;no MCP tool;approved ADR and receipt]
Auth: Product, operations, security, legal, cloud, and signing authorities.
AT: Planned artifact: P0 decision packet and digest graph validation receipt; Work contract: `P0-05`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Production controls are based on unapproved measurable inputs.
N/A: gap
Work: `P0-05`

### REQ-P0-PERFORMANCE-LAB-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=0; title=Production truth, decisions, and measurable baselines]`
RequirementID: `REQ-P0-PERFORMANCE-LAB-01`
RequirementText: Establish exclusive-CPU performance baselines and record capacity, saturation, and regression budgets; do not treat an invalid self-test as a baseline.
ContentLocator: `- Establish the performance lab with exclusive CPU placement and publish approved TerraBase benchmark baselines. Record capacity, saturation, and regression budgets instead of treating an invalid self-test as a baseline.`
Owner: Benchmark lane
Life: gap
REST: N/A[performance-lab baseline;API architecture authority;no public REST contract;CPU-isolation attestation]
Stream: N/A[performance-lab baseline;API architecture authority;no public streaming contract;CPU-isolation attestation]
.NET: N/A[performance-lab baseline;SDK architecture authority;no SDK surface;CPU-isolation attestation]
TS: N/A[performance-lab baseline;SDK architecture authority;no SDK surface;CPU-isolation attestation]
Dashboard: N/A[performance-lab baseline;Dashboard boundary authority;no Dashboard feature;CPU-isolation attestation]
MCP: N/A[performance-lab baseline;MCP architecture authority;no MCP tool;CPU-isolation attestation]
Auth: Positively owned isolated lab target and exclusive CPU allocation authority.
AT: Planned artifact: ARM64 benchmark manifest with target identity, CPU isolation, method, timestamp, and digest receipt; Work contract: `P0-04B`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Invalid or noisy test becomes a capacity claim.
N/A: gap
Work: `P0-04B`

### REQ-P0-CLAIM-REGISTRY-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=0; title=Production truth, decisions, and measurable baselines]`
RequirementID: `REQ-P0-CLAIM-REGISTRY-01`
RequirementText: Create a source-backed capability registry and correct stale deployment ownership, security/provider, pricing, and availability claims before public-marketing expansion.
ContentLocator: `- Create the source-backed capability registry and correct stale deployment ownership, security/provider, pricing, and availability claims before expanding public marketing.`
Owner: Documentation-claims investigator
Life: gap
REST: N/A[claim governance;API architecture authority;no public REST contract;claim-review receipt]
Stream: N/A[claim governance;API architecture authority;no public streaming contract;claim-review receipt]
.NET: N/A[claim governance;SDK architecture authority;no SDK surface;claim-review receipt]
TS: N/A[claim governance;SDK architecture authority;no SDK surface;claim-review receipt]
Dashboard: N/A[claim governance;Dashboard boundary authority;no Dashboard feature;claim-review receipt]
MCP: N/A[claim governance;MCP architecture authority;no MCP tool;claim-review receipt]
Auth: Product, commercial, and legal claim approvers.
AT: Planned artifact: claim register capability, evidence, owner, review-date, lifecycle, and approval receipt; Work contract: `P0-11`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Stale public claim creates an unauthorized commitment.
N/A: gap
Work: `P0-11`

### REQ-P0-EXIT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > PhaseHeading[level=3; number=0; title=Production truth, decisions, and measurable baselines]`
RequirementID: `REQ-P0-EXIT-01`
RequirementText: Require approved ADRs/decision records, bounded product model, named owners, cost/risk acceptance, benchmark baseline, threat-model action plan, and no unowned normative requirement.
ContentLocator: `- Exit evidence: approved ADRs/decision records, bounded product model, named owners, cost/risk acceptance, benchmark baseline, threat-model action plan, and a traceability matrix with no unowned normative requirement.`
Owner: Root integration coordinator
Life: gap
REST: N/A[Phase 0 exit evidence;API architecture authority;no public REST contract;independent P0 completion review]
Stream: N/A[Phase 0 exit evidence;API architecture authority;no public streaming contract;independent P0 completion review]
.NET: N/A[Phase 0 exit evidence;SDK architecture authority;no SDK surface;independent P0 completion review]
TS: N/A[Phase 0 exit evidence;SDK architecture authority;no SDK surface;independent P0 completion review]
Dashboard: N/A[Phase 0 exit evidence;Dashboard boundary authority;no Dashboard feature;independent P0 completion review]
MCP: N/A[Phase 0 exit evidence;MCP architecture authority;no MCP tool;independent P0 completion review]
Auth: Accepted decision, risk, and ownership authorities.
AT: Planned artifact: trace matrix independent review, fail-closed validation, and immutable-index receipt; Work contract: `P0-12`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Phase 0 closes with an unowned normative requirement.
N/A: gap
Work: `P0-12`

### REQ-P0-01-OWNERSHIP-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board`
RequirementID: `REQ-P0-01-OWNERSHIP-01`
RequirementText: P0-01 owns only the decision packet and readiness index, does not edit ADR prose or evidence summaries, has no dependency, and requires named owners without reopening accepted policy without authority.
ContentLocator: | P0-01 | **Decision register normalization.** Coordinator: Integration/contract steward. Owns only `TerraScale.Orchestrator/docs/decisions/owner-decision-packet.json` and `TerraScale.Orchestrator/docs/adr/readiness-index.yaml`; it does not edit ADR prose or evidence summaries. | None | Named product, operations, and security owners for unresolved measurable inputs. Do not reopen accepted policy decisions without authority. |
Owner: Integration/contract steward
Life: gap
REST: N/A[decision-register normalization;API architecture authority;no public REST contract;P0-01 receipt]
Stream: N/A[decision-register normalization;API architecture authority;no public streaming contract;P0-01 receipt]
.NET: N/A[decision-register normalization;SDK architecture authority;no SDK surface;P0-01 receipt]
TS: N/A[decision-register normalization;SDK architecture authority;no SDK surface;P0-01 receipt]
Dashboard: N/A[decision-register normalization;Dashboard boundary authority;no Dashboard feature;P0-01 receipt]
MCP: N/A[decision-register normalization;MCP architecture authority;no MCP tool;P0-01 receipt]
Auth: Named product, operations, and security owners; accepted policy remains closed absent authority.
AT: Planned artifact: P0 decision packet and digest graph validation receipt; Work contract: `P0-01`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unauthorised decision rewrite or source-scope expansion.
N/A: gap
Work: `P0-01`

### REQ-P0-01-EXIT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board`
RequirementID: `REQ-P0-01-EXIT-01`
RequirementText: Separate accepted topology policy from open numeric targets; resolve every normative requirement and controlling input, retain an acyclic executable graph, and require P0-01V final-digest rerun before acceptance.
ContentLocator: `A dated decision/status map separates accepted topology policy from open numeric targets; every normative requirement has owner, ADR/decision, dependency, and evidence location; no contradiction between the readiness index and evidence guide. The executable prerequisite graph is acyclic after closure evidence is classified separately; every controlling-input reference resolves to either an atomic packet ID or an aggregate alias that recursively expands to a non-empty, duplicate-free set of existing atomic packet IDs, with no alias cycle or self-reference; accepted owner policy is not mislabeled as a pending owner input. Before acceptance, P0-01V reruns against the exact final packet/index commit digests and its receipt records a matching result.`
Owner: Integration/contract steward
Life: gap
REST: N/A[decision-register normalization;API architecture authority;no public REST contract;P0-01V final-digest receipt]
Stream: N/A[decision-register normalization;API architecture authority;no public streaming contract;P0-01V final-digest receipt]
.NET: N/A[decision-register normalization;SDK architecture authority;no SDK surface;P0-01V final-digest receipt]
TS: N/A[decision-register normalization;SDK architecture authority;no SDK surface;P0-01V final-digest receipt]
Dashboard: N/A[decision-register normalization;Dashboard boundary authority;no Dashboard feature;P0-01V final-digest receipt]
MCP: N/A[decision-register normalization;MCP architecture authority;no MCP tool;P0-01V final-digest receipt]
Auth: Decision and acceptance authority.
AT: Planned artifact: trace matrix independent review, fail-closed validation, and immutable-index receipt; Work contract: `P0-01V`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Cyclic or unresolved prerequisite truth is accepted.
N/A: gap
Work: `P0-01V`

### REQ-P0-01V-VALIDATOR-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board`
RequirementID: `REQ-P0-01V-VALIDATOR-01`
RequirementText: P0-01V owns only TranslatedCommands.cs and ToolingTests.cs, reads but does not modify P0-01 data, begins from a draft, then reruns final exact P0-01 digests before P0-01 acceptance.
ContentLocator: | P0-01V | **Decision/readiness invariant validator.** Coordinator: Verification lane. Owns only `TerraScale.Orchestrator/tools/TerraScale.Orchestrator.Tooling/TranslatedCommands.cs` and `TerraScale.Orchestrator/tools/TerraScale.Orchestrator.Tooling/ToolingTests.cs`; it reads but does not modify the P0-01 packet/index. | A draft P0-01 packet/index; P0-01V must rerun against P0-01's exact final commit digests before P0-01 can be accepted. | None |
Owner: Verification lane
Life: gap
REST: N/A[invariant validator;API architecture authority;no public REST contract;validator command receipt]
Stream: N/A[invariant validator;API architecture authority;no public streaming contract;validator command receipt]
.NET: N/A[invariant validator;SDK architecture authority;no SDK surface;validator command receipt]
TS: N/A[invariant validator;SDK architecture authority;no SDK surface;validator command receipt]
Dashboard: N/A[invariant validator;Dashboard boundary authority;no Dashboard feature;validator command receipt]
MCP: N/A[invariant validator;MCP architecture authority;no MCP tool;validator command receipt]
Auth: Verification lease and read-only P0-01 access.
AT: Planned artifact: validator positive and adversarial results for unknown, duplicate, empty, cyclic, self-alias, dependency-cycle, malformed/missing, and invalid-reference classes; Work contract: `P0-01V`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Validator mutates its input or verifies a stale digest.
N/A: gap
Work: `P0-01V`

### REQ-P0-01V-INVARIANTS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board`
RequirementID: `REQ-P0-01V-INVARIANTS-01`
RequirementText: Fail closed on mandatory record cardinality and fields, declared status, owner, decision/ADR, executable dependency, closure evidence, evidence location, source anchor, readiness and controlling-input resolution, and distinction of executable prerequisites from closure evidence.
ContentLocator: `status constrained to a declared allowed value, owner, decision/ADR, executable dependency, closure evidence, evidence location, and source anchor`
SourcePosition: Structural disambiguator only, not source text: `second delimited Control Board clause`.
Owner: Verification lane
Life: gap
REST: N/A[invariant validator;API architecture authority;no public REST contract;fail-closed test receipt]
Stream: N/A[invariant validator;API architecture authority;no public streaming contract;fail-closed test receipt]
.NET: N/A[invariant validator;SDK architecture authority;no SDK surface;fail-closed test receipt]
TS: N/A[invariant validator;SDK architecture authority;no SDK surface;fail-closed test receipt]
Dashboard: N/A[invariant validator;Dashboard boundary authority;no Dashboard feature;fail-closed test receipt]
MCP: N/A[invariant validator;MCP architecture authority;no MCP tool;fail-closed test receipt]
Auth: None.
AT: Planned artifact: validator positive and adversarial results for unknown, duplicate, empty, cyclic, self-alias, dependency-cycle, malformed/missing, and invalid-reference classes; Work contract: `P0-01V`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Invalid readiness metadata appears valid.
N/A: gap
Work: `P0-01V`

### REQ-P0-01V-REJECTIONS-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board`
RequirementID: `REQ-P0-01V-REJECTIONS-01`
RequirementText: Reject unknown, duplicate, empty, cyclic, and self-referential aggregate aliases; dependency cycles; malformed or missing fields; and invalid status, owner, decision, ADR, evidence, and source-anchor references, with current positive P0-01 data and adversarial fixtures for every failure class.
ContentLocator: `and reject unknown/duplicate/empty/cyclic/self-referential aggregate aliases, dependency cycles, malformed/missing fields, and invalid status/owner/decision/ADR/evidence/source-anchor references. The proof includes current P0-01 data and adversarial negative fixtures for each failure class.`
Owner: Verification lane
Life: gap
REST: N/A[invariant validator;API architecture authority;no public REST contract;adversarial validator receipt]
Stream: N/A[invariant validator;API architecture authority;no public streaming contract;adversarial validator receipt]
.NET: N/A[invariant validator;SDK architecture authority;no SDK surface;adversarial validator receipt]
TS: N/A[invariant validator;SDK architecture authority;no SDK surface;adversarial validator receipt]
Dashboard: N/A[invariant validator;Dashboard boundary authority;no Dashboard feature;adversarial validator receipt]
MCP: N/A[invariant validator;MCP architecture authority;no MCP tool;adversarial validator receipt]
Auth: None.
AT: Planned artifact: validator positive and adversarial results for unknown, duplicate, empty, cyclic, self-alias, dependency-cycle, malformed/missing, and invalid-reference classes; Work contract: `P0-01V`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: A malformed, cyclic, or untraceable controlling input passes validation.
N/A: gap
Work: `P0-01V`

### REQ-P0-07-SOLE-PRODUCT-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board`
RequirementID: `REQ-P0-07-SOLE-PRODUCT-01`
RequirementText: P0-07 owns only this traceability report, has no dependency, receives accountable-owner assignment from product/engineering leads, and is a sole work product subject to independent task-ID and gap-completeness review before P0-12 imports it. This is not an acceptance claim.
ContentLocator: | P0-07 | **Normative requirements and future-work traceability.** Coordinator: Product integration lead. Owns only `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-07-requirement-traceability.md`. | None | Accountable owner assignment from product/engineering leads. |
Owner: Product integration lead
Life: gap
REST: N/A[traceability report;API architecture authority;no public REST contract;independent task-ID and gap-completeness review]
Stream: N/A[traceability report;API architecture authority;no public streaming contract;independent task-ID and gap-completeness review]
.NET: N/A[traceability report;SDK architecture authority;no SDK surface;independent task-ID and gap-completeness review]
TS: N/A[traceability report;SDK architecture authority;no SDK surface;independent task-ID and gap-completeness review]
Dashboard: N/A[traceability report;Dashboard boundary authority;no Dashboard feature;independent task-ID and gap-completeness review]
MCP: N/A[traceability report;MCP architecture authority;no MCP tool;independent task-ID and gap-completeness review]
Auth: Accountable-owner assignment and independent-review authority.
AT: Planned artifact: trace matrix task-ID and gap-completeness independent-review receipt; Work contract: `P0-07`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-07-requirement-traceability.md`
Runbook: gap
Risk: A normative requirement lacks a complete later-work mapping.
N/A: gap
Work: `P0-07`

### REQ-P0-03-ATOMIC-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board`
RequirementID: `REQ-P0-03-ATOMIC-01`
RequirementText: P0-03, after P0-01, owns only `TerraScale.Orchestrator/docs/retirement/workaround-ledger.yaml` and `TerraScale.Orchestrator/docs/evidence/phase0/runtime-build-descriptor-inventory.yaml`; each WRK item has source anchor, retained semantic behavior, native replacement gate, removal phase, owner, and regression scenario, and legacy CI/Auth/Flux claims are resolved without making historical behavior production contract.
ContentLocator: | P0-03 | **Descriptor inventory and retired-workaround ledger.** Coordinator: Cross-repository cleanup lane. Owns only `TerraScale.Orchestrator/docs/retirement/workaround-ledger.yaml` and `TerraScale.Orchestrator/docs/evidence/phase0/runtime-build-descriptor-inventory.yaml`. | P0-01 | None | Each `WRK-*` item has source anchor, retained semantic behavior, native replacement gate, removal phase, owner, and regression scenario; descriptor inventory resolves legacy CI/Auth/Flux claims without treating historical behavior as a production contract. |
Owner: Cross-repository cleanup lane
Life: gap
REST: N/A[retirement ledger;API architecture authority;no public REST contract;P0-03 receipt]
Stream: N/A[retirement ledger;API architecture authority;no public streaming contract;P0-03 receipt]
.NET: N/A[retirement ledger;SDK architecture authority;no SDK surface;P0-03 receipt]
TS: N/A[retirement ledger;SDK architecture authority;no SDK surface;P0-03 receipt]
Dashboard: N/A[retirement ledger;Dashboard boundary authority;no Dashboard feature;P0-03 receipt]
MCP: N/A[retirement ledger;MCP architecture authority;no MCP tool;P0-03 receipt]
Auth: None.
AT: Planned artifact: descriptor and workaround retirement-ledger receipt; Work contract: `P0-03`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Historical workaround becomes a production promise.
N/A: gap
Work: `P0-03`

### REQ-P0-04A-ATOMIC-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board`
RequirementID: `REQ-P0-04A-ATOMIC-01`
RequirementText: P0-04A, after P0-01, owns only `TerraScale.Orchestrator/docs/evidence/phase0/provider-tco-inputs.yaml`; using public pricing and read-only billing data where available, it produces a normalized provider comparison, an eligible-region matrix with at least 20 qualified rows or a documented failed claim, without entering an ARM64 lab or producing a performance baseline.
ContentLocator: | P0-04A | **Public provider/TCO and region research.** Coordinator: Cloud research lane. Owns only `TerraScale.Orchestrator/docs/evidence/phase0/provider-tco-inputs.yaml`. | P0-01 | Public pricing sources and read-only billing data where available. | Normalized provider comparison; eligible-region matrix with at least 20 qualified rows or a documented failed claim. This task does not enter an ARM64 lab or produce a performance baseline. |
Owner: Cloud research lane
Life: gap
REST: N/A[provider research;API architecture authority;no public REST contract;P0-04A receipt]
Stream: N/A[provider research;API architecture authority;no public streaming contract;P0-04A receipt]
.NET: N/A[provider research;SDK architecture authority;no SDK surface;P0-04A receipt]
TS: N/A[provider research;SDK architecture authority;no SDK surface;P0-04A receipt]
Dashboard: N/A[provider research;Dashboard boundary authority;no Dashboard feature;P0-04A receipt]
MCP: N/A[provider research;MCP architecture authority;no MCP tool;P0-04A receipt]
Auth: Public pricing sources and read-only billing authority.
AT: Planned artifact: price and region comparison receipt with source date and currency; Work contract: `P0-04A`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Unsupported provider, region, or cost claim.
N/A: gap
Work: `P0-04A`

### REQ-P0-04B-ATOMIC-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board`
RequirementID: `REQ-P0-04B-ATOMIC-01`
RequirementText: P0-04B owns only `TerraBase.Benchmark/docs/phase0/arm64-storage-baseline.manifest.json` and `TerraBase.Benchmark/docs/phase0/arm64-storage-baseline.md`; with positively owned isolated target and exclusive CPU partition, capture raw ARM64 database/block-storage p50/p95/p99, fsync, IOPS, expansion, and recovery data with approved target identity, methodology, and timestamp, excluding the non-exclusive 2026-07-27 self-test.
ContentLocator: | P0-04B | **ARM64/TerraBase storage benchmark inputs.** Coordinator: Benchmark lane. Owns only `TerraBase.Benchmark/docs/phase0/arm64-storage-baseline.manifest.json` and `TerraBase.Benchmark/docs/phase0/arm64-storage-baseline.md`. | Approved lab target | A positively owned isolated lab target and exclusive CPU partition. | Raw ARM64 database/block-storage p50/p95/p99, fsync, IOPS, expansion, and recovery data captured with the approved target identity, methodology, and timestamp. The non-exclusive 2026-07-27 self-test is excluded from baseline evidence. |
Owner: Benchmark lane
Life: gap
REST: N/A[ARM64 benchmark input;API architecture authority;no public REST contract;P0-04B receipt]
Stream: N/A[ARM64 benchmark input;API architecture authority;no public streaming contract;P0-04B receipt]
.NET: N/A[ARM64 benchmark input;SDK architecture authority;no SDK surface;P0-04B receipt]
TS: N/A[ARM64 benchmark input;SDK architecture authority;no SDK surface;P0-04B receipt]
Dashboard: N/A[ARM64 benchmark input;Dashboard boundary authority;no Dashboard feature;P0-04B receipt]
MCP: N/A[ARM64 benchmark input;MCP architecture authority;no MCP tool;P0-04B receipt]
Auth: Positively owned lab and exclusive CPU authority.
AT: Planned artifact: ARM64 benchmark manifest with target identity, CPU isolation, method, timestamp, and digest receipt; Work contract: `P0-04B`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Non-exclusive self-test is accepted as a baseline.
N/A: gap
Work: `P0-04B`

### REQ-P0-05-ATOMIC-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board`
RequirementID: `REQ-P0-05-ATOMIC-01`
RequirementText: P0-05, after P0-01, P0-03, P0-04A, and P0-04B, owns only `TerraScale.Orchestrator/docs/adr/0001-global-regional-authority.md`, `docs/adr/0002-dual-regional-nats.md`, `docs/adr/0003-jetstream-correctness.md`, `docs/adr/0006-workload-runtime-contract.md`, `docs/adr/0008-compact-profile.md`, `docs/adr/0011-pki-workload-identity.md`, `docs/adr/0012-vault-backend.md`, `docs/adr/0016-vpn-connectivity.md`, `docs/adr/0018-placement-boundary.md`, `docs/adr/0019-cost-slo-portability.md`, and `docs/evidence/phase0/slo-and-risk-acceptance.md` within TerraScale.Orchestrator; approved values bind NATS durability, storage, PKI/Vault, host, provider, and regional-survival choices, and every ADR states authority, failure policy, fencing/one-writer implications, rejected alternatives, and residual risk.
ContentLocator: `| P0-05 | **Measurable SLO approval and ADR tranche.** Coordinator: Integration/contract steward.`
Owner: Integration/contract steward
Life: gap
REST: N/A[SLO and ADR approval;API architecture authority;no public REST contract;P0-05 receipt]
Stream: N/A[SLO and ADR approval;API architecture authority;no public streaming contract;P0-05 receipt]
.NET: N/A[SLO and ADR approval;SDK architecture authority;no SDK surface;P0-05 receipt]
TS: N/A[SLO and ADR approval;SDK architecture authority;no SDK surface;P0-05 receipt]
Dashboard: N/A[SLO and ADR approval;Dashboard boundary authority;no Dashboard feature;P0-05 receipt]
MCP: N/A[SLO and ADR approval;MCP architecture authority;no MCP tool;P0-05 receipt]
Auth: Product, operations, security, and legal authority for cost, storage percentiles, RPO/RTO, retention, token TTL, density, survival window, and public commitments.
AT: Planned artifact: ADR and SLO numeric-target approval receipt; Work contract: `P0-05`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Runtime controls use unapproved SLO or residual-risk policy.
N/A: gap
Work: `P0-05`

### REQ-P0-06-ATOMIC-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board`
RequirementID: `REQ-P0-06-ATOMIC-01`
RequirementText: P0-06, after P0-05, owns only `TerraScale.Orchestrator/Directory.Packages.props`, `TerraScale.Orchestrator/global.json`, `TerraScale.Orchestrator/docs/adr/0014-ci-supply-chain.md`, `TerraScale.Orchestrator/docs/adr/0022-host-image-self-upgrade.md`, and `TerraScale.Orchestrator/docs/evidence/phase0/toolchain-and-rf1-lab-attestation.md`; CI/Forgejo administration, isolated signing identity, and local lab access establish immutable tool/image/artifact-mirror pins, SBOM/signing, NATS N/N-1, filesystem candidates, and repeatable rootless RF=1 conformance. Credentials cannot issue without exact-tree signed evidence, and this is not R3 or production qualification.
ContentLocator: `| P0-06 | **Credential-gated evidence tooling and bounded RF=1 lab qualification.** Coordinator: Verification lane.`
Owner: Verification lane
Life: gap
REST: N/A[RF=1 lab qualification;API architecture authority;no public REST contract;P0-06 receipt]
Stream: N/A[RF=1 lab qualification;API architecture authority;no public streaming contract;P0-06 receipt]
.NET: N/A[RF=1 lab qualification;SDK architecture authority;no SDK surface;P0-06 receipt]
TS: N/A[RF=1 lab qualification;SDK architecture authority;no SDK surface;P0-06 receipt]
Dashboard: N/A[RF=1 lab qualification;Dashboard boundary authority;no Dashboard feature;P0-06 receipt]
MCP: N/A[RF=1 lab qualification;MCP architecture authority;no MCP tool;P0-06 receipt]
Auth: CI/Forgejo administrator and isolated signing-identity authority; local lab only.
AT: Planned artifact: toolchain attestation with exact-tree provenance and RF=1 receipt; Work contract: `P0-06`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Credentials issue without signed evidence or RF=1 is represented as production.
N/A: gap
Work: `P0-06`

### REQ-P0-08-ATOMIC-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board`
RequirementID: `REQ-P0-08-ATOMIC-01`
RequirementText: P0-08, after P0-07, owns only `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-08-platform-openapi-inventory.md`; Platform and Documentation OpenAPI paths are read-only. With API architecture stewardship, it inventories versioned `/api/v1` method/path/schema/auth/idempotency/sensitivity/tenant scope, establishes Platform canonical provenance, excludes public MagicOnion/gRPC/internal-RPC, and resolves or owns the 149-versus-147 route discrepancy.
ContentLocator: `| P0-08 | **Authoritative public-contract inventory and snapshot provenance.** Coordinator: Platform-contract investigator.`
Owner: Platform-contract investigator
Life: gap
REST: gap
Stream: N/A[contract inventory;API architecture steward;no newly selected public stream;P0-08 inventory receipt]
.NET: N/A[contract inventory;SDK architecture authority;read-only SDK input;P0-08 inventory receipt]
TS: N/A[contract inventory;SDK architecture authority;read-only SDK input;P0-08 inventory receipt]
Dashboard: N/A[contract inventory;Dashboard boundary authority;no Dashboard feature;P0-08 inventory receipt]
MCP: N/A[contract inventory;MCP architecture authority;no MCP tool;P0-08 inventory receipt]
Auth: API architecture steward.
AT: Planned artifact: public-contract inventory and private-transport exclusion receipt; Work contract: `P0-08`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-08-platform-openapi-inventory.md`
Runbook: gap
Risk: Public contract drift or internal RPC exposure.
N/A: gap
Work: `P0-08`

### REQ-P0-09-ATOMIC-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board`
RequirementID: `REQ-P0-09-ATOMIC-01`
RequirementText: P0-09, after P0-08, owns only `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-09-sdk-contract-classification.md`; .NET, TypeScript, and manifests are read-only. Under SDK architecture authority, classify each public operation as .NET supported, TypeScript supported, intentionally unsupported, or gap, with reason, typed serialization/manifest mapping, success/failure/cross-tenant evidence, safe alternative, and express .NET organization/invitation/audit/admin-scope decision.
ContentLocator: `| P0-09 | **SDK support classification and parity evidence.** Coordinator: SDK-classification investigator.`
Owner: SDK-classification investigator
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: N/A[SDK classification;Dashboard boundary authority;no Dashboard feature;P0-09 classification receipt]
MCP: N/A[SDK classification;MCP architecture authority;no MCP tool;P0-09 classification receipt]
Auth: SDK architecture decision authority.
AT: Planned artifact: OpenAPI and typed SDK success, failure, cross-tenant, and safe-alternative receipt; Work contract: `P0-09`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-09-sdk-contract-classification.md`
Runbook: gap
Risk: Unsupported operation is represented as SDK parity.
N/A: gap
Work: `P0-09`

### REQ-P0-10-ATOMIC-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board`
RequirementID: `REQ-P0-10-ATOMIC-01`
RequirementText: P0-10, after P0-08 and P0-09, owns only `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-10-dashboard-mcp-boundary-proof.md`; Dashboard, Platform, and MCP sources/tests/manifests are read-only. Product security authority requires each Dashboard action map to public API, typed SDK, and MCP tool/resource/prompt or safe alternative, explicit sensitivity/scope/confirmation/idempotency/E2E evidence, static proof of no direct TerraScale/raw fetch/generic SDK/private route/direct TerraBase/MagicOnion use, and live AppHost representative read/mutation/two-tenant denial.
ContentLocator: `| P0-10 | **MCP safety/capability and Dashboard external-consumer proof.** Coordinator: Boundary/MCP investigator.`
Owner: Boundary/MCP investigator
Life: gap
REST: gap
Stream: gap
.NET: gap
TS: gap
Dashboard: gap
MCP: gap
Auth: Product security owner for mutation and confirmation policy.
AT: Planned artifact: static boundary and live AppHost two-tenant receipt; Work contract: `P0-10`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-10-dashboard-mcp-boundary-proof.md`
Runbook: gap
Risk: Dashboard bypass or unsafe MCP mutation.
N/A: gap
Work: `P0-10`

### REQ-P0-11-ATOMIC-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board`
RequirementID: `REQ-P0-11-ATOMIC-01`
RequirementText: P0-11, after P0-08 through P0-10, owns only `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-11-public-claim-governance.md`; documentation, landing, and claim-validator source are read-only. Product/commercial/legal approvers require every public claim link capability ID, exact evidence/commit, owner, review date, lifecycle state, and approval; Alpha versus production marketing, provider/metering claims, unsupported security assertions, and stale contacts are corrected or blocked before promotion.
ContentLocator: `| P0-11 | **Capability/status and documentation-claim governance.** Coordinator: Documentation-claims investigator.`
Owner: Documentation-claims investigator
Life: gap
REST: N/A[claim governance;API architecture authority;no public REST contract;P0-11 receipt]
Stream: N/A[claim governance;API architecture authority;no public streaming contract;P0-11 receipt]
.NET: N/A[claim governance;SDK architecture authority;no SDK surface;P0-11 receipt]
TS: N/A[claim governance;SDK architecture authority;no SDK surface;P0-11 receipt]
Dashboard: N/A[claim governance;Dashboard boundary authority;no Dashboard feature;P0-11 receipt]
MCP: N/A[claim governance;MCP architecture authority;no MCP tool;P0-11 receipt]
Auth: Product, commercial, and legal approvers for commitment claims.
AT: Planned artifact: claim register capability, evidence, owner, review-date, lifecycle, and approval receipt; Work contract: `P0-11`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-11-public-claim-governance.md`
Runbook: gap
Risk: Unapproved public commitment.
N/A: gap
Work: `P0-11`

### REQ-P0-12-ATOMIC-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board`
RequirementID: `REQ-P0-12-ATOMIC-01`
RequirementText: P0-12, after accepted P0-01, P0-01V, P0-03, P0-04A, P0-04B, and P0-05 through P0-11, owns only `TerraScale.Orchestrator/docs/planning/phase-work-package-schema.json`, `TerraScale.Orchestrator/docs/planning/phase-work-package-register.yaml`, `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-12-work-package-register-validation.md`, and `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/README.md`; fail closed on missing task/owner/scope/prerequisite/risk/real-boundary validation/exit evidence, cycles after closure-evidence separation, invalid controlling-input expansion, unleased writable overlap, or cross-repository item without owners/order/compatibility; final index uses immutable accepted reports and no parallel mutable matrix.
ContentLocator: `| P0-12 | **Register and validate every later-phase work package.** Coordinator: Root integration coordinator.`
Owner: Root integration coordinator
Life: gap
REST: N/A[work-package validation;API architecture authority;no public REST contract;P0-12 receipt]
Stream: N/A[work-package validation;API architecture authority;no public streaming contract;P0-12 receipt]
.NET: N/A[work-package validation;SDK architecture authority;no SDK surface;P0-12 receipt]
TS: N/A[work-package validation;SDK architecture authority;no SDK surface;P0-12 receipt]
Dashboard: N/A[work-package validation;Dashboard boundary authority;no Dashboard feature;P0-12 receipt]
MCP: N/A[work-package validation;MCP architecture authority;no MCP tool;P0-12 receipt]
Auth: None.
AT: Planned artifact: trace matrix independent review, fail-closed validation, and immutable-index receipt; Work contract: `P0-12`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-12-work-package-register-validation.md`
Runbook: gap
Risk: Later phase starts with missing, cyclic, overlapping, or incompatible work.
N/A: gap
Work: `P0-12`

### REQ-P0-RECEIPT-RULE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board > #### Phase 0 Report and Cross-Repository Integration Receipts`
RequirementID: `REQ-P0-RECEIPT-RULE-01`
RequirementText: Give every control-board task an exclusive Markdown report and, where evidence is in another repository, validate and commit evidence first, then the Documentation report with exact commit/digest, commands, methodology/version inputs, residual risk, and compatibility result; never substitute a report for evidence.
ContentLocator: `Every control-board task has an exclusive Markdown report. For any task that changes an evidence file in one repository and its report in Documentation, the evidence-repository commit is reviewed and validated first; the report is committed second and records the exact commit/digest, command results, methodology/version inputs, residual risk, and compatibility result. The report must not be created as a substitute for the underlying evidence.`
Owner: Product integration lead
Life: gap
REST: N/A[Phase 0 integration receipt;API architecture authority;no public REST contract;independent report review]
Stream: N/A[Phase 0 integration receipt;API architecture authority;no public streaming contract;independent report review]
.NET: N/A[Phase 0 integration receipt;SDK architecture authority;no SDK surface;independent report review]
TS: N/A[Phase 0 integration receipt;SDK architecture authority;no SDK surface;independent report review]
Dashboard: N/A[Phase 0 integration receipt;Dashboard boundary authority;no Dashboard feature;independent report review]
MCP: N/A[Phase 0 integration receipt;MCP architecture authority;no MCP tool;independent report review]
Auth: Exclusive report-path lease and repository reviewer.
AT: Planned artifact: trace matrix independent review, fail-closed validation, and immutable-index receipt; Work contract: `P0-12`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: Documentation reports obscure unreviewed underlying evidence.
N/A: gap
Work: `P0-12`

### REQ-P0-RECEIPT-SCHEDULE-01

SourceAnchor: `G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board > #### Phase 0 Report and Cross-Repository Integration Receipts`
RequirementID: `REQ-P0-RECEIPT-SCHEDULE-01`
RequirementText: Enforce the P0-01V draft/final rerun, P0-01 acceptance prerequisites, P0-03 scheduling, P0-07 parallelism, P0-04A/P0-04B lab prerequisites, P0-05 decision freeze, P0-08 through P0-11 dependencies, P0-12 acceptance prerequisites, and final P0 completion conditions.
ContentLocator: `P0-01V may begin once P0-01 has a draft packet/index, but it must rerun and pass against the exact final P0-01 commit digests before P0-01 is accepted. The coordinator may schedule P0-03 only after accepted P0-01, and P0-07 in parallel. P0-04A may run after P0-01; P0-05 is the control-plane decision freeze; P0-08 through P0-11 begin only after their stated contract dependencies; P0-12 begins only after P0-01, P0-01V, P0-03, P0-04A, P0-04B, and P0-05 through P0-11 are accepted. P0 does not complete until every control-board item is independently reviewed and every remaining requirement has a validated later-phase task, exact ownership, dependency, risk disposition, integration sequence, compatibility evidence, and acceptance evidence.`
Owner: Root integration coordinator
Life: gap
REST: N/A[Phase 0 scheduling;API architecture authority;no public REST contract;independent P0 completion review]
Stream: N/A[Phase 0 scheduling;API architecture authority;no public streaming contract;independent P0 completion review]
.NET: N/A[Phase 0 scheduling;SDK architecture authority;no SDK surface;independent P0 completion review]
TS: N/A[Phase 0 scheduling;SDK architecture authority;no SDK surface;independent P0 completion review]
Dashboard: N/A[Phase 0 scheduling;Dashboard boundary authority;no Dashboard feature;independent P0 completion review]
MCP: N/A[Phase 0 scheduling;MCP architecture authority;no MCP tool;independent P0 completion review]
Auth: Root coordination and independent-review authority.
AT: Planned artifact: trace matrix independent review, fail-closed validation, and immutable-index receipt; Work contract: `P0-12`; Evidence: gap.
Evidence: gap
Claim: gap
Docs: gap
Runbook: gap
Risk: P0 work begins or completes out of dependency order.
N/A: gap
Work: `P0-12`

## Scenario-pack coverage aid

Status: non-governing navigation and coverage aid. Each cell is an index to an AT token plus `Evidence:gap`; it does not impose a scenario dimension, acceptance threshold, or applicability decision. The governing records alone determine whether a scenario dimension is required or is `N/A[story;approving-authority;safe-alternative;validation-evidence]`.

Exactly nine source-named governing packs have authority: Account and security, Organization and membership, Onboarding and first value, Projects, products, and access, Database resilience, Monitoring and alerts, Billing and usage, Administration and compliance, and AI-agent and SDK parity. Additional internal rows are non-governing operational aids and cannot add, replace, relax, or conflict with a source-pack requirement or its governing semantic record.

| Pack | POS | AUTH-DENY | X-TENANT | RETRY | PARTIAL | AUDIT | NOTICE | A11Y | API-SDK | DASH | MCP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Account and security | AT-SP01.POS; Evidence:gap | AT-SP01.AUTH-DENY; Evidence:gap | AT-SP01.X-TENANT; Evidence:gap | AT-SP01.RETRY; Evidence:gap | AT-SP01.PARTIAL; Evidence:gap | AT-SP01.AUDIT; Evidence:gap | AT-SP01.NOTICE; Evidence:gap | AT-SP01.A11Y; Evidence:gap | AT-SP01.API-SDK; Evidence:gap | AT-SP01.DASH; Evidence:gap | AT-SP01.MCP; Evidence:gap |
| Organization and membership | AT-SP02.POS; Evidence:gap | AT-SP02.AUTH-DENY; Evidence:gap | AT-SP02.X-TENANT; Evidence:gap | AT-SP02.RETRY; Evidence:gap | AT-SP02.PARTIAL; Evidence:gap | AT-SP02.AUDIT; Evidence:gap | AT-SP02.NOTICE; Evidence:gap | AT-SP02.A11Y; Evidence:gap | AT-SP02.API-SDK; Evidence:gap | AT-SP02.DASH; Evidence:gap | AT-SP02.MCP; Evidence:gap |
| Onboarding and first value | AT-SP03.POS; Evidence:gap | AT-SP03.AUTH-DENY; Evidence:gap | AT-SP03.X-TENANT; Evidence:gap | AT-SP03.RETRY; Evidence:gap | AT-SP03.PARTIAL; Evidence:gap | AT-SP03.AUDIT; Evidence:gap | AT-SP03.NOTICE; Evidence:gap | AT-SP03.A11Y; Evidence:gap | AT-SP03.API-SDK; Evidence:gap | AT-SP03.DASH; Evidence:gap | AT-SP03.MCP; Evidence:gap |
| Projects, products, and access | AT-SP04.POS; Evidence:gap | AT-SP04.AUTH-DENY; Evidence:gap | AT-SP04.X-TENANT; Evidence:gap | AT-SP04.RETRY; Evidence:gap | AT-SP04.PARTIAL; Evidence:gap | AT-SP04.AUDIT; Evidence:gap | AT-SP04.NOTICE; Evidence:gap | AT-SP04.A11Y; Evidence:gap | AT-SP04.API-SDK; Evidence:gap | AT-SP04.DASH; Evidence:gap | AT-SP04.MCP; Evidence:gap |
| Non-governing operational aid: Database product | AT-SP04.POS; Evidence:gap | AT-SP04.AUTH-DENY; Evidence:gap | AT-SP04.X-TENANT; Evidence:gap | AT-SP04.RETRY; Evidence:gap | N/A[database product lifecycle;API architecture authority;approved partial-result behavior is evaluated per selected public operation;real-boundary scenario evidence] | AT-SP04.AUDIT; Evidence:gap | N/A[database product lifecycle;product authority;no universal customer notice contract;real-boundary scenario evidence] | N/A[database product lifecycle;accessibility authority;no universal user-interface contract;real-boundary scenario evidence] | AT-SP04.API-SDK; Evidence:gap | AT-SP04.DASH; Evidence:gap | AT-SP04.MCP; Evidence:gap |
| Database resilience | AT-SP05.POS; Evidence:gap | AT-SP05.AUTH-DENY; Evidence:gap | AT-SP05.X-TENANT; Evidence:gap | AT-SP05.RETRY; Evidence:gap | AT-SP05.PARTIAL; Evidence:gap | AT-SP05.AUDIT; Evidence:gap | AT-SP05.NOTICE; Evidence:gap | AT-SP05.A11Y; Evidence:gap | AT-SP05.API-SDK; Evidence:gap | AT-SP05.DASH; Evidence:gap | AT-SP05.MCP; Evidence:gap |
| Non-governing operational aid: Database resilience semantic binding | AT-SP05.POS; Evidence:gap | AT-SP05.AUTH-DENY; Evidence:gap | AT-SP05.X-TENANT; Evidence:gap | AT-SP05.RETRY; Evidence:gap | AT-SP05.PARTIAL; Evidence:gap | AT-SP05.AUDIT; Evidence:gap | N/A[recovery control;operations authority;customer notice is operation-specific;real-boundary scenario evidence] | N/A[recovery control;accessibility authority;no standalone user-interface contract;real-boundary scenario evidence] | AT-SP05.API-SDK; Evidence:gap | AT-SP05.DASH; Evidence:gap | AT-SP05.MCP; Evidence:gap |
| Non-governing operational aid: Dashboard monitoring, alerts, and operations | AT-SP06.POS; Evidence:gap | AT-SP06.AUTH-DENY; Evidence:gap | AT-SP06.X-TENANT; Evidence:gap | AT-SP06.RETRY; Evidence:gap | AT-SP06.PARTIAL; Evidence:gap | AT-SP06.AUDIT; Evidence:gap | AT-SP06.NOTICE; Evidence:gap | AT-SP06.A11Y; Evidence:gap | AT-SP06.API-SDK; Evidence:gap | AT-SP06.DASH; Evidence:gap | AT-SP06.MCP; Evidence:gap |
| Monitoring and alerts | AT-SP06.POS; Evidence:gap | AT-SP06.AUTH-DENY; Evidence:gap | AT-SP06.X-TENANT; Evidence:gap | AT-SP06.RETRY; Evidence:gap | AT-SP06.PARTIAL; Evidence:gap | AT-SP06.AUDIT; Evidence:gap | AT-SP06.NOTICE; Evidence:gap | AT-SP06.A11Y; Evidence:gap | AT-SP06.API-SDK; Evidence:gap | AT-SP06.DASH; Evidence:gap | AT-SP06.MCP; Evidence:gap |
| Non-governing operational aid: Billing and usage semantic binding | AT-SP07.POS; Evidence:gap | AT-SP07.AUTH-DENY; Evidence:gap | AT-SP07.X-TENANT; Evidence:gap | AT-SP07.RETRY; Evidence:gap | AT-SP07.PARTIAL; Evidence:gap | AT-SP07.AUDIT; Evidence:gap | AT-SP07.NOTICE; Evidence:gap | AT-SP07.A11Y; Evidence:gap | AT-SP07.API-SDK; Evidence:gap | AT-SP07.DASH; Evidence:gap | AT-SP07.MCP; Evidence:gap |
| Administration and compliance | AT-SP08.POS; Evidence:gap | AT-SP08.AUTH-DENY; Evidence:gap | AT-SP08.X-TENANT; Evidence:gap | AT-SP08.RETRY; Evidence:gap | AT-SP08.PARTIAL; Evidence:gap | AT-SP08.AUDIT; Evidence:gap | AT-SP08.NOTICE; Evidence:gap | AT-SP08.A11Y; Evidence:gap | AT-SP08.API-SDK; Evidence:gap | AT-SP08.DASH; Evidence:gap | AT-SP08.MCP; Evidence:gap |
| AI-agent and SDK parity | AT-SP09.POS; Evidence:gap | AT-SP09.AUTH-DENY; Evidence:gap | AT-SP09.X-TENANT; Evidence:gap | AT-SP09.RETRY; Evidence:gap | AT-SP09.PARTIAL; Evidence:gap | AT-SP09.AUDIT; Evidence:gap | AT-SP09.NOTICE; Evidence:gap | AT-SP09.A11Y; Evidence:gap | AT-SP09.API-SDK; Evidence:gap | AT-SP09.DASH; Evidence:gap | AT-SP09.MCP; Evidence:gap |

## Work contracts

Every `gap` above delegates only to one of these stable work IDs. Each item must retain its target phase, allowed and prohibited paths, predecessor evidence, dependencies, objective, non-goals, risk, external authority, validation artifact and threshold, migration or rollback or recovery need, and independent verifier.

### P0 work contracts

The three contracts below are the resolvable targets for every `Work: P0-01`, `Work: P0-01V`, and `Work: P0-03` record in this report, including `REQ-P0-01`, `REQ-P0-01V`, `REQ-P0-03`, and their scoped Control Board atoms. They are source-grounded in `REQ-P0-01-OWNERSHIP-01`, `REQ-P0-01-EXIT-01`, `REQ-P0-01V-VALIDATOR-01`, `REQ-P0-01V-INVARIANTS-01`, `REQ-P0-01V-REJECTIONS-01`, `REQ-P0-03-ATOMIC-01`, and `REQ-P0-RECEIPT-RULE-01`. The underlying Goal locator for the task and receipt clauses is the real heading chain `# TerraScale Production DBaaS Goal > ## Critical-Path Delivery Roadmap > ### Phase 0 Control Board > #### Phase 0 Report and Cross-Repository Integration Receipts`; that heading text is represented structurally here and is not a synthetic heading ID. These are open work contracts, not acceptance evidence.

#### Contract P0-01

ContractID: `P0-01`

Target phase: `P0`

Objective: Normalize the decision register so its dated decision/status map separates accepted topology policy from open numeric targets, every normative requirement resolves to owner, ADR/decision, executable dependency, closure evidence, and evidence location, and the readiness index does not contradict the evidence guide.

Non-goals: Do not edit ADR prose or evidence summaries. Do not reopen accepted policy decisions without authority.

Per-repository owners and exact allowed paths: TerraScale.Orchestrator, Integration/contract steward, only `TerraScale.Orchestrator/docs/decisions/owner-decision-packet.json` and `TerraScale.Orchestrator/docs/adr/readiness-index.yaml`; Terrascale.Documentation, Integration/contract steward, only `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-01-decision-register.md`.

Prohibited paths: ADR prose, evidence summaries, and every path other than the three allowed paths.

Exclusive path lease, predecessor evidence, executable dependencies, and integration order: The coordinator grants an exclusive path lease only after the owning-repository rules are read and its `develop` checkout is refreshed. The Control Board declares no predecessor. Executable dependencies are none, while closure evidence remains separately classified; P0-01's required executable prerequisite graph must be acyclic. Commit and validate the Orchestrator decision-register paths first, then commit the Documentation report.

Authority and risk: Named product, operations, and security owners supply unresolved measurable inputs. Accepted policy remains closed without authority. Risks are an unresolved controlling decision, unauthorised decision rewrite, and source-scope expansion.

Validation artifact and threshold: The committed packet and readiness index are the artifact. The threshold is a dated map with the stated policy/target separation; every normative requirement has owner, ADR/decision, dependency, and evidence location; the index and evidence guide do not contradict; the executable graph is acyclic after closure-evidence separation; every controlling input resolves to an atomic packet ID or a recursively non-empty, duplicate-free existing atomic-ID alias with no cycle or self-reference; and accepted owner policy is not marked pending. Before P0-01 can be accepted, P0-01V reruns against the exact final packet/index commit digests and records a matching result.

Recovery or rollback: No separate rollback or recovery procedure is specified for P0-01 in the Control Board. This remains `gap`; the required final exact-digest P0-01V rerun is a fail-closed validation boundary, not recovery evidence.

Compatibility receipt: The P0-01 report verifies owner and ADR identifiers against the exact committed index and records the required exact commit or digest, command results, methodology/version inputs, residual risk, and compatibility result.

Independent verifier: P0-01V, through its matching final-digest rerun, followed by the independent report review required before P0-12 import.

#### Contract P0-01V

ContractID: `P0-01V`

Target phase: `P0`

Objective: Implement and run the fail-closed decision/readiness invariant validator against current P0-01 data, then rerun it against P0-01's exact final packet/index commit digests before P0-01 acceptance.

Non-goals: Do not modify the P0-01 packet or readiness index. Do not accept stale-digest validation or a malformed, cyclic, or untraceable controlling input.

Per-repository owners and exact allowed paths: TerraScale.Orchestrator, Verification lane, only `TerraScale.Orchestrator/tools/TerraScale.Orchestrator.Tooling/TranslatedCommands.cs` and `TerraScale.Orchestrator/tools/TerraScale.Orchestrator.Tooling/ToolingTests.cs`; Terrascale.Documentation, Verification lane, only `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-01v-decision-readiness-validator.md`.

Prohibited paths: The P0-01 packet/index are read-only, and every path other than the two tooling files and the report is prohibited.

Exclusive path lease, predecessor evidence, executable dependencies, and integration order: The coordinator grants an exclusive path lease only after the owning-repository rules are read and its `develop` checkout is refreshed. The predecessor is a draft P0-01 packet/index. The executable dependency is P0-01; the validator must reject dependency cycles and preserve the distinction between executable prerequisites and closure evidence. Commit tooling implementation and tests first, rerun on P0-01's exact final packet/index digests, then commit the Documentation report.

Authority and risk: No external authority is required. The verification lane has a verification lease and read-only P0-01 access. Risks are validator mutation of its input, stale-digest verification, invalid readiness metadata appearing valid, and a malformed, cyclic, or untraceable controlling input passing validation.

Validation artifact and threshold: The fail-closed command, tooling tests, current P0-01 data, final-digest rerun result, and adversarial negative fixtures are the artifact. The threshold enforces mandatory cardinality and fields for every normative decision/readiness entry, declared allowed status, owner, decision/ADR, executable dependency, closure evidence, evidence location, and source anchor; resolves every readiness dependency and controlling input; distinguishes executable prerequisites from closure evidence; and rejects unknown, duplicate, empty, cyclic, and self-referential aliases, dependency cycles, malformed or missing fields, and invalid status, owner, decision, ADR, dependency, evidence, and source-anchor references. A current positive result, every listed adversarial failure, and a matching final-digest result are all required.

Recovery or rollback: No separate rollback or recovery procedure is specified for P0-01V in the Control Board. This remains `gap`; fail-closed rejection and rerun on exact final P0-01 digests are validation requirements, not recovery evidence.

Compatibility receipt: The P0-01V report records the matching final P0-01 digest, positive command result, and the adversarial unknown, duplicate, empty, cycle, self-reference, dependency-cycle, malformed/missing status/owner/decision/ADR/dependency/evidence/source-anchor failure results.

Independent verifier: The independent report review required before P0-12 import. P0-01V itself is the independent verifier for P0-01 and is not self-verification for this contract.

#### Contract P0-03

ContractID: `P0-03`

Target phase: `P0`

Objective: Produce the descriptor inventory and retired-workaround ledger, resolving legacy CI/Auth/Flux claims without making historical behavior a production contract.

Non-goals: Do not treat historical behavior as a production contract. Do not omit a required `WRK-*` source anchor, retained semantic behavior, native replacement gate, removal phase, owner, or regression scenario.

Per-repository owners and exact allowed paths: TerraScale.Orchestrator, Cross-repository cleanup lane, only `TerraScale.Orchestrator/docs/retirement/workaround-ledger.yaml` and `TerraScale.Orchestrator/docs/evidence/phase0/runtime-build-descriptor-inventory.yaml`; Terrascale.Documentation, Cross-repository cleanup lane, only `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-03-descriptor-and-retirement-ledger.md`.

Prohibited paths: Every path other than the two Orchestrator paths and the report.

Exclusive path lease, predecessor evidence, executable dependencies, and integration order: The coordinator grants an exclusive path lease only after the owning-repository rules are read and its `develop` checkout is refreshed. P0-01 is the predecessor. Its exact predecessor evidence or ADR identifier is `gap`, because the Control Board names only P0-01 at planning time. The sole executable dependency is P0-01, and no closure evidence is an executable prerequisite, so the dependency is acyclic if P0-01's required acyclic graph is retained. Commit and validate the Orchestrator ledger/inventory first, then commit the Documentation report.

Authority and risk: No external authority is required. The risk is a retired workaround or historical descriptor becoming a production promise.

Validation artifact and threshold: The workaround ledger and runtime/build descriptor inventory are the artifact. The threshold is that every `WRK-*` item has a source anchor, retained semantic behavior, native replacement gate, removal phase, owner, and regression scenario, while the descriptor inventory resolves legacy CI/Auth/Flux claims without elevating historical behavior into a production contract.

Recovery or rollback: Native replacement gate, removal phase, and regression scenario are required per `WRK-*` item. No separate rollback or recovery procedure is specified in the Control Board; this remains `gap`.

Compatibility receipt: The P0-03 report verifies every `WRK-*` source anchor and native replacement gate and records the required exact commit or digest, command results, methodology/version inputs, residual risk, and compatibility result.

Independent verifier: Independent report review before P0-12 import.

#### Contract P0-04A

ContractID: `P0-04A`

Target phase: `P0`

Objective: Produce a normalized public provider comparison, an eligible-region matrix with at least 20 qualified rows or a documented failed claim.

Non-goals: Do not enter an ARM64 lab or produce a performance baseline.

Per-repository owners and exact allowed paths: TerraScale.Orchestrator, Cloud research lane, only `TerraScale.Orchestrator/docs/evidence/phase0/provider-tco-inputs.yaml`; Terrascale.Documentation, Cloud research lane, only `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-04a-provider-tco-and-region-research.md`.

Prohibited paths: ARM64 lab and performance-baseline paths, and every path other than the Orchestrator path and the report.

Exclusive path lease, predecessor evidence, executable dependencies, and integration order: The coordinator grants an exclusive path lease only after the owning-repository rules are read and its `develop` checkout is refreshed. P0-01 is the predecessor. Its exact predecessor evidence or ADR identifier is `gap`, because the Control Board names only P0-01 at planning time. The sole executable dependency is P0-01, and no closure evidence is an executable prerequisite, so the dependency is acyclic if P0-01's required acyclic graph is retained. P0-04A may run after P0-01. Commit and validate the Orchestrator research first, then commit the Documentation report.

Authority and risk: Public pricing sources and read-only billing data where available are required. The risk is an unsupported provider, region, or cost claim.

Validation artifact and threshold: `provider-tco-inputs.yaml` and the report are the artifact. The threshold is a normalized provider comparison, an eligible-region matrix with at least 20 qualified rows or a documented failed claim, and report verification of price-source date/currency and region-qualification criteria.

Recovery or rollback: No separate rollback or recovery procedure is specified in the Control Board. This remains `gap`; this research contract does not authorize an ARM64 lab or a performance baseline.

Compatibility receipt: The P0-04A report verifies price-source date/currency and region-qualification criteria and records the required exact commit or digest, command results, methodology/version inputs, residual risk, and compatibility result.

Independent verifier: Independent report review before P0-12 import.

#### Contract P0-04B

ContractID: `P0-04B`

Target phase: `P0`

Objective: Capture raw ARM64 database and block-storage p50/p95/p99, fsync, IOPS, expansion, and recovery data using the approved target identity, methodology, and timestamp.

Non-goals: Do not use the non-exclusive 2026-07-27 self-test as baseline evidence.

Per-repository owners and exact allowed paths: TerraBase.Benchmark, Benchmark lane, only `TerraBase.Benchmark/docs/phase0/arm64-storage-baseline.manifest.json` and `TerraBase.Benchmark/docs/phase0/arm64-storage-baseline.md`; Terrascale.Documentation, Benchmark lane, only `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-04b-arm64-storage-benchmark.md`.

Prohibited paths: The non-exclusive 2026-07-27 self-test as baseline evidence, and every path other than the two TerraBase.Benchmark paths and the report.

Exclusive path lease, predecessor evidence, executable dependencies, and integration order: The coordinator grants an exclusive path lease only after the owning-repository rules are read and its `develop` checkout is refreshed. Required evidence is a positively owned, isolated, approved lab target identity with exclusive CPU partition. Commit and validate the TerraBase.Benchmark manifest/result first, then commit the Documentation report; before linking repositories, the report verifies target identity, timestamp, CPU-isolation attestation, workload/methodology version, and result digest.

Authority and risk: A positively owned isolated lab target and exclusive CPU partition are required. The risk is that a non-exclusive self-test is accepted as a baseline.

Validation artifact and threshold: The ARM64 storage-baseline manifest, baseline report, and Documentation receipt are the artifact. The threshold is raw database and block-storage p50/p95/p99, fsync, IOPS, expansion, and recovery data with the approved target identity, methodology, and timestamp, plus the receipt's target identity, timestamp, CPU-isolation, workload/methodology-version, and result-digest verification.

Recovery or rollback: Recovery data is a required captured measurement. No separate rollback or recovery procedure is specified for P0-04B in the Control Board; this remains `gap`.

Compatibility receipt: The P0-04B report verifies the approved lab target identity, timestamp, CPU-isolation attestation, workload/methodology version, and result digest before linking TerraBase.Benchmark and Documentation, and records the required exact commit or digest, command results, methodology/version inputs, residual risk, and compatibility result.

Independent verifier: Independent report review before P0-12 import.

#### Contract P0-05

ContractID: `P0-05`

Target phase: `P0`

Objective: Freeze measurable SLO decisions and the ADR tranche so approved values bind NATS durability, storage, PKI/Vault, host, provider, and regional-survival choices.

Non-goals: Do not use unapproved SLO or residual-risk policy. Do not omit an ADR's authority, failure policy, fencing or one-writer implications, rejected alternatives, or residual risk.

Per-repository owners and exact allowed paths: TerraScale.Orchestrator, Integration/contract steward, only `TerraScale.Orchestrator/docs/adr/0001-global-regional-authority.md`, `TerraScale.Orchestrator/docs/adr/0002-dual-regional-nats.md`, `TerraScale.Orchestrator/docs/adr/0003-jetstream-correctness.md`, `TerraScale.Orchestrator/docs/adr/0006-workload-runtime-contract.md`, `TerraScale.Orchestrator/docs/adr/0008-compact-profile.md`, `TerraScale.Orchestrator/docs/adr/0011-pki-workload-identity.md`, `TerraScale.Orchestrator/docs/adr/0012-vault-backend.md`, `TerraScale.Orchestrator/docs/adr/0016-vpn-connectivity.md`, `TerraScale.Orchestrator/docs/adr/0018-placement-boundary.md`, `TerraScale.Orchestrator/docs/adr/0019-cost-slo-portability.md`, and `TerraScale.Orchestrator/docs/evidence/phase0/slo-and-risk-acceptance.md`; Terrascale.Documentation, Integration/contract steward, only `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-05-slo-and-adr-acceptance.md`.

Prohibited paths: Every path other than the eleven Orchestrator paths and the report.

Exclusive path lease, predecessor evidence, executable dependencies, and integration order: The coordinator grants an exclusive path lease only after the owning-repository rules are read and its `develop` checkout is refreshed. P0-01, P0-03, P0-04A, and P0-04B are predecessors. Their exact predecessor evidence or ADR identifiers are `gap`, because the Control Board names task IDs at planning time. The executable dependencies are exactly those four P0 tasks, with closure evidence separately classified; P0-05 is the control-plane decision freeze and is acyclic when those predecessors retain their stated acyclic dependency conditions. Commit and validate the Orchestrator ADR/evidence paths first, then commit the Documentation report.

Authority and risk: Product, operations, security, and legal authority is required for pre-user cost, storage percentiles, RPO/RTO, retention, token TTL, density, survival window, and public commitments. The risk is runtime controls using unapproved SLO or residual-risk policy.

Validation artifact and threshold: The ten ADRs, SLO and risk-acceptance evidence, and report are the artifact. The threshold is approved values that bind the named NATS, storage, PKI/Vault, host, provider, and regional-survival choices; every ADR contains authority, failure policy, fencing/one-writer implications, alternatives rejected, and residual risk; and the report verifies every approved numeric target and authority/risk-acceptance reference.

Recovery or rollback: Each ADR must state failure policy and fencing or one-writer implications. No separate rollback or recovery procedure is specified in the Control Board; this remains `gap`.

Compatibility receipt: The P0-05 report verifies every approved numeric target and authority/risk-acceptance reference and records the required exact commit or digest, command results, methodology/version inputs, residual risk, and compatibility result.

Independent verifier: Independent report review before P0-12 import.

#### Contract P0-06

ContractID: `P0-06`

Target phase: `P0`

Objective: Qualify credential-gated evidence tooling and a bounded local, rootless RF=1 lab with immutable tool, image, and artifact-mirror pins, SBOM/signing approach, NATS N/N-1, filesystem candidates, and repeatable conformance evidence.

Non-goals: This is not R3 or production qualification. Local RF=1 and development-lab wiring are not production evidence and do not satisfy the later production clean-room, soak, or DR proof requirement. Credentials cannot issue without exact-tree signed evidence.

Per-repository owners and exact allowed paths: TerraScale.Orchestrator, Verification lane, only `TerraScale.Orchestrator/Directory.Packages.props`, `TerraScale.Orchestrator/global.json`, `TerraScale.Orchestrator/docs/adr/0014-ci-supply-chain.md`, `TerraScale.Orchestrator/docs/adr/0022-host-image-self-upgrade.md`, and `TerraScale.Orchestrator/docs/evidence/phase0/toolchain-and-rf1-lab-attestation.md`; Terrascale.Documentation, Verification lane, only `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-06-toolchain-and-rf1-attestation.md`.

Prohibited paths: R3 or production-qualification claims, credential issuance without exact-tree signed evidence, and every path other than the five Orchestrator paths and the report.

Exclusive path lease, predecessor evidence, executable dependencies, and integration order: The coordinator grants an exclusive path lease only after the owning-repository rules are read and its `develop` checkout is refreshed. P0-05 is the predecessor and control-plane decision freeze. Its exact predecessor evidence or ADR identifier is `gap`, because the Control Board names only P0-05 at planning time. The sole executable dependency is P0-05, with closure evidence separately classified, so the dependency is acyclic if P0-05 retains its stated acyclic predecessor conditions. Commit and validate the Orchestrator pins, ADRs, and evidence first, then commit the Documentation report.

Authority and risk: CI/Forgejo administrator and isolated signing-identity authority are required, with local lab access only. The risk is credentials issuing without signed evidence or RF=1 being represented as production.

Validation artifact and threshold: `Directory.Packages.props`, `global.json`, the two ADRs, the toolchain/RF=1 attestation, and the report are the artifact. The threshold is immutable tool/image/artifact-mirror pins, SBOM/signing approach, NATS N/N-1, filesystem candidates, repeatable rootless RF=1 conformance, no credential issuance absent exact-tree signed evidence, exact-tree provenance verification, and an explicit local-RF=1-only label in the report.

Recovery or rollback: No separate rollback or recovery procedure is specified for P0-06 in the Control Board. This remains `gap`; the credential-issuance gate and nonproduction label are safety and validation requirements, not recovery evidence.

Compatibility receipt: The P0-06 report verifies exact-tree provenance, explicitly labels the result local RF=1 only, and records the required exact commit or digest, command results, methodology/version inputs, residual risk, and compatibility result.

Independent verifier: Independent report review before P0-12 import.

| Work | Exact allowed path | Predecessor and order | Authority and objective exit evidence | Compatibility and independent verification |
| --- | --- | --- | --- | --- |
| P0-07 | `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-07-requirement-traceability.md` | No predecessor; exclusive Documentation lease; independent review before P0-12 import | Product integration lead; complete atomic matrix and later-work contracts | P0-12 records exact digest and task-ID/gap-completeness result; independent requirements reviewer |
| P0-08 | `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-08-platform-openapi-inventory.md` | P0-07 accepted; read-only Platform and Documentation inputs | API architecture steward; authoritative inventory and provenance comparison | P0-09 records exact P0-08 version and compatibility; independent API reviewer |
| P0-09 | `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-09-sdk-contract-classification.md` | P0-08 accepted; read-only SDK and manifest inputs | SDK architecture authority; operation classification and safe alternatives | P0-10 records P0-09 version; independent SDK reviewer |
| P0-10 | `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-10-dashboard-mcp-boundary-proof.md` | P0-08 and P0-09 accepted; read-only source and tests | Product security owner; Dashboard and MCP external-consumer proof | P0-11 imports accepted references; independent boundary reviewer |
| P0-11 | `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-11-public-claim-governance.md` | P0-08 through P0-10 accepted | Product, commercial, legal approvers; capability claim register | Claim owner approvals and accepted-source reference; independent claims reviewer |
| P0-12 | `TerraScale.Orchestrator/docs/planning/phase-work-package-schema.json`, `TerraScale.Orchestrator/docs/planning/phase-work-package-register.yaml`, `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-12-work-package-register-validation.md`, `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/README.md` | All named P0 reports accepted; Orchestrator schema/register commit, validation report, Documentation index last | Root integration coordinator; fail closed on missing, cyclic, overlapping, or incompatible work | Register digest and immutable report links; independent register reviewer |

| Work | Target phase | Owner and exact allowed path | Prohibited paths | Lease and order | Compatibility receipt | Objective and non-goals | Dependencies, authority, risk | Validation and recovery | Independent verifier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0-07 | P0 | Product integration lead: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-07-requirement-traceability.md` | All other paths | Exclusive Documentation lease; no predecessor; independent review before P0-12 import | P0-12 records exact digest and task-ID/gap-completeness result | Complete atomic matrix and later-work contracts; not acceptance evidence | No predecessor; product integration authority; incomplete traceability risk | Independent task-ID and gap-completeness review receipt; recovery is `gap` | Independent requirements reviewer |
| P0-08 | P0 | API architecture steward: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-08-platform-openapi-inventory.md` | All other paths; Platform and Documentation inputs are read-only | Exclusive Documentation lease after accepted P0-07 receipt | P0-09 records exact P0-08 version and compatibility | Authoritative inventory and provenance comparison; not product implementation | P0-07 accepted; API architecture authority; provenance-drift risk | Inventory and provenance comparison receipt with exact P0-07 predecessor reference; recovery is `gap` | Independent API reviewer |
| P0-09 | P0 | SDK architecture authority: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-09-sdk-contract-classification.md` | All other paths; SDK and manifest inputs are read-only | Exclusive Documentation lease after accepted P0-08 receipt | P0-10 records exact P0-09 version | Operation classification and safe alternatives; not SDK implementation | P0-08 accepted; SDK architecture authority; classification-drift risk | Classification and safe-alternative receipt with exact P0-08 predecessor reference; recovery is `gap` | Independent SDK reviewer |
| P0-10 | P0 | Product security owner: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-10-dashboard-mcp-boundary-proof.md` | All other paths; source and tests are read-only | Exclusive Documentation lease after accepted P0-08 and P0-09 receipts | P0-11 imports accepted references | Dashboard and MCP external-consumer proof; not privileged bypass implementation | P0-08 and P0-09 accepted; product security authority; boundary-leakage risk | Static boundary and live AppHost two-tenant receipt with exact predecessor references; recovery is `gap` | Independent boundary reviewer |
| P0-11 | P0 | Product, commercial, and legal approvers: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-11-public-claim-governance.md` | All other paths | Exclusive Documentation lease after accepted P0-08 through P0-10 receipts | Claim owner approvals and accepted-source reference | Capability claim register; not unapproved public claim | P0-08 through P0-10 accepted; product, commercial, legal authority; misrepresentation risk | Claim owner approval and accepted-source receipt with exact predecessor references; recovery is `gap` | Independent claims reviewer |
| P0-12 | P0 | Root integration coordinator: `TerraScale.Orchestrator/docs/planning/phase-work-package-schema.json`, `TerraScale.Orchestrator/docs/planning/phase-work-package-register.yaml`, `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/p0-12-work-package-register-validation.md`, `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-0/README.md` | All other paths | All named P0 reports accepted; Orchestrator schema/register commit, validation report, Documentation index last | Register digest and immutable report links | Fail closed on missing, cyclic, overlapping, or incompatible work; not acceptance without validated records | All named P0 reports accepted; root integration authority; invalid work-register risk | Fail-closed register validation receipt and immutable-index threshold; recovery is `gap` | Independent register reviewer |
| FW-QUALITY-06 | P6 | Release-quality owner: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-6/fw-quality-06.md` | All other paths | Exclusive Documentation lease after P0-11 and FW-OBS-06 receipts | Release candidate records the documentation, quality, and evidence-gate result | Implement the evidence-quality, release-gate, and non-applicability controls; not product capability implementation | P0-11, FW-OBS-06, release authority; false-closure risk | Real-boundary evidence audit with failure and recovery results; release evidence rollback procedure | Independent release-quality reviewer |
| FW-ID-01 | P1 | Platform identity owner: `TerraScale.Internals/docs/planning/fw-id-01.md` | All other Internals paths | Exclusive lease after P0-08 and P0-09 receipts | Versioned auth-contract and SDK parity receipt | Identity, onboarding, passkeys, session/device, trusted IP; not a production claim | Contract decisions; security authority; takeover risk | Real two-user AppHost matrix; session revocation recovery | Independent security reviewer |
| FW-AUTH-01 | P1 | Platform authorization owner: `TerraScale.Internals/docs/planning/fw-auth-01.md` | All other Internals paths | Exclusive lease after FW-ID-01 predecessor receipt | RBAC and tenant-isolation receipt | Organizations, invitations, RBAC; not admin work | P0-08 and P0-09; product authority; escalation risk | Real two-organization denial matrix; immediate-revocation recovery | Independent authorization reviewer |
| FW-PROJ-02 | P2 | Platform projects owner: `TerraScale.Internals/docs/planning/fw-proj-02.md` | All other Internals paths | Exclusive lease after FW-AUTH-01 receipt | Region-model contract compatibility receipt | Project regions and access; not provider actuation | FW-AUTH-01 and P0-05; product authority; placement risk | Real project lifecycle E2E; region-change rollback | Independent product reviewer |
| FW-DB-PROVISION-02 | P2 | Platform database owner: `TerraScale.Internals/docs/planning/fw-db-provision-02-platform.md`; Orchestrator owner: `TerraScale.Orchestrator/docs/planning/fw-db-provision-02-runtime.md` | All other paths | Platform contract first, independent receipt, Orchestrator second | Versioned create/readiness/endpoint schema and real-stack receipt | Project-scoped creation, naming, placement-derived configuration, progress, readiness, endpoints, and safe removal; not recovery proof or raw secret return | FW-CONTRACT-01, FW-PROJ-02, P0-05, P0-06; product and security authority; placement and deletion risk | Two-tenant create-to-ready-to-remove E2E, idempotent retry, and removal recovery runbook | Independent data-plane reviewer |
| FW-DB-CREDENTIAL-02 | P2 | Platform database owner: `TerraScale.Internals/docs/planning/fw-db-credential-02-platform.md`; Orchestrator owner: `TerraScale.Orchestrator/docs/planning/fw-db-credential-02-runtime.md` | All other paths and every secret location | Platform credential contract first, security receipt, Orchestrator second | Redacted issuance/rotation schema and public-contract receipt | Credential issuance and rotation; not exposing raw secrets after the controlled creation response | FW-DB-PROVISION-02, P0-05, P0-06; security authority; credential compromise risk | Real issuance, rotation, revocation, cross-tenant denial, and secret-redaction evidence; credential-recovery runbook | Independent security reviewer |
| FW-DB-OPERATE-02 | P2 | Platform database owner: `TerraScale.Internals/docs/planning/fw-db-operate-02-platform.md`; Orchestrator owner: `TerraScale.Orchestrator/docs/planning/fw-db-operate-02-runtime.md` | All other paths | Platform operation contract first, independent receipt, Orchestrator second | Versioned status/event/change schema and real-stack receipt | Status, events, scaling, configuration, maintenance, quotas, and limits; not R3 resilience evidence | FW-DB-PROVISION-02, FW-CONTRACT-01, P0-05; product and operations authority; availability and capacity risk | Authorized change, retry, quota/limit, maintenance, and cross-tenant denial E2E; operation rollback runbook | Independent operations reviewer |
| FW-DB-RESILIENCE-03 | P3 | TerraBase recovery owner: `TerraBase/docs/planning/fw-db-resilience-03-engine.md`; Orchestrator owner: `TerraScale.Orchestrator/docs/planning/fw-db-resilience-03-runtime.md`; Documentation owner: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-3/fw-db-resilience-03-receipt.md` | All other paths | TerraBase evidence first, DR receipt, Orchestrator second, Documentation last | Measured restore and lifecycle-semantic digest | Backups, retention, drills, PITR, clone, branch, promotion, merge, deletion, and post-deletion retention; not an unsupported durability claim | FW-DB-02, P0-04B, P0-05, P0-06; cloud and security authority; data-loss risk | Destructive clean-room drill, authorized restore/clone/branch and deletion tests, measured RPO/RTO, cutover and rollback runbook | Independent DR reviewer |
| FW-DB-SECURITY-02 | P2 | Platform security owner: `TerraScale.Internals/docs/planning/fw-db-security-02-platform.md`; TerraBase owner: `TerraBase/docs/planning/fw-db-security-02-engine.md`; Orchestrator owner: `TerraScale.Orchestrator/docs/planning/fw-db-security-02-runtime.md` | All other paths and every secret location | Threat-model and data-plane control receipt before runtime integration | Authentication, authorization, tenancy, encryption, secret, abuse, idempotency, audit, and secure-default receipt | Data-plane and control-plane controls; not customer-visible feature expansion | FW-CONTRACT-01, P0-05, P0-06; security authority; data and abuse risk | Real authentication, cross-tenant denial, encryption, audit, retry, rate-limit, and failure-containment evidence; incident and key-recovery runbook | Independent security reviewer |
| FW-DB-CONTRACT-01 | P1 | Platform owner: `TerraScale.Internals/docs/planning/fw-db-contract-01-platform.md`; .NET owner: `TerraScale.DotNet/docs/planning/fw-db-contract-01-dotnet.md`; TypeScript owner: `TerraScale.TypeScript/docs/planning/fw-db-contract-01-typescript.md`; MCP owner: `TerraScale.Mcp/docs/planning/fw-db-contract-01-mcp.md` | Private routes, generic request APIs, direct TerraBase clients, Dashboard-only headers, and service-internal client shortcuts | Platform REST contract first, SDKs under separate leases, MCP last | Signed database-operation inventory, parity, and prohibited-bypass review | Public versioned REST and typed .NET/TypeScript parity with no listed bypass; not private transport exposure | P0-08, P0-09, FW-CONTRACT-01; API and security authority; boundary-drift risk | Per-operation REST/.NET/TypeScript/MCP parity, forbidden-surface static checks, and real tenant-denial evidence; compatible deprecation rollback | Independent API and boundary reviewer |
| FW-DB-DEVELOPER-02 | P2 | Developer experience owner: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-2/fw-db-developer-02.md`; Platform owner: `TerraScale.Internals/docs/planning/fw-db-developer-02-platform.md` | All other paths and every secret location | Platform workflow receipt first, Documentation last | Reproducible local/CI/integration/migration/upgrade/rollback/troubleshooting receipt | Clear customer and contributor workflows; not replacing operational recovery proof | FW-DB-CONTRACT-01, FW-DB-PROVISION-02; developer experience and security authority; unsafe guidance risk | Fresh-environment local and CI execution, integration path, migration/upgrade/rollback rehearsal, and sanitized troubleshooting evidence | Independent developer-experience reviewer |
| FW-DB-02 | P2 | Platform database owner: `TerraScale.Internals/docs/planning/fw-db-02-platform.md`; Orchestrator owner: `TerraScale.Orchestrator/docs/planning/fw-db-02-orchestrator.md`; TypeScript owner: `TerraScale.TypeScript/docs/planning/fw-db-02-sdk.md`; MCP owner: `TerraScale.Mcp/docs/planning/fw-db-02-mcp.md` | All other paths | Per-path exclusive leases. Platform first, independent contract receipt, Orchestrator second, TypeScript third, MCP last | Versioned lifecycle schema and real-stack API receipt | Managed database, queues, Authentication product; not R3 production | FW-CONTRACT-01, FW-PROJ-02, P0-05, P0-06; product and security authority; data and secret risk | Create, use, rotate, delete, queue DLQ and Auth isolation; idempotent migration and recovery | Independent data-plane reviewer |
| FW-RUNTIME-03 | P3 | Orchestrator runtime owner: `TerraScale.Orchestrator/docs/planning/fw-runtime-03.md`; Documentation receipt owner: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-3/fw-runtime-03-receipt.md` | All other paths; retired infrastructure stubs; local RF=1 or development-lab results presented as production evidence; every secret location | Exclusive Orchestrator lease after P0-05 and P0-06 receipts; runtime-closure evidence first, Documentation receipt last | R3 runtime-foundation inventory revalidation and readiness-audit closure digest | Revalidate the substantial Orchestrator foundation and close the stated R3 runtime-readiness audit; not P0, product, or production acceptance, and not local-lab qualification | P0-05 and P0-06; cloud, security, and operations authority; runtime, credential, and recovery risk | Real R3 controllers/NATS, PKI/KMS/Vault/JWT lifecycle, host/volume execution, TerraBase topology/certificate/backup control, private ingress/DNS/VPN, HA observability, OIDC/RBAC/audit, native GitOps rollback, provenance, staged rollout, and clean-room/soak/DR evidence; recovery is `gap` until the required runtime rollback and DR proof are recorded | Independent runtime, security, and DR reviewer |
| FW-REC-03 | P3 | TerraBase recovery owner: `TerraBase/docs/planning/fw-rec-03-engine.md`; Orchestrator owner: `TerraScale.Orchestrator/docs/planning/fw-rec-03-runtime.md`; Documentation owner: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-3/fw-rec-03-receipt.md` | All other paths | TerraBase evidence first, DR receipt, Orchestrator second, Documentation last | Measured RPO/RTO and restore-schema digest | Recovery proof, not unsupported semantic claim | FW-DB-02, P0-04B, P0-05, P0-06; cloud and security authority; loss risk | Destructive R3 clean-room drill; cutover and rollback runbook | Independent DR reviewer |
| FW-CONTRACT-01 | P1 | Platform owner: `TerraScale.Internals/docs/planning/fw-contract-01-platform.md`; .NET owner: `TerraScale.DotNet/docs/planning/fw-contract-01-dotnet.md`; TypeScript owner: `TerraScale.TypeScript/docs/planning/fw-contract-01-typescript.md`; MCP owner: `TerraScale.Mcp/docs/planning/fw-contract-01-mcp.md` | All other paths | Platform first, then .NET and TypeScript under separate leases, MCP last | Signed operation inventory and version-diff review | Classify public contracts, not feature code | P0-08 and P0-09; API authority; drift risk | Every operation classified for REST, Stream, auth, tenant, idempotency, compatibility; deprecation rollback | Independent API reviewer |
| FW-BILL-04 | P4 | Platform owner: `TerraScale.Internals/docs/planning/fw-bill-04-platform.md`; Dashboard owner: `TerraScale.Internals/docs/planning/fw-bill-04-dashboard.md`; Documentation owner: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-4/fw-bill-04-receipt.md` | All other paths and every secret location | Platform first, finance-security receipt, Dashboard successor lease, Documentation last | Redacted Polar event and reconciliation digest | Sandbox billing, not live claim | FW-CONTRACT-01 and authorized secret import; Polar, finance, legal authority; financial and secret risk | All SP07 tests and reconciliation; ledger replay rollback | Independent finance-security reviewer |
| FW-ADMIN-04 | P4 | Platform Admin owner: `TerraScale.Internals/docs/planning/fw-admin-04.md` | All other paths | Exclusive lease after FW-AUTH-01 receipt | OIDC, RBAC, break-glass and audit receipt | Separate administration, not customer-membership extension | FW-AUTH-01; security and operations authority; staff-abuse risk | Real operator authorization and revocation test; break-glass recovery | Independent security reviewer |
| FW-MCP-05 | P5 | Platform owner: `TerraScale.Internals/docs/planning/fw-mcp-05-platform.md`; .NET owner: `TerraScale.DotNet/docs/planning/fw-mcp-05-sdk.md`; MCP owner: `TerraScale.Mcp/docs/planning/fw-mcp-05-adapter.md` | All other paths | Platform public contract first, .NET second, MCP third | Tool-to-operation parity and tenant-denial receipt | Safe agent tiers, not generic, direct, or internal tools | FW-CONTRACT-01 and approved mutation design; security authority; agent-harm risk | Full metadata and real denial evidence; two-step retry and recovery | Independent MCP reviewer |
| FW-DASH-06 | P6 | Dashboard owner: `TerraScale.Internals/src/Dashboard/TerraScale.Dashboard.Next/**`; Platform boundary owner: `TerraScale.Internals/src/Platform/**`; Documentation owner: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-6/fw-dash-06-receipt.md` | Dashboard code outside the Dashboard root; Dashboard-specific Platform feature/route/DTO/service/option/auth/notification/business logic; direct browser TerraScale calls; raw or generic SDK access | Public contract and typed SDK receipt first, Dashboard and Platform boundary leases second, Documentation last | Typed-SDK-only boundary, same-origin browser boundary, tenant-safe monitoring UX, and prohibited-surface review | Dashboard external-consumer and monitoring UX work, not a privileged Dashboard capability or a Platform Dashboard feature | P0-08, P0-09, P0-10, FW-CONTRACT-01, FW-OBS-06; product, API, security, accessibility, and operations authority; tenant, privacy, and usability risk | Real AppHost customer success, authorization denial, two-tenant isolation, same-origin, accessibility, empty/loading/error, metric-unit/reference-period, and partial-data evidence; rollback removes Dashboard changes and restores compatible public contracts | Independent Dashboard boundary and accessibility reviewer |
| FW-OBS-06 | P6 | Orchestrator observability owner: `TerraScale.Orchestrator/docs/planning/fw-obs-06-runtime.md`; Platform telemetry owner: `TerraScale.Internals/docs/planning/fw-obs-06-platform.md`; Dashboard owner: `TerraScale.Internals/docs/planning/fw-obs-06-dashboard.md`; Documentation owner: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-6/fw-obs-06-receipt.md` | All other paths | Orchestrator metric and SLO contract first, independent SRE receipt, Platform second, Dashboard successor exclusive lease third, Documentation last | Bounded-cardinality schema, tenant-redaction review, alert and partial-source-degradation receipt | HA telemetry and alerts, not arbitrary labels or internal-error exposure | P0-05 and FW-RUNTIME-03; operations and security authority; privacy, cost, outage risk | Soak, alert escalation, partial-source degradation, SLI/SLO/error-budget decision; alert rollback and incident recovery runbook | Independent SRE and privacy reviewer |
| FW-CLAIM-06 | P6 | Documentation claims owner: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-6/fw-claim-06.md` | All other paths | Exclusive Documentation lease after P0-11 | Claim registry, drift, localization receipt | Claim governance, not unapproved legal text | P0-11; legal and commercial authority; misrepresentation risk | Source-backed claim review; content rollback | Independent legal and documentation reviewer |
| FW-SEC-06 | P6 | Security engineering owner: `TerraScale.Orchestrator/docs/planning/fw-sec-06.md`; Documentation receipt owner: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-6/fw-sec-06-receipt.md` | All other paths and every secret location | Security control receipt first, Documentation last | Threat-model, scan, SBOM/provenance, secret, patch, privacy, audit, and access-review digest | Security engineering controls, not a public security certification claim | P0-05, P0-06, FW-OBS-06; security, privacy, and release authority; compromise and compliance risk | Signed threat model; real SAST, DAST, dependency and container scan receipts; redacted secret-control proof; patch, privacy, audit, and access-review evidence; vulnerability-response and secret-recovery runbooks | Independent security and privacy reviewer |
| FW-OPS-06 | P6 | SRE and runtime owner: `TerraScale.Orchestrator/docs/planning/fw-ops-06.md`; Documentation receipt owner: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-6/fw-ops-06-receipt.md` | All other paths | Approved SLO and failure-domain design first, measured scenario evidence second, Documentation last | HA, capacity, load/soak, chaos, recovery, incident, escalation, ownership, SLO/error-budget, and DR exercise digest | Production operability and resilience, not an unsupported availability or recovery claim | P0-05, P0-06, FW-OBS-06, FW-REC-03; operations and recovery authority; outage and data-loss risk | Production-like load/soak and chaos results, destructive recovery drill, SLO/error-budget decision, incident/escalation exercise, capacity review, and DR cutover/rollback runbooks | Independent SRE and DR reviewer |
| FW-DELIVERY-06 | P6 | Release engineering owner: `TerraScale.Orchestrator/docs/planning/fw-delivery-06.md`; Documentation receipt owner: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-6/fw-delivery-06-receipt.md` | Retired infrastructure stubs, unreviewed production mutation, and every secret location | Reproducible pipeline and environment-gate receipt first, Documentation last | Build, test, migration, deployment, progressive delivery, rollback, promotion, configuration, infrastructure-as-code, and artifact receipt | Reproducible delivery, not a production-control-plane replacement outside TerraScale.Orchestrator | P0-05, P0-06, FW-SEC-06; release, security, and operations authority; unsafe or irrecoverable release risk | Rebuilt artifact digest, real pipeline results, migration rehearsal, progressive-delivery and rollback exercise, promotion/configuration review, IaC plan/apply receipt, and release rollback runbook | Independent release and infrastructure reviewer |
| FW-ADR-06 | P6 | Architecture steward: `TerraScale.Orchestrator/docs/planning/fw-adr-06.md`; Documentation analysis owner: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-6/fw-adr-06-analysis.md` | Product implementation paths and unapproved provider adoption | Comparative source capture first, architecture review second, Documentation analysis last | ADR register and Vercel, Turso, and Neon pattern-analysis receipt with explicit fit decision | Architecture decision and relevant-pattern analysis, not vendor endorsement or automatic adoption | P0-04A, P0-05; product, architecture, compliance, security, and operations authority; architecture-mismatch risk | Source-cited analyses, ADR approval record, and fit assessment against TerraScale product, architecture, compliance, and operational constraints; reversal plan for rejected or reverted pattern | Independent architecture and compliance reviewer |
| FW-DOCS-06 | P6 | Documentation owner: `Terrascale.Documentation/docs/agentic-delivery/2026-08-05/phase-6/fw-docs-06.md` | All product implementation paths and every secret location | Accepted workflow and evidence receipts first, audience documentation last | Customer, SDK, API/MCP, operator, security, billing, support, on-call, recovery, release, and local-contributor documentation receipt | Audience-specific operational documentation, not evidence substitution or unapproved product claim | FW-SEC-06, FW-OPS-06, FW-DELIVERY-06, FW-ADR-06, P0-11; product, security, operations, support, billing, and legal authority; unsafe or misleading guidance risk | Fresh-reader task completion for each audience, redaction review, public-claim review, and recovery/release/support documentation exercises; documentation rollback procedure | Independent documentation and domain reviewers |
## Scoped atomic governing records

Status: open. These records are governing authority for the scoped source clauses. The broad objective record is a navigation pointer only. The separately replaced REQ-TRANSPORT-01 remains governing. This does not claim P0-07, product, or production acceptance.

### REQ-OBJ-SERVICE-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Objective

RequirementID: REQ-OBJ-SERVICE-01

RequirementText: Finish **TerraScale, powered by TerraBase**, as a production-ready Database-as-a-Service for human developers and AI agents.

ContentLocator: Finish **TerraScale, powered by TerraBase**, as a production-ready Database-as-a-Service for human developers and AI agents.

Owner: Integration

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: service-completeness acceptance ledger in `FW-QUALITY-06`; Work contract: `FW-QUALITY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Service scope.

N/A: gap

Work: FW-QUALITY-06

### REQ-OBJ-QUALITY-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Objective

RequirementID: REQ-OBJ-QUALITY-01

RequirementText: The delivered product must be cohesive, deployable, secure, observable, supportable, documented, and proven through real end-to-end and integration validation.

ContentLocator: The delivered product must be cohesive, deployable, secure, observable, supportable, documented, and proven through real end-to-end and integration validation.

Owner: Integration

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: cohesive-delivery evidence-quality gate in `FW-QUALITY-06`; Work contract: `FW-QUALITY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unproven delivery.

N/A: gap

Work: FW-QUALITY-06

### REQ-OBJ-NOT-MVP-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Objective

RequirementID: REQ-OBJ-NOT-MVP-01

RequirementText: This is not an MVP, demo, mock, or collection of disconnected feature slices.

ContentLocator: This is not an MVP, demo, mock, or collection of disconnected feature slices.

Owner: Integration

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: non-demo product-cohesion review in `FW-QUALITY-06`; Work contract: `FW-QUALITY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Non-production substitute.

N/A: gap

Work: FW-QUALITY-06

### REQ-DOD-E2E-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Definition of Done

RequirementID: REQ-DOD-E2E-01

RequirementText: Customer and operator workflows work end to end through supported public contracts, with robust authorization and tenant isolation.

ContentLocator: Customer and operator workflows work end to end through supported public contracts, with robust authorization and tenant isolation.

Owner: Platform

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: tenant-safe end-to-end boundary matrix in `FW-CONTRACT-01`; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unauthorized tenant access.

N/A: gap

Work: FW-CONTRACT-01

### REQ-DOD-DB-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Definition of Done

RequirementID: REQ-DOD-DB-01

RequirementText: Database lifecycle operations are reliable: provisioning, credentials, connection/access management, regions and high availability, branching, migrations where supported, backups, restore and point-in-time recovery, deletion, auditability, and operational visibility.

ContentLocator: Database lifecycle operations are reliable: provisioning, credentials, connection/access management, regions and high availability, branching, migrations where supported, backups, restore and point-in-time recovery, deletion, auditability, and operational visibility.

Owner: Database

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: managed-database lifecycle proof receipt in `FW-DB-RESILIENCE-03`; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Data lifecycle failure.

N/A: gap

Work: FW-DB-RESILIENCE-03

### REQ-DOD-DASH-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Definition of Done

RequirementID: REQ-DOD-DASH-01

RequirementText: The dashboard provides an excellent, accessible experience for people; all equivalent customer capabilities are available to AI agents through a documented, safe MCP server and/or typed public SDK APIs.

ContentLocator: The dashboard provides an excellent, accessible experience for people; all equivalent customer capabilities are available to AI agents through a documented, safe MCP server and/or typed public SDK APIs.

Owner: Dashboard and MCP

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Dashboard and MCP equivalent-access boundary receipt in `FW-DASH-06`; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Inaccessible or non-equivalent access.

N/A: gap

Work: FW-DASH-06

### REQ-DOD-WORKFLOW-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Definition of Done

RequirementID: REQ-DOD-WORKFLOW-01

RequirementText: Organization, project, identity, billing, usage, alerting, and administrative workflows conform to the requirements below, including role boundaries and failure paths.

ContentLocator: Organization, project, identity, billing, usage, alerting, and administrative workflows conform to the requirements below, including role boundaries and failure paths.

Owner: Platform

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: role-and-failure workflow authorization matrix in `FW-AUTH-01`; Work contract: `FW-AUTH-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Role and failure defects.

N/A: gap

Work: FW-AUTH-01

### REQ-DOD-POLAR-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Definition of Done

RequirementID: REQ-DOD-POLAR-01

RequirementText: Billing is integrated with Polar Sandbox and validated against real sandbox flows for subscriptions, metered usage, payment methods, failures, receipts, and webhooks.

ContentLocator: Billing is integrated with Polar Sandbox and validated against real sandbox flows for subscriptions, metered usage, payment methods, failures, receipts, and webhooks.

Owner: Billing

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar Sandbox billing reconciliation receipt in `FW-BILL-04`; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unvalidated billing.

N/A: gap

Work: FW-BILL-04

### REQ-DOD-SECRET-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Definition of Done

RequirementID: REQ-DOD-SECRET-01

RequirementText: Credentials are stored only in an approved secret manager or local ignored runtime-secret configuration; they must never be written to this file, source control, reports, logs, fixtures, or commits.

ContentLocator: Credentials are stored only in an approved secret manager or local ignored runtime-secret configuration; they must never be written to this file, source control, reports, logs, fixtures, or commits.

Owner: Security

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: credential and secret redaction control receipt in `FW-SEC-06`; Work contract: `FW-SEC-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Credential exposure.

N/A: gap

Work: FW-SEC-06

### REQ-DOD-ORCH-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Definition of Done

RequirementID: REQ-DOD-ORCH-01

RequirementText: The production control plane and GitOps/cluster lifecycle live exclusively in `TerraScale.Orchestrator`; retired `TerraScale.Infrastructure` and `Terrabase.Operator` are never used for production infrastructure.

ContentLocator: The production control plane and GitOps/cluster lifecycle live exclusively in `TerraScale.Orchestrator`; retired `TerraScale.Infrastructure` and `Terrabase.Operator` are never used for production infrastructure.

Owner: Orchestrator

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: native-Orchestrator production-control ownership review in `FW-DELIVERY-06`; Work contract: `FW-DELIVERY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Retired infrastructure path.

N/A: gap

Work: FW-DELIVERY-06

### REQ-DOD-GATE-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Definition of Done

RequirementID: REQ-DOD-GATE-01

RequirementText: Security, reliability, performance, capacity, disaster recovery, observability, CI/CD, release procedures, runbooks, documentation, SDKs, and developer experience meet a documented production gate.

ContentLocator: Security, reliability, performance, capacity, disaster recovery, observability, CI/CD, release procedures, runbooks, documentation, SDKs, and developer experience meet a documented production gate.

Owner: Release

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: production-gate decision ledger in `FW-QUALITY-06`; Work contract: `FW-QUALITY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: No production gate.

N/A: gap

Work: FW-QUALITY-06

### REQ-DOD-TEST-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Definition of Done

RequirementID: REQ-DOD-TEST-01

RequirementText: All required tests are green at appropriate real boundaries, meaningful coverage gaps are resolved, independent review findings are addressed, and no unresolved release blocker remains.

ContentLocator: All required tests are green at appropriate real boundaries, meaningful coverage gaps are resolved, independent review findings are addressed, and no unresolved release blocker remains.

Owner: Release

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: real-boundary validation closure report in `FW-QUALITY-06`; Work contract: `FW-QUALITY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Release blocker.

N/A: gap

Work: FW-QUALITY-06

### REQ-ARCH-DEVELOP-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Architecture and Repository Boundaries

RequirementID: REQ-ARCH-DEVELOP-01

RequirementText: Work is decomposed across the correct product repositories, with each change owned, tested, committed, and pushed separately on current `develop`:

ContentLocator: Work is decomposed across the correct product repositories, with each change owned, tested, committed, and pushed separately on current `develop`:

Owner: Integration

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: per-repository `develop` delivery ledger review, including owned paths, test results, commits, and push receipts, in `P0-12`; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unintegrated multi-repo work.

N/A: gap

Work: P0-12

### REQ-ARCH-ENGINE-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Architecture and Repository Boundaries

RequirementID: REQ-ARCH-ENGINE-01

RequirementText: | Database engine | `TerraBase/` |

ContentLocator: | Database engine | `TerraBase/` |

Owner: TerraBase

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: TerraBase repository-allocation review against the approved product-boundary inventory in `P0-12`; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Wrong repository.

N/A: gap

Work: P0-12

### REQ-ARCH-BENCH-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Architecture and Repository Boundaries

RequirementID: REQ-ARCH-BENCH-01

RequirementText: | Benchmarking and baselines | `TerraBase.Benchmark/` |

ContentLocator: | Benchmarking and baselines | `TerraBase.Benchmark/` |

Owner: Benchmark

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: TerraBase.Benchmark repository-allocation and baseline-ownership review in `P0-12`; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Wrong repository.

N/A: gap

Work: P0-12

### REQ-ARCH-ORCH-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Architecture and Repository Boundaries

RequirementID: REQ-ARCH-ORCH-01

RequirementText: | Production control plane, infra, delivery, host lifecycle, GitOps | `TerraScale.Orchestrator/` |

ContentLocator: | Production control plane, infra, delivery, host lifecycle, GitOps | `TerraScale.Orchestrator/` |

Owner: Orchestrator

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: sole-production-control-plane repository-allocation review for TerraScale.Orchestrator in `P0-12`; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Wrong repository.

N/A: gap

Work: P0-12

### REQ-ARCH-DEPLOY-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Architecture and Repository Boundaries

RequirementID: REQ-ARCH-DEPLOY-01

RequirementText: | Deploy CLI and image workflows | `TerraScale.Deploy/` |

ContentLocator: | Deploy CLI and image workflows | `TerraScale.Deploy/` |

Owner: Deploy

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Deploy CLI and image-workflow repository-allocation review in `P0-12`; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Wrong repository.

N/A: gap

Work: P0-12

### REQ-ARCH-DOTNET-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Architecture and Repository Boundaries

RequirementID: REQ-ARCH-DOTNET-01

RequirementText: | Public .NET SDK | `TerraScale.DotNet/` |

ContentLocator: | Public .NET SDK | `TerraScale.DotNet/` |

Owner: SDK

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: public .NET SDK repository-allocation review in `P0-12`; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Wrong repository.

N/A: gap

Work: P0-12

### REQ-ARCH-TS-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Architecture and Repository Boundaries

RequirementID: REQ-ARCH-TS-01

RequirementText: | Public TypeScript SDK | `TerraScale.TypeScript/` |

ContentLocator: | Public TypeScript SDK | `TerraScale.TypeScript/` |

Owner: SDK

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: public TypeScript SDK repository-allocation review in `P0-12`; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Wrong repository.

N/A: gap

Work: P0-12

### REQ-ARCH-INT-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Architecture and Repository Boundaries

RequirementID: REQ-ARCH-INT-01

RequirementText: | Platform, Dashboard, and AppHost | `TerraScale.Internals/` |

ContentLocator: | Platform, Dashboard, and AppHost | `TerraScale.Internals/` |

Owner: Platform

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Platform, Dashboard, and AppHost repository-allocation review for TerraScale.Internals in `P0-12`; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Wrong repository.

N/A: gap

Work: P0-12

### REQ-ARCH-MCP-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Architecture and Repository Boundaries

RequirementID: REQ-ARCH-MCP-01

RequirementText: | MCP product surface | `TerraScale.Mcp/` |

ContentLocator: | MCP product surface | `TerraScale.Mcp/` |

Owner: MCP

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: MCP product-surface repository-allocation review in `P0-12`; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Wrong repository.

N/A: gap

Work: P0-12

### REQ-ARCH-DEVHOST-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Architecture and Repository Boundaries

RequirementID: REQ-ARCH-DEVHOST-01

RequirementText: | Local developer supervision | `TerraScale.DevHost/` |

ContentLocator: | Local developer supervision | `TerraScale.DevHost/` |

Owner: DevHost

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: local developer-supervision repository-allocation review in `P0-12`; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Wrong repository.

N/A: gap

Work: P0-12

### REQ-ARCH-DOCS-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Architecture and Repository Boundaries

RequirementID: REQ-ARCH-DOCS-01

RequirementText: | Documentation and marketing | `Terrascale.Documentation/`, `Terrascale.Landingpage/` |

ContentLocator: | Documentation and marketing | `Terrascale.Documentation/`, `Terrascale.Landingpage/` |

Owner: Documentation

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: documentation and marketing repository-allocation review for the documentation and landing sites in `P0-12`; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Wrong repository.

N/A: gap

Work: P0-12

### REQ-ARCH-REFRESH-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Architecture and Repository Boundaries

RequirementID: REQ-ARCH-REFRESH-01

RequirementText: Before each repository write, refresh `develop` with `git fetch origin` and `git pull --ff-only origin develop`.

ContentLocator: Before each repository write, refresh `develop` with `git fetch origin` and `git pull --ff-only origin develop`.

Owner: Repository owner

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: pre-write `git fetch` and fast-forward `develop` refresh receipt for each affected repository in `P0-12`; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Stale checkout.

N/A: gap

Work: P0-12

### REQ-ARCH-RESTRICT-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Architecture and Repository Boundaries

RequirementID: REQ-ARCH-RESTRICT-01

RequirementText: Never treat the workspace root as a Git repository; never use `main` for ordinary delivery; never create branches or worktrees unless explicitly requested.

ContentLocator: Never treat the workspace root as a Git repository; never use `main` for ordinary delivery; never create branches or worktrees unless explicitly requested.

Owner: Repository owner

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: repository-root, branch, and worktree policy compliance review in `P0-12`; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Invalid workspace or branch.

N/A: gap

Work: P0-12

### REQ-ARCH-STAGE-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Architecture and Repository Boundaries

RequirementID: REQ-ARCH-STAGE-01

RequirementText: Use explicit path staging, make coherent commits, fetch again before pushing, and push each affected repository separately.

ContentLocator: Use explicit path staging, make coherent commits, fetch again before pushing, and push each affected repository separately.

Owner: Repository owner

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: explicit-path staging, final-fetch, per-repository commit, and push receipt review in `P0-12`; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unsafe staging or push.

N/A: gap

Work: P0-12

### REQ-ARCH-PRESERVE-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Architecture and Repository Boundaries

RequirementID: REQ-ARCH-PRESERVE-01

RequirementText: Preserve unrelated user work and never commit secrets.

ContentLocator: Preserve unrelated user work and never commit secrets.

Owner: Repository owner

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: unrelated-work preservation and secret-exclusion staging review in `P0-12`; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Loss of work or secret commit.

N/A: gap

Work: P0-12

### REQ-START-SNAPSHOT-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Verified Starting Point and Required Closures

RequirementID: REQ-START-SNAPSHOT-01

RequirementText: This section is a read-only inventory snapshot from 2026-08-05. It is deliberately evidence-based: existing code, tests, plans, or documentation are not proof that a customer-facing capability is production-ready. Every item below must be revalidated as work progresses.

ContentLocator: This section is a read-only inventory snapshot from 2026-08-05. It is deliberately evidence-based: existing code, tests, plans, or documentation are not proof that a customer-facing capability is production-ready. Every item below must be revalidated as work progresses.

Owner: Integration

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: dated starting-point inventory revalidation ledger, with each foundation item linked to its closure evidence, in `P0-12`; Work contract: `P0-12`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Foundation treated as acceptance.

N/A: gap

Work: P0-12

### REQ-START-ENGINE-F-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Verified Starting Point and Required Closures

RequirementID: REQ-START-ENGINE-F-01

RequirementText: A mature .NET 10 RavenDB-derived engine with clustered Rachis behavior, sharding, replication, periodic/incremental/snapshot backup and restore, encryption, certificate authorization, audit logging, and telemetry primitives. Evidence: `TerraBase/src/TerraBase.Server/`, `TerraBase/test/TerraBase.{SlowTests,RachisTests,StressTests,EndToEndTests}/`.

ContentLocator: A mature .NET 10 RavenDB-derived engine with clustered Rachis behavior, sharding, replication, periodic/incremental/snapshot backup and restore, encryption, certificate authorization, audit logging, and telemetry primitives. Evidence: `TerraBase/src/TerraBase.Server/`, `TerraBase/test/TerraBase.{SlowTests,RachisTests,StressTests,EndToEndTests}/`.

Owner: TerraBase

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: TerraBase engine-foundation source and test inventory revalidation receipt in `FW-DB-RESILIENCE-03`; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Foundation treated as acceptance.

N/A: gap

Work: FW-DB-RESILIENCE-03

### REQ-START-ENGINE-C-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Verified Starting Point and Required Closures

RequirementID: REQ-START-ENGINE-C-01

RequirementText: Convert engine primitives into a managed tenant-safe service: instance lifecycle state machine, routing, credential lifecycle, quota/isolation, supported branch/clone semantics, service-level backup/PITR policy, restore-to-new-instance/cutover, measured RPO/RTO, HA/failover/fencing/repair, customer-safe diagnostics, and recurring recovery evidence.

ContentLocator: Convert engine primitives into a managed tenant-safe service: instance lifecycle state machine, routing, credential lifecycle, quota/isolation, supported branch/clone semantics, service-level backup/PITR policy, restore-to-new-instance/cutover, measured RPO/RTO, HA/failover/fencing/repair, customer-safe diagnostics, and recurring recovery evidence.

Owner: TerraBase and Orchestrator

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: managed tenant-safe database lifecycle, recovery, HA, and diagnostics acceptance receipt in `FW-DB-RESILIENCE-03`; Work contract: `FW-DB-RESILIENCE-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Managed closure gap.

N/A: gap

Work: FW-DB-RESILIENCE-03

### REQ-START-BENCH-F-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Verified Starting Point and Required Closures

RequirementID: REQ-START-BENCH-F-01

RequirementText: `TerraBase.Benchmark/` has correctness, restart-durability, isolation-attestation, and statistics tooling.

ContentLocator: `TerraBase.Benchmark/` has correctness, restart-durability, isolation-attestation, and statistics tooling.

Owner: Benchmark

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: benchmark correctness, durability, isolation-attestation, and statistics-tooling revalidation receipt in `FW-OPS-06`; Work contract: `FW-OPS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Foundation treated as acceptance.

N/A: gap

Work: FW-OPS-06

### REQ-START-BENCH-C-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Verified Starting Point and Required Closures

RequirementID: REQ-START-BENCH-C-01

RequirementText: Establish exclusive benchmark capacity, approved standard/persistent/soak baselines, comparable regression gates, and load/capacity evidence. The 2026-07-27 canonical self-test is invalid because it lacked an exclusive CPU partition; it cannot support production performance claims.

ContentLocator: Establish exclusive benchmark capacity, approved standard/persistent/soak baselines, comparable regression gates, and load/capacity evidence. The 2026-07-27 canonical self-test is invalid because it lacked an exclusive CPU partition; it cannot support production performance claims.

Owner: Benchmark

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: exclusive-capacity benchmark baseline, regression-gate, and load-capacity review receipt in `FW-OPS-06`; Work contract: `FW-OPS-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Invalid performance proof.

N/A: gap

Work: FW-OPS-06

### REQ-START-ORCH-F-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Verified Starting Point and Required Closures

RequirementID: REQ-START-ORCH-F-01

RequirementText: `TerraScale.Orchestrator/` has substantial decision/control logic, NATS policy validation, planners, delivery journals, secret-store adapter, protocol tests, and a bounded local development lab.

ContentLocator: `TerraScale.Orchestrator/` has substantial decision/control logic, NATS policy validation, planners, delivery journals, secret-store adapter, protocol tests, and a bounded local development lab.

Owner: Orchestrator

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Orchestrator foundation inventory revalidation in `FW-RUNTIME-03`; Work contract: `FW-RUNTIME-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Foundation treated as acceptance.

N/A: gap

Work: FW-RUNTIME-03

### REQ-START-ORCH-C-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Verified Starting Point and Required Closures

RequirementID: REQ-START-ORCH-C-01

RequirementText: Close the production-readiness audit: real R3 controllers/NATS, PKI/KMS/Vault/JWT lifecycle, systemd/containerd host execution, volume/filesystem lifecycle, TerraBase topology/certificate/backup controllers, private ingress/DNS/VPN, HA observability, operator OIDC/RBAC/audit, native GitOps apply/drift/rollback, artifact provenance, staged live rollout, and clean-room/soak/DR proof. Development-lab wiring and local RF=1 are never production evidence.

ContentLocator: Close the production-readiness audit: real R3 controllers/NATS, PKI/KMS/Vault/JWT lifecycle, systemd/containerd host execution, volume/filesystem lifecycle, TerraBase topology/certificate/backup controllers, private ingress/DNS/VPN, HA observability, operator OIDC/RBAC/audit, native GitOps apply/drift/rollback, artifact provenance, staged live rollout, and clean-room/soak/DR proof. Development-lab wiring and local RF=1 are never production evidence.

Owner: Orchestrator

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: R3 runtime-readiness audit closure receipt in `FW-RUNTIME-03`; Work contract: `FW-RUNTIME-03`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Runtime closure gap.

N/A: gap

Work: FW-RUNTIME-03

### REQ-START-PLATFORM-F-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Verified Starting Point and Required Closures

RequirementID: REQ-START-PLATFORM-F-01

RequirementText: `TerraScale.Internals/` already has broad versioned Platform endpoints and a full-stack Dashboard for account/onboarding, organizations/projects/access, databases/environments, data, queues, backups/restores, monitoring, billing, notifications, profile security, and owner administration. It contains useful Dashboard and internal-RPC boundary guardrails.

ContentLocator: `TerraScale.Internals/` already has broad versioned Platform endpoints and a full-stack Dashboard for account/onboarding, organizations/projects/access, databases/environments, data, queues, backups/restores, monitoring, billing, notifications, profile security, and owner administration. It contains useful Dashboard and internal-RPC boundary guardrails.

Owner: Platform

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Platform and Dashboard endpoint, handler-boundary, and AppHost foundation revalidation receipt in `FW-DASH-06`; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Foundation treated as acceptance.

N/A: gap

Work: FW-DASH-06

### REQ-START-PLATFORM-C-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Verified Starting Point and Required Closures

RequirementID: REQ-START-PLATFORM-C-01

RequirementText: Prove every required story and privileged mutation on a real AppHost stack, including authorization and two-tenant isolation. Add typed-SDK-only structural enforcement for all Dashboard handlers, live public/internal RPC listener isolation and mTLS proof, bounded-cardinality telemetry, complete failure/retry/error UX, and production deployment evidence from the Orchestrator.

ContentLocator: Prove every required story and privileged mutation on a real AppHost stack, including authorization and two-tenant isolation. Add typed-SDK-only structural enforcement for all Dashboard handlers, live public/internal RPC listener isolation and mTLS proof, bounded-cardinality telemetry, complete failure/retry/error UX, and production deployment evidence from the Orchestrator.

Owner: Platform

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: real-AppHost privileged-mutation, two-tenant isolation, typed-SDK, RPC-isolation, telemetry, and failure-UX acceptance matrix in `FW-DASH-06`; Work contract: `FW-DASH-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Boundary closure gap.

N/A: gap

Work: FW-DASH-06

### REQ-START-SDK-F-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Verified Starting Point and Required Closures

RequirementID: REQ-START-SDK-F-01

RequirementText: TypeScript captures 149 typed routes and has an OpenAPI drift check; .NET provides typed public access to core database/project/queue/billing/backup/sync capabilities.

ContentLocator: TypeScript captures 149 typed routes and has an OpenAPI drift check; .NET provides typed public access to core database/project/queue/billing/backup/sync capabilities.

Owner: SDK

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: versioned OpenAPI inventory and existing .NET/TypeScript typed-SDK coverage revalidation receipt in `FW-CONTRACT-01`; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Foundation treated as acceptance.

N/A: gap

Work: FW-CONTRACT-01

### REQ-START-SDK-C-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Verified Starting Point and Required Closures

RequirementID: REQ-START-SDK-C-01

RequirementText: Make Platform OpenAPI the authoritative versioned inventory; verify .NET and TypeScript parity for every operation classified as SDK-supported, including account, organizations, invitations, access, onboarding, audit, pricing, and supported administration when the architecture decision admits them. Fix mutation idempotency for every non-safe verb, default-redact raw server error bodies, publish compatibility/deprecation policy, and require authenticated real success/failure/cross-tenant tests per operation.

ContentLocator: Make Platform OpenAPI the authoritative versioned inventory; verify .NET and TypeScript parity for every operation classified as SDK-supported, including account, organizations, invitations, access, onboarding, audit, pricing, and supported administration when the architecture decision admits them. Fix mutation idempotency for every non-safe verb, default-redact raw server error bodies, publish compatibility/deprecation policy, and require authenticated real success/failure/cross-tenant tests per operation.

Owner: SDK

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: authenticated per-operation SDK parity, idempotency, redaction, compatibility, and cross-tenant test matrix in `FW-CONTRACT-01`; Work contract: `FW-CONTRACT-01`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Contract closure gap.

N/A: gap

Work: FW-CONTRACT-01

### REQ-START-MCP-F-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Verified Starting Point and Required Closures

RequirementID: REQ-START-MCP-F-01

RequirementText: `TerraScale.Mcp/` currently offers 11 bounded, typed-SDK, read-only discovery/usage tools with redaction and stdio process tests.

ContentLocator: `TerraScale.Mcp/` currently offers 11 bounded, typed-SDK, read-only discovery/usage tools with redaction and stdio process tests.

Owner: MCP

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: bounded typed-SDK MCP discovery-tool and redaction process-test revalidation receipt in `FW-MCP-05`; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Foundation treated as acceptance.

N/A: gap

Work: FW-MCP-05

### REQ-START-MCP-C-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Verified Starting Point and Required Closures

RequirementID: REQ-START-MCP-C-01

RequirementText: Grow deliberately to full customer capability parity using public contracts only. First close .NET/contract gaps; then add sensitivity-classified, tenant-authorized tools with confirmation and idempotency for mutations. A repository-list read capability must first exist as a bounded typed public API and have tenant-isolation proof.

ContentLocator: Grow deliberately to full customer capability parity using public contracts only. First close .NET/contract gaps; then add sensitivity-classified, tenant-authorized tools with confirmation and idempotency for mutations. A repository-list read capability must first exist as a bounded typed public API and have tenant-isolation proof.

Owner: MCP

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: public-contract-only MCP capability-parity, authorization, confirmation, idempotency, and tenant-isolation acceptance receipt in `FW-MCP-05`; Work contract: `FW-MCP-05`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: MCP closure gap.

N/A: gap

Work: FW-MCP-05

### REQ-START-BILL-F-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Verified Starting Point and Required Closures

RequirementID: REQ-START-BILL-F-01

RequirementText: Platform and Dashboard contain pricing, checkout, portal, invoices, usage, and webhook surfaces.

ContentLocator: Platform and Dashboard contain pricing, checkout, portal, invoices, usage, and webhook surfaces.

Owner: Billing

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: billing surface inventory revalidation for pricing, checkout, portal, invoices, usage, and webhooks in `FW-BILL-04`; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Foundation treated as acceptance.

N/A: gap

Work: FW-BILL-04

### REQ-START-BILL-C-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Verified Starting Point and Required Closures

RequirementID: REQ-START-BILL-C-01

RequirementText: Complete Polar Sandbox lifecycle evidence, signed/idempotent webhook handling, entitlement/restriction behavior, metered usage export and reconciliation, payment failure/renewal/overage notifications, finance audit trail, real owner/non-owner tests, and documented commercial operations. Do not claim Stripe, metering, or live payment behavior until source-backed proof is current.

ContentLocator: Complete Polar Sandbox lifecycle evidence, signed/idempotent webhook handling, entitlement/restriction behavior, metered usage export and reconciliation, payment failure/renewal/overage notifications, finance audit trail, real owner/non-owner tests, and documented commercial operations. Do not claim Stripe, metering, or live payment behavior until source-backed proof is current.

Owner: Billing

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: Polar Sandbox lifecycle, signed webhook, entitlement, reconciliation, notification, finance-audit, and owner-authorization acceptance receipt in `FW-BILL-04`; Work contract: `FW-BILL-04`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Billing closure gap.

N/A: gap

Work: FW-BILL-04

### REQ-START-DOCS-F-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Verified Starting Point and Required Closures

RequirementID: REQ-START-DOCS-F-01

RequirementText: The documentation site includes localized API/SDK/auth/organization/MFA/backup/billing material and claim validators; the landing site has type/lint/e2e checks.

ContentLocator: The documentation site includes localized API/SDK/auth/organization/MFA/backup/billing material and claim validators; the landing site has type/lint/e2e checks.

Owner: Documentation

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: documentation localization, claim-validator, and landing-site type, lint, and E2E foundation revalidation receipt in `FW-CLAIM-06`; Work contract: `FW-CLAIM-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Foundation treated as acceptance.

N/A: gap

Work: FW-CLAIM-06

### REQ-START-DOCS-C-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Verified Starting Point and Required Closures

RequirementID: REQ-START-DOCS-C-01

RequirementText: Publish source-backed customer, agent, operator, recovery, security, billing, support, and release material. Create one capability/status registry for Dashboard, API, SDKs, MCP, docs, and landing claims. Resolve the current Public Alpha versus production-marketing contradiction before any production launch claim.

ContentLocator: Publish source-backed customer, agent, operator, recovery, security, billing, support, and release material. Create one capability/status registry for Dashboard, API, SDKs, MCP, docs, and landing claims. Resolve the current Public Alpha versus production-marketing contradiction before any production launch claim.

Owner: Documentation

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: source-backed capability/status registry and Public Alpha versus production-claim reconciliation review in `FW-CLAIM-06`; Work contract: `FW-CLAIM-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Claim closure gap.

N/A: gap

Work: FW-CLAIM-06

### REQ-CORR-STALE-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Known Documentation and Ownership Corrections

RequirementID: REQ-CORR-STALE-01

RequirementText: Reconcile TerraBase release/deployment documentation and metadata with `TerraScale.Orchestrator` as the sole production-infrastructure owner. `TerraBase/docs/release-automation.md` and `TerraBase/docker/readme.md` currently contain stale/incorrect ownership or workflow references; retired stubs must not re-enter the deployment path.

ContentLocator: Reconcile TerraBase release/deployment documentation and metadata with `TerraScale.Orchestrator` as the sole production-infrastructure owner. `TerraBase/docs/release-automation.md` and `TerraBase/docker/readme.md` currently contain stale/incorrect ownership or workflow references; retired stubs must not re-enter the deployment path.

Owner: Orchestrator and TerraBase

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: TerraBase release and Docker guidance correction review, confirming TerraScale.Orchestrator sole production-infrastructure ownership and retired-stub exclusion, in `FW-DELIVERY-06`; Work contract: `FW-DELIVERY-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Stale deployment guidance.

N/A: gap

Work: FW-DELIVERY-06

### REQ-CORR-CLAIM-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Known Documentation and Ownership Corrections

RequirementID: REQ-CORR-CLAIM-01

RequirementText: Security, performance, region, availability, billing, meter/overage, provider, privacy, and compliance claims require evidence, an owner, review date, and lifecycle status.

ContentLocator: Security, performance, region, availability, billing, meter/overage, provider, privacy, and compliance claims require evidence, an owner, review date, and lifecycle status.

Owner: Documentation claims

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: claim-registry review receipt verifying evidence, accountable owner, review date, and lifecycle status for every published operational claim in `FW-CLAIM-06`; Work contract: `FW-CLAIM-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unsupported claim.

N/A: gap

Work: FW-CLAIM-06

### REQ-CORR-BLOCKER-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Known Documentation and Ownership Corrections

RequirementID: REQ-CORR-BLOCKER-01

RequirementText: Unsupported values or stale contact details are release blockers, not marketing copy to preserve.

ContentLocator: Unsupported values or stale contact details are release blockers, not marketing copy to preserve.

Owner: Release and Documentation

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: release claim-blocker review receipt for unsupported values and stale contact details in `FW-CLAIM-06`; Work contract: `FW-CLAIM-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Misleading release.

N/A: gap

Work: FW-CLAIM-06

### REQ-CORR-LEGAL-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Known Documentation and Ownership Corrections

RequirementID: REQ-CORR-LEGAL-01

RequirementText: Do not publish legal, privacy, DPA, subprocessor, tax, refund, or retention commitments without the required product/legal authority. Track their approval separately from technical implementation.

ContentLocator: legal,

Owner: Product and legal

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: legal-commitment publication authority receipt, separately recording product approval, legal approval, scope, and review date, in `FW-CLAIM-06`; Work contract: `FW-CLAIM-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unapproved legal commitment.

N/A: gap

Work: FW-CLAIM-06

### REQ-CORR-PRIVACY-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Known Documentation and Ownership Corrections

RequirementID: REQ-CORR-PRIVACY-01

RequirementText: Do not publish legal, privacy, DPA, subprocessor, tax, refund, or retention commitments without the required product/legal authority. Track their approval separately from technical implementation.

ContentLocator: privacy,

Owner: Product and legal

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: privacy-commitment publication authority receipt, separately recording product approval, legal approval, scope, and review date, in `FW-CLAIM-06`; Work contract: `FW-CLAIM-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unapproved privacy commitment.

N/A: gap

Work: FW-CLAIM-06

### REQ-CORR-DPA-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Known Documentation and Ownership Corrections

RequirementID: REQ-CORR-DPA-01

RequirementText: Do not publish legal, privacy, DPA, subprocessor, tax, refund, or retention commitments without the required product/legal authority. Track their approval separately from technical implementation.

ContentLocator: DPA,

Owner: Product and legal

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: DPA publication authority receipt, separately recording product approval, legal approval, scope, and review date, in `FW-CLAIM-06`; Work contract: `FW-CLAIM-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unapproved DPA commitment.

N/A: gap

Work: FW-CLAIM-06

### REQ-CORR-SUBPROCESSOR-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Known Documentation and Ownership Corrections

RequirementID: REQ-CORR-SUBPROCESSOR-01

RequirementText: Do not publish legal, privacy, DPA, subprocessor, tax, refund, or retention commitments without the required product/legal authority. Track their approval separately from technical implementation.

ContentLocator: subprocessor,

Owner: Product and legal

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: subprocessor-commitment publication authority receipt, separately recording product approval, legal approval, scope, and review date, in `FW-CLAIM-06`; Work contract: `FW-CLAIM-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unapproved subprocessor commitment.

N/A: gap

Work: FW-CLAIM-06

### REQ-CORR-TAX-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Known Documentation and Ownership Corrections

RequirementID: REQ-CORR-TAX-01

RequirementText: Do not publish legal, privacy, DPA, subprocessor, tax, refund, or retention commitments without the required product/legal authority. Track their approval separately from technical implementation.

ContentLocator: tax,

Owner: Product and legal

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: tax-commitment publication authority receipt, separately recording product approval, legal approval, scope, and review date, in `FW-CLAIM-06`; Work contract: `FW-CLAIM-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unapproved tax commitment.

N/A: gap

Work: FW-CLAIM-06

### REQ-CORR-REFUND-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Known Documentation and Ownership Corrections

RequirementID: REQ-CORR-REFUND-01

RequirementText: Do not publish legal, privacy, DPA, subprocessor, tax, refund, or retention commitments without the required product/legal authority. Track their approval separately from technical implementation.

ContentLocator: refund,

Owner: Product and legal

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: refund-commitment publication authority receipt, separately recording product approval, legal approval, scope, and review date, in `FW-CLAIM-06`; Work contract: `FW-CLAIM-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unapproved refund commitment.

N/A: gap

Work: FW-CLAIM-06

### REQ-CORR-RETENTION-01

SourceAnchor: G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Known Documentation and Ownership Corrections

RequirementID: REQ-CORR-RETENTION-01

RequirementText: Do not publish legal, privacy, DPA, subprocessor, tax, refund, or retention commitments without the required product/legal authority. Track their approval separately from technical implementation.

ContentLocator: retention commitments

Owner: Product and legal

Life: gap

REST: gap

Stream: gap

.NET: gap

TS: gap

Dashboard: gap

MCP: gap

Auth: gap

AT: Planned artifact: retention-commitment publication authority receipt, separately recording product approval, legal approval, scope, and review date, in `FW-CLAIM-06`; Work contract: `FW-CLAIM-06`; Evidence: gap.

Evidence: gap

Claim: gap

Docs: gap

Runbook: gap

Risk: Unapproved retention commitment.

N/A: gap

Work: FW-CLAIM-06


## Source-grounded expansion status

Status: open. The narrative governing records above remain the source-grounded traceability baseline. Their SourceAnchor fields use genuine GOAL heading chains, their ContentLocator fields retain literal source excerpts, and a planned-artifact or Work-contract mapping only identifies future work. `Evidence: gap` keeps implementation, real-boundary proof, and acceptance open. No P0 or product acceptance is asserted in this repair.

The remaining review work is explicit gap: validate the retained atomic records against the current GOAL and resolve any semantic binding or work-contract gaps found by that review; the specific independent P0-01V positive and adversarial coverage review was completed and recorded in `p0-01v-independent-review.md`, with no Phase 0 acceptance claim.

## Coverage audit and non-claims

This is a retained, source-grounded traceability mapping, not implementation evidence. It is fail-closed because any remaining `gap`, including unexpanded GOAL clauses, semantic scenario bindings, and open evidence, prevents coverage or acceptance claims.

The ledger is a planning baseline, not acceptance evidence. No P0, product, production, live-infrastructure, Polar Sandbox, provider, R3, or public capability acceptance is claimed here.

## Agentic delivery workflow atomic governing records

Status: open. These rows atomize the literal clauses under the real GOAL heading chain `# TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow`, including its `### Required Task Contract` and `### AI-Agent Safety Model` subheadings. `gap` is not evidence or acceptance. The Work mapping uses the existing P0-07 traceability contract only and does not create product acceptance. `N/A` values use only `N/A[story;approving-authority;safe-alternative;validation-evidence]`.

| SourceAnchor | RequirementID | RequirementText | ContentLocator | Owner | Life | REST | Stream | .NET | TS | Dashboard | MCP | Auth | AT | Evidence | Claim | Docs | Runbook | Risk | N/A | Work |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow | REQ-ADW-ORCHESTRATOR-01 | The root orchestrator maintains the complete system view and does not implement feature code directly. | The root orchestrator maintains the complete system view and does not implement feature code directly. | Delivery governance | gap | N/A[delivery governance;delivery authority;no public REST effect;P0-07 traceability review] | N/A[delivery governance;delivery authority;no streaming effect;P0-07 traceability review] | N/A[delivery governance;delivery authority;no SDK effect;P0-07 traceability review] | N/A[delivery governance;delivery authority;no SDK effect;P0-07 traceability review] | N/A[delivery governance;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[delivery governance;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: root-orchestrator system-view and feature-code delegation review record; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | gap | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow | REQ-ADW-INVENTORY-01 | Establish a current, evidence-backed inventory of repositories, architecture, contracts, feature gaps, risk, dependencies, and production blockers. | Establishes a current, evidence-backed inventory of repositories, architecture, contracts, feature gaps, risk, dependencies, and production blockers. | Delivery governance | gap | N/A[delivery inventory;delivery authority;no public REST effect;P0-07 traceability review] | N/A[delivery inventory;delivery authority;no streaming effect;P0-07 traceability review] | N/A[delivery inventory;delivery authority;no SDK effect;P0-07 traceability review] | N/A[delivery inventory;delivery authority;no SDK effect;P0-07 traceability review] | N/A[delivery inventory;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[delivery inventory;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: current repository, architecture, contract, gap, risk, dependency, and blocker inventory review record; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | gap | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow | REQ-ADW-BACKLOG-01 | Create a dependency-aware backlog of small, outcome-based tasks with the required task information. | Creates a dependency-aware backlog of small, outcome-based tasks. Each task has an owner, exact paths or responsibility boundary, acceptance criteria, required validation, dependencies, risk level, and a written report location. | Delivery governance | gap | N/A[delivery backlog;delivery authority;no public REST effect;P0-07 traceability review] | N/A[delivery backlog;delivery authority;no streaming effect;P0-07 traceability review] | N/A[delivery backlog;delivery authority;no SDK effect;P0-07 traceability review] | N/A[delivery backlog;delivery authority;no SDK effect;P0-07 traceability review] | N/A[delivery backlog;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[delivery backlog;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: dependency-aware small outcome-based backlog with owner, boundary, acceptance, validation, dependency, risk, and report-location fields; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | gap | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow | REQ-ADW-WORKERS-01 | Delegate independent work to multiple GPT-5.6 Terra worker agents, calibrate reasoning to complexity, and prevent overlapping write ownership. | Delegates independent exploration, implementation, test, documentation, and verification tasks to multiple GPT-5.6 Terra worker agents. Reasoning effort is calibrated to task complexity; no worker receives overlapping write ownership. | Delivery governance | gap | N/A[worker delegation;delivery authority;no public REST effect;P0-07 traceability review] | N/A[worker delegation;delivery authority;no streaming effect;P0-07 traceability review] | N/A[worker delegation;delivery authority;no SDK effect;P0-07 traceability review] | N/A[worker delegation;delivery authority;no SDK effect;P0-07 traceability review] | N/A[worker delegation;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[worker delegation;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: independent worker delegation register with complexity-calibrated reasoning and non-overlapping write ownership; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | gap | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow | REQ-ADW-INTEGRATE-01 | Review every worker result, integrate only compatible changes, resolve conflicts and dependencies, and immediately create follow-up work for gaps or regressions. | Reviews every worker result against the task contract, integrates only compatible changes, resolves conflicts and cross-repository dependencies, and immediately creates follow-up work for gaps or regressions. | Delivery governance | gap | N/A[integration governance;delivery authority;no public REST effect;P0-07 traceability review] | N/A[integration governance;delivery authority;no streaming effect;P0-07 traceability review] | N/A[integration governance;delivery authority;no SDK effect;P0-07 traceability review] | N/A[integration governance;delivery authority;no SDK effect;P0-07 traceability review] | N/A[integration governance;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[integration governance;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: worker-result contract review and compatible-integration receipt with conflict, dependency, and follow-up tracking; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | gap | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow | REQ-ADW-BOUNDARY-TESTS-01 | Require real product-boundary testing rather than bypassing mocks, stubs, or fakes; permit deterministic seams only for focused protocol or state-machine tests with no live boundary under test. | Requires real product-boundary testing rather than mocks, stubs, or fakes that bypass services or persistence. Small deterministic seams are permitted only for focused protocol/state-machine tests where no live boundary is under test. | Delivery governance | gap | N/A[delivery validation;quality authority;no public REST contract;P0-07 traceability review] | N/A[delivery validation;quality authority;no streaming contract;P0-07 traceability review] | N/A[delivery validation;quality authority;no SDK contract;P0-07 traceability review] | N/A[delivery validation;quality authority;no SDK contract;P0-07 traceability review] | N/A[delivery validation;quality authority;no Dashboard contract;P0-07 traceability review] | N/A[delivery validation;quality authority;no MCP-specific customer scenario;P0-07 traceability review] | gap | Planned artifact: real product-boundary test review receipt, with deterministic seams limited to focused non-live protocol or state-machine tests; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | gap | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow | REQ-ADW-INTEGRATION-VALIDATION-01 | After each integration set, run relevant tests, static analysis, security checks, compatibility checks, and end-to-end scenarios, and track failures to closure. | After each integration set, runs relevant tests, static analysis, security checks, compatibility checks, and end-to-end scenarios; tracks failures to closure. | Delivery governance | gap | N/A[integration validation;quality authority;no public REST contract;P0-07 traceability review] | N/A[integration validation;quality authority;no streaming contract;P0-07 traceability review] | N/A[integration validation;quality authority;no SDK contract;P0-07 traceability review] | N/A[integration validation;quality authority;no SDK contract;P0-07 traceability review] | N/A[integration validation;quality authority;no Dashboard contract;P0-07 traceability review] | N/A[integration validation;quality authority;no MCP-specific customer scenario;P0-07 traceability review] | gap | Planned artifact: post-integration test, static-analysis, security, compatibility, end-to-end, and failure-closure validation receipt; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | gap | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow | REQ-ADW-INDEPENDENT-REVIEW-01 | Spawn a fresh read-only independent reviewer after implementation and tests; assess all listed dimensions and fix and revalidate every actionable finding. | Spawns a fresh, read-only independent Terra reviewer after implementation and tests. The reviewer assesses correctness, regressions, security, concurrency, architecture boundaries, documentation, and missing tests. Every actionable finding is fixed and revalidated. | Delivery governance | gap | N/A[independent review;quality authority;no public REST effect;P0-07 traceability review] | N/A[independent review;quality authority;no streaming effect;P0-07 traceability review] | N/A[independent review;quality authority;no SDK effect;P0-07 traceability review] | N/A[independent review;quality authority;no SDK effect;P0-07 traceability review] | N/A[independent review;quality authority;no Dashboard effect;P0-07 traceability review] | N/A[independent review;quality authority;no MCP-specific customer scenario;P0-07 traceability review] | gap | Planned artifact: fresh read-only independent-review receipt covering correctness, regressions, security, concurrency, architecture, documentation, tests, and finding revalidation; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | gap | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow | REQ-ADW-FINAL-GATE-01 | Perform a final orchestrator review of the complete integrated diff and production gate, iterate to all acceptance criteria, and never declare success because the task list is exhausted. | Performs a final orchestrator review of the complete integrated diff and production gate. Continue iterating until all acceptance criteria are satisfied; do not declare success because a task list is exhausted. | Delivery governance | gap | N/A[final delivery gate;delivery authority;no public REST effect;P0-07 traceability review] | N/A[final delivery gate;delivery authority;no streaming effect;P0-07 traceability review] | N/A[final delivery gate;delivery authority;no SDK effect;P0-07 traceability review] | N/A[final delivery gate;delivery authority;no SDK effect;P0-07 traceability review] | N/A[final delivery gate;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[final delivery gate;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: final orchestrator complete-diff and production-gate review receipt confirming iterative acceptance criteria, not task-list exhaustion; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | gap | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow | REQ-ADW-REPORT-CONTENT-01 | Each exploration, implementation, integration, review, validation, and fix thread must leave a concise Markdown report with scope, evidence, decisions, changed paths, commands or tests, results, known limitations, and next dependencies. | Each exploration, implementation, integration, review, validation, and fix thread must leave a concise Markdown report containing scope, evidence, decisions, changed paths, commands/tests, results, known limitations, and next dependencies. | Delivery governance | gap | N/A[delivery reporting;delivery authority;no public REST effect;P0-07 traceability review] | N/A[delivery reporting;delivery authority;no streaming effect;P0-07 traceability review] | N/A[delivery reporting;delivery authority;no SDK effect;P0-07 traceability review] | N/A[delivery reporting;delivery authority;no SDK effect;P0-07 traceability review] | N/A[delivery reporting;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[delivery reporting;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: concise Markdown delivery-report content receipt with scope, evidence, decisions, paths, commands or tests, results, limitations, and dependencies; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | gap | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow | REQ-ADW-REPORT-REDACTION-01 | Reports must not contain credentials, tokens, customer data, or other sensitive information. | Reports must not contain credentials, tokens, customer data, or other sensitive information. | Delivery governance | gap | N/A[delivery reporting;security authority;no public REST effect;P0-07 traceability review] | N/A[delivery reporting;security authority;no streaming effect;P0-07 traceability review] | N/A[delivery reporting;security authority;no SDK effect;P0-07 traceability review] | N/A[delivery reporting;security authority;no SDK effect;P0-07 traceability review] | N/A[delivery reporting;security authority;no Dashboard effect;P0-07 traceability review] | N/A[delivery reporting;security authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: delivery-report sensitive-data redaction review receipt covering credentials, tokens, customer data, and other sensitive information; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | gap | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### Required Task Contract | REQ-TC-REVIEWABLE-01 | Every delegated task must be small enough to review. | Every delegated task must be small enough to review, and must state: | Delivery governance | gap | N/A[task contract;delivery authority;no public REST effect;P0-07 traceability review] | N/A[task contract;delivery authority;no streaming effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[task contract;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: reviewable delegated-task sizing receipt; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Unreviewable delegated change. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### Required Task Contract | REQ-TC-OBJECTIVE-01 | Every delegated task must state objective and non-goals. | objective and non-goals; | Delivery governance | gap | N/A[task contract;delivery authority;no public REST effect;P0-07 traceability review] | N/A[task contract;delivery authority;no streaming effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[task contract;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: delegated-task objective and non-goal declaration receipt; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Scope expansion. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### Required Task Contract | REQ-TC-OWNERSHIP-01 | Every delegated task must state owned repositories and exact writable paths, or an explicit read-only designation. | owned repositories and exact writable paths (or an explicit read-only designation); | Delivery governance | gap | N/A[task contract;delivery authority;no public REST effect;P0-07 traceability review] | N/A[task contract;delivery authority;no streaming effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[task contract;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: repository ownership and writable-path declaration receipt; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Overlapping or unauthorized writes. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### Required Task Contract | REQ-TC-RISK-01 | Every delegated task must state dependencies, authority needed, risk level, and security or tenancy impact. | dependencies, authority needed, risk level, and security/tenancy impact; | Delivery governance | gap | N/A[task contract;delivery authority;no public REST effect;P0-07 traceability review] | N/A[task contract;delivery authority;no streaming effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[task contract;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: dependency authority risk and security-impact declaration receipt; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Unapproved security or tenancy impact. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### Required Task Contract | REQ-TC-EFFECTS-01 | Every delegated task must state public-contract, Dashboard, SDK, MCP, documentation, and operational effects. | public-contract, Dashboard, SDK, MCP, documentation, and operational effects; | Delivery governance | gap | gap | gap | gap | gap | gap | gap | gap | Planned artifact: public-contract Dashboard SDK MCP documentation and operations effects declaration receipt; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Unidentified customer or operational effect. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### Required Task Contract | REQ-TC-ACCEPTANCE-01 | Every delegated task must state acceptance criteria, expected test boundary, evidence commands, and report path. | acceptance criteria, expected test boundary, evidence command(s), and report path; | Delivery governance | gap | N/A[task contract;delivery authority;no public REST effect;P0-07 traceability review] | N/A[task contract;delivery authority;no streaming effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[task contract;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: acceptance criteria test-boundary evidence-command and report-path receipt; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Unverifiable task completion. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### Required Task Contract | REQ-TC-HANDOFF-01 | Every delegated task must state changed paths, commit hashes, test results, residual risk, migration or rollback notes, and follow-up work. | handoff details: changed paths, commit hashes, test results, residual risk, migration/rollback notes, and follow-up work. | Delivery governance | gap | N/A[task contract;delivery authority;no public REST effect;P0-07 traceability review] | N/A[task contract;delivery authority;no streaming effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[task contract;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: changed-path commit test residual-risk rollback and follow-up handoff receipt; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Incomplete handoff or unsafe rollback. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### Required Task Contract | REQ-TC-STATUS-01 | The orchestrator checks working-tree status of the owned repository before every write, stage, commit, and push. | The orchestrator checks the working-tree status of the owned repository before every write, stage, commit, and push. | Delivery governance | gap | N/A[task contract;delivery authority;no public REST effect;P0-07 traceability review] | N/A[task contract;delivery authority;no streaming effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[task contract;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: pre-write stage commit and push working-tree status receipt; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Hidden or conflicting workspace change. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### Required Task Contract | REQ-TC-STAGING-01 | The orchestrator never stages broadly. | It never stages broadly | Delivery governance | gap | N/A[task contract;delivery authority;no public REST effect;P0-07 traceability review] | N/A[task contract;delivery authority;no streaming effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[task contract;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: explicit-path staging prohibition receipt; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Accidental staging. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### Required Task Contract | REQ-TC-EXCLUSIVE-WRITES-01 | The orchestrator never mixes concurrent writers in an owned path. | never mixes concurrent writers in an owned path | Delivery governance | gap | N/A[task contract;delivery authority;no public REST effect;P0-07 traceability review] | N/A[task contract;delivery authority;no streaming effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[task contract;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: exclusive owned-path writer receipt; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Concurrent write conflict. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### Required Task Contract | REQ-TC-REMOTE-DEVELOP-01 | The orchestrator coordinates any remote develop movement before integration. | coordinates any remote `develop` movement before integration. | Delivery governance | gap | N/A[task contract;delivery authority;no public REST effect;P0-07 traceability review] | N/A[task contract;delivery authority;no streaming effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[task contract;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: remote develop movement coordination receipt; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Stale integration base. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### Required Task Contract | REQ-TC-DATED-INDEX-01 | Reports are stored under the stable, dated agentic-delivery documentation index once delivery work begins, with links to the task, requirement matrix entries, commits, evidence, decision records, and unresolved risks. | Reports are stored under the stable, dated `Terrascale.Documentation/docs/agentic-delivery/` index once delivery work begins, with an index linking the task, requirement matrix entries, commit(s), evidence, decision records, and unresolved risks. | Delivery governance | gap | N/A[task contract;delivery authority;no public REST effect;P0-07 traceability review] | N/A[task contract;delivery authority;no streaming effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no SDK effect;P0-07 traceability review] | N/A[task contract;delivery authority;no Dashboard effect;P0-07 traceability review] | N/A[task contract;delivery authority;no MCP customer workflow effect;P0-07 traceability review] | gap | Planned artifact: dated delivery-index linkage receipt; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Untraceable delivery history. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-PARITY-01 | MCP capability parity means a customer can accomplish the same supported outcome through a safe public agent workflow. | MCP capability parity means a customer can accomplish the same supported outcome through a safe public agent workflow | MCP safety | gap | gap | N/A[MCP safety;MCP security authority;no streaming clause;P0-07 traceability review] | gap | gap | gap | gap | gap | Planned artifact: safe typed-public-operation parity receipt for the supported customer outcome; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Unsafe or unequal customer agent outcome. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-BAN-SHELL-01 | An agent must not receive an unguarded shell. | unguarded shell | MCP safety | gap | N/A[MCP safety;MCP security authority;public API safe alternative;P0-07 traceability review] | N/A[MCP safety;MCP security authority;no streaming clause;P0-07 traceability review] | N/A[MCP safety;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP safety;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP safety;MCP security authority;no Dashboard clause;P0-07 traceability review] | gap | gap | Planned artifact: negative boundary receipt denying unguarded shell access; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Arbitrary host execution. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-BAN-HTTP-01 | An agent must not receive a generic HTTP client. | generic HTTP client | MCP safety | gap | N/A[MCP safety;MCP security authority;typed public API safe alternative;P0-07 traceability review] | N/A[MCP safety;MCP security authority;no streaming clause;P0-07 traceability review] | N/A[MCP safety;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP safety;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP safety;MCP security authority;no Dashboard clause;P0-07 traceability review] | gap | gap | Planned artifact: negative boundary receipt denying generic HTTP client access; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Unbounded network access. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-BAN-DB-SECRET-01 | An agent must not receive a database connection secret. | database connection secret | MCP safety | gap | N/A[MCP safety;MCP security authority;controlled credential flow;P0-07 traceability review] | N/A[MCP safety;MCP security authority;no streaming clause;P0-07 traceability review] | N/A[MCP safety;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP safety;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP safety;MCP security authority;no Dashboard clause;P0-07 traceability review] | gap | gap | Planned artifact: negative boundary receipt denying database connection-secret exposure; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Credential disclosure. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-BAN-TQL-DOCS-01 | An agent must not receive arbitrary TQL or documents. | arbitrary TQL/documents | MCP safety | gap | N/A[MCP safety;MCP security authority;typed bounded operations;P0-07 traceability review] | N/A[MCP safety;MCP security authority;no streaming clause;P0-07 traceability review] | N/A[MCP safety;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP safety;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP safety;MCP security authority;no Dashboard clause;P0-07 traceability review] | gap | gap | Planned artifact: negative boundary receipt denying arbitrary TQL or document access; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Arbitrary data access or execution. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-BAN-RPC-01 | An agent must not receive internal RPC access. | internal RPC access | MCP safety | gap | N/A[MCP safety;MCP security authority;public API safe alternative;P0-07 traceability review] | N/A[MCP safety;MCP security authority;public stream safe alternative;P0-07 traceability review] | N/A[MCP safety;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP safety;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP safety;MCP security authority;no Dashboard clause;P0-07 traceability review] | gap | gap | Planned artifact: negative boundary receipt denying internal RPC access; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Internal transport exposure. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-BAN-STAFF-01 | An agent must not receive staff privilege. | staff privilege | MCP safety | gap | N/A[MCP safety;MCP security authority;customer authorization safe alternative;P0-07 traceability review] | N/A[MCP safety;MCP security authority;no streaming clause;P0-07 traceability review] | N/A[MCP safety;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP safety;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP safety;MCP security authority;no Dashboard clause;P0-07 traceability review] | gap | gap | Planned artifact: negative boundary receipt denying staff privilege; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Privilege escalation. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-DISCOVERY-01 | Discovery and health reads must be typed, bounded, paginated, sensitivity-classified, explicit in tenant or project scope, and return sanitized errors only. | Typed, bounded, paginated, sensitivity-classified output; tenant/project scope is explicit; sanitized errors only. | MCP safety | gap | gap | gap | gap | gap | N/A[MCP discovery safety;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: typed-public-operation discovery safety receipt for bounded paginated scoped sanitized reads; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Data disclosure or unbounded read. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-REVERSIBLE-01 | Reversible mutations must use a typed public contract, authorization re-check, idempotency key, meaningful dry-run or impact preview, and explicit target-naming confirmation. | Typed public contract, authorization re-check, idempotency key, dry-run/impact preview where meaningful, and explicit confirmation that names the target. | MCP safety | gap | gap | N/A[MCP mutation safety;MCP security authority;no streaming requirement;P0-07 traceability review] | gap | gap | N/A[MCP mutation safety;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: typed-public-operation reversible-mutation receipt for authorization, idempotency, preview, and target confirmation; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Unauthorized or duplicate mutation. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-DESTRUCTIVE-01 | Destructive or financially consequential actions must identify the target and resource, provide impact and retention window, require two-step confirmation and idempotency, record an audit event, have safe retry semantics, and document recovery or escalation. | Target/resource identity, impact and retention window, two-step confirmation, idempotency, audit event, safe retry semantics, and a documented recovery/escalation path. | MCP safety | gap | gap | N/A[MCP destructive safety;MCP security authority;no streaming requirement;P0-07 traceability review] | gap | gap | N/A[MCP destructive safety;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: typed-public-operation destructive-action receipt for target, impact, retention, confirmation, audit, retry, and recovery; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Irreversible customer or financial harm. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-CREDENTIALS-ACCESS-01 | Credentials, recovery, access, and policy changes must apply required high-assurance control, least privilege, no raw-secret return after creation, immediate auditability, and cross-tenant denial tests. | Re-authentication or equivalent high-assurance control where required, least privilege, never return raw secrets after creation, immediate auditability, and cross-tenant denial tests. | MCP safety | gap | gap | N/A[MCP access safety;MCP security authority;no streaming requirement;P0-07 traceability review] | gap | gap | N/A[MCP access safety;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: typed-public-operation credential and access-change receipt for high assurance, least privilege, auditability, and cross-tenant denial; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Account compromise or cross-tenant access. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-META-INPUT-01 | Every MCP tool, resource, and prompt must declare input grammar. | input grammar | MCP safety | gap | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: MCP metadata receipt declaring input grammar; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Invalid or ambiguous agent input. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-META-OUTPUT-01 | Every MCP tool, resource, and prompt must declare output schema and sensitivity. | output schema and sensitivity | MCP safety | gap | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: MCP metadata receipt declaring output schema and sensitivity; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Sensitive output exposure. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-META-AUTH-01 | Every MCP tool, resource, and prompt must declare auth modes. | auth modes | MCP safety | gap | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: MCP metadata receipt declaring authentication modes; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Authentication bypass. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-META-SCOPE-01 | Every MCP tool, resource, and prompt must declare organization or project scope. | organization/project scope | MCP safety | gap | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: MCP metadata receipt declaring organization or project scope; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Cross-tenant scope confusion. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-META-PAGINATION-01 | Every MCP tool, resource, and prompt must declare pagination limits. | pagination limits | MCP safety | gap | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: MCP metadata receipt declaring pagination limits; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Unbounded data retrieval. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-META-IDEMPOTENCY-01 | Every MCP tool, resource, and prompt must declare idempotency or confirmation rules. | idempotency/confirmation rules | MCP safety | gap | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: MCP metadata receipt declaring idempotency or confirmation rules; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Duplicate or unconfirmed mutation. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-META-ERROR-01 | Every MCP tool, resource, and prompt must declare error envelope. | error envelope | MCP safety | gap | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: MCP metadata receipt declaring the sanitized error envelope; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Error leakage or unsafe retry. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-META-DEPENDENCY-01 | Every MCP tool, resource, and prompt must declare public API or SDK dependency. | public API/SDK dependency | MCP safety | gap | gap | N/A[MCP metadata;MCP security authority;no streaming dependency declaration;P0-07 traceability review] | gap | gap | N/A[MCP metadata;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: MCP metadata receipt declaring public API or SDK dependency; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Undeclared private dependency. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-META-EVIDENCE-01 | Every MCP tool, resource, and prompt must declare real-boundary test evidence. | real-boundary test evidence | MCP safety | gap | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;metadata is tool-local;P0-07 traceability review] | N/A[MCP metadata;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: MCP metadata receipt declaring real-boundary test evidence; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Unproven tool safety. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-BAN-TERRABASE-01 | Tools cannot call TerraBase directly. | Tools cannot call TerraBase directly | MCP safety | gap | N/A[MCP boundary;MCP security authority;typed public API safe alternative;P0-07 traceability review] | N/A[MCP boundary;MCP security authority;no streaming clause;P0-07 traceability review] | N/A[MCP boundary;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP boundary;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP boundary;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: negative boundary receipt denying direct TerraBase calls; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Direct data-plane bypass. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-BAN-MAGICONION-01 | Tools cannot consume MagicOnion. | consume MagicOnion | MCP safety | gap | N/A[MCP boundary;MCP security authority;public API safe alternative;P0-07 traceability review] | N/A[MCP boundary;MCP security authority;public stream safe alternative;P0-07 traceability review] | N/A[MCP boundary;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP boundary;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP boundary;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: negative boundary receipt denying MagicOnion consumption; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Private transport exposure. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-BAN-GENERIC-SDK-01 | Tools cannot use generic SDK requests. | use generic SDK requests | MCP safety | gap | N/A[MCP boundary;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP boundary;MCP security authority;no streaming clause;P0-07 traceability review] | gap | gap | N/A[MCP boundary;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: negative boundary receipt denying generic SDK requests; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Untyped contract bypass. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-BAN-HIDDEN-HEADERS-01 | Tools cannot add hidden headers. | add hidden headers | MCP safety | gap | N/A[MCP boundary;MCP security authority;documented public contract;P0-07 traceability review] | N/A[MCP boundary;MCP security authority;no streaming clause;P0-07 traceability review] | N/A[MCP boundary;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP boundary;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP boundary;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: negative boundary receipt denying hidden headers; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | Hidden authorization bypass. | gap | P0-07 |
| G0-20260805-0a2fe859ee1d8c6e345a10cb48be35e419978ebe8315d24a13515df8357c95b9 > # TerraScale Production DBaaS Goal > ## Agentic Delivery Workflow > ### AI-Agent Safety Model | REQ-AIS-BAN-AI-ADMIN-01 | Tools cannot expose an AI-only administrative backdoor. | expose an AI-only administrative backdoor | MCP safety | gap | N/A[MCP boundary;MCP security authority;customer authorization safe alternative;P0-07 traceability review] | N/A[MCP boundary;MCP security authority;no streaming clause;P0-07 traceability review] | N/A[MCP boundary;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP boundary;MCP security authority;typed SDK safe alternative;P0-07 traceability review] | N/A[MCP boundary;MCP security authority;Dashboard is not an MCP tool;P0-07 traceability review] | gap | gap | Planned artifact: negative boundary receipt denying an AI-only administrative backdoor; Work contract: `P0-07`; Evidence: gap. | gap | gap | gap | gap | AI-only privilege escalation. | gap | P0-07 |
