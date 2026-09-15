The Faclon Labs monogram — the mark on its own, without the wordmark. Use for favicons, avatars, app icons, and any square or small-scale placement where the full wordmark would not read.

```jsx
<Monogram style="color" size={32} basePath="../../assets/logo/" />
<Monogram style="dark" size={48} />
```

- `color` — blue monogram, for light surfaces
- `light` / `dark` — white monogram, for brand blue and any dark surface

Same light/dark rule as `Wordmark`: blue on light, white on everything darker. Set `basePath` to the relative route to `assets/logo/` from your page. Never recolour or redraw the mark — only the two supplied SVGs are legitimate.
