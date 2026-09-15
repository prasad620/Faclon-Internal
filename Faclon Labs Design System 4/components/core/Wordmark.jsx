import React from 'react';

const SRC = {
  color: 'faclon-logo-blue.svg',
  light: 'faclon-logo-white.svg',
  dark:  'faclon-logo-white.svg',
};

/** Wordmark — the full Faclon Labs wordmark, in three styles. */
export function Wordmark({ style: variant = 'color', height = 32, basePath = '/assets/logo/', alt = 'Faclon Labs', style: css, ...rest }) {
  return (
    <img
      {...rest}
      src={basePath + (SRC[variant] || SRC.color)}
      alt={alt}
      style={{ height, width: 'auto', display: 'block', ...css }}
    />
  );
}
