# Dashboard

The operator dashboard at `/dashboard`: what it shows, the Routing page
controls, the review queue, the request log, sign-in and how the pages are
built. Routing itself is described in [routing.md](routing.md); sign-in
secrets and deploys are covered in [operations.md](operations.md). Back to the
[README](../README.md).

## Dashboard

`/dashboard` shows the last day at a glance (headline figures, requests per
hour stacked by model, the model mix over a day or a week, CLIProxy's catalog,
deciders with their health and the reasoning mix, and a live request feed),
every pinned thread with a model filter, a thread's decision (why the model
and level were chosen, each candidate's and level's probability and each
step's cost-weighted policy score, with the time and the learned miss rate
it counted,
every decider's attempt and the exact request and reply of each, flagged
when today's request format no longer matches the digest of what was sent),
what similar past prompts suggested and how much it weighed, the first
prompt as the user wrote it, a review of the decision, pin
history with its redecisions, links between a session's thread and its
subagents' threads, a re-pin form that moves the thread to another model and level,
and its requests, and a live, filterable request log that can be paused.
The Decisions tab shows how `auto` classifies: the last 30 days of
decisions per model with the latest prompts each got, the classifier's
input (decider chain, instructions, the candidate descriptions Jev weighs as
criteria, the reasoning levels and the cost per task of each model at each
level, with the time a task takes there and how often its threads moved up),
a box that decides any prompt without pinning it and shows what
each decider was sent and answered, how the reviewed decisions fared, what
routing learned from its history (the labels settled threads left, by kind,
and the weight similar prompts earned for the model and the reasoning), the
decisions likely misrouted, and every decision with its review, filterable by model, decider, review and prompt
text. Decisions and Logs both offer indexed full-text search: all entered
words must match the recorded first prompt or classifier input, ignoring case,
accents and punctuation. Logs selects requests belonging to matching threads;
it does not record or search later conversation messages. Search combines
with existing filters and survives page reloads. Search is limited to 256
characters, and prompts removed by retention are no longer searchable.

Logs also has a collapsed **Delete request logs** form for requests older than
24 hours, 7 days, 30 days, or all requests before the deletion starts. An explicit
confirmation is required. Deletion applies across all models, regardless of
search and filters, and preserves pins, decisions and reviews. Request usage,
cost totals and learned estimates lose the deleted records. Open live request
tables refresh automatically after an operator deletion.

Each distinct policy is
recorded once by its fingerprint, so a decision's decider requests are
rebuilt from its recorded prompt, and checked against the digest of the
bytes sent.

The Routing page controls subsequent `auto` requests, with settings saved
in the router's SQLite database across restarts. Requests already in
progress keep the settings they started with. Without saved settings, the
router uses automatic mode, all candidates and Jev enabled:

- **Automatic** uses the normal routing policy within the selected
  **Automatic model group**. Select at least one configured candidate;
  selecting every candidate keeps the unrestricted default, including the
  configured auxiliary model. With a smaller group, existing pins outside
  it migrate to an available, compatible selected model on their next
  regular turn with a recorded history entry, preserving their reasoning
  level and capability requirements. Without a compatible replacement,
  that turn returns 503. The smaller group also constrains auxiliary and
  side requests, capability upgrades, failover, spill and operator re-pins.
- **Fixed model** sends `auto` requests to one selected candidate and
  bypasses every decider. Saved automatic pins and reasoning levels remain
  available when automatic mode resumes. Fixed mode does not spill, fail
  over or switch models for images; an unavailable target or an
  image-incompatible target returns 503. A thread's image requirement
  persists across mode changes even before it has an automatic pin.
- **Priority override** chooses quality, speed, or cost among suitable models.
  Leave it at **Let Jev decide** for the normal policy. Quality multiplies the
  economy's miss penalty by four; cost uses one third of it. Speed leaves cost
  promotion disabled and asks the decider to use candidate `expected_latency`
  estimates, when supplied, without guessing performance from model names.
  These are operating preferences, not measured task-success guarantees.
- **Optional model ranking** uses a preference dropdown beside each model.
  Choose distinct positions, with 1 highest, or leave **No preference**. Deciders use it to break ties after task fit and
  priority. It does not reorder the capability ladder, exclude unlisted models,
  or bypass availability and image requirements.
- **Full auto** clears the fixed model, group restriction, priority and ranking,
  and enables Jev in one save. New threads use the configured automatic policy;
  existing threads retain their automatic pins and reasoning.
- **Enable Jev** controls configured Jev SystemOne classifiers (`jev` or
  `jev-*`) in automatic mode. Turning it off leaves other configured
  deciders available. Fixed mode bypasses every decider.

Priority and ranking are saved in the same SQLite settings as mode and group.
Each request snapshots them; recorded policy fingerprints and reconstructed
classifier requests include the exact preference used. The Decisions prompt
trial uses these controls too. Priority changes affect new decisions, while
model-group restrictions can migrate existing pins as described above.

