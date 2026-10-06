# C# project team-member access guidance

Updated the English, Spanish, and Brazilian Portuguese C# management guides with the public typed `TerraScaleClient.Access` list, add, update, and remove methods.

Contract evidence: TerraScale.DotNet revision `58c9b67f74133c2bce159de4d7196a742b8d6da9`, `TerraScaleProjectAccessClient`. The TypeScript public SDK uses the matching `access` family and team-member terminology.

The guidance requires an owner bearer identity, states that project API keys do not authorize team-member management, and preserves the mutation safety boundary: real automation requires a server-enforced disposable or create-only contract. It documents no generic requests, private Platform APIs, Dashboard shortcuts, direct data access, credentials, or internal endpoints.
