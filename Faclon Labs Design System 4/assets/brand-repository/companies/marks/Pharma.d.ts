import * as React from 'react';

export type PharmaVariant = "mainkind" | "zydus";

/** Pharma customer marks from the Faclon brand repository, 2 variants. Third-party trademark. */
export interface PharmaProps extends React.SVGProps<SVGSVGElement> {
  /** @default "mainkind" */
  variant?: PharmaVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function Pharma(props: PharmaProps): JSX.Element;
