import React from 'react';
import { TokenRow } from './TokenRow.jsx';
import { Size } from './Size.jsx';

const SCALE = [["00",0],["01",2],["02",4],["03",8],["04",12],["05",16],["06",20],["07",24],["08",32],["09",40],["10",48],["11",56]];

/** SpatialTokens — the theme.spacing token table, each row showing a swatch at true size. */
export function SpatialTokens({ scale = SCALE, style, ...rest }) {
  return (
    <div {...rest} style={style}>
      <TokenRow header name="Token Name" value="Value" />
      {scale.map(([n, v]) => (
        <TokenRow
          key={n}
          name={'theme.spacing.' + n}
          value={<span style={{ display: 'inline-flex', alignItems: 'center', gap: 12 }}><Size px={v} /><span style={{ fontFamily: 'var(--font-mono)', fontSize: 14, lineHeight: '20px' }}>{v}px</span></span>}
        />
      ))}
    </div>
  );
}
