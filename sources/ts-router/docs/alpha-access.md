# Alpha access from mariogk-dev

Use the existing operator SSH key on `mariogk-dev`. This server does not need
Bitwarden, `bw`, an SSH agent, an unlock session, or a newly generated key.
The operator confirmed `ssh alpha` works from a normal terminal on 2026-09-30.

The existing `~/.ssh/config` contains:

```sshconfig
Host alpha
    HostName alpha
    User mariogk
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
    IdentityAgent none
```

Keep the existing key and known-host entries. Do not replace a working key,
copy it into this repository, print it, or disable host-key verification.
The configuration, private key and known-hosts file were all mode `0600`.

## Commands to use

From the operator's normal terminal:

```sh
ssh alpha
```

For agent and noninteractive operations, load the same user configuration
explicitly. This avoids the system SSH include's ownership check inside a
user-mapped Nix sandbox while retaining the configured key and known hosts:

```sh
ssh -F "$HOME/.ssh/config" \
  -o BatchMode=yes -o StrictHostKeyChecking=yes -o ConnectTimeout=10 \
  alpha hostname
```

This command should print `alpha`. Start with a read-only probe before any
deployment. Alpha's HomeLab deployer owns router deployments; ts-router CI
publishes the image and holds no deployment credential.

## An agent session also needs network access

An SSH configuration cannot grant permissions withheld by the agent launcher.
The failing session used `workspace-write` with network access disabled and
approval policy `never`. It could not even create an IPv4 or IPv6 socket.
The socket error occurred before DNS, connection establishment or SSH
authentication, so neither a different key nor an SSH agent could fix it.

Launch a new operational session from the working terminal with network
access explicitly enabled and HomeLab included in its writable workspace:

```sh
codex --no-daemon \
  --cd /home/mariogk/Projects/TerraScale \
  --add-dir /home/mariogk/Projects/HomeLab \
  --sandbox workspace-write \
  --config sandbox_workspace_write.network_access=true
```

This retains workspace filesystem restrictions and does not stop an existing
daemon or active session. For a GUI or app-server client, select the equivalent
network-enabled workspace permissions when creating the operational session;
the client can override user configuration. Organization or host restrictions
still take precedence. Do not attempt to change an active session's sandbox
from inside it.

The command flags and `sandbox_workspace_write.network_access` setting were
checked against installed Codex CLI `0.159.2` help and its generated
`ConfigReadResponse` schema. That schema defaults network access to `false`.
The official documentation endpoint was unreachable from the failing session;
live SSH from a newly launched operational session remains a required check.

## Diagnose the layer that failed

First test socket creation without contacting any server or reading a key:

```sh
python3 - <<'PY'
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM):
    print("IPv4 socket creation is allowed")
PY
```

| Failure | Meaning and action |
| --- | --- |
| `socket: Operation not permitted` | The execution sandbox or host policy blocks networking. Use an authorized operational session; changing SSH credentials cannot help. |
| `Bad owner or permissions on /nix/store/.../20-systemd-ssh-proxy.conf` | The user namespace presents the system-owned include as an unmapped owner. Use `-F "$HOME/.ssh/config"`; do not chmod or edit the immutable Nix store. |
| `Could not resolve hostname alpha` | Check socket permissions first. If allowed, check Tailscale/MagicDNS in that execution environment. A numeric address cannot overcome denied sockets. |
| `Permission denied (publickey)` | Networking reached SSH authentication. Inspect the configured identity and the remote authorized key; preserve the current key until there is evidence it is wrong. |
| `Host key verification failed` | Verify the server identity through the existing trusted inventory before updating known hosts. Keep strict host-key checking enabled. |

Inspect effective identity settings without showing any secret values:

```sh
ssh -G -F "$HOME/.ssh/config" alpha |
  rg '^(hostname|user|identityfile|identityagent|identitiesonly|stricthostkeychecking|userknownhostsfile) '
```

The failing sandbox had only one UID mapping and presented the system include
as UID/GID `65534:65534`, despite its read-only `0444` mode. `NoNewPrivs: 1`
and `Seccomp: 2` were also present. The decisive network evidence was the
standalone socket-creation failure, not the mere presence of seccomp.

## Server configuration and verification

HomeLab owns the server package list and its operator helpers. The
`mariogk-dev` declaration must exclude `bitwarden-cli` from its ordinary CLI
packages and reject future inclusion in `environment.systemPackages`. Other
hosts' credential systems are outside this server-specific change. Shared
SSH helpers must use the user's configured identity without requiring
Bitwarden or running `ssh-add` as a prerequisite.

Apply the reviewed HomeLab source changes through its normal Nix workflow;
deleting `/run/current-system/sw/bin/bw` or a Nix-store path is not a durable
package removal. A production activation can interrupt active work, so follow
the development VM runbook before activating a new generation.

After activation, verify that `bw` is absent from the active system profile,
plain `ssh alpha` still works from the operator terminal, and the explicit
user-config probe works from the network-enabled agent session. Only then
resume deployed-router inspection and the live
[Jev/Luna/Sol comparison](../bench/README.md). Keep Bao credentials in their
existing secret delivery path; never print secret files during diagnosis.
