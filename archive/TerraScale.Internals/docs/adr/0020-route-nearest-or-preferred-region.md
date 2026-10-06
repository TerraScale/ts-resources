# Route globally and expose strict regional endpoints

`api.terrascale.tech` routes customer traffic to the nearest healthy region selected by the project. SDKs and requests may name a preferred region and fail over to another selected region when it is unavailable, unless strict affinity is requested. Each region also has a strict `{region}.api.terrascale.tech` endpoint, such as `gru.api.terrascale.tech`, which returns an availability error rather than silently serving from a different region.
