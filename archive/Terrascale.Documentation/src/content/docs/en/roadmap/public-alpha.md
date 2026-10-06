---
title: Public Alpha
description: What TerraScale Public Alpha includes today, where the current limits are, and what is still being built.
sidebar:
  order: 2
---

Public Alpha is the current release stage for TerraScale. The platform is ready for real evaluation and early workloads, but some capabilities are still evolving as the team gathers usage data and feedback.

## What Public Alpha Means

Public Alpha means the core platform is functional and available to users today. You can build against it, test real traffic patterns, and evaluate the supported public API, SDK, dashboard, TQL, queue, auth, and payments surfaces. At the same time, this stage is still shaped by feedback, so limits may change and some important live Stripe, email-provider, OAuth-provider, and production-like proofs are still on the way.

For the broader roadmap context, see the [Public Roadmap](/roadmap/).

## Available Features

- Versioned `/api/v1` HTTP JSON API support
- TQL query interface access
- C# SDK support
- TypeScript SDK support
- Dashboard workflows backed by the public API and SDK surface
- TerraBase-backed typed collections and schema operations
- Queue, Auth, and Payments local/default-CI workflows
- Launch-region model for `gru`, `sfo`, and `fra`

If you want to start using the platform now, see the [Getting Started guide](/guides/getting-started/).

## Current Limits

- Current launch-region validation is limited to `gru`, `sfo`, and `fra`
- Rate limits apply during Public Alpha
- Live Stripe, email-provider, and OAuth-provider workflows require operator-supplied credentials and webhook/account setup
- Production-like multi-region outage evidence is still a release blocker

These guardrails help the team keep the current platform reliable while Public Alpha expands.

## What's Not Available Yet

The following items are planned, but they are not part of the current Public Alpha release:

- Production-like multi-region outage proof
- Live Stripe payment sandbox proof
- Full production-like multi-region TerraBase/NATS/Fabric outage proof
- Live Sentry and production Alertmanager proof
- Live OAuth/IdP provider proof
- Live Stripe payment and email-provider sandbox proof
- Automatic caching

See the [Public Alpha Roadmap](/roadmap/public-alpha-roadmap/) for the next set of priorities.

## How to Give Feedback

Public Alpha priorities are heavily influenced by real user feedback. Join the [Discord community](https://discord.gg/8Zr2Nw9g) to share ideas, report friction, and discuss your use case with the team.

For direct support or roadmap feedback, email [support@terrascale.tech](mailto:support@terrascale.tech).
