import React from 'react';

const COLS = [
  { key: 'name', width: 200 },
  { key: 'description', width: 320 },
  { key: 'type', width: 160 },
  { key: 'values', width: 200 },
  { key: 'defaultValue', width: 120 },
];

/** PropRow — one row of a component API table. */
export function PropRow({ header = false, name, description, type, values, defaultValue, style, ...rest }) {
  const data = { name, description, type, values, defaultValue };
  return (
    <div
      {...rest}
      style={{
        display: 'flex', alignItems: 'stretch', minHeight: header ? 56 : 52,
        background: header ? 'rgb(241,245,250)' : 'transparent',
        border: '1px solid var(--surface-line)',
        borderBottomWidth: header ? 2 : 1,
        ...style,
      }}
    >
      {COLS.map((c) => (
        <div key={c.key} style={{ width: c.width, flexShrink: 0, boxSizing: 'border-box', display: 'flex', alignItems: 'center', padding: '16px' }}>
          <span style={header
            ? { fontFamily: 'var(--font-body)', fontWeight: 600, fontSize: 16, lineHeight: '24px', color: 'rgb(32,34,35)' }
            : { fontFamily: 'var(--font-mono)', fontWeight: 400, fontSize: 14, lineHeight: '20px', color: c.key === 'name' ? 'rgb(64,86,109)' : 'rgb(118,142,167)' }}>{data[c.key]}</span>
        </div>
      ))}
    </div>
  );
}
