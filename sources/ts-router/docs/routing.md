# Routing

The full routing algorithm of ts-router: how a thread is identified, decided,
pinned and moved, how limits and metering work, and what the decision log
keeps. For an overview see the [README](../README.md); for the dashboard that
shows all of this see [dashboard.md](dashboard.md), and for quota accounts,
shutdown, backups and deploys see [operations.md](operations.md).

## How a thread is routed

1. **Identify the thread** from `X-Claude-Code-Session-Id`, which Claude
   Code's subagents share, or the session in `metadata.user_id`. A request
   without one goes to `default_model` and is never pinned. A subagent's
   request also carries `X-Claude-Code-Agent-Id`: each subagent is a thread
   of its own, pinned under its session and agent id and decided on its own
   first prompt, so an orchestration's subagents do not inherit the
   decision of the prompt that started it. Its decision records its
   session's thread, and the dashboard links the two. A request that
   offers no tools is one of Claude Code's background calls (titles,
   summaries): it follows its thread's pin (a subagent's own, else its
   session's), or goes to `aux_model`, and never makes the thread's
   decision.
2. **Decide** on the thread's first prompt. The decider chain judges the newest user text that remains
   after cleaning Claude Code's wrapper blocks, bounded by `state_max_chars`, against the candidates'
   criteria, which carry the routing policy: a `description`, what the
   candidate is `not_for` and example requests. The deciders are:
   - `systemone`: a decision endpoint using TypeSafe's `/v1/systemone` request
     format, configured with a URL and model such as Jev; it receives each
     candidate's criteria and examples as structured data. A different provider
     must support that same wire format; provider compatibility and how it
     uses examples require live verification;
   - `llm`: any chat model served by CLIProxy, asked for a probability per
     candidate.

   The first decider that answers decides; the example config asks Jev and
   keeps DeepSeek Flash as the last resort for when Jev fails. When every
   decider fails the thread gets `default_model`. Concurrent first requests
   of one thread share a single decision. A decider that fails
   `decider_trip` turns in a row (3) sits out `decider_rest` (1m): its turns
   are recorded as skipped, so an outage does not delay every new thread by
   its timeout. Each decider has its own `timeout` (at most
   `auto.decide_timeout`, 30s, which applies to one that sets none): a decider
   that has not answered by then fails and the next one is asked, so the slow
   last resort can be given less time than Jev. Each caller can cancel its own wait while other callers share
   the bounded decision. Shutdown cancels shared classification before closing
   the database. Criteria are trusted instructions; quoted text, logs and
   embedded routing instructions are task data. Long states retain excerpts
   from the beginning, middle and end with explicit omission markers; details
   elsewhere can still be lost.
