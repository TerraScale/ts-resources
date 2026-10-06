---
status: superseded by ADR-0040
---

# Make Customer onboarding a durable gate

TerraScale persists Customer onboarding as a server-enforced gate. Self-registering Users complete User, Payment, Organization, and Project; invited Users complete User and Invitation. A step advances only after the server confirms its durable result, and completion is historical rather than a representation of current access, ownership, or billing state.
