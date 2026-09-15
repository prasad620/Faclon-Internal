import * as React from 'react';

export type DynamicSLDVariant = "1" | "2";

/** The DynamicSLD mark from the Faclon brand repository, 2 variants. */
export interface DynamicSLDProps extends React.SVGProps<SVGSVGElement> {
  /** @default "1" */
  variant?: DynamicSLDVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function DynamicSLD(props: DynamicSLDProps): JSX.Element;
