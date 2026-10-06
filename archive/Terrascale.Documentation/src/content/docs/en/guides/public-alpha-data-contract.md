---
title: Public Alpha data contract
description: Data ownership, regional routing, consistency, placement, and monitoring semantics.
sidebar:
  order: 3
---

This guide defines the customer-visible regional data contract for Public Alpha. It does not promise an uptime percentage or a maximum replication delay.

## Data model

An **Organization** owns a subscription, members, and Projects. A **Project** is the tenant and authorization boundary for application resources. A **Database** is a named logical data container inside one Project and records the selected regions. An **Environment** is a virtual namespace inside one Database. A **Repository** defines a named document collection and its schema inside an Environment. A **Document** is the versioned customer JSON value stored in a Repository.

Environment names are unique within a Database. The Environment kind does not provide identity, so a Database may contain multiple same-kind Environments with different names. For example, `review-42` and `review-57` may both have the `Preview` kind.

## Replication and write acknowledgement

Selected regions use active-active asynchronous replication. A successful write means the receiving region durably accepted the write. This is durable local write acknowledgement. Other selected regions receive it later.

Concurrent writes use last-write-wins by default. Applications that must reject a stale update use an optional conditional mutation with the last observed document version. A failed condition does not overwrite the newer value. Public Alpha has no majority write mode.

This contract has no bounded replication-lag promise. A local acknowledgement does not say that every selected region has converged.

## Session consistency

A successful mutation returns a session consistency token. Send that token on a later read when the session must observe that mutation. The service either returns a version at least as recent as the token or reports that the selected serving path cannot satisfy it yet.

```text
write document A -> receive session token T
read document A with T -> observe that write or receive an unsatisfied-session result
```

Clients may use stale-read opt-in for work that prefers an older available replica over waiting for session visibility. The opt-in applies to that read. It does not change the Database's write or conflict policy.

## Equivalent client outcomes

The launch qualification fixture performs one repository document mutation, then a read that carries the returned session token. The raw API sends the versioned `/api/v1` request and token, the .NET SDK uses its typed document client, the TypeScript SDK uses its typed document client, and MCP performs the corresponding scoped read when the tool exposes it. All four must either observe the mutation at or above the token's version, or return the documented unsatisfied-session result. A client must not silently downgrade the request to an unscoped or stale read.

The same fixture also checks a conditional mutation with an old document version. The API, .NET, TypeScript, and MCP surfaces must all preserve the newer value and return the conditional-failure outcome. Qualification records the exact API revision and package versions; a source build or private route is not evidence.

## Endpoint behavior

Every routing choice remains inside the Database's selected regions.

| Endpoint mode | Behavior |
| --- | --- |
| Global endpoint | Chooses the nearest healthy selected region using the routing service's current observations. |
| Preferred regional endpoint | Tries the named selected region first, then may use another healthy selected region. |
| Failover regional endpoint | Uses the named selected region when healthy and follows the Database's configured selected-region failover order when it is not. |
| Strict regional endpoint | Uses only the named selected region and returns an unavailable result rather than using another region. |

The routing layer never serves from an unselected region. Customer content remains in selected regions. Geographic distance is an estimate and does not predict current API latency or replication convergence.

## Region placement changes

Adding a selected region creates a placement and starts catch-up from an existing selected region. The operation reports progress until the placement can serve its intended traffic. A failed step remains retryable and reports the next retry state instead of pretending the placement is ready.

Removing a region first moves it into drain. TerraScale stops assigning new work there, completes or safely retries in-flight placement work, and removes the placement only after the drain finishes. A failed drain remains visible and retryable.

Storage usage follows actual placement. Bytes begin contributing when TerraScale stores Customer content in the added region, including during catch-up. Bytes stop contributing after the removed placement no longer stores that content. The requested region list alone does not determine a charge.

## Monitoring values

Monitoring keeps unlike signals separate:

| Value | What it reports | Time and status rule |
| --- | --- | --- |
| Replication health | Whether each selected placement is accepting and applying replication work | Includes the observation time and a status that distinguishes a current observation, stale data, and unavailable data. |
| Convergence | Whether known versions have reached the observed placements | Includes the observation time. It is not a time guarantee. |
| Replication lag | A measured delay for a specific observed path and window | Includes the sample window and observation time. Missing data stays unavailable rather than becoming zero. |
| Conflicts | Detected concurrent-version resolutions | Includes the counted window and observation time. |
| Estimated network distance latency | A geographic routing estimate | Marked as estimated with the estimate time. |
| Measured API latency | End-to-end API request samples | Includes the sample window, percentile, region, and observation time. |
| Probe latency | Synthetic probe samples | Identifies the probe path, sample window, and observation time. |

Every displayed value carries its own status and observation time. A stale, unavailable, or estimated value cannot be presented as a current measurement. None of these values creates a bounded replication-lag promise or an uptime SLA.

## Client outcomes

The raw API, .NET SDK, TypeScript SDK, and MCP must produce the same observable result for an operation before that client is listed as qualified. The release evidence records the exact client and API versions. See [Public Alpha clients](/guides/public-alpha-clients/) for current qualification state.
