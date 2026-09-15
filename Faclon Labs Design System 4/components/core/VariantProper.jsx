import React from 'react';

/** VariantProper — the kit's direction-routing wrapper: lays children out along one axis. */
export function VariantProper({ direction = 'horizontal', gap = 8, children, style, ...rest }) {
  return (
    <div
      {...rest}
      style={{
        display: 'flex',
        flexDirection: direction === 'vertical' ? 'column' : 'row',
        alignItems: direction === 'vertical' ? 'flex-start' : 'center',
        gap,
        ...style,
      }}
    >
      {children}
    </div>
  );
}
