# Skill catalog audit

Issue: `TerraScale/TerraScale.Skills#2`
Baseline: `a30500fcc06cd892c283276e3a951a4f3e34a2aa`
Audit date: 2026-08-24

## Result

The catalog falls from 40 to 25 skills. Fifteen skills are removed because
they are aliases, generic agent defaults, overlapping routes, or unused
upstream utilities. Unique planning and architecture guidance moves into
`wayfinder` and `codebase-design`; specialized TerraScale operational and
safety knowledge stays.

Test fixtures are explicit-only so Codex no longer exposes fake fixture skills
such as `alpha`, `broken-link`, duplicate `same`, or the fixture fleet.

## Decision criteria

A retained skill must change agent behavior with non-obvious, reusable
guidance. The audit weighed:

1. **Usefulness:** concrete benefit beyond normal agent behavior.
2. **Distinctness:** a clear capability not better owned by another skill,
   repository policy, or the runtime.
3. **Use evidence:** observed pre-audit loads, callers, generated
   configuration, and tracker history. Missing telemetry is weak evidence,
   never proof of non-use.
4. **Maintainability:** one source of truth, truthful runtime claims, working
   links and metadata, and a size proportional to the job.
5. **Trigger clarity:** a discriminating description and an invocation mode
   that matches how the capability is reached.
6. **Safe deletion:** known references are removed or migrated and any useful
   behavior has a named replacement.

An uncertain skill stays when it contains unique high-risk or
TerraScale-specific knowledge. Low use is enough for deletion only when
overlap or generic behavior independently supplies the case.

## Evidence reviewed

- All 60 commits reachable from every local and remote ref, including the
  issue #1 work branches, plus per-path introduction and change history.
- Every current `SKILL.md`, `agents/openai.yaml`, set catalog, supporting
  resource, validator, fixture, test, linker, and live managed symlink.
- Forgejo issue #1 and its 13 comments, which explain the prior 40-skill
  hardening and its independent reliability gates.
- 382 pre-audit Codex session files containing 234,932 records. The
  `organic sessions` column counts distinct sessions that loaded no more
  than five catalog skills, excluding this audit; bulk catalog/fixture
  inspection is excluded. A load proves reach, not value.
- Current repository references and generated `docs/agents` configuration
  across the TerraScale workspace.

The complete history is short: the catalog was created on 2026-08-22, most
generic skills came from the Matt Pocock import, eight TerraScale workflows
were derived from workspace history, and issue #1 hardened all 40 on
2026-08-23. Earlier history had already removed `migrate-to-shoehorn` and
the old multi-tracker setup wrapper.

## Evidence locators

These evidence IDs apply to every row in the disposition table:

- **H1 — complete history:** `git rev-list --all --count` returns 60. Per-skill
  origin and change evidence comes from `git log --all -- <skill-path>` and
  the baseline tree at `a30500f`.
- **H2 — imported workflows:** `303d5a4` vendors the general skill set and
  `87292df` reorganizes it into the current top-level sets.
- **H3 — TerraScale workflows:** `2c2cadd` introduces `benchmark-record`,
  `contract-sync`, `devhost-cycle`, `evidence-gate`, `promote`, `sdk-release`,
  `upstream-sync`, and `workspace-wave` from workspace history.
- **H4 — independent additions:** `e35a671` introduces `agent-fleet`,
  `555459a` introduces `fleet-orchestrator`, `109690a` introduces `unslop`,
  and `5d63005` introduces `thread-to-tickets`.
- **T1 — hardening record:** Forgejo issue
  `TerraScale/TerraScale.Skills#1` and its 13 comments; mainline anchors
  `dd364d8`, `0eec477`, and `a30500f` cover policy, catalog/fleet validation,
  and final installation checks.
- **U1 — use evidence:** the 382 session files under `~/.codex/sessions/`
  before issue #2. Counts group loads by session, exclude this audit and bulk
  sessions that load more than five catalog skills, and do not equate a load
  with a successful outcome.
- **C1 — sources and consumers:** the baseline root catalog at
  `a30500f:README.md`, per-set catalogs, `git ls-tree -r a30500f`, current
  skill-local links, the two managed discovery directories, and workspace
  `docs/agents/issue-tracker.md` files that name `wayfinder` labels.
- **V1 — executable evidence:** `scripts/validate-skills.py`,
  `scripts/validate-fleet.py`, `tests/test_validate_skills.py`,
  `tests/test_validate_fleet.py`, the guardrail fixture script, and
  `scripts/link-codex-skills.sh --check` against both discovery directories.

