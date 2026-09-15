import * as React from 'react';

/**
 * One row of a two-column token table — monospaced token name and its value.
 */
export interface TokenRowProps extends React.HTMLAttributes<HTMLDivElement> {
  name?: React.ReactNode;
  value?: React.ReactNode;
  /** Render as the table header row (tinted, 16/24 semibold, 2px bottom rule). @default false */
  header?: boolean;
  /** Width of the name column in px. @default 280 */
  nameWidth?: number;
}

export declare function TokenRow(props: TokenRowProps): JSX.Element;
