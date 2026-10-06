# Fail over only within selected regions

The selected set belongs to the database. Every selected region stores every
key-range shard and is writable. Failover cannot weaken RF=2
`RegionalDurable`.

When a selected region becomes unavailable, TerraScale routes eligible traffic
to another healthy selected region. It exposes the degraded region,
replication state, and any unmet durability requirement to the customer. It
never serves customer content from an unselected region.
