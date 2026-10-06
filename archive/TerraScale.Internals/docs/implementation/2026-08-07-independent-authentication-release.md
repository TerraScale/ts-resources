# Independent Authentication release boundary

## Outcome

Authentication is now built, tested, and published as an independent executable in the repository release graph. Both Authentication and Platform consume a shared `TerraScale.Platform.Application` library; neither executable references the other.

## Root cause

`TerraScale.Authentication` previously referenced the executable `TerraScale.Platform` project to reuse its application services. Publishing Authentication therefore traversed two web hosts. Both hosts contributed an `appsettings.json` to the same publish output, and the .NET SDK correctly rejected the ambiguous output with `NETSDK1152`.

The deployment descriptor did not publish Authentication, so the invalid executable dependency remained outside the normal candidate gate.

## Resolution

- `TerraScale.Platform.Application` owns the reusable configuration, feature, and infrastructure code as a library assembly.
- Platform and Authentication reference that library instead of one host referencing another host.
- Only the application library holds the TerraBase client dependency, preserving the storage access boundary.
- The release descriptor runs Authentication's non-integration regression suite and publishes both `linux-x64` and `linux-arm64` candidates.
- Promotion declares the native `native-blue-green` strategy. The retired Flux strategy is no longer part of this repository's contract.

Integration tests remain in their dedicated real-topology lane because they acquire the shared AppHost topology lease. The release-profile regression command deliberately excludes tests categorized `Integration`.

## Verification

The change was verified with:

- a Release restore and solution build;
- all non-integration Authentication tests (12 passed);
- all non-integration Platform tests (202 passed);
- focused storage-boundary, TerraBase API contract, and AppHost diagnostic tests;
- Release publishes for Authentication and Platform on `linux-x64` and `linux-arm64`;
- executable presence checks in all four candidate outputs.
