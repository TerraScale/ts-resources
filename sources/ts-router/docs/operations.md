# Operations

Running ts-router: subscription accounts and quota, authentication,
shutdown, metering repair, configuration, commands, the bench, backups and
deploys. Remote access to the deployed router is described in
[Alpha SSH access](alpha-access.md). Routing is described in
[routing.md](routing.md) and the dashboard in [dashboard.md](dashboard.md).
Back to the [README](../README.md).

## Accounts and quota

With `accounts.management_key_env` set, the router watches CLIProxy's
ChatGPT and Claude subscription accounts through its management API: every
`accounts.interval` it reads each account's quota windows (Anthropic's
five-hour, weekly and per-family weekly windows; ChatGPT's primary and
secondary windows) from the rate limit headers CLIProxy recorded on the
last response the account served. The router never calls Anthropic or
ChatGPT itself: a quota probe is traffic no real Claude Code or Codex client
sends. CLIProxy fills one account at a time, so an account at its limit gets
`limited_priority` and waits behind the others until its window resets. When
the provider reports available credits or extra usage, exhausted included
quota can continue serving behind accounts with included quota remaining:
with the standard `limited_priority: -10`, included quota has priority 0,
credit-backed accounts -5, and blocked accounts -10. The router owns these
accounts' priorities. The Overview shows the provider's remaining credit
balance when reported, unlimited credit status, or Claude extra-usage
availability. Missing credit metadata is shown as unknown and never restores
an exhausted account; a provider refusal still blocks requests despite a
reported balance. Credits have no inferred currency, and credit-backed
status does not claim an amount has been charged. A
model that no account can serve any more is withheld from new decisions and
failovers (recorded with each decision), and the Overview shows every
account's windows and when they were seen. A window that has reset since no
longer limits; when CLIProxy knows no quota for an account (it restarted),
the account keeps what the last refresh found until the window it limited
resets, and an account nothing is known about counts as usable but keeps
its priority, so an account never returns to rotation without evidence that
it may; each refresh is bounded, so a stalled call cannot freeze the watch. GLM,
DeepSeek and other API-key upstreams always count as available.

### Claude usage limits in T3 Code

Enable CLIProxyAPI's `passthrough-headers` so its observed
`anthropic-ratelimit-unified-*` signals reach Claude Code through the router.
Native signals, including warning, overage and reset metadata, pass through
unchanged on successful streams and errors. When a final Claude `429` has
only a valid `Retry-After`, the router supplies unified status `rejected` and
a Unix reset timestamp for Claude Code's `rate_limit_event`. It preserves
the response body and retry hint, does not invent a reset without a valid
hint, and does not attach Claude limits to other models or a successful
failover.

Claude Code using `ANTHROPIC_AUTH_TOKEN` suppresses these events unless
gateway mode is enabled. For T3's Claude provider, set
`CLAUDE_CODE_USE_GATEWAY=1` in its environment and use an HTTPS router
origin in Claude's `settings.json` `env.ANTHROPIC_BASE_URL` (remote HTTP is
rejected in gateway mode; localhost HTTP remains usable for tests). These
settings take effect on new Claude processes; active sessions need not be
interrupted. T3 reads the passive SDK events to display the relevant usage
window and schedule resume at its reset. Its OAuth-only `get_usage` query
is not the proxy quota source. No provider usage probes are added.

## Authentication and shutdown

Claude Code and `/stats` authenticate with the CLIProxy client key; the
router checks it before spending an upstream or decider call and forwards
it unchanged for API requests. Dashboard sign-in uses separate operator
credentials. Any other path gets 404, so CLIProxy's management API stays
out of reach, and `X-Management-Key` and forwarding headers never pass. A
request CLIProxy sends nothing for `upstream.idle_timeout` (10m; no headers, or no chunk
mid-stream) is ended with 504 and frees its slot; the silence is counted
from what CLIProxy sends, so a slow client is never taken for it, and time
spent queued for a slot does not count. On SIGTERM the router drains:
`/healthz` turns 503, and streaming responses get `shutdown_grace` (1m) to
finish before they are cut and logged as cut at shutdown; a second signal
stops it at once.

## Metering repair

Streams metered before the translated-stream fix (2026-09-30) logged that
estimate as input on top of the cache reads, which priced the prompt twice and
dragged the cache hit rate down. `ts-router repair-metering` counts the rows
that look affected and, with `--apply`, repairs and reprices them; it is
opt-in because the log cannot tell a translated stream from a plain JSON
response, so a correct row can match. A row looks affected when it is a
non-Claude request logged before the fix that succeeded, read at least 10000
tokens from the cache and has an input of at least half its cache reads and
writes (the opening estimate counted the whole prompt). It takes the cache
reads and writes off the input, never below zero, and flags the row
`repaired`, keeping the logged input and cost in `original_input_tokens` and
`original_cost_usd` so a correct row the rule caught can be restored. The
corrected input is an approximation, since the real fresh count was
overwritten. The cost of a repaired row is recomputed from the `prices`
table, again whenever the router starts.

