import * as React from 'react';

/**
 * Do / Don't / Caution heading that labels a usage example in the guide.
 */
export interface UsageMarkerProps extends React.HTMLAttributes<HTMLDivElement> {
  /** @default 'do' */
  type?: 'do' | 'dont' | 'caution';
  /** Override the label text. */
  children?: React.ReactNode;
}

export declare function UsageMarkers(props: UsageMarkerProps): JSX.Element;
