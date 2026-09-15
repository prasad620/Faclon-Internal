import React from 'react';

// Path copied verbatim from assets/icons/arrow-right.svg (brand file vector).
// Inlined so `fill="currentColor"` inherits the label colour in both themes.
const ARROW = 'M 0 6.064 C -0.717 6.064 -1.298 6.645 -1.298 7.362 C -1.298 8.079 -0.717 8.66 0 8.66 L 0 7.362 L 0 6.064 Z M 17.178 7.362 L 18.096 8.28 C 18.603 7.773 18.603 6.951 18.096 6.444 L 17.178 7.362 Z M 10.734 -0.918 C 10.227 -1.425 9.405 -1.425 8.899 -0.918 C 8.392 -0.411 8.392 0.411 8.899 0.918 L 9.816 0 L 10.734 -0.918 Z M 8.899 13.807 C 8.392 14.313 8.392 15.135 8.899 15.642 C 9.405 16.149 10.227 16.149 10.734 15.642 L 9.816 14.724 L 8.899 13.807 Z M 0 7.362 L 0 8.66 L 17.178 8.66 L 17.178 7.362 L 17.178 6.064 L 0 6.064 L 0 7.362 Z M 9.816 0 L 8.899 0.918 L 16.261 8.28 L 17.178 7.362 L 18.096 6.444 L 10.734 -0.918 L 9.816 0 Z M 17.178 7.362 L 16.261 6.444 L 8.899 13.807 L 9.816 14.724 L 10.734 15.642 L 18.096 8.28 L 17.178 7.362 Z';

/** ActionButton — the marketing CTA: pill fill, label, trailing arrow, raised shadow. */
export function ActionButton({ icon = 'arrow', shadow = true, as: Tag = 'button', style, children, ...rest }) {
  return (
    <Tag
      {...rest}
      style={{
        display: 'inline-flex', alignItems: 'center', justifyContent: 'center', boxSizing: 'border-box',
        gap: 25.236406326293945,
        padding: '10.095px 20.189px',
        border: 0,
        borderRadius: 'var(--border-radius-max)',
        background: 'var(--action-bg)',
        color: 'var(--action-text)',
        fontFamily: 'var(--font-body)',
        fontWeight: 500,
        fontSize: 20.189125061035156,
        lineHeight: '100%',
        whiteSpace: 'nowrap',
        cursor: 'pointer',
        boxShadow: shadow ? 'var(--action-shadow)' : 'none',
        textDecoration: 'none',
        transition: 'background var(--duration-gentle) var(--ease-standard)',
        ...style,
      }}
    >
      <span>{children}</span>
      {icon ? (
        <span style={{ display: 'inline-flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, color: 'inherit' }}>
          {icon === 'arrow' ? (
            <svg width="17.178" height="14.724" viewBox="0 0 17.178 14.724" fill="none" aria-hidden="true" style={{ display: 'block', overflow: 'visible' }}>
              <path d={ARROW} fill="currentColor" fillRule="nonzero" />
            </svg>
          ) : icon}
        </span>
      ) : null}
    </Tag>
  );
}
