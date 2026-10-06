---
title: Public Alpha Roadmap
description: Planned improvements for TerraScale during Public Alpha, including performance automation and higher database limits.
sidebar:
  order: 3
---

This page covers the main improvements planned during Public Alpha. The focus is straightforward: make TerraScale faster to adopt, easier to tune, and more capable under real workloads.

For the full product view, see the [Public Roadmap](/roadmap/). For the current release stage, see [Public Alpha](/roadmap/public-alpha/).

## Overview

Public Alpha is already usable, but several important improvements are still ahead. The roadmap in this stage is centered on performance automation, automatic schema evolution, better cache behavior, and production-like proof for the supported launch-region model.

## Planned Features

### Auto Indexing

TerraScale already has default-CI and deterministic coverage for workload-informed auto-index candidates, including repeated JSON property query shapes. The remaining roadmap work is broader DevHost/runtime cutover evidence, policy tuning from real workloads, and operator visibility that explains why a generated index was selected.

### Auto Caching with Invalidation

Automatic query result caching is planned to improve read performance without requiring teams to hand-manage every cache decision. Cache invalidation is part of the design so cached results stay aligned with underlying data changes.

### Automatic Schema Evolution

TerraScale makes model changes feel automatic from the SDK for safe changes while TerraBase storage remains typed and schema-operation-backed internally. The SDK and control plane infer safe collection and index changes, track schema versions, and run background rewrites so application developers do not need storage upgrade code for ordinary model evolution.

### Production-Like Launch-Region Proof

The launch-region model is `gru`, `sfo`, and `fra`. The roadmap includes production-like TerraBase/NATS/Fabric outage proof, live Vault reconciliation, live Sentry delivery, and production Alertmanager routing before the platform can claim stable multi-region readiness.

### Manual Cache Controls

Alongside automatic caching, TerraScale plans to add manual cache controls for teams that want tighter control over behavior. That includes LRU eviction and explicit cache management for workloads that need predictable tuning.

## Timeline Notes

This roadmap is prioritized by user feedback and real usage patterns. There are no fixed public dates yet, and the order may shift as the team learns more from production-like workloads during Public Alpha.

## Request a Feature

Want to influence the roadmap? Join the [Discord community](https://discord.gg/8Zr2Nw9g) and share what your workload needs next.

For direct requests or follow-up questions, email [support@terrascale.tech](mailto:support@terrascale.tech).
