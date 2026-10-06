# Use no fixed rate quota for database traffic

Authenticated billable database operations have no fixed requests-per-second
quota by plan because TerraScale meters their operation units. Database API
still enforces finite protocol, request, query, concurrency, and machine
limits. It returns a typed overload or unavailable outcome when those bounds
are exhausted.

Dashboard applies separate abuse throttles to Better Auth signup, login,
recovery, email verification, factor, provider, passkey, token, and credential
operations.