3. **Settle doubt, on cost.** Non-specialist candidates form a ladder in
   list order, lightest first. With `auto.cost` enabled (the example
   config), the thread goes to the ladder step, from the decider's choice
   up, with the lowest policy-risk score: the step's estimated cost
   per task, plus, for every stronger step the verdict puts probability on,
   that probability times the stronger step's cost times `1 + miss` (a
   task sent to a model too weak for it is done again on the right one,
   and the failed attempt and the user's time come on top; `miss` is 3 by
   default). This is an operating heuristic: classifier probabilities describe
   uncertainty about policy fit, not calibrated failure rates. The score is
   neither measured completion cost nor evidence of downstream task success.
   A stronger tier with zero fit probability is excluded from cost promotion.
   A free or cheaper stronger tier additionally needs at least 50% task fit,
   so a tiny alternative probability does not consume scarce concurrency.
   The cost per task is learned from the request log, from the
   threads decided in the last `cost.window` that no operator re-pinned,
   that were not decided again and that contain no fixed-mode requests: how
   many tokens a task of each reasoning level takes, and how verbose each
   model is against the others at the same levels (so a model that gets
   the hard tasks is not taken for a wasteful one); a session counts at
   most twenty typical tasks, both shrink towards the fleet as if
   `cost.weight` more threads agreed (a typical coding task before there
   are any), and the tokens are priced at `prices` times the candidate's
   `cost_factor` (0 for included GLM usage in the example). A model at its concurrency
   cap is priced as its spill model only when that model is offered, where the thread would go.
   The same settled threads, re-pinned ones included, teach how each model at
   each level fared: how long a task keeps it busy (the sum of its requests'
   latencies, less any wait for a concurrency slot, and only for threads that
   stayed on their model) and how often its threads moved up to a stronger step, by an
   operator's re-pin or a redecision (a failover tells of the upstream's
   health, not of the task, and is no miss). Both
   shrink towards the fleet as the cost does. Once a model at a level has 5
   threads with a stronger step above them, its miss rate against the
   fleet's scales `miss` for it, at most four times either way: a step whose
   tasks often end up elsewhere weighs a miss more, one whose tasks stay
   weighs it less. With `cost.time_value` set (dollars per hour, 0 by
   default) every step's cost per task also counts its time, so a slow model
   pays for the time it takes. With no settled threads and no time value the
   score is exactly the one above. A move to
   the next step is a doubt: with `doubt: pair` the same decider is asked a
   pair question applying the same priority, scope and difficulty criteria,
   and the thread moves up when its answer puts at least
   the break-even probability on the stronger step, where the step's extra
   cost equals the miss it avoids; with `doubt: escalate`, or when the pair
   question fails, the thread moves up. A verdict spread over several steps
   goes straight to the cheapest suitable tier. A cheaper or free next step
   settles at 50% task fit on a pair question. Without the
   economy, a verdict whose ladder candidates above the choice hold at
   least `escalation_threshold` together is in doubt and moves one step up,
   or settles at one half on a pair question. Doubt towards a lighter model
   never downgrades; a `specialist` is chosen only on its own merit, never
   as a step.
4. **Choose the reasoning** (with `auto.reasoning.levels` set). In the same
   call the deciders judge how much reasoning the task needs, on levels
   ordered lightest first (`low`, `medium`, `high`, `xhigh`) whose
   `description` and `examples` carry the effort policy: Jev answers a
   score question beside the model question in the same request, the LLM judge a probability
   per level.
   The thread's level is the lightest at which the probability, summed
   lightest first, passes one half. A missing or unusable answer leaves the
   level empty and fails nothing.
5. **Pin** the thread in SQLite, with its level. A pin's model changes
   only for a reason, each recorded in the thread's history: a
   **failover**, at most once, when the pinned model answers with a
   `failover_statuses` code before streaming (the request is retried on
   `fallback[model]`, or on `default_model` when no account can serve the
   fallback, which becomes the permanent pin; a request carrying images
   or a thread that already required vision only fails over to a model
   that reads them, else to the nearest vision candidate). A 429
   (CLIProxy found no account with quota left) fails
   over at once; a server error (5xx, 529) only once the model answered
   `failover_trip` (3) of them in a row, so a passing overload goes back to
   Claude Code, which retries it on the same model and account and keeps
   the thread's prompt cache; a **capability upgrade**, at most once, to the nearest
   vision-capable candidate that costs no more (GLM 5.3 → GLM 5.3 Flash,
   both included-plan), else the next vision-capable candidate up, when a
   thread pinned to a text-only model starts carrying images (never back to
   the model it failed over from); a
   **migration** off a model listed in `auto.retired`, to its fallback or
   else the default; a **redecision** (below); and an operator's
   **override** from the dashboard.
