# TerraScale public product

This context defines the language used for TerraScale's customer-facing product, availability, and release status.

## Release status

**Public Alpha**:
An openly available early release that anyone may register to use, but that is not approved for critical data or production reliability commitments.
_Avoid_: Private alpha, production-ready, generally available

## Onboarding

**Customer onboarding**:
The target guided setup for a self-registering User. It opens with identity and email verification already counted as the completed first step, then guides the User through provisioning the first Organization, Project, and logical Database.
_Avoid_: Invited-user onboarding, plan checkout

**Signup verification method**:
A payment card enrolled and verified during Customer onboarding for signup abuse control. Verification does not charge the card, start a paid trial, create a subscription, or enable automatic renewal.
_Avoid_: Trial card, subscription payment

**Free-only choice**:
The explicit post-verification choice to select no paid plan and no automatic renewal. The Organization retains its non-expiring Developer allowance.
_Avoid_: No plan, trial cancellation

**Automatic renewal**:
The explicit monthly renewal commitment accepted only when an Organization Owner selects Starter or Pro. An eligible paid Organization receives its first 30 days at no charge before monthly billing begins.
_Avoid_: Default renewal, implicit renewal

**Invited-user onboarding**:
The separate flow for a User joining an existing Organization by invitation. It does not reuse the self-registration sequence or imply that the invited User must provision a Personal Organization, Project, or Database.
_Avoid_: Customer onboarding

**Free tier**:
A non-expiring plan with 1 GB of storage usage across all selected regions and 10,000 operation units per calendar month. TerraScale warns customers as they approach the monthly operation limit and resets that allowance at the start of the next month. Reaching an allowance may stop new billable work, but does not delete stored data or prevent reads, exports, and deletion.
_Avoid_: Trial, temporary plan

## Billing measures

**Storage usage**:
The sum of customer-document bytes stored in every selected region. For example, 100 MB replicated to three regions counts as 300 MB of storage usage.
_Avoid_: Logical document size, single-region size

**Operation unit**:
The billing measure for each started 4 KiB of uncompressed customer-document data processed by a billable database operation. It measures data processed, not the number of API requests.
_Avoid_: Request, API call, database operation

## Plans

**Personal Organization**:
The non-transferable Organization automatically created for every new User. Its payment method, Polar Customer identity, subscriptions, trials, billing history, Projects, and memberships belong to the Organization, not directly to the User. The owner may rename it, and it uses the selected plan's normal member allowance.
_Avoid_: Personal account, User subscription

**Developer plan**:
The default non-expiring free plan. Each verified User may own one Developer Organization, and joining Organizations owned by other Users does not consume that allowance. Every self-registering User enrolls a verified card for signup abuse control, including a User who chooses no paid plan, but Developer creates no subscription or charge. An invited User follows the separate invitation flow. Card reuse is an abuse signal, not an automatic rejection.
_Avoid_: Trial, introductory plan

**Paid plan**:
An organization subscription selected explicitly by an Organization Owner and renewed according to the accepted billing interval.
_Avoid_: Account subscription, default plan

**Paid trial eligibility**:
The first 30 days at no charge for an eligible paid Organization that explicitly selects Starter or Pro and accepts monthly automatic renewal. Eligibility is evaluated from durable billing history rather than current card, owner, or membership identity. Changing a card, owner, or membership does not restore eligibility.
_Avoid_: Per-user trial, new-card trial

**Enterprise plan**:
A contract plan with a monthly support base and separately metered usage, with no usage included in the base.
_Avoid_: Unlimited plan, flat-rate plan

## Data lifecycle

**Payment retry period**:
The first seven days after a failed renewal. The Organization keeps normal access while TerraScale retries payment. Payment during this period restores the existing paid plan without data loss.
_Avoid_: Read-only grace, cancellation window

**Unpaid Organization grace**:
The 30-day read-only state after an unresolved payment retry period. It permits reads, usage reduction, deletion, and export while blocking new billable work. Payment restores the prior plan and data access. At the end, TerraScale purges Customer content and customer-restorable copies, retaining only the minimal Organization, billing, security, Audit, and deletion-receipt records required by policy. The empty Organization may later reactivate, but purged data cannot return.
_Avoid_: Developer downgrade, free overage

**Project export**:
A versioned ZIP package with a versioned manifest, integrity hashes, and one newline-delimited JSON file per Repository. It excludes credential secrets. Delivery is either an authenticated, revocable download available for 24 hours or an upload to a short-lived customer-provided AWS S3 presigned destination. TerraScale never stores the customer's AWS access keys.
_Avoid_: Backup, database snapshot

**Voluntary User deletion**:
A separate seven-day cancellable lifecycle that immediately revokes sessions and stops charges while preserving export. Completion deletes the Personal Organization, memberships, and Customer content, retaining only legally required records and a deletion receipt.
_Avoid_: Unpaid Organization grace, immediate purge

## MCP access

**MCP access key**:
A distinct user-bound credential for MCP, never a Project Application credential. The User selects Organization, Project, and operation scopes. Future Organizations and Projects are excluded by default. The key expires after 90 days by default, is shown once, stored only as a hash, immediately revocable and rotatable, and audited for last use.
_Avoid_: Project API key, operator credential

**MCP public-operation parity**:
MCP may expose every typed public operation available to the authenticated User, including Document, billing, credential, membership, and role-protected administration operations. Each tool applies identical authorization, tenant isolation, confirmation, Audit, and secret-handling rules. Private control-plane operations, private routes, and raw or generic HTTP forwarding remain unavailable.
_Avoid_: Read-only MCP, operator MCP

**MCP sensitive-operation confirmation**:
A two-step public-server protocol. The first tool returns the exact plan, impact, price where relevant, and a five-minute single-use token. The User confirms in the AI conversation, then the AI invokes the confirmation tool. The server rechecks permissions, tenant scope, payload, target state, and price before consuming the token and recording the Audit event. No Dashboard confirmation or separate fresh-authentication challenge is required.
_Avoid_: Confirmation boolean, Dashboard approval

**Deletion receipt**:
A record confirming that a scheduled account or organization deletion completed, without retaining the deleted customer content.
_Avoid_: Backup manifest, audit export

## Geography

**Launch region**:
A region that customers can select during Public Alpha. The launch regions are Sao Paulo, San Francisco, and Falkenstein.
_Avoid_: Planned region, future region

**Planned region**:
A proposed customer location that has not yet qualified for selection.
_Avoid_: Available region, supported region
