# Fail over only within selected regions

When a selected region becomes unavailable, TerraScale routes traffic to another healthy selected region and keeps reads and writes available under the documented eventual-consistency model. It exposes the degraded region and replication state to the customer. It never fails customer content over to an unselected serving region.
