import React from 'react';

const KEY = 'faclon-theme';

function resolve(t) {
  if (t === 'light' || t === 'dark') return t;
  return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}

/** Applies a theme to a root element by setting data-theme and the .dark class. */
export function applyTheme(theme, root) {
  const el = root || document.documentElement;
  const resolved = resolve(theme);
  el.setAttribute('data-theme', resolved);
  el.classList.toggle('dark', resolved === 'dark');
  return resolved;
}

/** Reads the stored preference ('light' | 'dark' | 'system'). */
export function getStoredTheme() {
  try { return localStorage.getItem(KEY) || 'system'; } catch (e) { return 'system'; }
}

/**
 * ThemeToggle — segmented control that lets the user pick Light, Dark or System.
 * Writes the choice to localStorage and applies it to the document root.
 */
export function ThemeToggle({ options = ['light', 'dark', 'system'], value, onChange, root, persist = true, style, ...rest }) {
  const [internal, setInternal] = React.useState(() => (value ?? getStoredTheme()));
  const active = value ?? internal;

  React.useEffect(() => { applyTheme(active, root); }, [active, root]);

  function pick(next) {
    if (persist) { try { localStorage.setItem(KEY, next); } catch (e) { /* storage unavailable */ } }
    if (value == null) setInternal(next);
    if (onChange) onChange(next);
  }

  const LABEL = { light: 'Light', dark: 'Dark', system: 'System' };

  return (
    <div
      {...rest}
      role="radiogroup"
      aria-label="Colour theme"
      style={{
        display: 'inline-flex', gap: 2, padding: 2,
        background: 'var(--button-neutral-bg)',
        borderRadius: 'var(--border-radius-max)',
        ...style,
      }}
    >
      {options.map((opt) => {
        const on = active === opt;
        return (
          <button
            key={opt}
            type="button"
            role="radio"
            aria-checked={on}
            onClick={() => pick(opt)}
            style={{
              appearance: 'none', border: 0, cursor: 'pointer',
              height: 26, padding: '0 12px',
              borderRadius: 'var(--border-radius-max)',
              fontFamily: 'var(--font-body)',
              fontSize: 'var(--label-medium-size)', lineHeight: 'var(--label-medium-line)',
              fontWeight: on ? 600 : 400,
              background: on ? 'var(--container-default)' : 'transparent',
              color: on ? 'var(--text-heading)' : 'var(--text-secondary)',
              boxShadow: on ? 'var(--shadow-low-raised)' : 'none',
              transition: 'background var(--duration-gentle) var(--ease-standard), color var(--duration-gentle) var(--ease-standard)',
            }}
          >
            {LABEL[opt] || opt}
          </button>
        );
      })}
    </div>
  );
}
