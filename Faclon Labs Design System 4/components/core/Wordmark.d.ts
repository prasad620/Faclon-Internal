import * as React from 'react';

/**
 * The full Faclon Labs wordmark — monogram plus FACLON / LABS type.
 * Pair with `Monogram` when only the mark is needed.
 */
export interface WordmarkProps extends Omit<React.ImgHTMLAttributes<HTMLImageElement>, 'style' | 'src'> {
  /** 'color' is the blue mark for light surfaces; 'light' and 'dark' both use the white mark — on brand blue and on dark surfaces respectively. @default 'color' */
  style?: 'color' | 'dark' | 'light';
  /** Rendered height in px. @default 32 */
  height?: number;
  /** Path prefix to assets/logo/. Adjust when the page is not at the project root. @default '/assets/logo/' */
  basePath?: string;
  alt?: string;
}

export declare function Wordmark(props: WordmarkProps): JSX.Element;
