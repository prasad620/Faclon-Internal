The UI card from the brand file. The source defines 16 frames; they are all the same card with different parts present, so this is one component — supply what the content needs.

```jsx
<Card media={<Logo/>} title="Header" subtitle="sub-text comes here"
      body="Lorem ipsum dolor sit amet, consectetur adipiscing elit." />

<Card mediaPosition="trailing" media={<Icon/>} title="Header" subtitle="sub-text comes here" body="…" />

<Card eyebrow="eyebrow text" chip="Chip text comes here" title="Header" body="…" />

<Card title="Header" body="…" footer={<><Indicator intent="positive">Live</Indicator><Chip shape="pill" size="small">v2.4</Chip></>} />
```

**Picking a layout** — match the parts to the content, don't decorate:

- **The 30×30 square is a placeholder, never ship it empty.** In the Figma frames it is drawn as
  a grey square; in real use it holds an icon, a product or company mark, or a short highlight
  value — a metric, a count, a keyword ("98%", "3", "NEW"). If there is nothing to put in it,
  use a no-media layout rather than an empty box.
- **Media leading** — the card is *about* the thing the icon represents (a device, a plant, a product).
- **Media trailing** — the icon is a status or type marker, secondary to the words.
- **No media** — text-only content. Most cards.
- **Eyebrow** — only when the card needs a category above the title, and the title alone is ambiguous.
- **Chip** — a single status or tag. One per card; more than one competes with the title.
- **Footer** — actions or metadata that belong after the body.

Geometry is verbatim from the file: 10px radius, 18px padding, 30×30 media at 4px radius, 15px TASA Orbiter title, 10px Inter body, 14px header-to-body gap (12px once a chip is present).

Colour comes from role tokens — `--container-default` fill, `--text-heading` title, `--text-body` copy, `--container-muted` media slot, `--container-subtle` chip — so the card themes without any extra work. `elevation` is off by default; the source card is flat.

**The card keeps a pale surface in both themes** — `#FFFFFF` on light, `#E3EAF3` on dark — with a 1px `--card-border` (`#CBD5E2` / `#B1C1D2`) instead of a shadow.

Because of that it does **not** follow the theme's text roles. Its ink is card-scoped and stays dark in both themes: `--card-heading` `#0C1927`, `--card-body` `#243547`, `--card-eyebrow`, `--card-chip-bg` / `--card-chip-text`, `--card-media`. Never put `--text-heading` or `--text-body` inside a Card — on dark they are pale and would vanish against the pale fill.
