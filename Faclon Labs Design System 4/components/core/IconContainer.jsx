import React from 'react';

/** IconContainer — 24px padded slot the guide uses for resource-link glyphs. */
export function IconContainer({ children, size = 24, style, ...rest }) {
  return (
    <span
      {...rest}
      style={{
        display: 'inline-flex', alignItems: 'center', justifyContent: 'center', boxSizing: 'border-box',
        width: size, height: size, padding: 8, flexShrink: 0,
        ...style,
      }}
    >
      {children}
    </span>
  );
}
