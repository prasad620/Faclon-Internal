import React from 'react';

/** TokenRow — one row of a token table: monospaced name plus value. */
export function TokenRow({ name, value, header = false, nameWidth = 280, style, ...rest }) {
  const cell = {
    display: 'flex', alignItems: 'center', boxSizing: 'border-box',
    padding: '16px', gap: 8, alignSelf: 'stretch',
  };
  const text = header
    ? { fontFamily: 'var(--font-body)', fontWeight: 600, fontSize: 16, lineHeight: '24px', color: 'rgb(32,34,35)' }
    : { fontFamily: 'var(--font-mono)', fontWeight: 400, fontSize: 14, lineHeight: '20px' };
  return (
    <div
      {...rest}
      style={{
        display: 'flex', alignItems: 'center', minHeight: header ? 56 : 52,
        background: header ? 'var(--interactive-background-gray-default)' : 'transparent',
        border: '1px solid ' + (header ? 'var(--surface-line)' : 'rgb(225,227,229)'),
        borderBottomWidth: header ? 2 : 1,
        ...style,
      }}
    >
      <div style={{ ...cell, width: nameWidth, flexShrink: 0 }}>
        <span style={{ ...text, color: header ? 'rgb(32,34,35)' : 'rgb(64,86,109)' }}>{name}</span>
      </div>
      <div style={{ ...cell, flex: 1 }}>
        <span style={{ ...text, color: header ? 'rgb(32,34,35)' : 'rgb(118,142,167)' }}>{value}</span>
      </div>
    </div>
  );
}
