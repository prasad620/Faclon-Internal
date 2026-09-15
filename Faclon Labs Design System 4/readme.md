# Faclon Labs Design System

The design guide and manifest for this project. Everything here was extracted from a single
source: the Figma file **"Marketing style guide.fig"**, mounted as a read-only virtual
filesystem during the build, plus five TASA Orbiter font binaries and two Faclon Labs logo
SVGs supplied directly by the user.

## Context

Faclon Labs is the company this guide belongs to. The attached Figma file is explicitly a
**marketing style guide** — it defines foundations (colour, typography, spacing, elevation,
radius, opacity, border width) and documents one UI component family (`Badge`, with its
companion status light `Indicator`) in full: introduction, anatomy, component props,
variations, usage guidelines and accessibility.

There is no product application, marketing site, or slide template in the source file. Those
surfaces are therefore **not** recreated here — the only interface the file describes is the
style-guide site itself, which is what `ui_kits/style-guide/` reproduces.

### Sources given

| Source | Detail |
| --- | --- |
| Figma (3) | "colours.fig" — the role-assignment views (Light / Dark) that the two "Role colours" cards are transcribed from. No public URL was provided. |
| Figma (2) | "Brand Repository.fig" — pages: Logo, Product-Logo, Companies-Logo, Photographs, Hardware-Photos, HR-Assets, Vector-Assets, Widgets. Extracted into `assets/brand-repository/`. No public URL was provided. |
| Figma (1) | "Marketing style guide.fig" — pages: Cover, Colours, layout, typography, Badges, styles. Scope: 29 frames across Colours / layout / typography / Badges / styles. No public URL was provided. |
| Fonts | `uploads/TASAOrbiter-{Regular,Medium,SemiBold,Bold,ExtraBold}.ttf` → copied to `assets/fonts/` |
| Logos | `uploads/faclon-logo-{blue,white}.svg` → copied to `assets/logo/` |

No codebase or GitHub repo was attached.

---

## Content fundamentals

The guide's own copy is the only writing sample available, and it is consistent:

- **Voice is instructional and impersonal.** Rules are stated as facts about the component,
  not as advice to a person: *"Badges should identify not explain."* — not "You should…".
  Where a reader is addressed it is in the third person: *"it confuses the users."*
- **Sentence case everywhere.** Headings ("Usage Guidelines", "Component Props", "Type Scale",
  "Letter Spacing Tokens") are title-cased; body copy is plain sentence case. No ALL CAPS
  except tiny table column headers inside example UI ("LINK ID", "CUSTOMER").
- **Imperative captions.** Usage examples are labelled with a bare verb phrase, one line, ending
  in a period: *"Use a single badge at a time."* / *"Never make your badge as links."*
- **Do / Don't framing.** Every guideline is a matched pair — a green "Do" and a red "Don't",
  each with an example and a caption. The Don't caption always explains the consequence, not
  just the prohibition: *"Don't use multiple badges at a single place, it confuses the users.
  For such use-cases instead of using multiple badges we should try to assign priorities and
  hierarchies as a first step."*
- **Short declarative product descriptions.** Foundation pages open with one sentence:
  *"Different typefaces available in the system for usage."* /
  *"Properties offered by the component useful for developers"*.
- **Rationale is included, briefly.** Rules come with a because: *"Badges should support the
  content hierarchy, not dominate it."*
- **No emoji. No exclamation marks. No marketing adjectives.** The vibe is a working
  engineering document — dense, tabular, unembellished.
- **Token names are written in dot notation in prose** (`theme.spacing.05`,
  `theme.borderRadius.large`, `theme.elevation.lowRaised`) and always set in Menlo/mono.

---

## Visual foundations

### Colour

**Three** colour systems live in the file and all are shipped. The one to reach for depends on
what you are building:

