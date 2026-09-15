import * as React from 'react';

/** The theme.spacing token table: name, true-size swatch and pixel value per row. */
export interface SpatialTokensProps extends React.HTMLAttributes<HTMLDivElement> {
  /** Override the scale as [name, px] pairs. Defaults to theme.spacing.00–11. */
  scale?: Array<[string, number]>;
}

export declare function SpatialTokens(props: SpatialTokensProps): JSX.Element;
