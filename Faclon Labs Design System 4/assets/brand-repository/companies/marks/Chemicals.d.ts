import * as React from 'react';

export type ChemicalsVariant = "basf" | "sRF";

/** Chemicals customer marks from the Faclon brand repository, 2 variants. Third-party trademark. */
export interface ChemicalsProps extends React.SVGProps<SVGSVGElement> {
  /** @default "basf" */
  variant?: ChemicalsVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function Chemicals(props: ChemicalsProps): JSX.Element;
