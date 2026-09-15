import * as React from 'react';

/** Square swatch representing one step of the spacing scale (2, 4, 8, 12, 16, 24px in the source). */
export interface SizeProps extends React.HTMLAttributes<HTMLSpanElement> {
  /** Edge length in px. @default 16 */
  px?: number;
  /** @default 'var(--brand-primary)' */
  color?: string;
  /** Print the pixel value under the swatch. @default false */
  showValue?: boolean;
}

export declare function Size(props: SizeProps): JSX.Element;
