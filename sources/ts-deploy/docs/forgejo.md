# Forgejo Actions logs API

Forgejo 16.0 added REST endpoints for downloading Actions logs
(`forgejo/forgejo#12666`). They are plain HTTPS `GET`s against
`https://<host>/api/v1` — this is the reference to reach for whenever log
reads are needed (e.g. pulling a failed CI job's output).

Authenticate with a token in the `Authorization` header:

```
Authorization: token <token>
```

(Basic auth also works. Tokens live outside this repo — never put one in a
command argument that gets logged; prefer an environment variable.)

## Endpoints

| Method and path | Result |
| --- | --- |
| `GET /repos/{owner}/{repo}/actions/jobs/{job_id}/logs` | Plaintext log of one job (`text/plain`). Latest attempt by default; `?attempt=N` selects a historical attempt. Supports HTTP `Range:` resume (`200` full, `206` partial). |
| `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs` | ZIP (`application/zip`) of every job's latest-attempt log in the run. One entry per job named `{job-name}-{job-id}-attempt-{N}.log`. No `Range:` support. |

Both return `401`/`403`/`404` for bad credentials, forbidden access, and
unknown job/run ids. Pass the **job** id (from the job-listing endpoints),
not a task id — a task id here returns `404`.

## Finding the run and job ids

```
# Newest runs first; filters: event, status, run_number, head_sha, ref, workflow_id, page, limit
GET /repos/{owner}/{repo}/actions/runs?event=push&status=failure&limit=10

# Jobs of a run (each entry carries the job id and its attempt number)
GET /repos/{owner}/{repo}/actions/runs/{run_id}/jobs

# One job, including its ordered step list
GET /repos/{owner}/{repo}/actions/jobs/{job_id}
```

The `attempt` value from the job listing is what `?attempt=N` on the
job-logs endpoint expects. The run ZIP always holds the latest attempt of
each job; for an older attempt of one job, use the per-job endpoint with
`?attempt`.

## Examples

```bash
# Single job log (latest attempt)
curl -sSL -H "Authorization: token $FORGEJO_TOKEN" \
  "https://git.terrascale.tech/api/v1/repos/OWNER/NAME/actions/jobs/JOB_ID/logs"

# Older attempt of the same job
curl -sSL -H "Authorization: token $FORGEJO_TOKEN" \
  "https://git.terrascale.tech/api/v1/repos/OWNER/NAME/actions/jobs/JOB_ID/logs?attempt=2"

# Resume a large log from byte 1048576
curl -sSL -H "Authorization: token $FORGEJO_TOKEN" \
  -H "Range: bytes=1048576-" \
  "https://git.terrascale.tech/api/v1/repos/OWNER/NAME/actions/jobs/JOB_ID/logs"

# Whole run as a ZIP file
curl -sSL -H "Authorization: token $FORGEJO_TOKEN" \
  "https://git.terrascale.tech/api/v1/repos/OWNER/NAME/actions/runs/RUN_ID/logs" \
  -o "run-RUN_ID-logs.zip"
```

## Version floor

These endpoints exist only on Forgejo 16.0 and newer. Older instances
expose no REST log endpoint (only the web UI). Before relying on them
against an unfamiliar host, confirm the operation id is advertised:

```bash
curl -sSL https://<host>/swagger.v1.json | grep -o repoGetActionJobLogs
curl -sSL https://<host>/swagger.v1.json | grep -o repoGetActionRunLogs
```

References: [Forgejo 16.0 release announcement](https://forgejo.org/2026-07-release-v16-0/),
operation ids `repoGetActionJobLogs` / `repoGetActionRunLogs` in
`https://<host>/swagger.v1.json`.
