import * as React from 'react';

export type SpacerSize = '00' | '01' | '02' | '03' | '04' | '05' | '06' | '07' | '08' | '09' | '10' | '11';

/** Fixed gap from the theme.spacing scale (0, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 56px). */
export interface SpacerProps extends React.HTMLAttributes<HTMLSpanElement> {
  /** @default '05' */
  size?: SpacerSize;
  /** @default 'vertical' */
  direction?: 'vertical' | 'horizontal';
  /** Fill the cross axis. @default false */
  stretch?: boolean;
}

export declare function Spacer(props: SpacerProps): JSX.Element;
