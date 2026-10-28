# GitHub Actions logs

Use `gh` against github.com. This legacy filename remains for incoming links.

```sh
gh run list --repo TerraScale/ts-orchestrator --status failure --limit 10
gh run view RUN_ID --repo TerraScale/ts-orchestrator --json jobs
gh run view RUN_ID --repo TerraScale/ts-orchestrator --log-failed
gh run view RUN_ID --repo TerraScale/ts-orchestrator --job JOB_ID --log
gh run view RUN_ID --repo TerraScale/ts-orchestrator --attempt 2 --log
```

Use the GitHub run ID, not its displayed run number. Job IDs come from that
run's jobs. For raw API access, GitHub returns a redirect to a log archive:

```sh
gh api repos/TerraScale/ts-orchestrator/actions/runs/RUN_ID/logs > run-logs.zip
gh api repos/TerraScale/ts-orchestrator/actions/jobs/JOB_ID/logs > job.log
```

Use the CLI's authenticated credential store; never put a token in a command
argument or print it. Logs can contain sensitive data; retain them in an owned
location and redact before sharing. Use the T3 PR watcher for pending checks.
