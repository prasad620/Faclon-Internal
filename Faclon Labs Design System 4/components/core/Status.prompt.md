26px capsule, 12/18 Inter, 9% tinted fill with a 1px inset hairline of the same hue. Mirrors the kit's 4-variant status badge set.

```jsx
<Status variant="published" />
<Status variant="version">v2.0</Status>
<Status variant="documentation" />
```

Exact values from the source: Published `rgba(0,162,81,0.09)` / `rgb(0,108,54)`;
Version Number `rgba(33,75,222,0.09)` / `rgb(23,44,120)`. Foundation and Documentation use the
neutral tint of the same pattern — the source renders those two as breadcrumb text rather than
capsules, so their capsule colours are inferred.
