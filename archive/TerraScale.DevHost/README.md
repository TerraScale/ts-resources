# TerraScale DevHost

TerraScale DevHost is TerraScale's systemd-managed local-development supervisor with a small Blazor Server dashboard. It owns the outer developer experience, local TypeScript SDK watcher, landing and documentation development servers, and Tailscale Serve routes. TerraScale.Orchestrator is the only backend control plane: it owns the production-shaped regional dependency graph and publishes the resource projection rendered by DevHost.

## Workspace

The default checkout root is `/workspaces/TerraScale`. `up` clones missing managed repositories into that workspace; `verify` instead clones its required consumers into a disposable owner-private state directory and never changes existing checkouts. Verification requires a running Linux user-systemd manager and `TERRASCALE_DEVHOST_VERIFY_KNOWN_HOSTS` set to an owner-only absolute trusted `known_hosts` file. Set `TERRASCALE_WORKSPACE_ROOT` to use a different checkout root. Deployment repositories are intentionally not provisioned or managed by DevHost.

After provisioning, DevHost fetches `origin/develop` in every repository every 30 seconds. A clean `develop` checkout is fast-forwarded automatically. A different branch remains paused. Local changes are preserved and automatic pulls remain paused until the repository owner commits and pushes the work or restores a clean checkout. DevHost never resets or overwrites local changes.

After a validated product update, DevHost sends the repository, commit range,
and bounded changed paths to the running Orchestrator over its owner-private
Unix socket. Orchestrator owns impact analysis and targeted replacement.
Orchestrator source changes still require exact-tree attestation before process
replacement. DevHost source changes cause a graceful exit so systemd rebuilds
and restarts DevHost. SDK, landing-page, and documentation watchers remain
running for their own source changes.

## One-time setup

```bash
cd /workspaces/TerraScale/TerraScale.TypeScript && npm ci && npm run build
cd /workspaces/TerraScale/TerraScale.Dashboard && vp install --frozen-lockfile
cd /workspaces/TerraScale/Terrascale.Landingpage && npm ci
cd /workspaces/TerraScale/Terrascale.Documentation && npm ci
sudo tailscale set --operator="$USER"
cd /workspaces/TerraScale/TerraScale.DevHost && ./scripts/install-systemd-service.sh
```

DevHost always starts TerraScale.Orchestrator's bounded three-region topology:
RF=1 product cells in GRU, SFO, and FRA. The topology is not selectable or
reducible and runs no email server: email delivery is disabled in the lab and
Authentication auto-verifies signup addresses, so no email verification is
required. Its rootless Podman containers share a
private pod network, run without added capabilities or privileges, and use
explicit resource limits. NATS runs exclusively from Orchestrator's digest-pinned
container image; no host `nats-server` installation is required.

## Manage the service

```bash
systemctl --user start terrascale-devhost.service
systemctl --user restart terrascale-devhost.service
systemctl --user stop terrascale-devhost.service
systemctl --user status terrascale-devhost.service
journalctl --user -u terrascale-devhost.service -f
```

`systemctl --user start terrascale-devhost.service` is the one command that
starts the complete local customer path. The managed service starts
Orchestrator's GRU/SFO/FRA graph, Authentication, Dashboard, Platform,
TerraBase, monitoring, export, and the configured Polar sandbox or
contract boundary. DevHost does not start a separate payment emulator or an
email server; email delivery is disabled and signup is auto-verified.

The installer links the tracked unit into the user systemd manager, enables user linger so the service starts at boot without an interactive login, enables the unit for `default.target`, and starts it. Direct `devhost up`, `dotnet run -- ... up`, and executable launches are prohibited and rejected at runtime; systemd is the sole owner of the long-running process.

The Blazor dashboard is available at `https://<this-host>.<tailnet>.ts.net:18443`. The hostname is discovered from Tailscale rather than hard-coded. These HTTPS ports are **fixed** — every boot and every monitor cycle re-asserts the same Serve map so the tailnet URLs never drift, including while Orchestrator is still converging. Authentication and the product Dashboard routes are installed immediately against their reserved GRU loopback ports; their health remains pending until those backends are actually ready.

