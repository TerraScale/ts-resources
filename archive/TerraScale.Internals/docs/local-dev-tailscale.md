# Local Dev: DevHost lab + Remote Access via Tailscale

This workspace (`terrascale-dev`) is a **remote development machine**. The
primary local stack is the DevHost-managed GRU/SFO/FRA RF=1 lab
(`terrascale-devhost.service`), which owns every fixed Tailscale Serve route.
`TerraScale.AppHost` (Aspire orchestration) remains the product-local
composition host for focused, standalone work.

## Canonical surface (DevHost lab)

`systemctl --user start terrascale-devhost.service` starts the complete local
customer path: the GRU/SFO/FRA graph, Authentication, Dashboard, Platform,
TerraBase, monitoring, and export. DevHost installs fixed tailnet HTTPS routes
at startup and reconciles them continuously, so these URLs never drift:

| Service       | URL                                              | Local target           |
|---------------|--------------------------------------------------|------------------------|
| DevHost panel | `https://terrascale-dev.tail057f.ts.net:18443`   | `127.0.0.1:5180`       |
| Platform      | `https://terrascale-dev.tail057f.ts.net:18444`   | Orchestrator-published |
| Authentication| `https://terrascale-dev.tail057f.ts.net:18445`   | `127.0.0.1:18670`      |
| **Dashboard** | `https://terrascale-dev.tail057f.ts.net:18446`   | `127.0.0.1:18672`      |
| Landing       | `https://terrascale-dev.tail057f.ts.net:18447`   | `127.0.0.1:3002`       |
| Documentation | `https://terrascale-dev.tail057f.ts.net:18448`   | `127.0.0.1:3003`       |
| TerraBase     | `https://terrascale-dev.tail057f.ts.net:18449`   | Orchestrator-published |

**Canonical product Dashboard rule.**
`https://terrascale-dev.tail057f.ts.net:18446/` is the workspace's canonical
product Dashboard URL and it must work correctly whenever the lab is converged:
opening it serves the TerraScale Dashboard (an unauthenticated request
redirects to `/login`, which must return HTTP 200). A 502 is acceptable only
inside the convergence window after a service (re)start or Orchestrator
re-attestation; leaving this URL broken outside that window is a release
blocker. Verify it after every service action and before handing off any
change that touches DevHost, Orchestrator, Authentication, or Dashboard
contracts. A scheduled check verifies this URL every 30 minutes and reports or
recovers failures.

```bash
curl -skL -o /dev/null -w '%{http_code}\n' https://terrascale-dev.tail057f.ts.net:18446/   # expect 200
```

Manage and inspect the lab only through the service — never launch `devhost up`
or the executables directly:

```bash
systemctl --user status terrascale-devhost.service
journalctl --user -u terrascale-devhost.service -f
```

## Standalone AppHost workflow (secondary)

For focused work outside the DevHost lab, `TerraScale.AppHost` starts the real
local backends — TerraBase, `TerraScale.Authentication`, `TerraScale.Platform`,
NATS, and Dashboard Next — on Aspire-managed randomized ports, and injects the
local Platform/Auth base URLs into Dashboard Next (`TERRASCALE_API_BASE_URL`,
`TERRASCALE_AUTH_API_BASE_URL`). Payment testing uses configured Polar sandbox
or Stripe test credentials through the same Platform adapters as production;
AppHost does not start a payment emulator.

For HMR work, run Dashboard Next standalone only after AppHost is running and
explicitly set `TERRASCALE_API_BASE_URL` / `TERRASCALE_AUTH_API_BASE_URL` to
the local AppHost URLs. Never point Dashboard Next dev work at production
`api.terrascale.tech` / `auth.terrascale.tech`.

From the TerraScale.Internals repo root:

```bash
dotnet build -m src/Hosting/TerraScale.AppHost/TerraScale.AppHost.csproj
dotnet run  --project src/Hosting/TerraScale.AppHost/TerraScale.AppHost.csproj --no-build
```

