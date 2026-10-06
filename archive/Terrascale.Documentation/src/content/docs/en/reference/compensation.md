---
title: Public Alpha allowance behavior
description: Hard plan allowances, monthly operation resets, and usage reduction during Public Alpha.
---

Public Alpha uses hard storage and operation-unit allowances. This page records what happens when an organization approaches or reaches a plan limit.

## Monthly operation units

Unused operation units do not roll over. The allowance resets at the start of the next calendar month. TerraScale warns customers as they approach the allowance, then rejects new billable work that would exceed it.

Reads, project export, deletion, and work that reduces usage remain available after a hard allowance is reached. Stored data is not deleted merely because an allowance was reached. Public Alpha has no paid overages and does not bill customer egress.

## Example

If a Developer organization has used 9,999 of its 10,000 monthly operation units, a new billable operation that needs two units is rejected. A read, export, delete, or usage-reducing operation remains available when its contract permits it. The 10,000-unit allowance resets at the next calendar month, without carrying unused units forward.

See [Pricing and metering](/reference/pricing/), [Public Alpha plans](/reference/plans/), and [Billing lifecycle](/reference/billing/).
