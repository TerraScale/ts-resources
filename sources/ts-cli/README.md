# TerraScale CLI

A standalone **Go 1.27** CLI built with **Cobra** and **Lip Gloss**. There is no
full-screen TUI. Commands have searchable help, shell completion, readable
terminal tables, color that honors `NO_COLOR`, and lossless JSON for scripts.

Use `ts` as the primary command. `terrascale` provides the same commands and
shares the same configuration and saved credentials.

## Install and run

```sh
make build
./bin/ts --help
# Put bin/ts and bin/terrascale on PATH to use either name anywhere.
```

Install both names directly into your Go binary directory:

```sh
go install -mod=readonly ./cmd/ts ./cmd/terrascale
```

Development:

```sh
go run -mod=readonly ./cmd/ts --help
```

Dependencies are pinned in `go.mod` and verified by `go.sum`. The first build
downloads them into Go's module cache. Building requires Go, with no .NET or C
compiler. Make targets select module mode explicitly because `vendor` retains
repository guidance files.

## Get started with the dashboard

```sh
ts auth login
# Confirm the displayed code in the dashboard. The CLI receives its token automatically.
ts context show
ts overview show
ts databases list --project-id PROJECT_ID
```

Dashboard commands use a personal access token, exactly like the dashboard's
published authenticated feature API. API keys for regional databases are
separate credentials. `auth status` and `config show` never display either
credential. Store secrets outside shell history and source control.

`auth login` prints a short code and polls while you approve it in the dashboard.
It makes outbound requests only: no localhost server, redirect URI, or browser
callback is used. After approval, the credential is saved privately and dashboard
commands work immediately. Use `--no-open` to enter the code from another browser
or device; the CLI continues polling. Codes expire after 10 minutes. Denial,
expiry, and Ctrl+C leave existing local credentials unchanged.

The dashboard issues a 30-day personal token after browser sign-in and current
password confirmation. Revoke it from the profile's Access tokens page when
needed. Existing tokens can still be imported with
`auth import --dashboard --token-stdin < dashboard-token.txt`.

`--dashboard-url` or `TERRASCALE_DASHBOARD_URL` selects another dashboard origin.
`--dashboard-token` or `TERRASCALE_DASHBOARD_TOKEN` overrides the stored personal
access token. Stored tokens are bound to their origin; changing an origin clears
its stored credential.

## Dashboard features

The CLI exposes **all 110 currently published dashboard actions** as named
commands. See the [complete command reference](docs/dashboard-commands.md).

| Area | Commands |
| --- | --- |
| Workspaces and projects | `organizations`, `projects`, `context`, `overview`, `onboarding` |
| Data and databases | `databases`, `data`, `backups`, `subscriptions` |
| Credentials and access | `keys`, `access`, `authentication` |
| Billing and usage | `billing`, `usage` |
| Account and operations | `profile`, `settings`, `notifications`, `audit` |
| Platform administration | `admin` (requires the platform administrator role) |

```sh
ts organizations create --name 'My team'
ts projects create --name app --region GRU
ts databases create --name app --region GRU
ts data list-documents --database-id DB_ID --collection users
ts data create-document --database-id DB_ID --collection users \
  --document '{"name":"Ada"}'
ts keys create --name deploy --scopes database:read,database:write
ts access invite --email teammate@example.com --role member
ts billing plans
ts billing show
ts usage show
ts authentication sections
ts usage set-spending-controls \
  --project-caps '[{"id":"PROJECT_ID","capCents":5000}]'
```

Use `--organization-id` and `--project-id` to select a scope. Their environment
counterparts are `TERRASCALE_ORGANIZATION_ID` and `TERRASCALE_PROJECT_ID`.
Omitted scopes use the account's saved dashboard selection. Permissions and plan
limits are enforced by the dashboard; showing an admin command does not grant
admin access.

Complex arguments and lists of objects accept JSON, `@file.json`, or `@-` for stdin. The `--input`
option supplies a complete argument object using the dashboard's camelCase
property names; individual flags override it.

```sh
ts data patch-document --database-id DB_ID --collection users \
  --document-id ada --patch @changes.json
ts data create-document --input @request.json --dry-run
ts databases delete --database-id DB_ID --confirm-name app --yes
ts databases list --json | jq '.databases[].id'
```

Destructive actions require `--yes`. `--dry-run` validates and prints the named
action and arguments without sending any request. Request and response JSON
preserve the exact numbers supplied to the CLI or returned by the server. Human
output sanitizes terminal control characters from server strings.

The dashboard MCP backend currently rounds document integers beyond the safe
IEEE-754 integer range: the integration fixture stored `9007199254740993` as
`9007199254740992`. Exact CLI serialization cannot repair server-side rounding.
Use the regional data commands for documents requiring exact large integers
until the dashboard backend supports them.

### Account-security and payment flows

The dashboard's current personal-token API does **not** expose password changes,
verified email changes, MFA/passkey enrollment, or initial personal-token
creation through a token-authenticated request. `profile change-password`, `change-email`,
`mfa`, `passkeys`, `security`, and `create-access-token` open the dashboard's
existing secure browser flow. `--no-open`, `--json`, or redirected output prints
the URL instead. These commands do not claim to complete a browser-only action.
Token-authenticated terminal implementations of those flows need backend API
support. `organizations cancel-ownership-transfer` opens the current dashboard
organization because cancellation is also not published as a dashboard tool.

Billing checkout and the billing portal return the same provider URLs the
dashboard uses. Payments and provider-side verification still complete through
the provider's secure flow. The CLI preserves the dashboard's current behavior;
local tests do not establish production billing or real MFA/WebAuthn behavior.

