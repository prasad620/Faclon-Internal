import React from 'react';

const INTENTS = {
  positive:    'rgb(0,162,81)',
  negative:    'rgb(217,45,32)',
  notice:      'rgb(233,105,12)',
  information: 'rgb(18,145,208)',
  neutral:     'rgb(108,132,157)',
};

const SIZES = {
  small:  { height: 16, dot: 6,  gap: 4, fontSize: 12, lineHeight: '18px' },
  medium: { height: 20, dot: 8,  gap: 4, fontSize: 12, lineHeight: '18px' },
  large:  { height: 20, dot: 10, gap: 4, fontSize: 12, lineHeight: '18px' },
};

/** Indicator — status light: a coloured dot with an optional neutral label. */
export function Indicator({ intent = 'neutral', size = 'small', showLabel = true, children, style, ...rest }) {
  const s = SIZES[size] || SIZES.small;
  return (
    <span {...rest} style={{ display: 'inline-flex', alignItems: 'center', height: s.height, gap: s.gap, ...style }}>
      <span style={{ width: s.dot, height: s.dot, borderRadius: '50%', background: INTENTS[intent] || INTENTS.neutral, flexShrink: 0 }} />
      {showLabel ? (
        <span style={{ fontFamily: 'var(--font-body)', fontSize: s.fontSize, lineHeight: s.lineHeight, fontWeight: 500, color: 'var(--text-subtle)', whiteSpace: 'nowrap' }}>{children}</span>
      ) : null}
    </span>
  );
}
