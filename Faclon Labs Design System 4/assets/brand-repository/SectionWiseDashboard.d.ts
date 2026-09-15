import * as React from 'react';

export type SectionWiseDashboardVariant = "1" | "2";

/** The SectionWiseDashboard mark from the Faclon brand repository, 2 variants. */
export interface SectionWiseDashboardProps extends React.SVGProps<SVGSVGElement> {
  /** @default "1" */
  variant?: SectionWiseDashboardVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function SectionWiseDashboard(props: SectionWiseDashboardProps): JSX.Element;
