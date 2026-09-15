import * as React from 'react';

/**
 * Faint dotted backdrop used behind type and colour specimens.
 */
export interface DotGridProps extends React.HTMLAttributes<HTMLDivElement> {
  /** Grid pitch in px. @default 16 */
  spacing?: number;
  /** Dot radius in px. @default 1 */
  dotSize?: number;
  /** @default 'rgba(108,132,157,0.35)' */
  color?: string;
  children?: React.ReactNode;
}

export declare function BgDotGrid(props: DotGridProps): JSX.Element;
