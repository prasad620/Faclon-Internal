import * as React from 'react';

/**
 * The marketing chip / badge lockup. `shape="square"` is the uppercase tracked chip;
 * `shape="pill"` is the contact badge, with `shadow` for the raised variant.
 */
export interface ChipProps extends React.HTMLAttributes<HTMLSpanElement> {
  /** 'square' = 4px radius chip; 'pill' = fully rounded badge. @default 'square' */
  shape?: 'square' | 'pill';
  /** Uppercase + 2.24px tracking. Defaults to true for square, false for pill. */
  uppercase?: boolean;
  /** Raised variant — applies the 5-layer marketing shadow. @default false */
  shadow?: boolean;
  /** @default 'large' */
  size?: 'large' | 'small';
  children?: React.ReactNode;
}

export declare function Chip(props: ChipProps): JSX.Element;
