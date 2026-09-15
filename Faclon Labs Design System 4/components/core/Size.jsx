import React from 'react';

const SIZES = { 2: 2, 4: 4, 8: 8, 12: 12, 16: 16, 24: 24 };

/** Size — a square swatch standing in for one step of the spacing scale. */
export function Size({ px = 16, color = 'var(--brand-primary)', showValue = false, style, ...rest }) {
  const v = SIZES[px] ?? px;
  return (
    <span {...rest} style={{ display: 'inline-flex', flexDirection: 'column', alignItems: 'center', gap: 6, ...style }}>
      <span style={{ width: Math.max(v, 2), height: Math.max(v, 2), background: color, borderRadius: 'var(--border-radius-xsmall)', flexShrink: 0 }} />
      {showValue ? <span style={{ fontFamily: 'var(--font-mono)', fontSize: 10, lineHeight: '14px', color: 'var(--text-muted)' }}>{v}px</span> : null}
    </span>
  );
}
