import * as React from 'react';

/**
 * The SHT-30 temperature and humidity sensor. Photographic, not vector — the source
 * component in the Figma file is a bitmap fill with no extractable geometry.
 */
export interface SHT30Props extends Omit<React.ImgHTMLAttributes<HTMLImageElement>, 'src' | 'height'> {
  /** Rendered height in px. @default 120 */
  size?: number | string;
  /** Path prefix to assets/brand-repository/hardware/. @default '/assets/brand-repository/hardware/' */
  basePath?: string;
  alt?: string;
}

export declare function SHT30(props: SHT30Props): JSX.Element;
