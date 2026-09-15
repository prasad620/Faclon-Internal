import React from 'react';

const TYPES = {
  do:      { label: 'Do',      color: 'rgb(0,134,89)',   glyph: 'M3.5 8.5l3 3 6-6' },
  dont:    { label: "Don't",   color: 'rgb(217,45,32)',  glyph: 'M4 4l8 8M12 4l-8 8' },
  caution: { label: 'Caution', color: 'rgb(233,105,12)', glyph: 'M8 4v5M8 11.5v.5' },
};

/** UsageMarkers — the Do / Don't / Caution heading above a usage example. */
export function UsageMarkers({ type = 'do', children, style, ...rest }) {
  const t = TYPES[type] || TYPES.do;
  return (
    <div {...rest} style={{ display: 'flex', alignItems: 'center', gap: 8, height: 32, ...style }}>
      <span style={{ width: 20, height: 20, borderRadius: '50%', background: t.color, display: 'inline-flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
        <svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="#fff" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d={t.glyph} /></svg>
      </span>
      <span style={{ fontFamily: 'var(--font-display)', fontWeight: 600, fontSize: 'var(--heading-large-size)', lineHeight: 'var(--heading-large-line)', color: t.color }}>{children || t.label}</span>
    </div>
  );
}