| Port | Surface | Local target |
| ---: | --- | --- |
| 18443 | DevHost Blazor dashboard | `127.0.0.1:5180` |
| 18444 | TerraScale Platform | Orchestrator-published |
| 18445 | Authentication | Orchestrator-published |
| 18446 | Product dashboard with HMR | Orchestrator-published |
| 18447 | Landing page preview | `127.0.0.1:3002` |
| 18448 | Documentation preview | `127.0.0.1:3003` |
| 18449 | TerraBase | Orchestrator-published |

**Canonical product Dashboard rule.** `https://terrascale-dev.tail057f.ts.net:18446/` is the workspace's canonical product Dashboard URL and it must work correctly whenever the lab is converged: opening it serves the TerraScale Dashboard (port `18446` proxies the reserved GRU loopback target `127.0.0.1:18672`; an unauthenticated request redirects to `/login`, which must return HTTP 200). A 502 is acceptable only inside the convergence window after a service (re)start or Orchestrator re-attestation; leaving this URL broken outside that window is a release blocker. Verify it after every service action:

```bash
curl -skL -o /dev/null -w '%{http_code}\n' https://terrascale-dev.tail057f.ts.net:18446/   # expect 200
```

A scheduled check verifies this URL every 30 minutes on the DevHost host and reports or recovers failures without interrupting a healthy converging lab.

Polar is the default payment gateway, but DevHost admits it only when an access
token is configured. Without one, Developer onboarding uses the local development
payment gateway. To exercise Polar Sandbox, create
`~/.config/terrascale/devhost-payments.env` with:

```text
Payments__Provider=polar
Payments__Polar__AccessToken=<sandbox-access-token>
Payments__Polar__ApiBaseUrl=https://sandbox-api.polar.sh
```

DevHost supplies the onboarding return URL and a local webhook secret. Replace the
webhook secret and configure public webhook ingress before testing Starter or Pro
lifecycle events. Set `Payments__Provider=stripe` with
`Payments__Stripe__SecretKey` and `Payments__Stripe__WebhookSecret` in the same
owner-readable file to test Stripe instead. Payment settings are forwarded unchanged
to Platform, and explicit values override DevHost defaults. Configure the matching
Polar product IDs or Stripe price IDs in the billing plan catalog. Keep the file mode
at `0600`, then run `systemctl --user daemon-reload` and
`systemctl --user restart terrascale-devhost.service`. The tracked systemd unit reads
this optional file and DevHost never starts a payment emulator.

Repository-update notifications are optional. To enable them, create the
owner-readable file `~/.config/terrascale/devhost-notifications.env` with
`0600` permissions and set `TERRASCALE_DEVHOST_DISCORD_WEBHOOK_URL` to the
owner-private runtime value. Leave the file absent or the setting unset to
keep notifications disabled; repository synchronization and reconciliation do
not depend on notification delivery. Reload the user unit after changing the
file with `systemctl --user daemon-reload` and restart the service.

### Autonomous error repair agent

Every error DevHost observes is fingerprinted (commit identifiers, timestamps,
durations, and GUIDs are normalized before hashing). The first time a unique
error appears, DevHost spawns an autonomous agent — Claude Code in print mode
with `--dangerously-skip-permissions` — inside the repository that owns
the failing resource. Repeats of a known fingerprint never spawn a second
agent, and the fingerprint store under
`~/.local/share/terrascale-devhost/data/agent/` survives restarts, so each
distinct error triggers exactly one repair attempt.

DevHost also runs a public-URL watchdog over every fixed tailnet HTTPS port —
`18443` through `18449`: the DevHost dashboard, Platform, Authentication,
product Dashboard, landing page preview, documentation preview, and TerraBase.
Each URL is probed once a minute, and each probe is debounced the same way: a
failure streak must outlast the convergence window after a service restart or
Orchestrator re-attestation before it is reported, so a normal restart never
spawns an agent, but a persistent outage does. The canonical product Dashboard
URL (`https://terrascale-dev.tail057f.ts.net:18446/`) additionally follows its
redirect to `/login`, which must return HTTP 200. Watchdog activity is visible
in the event log on the matching resource: a trace on the watchdog's first
probe, on the first failure of a streak, on recovery, an hourly heartbeat
while healthy, and the escalation error itself when an agent is spawned.

