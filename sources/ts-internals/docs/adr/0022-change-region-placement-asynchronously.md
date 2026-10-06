# Change region placement asynchronously

Placement is selected per database. Database API owns the public operation,
Orchestrator owns placement intent, and TerraBase owns member assignment,
snapshot catch-up, journal catch-up, and repair.

A newly selected region does not serve customer traffic until its data catches
up and routing publishes the new placement generation. A removed region drains
traffic and replication before TerraScale deletes its active copies. The
operation exposes progress and failure states and supports idempotent retry.
