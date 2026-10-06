# TerraScale Development Certificates

AppHost uses a TerraScale-owned local development certificate for Internals and other ASP.NET project resources.

## Generated Files

AppHost generates certificate material under:

```text
src/Hosting/TerraScale.AppHost/.data/certs/
```

Files:

- `terrascale-development-root-ca.crt`: local root CA to register on your computer.
- `terrascale-development-root-ca.key`: root CA private key; do not install or share.
- `terrascale-internals-development.crt`: server certificate used by Kestrel.
- `terrascale-internals-development.key`: server private key used by Kestrel.

The `.data/` directory is ignored. Do not commit generated certificate material.

## Hostnames

The default certificate covers:

- `localhost`
- `terrascale-internals.localhost`
- `terrascale-dashboard.localhost`
- `terrascale-apphost.localhost`
- `terrascale-dev.localhost`

AppHost also adds `TERRASCALE_PUBLIC_HOSTNAME` and `TERRASCALE_ALTERNATE_PUBLIC_HOSTNAME` to the certificate when they are set.

## Register The Root CA

Start AppHost once so the certificate files exist. Then trust only the root CA file on your local computer.

Linux with p11-kit:

```bash
sudo trust anchor src/Hosting/TerraScale.AppHost/.data/certs/terrascale-development-root-ca.crt
```

Debian or Ubuntu without p11-kit:

```bash
sudo cp src/Hosting/TerraScale.AppHost/.data/certs/terrascale-development-root-ca.crt \
  /usr/local/share/ca-certificates/terrascale-development-root-ca.crt
sudo update-ca-certificates
```

macOS:

```bash
sudo security add-trusted-cert -d -r trustRoot \
  -k /Library/Keychains/System.keychain \
  src/Hosting/TerraScale.AppHost/.data/certs/terrascale-development-root-ca.crt
```

Windows PowerShell:

```powershell
Import-Certificate `
  -FilePath src\Hosting\TerraScale.AppHost\.data\certs\terrascale-development-root-ca.crt `
  -CertStoreLocation Cert:\CurrentUser\Root
```

## AppHost Usage

AppHost injects the generated server certificate into ASP.NET project processes with:

```text
TerraScale__Kestrel__CertificatePath
TerraScale__Kestrel__CertificateKeyPath
```

Auth/Platform project processes use the generated HTTPS certificate when HTTPS is enabled.
Dashboard Next is a Node/Vinext process and currently uses the AppHost-provided Dashboard
HTTP URL unless HTTPS is explicitly added to the Node runtime. If your browser or local
tools still report trust errors for ASP.NET service HTTPS URLs, re-register the root CA and
restart the process that is making the request.

AppHost resource endpoints must use Aspire-managed randomized ports. Do not pin fixed host ports in AppHost code, tests, launch settings, or documentation; consume the URLs and connection strings printed or exposed by Aspire at runtime. See `docs/AppHost.md`.

To regenerate everything, stop AppHost and delete:

```text
src/Hosting/TerraScale.AppHost/.data/certs/
```
