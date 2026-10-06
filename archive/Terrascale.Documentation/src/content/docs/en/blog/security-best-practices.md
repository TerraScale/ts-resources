---
title: "Security Best Practices for TerraScale"
date: 2024-09-25
authors:
  - name: Mario Gabriell Karaziaki Belchior
    title: Founder
    url: mailto:mariogk@terrascale.tech
tags:
  - security
  - best-practices
excerpt: Security isn't optional. Here's how to keep your TerraScale databases secure with sensible API key management, passwordless email sign-in, and access controls.
cover:
  wide: /images/blog/security-best-practices/cover-wide.svg
  square: /images/blog/security-best-practices/cover-square.svg
  alt: Layered shield geometry and guarded perimeter nodes, conveying careful database security.
---

Security isn't optional. Here's a practical checklist to help you keep your TerraScale databases secure.

## What you'll learn

- How to manage API keys without creating unnecessary risk
- Which account and team controls matter most
- What to review regularly so security stays boring, in the best way

If you're configuring access as you read, keep the [authentication reference](/reference/authentication/), [API keys reference](/reference/management/api-keys/), and [MFA guide](/reference/mfa/) nearby.

## API Key Security

### Use Specific Scopes

Never use `*` for production workloads. Grant only the permissions each service actually needs:
```csharp
// Bad: Full access
{ "scopes": ["*"] }

// Good: Specific permissions
{ "scopes": ["database:read"] }  // Read-only service
{ "scopes": ["database:read", "database:write"] }  // Backend API
{ "scopes": ["repository:read", "repository:write"] }  // Specific to repositories
```

### Separate Keys by Environment

Use different API keys for different environments. That way, a problem in one environment doesn't automatically become a problem everywhere.

| Environment | Key Name | Scopes |
|-------------|----------|--------|
| Production | prod-backend | database:read, database:write |
| Staging | staging-backend | database:read, database:write |
| Development | dev-local | database:* |
| CI/CD | ci-tests | database:read |

### Rotate Keys Regularly

API keys should be rotated every 90 days:

1. Create a new key with the same scopes
2. Update your application configuration
3. Deploy and verify
4. Revoke the old key

### Never Commit Keys

API keys should never be in source control:
```csharp
// Bad: Hardcoded
var apiKey = "tsauth_abc123...";

// Good: Environment variable
var apiKey = Environment.GetEnvironmentVariable("TERRASCALE_API_KEY");

// Good: Secret manager
var apiKey = await secretManager.GetSecretAsync("terrascale-api-key");
```

Add these patterns to your `.gitignore` if they aren't already there:
```
.env
.env.local
*.env
appsettings.Development.json
```

## Account Security

### Protect Your Email Inbox

Passwordless email sign-in uses a link sent to the verified address, so protecting the account means protecting the mailbox. ADR-0041 makes this the target account model, but the current public contract still exposes legacy account credential routes while the migration is incomplete. If you use passwordless sign-in:

- Use a dedicated mailbox for production accounts, not a shared personal address
- Enable your email provider's own multi-factor authentication and phishing-resistant sign-in
- Treat unexpected TerraScale sign-in emails as a signal that someone else knows the address — don't click the link, and review active sessions

### Review Active Sessions

Periodically check Settings > Security > Sessions:

- Look for unfamiliar locations or devices
- Revoke any sessions you don't recognize
- Consider revoking all sessions after any suspected mailbox compromise

## Team Security

### Principle of Least Privilege

Assign the minimum role needed:

| Role | Use Case |
|------|----------|
| Owner | Only the account creator (one person) |
| Admin | Team leads who need to manage members |
| Member | Developers who create and manage resources |
| Read-only | Auditors, analysts, support staff |

### Audit Team Members

Review your team quarterly:

- Remove people who've left the organization
- Downgrade permissions that are no longer needed
- Verify all member email addresses are verified and current

### Handle Departures Promptly

When someone leaves:

1. Remove them from the organization immediately
2. Revoke any API keys they created
3. Review any resources they had access to
4. Consider rotating shared credentials

## Network Security

### Use HTTPS Only

All TerraScale Platform APIs require HTTPS. Never attempt to use HTTP.

### Validate TLS Certificates

Don't disable certificate validation in production:
```csharp
// Never do this in production
ServicePointManager.ServerCertificateValidationCallback = (s, c, ch, e) => true;
```

### Network access controls

The current public contract does not document IP-based network restrictions. Do not assume that a plan includes them. Use project scopes, environment separation, and the authentication controls documented in the public references.

## Data Security

### Sensitive Data Handling

Don't store highly sensitive data directly unless you have a clear reason and a documented handling plan:
```csharp
// Bad: Storing raw SSN
["ssn"] = "123-45-6789"

// Better: Store a hash or encrypted value
["ssnHash"] = Hash("123-45-6789")

// Best: Don't store it at all if you don't need it
```

### Encryption at rest

TerraScale uses qualified storage and key-management controls for data at rest. The public security policy does not name an algorithm until production evidence covers every relevant path. Encryption does not replace authorization, tenant isolation, recovery, or deletion controls.

### Encryption in transit

Customer traffic requires TLS 1.2 or newer. Keep certificate validation enabled and do not infer a stronger protocol floor from a client or network default.

Why this matters: infrastructure defaults can protect you from broad classes of mistakes, but they don't replace application-level decisions like scoping secrets correctly or choosing what data should live in the database at all.

## Monitoring and Alerting

### Enable Audit Logs

Track who's accessing your data:

- API key usage by operation type
- Failed authentication attempts
- Administrative actions (member changes, key creation)

### Set Up Alerts

Configure alerts for:

- Unusual API usage patterns
- Failed authentication spikes
- New API key creation
- Team member changes

### Regular Reviews

Monthly security checklist:

- [ ] Review API key usage - any surprises?
- [ ] Check for inactive API keys - revoke them
- [ ] Verify team member list is accurate
- [ ] Confirm all team member emails are verified and current
- [ ] Review any security alerts

## Incident Response

### If an API Key is Compromised

1. **Revoke immediately** - Don't wait, revoke the key now
2. **Create a new key** - Generate a replacement
3. **Update applications** - Deploy the new key
4. **Audit usage** - Check logs for unauthorized access
5. **Review data** - Look for any data modifications
6. **Document** - Record what happened and how you responded

### If an Account is Compromised

1. **Secure the mailbox first** - Reclaim control of the email inbox through your provider
2. **Revoke all sessions**
3. **Review and revoke API keys**
4. **Request a fresh sign-in link** once the mailbox is secure
5. **Check for unauthorized team members**
6. **Contact support** at support@terrascale.tech

## Summary

Security is everyone's responsibility. The goal is not perfection. The goal is to make the safe path the normal path.

1. Use specific API key scopes
2. Rotate keys every 90 days
3. Protect the email inbox that owns each account
4. Use the principle of least privilege
5. Never commit secrets to source control
6. Monitor for unusual activity
7. Have an incident response plan

Questions about security? Contact security@terrascale.tech. For general operational guidance, the [best practices reference](/reference/best-practices/) is also worth bookmarking.
