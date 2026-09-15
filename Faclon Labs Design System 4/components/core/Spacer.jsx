import React from 'react';

const SCALE = { '00': 0, '01': 2, '02': 4, '03': 8, '04': 12, '05': 16, '06': 20, '07': 24, '08': 32, '09': 40, '10': 48, '11': 56 };

/** Spacer — inserts a fixed gap from the theme.spacing scale. */
export function Spacer({ size = '05', direction = 'vertical', stretch = false, style, ...rest }) {
  const px = SCALE[size] ?? Number(size) ?? 0;
  const vertical = direction === 'vertical';
  return (
    <span
      {...rest}
      aria-hidden="true"
      style={{
        display: 'block', flexShrink: 0,
        width: vertical ? (stretch ? '100%' : 1) : px,
        height: vertical ? px : (stretch ? '100%' : 1),
        ...style,
      }}
    />
  );
}
