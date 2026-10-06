---
title: Account Registration
description: Email-only signup and verification flow.
sidebar:
  order: 1
---

TerraScale provides a passwordless email signup path: provide an email address and verify it with the code sent to the mailbox. ADR-0041 makes this the target account model, but the current published contract still includes the legacy password signup route while the migration is incomplete.

In the target Dashboard self-registration flow, identity and email verification appear as the completed first step, then the User is guided through the first Organization, Project, and logical Database, followed by payment-card verification for signup abuse control. Card verification will create no charge, subscription, paid trial, or automatic renewal. The User will then choose either no paid plan and no automatic renewal, retaining the Developer allowance, or Starter or Pro with monthly automatic renewal and an eligible first 30 days at no charge. Invited-user onboarding remains separate.

The target flow is tracked in [TerraScale.Internals issue 30](https://git.terrascale.tech/TerraScale/TerraScale.Internals/issues/30) and its typed SDK work in [TerraScale.TypeScript issue 6](https://git.terrascale.tech/TerraScale/TerraScale.TypeScript/issues/6). It is not yet the released behavior.

## Verify Email

```http
POST /api/v1/auth/password/verify-email
```

```json
{
  "pendingAuthenticationToken": "pending-token",
  "code": "123456"
}
```

## Resend Verification

```http
POST /api/v1/auth/password/resend-verification
```

```json
{
  "pendingAuthenticationToken": "pending-token",
  "verifyUrl": "https://app.example.test/verify"
}
```

Project-scoped signup and verification routes are under `/api/v1/projects/{projectId}/auth/signup`, `/verify-email`, and `/resend-verification`.

## TypeScript SDK

```ts
await client.auth.verifyEmail({
  pendingAuthenticationToken: 'pending-token',
  code: '123456'
});
```

## C# Status

The current `TerraScale.DotNet` SDK does not expose signup or verification helpers.

## Next Steps

- [Login](/account/login/)
- [Authentication](/reference/authentication/)
- [Profile](/account/profile/)
