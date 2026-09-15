import * as React from 'react';

export type SpacerBaseStep = '00' | '01' | '02' | '03' | '04' | '05' | '06' | '07' | '08' | '09' | '10' | '11';

/**
 * The raw square box behind `Spacer` — one step of theme.spacing, 12 steps in all.
 * Use `Spacer` in layouts; use this directly only when documenting the scale.
 */
export interface SpacerBaseProps extends React.HTMLAttributes<HTMLSpanElement> {
  /** @default '05' */
  spacer?: SpacerBaseStep;
  /** Tint the box so the step is visible in a specimen. @default false */
  visualise?: boolean;
  /** @default 'rgba(48,94,255,0.18)' */
  color?: string;
}

export declare function SpacerBase(props: SpacerBaseProps): JSX.Element;
