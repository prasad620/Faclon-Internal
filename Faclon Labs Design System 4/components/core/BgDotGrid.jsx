import React from 'react';

/** BgDotGrid — the faint dotted backdrop behind specimen tiles. */
export function BgDotGrid({ spacing = 16, dotSize = 1, color = 'rgba(108,132,157,0.35)', children, style, ...rest }) {
  return (
    <div
      {...rest}
      style={{
        position: 'relative',
        backgroundImage: 'radial-gradient(' + color + ' ' + dotSize + 'px, transparent ' + dotSize + 'px)',
        backgroundSize: spacing + 'px ' + spacing + 'px',
        ...style,
      }}
    >
      {children}
    </div>
  );
}