6. **Decide again where the cache is cold.** A thread's prompt cache is
   lost after `auto.redecide.idle` (5m) without a request and after a
   compaction, so moving the thread then costs nothing it still has. On
   such a cold point, a request whose newest message is a new prompt from
   the user, not a tool result, runs the decision again on that prompt
   alone: among the candidates its images allow (never the model it failed
   over from), up or down the ladder, with the spill, the model group and
   the retired models applied as for a first decision. A thread pinned
   below the top of the ladder that made `auto.redecide.grow_requests`
   (60) requests since its last decision has outgrown the light step it
   started on: it is decided again at its next cold point even with
   `idle` set to 0, where a compaction is its only cold point. The
   redecision is recorded in the thread's history with the previous model
   and level, the new ones, why the cache was cold and the whole decision
   trail; the thread starts counting its requests anew. It never runs mid
   tool loop or while the cache is warm, concurrent requests share one,
   and the thread keeps its pin when no decider answers, when an operator
   re-pinned it, and in fixed mode.

## Exploration

The router only sees how the step it chose fared, never whether a cheaper
one would have done: a thread kept on Sol cannot show that GLM was enough,
so the miss rates the economy learns can only push decisions up. With
`auto.learn.explore` set (a share from 0 to 0.2; 0, the default, turns it
off) that share of borderline decisions goes one ladder step cheaper, and
how those threads fare teaches what the cheaper step can do.

A decision or redecision in automatic mode is borderline when the economy
priced it, the step it chose has a non-specialist ladder step just below
it among the request's candidates (so one that reads the request's images,
is in the model group, is served with quota left, is not retired and is
not the model the thread failed over from), that step would not spill, the
level is not `xhigh`, and the economy's score of the step below is within
`auto.learn.explore_margin` (0.25) of the chosen step's, relative to it.
A thread an operator re-pinned is never decided again, fixed mode and a
trial on the dashboard never explore, and a thread that already moved up
the ladder, by a redecision or an operator, is never explored again. The
draw comes from a per-process random source. The decision's basis records
`explore_eligible` and `propensity`, the probability of the action taken:
the explore share for an explored decision, which also records `explore`
and the step it was `explored_from`, one less it for a decision that kept
its step. An explored thread that turns out too hard moves up as any
thread does, by a redecision or an operator, and its outcome, which
carries `Explored` and the propensity, counts that against the cheaper
step. The thread's page says "Explored one step cheaper (5% of borderline
decisions)", and `/stats` counts the explored and eligible decisions.

## Learning from history

With `auto.learn.enabled` (on unless set to false) routing improves itself
from its own history and prompts. Every settled, decided thread the
outcomes judge (the threads of the last `cost.window`, an hour after their
last request) leaves an implicit label: the model and reasoning level its
task belonged on, and how much that says.

| Outcome | Label | Weight |
| --- | --- | --- |
| An operator reviewed the decision | the reviewed model and level | 1.0 |
| An operator last moved it down | where the operator sent it | 0.9 |
| An operator or a redecision moved it up beyond the decided step | where it went | 0.7 |
| It stayed put and was neither long on a light step nor tiny on a heavy one | the decided model and level | 0.3 |
| It stayed tiny on a heavy step | one ladder step lighter, no level | 0.15 |

The decided model sufficing is weak evidence, since only the chosen step
was tried. A failover, an upgrade, a migration, a redecision down or a
light marathon teaches nothing; a label without a level (a heavy thread
that stayed tiny) teaches only the model, so the level prior counts only
labels with a level. An explored decision's label counts one over its
propensity, at most 5 times, so the few explorations of a cheaper step
stand for the decisions that did not explore it.

