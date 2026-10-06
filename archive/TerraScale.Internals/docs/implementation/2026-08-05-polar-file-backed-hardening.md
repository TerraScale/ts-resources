# Polar file-backed hardening

Polar production secrets now use absolute owner-private file references. The selected Polar provider
fails startup for invalid secret sourcing, URLs, or webhook bounds; raw secrets remain limited
to Development and Testing. On Linux, the reader opens every path component with `O_NOFOLLOW`,
validates the already-open descriptor as an owner-owned regular file, caps it at 16 KiB, and reads
only that descriptor. This rejects symlinked ancestors, final symlinks, directories, group/other
permissions, and replacement races; unsupported platforms fail closed.

The opt-in external Polar sandbox harness reuses that reader before it constructs an Authorization
header, so arbitrary local file contents cannot be transmitted. Coverage includes oversized,
non-regular, symlinked-ancestor, and deterministic path-replacement cases, plus file-backed
current/previous webhook-secret rotation. Webhook ingress verifies the exact bounded raw request
bytes before queueing; AppHost tests cover a valid signed max-plus-one body and a valid signed
unknown-length (chunked) body, alongside a raw UTF-8 byte signature case.

Validation: `dotnet test --project src/Payments/TerraScale.Payments.Tests/TerraScale.Payments.Tests.csproj --no-progress --fail-fast`
passed (25 tests; 2 opt-in live-sandbox tests skipped). The AppHost fixture currently supplies its
Polar secret as a Testing raw-secret environment value, so an end-to-end *file-backed* rotation
test requires fixture configuration outside this change's owned paths. The existing AppHost DI
failure must be recorded if it prevents that suite from running; this change does not weaken it.

Attempted AppHost evidence: the filtered `PolarBillingAspireAppHostIntegrationTests` runner remained
blocked in `futex_do_wait` for 6m23s (its child runner for 5m51s) without producing a test result or
diagnostic output, so its directly-owned test process was stopped rather than restarted. A subsequent
fast Platform test-project build is independently blocked by unrelated concurrent Core Metadata edits:
`TerraBaseCoreMetadataRepository.cs` has six `CS0104` ambiguous `SessionOptions` errors (lines 1089,
1384, 1838, 1912, 2022, and 2596). No AppHost fixture or Core Metadata source was changed here.
