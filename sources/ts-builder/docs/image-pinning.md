# Pin ts-builder in GitHub Actions

ts-builder publishes to `ghcr.io/terrascale/ts-builder` from
`main` only, after lint, all checks, and verification inside the freshly built
image succeed. Pull-request builds never publish.

| Reference | Behavior |
| --- | --- |
| `:latest` | Mutable: moves to the image from a successful main publication. |
| `:<full commit SHA>` | Tied to the ts-builder source commit; its existing image is preserved on reruns. |
| `@sha256:<digest>` | Strongest content pin: selects the exact published image manifest. |

## Pin a consuming repository

In `.github/workflows/ci.yml`, replace the placeholders below with values
from a successful ts-builder publication. Use one of these alternatives.

Full commit SHA (all 40 hexadecimal characters):

```yaml
jobs:
  build:
    runs-on: ubuntu-24.04
    container:
      image: "ghcr.io/terrascale/ts-builder:<full-40-character-commit-sha>"
    steps:
      - run: ts-builder-verify
```

Image digest (64 hexadecimal characters after `sha256:`):

```yaml
jobs:
  build:
    runs-on: ubuntu-24.04
    container:
      image: "ghcr.io/terrascale/ts-builder@sha256:<64-character-digest>"
    steps:
      - run: ts-builder-verify
```

## Find the pin

1. Select the current GitHub publishing repository from the release inventory,
   verify it with `gh api repos/TerraScale/<repo>`, and inspect a successful
   **main** run with `gh run view RUN_ID --repo TerraScale/<repo>`. The old
   standalone ts-builder repository has no verified GitHub copy; do not infer
   that these example GHCR references are published.
2. For a SHA pin, copy that run's full source commit SHA from its commit page.
   Use the **ts-builder** commit, not the consuming repository's commit or a PR
   revision. Confirm the tag exists in the GHCR container package.
3. For a digest pin, copy the published `sha256:…` value from the publishing
   job summary. Keep the `sha256:` prefix and use `@` instead of `:` before it.

To upgrade, select another successful main publication and replace the pin
in the consuming workflow.
