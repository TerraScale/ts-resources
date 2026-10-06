# TerraScale platform

This context defines the customer identity, ownership, and access boundaries used across the TerraScale platform.

## Identity

**User**:
A person with one TerraScale identity. A verified email address is the only sign-in method: requesting a sign-in link or one-time code and proving possession of the mailbox establishes the identity. TerraScale accounts have no password, username, external-provider, passkey, or MFA credentials.
_Avoid_: Account, project user

**Project authentication user**:
An end user of a customer's application managed by TerraScale's project-scoped Authentication product.
_Avoid_: TerraScale User, Project Member

**TerraScale Admin**:
An internal TerraScale operator with global administrative authority but no standing access to customer documents. This authority does not make the user a member of any customer organization or project.
_Avoid_: Admin, Organization Owner

**Break-glass access**:
A time-limited grant that allows a TerraScale Admin to inspect narrowly scoped customer data for an approved support or incident reason.
_Avoid_: Admin access, impersonation

**Fresh authentication**:
A proof of the User's identity no older than 15 minutes, established by completing email sign-in verification and required before a sensitive billing, credential, deletion, or break-glass action.
_Avoid_: Active session, refresh token

**Customer onboarding**:
The mandatory flow a self-registering User completes to verify identity, create a Personal Organization, verify an Organization-owned card, and create the first Project before using the Customer Dashboard. A paid Organization also confirms its selected subscription. A new invited User completes Personal Organization card verification before accepting the Invitation, while a previously verified User resumes at Invitation acceptance. Completion records the finished journey, not the User's current access, ownership, or billing state.
_Avoid_: Account activation, Project activation

**Organization creation eligibility**:
A legacy historical approval recorded by the retired User-level Signup verification flow. Existing approvals remain available for migration history but neither grant nor block new Organization creation.
_Avoid_: Account activation, billing authority

## Customer ownership

**Organization**:
The customer boundary that owns projects, membership, subscriptions, payment methods, billing history, and consolidated usage.
_Avoid_: Account, tenant

**Organization billing method**:
A verified payment method attached to the Polar Customer identified by an Organization. It is required for every Personal Organization as an abuse-prevention control and for paid plans or upgrades. It never belongs to an individual User.
_Avoid_: Signup verification method, User payment method

**Billing-pending Organization**:
A newly created paid Organization waiting for its initial billing confirmation. It permits billing recovery and basic Organization management but owns no Projects, Invitations, Application credentials, or billable resources.
_Avoid_: Inactive User, unpaid Project

**Developer Organization**:
The non-transferable Personal Organization a User receives on the free Developer plan. It requires verified-card enrollment but creates no subscription or charge. Its Projects share the Organization's storage and operation allowances.
_Avoid_: Free Project, Developer account

**Organization Owner**:
An organization member who may manage the organization, all of its projects, its membership, and its billing. Every organization retains at least one Organization Owner.
_Avoid_: Admin, Project Owner

**Organization Member**:
A user who belongs to an organization but receives access only to explicitly assigned projects.
_Avoid_: Member, project user, Organization Owner

**Active organization**:
The organization currently selected as the user's working context.
_Avoid_: Active subscription, last organization

## Project access

**Project**:
An application scope inside one organization. It owns regional placement, customer products, project access, and project usage.
_Avoid_: Organization, tenant

**Project Owner**:
An organization member who may administer one assigned project without gaining organization-wide billing or membership authority.
_Avoid_: Organization Owner, Admin

**Project Member**:
An organization member who may use the assigned project's products but may not administer the project.
_Avoid_: Member, Organization Member

**Project Viewer**:
An organization member with read-only access to an assigned project.
_Avoid_: Viewer, Project Member

**Permission group**:
A set of project capabilities that may narrow Project Member or Project Viewer access but may never grant authority above Project Owner.
_Avoid_: Custom role, global role

**Project capability**:
One assignable authority for database reads, database writes, queries, queue publishing, queue consumption, authentication management, monitoring, or project administration.
_Avoid_: Role, global permission

**Application credential**:
A machine identity with explicit project and product capabilities and no human ownership authority.
_Avoid_: Project Owner, user session

**Audit record**:
An append-only, secret-redacted account of a security, membership, billing, credential, administrative, or destructive customer action.
_Avoid_: Monitoring event, application log

## Data location

**Customer content**:
Customer documents, queue payloads, and project-authentication user data that remains inside the project's selected regions.
_Avoid_: Control metadata, billing record

**Control metadata**:
The minimal account, organization, billing, audit, and placement data TerraScale needs to operate the service across control regions.
_Avoid_: Customer content, document data

## Capability delivery

**Feature flag**:
An audited server-side control that enables one capability for selected environments or organizations without changing authorization.
_Avoid_: Permission, permanent configuration

## Customer data

**Database**:
A logical customer grouping inside a project.
_Avoid_: Physical database, project data plane

**Database deletion**:
A seven-day scheduled removal of one explicitly selected Database and all content it owns. It does not delete the User, Organization, or Project, and it requires fresh authentication plus confirmation using the Database identifier and name.
_Avoid_: Account deletion, Organization deletion, Project deletion

**Deletion-pending Database**:
A Database scheduled for deletion that remains readable and exportable while rejecting writes, new Environments, new Repositories, and new charges. An Organization Owner or Project Owner may cancel the deletion before its seven-day deadline.
_Avoid_: Deleted Database, read-only Organization

**Portable project export**:
A compressed, customer-readable archive for one Project containing a manifest and newline-delimited JSON for each Repository. It excludes credential secrets and keeps billing receipts separate.
_Avoid_: Backup, account export

**Environment**:
A named virtual namespace inside a database, not a physical clone. A database may contain any number of environments, including several with the same kind, but each environment name is unique within that database.
_Avoid_: Database branch, isolated database

**Repository**:
A typed collection and the document API boundary.
_Avoid_: Git repository, database

**Document**:
One stored customer object inside a repository.
_Avoid_: Row, record

## Customer monitoring

**Customer Dashboard**:
The customer-facing application for organization, project, product, usage, billing, and monitoring workflows.
_Avoid_: Grafana, operator console

**Operator dashboard**:
The private Grafana-based view used by TerraScale operators for infrastructure and service monitoring.
_Avoid_: Customer Dashboard, public monitoring API

**Public status page**:
The public view of shared TerraScale service incidents by region and product.
_Avoid_: Customer Dashboard, operator dashboard

**Estimated network distance latency**:
A geographic estimate derived from locations rather than observed network traffic.
_Avoid_: Live latency, measured latency

**Measured API latency**:
Observed request latency for TerraScale's customer API.
_Avoid_: Estimated network distance latency

**Inter-region probe latency**:
Observed network latency from a controlled probe between two TerraScale regions.
_Avoid_: Replication lag, estimated latency

**Usage value status**:
The evidence label attached to a usage value: measured, estimated, provisional, or unavailable.
_Avoid_: Billing status, metric health

**Customer region state**:
The customer-visible state of one selected region: healthy, degraded, unavailable, or unknown.
_Avoid_: Replication health, placement progress

## API routing

**Global API endpoint**:
The customer endpoint that routes a request to the nearest healthy region selected by the project.
_Avoid_: Regional endpoint, control endpoint

**Regional API endpoint**:
A customer endpoint with strict affinity to one selected region and no silent failover to another region.
_Avoid_: Preferred region, global endpoint

**Region placement change**:
An asynchronous operation that adds or removes one of a project's selected regions only after catch-up or drain completes.
_Avoid_: Instant region switch, routing preference