Recovery from a failing public URL is deterministic and least-invasive first.
Once a URL has failed `TERRASCALE_DEVHOST_AGENT_REMEDIATION_THRESHOLD`
(default 3) consecutive checks, DevHost re-asserts the fixed Tailscale Serve
map, then restarts the local preview process that owns the URL when DevHost
owns one (landing page or documentation preview), then asks Orchestrator to
reconcile the affected product workload. Every step of that ladder re-asserts
the reserved `18445` and `18446` routes against their GRU loopback targets
instead of removing or narrowing them, and no step touches repository
checkouts. Only a streak that survives the whole ladder and reaches
`TERRASCALE_DEVHOST_AGENT_REPORT_THRESHOLD` (default 20 consecutive failures)
is reported as an error and spawns the repair agent.

Agent runs are gated, so a persistently broken lab cannot churn agents forever.
A run starts only `TERRASCALE_DEVHOST_AGENT_COOLDOWN_SECONDS` (default 600)
after the previous one started, at most `TERRASCALE_DEVHOST_AGENT_HOURLY_CAP`
(default 3) runs are allowed per rolling hour, and after two consecutive
failed runs the engine opens a circuit breaker for
`TERRASCALE_DEVHOST_AGENT_BREAKER_SECONDS` (default 3600) during which no agent
is spawned at all. The gate is persisted in the owner-private DevHost state
directory beside the fingerprint store, so restarting the service does not
clear it; the cooldown and the hourly window age out on their own durations and
the breaker closes again once its duration elapses. Probing and the
deterministic remediation ladder keep running while the gate is closed, so a
URL that recovers on its own is never escalated.

The agent receives a written context bundle — the redacted error, the target
repository's git state, recent warning/error history, and recent events — and
a mandatory git protocol: verify the `develop` checkout, commit any baseline
state first, pull `origin/develop` with `--ff-only`, fix the root cause, run
the relevant build or tests, commit again, and push to the remote `develop`
branch. When the agent exits, DevHost verifies that protocol against the
repository (clean worktree, HEAD pushed to `origin/develop`) and records the
outcome beside the context bundle. The agent never force-pushes or rewrites
history.

The mechanism is presence-based like the notifier: it is enabled when the
agent executable resolves on the system `PATH`. Configure it with
`TERRASCALE_DEVHOST_AGENT_COMMAND` (default `claude`),
`TERRASCALE_DEVHOST_AGENT_MODEL` (unset by default, Claude Code uses its own
default model), `TERRASCALE_DEVHOST_AGENT_TIMEOUT_SECONDS` (default 2700), or
disable it entirely with `TERRASCALE_DEVHOST_AGENT_DISABLE=1`. The watchdog
thresholds and the run gate are configured with
`TERRASCALE_DEVHOST_AGENT_REMEDIATION_THRESHOLD` (default 3),
`TERRASCALE_DEVHOST_AGENT_REPORT_THRESHOLD` (default 20),
`TERRASCALE_DEVHOST_AGENT_COOLDOWN_SECONDS` (default 600),
`TERRASCALE_DEVHOST_AGENT_HOURLY_CAP` (default 3), and
`TERRASCALE_DEVHOST_AGENT_BREAKER_SECONDS` (default 3600). Agent activity
is reported on the `agent` resource in the dashboard event list. A fatal
startup failure gets one additional bounded out-of-band attempt (25
minutes, same gates) before the process exits, so a blocking cause — for
example an attestation rejected by a worktree an interrupted agent left
dirty — is repaired instead of restart-looping. The startup phase itself
is bounded by a 30-minute overall budget (above a full cold Orchestrator
attestation, which alone can run fifteen-plus minutes): a startup step
that cannot succeed fails the process so systemd restarts it and fresh
repository updates are picked up, rather than retrying forever inside a
loop that never reaches the sync, watchdog and auto-fix lanes. That
restart only picks up fresh code if DevHost's own checkout can be
fast-forwarded, so when that checkout holds local changes the expiry
carries it as its blocking failure — reporting a stale build that no
restart can replace instead of reading as a budget problem.

