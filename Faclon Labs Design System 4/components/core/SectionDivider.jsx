import React from 'react';

/** SectionDivider — horizontal rule between documentation or content sections. */
export function SectionDivider({ weight = 'thick', style, ...rest }) {
  const h = weight === 'thin' ? 'var(--border-width-thin)' : 'var(--border-width-thicker)';
  return <hr {...rest} style={{ border: 0, height: h, width: '100%', background: 'var(--surface-line)', margin: 0, ...style }} />;
}
