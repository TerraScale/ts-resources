# GitHub repository workflow and Ku tickets

This legacy document path now points to the supported workflow. The former
repository integration is retired; the old settings, webhook routes, tokens,
and automation rules must not be used. These resource copies do not implement
or prove deployment of a replacement Ku integration.

TerraScale tickets live in Ku at ku.mariogk.com and are accessed through Ku
MCP. Repository issues, PRs, CI, and releases live on github.com/TerraScale.
Use `gh` for those operations and Git over SSH to github.com. Validate the
selected repository with `gh api repos/TerraScale/<repo>` before writing.

```sh
gh issue list --repo TerraScale/ts-resources
gh pr list --repo TerraScale/ts-resources
gh pr view NUMBER --repo TerraScale/ts-resources --comments
gh run list --repo TerraScale/ts-resources --limit 10
gh release list --repo TerraScale/ts-resources
```

Keep ticket identifiers in branch names and PR descriptions so work remains
traceable. Update Ku explicitly through Ku MCP; do not assume a PR event or
closing keyword updated a ticket. Repo issue closing keywords target GitHub
Issues in that repository.

Open ready-for-review PRs, never drafts, with at most one open PR per repository
per thread. CI runs on GitHub-hosted runners and is the gate; local tests are
optional before push. No review approval is required. Fix and answer every finding, rebase on current main, and merge only
when the exact latest head is green. `terrascale` and `ts-dashboard` use
`gh pr merge --auto --squash` for their merge queues; other repositories merge
directly when green. Use the T3 PR watcher for pending checks.

See [Actions commands](forgejo-actions-mcp.md) and the root
[workflow](../../../../../AGENTS.md). Keep all credentials out of logs and
source. Configure only integration features actually available in the deployed
Ku version; this document does not authorize installing or redeploying one.
