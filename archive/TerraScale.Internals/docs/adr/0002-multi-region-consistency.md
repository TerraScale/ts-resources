# Prefer regional availability and eventual convergence

TerraScale allows every selected region to accept customer document writes during a WAN partition. Regions replicate asynchronously and converge after connectivity returns, using TerraBase's last-write-wins behavior or an explicitly configured collection conflict script. TerraScale chooses regional availability over immediate global consistency, so public contracts must describe replication lag and conflict behavior and must not promise zero-latency convergence, global linearizability, or automatic read-your-writes across regions.
