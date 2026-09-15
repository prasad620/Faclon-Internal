import React from 'react';

const SCALE = { '00': 0, '01': 2, '02': 4, '03': 8, '04': 12, '05': 16, '06': 20, '07': 24, '08': 32, '09': 40, '10': 48, '11': 56 };

/** SpacerBase — the raw sized box Spacer is built on; renders a visible swatch when `visualise` is set. */
export function SpacerBase({ spacer = '05', visualise = false, color = 'rgba(48,94,255,0.18)', style, ...rest }) {
  const px = SCALE[spacer] ?? Number(spacer) ?? 0;
  return (
    <span
      {...rest}
      aria-hidden="true"
      style={{
        display: 'inline-block', flexShrink: 0,
        width: px || 1, height: px || 1,
        background: visualise ? color : 'transparent',
        ...style,
      }}
    />
  );
}
