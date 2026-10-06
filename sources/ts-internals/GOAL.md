# ts-internals goal

## Authority

The [workspace goal](../GOAL.md) is the sole authority for ts-internals.

## Mission

The public **Database API gateway** (`TerraScale.Database`). Sole
customer-facing process that speaks TBEP to terrabase. REST `/api/v1` +
reactive WebSocket (MessagePack, D-14). Also home of the `terrascale` CLI.

## Verification

```bash
gofmt -l .            # must print nothing
go vet ./...
go build ./...
go test ./...
go test -race ./...
```
