# TerraScale.Skills

Reusable skills for TerraScale development and delivery work.

## Issue-first work

Substantive engineering work starts with an issue in the owning Forgejo
repository. Read [engineering/WORK-ITEM-POLICY.md](engineering/WORK-ITEM-POLICY.md)
for the work contract and external-effect boundaries.

## Checkout and discovery

Keep the canonical checkout at `~/.codex/skills/TerraScale.Skills/`. Link its
skills into `~/.codex/skills/`:

```bash
git clone ssh://git@git.terrascale.tech/TerraScale/TerraScale.Skills.git \
  ~/.codex/skills/TerraScale.Skills
~/.codex/skills/TerraScale.Skills/scripts/link-codex-skills.sh
```

The linker creates missing canonical links. It does not replace real paths or
remove stale links; removals are deliberate and `--check` reports drift.

## Catalog

| Skill | Canonical source |
| --- | --- |
| agent-fleet | [agent-fleet/SKILL.md](agent-fleet/SKILL.md) |
| fleet-orchestrator | [agent-fleet/codex/fleet-orchestrator/SKILL.md](agent-fleet/codex/fleet-orchestrator/SKILL.md) |
| benchmark-record | [engineering/benchmark-record/SKILL.md](engineering/benchmark-record/SKILL.md) |
| code-review | [engineering/code-review/SKILL.md](engineering/code-review/SKILL.md) |
| codebase-design | [engineering/codebase-design/SKILL.md](engineering/codebase-design/SKILL.md) |
| contract-sync | [engineering/contract-sync/SKILL.md](engineering/contract-sync/SKILL.md) |
| devhost-cycle | [engineering/devhost-cycle/SKILL.md](engineering/devhost-cycle/SKILL.md) |
| diagnosing-bugs | [engineering/diagnosing-bugs/SKILL.md](engineering/diagnosing-bugs/SKILL.md) |
| domain-modeling | [engineering/domain-modeling/SKILL.md](engineering/domain-modeling/SKILL.md) |
| evidence-gate | [engineering/evidence-gate/SKILL.md](engineering/evidence-gate/SKILL.md) |
| promote | [engineering/promote/SKILL.md](engineering/promote/SKILL.md) |
| prototype | [engineering/prototype/SKILL.md](engineering/prototype/SKILL.md) |
| research | [engineering/research/SKILL.md](engineering/research/SKILL.md) |
| sdk-release | [engineering/sdk-release/SKILL.md](engineering/sdk-release/SKILL.md) |
| setup-skills | [engineering/setup-skills/SKILL.md](engineering/setup-skills/SKILL.md) |
| tdd | [engineering/tdd/SKILL.md](engineering/tdd/SKILL.md) |
| thread-to-tickets | [engineering/thread-to-tickets/SKILL.md](engineering/thread-to-tickets/SKILL.md) |
| triage | [engineering/triage/SKILL.md](engineering/triage/SKILL.md) |
| upstream-sync | [engineering/upstream-sync/SKILL.md](engineering/upstream-sync/SKILL.md) |
| wayfinder | [engineering/wayfinder/SKILL.md](engineering/wayfinder/SKILL.md) |
| wizard | [engineering/wizard/SKILL.md](engineering/wizard/SKILL.md) |
| git-guardrails-claude-code | [misc/git-guardrails-claude-code/SKILL.md](misc/git-guardrails-claude-code/SKILL.md) |
| grilling | [productivity/grilling/SKILL.md](productivity/grilling/SKILL.md) |
| writing-for-agents | [productivity/writing-for-agents/SKILL.md](productivity/writing-for-agents/SKILL.md) |
| unslop | [unslop/SKILL.md](unslop/SKILL.md) |

The repository contains 25 skills. See [CATALOG-AUDIT.md](CATALOG-AUDIT.md)
for the evidence and disposition of the former 40-skill catalog.
