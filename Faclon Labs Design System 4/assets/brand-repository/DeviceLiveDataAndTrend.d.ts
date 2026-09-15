import * as React from 'react';

export type DeviceLiveDataAndTrendVariant = "1" | "2" | "3";

/** The DeviceLiveDataAndTrend mark from the Faclon brand repository, 3 variants. */
export interface DeviceLiveDataAndTrendProps extends React.SVGProps<SVGSVGElement> {
  /** @default "1" */
  variant?: DeviceLiveDataAndTrendVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function DeviceLiveDataAndTrend(props: DeviceLiveDataAndTrendProps): JSX.Element;
