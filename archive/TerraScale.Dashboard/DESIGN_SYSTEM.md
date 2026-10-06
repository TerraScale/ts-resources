# TerraScale Design System — v1

Source of truth for all TerraScale frontend design. This copy governs the
**Dashboard** (`TerraScale.Dashboard.Next`). Sibling copies with the same
"Shared Core" section live in `Terrascale.Landingpage/docs/DESIGN_SYSTEM.md`
and `Terrascale.Documentation/DESIGN_SYSTEM.md` — when the Shared Core
changes, update all three together and bump the version.

The token values live in `app/globals.css` (`BEGIN/END TerraScale shared core
tokens v1` block). Never hardcode a color, font, spacing, or radius that a
token already expresses.

---

## Part 1 — Shared Core (identical across Dashboard, Landing, Docs)

### Principles

1. **Quiet neutral base, one loud accent.** Everything is grey/white/black
   except: the accent blue on interactive elements that must draw attention,
   and status colors that convey real state. If a screen has blue in more than
   ~3 places, something is over-accented.
2. **Dark is the default theme.** The dark canvas is a really dark gray
   (#0E0F14), never pure black. Dashboard also ships light; Landing/Docs are
   dark-only.
3. **Glass over flat.** Panels, cards, and sticky chrome are translucent with
   a 20px backdrop blur, sitting on a faint blue ambient glow. Depth comes
   from borders + surface steps first; shadows reinforce, never decorate.
4. **Mono for data.** Every ULID, connection string, query, version, metric,
   and tabular number renders in JetBrains Mono (`font-mono`), with
   `tabular-nums` where digits align.
5. **Mobile-friendly is mandatory.** Sidebars collapse to drawers, stat grids
   collapse 4→2→1, tables scroll horizontally in their own container, touch
   targets ≥ 40px. Content areas are full-width — no max-width caps on app
   surfaces.
6. **No keyboard-shortcut hints in UI.** Do not render shortcut badges or
   platform-specific hints (⌘K etc.) anywhere.

### Typography

| Role                 | Font                                  | Notes                                                                    |
| -------------------- | ------------------------------------- | ------------------------------------------------------------------------ |
| UI / headings / body | **Oxanium** (variable 200–800)        | Self-hosted latin woff2. **No italic exists — never use italic styles.** |
| Data / code / IDs    | **JetBrains Mono** (variable 100–800) | Self-hosted latin woff2. First in the `font-mono` stack.                 |

Type scale: 12px meta/badges · 14px UI default/tables · 16px body ·
18px/600 panel titles · 22px/700 page titles · 28px/700 section heroes ·
36px/700 marketing (landing only). Weights: use 500/600 for UI emphasis;
reserve 700+ for titles.

### Color

Neutral ramp (the only greys):

```
0 #FFFFFF · 50 #F7F8FA · 100 #F2F3F5 · 200 #E7E9EE · 300 #D3D7DF
400 #8B93A4 · 600 #687083 · 800 #333846 · 900 #1F222B · 950 #16181F · 1000 #0E0F14
```

Semantic surfaces (theme-flipped): `canvas` (page) · `surface` (panels) ·
`surface-muted` (hovers, wells, secondary buttons) · `ink` / `ink-muted`
(text) · `line` (borders).

Accent — the ONLY non-neutral interactive color:

| Token                | Light   | Dark    | Use                                                                                   |
| -------------------- | ------- | ------- | ------------------------------------------------------------------------------------- |
| `--ts-accent`        | #2563EB | #3B82F6 | primary buttons, active nav, focus rings, selection                                   |
| `--ts-accent-strong` | #1D4ED8 | #2563EB | hover / pressed                                                                       |
| `--ts-accent-soft`   | #60A5FA | #60A5FA | **dark-mode links & blue text** (saturated blue text fails contrast on dark — ~2.9:1) |

Allowed blue: primary CTAs (max one per view region), links, focus rings,
active nav/selection. Banned blue: backgrounds at scale, decorative icons,
headings, badges that don't mean "selected".

Status — state only, never decorative, always paired with an icon or label:

| Token          | Light    | Dark          | Meaning              |
| -------------- | -------- | ------------- | -------------------- |
| `--ts-success` | #15803D  | #34D399       | healthy, completed   |
| `--ts-warning` | #B45309  | #FBBF24       | degraded, limits     |
| `--ts-danger`  | #DC2626  | #F87171       | error, destructive   |
| `--ts-info`    | = accent | = accent-soft | notices, in-progress |

Permitted status forms: inline text, tinted badge, tinted alert, and (danger
only) a solid confirm button. Destructive actions are quiet (tinted outline)
until the final confirm step.

Charts: `--ts-chart-1` #2563EB and `--ts-chart-2` #0891B2 (CVD-validated on
white and #16181F). Max two series per chart — more folds into "Other" or
splits into small multiples. Extra ordinal steps use greys (chart-3..5).
Status colors appear in charts only when encoding actual state. Text on
charts always wears ink tokens, never series colors.

Glass: `--ts-glass-bg` (panels/cards/sidebar) and `--ts-glass-strong`
(sticky chrome, dialogs, mobile drawers) with `--ts-blur: 20px`. Apply via
the `.ts-glass` / `.ts-glass-strong` utility classes; pair with a `line`
border. The ambient glow behind them is defined once on `body::before` —
sections never paint their own decorative backgrounds.

### Spacing, radius, shadow

8pt grid with a 4px half-step: 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64.
Usage: 4–8 inside controls · 12–16 between related elements · 24 between
panels/sections · 32–64 page sections (landing/docs use the airy end).

Anatomy constants: buttons/inputs 36px tall (30px small), button x-padding
16px (12px small); badges 22px tall, x-padding 8px; table cells 12×16px,
compact rows ≈ 40px; label→input 4px, field→field 16px, fields→actions 24px.

Radius: 6px badges/chips · 8px buttons/inputs (`rounded-lg`) · 12px
panels/cards (`rounded-xl`) · pill for round elements. Two shadows only:
`--ts-shadow-panel` and `--ts-shadow-overlay` (dialogs/popovers).

### Accessibility

- White on #2563EB: 5.2:1 ✓ · #2563EB on white: 5.2:1 ✓ · white on #3B82F6:
  3.7:1 (UI/large ✓) · **#2563EB text on dark fails — use `--ts-accent-soft`.**
- Focus is always visible: 2px accent outline, 2px offset.
- Status is never color-alone: pair with pip/icon/label.
- Respect `prefers-reduced-motion`; transitions 120–260ms ease-out.

---

## Part 2 — Dashboard specifics

### Token architecture (`app/globals.css`)

- `--ts-*` shared core on `:root`, dark overrides on `:root[data-theme="dark"]`.
- TerraScale utilities (`bg-canvas`, `text-ink`, `border-line`, …) map through
  `@theme inline` to the core. Token names are stable.
- shadcn tokens (`--background`, `--primary`, …) are pure `var()` references
  into the core — there is no separate `.dark` literal block. `--primary` IS
  the accent blue: `variant="primary"` buttons are the attention-drawing CTAs.
- Theme flip invariant: `app/layout.tsx` sets BOTH `data-theme` (token values)
  and the `.dark` class (`dark:` utilities) atomically. Never change one
  without the other.

### Components

- Use the existing shadcn/ui components in `src/components/ui/` and the
  TerraScale wrappers (`Panel`, `DataTable`, `EmptyState`, `FormField`,
  `IconButton`, `ChartShell`). Do not invent parallel primitives.
- Button variants (compat `Button` maps `primary→default`, `danger→destructive`;
  its default is `secondary`): `primary` = blue CTA (max one visible per view
  region), `secondary`/`outline`/`ghost` = neutral workhorses, `destructive` =
  quiet tinted red, solid red only on the final confirm.
- Cards/panels and the sidebar are `ts-glass`; sticky header and mobile drawer
  are `ts-glass-strong`. Tables stay inside glass panels with `overflow-x-auto`.
- Charts use `--ts-chart-1/2` via the chart shell; grids/axis text muted mono
  10–11px; 2px lines; direct labels at line ends; hover crosshair + tooltip.
- Existing AGENTS.md rules still apply: compact operational surfaces, no
  marketing heroes, no badges on titles, stable dimensions for repeated UI,
  `lucide-react` icons (use `KeyRound`, not `Key`, for API keys).

### Density & layout

Dashboard sits at the dense end of the spacing scale: compact rows, 16px gaps
between sibling panels, 24px between sections, full-width main content
(`px-5 md:px-8`). Sidebar 288px, items 40–42px tall with 18px icons.

### Fonts on this app

`public/fonts/oxanium-latin-wght-normal.woff2` and
`public/fonts/jetbrains-mono-latin-wght-normal.woff2` (OFL licenses alongside).
Quantico is removed — do not reintroduce it.
