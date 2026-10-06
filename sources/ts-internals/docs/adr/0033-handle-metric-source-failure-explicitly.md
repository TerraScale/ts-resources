# Handle metric-source failure explicitly

TerraScale validates metric units and sources, rejects malformed values, and alerts operators when collection fails. The Customer Dashboard keeps panels with valid data visible and marks a failed panel unavailable with its last successful observation. It never displays a guessed or silently stale value as current.