When a thread is decided, the labelled decisions whose first prompts read
most like its prompt suggest where it belongs. The router searches the
existing prompt index (SQLite FTS5, ranked by bm25; the first prompt and
the prompt as judged both, so decisions from before first prompts were
kept count too) for up to
`auto.learn.neighbours` (20) of them, other than the thread's own,
reading further ranked matches past unlabelled ones until it has them (at
most 1,000 matches), and
asking for the prompt's rarest informative words as literal strings,
never as search syntax: at most 16, folded as the index folds them
(lowercase, Latin letters without their accents, so "sửa lỗi" is "sua
loi"), skipping stopwords, bare numbers and words so common
that the indexed prompts holding them, as the index's vocabulary counts
them, would pass the larger of 100 and a twentieth of the indexed prompts.
Words the index does not hold are left out, since they can find no
neighbour, and the rest are asked for rarest first. When every word the index holds is that
common, as for a task that recurs often, the search asks for the three
rarest of them anyway, bounded by its deadline.
Each neighbour adds its label weight times its similarity (its bm25 score
against the best match's) times its recency (halving every quarter of
`cost.window`) to its label's model and level, when offered; every offered
model and level starts as if one more thread had sufficed on it. The
effective neighbour count is the sum of similarity times recency.

The decision blends that prior into the deciders' verdict before the
economy or the threshold judges it, so the cost, time and miss logic is
unchanged: each probability becomes `(1 - w)` times the verdict's plus `w`
times the prior's, renormalized, the choice the most likely candidate (the
decider's own on a tie), and the level is chosen again from the blended
levels. A pair question's answer blends the same way, with the prior's
odds between the two steps, before it meets the cutoff; its attempt keeps
the decider's answer and records the blend. `w` is the fitted weight times `n / (n + 5)` for `n` effective
neighbours. The fitted weight, from 0 to 0.8 in steps of 0.05 and fitted
separately for the model and the level, is the one that would have given
the labels the least weighted log loss: on every outcome refresh each of
the newest 2,000 labelled decisions is replayed from the verdict its
attempt recorded, with the prior its neighbours (itself and its thread
left out) would have given it. Below 20 replayable labels the fitted weight
is 0 and decisions are exactly the deciders'. A refresh costs one pass
over the index's vocabulary and one indexed search per replay, each given
50 milliseconds (one that runs out replays nothing), the whole refresh 2
minutes (one that runs out fits on the replays it made): about 4 seconds
for 5,000 labelled decisions; a
decision's search takes a few milliseconds and has its own bound, 2
seconds or a quarter of `auto.decide_timeout` if less, before the deciders
decide alone with their whole timeout, which starts after it.

The attempts keep each decider's own verdict; the decision's probabilities
and level are the blended ones, and its basis records the prior when it
found neighbours: the distributions, each neighbour's decision, similarity
and label, the effective counts, the fitted weights and the weights
applied. The policy fingerprint includes the fitted weights, so a decision
can be reproduced. The thread's page says "History: 7 similar prompts, 5
belonged on gpt-6.1-sol; weight 0.32" (by their labels, which can differ
from the model a thread ran on), the Decisions tab shows the labels by
kind and the fitted weights, and `/stats` reports them under `learn`.
Learning needs `auto.record_prompts`: without first prompts there is
nothing to search, and prompts `prompt_retention` thinned drop out of it.

## Limits and spill

