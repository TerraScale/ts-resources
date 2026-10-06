# Use expand-and-contract data migrations

TerraScale makes data-model changes in stages. New code first reads old and new shapes, then writes the new shape, then migrates existing data, and removes old-shape support only in a later qualified release. Destructive one-release migrations are rejected so a server rollback remains compatible with stored data.
