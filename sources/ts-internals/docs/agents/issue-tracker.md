# Issue tracker: GitHub and Ku

TerraScale tickets and specs live in Ku (ku MCP, ku.mariogk.com). Repository
issues live in GitHub Issues and use the `gh` CLI. Choose the tracker from the
request; do not copy a Ku ticket into GitHub unless explicitly requested.

## Conventions

- Infer the GitHub repository from `origin` and verify it before any write.
- Preserve existing issue content and labels unless the task changes them.
- Outside a checkout, pass `--repo TerraScale/<repo>` explicitly.
- Use `--body-file` for long issue bodies and comments.

## Repository issue commands

- Create: `gh issue create --title "..." --body-file /path/to/body.md`
- Read: `gh issue view <number> --comments`
- Search: `gh issue list --search "query" --state open`
- Comment: `gh issue comment <number> --body-file /path/to/comment.md`
- Labels: `gh issue edit <number> --add-label "..." --remove-label "..."`
- Assign: `gh issue edit <number> --add-assignee "@me"`
- Close: `gh issue close <number> --comment "explanation"`

## Pull requests

Use ready-for-review GitHub PRs for code changes; never drafts. CI is the gate,
with no local tests required before push and no required review approval.
ts-reviewer is not deployed. Address and answer every reviewer finding. Keep
at most one open PR per repository per thread. Rebase on current main and
merge only when CI is green on the exact latest head. Use the T3 PR watcher
instead of polling. See the root [workflow](../../../../AGENTS.md).

## Skills and wayfinding

When a skill says "publish to the issue tracker" or "fetch the relevant ticket",
use Ku for TerraScale tickets and `gh issue` for repository issues. Read the
body, comments, labels, state, assignees, and blockers in the chosen tracker.

For a repository map, use one GitHub issue labelled `wayfinder:map`. Child
issues begin with `Part of #<map>` and carry `wayfinder:research`,
`wayfinder:prototype`, `wayfinder:grilling`, or `wayfinder:task`. Record
`Blocked by: #<number>, #<number>` at the top of the body. A ticket is available
when open, unassigned, and without an open blocker. Claim it with
`gh issue edit <number> --add-assignee "@me"`. Post the answer, close the
issue, and update the map's Decisions-so-far section when done. For Ku maps,
use Ku identifiers, relationships, and assignments instead.
