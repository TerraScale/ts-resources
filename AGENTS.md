# Working in ts-resources

This public repository collects resource snapshots. Repository issues belong in
GitHub Issues; TerraScale tickets belong in Ku (ku MCP, ku.mariogk.com).

Workspace rules (hosting, secrets, models, Cloudflare, GitHub and shipping) are in the **Shipping code** section of the TerraScale workspace AGENTS.md.

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