Any model ID served by CLIProxy can be a routing candidate, including private
and newly released models. Add its task criteria, capability limits, supported
efforts, fallback and price to the config; model selection does not depend on
vendor names. An optional `expected_latency: 750ms` field supplies an operator
estimate for comparable requests to guide speed priority. Leave it unset when
unknown; no performance estimate is inferred from a model name. Concrete-model
requests continue to use CLIProxy's full catalog directly.

These controls apply only to the virtual model configured by
`auto.model_id` (`auto` in the example). Requests naming a concrete upstream
model retain their API passthrough behavior and bypass router selection.
The selected model's configured effort policy still applies to virtual-model
requests, including Sol 6.1's fixed `high` effort. `check` and `bench` use
the configured deciders independently of these runtime settings.

`POST /dashboard/routing` requires a dashboard session and an
`application/x-www-form-urlencoded` form: `mode` is `auto` or `fixed`,
`fixed_model` selects the fixed candidate, repeated `models` fields select
the automatic group, `priority` chooses `auto`, `quality`, `speed` or `cost`,
`rank:<model-id>` supplies an optional numeric preference (1 highest; duplicate
positions are rejected), and `jev_enabled=true` enables Jev (omitting it
disables Jev). Automatic mode requires at least one model selection;
unknown or retired candidates are rejected. A successful save redirects
back to the Routing page with a saved confirmation.

Operators sign in with a username and password. `dashboard.username`
defaults to `mariogk`; `dashboard.password_hash_env` defaults to
`TS_ROUTER_DASHBOARD_PASSWORD_HASH` and names the secret holding the bcrypt
password hash, resolved from `secrets_files` or the environment. A missing
hash disables dashboard sign-in; a malformed nonempty hash is a
configuration error. Dashboard sign-in accepts no API key. Claude Code,
model discovery and `/stats` continue to use the CLIProxy client key.

Generate the hash from a non-echoing Bash prompt. The helper accepts one
password of 1 to 72 bytes through non-terminal stdin and writes only the
bcrypt hash:

```bash
umask 077
router_dashboard_hash_file="$(mktemp)"
read -rsp 'Dashboard password: ' router_dashboard_password
printf '\n'
printf '%s' "$router_dashboard_password" | ts-router hash-password > "$router_dashboard_hash_file"
unset router_dashboard_password
```

Store the generated file's contents as `TS_ROUTER_DASHBOARD_PASSWORD_HASH`
in the secret materializer or a configured `secrets_files` entry, then
remove the temporary file and restart the router. A dotenv entry uses the
generated hash, never the password:

```dotenv
TS_ROUTER_DASHBOARD_PASSWORD_HASH='<generated bcrypt hash>'
```

An address gets 429 after 5 failed sign-ins in 10 minutes. The session is
an in-memory, HttpOnly, SameSite=Strict cookie that lasts 12 hours, so a
restart signs everyone out. Signing out or reaching the session expiry
also closes active dashboard streams. Cross-origin
POSTs are refused, and the trial box runs at most 4 trials at once.

Pages render on the server with [templ](https://templ.guide) and stay live
through [Datastar](https://data-star.dev) server-sent events; there is no other
JavaScript and nothing loads from another origin. The generated `*_templ.go`
files, the built Tailwind stylesheet and the vendored Datastar bundle are
committed and embedded in the binary. After changing a template or the
stylesheet source, regenerate them:

```bash
mise exec -- make generate                 # templ v0.3.1020 -> *_templ.go
mise exec -- make css                      # Tailwind v4.3.3 standalone CLI (downloaded to tools/)
mise exec -- make datastar                 # re-vendor Datastar v1.0.4
```

## Review queue

Above every decision, **Likely misrouted** lists the unreviewed decisions
whose settled threads went worst, the strongest sign first, each sign in
words and each linking to the thread's review: an operator moved the thread
up (strongest) or down, the router decided it again up or down, a thread on
the lighter half of the ladder ran more than `outcomes.long` regular turns
(200), it failed over on a server error, a thread on the heavier half stayed
within `outcomes.tiny` turns (3), or it started carrying images its model could
not read. Turns are regular requests: token counts, compactions and
background calls do not count, and a thread's size counts only while it
stayed on the model it was decided for. A failover on a 429 and a migration say
nothing about the decision and never queue one. `/stats` counts the settled threads showing each sign.

## Request log

The request log keeps, per `auto` request, the pin key hash (side requests
too, so a thread's compactions count towards its cost), endpoint kind, sent
model and effort, reason, status, failover, latency, queue wait, tokens, cost and a
short error, and reads each request back with its thread's cost so far. Latency runs from the
request's arrival until the response finished streaming, so it includes the
queue wait (time spent waiting for a `limits` slot, logged apart) and the
routing decision. Requests for an explicit model pass through unlogged, so the log and
the dashboard show only `auto` traffic. The request log is written off the
request path (a full queue drops entries rather than delaying a response)
and pruned hourly to `log_retention` (30 days by default); pins and
decisions are kept.