AppHost prints the live URLs, for example:

```
TerraBase:       http://127.0.0.1:43221/
Authentication: http://127.0.0.1:41207/
Platform:       http://127.0.0.1:43833/
Dashboard:      http://127.0.0.1:41251/
```

Ports are randomized every run — read them from this output each time.

For Dashboard HMR against the same local backend:

```bash
cd ../TerraScale.Dashboard
TERRASCALE_API_BASE_URL=http://127.0.0.1:<API-port> \
TERRASCALE_AUTH_API_BASE_URL=http://127.0.0.1:<Auth-port> \
vp run vinext:dev
```

## Expose the standalone workflow over Tailscale (tailnet-only)

All services bind to `127.0.0.1` only. The fixed ports `18443`–`18449` belong
to the DevHost lab — do not repoint them at AppHost. When running the
standalone AppHost workflow, expose it on separate one-off ports and tear them
down when done, so the canonical DevHost surface stays intact:

```bash
# One-time: let `tailscale serve` run without sudo
sudo tailscale set --operator="$USER"

# Point each serve port at the AppHost port printed above
tailscale serve --bg --https=8443 http://127.0.0.1:<Dashboard-port>
tailscale serve --bg --https=8444 http://127.0.0.1:<API-port>
tailscale serve --bg --https=8445 http://127.0.0.1:<Auth-port>
tailscale serve --bg --https=8446 http://127.0.0.1:<TerraBase-port>
```

Open these from any device on your tailnet:

| Service   | URL                                                  |
|-----------|------------------------------------------------------|
| Dashboard | `https://terrascale-dev.tail057f.ts.net:8443`           |
| API       | `https://terrascale-dev.tail057f.ts.net:8444`           |
| Auth      | `https://terrascale-dev.tail057f.ts.net:8445`           |
| TerraBase | `https://terrascale-dev.tail057f.ts.net:8446`           |

The Dashboard makes server-side calls to the local Platform/Auth, so opening the
Dashboard URL exercises the full local stack end to end (login, data, etc.).

## Verify

Canonical DevHost surface (the rule):

```bash
curl -skL -o /dev/null -w '%{http_code}\n' https://terrascale-dev.tail057f.ts.net:18446/   # expect 200
```

Standalone AppHost workflow:

```bash
TS_IP=100.76.242.91; H=terrascale-dev.tail057f.ts.net
curl -s --resolve "$H:8443:$TS_IP" -o /dev/null -w '%{http_code}\n' "https://$H:8443/api/health"   # expect 200
curl -s --resolve "$H:8443:$TS_IP" -o /dev/null -w '%{http_code}\n' "https://$H:8443/login"         # expect 200
curl -s --resolve "$H:8444:$TS_IP" -o /dev/null -w '%{http_code}\n' "https://$H:8444/health/ready"  # expect 200
curl -s --resolve "$H:8445:$TS_IP" -o /dev/null -w '%{http_code}\n' "https://$H:8445/health/ready"  # expect 200
curl -s --resolve "$H:8446:$TS_IP" -o /dev/null -w '%{http_code}\n' "https://$H:8446/databases"     # expect 200
```

The `--resolve` flag pins the tailnet IP explicitly; MagicDNS on this box
resolves the name as well, but the pin keeps the check independent of local
resolver state.

## Teardown / restart

```bash
tailscale serve --https=8443 off   # repeat for 8444/8445/8446 (one-off AppHost routes only)
systemctl --user restart terrascale-devhost.service   # the canonical lab
```

AppHost ports are randomized, so after each AppHost restart, re-point the
one-off `serve` targets at the new ports (or run `tailscale serve status` to
see current mappings). The fixed DevHost routes never need re-pointing; the
service reconciles them itself. After any DevHost service action, re-verify
the canonical Dashboard URL and expect it to return to HTTP 200 once the lab
re-converges.
