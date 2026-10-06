# Pin ts-builder in Forgejo Actions

ts-builder publishes to `git.terrascale.tech/terrascale/ts-builder` from
`main` only, after lint, all checks, and verification inside the freshly built
image succeed. Pull-request builds never publish.

| Reference | Behavior |
| --- | --- |
| `:latest` | Mutable: moves to the image from a successful main publication. |
| `:<full commit SHA>` | Tied to the ts-builder source commit; its existing image is preserved on reruns. |
| `@sha256:<digest>` | Strongest content pin: selects the exact published image manifest. |

## Pin a consuming repository

In `.forgejo/workflows/ci.yml`, replace the placeholders below with values
from a successful ts-builder publication. Use one of these alternatives.

Full commit SHA (all 40 hexadecimal characters):

```yaml
jobs:
  build:
    runs-on: terrascale-builder
    container:
      image: "git.terrascale.tech/terrascale/ts-builder:<full-40-character-commit-sha>"
    steps:
      - run: ts-builder-verify
```

Image digest (64 hexadecimal characters after `sha256:`):

```yaml
jobs:
  build:
    runs-on: terrascale-builder
    container:
      image: "git.terrascale.tech/terrascale/ts-builder@sha256:<64-character-digest>"
    steps:
      - run: ts-builder-verify
```

## Find the pin

1. Open [ts-builder Actions](https://git.terrascale.tech/terrascale/ts-builder/actions)
   and select a successful **main** run that published an image.
2. For a SHA pin, copy that run's full source commit SHA from its commit page.
   Use the **ts-builder** commit, not the consuming repository's commit or a PR
   revision. Confirm the tag exists in the Forgejo ts-builder container package.
3. For a digest pin, copy the published `sha256:…` value from the publishing
   job summary. Keep the `sha256:` prefix and use `@` instead of `:` before it.

To upgrade, select another successful main publication and replace the pin
in the consuming workflow.