All 40 rows use H1, T1, U1, C1, and V1. Imported rows additionally use H2;
the eight TerraScale-derived rows use H3; and the four independent additions
use H4. The final column states the row-specific judgment and replacement.

## Per-skill disposition

| Skill | Organic sessions | Decision | Evidence and replacement |
| --- | ---: | --- | --- |
| agent-fleet | 16 | Keep | Unique OpenCode fleet runtime and installation contract. |
| fleet-orchestrator | 35 | Keep | Unique Codex delegation, capability, and verification protocol. |
| benchmark-record | 1 | Keep | Low use, but unique TerraBase benchmark provenance and lane rules. |
| code-review | 53 | Keep | High use and distinct Standards/Spec review axes. |
| codebase-design | 50 | Keep and deepen | High use; absorbs architecture scanning from `improve-codebase-architecture`. |
| contract-sync | 0 | Keep | No organic load, but unique cross-repository public-contract order and safety rules. |
| devhost-cycle | 1 | Keep | Unique fixed tailnet URL, lease, and profile invariants. |
| diagnosing-bugs | 14 | Keep | Distinct red-capable feedback-loop discipline. |
| domain-modeling | 6 | Keep | Owns glossary, context, and ADR decisions used across repositories. |
| evidence-gate | 0 | Keep | Unique candidate/evidence binding and external repository consumers; low use alone is insufficient. |
| grill-with-docs | 2 | Remove | Thin composition of `grilling` and `domain-modeling`; callers can use those directly. |
| implement | 29 | Remove | Frequently loaded by old protocols but contains only generic implementation steps already enforced by the runtime, issue policy, `tdd`, and `code-review`. |
| improve-codebase-architecture | 0 | Remove and merge | Architecture audit guidance moves to `codebase-design/ARCHITECTURE-AUDIT.md`; the mandatory styled HTML report is discarded. |
| promote | 0 | Keep | Unique digest-bound TerraScale promotion and rollback boundaries. |
| prototype | 0 | Keep | Unique logic/UI prototype branches and reusable supporting guides. |
| research | 5 | Keep | Demonstrated use and a clear primary-source Markdown deliverable. |
| resolving-merge-conflicts | 2 | Remove | Generic Git behavior already covered by runtime safety and repository instructions; no TerraScale-specific mechanism. |
| router | 2 | Remove | Duplicates descriptions and three catalogs, costs 13 KB, and cannot invoke explicit-only skills. |
| sdk-release | 0 | Keep | Unique protected npm/NuGet gates and immutable artifact rules. |
| setup-skills | 3 | Keep and trim references | Proven generator of workspace `docs/agents` configuration; retains a one-time setup boundary. |
| tdd | 87 | Keep | Highest-use engineering skill and distinct seam/test guidance. |
| thread-to-tickets | 2 | Keep | Explicit user-requested history reconciliation with stable identity and retry safety. |
| to-spec | 0 | Remove and merge | Spec behavior moves to `wayfinder/references/spec.md`. |
| to-tickets | 0 | Remove and merge | Vertical slicing and dependency guidance moves to `wayfinder/references/tickets.md`. |
| triage | 9 | Keep | Used and coupled to the workspace's triage labels and agent briefs. |
| upstream-sync | 0 | Keep | Unique TerraBase fork, licensing, branding, and cherry-pick policy. |
| wayfinder | 0 | Keep and deepen | Existing generated tracker configuration depends on it; it now routes decision maps, specs, and tickets. |
| wizard | 1 | Keep | Unique provider-neutral human-in-the-loop script template and secret handling. |
| workspace-wave | 0 | Remove | Multi-repository mechanical work is already owned by `fleet-orchestrator` plus the workspace and work-item policies. |
| git-guardrails-claude-code | 4 | Keep | Demonstrated use, executable defense-in-depth hook, and fixture suite. |
| scaffold-exercises | 0 | Remove | Unused imported course-specific utility outside TerraScale's product workflow. |
| setup-pre-commit | 0 | Remove | Unused generic package setup that duplicates repository-native discovery and can become stale across package managers. |
| grill-me | 0 | Remove | Eleven-line alias for `grilling`. |
| grilling | 6 | Keep | Used shared primitive that distinguishes facts, defaults, and user decisions. |
| handoff | 0 | Remove | Generic summarization now covered by goal persistence, issue receipts, and normal agent behavior. |
| teach | 0 | Remove | Large imported teaching workspace with no demonstrated TerraScale use. |
| to-questionnaire | 0 | Remove | Generic document writing with no specialized TerraScale knowledge or observed use. |
| wait-what | 0 | Remove | Normal re-explanation behavior encoded as a 17-line alias. |
| writing-for-agents | 23 | Keep | Demonstrated use and unique pointer, load, metadata, and runtime-truth review model. |
| unslop | 165 | Keep | Most-used catalog skill; preserves protected content while editing prose. |

