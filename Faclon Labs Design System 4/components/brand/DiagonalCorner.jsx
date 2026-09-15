import React from 'react';

const SRC = {
  blue: 'diagonal-blue.svg',
  dark: 'diagonal-dark.svg',
};

/**
 * DiagonalCorner — the brand's diagonal light-streak graphic.
 *
 * Two rules from the brand file, both enforced here:
 *   1. `blue` goes on blue backgrounds ONLY; `dark` on dark backgrounds ONLY.
 *   2. It sits in a CORNER of the artboard — never centred, never mid-edge.
 *
 * The parent must be `position: relative` (or otherwise positioned) and clip overflow.
 */
export function DiagonalCorner({
  variant = 'blue',
  corner = 'top-right',
  width = '55%',
  opacity = 1,
  basePath = '/assets/graphics/',
  style,
  ...rest
}) {
  const [v, h] = corner.split('-'); // top|bottom , left|right
  const flipX = h === 'left';
  const flipY = v === 'bottom';

  return (
    <img
      {...rest}
      src={basePath + SRC[variant]}
      alt=""
      aria-hidden="true"
      style={{
        position: 'absolute',
        [v]: 0,
        [h]: 0,
        width,
        height: 'auto',
        opacity,
        pointerEvents: 'none',
        userSelect: 'none',
        transform: `scale(${flipX ? -1 : 1}, ${flipY ? -1 : 1})`,
        transformOrigin: 'center',
        ...style,
      }}
    />
  );
}
