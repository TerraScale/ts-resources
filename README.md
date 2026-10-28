# ts-resources

TerraScale logos, images, fonts, documentation, agreements, terms of service,
privacy policies, and other reusable resources collected from the local
TerraScale repositories.

## Find a resource

| Resource | Location |
| --- | --- |
| TerraScale logos and icons, including Auth | [logos/terrascale](logos/terrascale/) |
| Ku logos and icons | [logos/ku](logos/ku/) |
| Current documentation | [sources/ts-docs/docs](sources/ts-docs/docs/) |
| Terms, privacy policy, DPA, security, and support | [sources/ts-docs/docs/legal](sources/ts-docs/docs/legal/) |
| Landing site images, icons, and fonts | [sources/ts-landing/static](sources/ts-landing/static/) |
| Dashboard assets | [sources/ts-dashboard/web/static](sources/ts-dashboard/web/static/) |
| Current repository resources | [sources](sources/) |
| Earlier repository resources | [archive](archive/) |
| Complete source catalog | [SOURCES.md](SOURCES.md) |

### Logo formats

Every SVG has a PNG with the same basename beside it. Original SVGs and
existing raster formats are preserved. PNG companions use `rsvg-convert`
at twice the SVG's natural dimensions, with transparency preserved.
White logos are intended for dark backgrounds.

Known source defect: `layout-dashboard.svg` in both the current and archived
landing-site Lucide icons omits rectangle widths and heights. Those original
SVGs and their PNG companions are blank; the source defect is recorded in
the manifest. Other SVG companions contain visible content.

![TerraScale blue logo](logos/terrascale/logo-terrascale-blue.png)

### Legal documents

The current legal directory contains the Terms of Service, Privacy Policy,
Data Processing Agreement, Security Policy, and Support Policy. Additional
language versions are under `sources/ts-docs/docs/<language>/legal/`.
Earlier terms, acceptable-use policies, and data-processing terms are under
[archive/Terrascale.Documentation/docs/legal](archive/Terrascale.Documentation/docs/legal/).
Ku's privacy page source is preserved under
[sources/ku/WEB/src/routes/privacy](sources/ku/WEB/src/routes/privacy/).

Legal files retain their original draft warnings, placeholders, and approval
requirements. Collecting them here does not approve them or put them into
effect. Files in `archive/` are historical references.

## Source copies

`sources/<repository>/` and `archive/<repository>/` preserve original paths.
These are snapshots of local files, not automatically synchronized mirrors.
Local hosting adaptations are labelled in the manifest; see [HOSTING.md](HOSTING.md).
The original repositories are unchanged. Active copied instructions are adapted
to the current GitHub workflow, with changes recorded in the manifest.
Application code, dependencies,
build outputs, test fixtures, and source-root agent instruction files are excluded;
the Ku privacy page source is included because it contains the policy.

[manifest.json](manifest.json) records source repositories, commit IDs,
original paths, and SHA-256 hashes for every copied or generated resource.
`logos/` provides convenient copies of the existing brand files.
Source licenses and font notices are retained where available; collecting
a file does not change its ownership or license. This repository is public on
[GitHub](https://github.com/TerraScale/ts-resources).

## GitHub workflow

Use `gh` for PRs, GitHub Issues, Actions, and releases, and Git over SSH to
github.com. TerraScale tickets use Ku (ku MCP, ku.mariogk.com). Forgejo and
`git.terrascale.tech` have been dead since 2026-10-11. The
[contributor instructions](AGENTS.md) define ready-for-review PRs, optional
local checks, CI on GitHub-hosted runners, and merging only a green latest
head rebased on current main. No review approval is required.

Dated evidence and original provenance remain historical. Retired repositories
without a verified GitHub copy are named as plain text. See the
[archive notice](archive/README.md) before following archived references.

## Verify the collection

Run from this repository with Python 3; no Python packages are required:

```sh
python3 scripts/check_resources.py
```

The check verifies the manifest, resource hashes, PNG headers, and a PNG
companion for every SVG.
