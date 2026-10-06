# Support session read-your-writes

TerraScale returns a session consistency token after writes. SDKs send it on later reads and briefly wait for the selected region to catch up or route to a selected region that has observed the write. Callers may opt into stale reads when lower latency matters more. This does not change the local acknowledgement contract for writes.
