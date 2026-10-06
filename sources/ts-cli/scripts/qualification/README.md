# Real all-SDK CLI consumer

`cli-real-journey.mjs` is the noninteractive CLI leg for the coordinator. Run
one phase per process:

```sh
node scripts/qualification/cli-real-journey.mjs seed
node scripts/qualification/cli-real-journey.mjs verify
node scripts/qualification/cli-real-journey.mjs exercise
node scripts/qualification/cli-real-journey.mjs cleanup
```

The coordinator supplies `TERRASCALE_API_URL`, `TERRASCALE_PROJECT_ID`,
`TERRASCALE_DATABASE_ID`, `TERRASCALE_JOURNEY_RUN_ID`, `TERRASCALE_API_KEY`,
`TERRASCALE_CLI_PATH`, and its expected `TERRASCALE_CLI_SHA256`. An optional
`TERRASCALE_DENY_API_KEY` runs a separate denied SQL check,
`TERRASCALE_COLLECTION` selects the collection (default `sdk_journey`), and
`TERRASCALE_CLI_TIMEOUT_MS` bounds each CLI invocation (default 30000). The executable must
be an absolute regular executable file whose SHA-256 matches before any CLI
command is started. Credentials remain environment-only and are never written
to logs or arguments.

Seed and exercise use the public JSONL `import` command; reads and the
parameterized peer check use public `sql`. Verification requires exactly the
five IDs `${RUN_ID}-{typescript,go,rust,dotnet,cli}` and each row body must be
exactly `{sdk, runId}`. Invalid SQL must return the CLI's typed SQL validation
error; an optional deny key must return HTTP 401/403 (transport failure alone
is not accepted). The CLI has
no public document-delete command, so `cleanup` records delegation to the
coordinator, whose database teardown owns removal of the run records.

`node --test scripts/qualification/cli-real-journey.test.mjs` runs its tests
against a fake executable; they are local contract evidence only and do not
qualify a live service or CLI artifact.
