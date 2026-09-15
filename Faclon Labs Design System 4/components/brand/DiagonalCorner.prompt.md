The brand's diagonal light-streak graphic, anchored to a corner of the artboard.

```jsx
<div style={{ position: 'relative', overflow: 'hidden', background: 'var(--brand-blue)' }}>
  <DiagonalCorner variant="blue" corner="top-right" basePath="../../assets/graphics/" />
  …content…
</div>
```

**Two hard rules, both from the brand file:**

1. **`blue` on `--brand-blue` (#1655F2) only; `dark` on dark grounds (`--neutral-light-1300`, #0C1927) only.** They are not interchangeable — the streak is tuned to its ground, and the wrong pairing reads as a dirty smear.
2. **Corners only.** Top-left, top-right, bottom-left, bottom-right. Never centred, never along a mid-edge, never floating in open space.

The component flips the artwork automatically for whichever corner you name, so one asset serves all four. The parent must be `position: relative` and should clip overflow.

One per artboard is the norm; two opposite corners is the most it should ever carry.
