# Support conditional document mutations

Public document APIs accept an optional change token for updates and deletes. If the stored version has changed, TerraScale returns a conflict without charging an operation unit. Blind writes remain available and retain the documented last-write-wins behavior across regions.
