# Initial workflow implementation record

## Index

- [Validation evidence](validation-evidence.md)
- [OpenAPI contract integration](integration-openapi-contract.md)
- [Initial independent review](review-initial.md)
- [SDK snapshot-reference fix](fix-sdk-snapshot-ref.md)

## Scope

The initial delivery workflow standardized repository-local agent guidance and then exercised the SDK publication contract against the Documentation OpenAPI snapshot. Six focused guidance commits were recorded:

| Repository | Commit | Record |
| --- | --- | --- |
| TerraBase | `5af55dc866e` | engine change evidence guidance |
| TerraBase.Benchmark | `b51822d` | benchmark agent run guidance |
| TerraScale.Deploy | `bcb20cb` | autonomous delivery CLI guardrails |
| TerraScale.DotNet | `48d8a0e` | parallel SDK contract delivery guidance |
| TerraScale.TypeScript | `c55cd75` | SDK agent contract guidance |
| TerraScale.DevHost | `250541e` | autonomous development guidance |

## Validation and push outcome

The workflow exposed the authoritative-snapshot dependency rather than masking it: the TypeScript OpenAPI drift command reported `147/149` coverage. The two missing routes are recorded in the contract integration note. The Deploy correction was committed separately as `bd5ecec` and has a targeted dry-run assertion.

The observed validation and ordinary push outcomes are recorded in [validation evidence](validation-evidence.md). That evidence shows a passed Documentation content-claim command and a protected-branch rejection for the ordinary Documentation push. No secret material is included in these records.
