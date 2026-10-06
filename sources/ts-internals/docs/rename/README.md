# Product-name migration checks

`src/core/repohygiene/repohygiene_test.go` scans tracked paths and UTF-8 text
files. It fails when the retired product name remains in a path or file.

`legacy-name-allowlist.tsv` is limited to files that repository rules reserve
for human owners. Each entry names its repository-relative path and explains
why an agent cannot rewrite it. The test rejects missing paths, empty reasons,
and stale entries. Active goals, contracts, source, configuration, and operator
documentation cannot use this exception.
