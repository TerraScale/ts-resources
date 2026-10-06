# Use explicit project capabilities

Project access uses a closed capability set for database reads, writes,
queries, schemas, backups, usage, and administration. Dashboard issues grants
for those named scopes. Application credentials receive explicit project and
database scopes and never inherit a human role or ownership authority.

Database API rejects an unknown scope and binds the verified grant to the
tenant, project, database, principal, and operation before calling TerraBase.
