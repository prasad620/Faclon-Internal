# Brand Repository

Everything extracted from the second attached Figma file, **"Brand Repository.fig"**
(pages: Logo, Product-Logo, Companies-Logo, Photographs, Hardware-Photos, HR-Assets,
Vector-Assets, Widgets). No public URL was provided.

| Folder | What's in it |
| --- | --- |
| `icon-data.js` + `Icon.jsx` | 66 Faclon brand and product marks as SVG path data — Faclonlogo and Faclonmono (Black / Blue / White), IOSense, IOConnect, Deepsense, Bruce, Bruce AI, Forge & Foundry, IO Lens, IO Lens Widget, GT, ST (25 device variants), Admin Panel, Dynamic SLD, Map, Device Live Data and Trend, Section Wise Dashboard. Read `Icon.d.ts` for the exact names. |
| `companies/icon-data.js` + `companies/CompanyIcon.jsx` | 51 customer marks as SVG path data, grouped by sector — Automobile, Chemicals, Comm. Infra, Consumer Durables, Consumer Goods, Energy, Metals, OEM, Pharma — plus Ultratech Cement and the Accenture partnership mark. Read `companies/Icon.d.ts`. |
| `companies/png/` | 27 customer marks that exist only as bitmaps. |
| `companies/svg/` | All 50 customer / partner marks as standalone SVG files, exported from `icon-data.js` so each keeps its real brand colours. Filenames match the `CompanyIcon` names (e.g. `MetalsProperty1Tata.svg`). |
| `photographs/` | 20 team and site photographs (PNG, 250 KB – 6.7 MB). |
| `hardware/` | 27 product shots of the ST sensor family, the GT gateway and ST-110. |
| `widgets/` | 16 product-UI screenshots: IO Lens, IO Lens widgets, Admin Panel, Dynamic SLD, Section Wise Dashboard, Reports & Scheduler. |
| `diagrams/` | 29 diagram and illustration vectors: flow view, process view, feature circle, multi-level ring, semi circle, pyramid, staircase, stacked block tower, world map, location pin. *(No Design System card — removed on request; the files remain.)* |
| `hr/` | 18 HR artwork files: employee ID card and birthday/celebration graphics. *(No Design System card — removed on request; the files remain.)* |

## Usage

```jsx
import { Icon } from './assets/brand-repository/Icon.jsx';
<Icon name="FaclonlogoProperty1Blue" size={40} />

import { CompanyIcon } from './assets/brand-repository/companies/CompanyIcon.jsx';
<CompanyIcon name="MetalsProperty1Tata" size={64} />
```

Single-colour marks paint with `currentColor`; recolour via the CSS `color` property.

## Caveats

- **Customer and partner logos are third-party trademarks.** They are stored here because the
  source file is Faclon's own brand repository of customer marks; use them only in the
  contexts their owners permit.
- Some large bitmap fills (>4 MB) were dropped by the vector extractor — those live as PNGs in
  `hardware/` instead. Where a mark exists in both `companies/icon-data.js` and
  `companies/png/`, prefer the vector.
- The ST device variants share generic names (`STProperty152L`, `STProperty1120D`…) taken
  verbatim from the Figma layer names; the file does not label which physical product each is.
- Fonts referenced by the extracted vectors — Outfit, Poppins, Roboto, Noto Sans — are **not**
  bundled. Marks containing live text fall back to a generic sans until those are added.

## Coverage against "Brand Repository.fig"

The file lists **35 component families**. They are asset sets, not UI primitives, so they ship
as SVG path data behind two components rather than 35 separate React files:

| Families | Delivered as |
| --- | --- |
| Faclonlogo, Faclonmono, Bruce, Bruce_AI, Deepsense (×2), Forgeandfoundry, Forge & Foundry, IOConnect, I_O Connect, Iosense, IO_sense, IO_Lens, IO_Lens_Widget, GT, ST, Admin Panel, Map, Dynamic SLD, Device Live Data and Trend, Section Wise Dashboard | `Icon` — 66 named marks in `icon-data.js` |
| Automobile, Chemicals, comminfra, Consumerdurables, ConsumerGoods, Enegrgy, Metals, OEM, Pharma, Vector, Cement/Ultratech, Consumerdurables/Ashirvad, Partnership/Accenture, SHT/30 | `CompanyIcon` — 51 named marks in `companies/icon-data.js` |

Every family is represented **twice over**: once as a name in the shared `Icon` / `CompanyIcon`
lookup, and once as a typed per-family component under `marks/` and `companies/marks/`:

```jsx
<IOSense variant="white" size={40} />        // marks/IOSense.jsx
<Metals variant="tata" size={64} />          // companies/marks/Metals.jsx
```

Prefer the per-family components — the variant names are typed, so an invalid variant is a
compile error rather than a blank render. Reach for `Icon` / `CompanyIcon` when the mark is
chosen at runtime.
