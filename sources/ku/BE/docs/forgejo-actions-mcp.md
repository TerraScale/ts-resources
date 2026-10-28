# GitHub Actions and Ku MCP

The old Actions MCP integration is retired. This legacy filename is retained
for incoming links; it does not describe a supported MCP tool surface.
Use Ku MCP for TerraScale tickets at ku.mariogk.com, and `gh` for repository
CI. Do not assume a renamed GitHub Actions MCP implementation is deployed.

```sh
gh run list --repo TerraScale/ts-resources --status failure --limit 20
gh run view RUN_ID --repo TerraScale/ts-resources
gh run view RUN_ID --repo TerraScale/ts-resources --log-failed
gh run view RUN_ID --repo TerraScale/ts-resources --job JOB_ID --log
gh run rerun RUN_ID --repo TerraScale/ts-resources --failed
gh run cancel RUN_ID --repo TerraScale/ts-resources
```

Use the numeric GitHub run ID, not the displayed run number. Inspect an older
attempt with `gh run view RUN_ID --attempt N`. Mutations require the relevant
GitHub permissions. Never print credentials or include them in command arguments.
Use the T3 PR watcher while waiting for checks; do not poll `gh` in loops.
