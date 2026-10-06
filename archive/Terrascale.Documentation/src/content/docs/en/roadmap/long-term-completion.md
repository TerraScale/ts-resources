---
title: Long-Term Completion Plan
description: The acceptance-driven roadmap for completing TerraScale across database, auth, queue, payments, SDKs, dashboard, GitOps, and operations.
sidebar:
  order: 5
headingBadge:
  text: Planned
  variant: secondary
---


## Final Product Goal


## Milestones

| Milestone | Outcome |
| --- | --- |
| Decisions and baseline | Public API transport, region/provider ADRs, MVP matrices, and one local E2E command. |
| Database MVP | Typed collections, automatic safe schema evolution, query support, API keys, SDK repository APIs, and dashboard database flows. |
| Auth MVP | Signup, email-only login with sign-in links, verification, sessions, invitations, RBAC, and payment-aware account foundations. |
| Queue MVP | NATS JetStream runtime, Fabric NATS topology, send/receive/ack/lease/DLQ/redrive, SDKs, dashboard queue pages, and email/export worker validation. |
| Fabric and multi-region | Standalone Fabric adoption, node registration, placement, routing, `gru`, `sfo`, `fra` topology, and outage simulation. |
| Beta hardening | Observability, email providers, direct Stripe payments, Auth and Payments SaaS builder features, security, docs, samples, and release automation. |

## MVP Scope

MVP freezes the smallest complete platform that can be finished end to end:

- Public REST HTTP APIs with WebSockets or SSE for browser real-time flows.
- Database create, collection create, typed repository CRUD, query, pagination, safe schema evolution, and operation history.
- Auth signup, verification, email-only sign-in links, refresh rotation, sessions, organization membership, invitations, API keys, and payment-aware account summaries.
- Queue create, send, receive, acknowledge, abandon, lease extension, DLQ, redrive, retry policy, stats, and NATS JetStream verification.
- Provider-agnostic email delivery with local Mailpit and tested provider adapters.
- Direct Stripe payments with deterministic queue and webhook tests, checkout sessions, billing portal sessions, signed webhooks, persisted billing projection, and live Stripe sandbox proof blocked until credentials are supplied.
- TypeScript and C# SDKs that use the public HTTP API.
- Dashboard-specific endpoints and orchestration live only in the Dashboard full-stack project. Its server routes use typed TypeScript SDK methods as an ordinary external TerraScale.Platform user under the same public contracts, authentication, authorization, and tenant boundaries as customer applications.

## Final Acceptance Scenarios


1. Account and organization creation with email verification, login, refresh, and TerraBase metadata checks.
2. Database and schema evolution across `gru`, `sfo`, and `fra`.
3. TQL query validation with explain plans and standard errors.
4. Queue processing through NATS JetStream, including DLQ and redrive.
5. Stripe checkout, signed webhooks, subscriptions, entitlements, Auth role updates, usage, invoices, and event replay safety through TerraScale Payments and TerraScale.Queue, with deterministic queue/webhook coverage and opt-in live Stripe sandbox evidence.
6. Advanced project-auth flows with MFA, passkeys, OAuth providers, invitations, API key scopes, and audit for the project-scoped Authentication product.
7. Dashboard route coverage with real backend data.
8. Multi-region Fabric topology, routing, outage, and recovery.
10. Observability checks for correlated logs, traces, metrics, alerts, and operational status.

## Current Acceptance Rule

Features described on this page are not public availability claims. A feature becomes accepted only when the implementation, SDKs, dashboard, docs, and tests prove the behavior through the intended public surface and durable backend state.

## Related Concepts

Read [Platform Concepts](/guides/platform-concepts/) for the product concepts behind this roadmap.
