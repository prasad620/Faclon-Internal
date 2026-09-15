import * as React from 'react';

export type FaclonmonoVariant = "black" | "blue" | "white";

/** The Faclonmono mark from the Faclon brand repository, 3 variants. */
export interface FaclonmonoProps extends React.SVGProps<SVGSVGElement> {
  /** @default "black" */
  variant?: FaclonmonoVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function Faclonmono(props: FaclonmonoProps): JSX.Element;