Health status and agent transcripts are owner-private and survive restarts.
The event log — including every watchdog trace, remediation step, and
escalation — is `~/.local/share/terrascale-devhost/events.ndjson` (append-only
within a session; it starts fresh at each service start and rotates at 8 MiB),
and the last public-URL health view is
`~/.local/share/terrascale-devhost/health-status.json`. The fingerprint store
is `~/.local/share/terrascale-devhost/data/agent/fingerprints.json`, the run
gate is `~/.local/share/terrascale-devhost/data/agent/control-state.json`, and
each agent run keeps its written context bundle (`context.md`) and recorded
outcome (`run.json`) under
`~/.local/share/terrascale-devhost/data/agent/contexts/<timestamp>-<fingerprint>/`.

TerraBase, control NATS, product NATS, backup, and Orchestrator state persist
across restarts under `~/.local/share/terrascale-devhost/data/profiles/regional`.
For an intentional clean database, stop the service before running reset:

```bash
systemctl --user stop terrascale-devhost.service
devhost reset --force
systemctl --user start terrascale-devhost.service
```

## Commands

```bash
devhost status
devhost logs [resource]
devhost doctor [--fix]
devhost verify
devhost verify --repository TerraScale.TypeScript
devhost fixture \
  --output artifacts/public-alpha-local-evidence.json
devhost qualify-public-alpha \
  --input artifacts/public-alpha-local-evidence.json \
  --output artifacts/public-alpha-local-receipt.json
devhost coordination recover
devhost reset --force
```

The systemd service owns every child process and all routes listed above. A service stop shuts them down and removes only those routes.
`verify` runs the repository build and test checks introduced on `develop`; use `--repository` for a focused check.

Warnings and errors are redacted before they are written to the event store.

`qualify-public-alpha` is the CI and release boundary for the local Public Alpha
fixture. The evidence producer must run the same signup-to-cancellation journey
through the raw API, .NET SDK, TypeScript SDK, and MCP against one candidate and
journey specification. Each client must cover payment verification,
onboarding, organization, project, Database, Environment, Repository, Document
create/read/update/delete/query/batch/index operations, monitoring, export, and
cancellation. Signup runs without email verification: the lab disables email
delivery and Authentication auto-verifies addresses.

The gate also requires:

- working global, GRU, SFO, and FRA local host mappings plus browser-ready Auth
  and Dashboard endpoints, without changing production defaults;
- per-run identity, payment-method, and content digests and at least two
  organizations, projects, users, roles, and application credentials;
- cross-organization and cross-project denials through the API, both SDKs, MCP,
  session tokens, confirmation tokens, exports, and monitoring;
- 4 KiB rounding, selected-region multiplication, storage summation, rejected
  request exclusion, retry idempotency, and monthly reset assertions;
- in-app threshold, optional Discord failure, and required
  Polar webhook retry or escalation scenarios;
- evidence labels, units, stale values, source failure, last successful
  observation, and retention checks;
- namespace-only reset evidence and a scan proving retained output contains no
  Document content, secrets, authorization headers, payment data, or raw query
  parameters.

Missing, failed, stale, mismatched, or unredacted evidence fails closed. A
receipt proves the supplied local run met this contract. It is not evidence that
production endpoints, cloud resources, DNS, billing, or regional routing passed.

`fixture` writes an explicitly unqualified, disposable provider-neutral harness
template for offline and CI contract checks. It generates a new run namespace,
identity/payment/content placeholders, and redacted contract entries for all
four client adapters and boundary rules, but records no executed journey steps
or passed assertions. It does not start services, call external providers, or
create credentials. `qualify-public-alpha` rejects this template. A captured
service run must replace it and mark its provenance as `capturedServiceRun`
before using the receipt as launch evidence. Its `rawEvidenceDigest` must be
`sha256:` plus the lowercase SHA-256 of the canonical UTF-8 evidence JSON with
the `rawEvidenceDigest` value empty.

`doctor` checks the local CLI and runtime prerequisites. `doctor --fix` runs only deterministic project-local npm installs. Verification is read-only. An expired coordination record needs explicit `coordination recover` after its holder is proven inactive.