## Configuration

See [config.example.yaml](config.example.yaml). The document is read from
`TS_ROUTER_CONFIG` when that variable is set (HomeLab passes it as an Incus
environment key), else from `--config`. Adding a candidate is one entry
under `auto.candidates`; retiring a model is removing it there (new threads
stop going to it) and listing it under `auto.retired` (its threads move
off). Secrets come from the dotenv `secrets_files` (later files win),
falling back to the environment.

## Commands, bench and deploys

For deployed-router access from `mariogk-dev`, follow
[Alpha SSH access](docs/alpha-access.md). It uses the existing key file and
documents agent network permissions; Bitwarden is not required on this server.

```bash
mise exec -- make verify                   # gofmt, vet, race tests
mise exec -- make release-linux            # static dist/ts-router-linux-amd64
ts-router serve --config config.yaml
ts-router check --config config.yaml       # catalog + one probe per decider
ts-router bench --config config.yaml --cases bench/routing.yaml --min-accuracy 0.9
ts-router backup --db /var/lib/ts-router/router.db --to /var/backups/router.db   # online snapshot, no config needed
```

`bench` asks every decider alone, and the whole chain, about every labelled
case in [bench/routing.yaml](bench/routing.yaml), settling doubt within
`decide_timeout` with cold-start task estimates. Cases can supply `images`,
an `offered` model subset, a `group` and a label rationale in `note`.
It reports model, task-depth and joint accuracy, group and tier support,
under/over-routing, calls, reported token usage and latency. Predicted depth
is separate from applied effort: a correctly judged `medium` task on Sol still
runs at `high`. Unstarted cancellations do not enter latency percentiles.
`--repeat` measures consistency across trials of the same tasks;
`--format json` saves inputs, policies, attempts, costs and execution settings.
`--reference sol61` compares each decider with a configured Sol teacher,
separately scoring initial model choice, task depth and final routing.
Optional `--min-accuracy`, `--min-group-accuracy` and `--min-joint-accuracy`
gates apply to the configured chain. Incomplete runs fail.

The benchmark tests classifier policy compliance, not downstream task success
or the full resolver: defaults, persisted pins, quota changes, concurrency
spill and failover need integration tests. [bench/diagnostic.yaml](bench/diagnostic.yaml)
adds multilingual, contrastive, quoted-content, injection, vision and
availability cases. Both shipped corpora are development data. See
[benchmark methodology](bench/README.md) before interpreting a live run.
`check` reports CLIProxy's catalog, `limits` on models it does not serve,
and one probe per decider. Quick, straightforward prompts and tiny explicit
edits, even urgent ones, use `deepseek-flash`. Everyday work uses
`glm-5.3-flash` for small routine coding, focused tests and native
image-based work; broader text-only maintenance, module tests and mechanical
bulk changes use `glm-5.3`. GLM's marginal
usage is priced at zero while its adaptive concurrency cap and spill remain
active. Substantive features coordinating persistence, API, UI and integration
tests, higher priority work, and trickier bounded debugging, algorithms,
concurrency or integrations use `gpt-6.1-sol` at high effort, which is also the default when
a decision cannot be made. High-difficulty tasks (architecture, distributed
systems, security, durability and investigations across services) and
substantial UI changes (whole new pages, multi-screen flows, major redesigns
and frontend architecture) use Opus regardless of urgency. Sonnet 5.5 is
retired, and its existing threads move to Sol 6.1 on their next request. The
ladder is `deepseek-flash` → `glm-5.3-flash` → `glm-5.3` → `gpt-6.1-sol` →
`claude-opus-5-5`. Each case also lists its acceptable reasoning levels,
which follow the depth of thinking, not the model or urgency: tiny and
mechanical edits, however large → `low`; everyday work with a clear path →
`medium`; bounded but tricky problems → `high`; open-ended design and
unknown causes → `xhigh`. Tune the candidate and level criteria and
`escalation_threshold` against it; keep the criteria's examples distinct
from the cases.

The store refuses a database a newer build migrated, and migrations only
run forward, so a rollback needs the database from before the deploy: take
`ts-router backup` first wherever the deploy does not snapshot it.

CI (`.forgejo/workflows/ci.yml`) verifies every push and, on `main`,
publishes `git.terrascale.tech/terrascale/ts-router:<sha>`; it holds no
deploy credential. Alpha's homelab-deployer follows `main`: once the check
`ts-router CI / Verify and build ts-router (push)` passes it stops the
router (which drains), snapshots `router.db`, rolls the instance onto the
image behind the `/healthz` gate (restoring the snapshot and the previous
image when it fails) and reports a `deploy/alpha` status on the commit.
Renaming the workflow or its job changes that check, so update HomeLab
`ops/deployer/apps.json` with it (HomeLab `services/deployer.md`).

Which commit runs on alpha: the newest commit whose `deploy/alpha` status
reads "Running on alpha", `sudo homelab-deployer status` on alpha, or the
`org.opencontainers.image.revision` label of any published image.
