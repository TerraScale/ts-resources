# Implementation: public SDK guidance

## Delivered commits

Documentation delivery commits: `50c1666`, `08c932c`, `e120ba8`, and `2750d97`. The external SDK revision used as evidence is `faa471f`.

## Improvements

- All public `client.request` samples were replaced with named TypeScript SDK methods.
- Required `toUlid` imports were added.
- The landing-page example was corrected.
- Content-validator coverage was added.

## Guidance retained

Public SDK documentation should use the current exported typed surface and public contracts. Dashboard-specific workflows remain composed at the Dashboard boundary and must not create private shortcuts, generic SDK requests, or undocumented public behavior.

This documentation increment records SDK-facing corrections. It does not close OpenAPI or SDK contract debt across the product.