0. **Marketing palette** (`tokens/palette.css`) — the "Colours" file, Light Theme and Dark.
   It does not just list ramps: it assigns each ramp step to a **role** — Background,
   Containers, Borders, Text, Buttons — and only the steps listed under a role are legal for
   that role. `tokens/palette.css` encodes those sets as `--bg-*`, `--container-*`,
   `--border-*`, `--text-*` and `--button-*`, resolved per theme; the full allowed matrix is
   in `guidelines/colors-roles-light-theme.card.html`.
   This is the brand-facing set and the default for marketing work. Brand blue is
   **azure `#165FF2`**; the ramps are `neutralLight` (000 → 1300), `azure`, `crimson`,
   `emerald` (each 050 → 1000), an accent **`neon-lime` `#68DD68`**, and two brand gradients
   (`106.85° #0D4AC5 → #165FF2` and `75.42° #165FF2 → #16295C`). Each family also carries
   alpha steps — a25 6%, a50 9%, a100 18%, a150 24%, a200 32%. The page organises every ramp
   by role: Background, Containers, Borders, Text, Buttons.

The two product systems below come from the Figma Variables and use a *different* brand blue
(`#305EFF`) — do not mix them with the marketing palette in one surface:

1. **Global palette** — `_global-colors/*`: a blue-grey neutral ramp in light and dark
   variants (`bluegrayLight` / `bluegrayDark`, 0 → 1300) and four chromatic families:
   **azure** (brand blue, `#305EFF`), **emerald** (positive), **crimson** (negative),
   **cider** (notice, orange), **sapphire** (information).
2. **Semantic layer** — `surface/*`, `feedback/*`, `interactive/*`: every UI decision points
   at one of these, and each has a Light and a Dark mode value. `custom/primary`,
   `custom/neutral` and `custom/accent` ramps plus a Tailwind v3 mirror are also present.

**Accent is capped at 10%.** `neon-lime` (`#68DD68`) may occupy **no more than 10% of any
composition**. It is an emphasis colour — a highlight, a marker, a single call-out — never a
background, a large fill, or the dominant colour of a layout. The working split is roughly
60% neutral / 30% brand azure / ≤10% accent.

Rules the file follows without exception:
- **Feedback colour comes in exactly two strengths**: a *subtle* 9% alpha wash of the hue with
  700-weight text of the same hue, and an *intense* solid 600 fill with white text. There is
  no third level.
- **The brand blue is never used as a page background** — only as fill for primary state,
  text links, and icons.
- **Headers and body copy have different default colours.** In the light theme a header is
  `#0C1927` (`--text-heading`) and body copy is `#243547` (`--text-body`); in dark they are
  `#F1F5FA` and `#CBD5E2`. The step between them carries hierarchy before size does.
  Supporting text is `#40566D`, muted/meta `#768EA7`.
- **Neutral text is blue-tinted, never pure grey.**
- **Borders are alpha, not solid**: `rgba(108,132,157,0.18)` is the default hairline; the
  1.5px inset variant (`box-shadow: inset 0 0 0 1.5px …`) is used on specimen tiles instead
  of a real border so it doesn't affect layout.
- **UI cards.** `UI cards.fig` defines 16 card frames — all the same card with different parts
  present, so they ship as one **Card** with `media` / `mediaPosition` / `eyebrow` / `chip` /
  `footer`. Geometry is verbatim (10px radius, 18px padding, 30×30 media, 15px title, 10px
  body); colour comes from the role tokens so it themes. The 30×30 square in the frames is a **placeholder** — it takes an icon, a mark, or a short
  highlight value (a metric, count or keyword), never a literal grey box. Guidance on picking
  a layout is in `Card.prompt.md`. The card keeps a **pale surface in both themes** — `#FFFFFF` light, `#E3EAF3` dark — with a
  1px `--card-border` (`#CBD5E2` / `#B1C1D2`) instead of a shadow. Its ink is therefore
  card-scoped (`--card-heading`, `--card-body`, `--card-eyebrow`, `--card-chip-*`,
  `--card-media`) and stays dark in both themes; the theme text roles must not be used inside
  a Card.
- **Marketing lockups.** `badge.fig` defines a separate, larger family for marketing surfaces:
  a squared uppercase **Chip** (4px radius, 24px, 2.24px tracking), a pill **badge** with and
  without a 5-layer raised shadow, and an **ActionButton** CTA (pill, 20.19px label, trailing
  brand arrow). All three are layout specs only — colour comes from `--chip-*` / `--action-*`
  and flips with the theme: solid `#40566D` with white text in light, pale `#E3EAF3` with dark
  text in dark. Do not confuse these with `Badge` in `components/feedback/`, which is the small
  10–12px product status pill.
