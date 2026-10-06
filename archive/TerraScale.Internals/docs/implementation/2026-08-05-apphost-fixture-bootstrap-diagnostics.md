# AppHost fixture bootstrap diagnostics

The shared real AppHost fixture wraps each bounded startup phase in one sanitized final diagnostic containing only the fixed phase, failed state, dependency class, and failure category. It intentionally excludes addresses, exception text, credentials, tokens, and payloads. The deterministic helper test injects a failing phase without creating an AppHost topology; no live-stack validation is implied.
