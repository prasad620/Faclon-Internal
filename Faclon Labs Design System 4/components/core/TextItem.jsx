import React from 'react';

/** TextItem — heading + body pair used throughout the guide's prose sections. */
export function TextItem({ heading, children, borderLess = true, style, ...rest }) {
  return (
    <div
      {...rest}
      style={{
        display: 'flex', flexDirection: 'column', gap: 4,
        paddingBottom: borderLess ? 0 : 16,
        borderBottom: borderLess ? 'none' : '1px solid var(--surface-line)',
        ...style,
      }}
    >
      {heading ? (
        <span style={{ fontFamily: 'var(--font-display)', fontWeight: 600, fontSize: 'var(--heading-medium-size)', lineHeight: 'var(--heading-medium-line)', color: 'rgb(25,40,57)' }}>{heading}</span>
      ) : null}
      <span style={{ fontFamily: 'var(--font-body)', fontWeight: 400, fontSize: 'var(--body-medium-size)', lineHeight: 'var(--body-medium-line)', color: 'rgb(118,142,167)', whiteSpace: 'pre-line' }}>{children}</span>
    </div>
  );
}