- **Two themes, user-selectable.** `ThemeToggle` offers Light / Dark / System, writes the choice
  to `localStorage` and applies it to `document.documentElement`, which flips every role token
  at once. `applyTheme(theme, root?)` and `getStoredTheme()` ship alongside it — call
  `applyTheme(getStoredTheme())` in a blocking `<head>` script to avoid a light flash on load.
  `'system'` resolves against `prefers-color-scheme`. Any subtree can be themed independently
  with `class="dark"`.
- **Dark theme is a first-class scope, not an afterthought.** Every role token resolves under
  `:root[data-theme="dark"]` / `.dark` — background, container, border, text and button. Flip a
  subtree by adding `class="dark"` to any element. Dark raises feedback washes from 9% to 18%
  alpha and drops shadow colour from `rgba(25,40,57,…)` to `rgba(12,25,39,…)`. See the
  "Role colours — dark" and "Dark theme in use" cards.

### Typography

Two faces, **strictly** divided by job — this is a rule, not a preference:

> **TASA Orbiter Display is for headers only. Inter is for body content only.**
> Never set body copy in TASA Orbiter; never set a heading in Inter.

`tokens/typography.css` exposes `--font-heading` and `--font-content` aliases plus
`.fl-display-*` / `.fl-heading-*` (TASA Orbiter) and `.fl-body-*` (Inter) classes so the split
is visible at the usage site.


- **TASA Orbiter Display** — every Display and Heading style. Weights 400 / 500 / 600.
  Tracking −1% at 400 and 500, 0% at 600. *"Default heading font across all the website &
  marketing assets."*
- **Inter** — every Body, Caption and Label style, plus all table and UI chrome.
  Weights 400 / 600 (500 and 700 appear in practice). Tracking 0% everywhere.
- **Menlo** is the de-facto mono for token names and code values (14/20).

**LabelSmall, LabelMedium and CaptionMedium are restricted styles.** They are only ever used
for **eyebrow text and footers** — never body copy, UI labels, table cells or image captions,
which all use Body*. `tokens/typography.css` ships `.fl-eyebrow` (CaptionMedium 11/16),
`.fl-eyebrow-lg` (LabelMedium 12/18), `.fl-eyebrow-sm` (LabelSmall 10/14) and
`.fl-footer` / `.fl-footer-lg` so the restriction is enforceable rather than advisory.

**The wordmark sets a typographic rule.** The lockup is the monogram, then `FACLON` in solid
bold caps, then `LABS` in light caps with wide letter-spacing tucked under it. That wide
spaced-caps treatment is **reserved for eyebrows and overlines** — the small label that sits
above a heading. Never set body copy that way. Use the `.fl-eyebrow` class (or the
`--eyebrow-*` tokens) in `tokens/typography.css`: 11/16, weight 600, `0.18em` tracking,
uppercase.

The scale is fully responsive with two breakpoints, Desktop (≥768px) and Mobile (360–767px);
only Display and Heading styles change, Body/Caption/Label are identical at both. Paragraph
spacing is a first-class token attached to each Body style (12 / 11 / 10 / 8px). List spacing
has only two values: 0 and 8px.

### Space, shape, depth

- **Spacing** is a 12-step named scale, `theme.spacing.00`–`11`: 0, 2, 4, 8, 12, 16, 20, 24,
  32, 40, 48, 56. It is *not* a pure 4px grid — the 2px step is deliberate and used inside
  small components.
- **Radius is capped at 10px.** The scale is `none` 0, `xsmall` 1, `small` 2, `medium` 4,
  `large` 8 and `max` 10 — `max` resolves to 10px, not a full pill. Nothing in this system is rounder than 10px: badges,
  chips, the CTA button and the theme toggle all sit at the cap. Specimen tiles and cards are
  `8px`; tables are square or 4px. There are no 12px or 16px radii.
- **Border width** has four steps including a half-pixel: 0.5, 1, 1.5, 2px. 1.5px is the
  specimen-tile hairline; 2px is the heavy rule under a table header.
- **Elevation** has exactly two levels and both are wide, soft and low-opacity:
  `lowRaised` = `0 2px 16px rgba(25,40,57,0.09)`, `midRaised` = `0 8px 24px rgba(25,40,57,0.12)`.
  Nothing floats higher than that. Cards are shadow **or** border, rarely both.
