# Use no fixed rate quota for database traffic

Authenticated billable database operations have no fixed requests-per-second quota by plan because TerraScale charges and meters their operation units. Security-sensitive endpoints such as signup, login, password recovery, and payment verification retain their approved abuse throttles. Database requests remain subject to finite protocol, request, query, and machine capacity and may fail as unavailable when the service has exhausted that capacity.

_Amended by [ADR-0041](0041-authenticate-terraScale-accounts-with-email-only.md): the security-sensitive endpoints are signup, login, email verification and sign-in links, token, and payment verification; password recovery no longer exists._
