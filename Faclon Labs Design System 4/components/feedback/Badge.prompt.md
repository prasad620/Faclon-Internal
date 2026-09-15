Pill status label that identifies a single concept at a glance — use it for state ("Active", "Refunded"), never for explanatory or promotional copy.

```jsx
<Badge color="positive" size="medium" emphasis="subtle">Paid</Badge>
<Badge color="negative" emphasis="intense" size="large">Failed</Badge>
```

- `color`: primary | positive | negative | notice | information | neutral
- `size`: small (16px, 10/14 text) | medium (20px, 12/18) | large (24px, 12/18)
- `emphasis`: subtle (9% wash + coloured text, weight 500) | intense (solid fill + white text, weight 400)
- Radius is `--border-radius-max`, which is capped at 10px in this system — a soft rounded rectangle, not a full pill. Leading icon sizes 8 / 12 / 16px.
- Usage rules from the source guide: one badge at a time; inside tables prefer `Indicator`; never make a badge a link.