- **Opacity** is a 13-step token scale (0, 9, 12, 18, 24, 32, 48, 56, 64, 72, 80, 88, 100%);
  the 9 / 12 / 18% steps are what produce all the alpha washes and hairlines.
- **Icon sizes** are 8, 12, 16, 20, 24, 32px, and a badge's icon size is bound to its own size
  token (8 / 12 / 16) rather than chosen freely.

### Surfaces, backgrounds, motion

- **Backgrounds are flat.** White or `#F8FAFC` pages; specimen tiles are `#F5F6F7`. There are
  **no gradients, no photography, no illustration and no texture** anywhere in the source —
  the one decorative element is a faint dotted grid (`.bg-dot-grid`) behind type and colour
  specimens, and it only covers the upper portion of a tile.
- **Cards** = 8px radius + `#F5F6F7` or white fill + a 1.5px inset hairline, or (in real UI
  contexts) a 4px radius + `lowRaised` shadow. Never both a heavy border and a heavy shadow.
- **Transparency and blur**: alpha is used constantly (washes, hairlines), backdrop blur never.
- **Annotation language**: anatomy callouts are 11px *italic* Inter in `#40566D` on a 1px
  **cider orange** leader line ending in a 4px dot. Orange is reserved for annotation and for
  the Notice intent — it is never a UI accent.
- **Motion is not specified in the source.** The tokens shipped in
  `tokens/semantic-colors.css` (`--ease-standard: cubic-bezier(0.5,0,0,1)`, 70 / 150 / 250ms)
  are a **flagged addition** so consumers have a consistent default; treat them as provisional.
- **Hover / press states are not specified either.** The house convention that follows from
  the palette: hover moves a solid fill one step lighter (600 → 500 → 400) or deepens a wash
  from 9% to 12%; press deepens the wash to 18%. No scale or bounce. Confirm with the team
  before relying on this.

---

## Iconography

