# Required cryptographic key material

## Outcome

Authentication and Data Protection now fail during registration or first key
resolution when their required key material is absent. Development and testing
service code no longer silently substitutes compiled-in signing or
key-encryption material.

Local and regional operation remain explicit: AppHost and the Orchestrator
provide `Jwt__Secret` to Authentication and Platform workloads. A deployment
may instead provide a dedicated 256-bit Data Protection key through
`DataProtection__KeyEncryptionKeyBase64`; key rotation continues to use the
configured key ID and key collection.

## Compatibility

This is an intentional greenfield configuration break for hosts that depended
on an implicit development secret. Such hosts must provide `Jwt:Secret` (or
`Jwt__Secret`) before startup. There is no storage-format or public API change.
Existing encrypted Data Protection records remain readable when the same
configured JWT secret or dedicated key material is supplied.

## Coordination and evidence

- Owner: Authentication and shared Data Protection configuration.
- Kind: source and validation.
- Scope: shared AES-GCM key resolution, Authentication resource registration,
  token-issuing handlers, host registration call sites, and focused tests.
- Baseline: Development and Testing silently used compiled-in secret material
  when configuration was absent.
- Dependencies: AppHost and the Orchestrator already inject explicit JWT key
  material for every local/regional Authentication and Platform workload.
- Evidence: Release build of `TerraScale.Platform.Tests` succeeded with zero
  warnings; all eight `AuthenticationApiRegistrationTests` passed, including
  missing-JWT and missing-Data-Protection-key regression cases; source search
  confirms the application fallback constant and the fixed Data Protection
  secret are absent. The Authentication test project also built with zero
  warnings, and its focused discovery/token-request host test passed with
  explicit fixture key material.
- Full-suite note: the broader Platform run passed 18 tests and skipped two
  externally gated cases before its Aspire fixture failed to start a second
  three-node TerraBase topology while the regional DevHost topology was active.
  The Authentication suite passed nine service tests before a separate AppHost
  case timed out while attempting another three-node topology under the same
  contention. These topology-contention results are not represented as product
  validation.
- Handoff: the active regional DevHost remains running and was not stopped or
  mutated. Its exclusive Orchestrator validation lease remains in force.
