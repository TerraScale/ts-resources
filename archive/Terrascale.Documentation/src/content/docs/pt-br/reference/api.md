---
title: API
description: Information about TerraScale Platform APIs.
order: 1000
---

TerraScale exposes versioned `/api/v1` JSON HTTP APIs.

## Base URL

```text
https://api.terrascale.tech
```

## Authentication

Bearer tokens:

```http
Authorization: Bearer eyJhbGciOi...
```

Project API keys:

```http
X-TerraScale-Auth-Key: tsauth_...
X-TerraScale-Project-Id: 01J2K7RTEQC3F4NG9HZ8Y62P6A
```

## Current Data Routes

| Area | Route family |
| --- | --- |
| Databases | `/api/v1/databases` |
| Repositories | `/api/v1/repositories` |
| Documents | `/api/v1/repositories/{repositoryId}/documents` |
| TQL | `/api/v1/repositories/{repositoryId}/tql` |
| Project auth | `/api/v1/projects/{projectId}/auth/...` |

## Next Steps

- [API Overview](/reference/api/)
- [Authentication](/reference/authentication/)
- [Error Handling](/reference/error-handling/)
- [Rate Limits](/reference/rate-limits/)
