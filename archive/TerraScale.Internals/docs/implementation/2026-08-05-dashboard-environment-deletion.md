# Dashboard environment deletion

Dashboard now deletes a database environment through its same-origin nested route after a typed-name
confirmation. The handler validates the Dashboard session, resolves the target through typed public
SDK `getEnvironment`, rejects a missing or mismatched name before delete, and calls only typed public
SDK `client.databases.deleteEnvironment` with the selected project context. If persisted page-data
reload fails after a successful delete, the Dashboard preserves its previous view and clearly reports
that the mutation succeeded but the refresh failed.

The delete request sends the exact typed confirmation value. Invalid database or environment ULIDs are
rejected as 400 before project-context resolution, SDK lookup, or mutation. Project-context failures
retain their original HTTP status; scoped environment lookup maps only a 404 missing target to 400 and
preserves authentication and service failures. The live E2E covers omitted and mismatched names,
malformed database/environment IDs, malformed input under a bogus session, and a valid path returning
401 under that session before verifying the real environment remains for confirmed UI deletion.

Validation: static Dashboard checks are recorded with the change. Live Playwright execution requires
the shared Aspire topology lease and is not started when that lease is held.
