The primary marketing call-to-action — pill fill, 20.19px label, trailing arrow, and the 5-layer raised shadow.

```jsx
<ActionButton>Book a Demo</ActionButton>
<ActionButton as="a" href="/demo">Book a Demo</ActionButton>
<ActionButton icon={null} shadow={false}>Learn more</ActionButton>
```

- Radius is `252.364px` — effectively a pill, taken verbatim from the source frame.
- The arrow is the real vector from the brand file (`assets/icons/arrow-right.svg`), inlined so its `currentColor` fill follows the label in both themes. No asset path to configure.
- Colour comes from `--action-bg` / `--action-text`, so it flips with the theme. Hover moves the fill to `--action-bg-hover`.
- Use one per view — this is the page's primary action, not a general-purpose button.
