import React from 'react';

const ORANGE = 'rgb(233,105,12)';

/** AnatomyMarker — italic caption on a leader line pointing at part of a component. */
export function AnatomyMarker({ label = 'name', direction = 'top', length = 40, style, ...rest }) {
  const vertical = direction === 'top' || direction === 'bottom';
  const text = (
    <span style={{ fontFamily: 'var(--font-body)', fontWeight: 500, fontStyle: 'italic', fontSize: 11, lineHeight: '16px', textAlign: 'center', color: 'rgb(64,86,109)', whiteSpace: 'nowrap' }}>{label}</span>
  );
  const line = <span style={{ background: ORANGE, width: vertical ? 1 : length, height: vertical ? length : 1, flexShrink: 0 }} />;
  const dot = <span style={{ width: 4, height: 4, borderRadius: '50%', background: ORANGE, flexShrink: 0 }} />;
  const reverse = direction === 'bottom' || direction === 'right';
  return (
    <span {...rest} style={{ display: 'inline-flex', flexDirection: vertical ? 'column' : 'row', alignItems: 'center', gap: 4, ...style }}>
      {reverse ? <>{dot}{line}{text}</> : <>{text}{line}{dot}</>}
    </span>
  );
}
