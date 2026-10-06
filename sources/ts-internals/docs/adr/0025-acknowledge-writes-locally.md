# Acknowledge public writes locally

`RegionalDurable` is the default. It acknowledges a mutation only after the
local SQLite writer and RF=2 journal follower make it durable. It does not wait
for another region.

`GlobalDurable` is the WAN-bound alternative. It requires durable
acknowledgement from at least two active regions and fails closed when fewer
than two regions are active. A single-member acceptance is never a successful
production write.
