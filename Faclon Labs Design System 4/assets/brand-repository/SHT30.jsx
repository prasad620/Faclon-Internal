import React from 'react';

/**
 * SHT30 — the SHT-30 temperature and humidity sensor.
 * The source component is a photograph, not a vector, so this renders the bitmap.
 */
export function SHT30({ size = 120, basePath = '/assets/brand-repository/hardware/', alt = 'SHT-30 sensor', style, ...rest }) {
  return (
    <img
      {...rest}
      src={basePath + 'sht-30.png'}
      alt={alt}
      style={{ height: size, width: 'auto', display: 'block', objectFit: 'contain', ...style }}
    />
  );
}
