import React from 'react';

/**
 * SignatureStroke — the brand's hand-drawn gradient underline.
 * Sits directly under a title. Scales to the width of its container.
 */
export function SignatureStroke({
  width = 483,
  basePath = '/assets/graphics/',
  style,
  ...rest
}) {
  return (
    <img
      {...rest}
      src={basePath + 'signature-gradient-stroke.svg'}
      alt=""
      aria-hidden="true"
      style={{ display: 'block', width, height: 'auto', maxWidth: '100%', pointerEvents: 'none', userSelect: 'none', ...style }}
    />
  );
}