The same command groups are available under `ts dashboard`.
`dashboard tools list` discovers the live server's role-filtered actions and
schemas. `dashboard tools call TOOL --input @request.json` can use newly published
actions; destructive calls use the server's own confirmation annotations.

## Regional API and developer commands

The TerraBase producer contract remains pinned under `contracts/v1`. Commands
validate media types, response shapes, and embedded artifact digests.

```sh
ts config set --api-url https://gru.api.terrascale.tech
ts auth import --token-stdin < api-key.txt
ts doctor
ts db list
ts db create app --placement GRU --operation-id create-app-1
ts operations wait create-app-1 --timeout 5m
ts sql app 'SELECT * FROM users WHERE age >= :age' --parameters '{"age":18}'
ts push --database app
ts diff --database app
ts codegen --language go --out generated/schema.go
ts dev app --branch my-dev --no-log-tail
```

Member-data commands use public Atlas bootstrap followed by authenticated
scoped discovery for the requested tenant, database, and shard. Prefer the
nearest currently eligible `https://<region>.api.terrascale.tech` endpoint;
GRU uses `https://gru.api.terrascale.tech`. Pins are bounded by the original
scoped expiry and at most 10 seconds remaining; catalog availability alone
cannot select a database endpoint.

`https://api.terrascale.tech` is an optional slower, costlier global Atlas
proxy that must admit the same scope and select an eligible target before
forwarding. Product requests use their separately configured owning service;
database creation without placement requires an admitted management authority.
Explicit regional or custom origins retain exact-scope admission and TLS
verification. `TERRASCALE_ATLAS_URL` overrides Atlas for development.
Credentials and writes are never forwarded through HTTP redirects. Flags
override environment variables, which override local configuration.

`TERRASCALE_API_KEY`, `TERRASCALE_ACCESS_TOKEN`, and `TERRASCALE_TOKEN` override
stored API credentials. Native `auth login --api` uses the published device flow and
refreshes short-lived access tokens under a process-safe file lock.
`--auth-base-url` or `TERRASCALE_AUTH_BASE_URL` overrides the issuer.
`auth logout` revokes native refresh tokens and removes local credentials;
imported API keys and dashboard personal tokens must be revoked through their
issuer (`keys revoke` or `profile revoke-access-token`).

Configuration is stored in the user configuration directory at
`terrascale/config.json`, or at `TERRASCALE_CONFIG_FILE`. Updates atomically
replace a private file; symlinks and public configuration files are rejected.

Database create, branch, and backup restore return provisioning operations;
HTTP acceptance does not mean readiness. `operations get` and `operations wait`
inspect the original operation without repeating writes. Deletion requires
`--yes`, supports `--dry-run`, and returns a durable identity. Inspect an uncertain
outcome before retrying.

```sh
ts db delete app --operation-id delete-app-1 --dry-run
ts db delete app --operation-id delete-app-1 --yes
ts db deletion get app delete-app-1
ts db deletion watch app delete-app-1 --timeout 5m
ts index wait app --collection users --timeout 2m
```

### Data transfers and code generation

```sh
ts import records.jsonl --database app --collection users --dry-run
ts import records.jsonl --database app --collection users --skip-records 120
ts db export app --collection users --output users.jsonl \
  --manifest users.manifest.json
ts db export app --format lossless
ts dev app --branch my-dev --seed seed.jsonl --seed-collection users \
  --watch --language typescript --codegen-out src/generated.ts
```

Import supports JSONL, CSV, MongoDB, Cosmos DB, and DynamoDB data. Skipped records
are validated and generate no writes. Failure reports newly confirmed records;
resolve uncertain write outcomes before adjusting `--skip-records`.

JSONL export resumes one collection using `--after LAST_COMPLETE_ID` and appends
to the output. Remove an incomplete final line before resuming after an output
failure. Current-data export is not a consistent snapshot. Use the server's
lossless export for recovery guarantees when available. Export manifests record
the scope, whole-file record count, and SHA-256 of the exact output bytes.
Lossless artifact downloads verify the producer's byte length and BLAKE3 checksum
before replacing the destination file.

Code generation supports Go, TypeScript, C#, and Rust consumer bindings. Bytes use
standard padded base64 JSON; timestamps use epoch milliseconds. Invalid watch
edits preserve the last generated file. Published development faults are bounded
and never affect durability.

## Status and shell completion

```sh
ts status
ts status --json | jq -r .status.indicator
ts completion bash > /etc/bash_completion.d/ts
ts completion zsh > "${fpath[1]}/_ts"
```

Use `terrascale completion bash` or `terrascale completion zsh` when installing
completion for the alternate executable name.

Status needs no credential. `--url` or `TERRASCALE_STATUS_URL` selects a
Statuspage-compatible summary. Its exit codes are `0` operational, `1` degraded
or invalid usage, and `2` unavailable or invalid response. The default deadline
is 5 seconds, with a maximum of one minute.

## Verify and maintain

```sh
make check
make test
make audit
make build
```

`make test` runs Go tests with the race detector. Checks include contract pin
verification, Go formatting and vet, contract tooling tests, and qualification
runner tests. The vulnerability audit is pinned to govulncheck v1.8.0.

Regenerate dashboard command metadata from the authoritative dashboard source:

```sh
make dashboard-catalog
```

This only reads source; it does not connect to a service or invoke an action.
Contract updates use `make contracts` with an immutable `CONTRACT_URL`, or an
explicit development-only `CONTRACT_SOURCE` from the producer. Consumer SDKs
are not contract sources.

The [real cloud qualification runner](scripts/cloud-dev/README.md) and
[all-SDK journey runner](scripts/qualification/README.md) remain available.
They require explicitly authorized test services and credentials. Local tests
and fixture servers do not qualify the real cloud journey.
