# Working in ts-resources

This public repository collects resource snapshots. Use GitHub at
https://github.com/TerraScale/ts-resources and Git over SSH to github.com.
Use `gh` for pull requests, repository issues, Actions, and releases. TerraScale
tickets belong in Ku (ku MCP, ku.mariogk.com); repository issues belong in
GitHub Issues. Forgejo at git.terrascale.tech has been dead since 2026-10-11.
Do not use its CLI, MCP, API, package registry, or the retired COS script.

## GitHub workflow

- Open ready-for-review pull requests, never drafts. Keep at most one open PR
  per repository per thread. Do not add AI attribution to commits or PRs.
- CI is the gate; local tests are optional before pushing. GitHub Actions
  must use GitHub-hosted runners only.
- **Start from latest main.** Base every change on the most recent `main`: before starting, `git fetch origin` and branch from `origin/main`, never from a stale local `main`, another feature branch or an old worktree. Before every push, `git fetch origin && git rebase origin/main` again; right before merging, rebase once more and merge only when CI is green on that exact head.
- Address and answer every reviewer finding.
- No review approval is required. Do not request mariogk or any bot as
  reviewers.
- This repository merges directly when green. `terrascale` and `ts-dashboard`
  use the merge queue through `gh pr merge --auto --squash`.
- Use the T3 PR watcher for pending checks or reviews; do not poll `gh` in loops.

## Preserve the collection

Keep `archive/**` historical. Its README identifies dead references. Preserve
original dated evidence, review reports, changelogs, captured output,
`docs/evidence/**`, and `.qualification/**` under `sources/**` as well.
Update active instructions without presenting historical results as current.
Do not invent GitHub counterparts for retired repositories or issue numbers;
verify replacement repositories and paths with `gh api`.

For an adapted resource, update its SHA-256 and append a dated
`local_adaptation` note in `manifest.json`. Keep original source paths,
repositories, remotes, commits, and other provenance intact. Register new
resources under `sources/`, `archive/`, or `logos/` in the manifest.
`python3 scripts/check_resources.py` checks hashes and image coverage; CI runs
it for resource changes. No application builds are needed for documentation.
