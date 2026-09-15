import * as React from 'react';

export type IndicatorIntent = 'positive' | 'negative' | 'notice' | 'information' | 'neutral';
export type IndicatorSize = 'small' | 'medium' | 'large';

/**
 * Status light — a coloured dot plus a neutral label. Preferred over Badge inside dense tables.
 */
export interface IndicatorProps extends React.HTMLAttributes<HTMLSpanElement> {
  /** @default 'neutral' */
  intent?: IndicatorIntent;
  /** @default 'small' */
  size?: IndicatorSize;
  /** @default true */
  showLabel?: boolean;
  children?: React.ReactNode;
}

export declare function Indicator(props: IndicatorProps): JSX.Element;
