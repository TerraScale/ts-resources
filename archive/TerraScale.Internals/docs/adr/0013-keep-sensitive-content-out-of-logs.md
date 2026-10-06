# Keep customer content and secrets out of logs

TerraScale does not log document bodies, secrets, authorization headers, payment data, or raw query parameters by default. It records identifiers, sizes, status, timing, and redacted error categories. Temporary content diagnostics require the same scoped, audited, expiring break-glass access used for customer-document support.
