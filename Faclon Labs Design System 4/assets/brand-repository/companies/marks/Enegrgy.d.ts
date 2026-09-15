import * as React from 'react';

export type EnegrgyVariant = "cairn" | "haldiapetrochemicals" | "indianOIL" | "jSWEnergy" | "tatapower";

/** Enegrgy customer marks from the Faclon brand repository, 5 variants. Third-party trademark. */
export interface EnegrgyProps extends React.SVGProps<SVGSVGElement> {
  /** @default "cairn" */
  variant?: EnegrgyVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function Enegrgy(props: EnegrgyProps): JSX.Element;
