# Qualify every advertised public client

TerraScale qualifies each advertised client against the exact API release candidate and the workflows that client actually exposes. The public API, TypeScript SDK, .NET SDK, and MCP share the customer journey for resource, Document, consistency, billing, export, credential, membership, and role-protected administration workflows where the typed public contract exposes them. MCP uses a user-bound access key with selected Organization, Project, and operation scopes and must qualify the same live authorization, tenant-isolation, confirmation, Audit, and secret-handling behavior as the corresponding public operation.

If a client misses the evidence gate for an exposed workflow, TerraScale removes that operation's launch claim instead of publishing an unqualified capability. A missing MCP gate blocks the affected operation rather than forcing every otherwise-qualified MCP tool into a read-only product boundary.