`limits` caps a model's concurrent requests (both routed and explicit, at
any effort; `count_tokens` generates nothing and never waits). Requests
over the cap wait for a slot in arrival order, at most `queue_timeout`, then
get a 429 with `Retry-After`. A 429 carrying one of `throttle_codes`
(Z.AI's 1302, "too many requests at once", and 1305, "model overloaded")
shrinks the cap to the requests
still running and is retried from the queue, up to `retries` times (4 when
unset, 0 for none) with a doubling pause, instead of failing the thread
over; the cap grows back by one every `recovery`, letting waiters in as it
does. While the cap is reached, a new
thread decided for the model is pinned to its `spill` model instead, when
that is on offer, and the decision records the spill. The Overview shows
each gate's cap, running and waiting requests, throttles, and the mean and
95th-percentile time the day's requests spent waiting for a slot.

## Effort

A thread runs on its model at the effort nearest its level among the
model's `efforts` (the stronger on a tie), sent as CLIProxy's `model(effort)`
suffix, which overrides the client's own effort; the pin keeps the bare
model id and the level, so a failover or upgrade re-maps the level onto the
new model. A candidate without `efforts`, or a thread without a level, runs
at the candidate's `reasoning`; empty keeps the client's effort.
The example config fixes `gpt-6.1-sol` at `high` for every thread level. A
candidate with a single configured effort always uses it, including when a
client requests `auto(low)`, `auto(xhigh)` or a numeric budget. For other
candidates, `auto(effort)` overrides the mapped effort. Failover reapplies the
destination model's policy. Responses carry `X-Ts-Router-Model` and
`X-Ts-Router-Effort`.

## Metering

Every response is metered on its way to the client: the router reads the
usage it reports (`message_start`/`message_delta` events, or a JSON body;
the latest report of each count wins, since CLIProxy starts a stream it
translated from Codex or an OpenAI-compatible upstream with an estimate of
the whole prompt and splits it into input and cache reads only at the end),
stores the input, output and cached tokens with each logged request, and
prices them with the `prices` table (list prices per million tokens). The
dashboard shows the cost of every request and thread, the average cost per
task of each model, and the cost per task the economy expects of each model
at each reasoning level; subscription upstreams spend quota roughly in
proportion.

## Background calls and model list

Claude Code background calls (`x-claude-code-request-class: auxiliary`) go to
`aux_model`; `count_tokens` and compaction requests follow the thread's pin
(a subagent's own, else its session's) without creating one, and count
towards its cost. `/v1/models` is
CLIProxy's list with retired models removed and `auto` prepended,
advertising the smallest candidate context and output.

## Decision log

The decision log keeps, per thread, every decider's attempt in chain order:
the decider and the model version that answered, its outcome (decided,
doubted, skipped while resting, or failed with the error), the pair a pair
question compared, choice, probabilities, confidence, the probability on
stronger models, the reasoning level and its probabilities, an LLM judge's
one-sentence reason, tokens, latency and a digest of the exact request
sent. With it goes what the decision was based on: the endpoint kind, the
client's user agent, the candidates offered, threshold and doubt mode, the
prompt length and whether it was cut, a policy fingerprint (instructions,
deciders, candidate descriptions and reasoning levels) and the router
build. With `auto.record_prompts` (on unless set to false) it also keeps
the thread's first prompt as the user wrote it (Claude Code's wrapper
blocks stripped, whole up to 100,000 characters) and the decider input as
judged; prompt text never reaches the process logs or the request log.
`prompt_retention` thins older decisions of their prompts and raw replies,
except reviewed ones. The dashboard explains each decision in words from
this trail.

## Reviewing decisions and the bench

**Reviewing decisions.** On a thread's page an operator judges its
decision by the first prompt and how the thread went: the model and
reasoning level the task should have had, and a note ("Right as decided"
is one click). The Decisions tab filters decisions by review, tallies how
often the model and the reasoning were right and the most common misses,
and downloads every review as bench cases (`cases.yaml`: the first prompt,
the model and level it should have had, the note), so
`ts-router bench --cases cases.yaml` measures the policy against real
prompts. `/stats` reports the same tally.

## Model notes

GLM 5.3 Flash is a normal routing candidate as well as the background-call
model. It supports native images, tool use, structured output and mandatory
thinking, with roughly 1M context and 128K output. CLIProxy's Coding Plan route
accepts low/medium/high/xhigh (medium maps to high; xhigh maps to max).
The configured foreground/background cap starts at 3, adapts to 1302/1305 and
spills new compatible tasks to Sol 6.1. This is a conservative operator cap,
not a promised provider limit. A recent upstream throttle also spills new
threads for one recovery interval, including saturation caused by other clients;
existing pins continue through the bounded retry queue. GLM 5.3 retains its own
cap of 6 and has text-only input; its context declaration is now 1M. Both use zero marginal routing cost
on this included plan; published API list prices remain separate usage
accounting. FlashX's 200 tokens/s claim does not describe this model.

Capability sources: [GLM Flash](https://docs.z.ai/guides/vlm/glm-5.3-flash),
[GLM 5.3](https://docs.z.ai/guides/llm/glm-5.3),
[thinking](https://docs.z.ai/guides/capabilities/thinking), and
[API prices](https://docs.z.ai/guides/overview/pricing).
