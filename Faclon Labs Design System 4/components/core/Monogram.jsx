import React from 'react';

const SRC = {
  color: 'faclon-monogram-blue.svg',
  light: 'faclon-monogram-white.svg',
  dark:  'faclon-monogram-white.svg',
};

/** Monogram — the Faclon Labs mark on its own, for square and small-scale placements. */
export function Monogram({ style: variant = 'color', size = 32, basePath = '/assets/logo/', alt = 'Faclon Labs', style: css, ...rest }) {
  return (
    <img
      {...rest}
      src={basePath + (SRC[variant] || SRC.color)}
      alt={alt}
      style={{ height: size, width: 'auto', display: 'block', ...css }}
    />
  );
}
