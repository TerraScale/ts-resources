# Keep API v1 backward-compatible

Database API keeps `/api/v1` clients working through compatible additions.
Breaking public-contract changes require a new API major, a documented support
window, migration guidance, and matching `@terrascale/sdk` support. Public API
versioning does not imply compatibility with an old private engine protocol or
storage format.
