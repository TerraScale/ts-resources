# Expire and rotate application credentials

TerraScale shows each application secret once, stores only a hash, requires explicit project capabilities, and records last use. New keys expire after 90 days by default and at most one year during Public Alpha. Overlapping rotation lets applications replace a key without downtime, while OAuth client credentials support long-running services that rotate automatically.

Dashboard owns application-credential issuance and revocation. Database API
verifies the credential's signed scope and never accepts caller-supplied tenant,
project, or database authority.
