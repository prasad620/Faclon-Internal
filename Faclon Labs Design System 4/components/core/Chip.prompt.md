The marketing chip / badge lockup from the brand file. One component, three configurations:

```jsx
<Chip>Industry 4.0 in a box</Chip>                        {/* squared, uppercase, tracked */}
<Chip shape="pill" shadow>rishi.sharma@faclon.com | +1 (929) 220-3610</Chip>
<Chip shape="pill">rishi.sharma@faclon.com | +1 (929) 220-3610</Chip>
```

- `shape="square"` — 4px radius, uppercase, 2.24px tracking, 24px. The eyebrow-style chip.
- `shape="pill"` — fully rounded, sentence case, 20.19px. The contact badge.
- `shadow` — the 5-layer marketing shadow (`--action-shadow`). Only used on pills in the source.

Colour comes from `--chip-bg` / `--chip-text`, so it flips with the theme: a solid `#40566D` fill with white text in light, a pale `#E3EAF3` fill with dark text in dark.

Distinct from `Badge` in `components/feedback/` — that one is the small product status pill (10–12px text). This is the large marketing lockup.
