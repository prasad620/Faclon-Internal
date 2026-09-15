import * as React from 'react';

/**
 * The brand's diagonal light-streak graphic, anchored to a corner of the artboard.
 *
 * Two hard rules from the brand file: `blue` only on blue backgrounds and `dark` only on dark
 * backgrounds; and it is always placed in a CORNER — never centred or along a mid-edge.
 *
 * The parent must be positioned (`position: relative`) and should clip overflow.
 */
export interface DiagonalCornerProps extends React.ImgHTMLAttributes<HTMLImageElement> {
  /** `blue` for the brand-blue ground `--brand-blue` (#1655F2); `dark` for dark grounds
   * (`--neutral-light-1300`, #0C1927). Do not mix. @default 'blue' */
  variant?: 'blue' | 'dark';
  /** Which corner of the artboard it anchors to. @default 'top-right' */
  corner?: 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right';
  /** Width relative to the artboard. @default '55%' */
  width?: string | number;
  /** @default 1 */
  opacity?: number;
  /** Where the graphic files live. @default '/assets/graphics/' */
  basePath?: string;
}

export declare function DiagonalCorner(props: DiagonalCornerProps): JSX.Element;
