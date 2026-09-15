import * as React from 'react';

export type IOLensVariant = "dashboardOuput" | "dashboardOuput2" | "processOverviewDashboard";

/** The IOLens mark from the Faclon brand repository, 3 variants. */
export interface IOLensProps extends React.SVGProps<SVGSVGElement> {
  /** @default "dashboardOuput" */
  variant?: IOLensVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function IOLens(props: IOLensProps): JSX.Element;
