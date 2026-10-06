# Local development through the DevHost Tailscale routes

This workspace (`terrascale-dev`) is a **remote development machine**. The
primary local stack is the DevHost-managed GRU/SFO/FRA RF=1 lab
(`terrascale-devhost.service`), which owns every fixed Tailscale Serve route.
`TerraScale.DevHost` is the only long-running local supervisor. Internals does not
contain a Dashboard composition host.

## Canonical surface (DevHost lab)

`systemctl --user start terrascale-devhost.service` starts the complete local
customer path: the GRU/SFO/FRA graph, Dashboard-owned Better Auth, the one
full-stack Dashboard, the independent Database API, TerraBase, monitoring,
and export. DevHost installs fixed tailnet HTTPS routes
at startup and reconciles them continuously, so these URLs never drift:

| Service       | URL                                              | Local target           |
|---------------|--------------------------------------------------|------------------------|
| DevHost panel | `https://terrascale-dev.tail057f.ts.net:18443`   | `127.0.0.1:5180`       |
| Better Auth, Dashboard-owned | `https://terrascale-dev.tail057f.ts.net:18445` | `127.0.0.1:18670` |
| **Dashboard** | `https://terrascale-dev.tail057f.ts.net:18446`   | `127.0.0.1:18672`      |
| Landing       | `https://terrascale-dev.tail057f.ts.net:18447`   | `127.0.0.1:3002`       |
| Documentation | `https://terrascale-dev.tail057f.ts.net:18448`   | `127.0.0.1:3003`       |
| TerraBase operations, private development only | `https://terrascale-dev.tail057f.ts.net:18449` | Orchestrator-published |

The new `TerraScale.Database` route is a required gap. It needs a fixed
tailnet port and loopback target recorded atomically in DevHost, Orchestrator,
SDK integration tests, root instructions, and this table. Until the owner
confirms the proposed `18444` and `18673` reservation and a runtime collision
check passes, do not invent a floating or temporary customer API URL.

**Canonical product Dashboard rule.**
`https://terrascale-dev.tail057f.ts.net:18446/` is the workspace's canonical
product Dashboard URL and it must work correctly whenever the lab is converged:
opening it serves the TerraScale Dashboard (an unauthenticated request
redirects to `/login`, which must return HTTP 200). A 502 is acceptable only
inside the convergence window after a service (re)start or Orchestrator
re-attestation; leaving this URL broken outside that window is a release
blocker. Verify it after every service action and before handing off any
change that touches DevHost, Orchestrator, Better Auth, Database API, or Dashboard
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

## Dashboard development

For HMR work, run the Dashboard app from the sibling checkout while DevHost is
running. The app is one Vinext workload, so its route handlers and TypeScript
backend modules use the app's local URL. The SDK uses the fixed Database API
route once DevHost admits it:

```bash
cd ../TerraScale.Dashboard
vp run vinext:dev
```

## Verify

Canonical DevHost surface (the rule):

```bash
curl -skL -o /dev/null -w '%{http_code}\n' https://terrascale-dev.tail057f.ts.net:18446/   # expect 200
```

## Restart

```bash
systemctl --user restart terrascale-devhost.service
curl -skL -o /dev/null -w '%{http_code}\n' https://terrascale-dev.tail057f.ts.net:18446/   # expect 200
```

DevHost owns and reasserts the fixed routes. Do not run a second supervisor or
repoint the `18443`–`18449` ports. After a restart, wait for convergence and
recheck the canonical Dashboard URL. A temporary 502 is expected only during
that convergence window.
