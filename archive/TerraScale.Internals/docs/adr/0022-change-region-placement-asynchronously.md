# Change region placement asynchronously

A newly selected region does not serve customer traffic until its data catches up. A removed region drains traffic and replication before TerraScale deletes its customer data. The operation exposes progress and failure states, supports idempotent retry, and continues billing the old placement until data removal completes.
