import * as React from 'react';

export type BadgeColor = 'primary' | 'positive' | 'negative' | 'notice' | 'information' | 'neutral';
export type BadgeSize = 'small' | 'medium' | 'large';
export type BadgeEmphasis = 'subtle' | 'intense';

/**
 * Pill-shaped status label used to identify — never to explain.
 */
export interface BadgeProps extends React.HTMLAttributes<HTMLSpanElement> {
  /** Semantic colour. @default 'neutral' */
  color?: BadgeColor;
  /** @default 'medium' */
  size?: BadgeSize;
  /** 'subtle' = tinted wash + coloured text; 'intense' = solid fill + white text. @default 'subtle' */
  emphasis?: BadgeEmphasis;
  /** Optional leading icon: a node or a component taking { size, color }. */
  icon?: React.ReactNode | React.ComponentType<{ size: number; color: string }>;
  children?: React.ReactNode;
}

export declare function Badge(props: BadgeProps): JSX.Element;
