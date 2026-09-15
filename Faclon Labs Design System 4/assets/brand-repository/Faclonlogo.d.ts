import * as React from 'react';

export type FaclonlogoVariant = "black" | "blue" | "white";

/** The Faclonlogo mark from the Faclon brand repository, 3 variants. */
export interface FaclonlogoProps extends React.SVGProps<SVGSVGElement> {
  /** @default "black" */
  variant?: FaclonlogoVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function Faclonlogo(props: FaclonlogoProps): JSX.Element;