## Supporting-resource disposition

The baseline contains 26 non-entrypoint files outside the fleet package, plus
20 fleet manuals, contracts, agent definitions, commands, and manifests.
Skill metadata follows its owning skill: 25 `agents/openai.yaml` files remain,
15 are removed with their skills, and test-fixture metadata becomes
explicit-only.

| Baseline resource group | Decision | Evidence and replacement |
| --- | --- | --- |
| `agent-fleet/FLEET.md`, `fleet-orchestrator-manifest.yaml`, nine `opencode/agents/fleet/*.md`, five `opencode/commands/fleet/*.md`, and four `codex/fleet-orchestrator/references/*.md` | Keep | Unique fleet runtime, capability, handoff, and verification contract (H4, T1, V1). Coordination references drop the deleted `implement` wrapper. |
| `codebase-design/DEEPENING.md` and `DESIGN-IT-TWICE.md` | Keep | Existing deep-module design branches remain linked; new `ARCHITECTURE-AUDIT.md` receives the evidence-ranking behavior from the removed architecture skill. |
| `diagnosing-bugs/scripts/hitl-loop.template.sh` | Keep | Executable HITL feedback-loop template remains owned and linked by `diagnosing-bugs`. |
| `domain-modeling/ADR-FORMAT.md` and `CONTEXT-FORMAT.md` | Keep | Stable templates remain the single format source for ADR and bounded-context artifacts. |
| `improve-codebase-architecture/HTML-REPORT.md` | Remove | CDN-backed styled output is not required for an architecture decision; compact Markdown guidance moves to `codebase-design/ARCHITECTURE-AUDIT.md`. |
| `prototype/LOGIC.md` and `UI.md` | Keep | Distinct logic and visual-prototype branches remain progressively loaded. |
| `router/PHASE-BOUNDARIES.md` | Remove | Its phase table existed only to support the deleted duplicative router; retained descriptions and catalogs own selection. |
| Four `setup-skills/*.md` references | Keep and repair | Domain, project-state, triage, and Forgejo configuration remain unique; deleted-skill pointers and Forgejo label-removal syntax are corrected. |
| `tdd/mocking.md` and `tdd/tests.md` | Keep | Focused test-boundary and mocking references remain progressively loaded. |
| `thread-to-tickets/references/ticket-reconciliation-schema.md` | Keep | Stable identity and retry-safe reconciliation schema remains unique (H4, T1). |
| `triage/AGENT-BRIEF.md` and `OUT-OF-SCOPE.md` | Keep | Tracker-specific handoff and classification formats remain owned by `triage`. |
| `wizard/template.sh` | Keep | Provider-neutral human-executed shell template remains the skill's deliverable. |
| Two `git-guardrails-claude-code/scripts/*.sh` files | Keep | Hook implementation and its 23-blocked/7-safe fixture suite remain executable defense in depth (V1). |
| Four `teach/*-FORMAT.md` files | Remove | They serve only the unused imported teaching workspace and have no independent consumer. |
| `writing-for-agents/SKILL-MECHANICS.md` | Keep | Unique skill metadata, invocation, and progressive-disclosure mechanics remain used by skill maintenance. |
| New `wayfinder/references/{map,spec,tickets}.md` | Add | These receive the useful decision-map, contract, vertical-slice, ownership, and dependency behavior formerly split across three planning skills. |

## Compatibility

- Root and set catalogs list exactly the 25 retained skills.
- Removed names have no live managed symlink after relinking either
  `~/.codex/skills/` or the workspace-local `.codex/skills/`; both contain the
  same 25 retained links. The workspace-local README points to the canonical
  catalog instead of duplicating stale entries.
- `wayfinder` is now model-invoked and covers the former spec and ticket
  branches without requiring users to remember three planning skills.
- `codebase-design` covers architecture audits without a second skill or
  mandatory CDN-backed HTML artifact.
- The validator no longer requires a duplicative router, and it rejects
  model-invoked fixture skills that would leak into discovery.
- Retained skill references, UI metadata, scripts, and supporting resources
  remain validator- and link-checked.