**The style-guide file contains no reusable icon set** (the Brand Repository file does — see
below). Seven glyph symbols are referenced by name
in the Badges page — `alert-circle`, `check`, `check-circle`, `chevron-right`, `info`, `star`,
`arrow-down-left` — but they are stored as boolean operations with no extractable geometry, so
they could not be copied out. The single vector that did survive is `assets/icons/union.svg`
(the badge's leading-icon glyph).

What this means in practice:

- **There is no icon font and no sprite sheet.** Icons in the source are individual vector
  symbols placed in a fixed-size square (8 / 12 / 16 / 20 / 24 / 32px per the `iconSize` tokens).
- **Substitution (flagged):** for new work, use **[Lucide](https://lucide.dev)** from CDN —
  the closest match to the named set (same 1.5–2px outline style, 24px grid, identical names
  for `alert-circle`, `check-circle`, `chevron-right`, `info`, `star`). Load it with
  `<script src="https://unpkg.com/lucide@latest"></script>` and size it to an `iconSize` token.
  **Please supply the real Faclon icon set if one exists** — this is a substitution, not the
  brand's own iconography.
- **Emoji are never used.** No unicode characters stand in for icons anywhere in the source.
- Icons inherit the text colour of their context: in a subtle badge the icon is the hue's
  700 shade; in an intense badge it is white.
- **The Brand Repository file supplies the real vector library**: 66 Faclon brand/product marks
  and 51 customer marks, all as SVG path data in `assets/brand-repository/`, rendered through
  an `<Icon name="…" size={…} />` wrapper. These are logos and diagram vectors, not a UI icon
  set — the Lucide substitution above still stands for interface glyphs.
- Three third-party product logos (Storybook, Figma, Loom) appear in the guide's page headers.
  They are other companies' marks and are **not** redistributed here — `IconContainer` provides
  the 24px slot they occupied, empty.

---

## Index

### Root
- `styles.css` — the entry point consumers link. `@import` list only.
- `thumbnail.html` — homepage tile.
- `readme.md` — this file.
- `SKILL.md` — Agent Skills wrapper.

### Tokens (`tokens/`)
- `figma/fig-tokens.css` — 1,470 Figma Variables verbatim (Tailwind v3 mirror, `_global-colors`,
  `surface/*`, `feedback/*`, `interactive/*`, Design System Foundations, Components), with
  `:root[data-theme="dark"]` and `:root[data-mode="mobile-360px-767px"]` scopes.
- `figma/fig-typography.css` — generated (empty: the file defines no Figma text styles).
- `fonts.css` — TASA Orbiter Display `@font-face` rules + Inter from Google Fonts.
- `palette.css` — the marketing palette from the Colours page: neutralLight, azure, crimson,
  emerald, neon-lime, alpha steps and the two brand gradients.
- `semantic-colors.css` — brand / surface / text / icon aliases and motion defaults.
- `typography.css` — type scale, responsive breakpoint, weight / tracking / paragraph tokens.
- `spacing.css` — `theme.spacing.00–11` and icon sizes.
- `styles.css` — radius, border width, opacity, elevation.

### Components
| Directory | Components |
| --- | --- |
| `components/feedback/` | **Badge**, **Indicator** |
| `components/core/` | **Card**, **Chip**, **ActionButton**, **ThemeToggle**, **Wordmark**, **Monogram**,  **Spacer**, **SpacerBase**, **SectionDivider**, **FrameHeader**, **Status**, **TextItem**, **TokenRow**, **PropRow**, **UsageMarkers**, **AnatomyMarker**, **BgDotGrid**, **IconContainer**, **Size**, **SpatialTokens**, **VariantProper** |
| `assets/brand-repository/` | **Icon** (all 66 Faclon marks by name) |
| `assets/brand-repository/` (marks) | **Faclonlogo**, **Faclonmono**, **IOSense**, **IOConnect**, **Deepsense**, **Bruce**, **BruceAI**, **Forgeandfoundry**, **ForgeFoundry**, **IOLens**, **IOLensWidget**, **GT**, **ST**, **AdminPanel**, **Map**, **DynamicSLD**, **DeviceLiveDataAndTrend**, **SectionWiseDashboard**, **SHT30** |
| `assets/brand-repository/companies/` | **CompanyIcon** (all 51 customer marks by name) |
| `assets/brand-repository/companies/` (marks) | **Automobile**, **Chemicals**, **Comminfra**, **Consumerdurables**, **ConsumerdurablesAshirvad**, **ConsumerGoods**, **Enegrgy**, **Metals**, **OEM**, **Pharma**, **Vector**, **CementUltratech**, **PartnershipAccenture** |

Each directory has one `@dsCard` HTML showing every state.

**Coverage against the source's 24 component families.** Built: Badge (36 variants),
Indicator (30 variants), Spacer, SpacerBase, `_SectionDivider` → SectionDivider,
`.frame-header` → FrameHeader, `Status`, `.Text Item` → TextItem, `.Token` → TokenRow,
`.prop` → PropRow, `.usage-markers` → UsageMarkers, `.anatomy-marker` → AnatomyMarker,
`.bg-dot-grid` → BgDotGrid, `icon-container` → IconContainer, `Size` → Size,
`_Spatial Tokens` → SpatialTokens.

The source file's logo component (`blade-logo`, ×2) is **deliberately not carried over under
that name.** It belongs to the third-party design system the Figma file was built on. Faclon's
own wordmark ships instead as **Wordmark**, with the same three style variants. A coverage
check will report `blade-logo` as unbuilt — that is intended, not a gap.

`_VariantProper` ships as **VariantProper** — a direction-routing wrapper with no visual style
of its own, matching the source symbol exactly.

**Coverage: 18 components for 24 counted families — every family is represented; nothing is skipped.**
The 6-family gap is duplicate component sets in the Figma file, which the counter lists
separately because each is its own set node:

| Counted separately in the file | Built as |
| --- | --- |
| `Badge` (4 variants), `Badge` (4 variants), `Badge` (36 variants), `Badge/Notice/Medium/False/False/Desktop/Low` | one `Badge` (36 variants: 6 colours × 3 sizes × 2 emphasis) |
| `.frame-header` ×2 (one per page) | one `FrameHeader` |
| the source logo component ×2 | one `Wordmark` |
| `icon-container` ×2 | one `IconContainer` |

18 built + 6 duplicate entries = 24. Collapsing them is correct: a consumer needs one `Badge`,
not four.

**Naming:** `.bg-dot-grid` → `BgDotGrid`, `.usage-markers` → `UsageMarkers` and
`_Spatial Tokens` → `SpatialTokens` are the same components as in the source, PascalCased for
JSX. They are not new inventions.

**Two Figma files, one system — read this before trusting a coverage warning.**
`check_design_system` compares the project against whichever `.fig` is currently mounted. Two
were supplied, so roughly half the components will always look unaccounted for:

| Mounted file | Components it accounts for | Components it flags as "named after nothing in the kit" |
| --- | --- | --- |
| Marketing style guide.fig | Badge, Indicator, Spacer, SpacerBase, SectionDivider, FrameHeader, Status, TextItem, TokenRow, PropRow, UsageMarkers, AnatomyMarker, BgDotGrid, IconContainer, Size, SpatialTokens, VariantProper, Wordmark | Icon, CompanyIcon and the 32 `marks/` components |
| Brand Repository.fig | Icon, CompanyIcon and the 32 `marks/` components | the 18 style-guide components above |

Every component in this system is sourced from one of the two files. Nothing here is invented,
and no rename would satisfy both counters at once.

**Signature graphics.** Three brand elements supplied directly as SVG (`assets/graphics/`),
each with a usage rule that is part of the asset:
- **`SignatureStroke`** (`signature-gradient-stroke.svg`, 483×9) — the hand-drawn gradient
  underline. Goes **directly under a title**, and nowhere else. Not a divider or a rule.
- **`DiagonalCorner`** (`diagonal-blue.svg` / `diagonal-dark.svg`) — the diagonal light streak.
  **Blue on `--brand-blue` (#1655F2) only, dark on dark grounds (#0C1927) only**, and always in a **corner**
  of the artboard — never centred or mid-edge. The component flips the artwork for whichever
  corner you name, so one asset serves all four.
- **`ParticleGraphic`** (`particle-graphic.svg`, 743×763) — dotted particle field. Decorative
  background only; never over text.

**Intentional additions:**
- **`SignatureStroke`, `DiagonalCorner`, `ParticleGraphic`** — wrappers around brand SVGs the
  user supplied directly (not present in any mounted Figma file). Each exists to enforce the
  usage rule that ships with the asset, rather than leaving it to a comment.
- **`Card`** — the 16 source frames are named `Frame 1`…`Frame 15`, so there is no kit name to
  inherit. One component covers all 16 layouts.
- **`ActionButton`** — the source frame labels this lockup "Button with icon" / "CTA + Icon",
  neither of which is a usable component name. `Chip` keeps the file's own layer name.
- **`ThemeToggle`** — no source file defines a theme switcher, but both themes exist in the
  token set, so a control to pick between them is needed for either to be usable.
- **`Monogram`** — neither Figma file contains the monogram. It is built from
  `Blue monogram.svg` and `White monogram.svg`, supplied directly by the user, and mirrors
  `Wordmark`'s variant API so the two marks behave the same way.
- The motion tokens noted above (`--ease-standard`, `--duration-*`), since no source specifies
  motion.

### UI kits
- None. The only interface either source file described was the style-guide site itself, and
  that kit was removed on request. No product application screens exist in the sources, so
  none are invented here.

### Templates
- None.

### Guidelines (`guidelines/`)
18 specimen cards feeding the Design System tab, grouped **Colors**, **Type**, **Spacing**,
**Styles**, **Brand**.

### Assets (`assets/`)
- `logo/faclon-logo-blue.svg`, `logo/faclon-logo-white.svg` — full wordmark
- `logo/faclon-monogram-blue.svg`, `logo/faclon-monogram-white.svg` — monogram, for square
  and small-scale placements
- `fonts/TASAOrbiter-*.ttf` (5 weights)
- `icons/union.svg` — the one vector recoverable from the style-guide .fig
- `brand-repository/` — everything from "Brand Repository.fig". See its own
  [README](assets/brand-repository/README.md). 66 Faclon brand/product marks and 51 customer
  marks as SVG path data, plus `photographs/` (20), `hardware/` (27), `widgets/` (16),
  `diagrams/` (29), `companies/png/` (27), `companies/svg/` (29) and `hr/` (18).

### Product logos
The Brand Repository names Faclon's products: **IOSense**, **IOConnect**, **Deepsense**,
**Bruce** / **Bruce AI**, **Forge & Foundry**, **IO Lens**, plus the **ST** sensor family and
the **GT** gateway on the hardware side. Each ships as a Black and a White (and for the Faclon
wordmark, a Blue) variant in `assets/brand-repository/icon-data.js`.
