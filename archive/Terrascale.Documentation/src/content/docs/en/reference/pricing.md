---
title: Pricing and metering
description: Public Alpha storage and operation-unit rules with worked examples.
sidebar:
  order: 7
---

TerraScale measures storage across regions and database work in operation units. Public Alpha uses hard plan allowances and does not charge egress. Billing, payment methods, and billing history belong to the Organization, not directly to the User.

## Storage across regions

Storage usage is the sum of uncompressed customer-document bytes stored in every selected region. A 100 MB dataset stored in three regions consumes 300 MB of storage usage. The Developer 1 GB allowance uses the same calculation.

Per-database storage displays are estimates. TerraScale applies the plan allowance to exact project usage aggregated at the owning organization.

## Operation units

One operation unit covers each started 4 KiB, or 4,096 bytes, of uncompressed customer-document data processed by a billable database operation.

- Reads charge the bytes in documents returned from the serving region.
- An empty successful query costs one unit.
- Creates, replacements, and updates charge the document units once in each selected region. This includes the receiving region and every replication destination.
- A batch rounds each document separately, then adds the document units.
- Deletes cost one unit per selected region.

### Rounding

A 1-byte document and a 4,096-byte document each cost one unit. A 4,097-byte document costs two units.

### Multi-region write

Writing a 5 KiB document uses two document units. With three selected regions, that write costs six operation units. Replication does not add a second charge.

### Batch

A batch writes documents of 1 KiB, 4 KiB, and 5 KiB to two selected regions. They round to one, one, and two units per region. The batch costs eight units: `(1 + 1 + 2) × 2`.

### Query and delete

A query that returns no documents costs one unit. A query returning three 2 KiB documents costs three units because each returned document rounds separately. Deleting one document from a three-region database costs three units.

## Work that is not charged

Rejected requests, server failures, internal retries, indexing, backups, monitoring, internal repair, and replication after the selected-region write multiplication do not add operation units. Customer egress is visible in usage reporting but is not billed during Public Alpha.

## At an allowance

When new billable work would exceed an allowance, TerraScale rejects it. Existing reads, project export, deletion, and work that reduces usage remain available. Stored data is not deleted merely because an allowance was reached.

See [Public Alpha plans](/reference/plans/) for each plan's monthly allowances.
