Lets the user pick Light, Dark or System. Drop it in a header or settings row — it applies the choice to `document.documentElement`, which flips every role token at once, and remembers it across reloads.

```jsx
<ThemeToggle />
<ThemeToggle options={['light','dark']} />
```

Controlled, if the app already owns theme state:

```jsx
<ThemeToggle value={theme} onChange={setTheme} persist={false} />
```

Theming a subtree instead of the whole page — pass a `root`, or just add the class yourself:

```jsx
<div className="dark"> … </div>
```

Two helpers ship alongside it:

- `applyTheme(theme, root?)` — sets `data-theme` and toggles `.dark`; resolves `'system'` against `prefers-color-scheme`. Call this on first paint to avoid a flash.
- `getStoredTheme()` — reads the saved preference, defaulting to `'system'`.

To prevent a light flash before React mounts, run `applyTheme(getStoredTheme())` in a blocking script in `<head>`.
