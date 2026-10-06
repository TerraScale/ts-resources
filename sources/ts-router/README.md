# ts-router

ts-router puts a virtual model, `auto`, in front of CLIProxy for Claude
Code. In automatic mode, when a Claude Code session first asks for `auto`,
the router picks the model that fits the routing policy, with a cost-based
doubt heuristic, and how much reasoning the task needs, and pins the thread
to both: every later request of that thread goes to the same model at the
same effort, across router restarts. Operators can change the runtime mode
and model group from the dashboard. Requests naming any other model pass
through untouched, byte for byte. Claude Code is the only client: the
router serves `/v1/messages`, `/v1/messages/count_tokens` and `/v1/models`,
and nothing else.

## How a thread is routed

1. **Identify the thread** by Claude Code session (and subagent) id; a
   request without one goes to `default_model`, and requests that offer no
   tools are background calls that never make a decision.
2. **Decide** on the thread's first prompt: a chain of deciders (`systemone`,
   `llm`) judges it against each candidate's criteria; the first to answer
   wins, and `default_model` is the last resort. With `auto.learn` on, the
   verdict blends in where similar past prompts' threads belonged, by a
   weight the history earns on its own outcomes.
3. **Settle doubt, on cost**: with `auto.cost` on, the thread goes to the
   ladder step with the lowest policy-risk score, learned from the request log.
4. **Choose the reasoning** level the task needs, in the same call.
5. **Pin** it in SQLite along with the level; the pin moves only for a
   recorded reason: failover, capability upgrade, migration, redecision where
   the cache is cold, or an operator override.

The full algorithm is in [docs/routing.md](docs/routing.md).

## Claude Code

Point Claude Code at the router and the virtual model:

```bash
export ANTHROPIC_BASE_URL=https://router.example   # the router
export ANTHROPIC_AUTH_TOKEN=<CLIProxy client key>
export ANTHROPIC_MODEL=auto                         # discovery lists only Claude ids
export CLAUDE_CODE_GATEWAY_HINT_HEADERS=1           # request classes for background and compaction calls
export CLAUDE_CODE_MAX_CONTEXT_TOKENS=272000        # auto's window: the smallest candidate context
```

Without the hint headers the router still tells background calls apart
by their missing tools, and compaction follows the thread's pin as a
regular turn. Claude Code does not read context windows from `/v1/models`:
without `CLAUDE_CODE_MAX_CONTEXT_TOKENS` it takes `auto`, an id it does not
know, for a 200k model and compacts early. The variable applies only to ids
Claude Code does not know, so explicit Claude models keep their own
windows; leave `CLAUDE_CODE_MAX_OUTPUT_TOKENS` alone, since raising it
shrinks the context left before compaction.

Claude Code's system prompt only names `auto`, so a request routed to a
model other than Claude gets a last system text block naming the model,
after Claude Code's cache breakpoints and the same on every request of the
thread. A request routed to Claude gets nothing added: Anthropic serves it
through the Claude subscription accounts and expects Claude Code's own
request shape, so its body changes only in the model value.

## Endpoints

| Path | Purpose |
| --- | --- |
| `POST /v1/messages`, `POST /v1/messages/count_tokens` | Routed, or passed through to CLIProxy for an explicit model |
| `GET /v1/models` | CLIProxy's models plus `auto` |
| `GET /healthz` | 200 when CLIProxy serves every configured model, per a model list at most 10 minutes stale; 503 otherwise and while draining (no auth, no error details) |
| `GET /stats` | Pins by model, decisions and their reasoning levels, escalations, failovers, migrations, overrides and decider latency for the last day and week, each decider's health, request counters, the settled threads showing each sign of a misroute, the time per task and miss rate learned per model and level, and what routing learned from its history: labels by kind and the fitted weights (auth) |
| `/dashboard` | Operator dashboard (its own sign-in) |
| `GET /dashboard/routing`, `POST /dashboard/routing` | Read or save runtime routing settings (dashboard session required) |
| `POST /dashboard/logs/delete` | Confirmed deletion of request logs by age (dashboard session and same origin required) |

## Documentation

- [docs/routing.md](docs/routing.md): the routing algorithm, limits and
  spill, metering, decision log, reviews and bench, model notes.
- [docs/dashboard.md](docs/dashboard.md): dashboard, Routing page controls,
  review queue, request log, sign-in.
- [docs/operations.md](docs/operations.md): accounts and quota, shutdown,
  metering repair, configuration, commands, backups, deploys.
- [docs/alpha-access.md](docs/alpha-access.md): SSH access to the deployed
  router.
- [config.example.yaml](config.example.yaml): the example configuration.
