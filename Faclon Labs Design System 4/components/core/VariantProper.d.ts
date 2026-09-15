import * as React from 'react';

/**
 * Direction-routing wrapper from the source kit (`_VariantProper`). It carries no visual style
 * of its own — it only propagates a horizontal/vertical axis to the documentation symbols inside.
 */
export interface VariantProperProps extends React.HTMLAttributes<HTMLDivElement> {
  /** @default 'horizontal' */
  direction?: 'horizontal' | 'vertical';
  /** Gap between children in px. @default 8 */
  gap?: number;
  children?: React.ReactNode;
}

export declare function VariantProper(props: VariantProperProps): JSX.Element;
