import React from 'react';

/**
 * ParticleGraphic — the brand's dotted particle-field graphic.
 * Decorative background element; sits behind or beside content, never over text.
 */
export function ParticleGraphic({
  width = 743,
  opacity = 1,
  basePath = '/assets/graphics/',
  style,
  ...rest
}) {
  return (
    <img
      {...rest}
      src={basePath + 'particle-graphic.svg'}
      alt=""
      aria-hidden="true"
      style={{ display: 'block', width, height: 'auto', opacity, pointerEvents: 'none', userSelect: 'none', ...style }}
    />
  );
}
