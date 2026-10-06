# Route globally and expose strict regional endpoints

> Amended on 2026-08-29. Placement is selected per database, subject to Project
> and residency policy. Routing may use only that database's selected active
> Regions. The final public origin and path routing await owner confirmation.

`api.terrascale.tech` routes customer traffic to the nearest healthy region selected by the project. SDKs and requests may name a preferred region and fail over to another selected region when it is unavailable, unless strict affinity is requested. Each region also has a strict `{region}.api.terrascale.tech` endpoint, such as `gru.api.terrascale.tech`, which returns an availability error rather than silently serving from a different region.
