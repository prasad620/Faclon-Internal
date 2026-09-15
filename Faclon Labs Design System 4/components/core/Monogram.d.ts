import * as React from 'react';

/**
 * The Faclon Labs monogram — the mark without the wordmark. Use for favicons, avatars,
 * app icons and any square or small-scale placement where the full wordmark would not read.
 */
export interface MonogramProps extends Omit<React.ImgHTMLAttributes<HTMLImageElement>, 'style' | 'src' | 'height'> {
  /** 'color' is the blue monogram for light surfaces; 'light' and 'dark' both use the white monogram for brand-blue and dark surfaces. @default 'color' */
  style?: 'color' | 'dark' | 'light';
  /** Rendered height in px. @default 32 */
  size?: number | string;
  /** Path prefix to assets/logo/. Adjust when the page is not at the project root. @default '/assets/logo/' */
  basePath?: string;
  alt?: string;
}

export declare function Monogram(props: MonogramProps): JSX.Element;
