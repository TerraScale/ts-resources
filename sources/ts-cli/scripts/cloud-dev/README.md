# Real cloud CLI journey

This executable runner measures the CLI-to-two-browser journey using
an exact CLI binary and packaged `create-terrascale-app` artifact against real
public test services. It never starts TerraBase, replaces API responses, imports
browser login state, creates accounts, or supplies infrastructure credentials.
A passed report requires the entire measured journey to finish within 300 seconds.
Until a report from an identified environment passes, this journey remains unqualified.

Prerequisites are Node.js, npm, tar, a graphical session, the CLI release candidate,
the starter package archive, and an existing authorized disposable project/source
database on the intended public services. The API must accept the externally
issued project API key; the auth service must support `terrascale-starter-web`
with callback `http://localhost:3000/`, branch
creation, schema/seed writes, and the shared HTTP reactive transport. Browser users
must already have access to the selected project. No signup/payment steps are automated.
Provide source revisions from the verified artifact build records; the runner
hashes the artifacts itself but does not independently attest their source mapping.
Installing the runner and Chromium is setup outside the measured journey:

```sh
cd scripts/cloud-dev
npm ci
npx playwright install chromium
export QUALIFICATION_TEST_ENVIRONMENT=authorized
export QUALIFICATION_CLI=/absolute/path/to/ts
export QUALIFICATION_STARTER_ARTIFACT=/absolute/path/to/create-terrascale-app.tgz
export QUALIFICATION_CLI_REVISION=verified-cli-source-revision
export QUALIFICATION_STARTER_REVISION=verified-starter-source-revision
export QUALIFICATION_API_URL=https://api.terrascale.tech
export QUALIFICATION_AUTH_URL=https://app.terrascale.tech
export QUALIFICATION_API_KEY=externally-issued-disposable-project-key
export QUALIFICATION_SOURCE_DATABASE=authorized-test-source
export QUALIFICATION_PROJECT_ID=authorized-test-project
export QUALIFICATION_REPORT=/absolute/path/to/cloud-journey.json
./qualify.mjs
```

Replace these service and project values with the explicitly authorized test
environment. Running creates a unique branch and submits schema/document writes
under that project's normal billing policy. The runner requires the explicit
`authorized` value before beginning; setting it attests that the test project and
its effects are authorized. It does not itself establish a billing sandbox.
`QUALIFICATION_PORT` optionally selects another registered localhost callback port.

The API key must be issued beforehand by an authorized project owner; the runner
never creates, guesses, or interactively replaces credentials. Sign in separately
in the two browser windows when prompted. The runner uses fresh private CLI
configuration and separate browser contexts.
It runs `doctor`, scaffolds and installs the packaged starter, creates/reuses the cloud branch,
applies the schema, seeds one post, generates all four binding languages, verifies cloud dev regenerates bindings after
a local schema edit while its public diagnostic polling is active, and
verifies seed visibility plus a write from each browser observed in both live views.
All CLI calls and the browser waits share the five-minute deadline. The app uses
the normal public SDK, authorization, and reactive paths.

The owner-only JSON report records exact CLI/starter archive hashes, the resolved
starter dependency-lock hash, supplied source revisions, service origins, test scope, each phase's elapsed
time, and the outcome. Browser sign-in is interactive and is not captured in
screenshots, traces, or stored browser state. On exit the runner removes its
private CLI configuration; the report records `loginRevocation` as
`not-applicable-external-key` because the externally issued API key remains
owned by its issuer and must be revoked there. The private temporary workspace and branch remain available
for investigation; remove the disposable branch through its public deletion flow
after reviewing the run. A retained branch is not evidence of completed cleanup.

`node --check qualify.mjs` verifies syntax only. Missing service access, browser
setup, package access, or authorization leaves the scenario unpassed. This runner
covers the fresh CLI/cloud developer journey; it does not qualify signup, billing,
all SDK runtime consumers, or production recovery.
