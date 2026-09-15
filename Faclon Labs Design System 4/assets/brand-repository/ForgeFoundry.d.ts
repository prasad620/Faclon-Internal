import * as React from 'react';

export type ForgeFoundryVariant = "black" | "white";

/** The ForgeFoundry mark from the Faclon brand repository, 2 variants. */
export interface ForgeFoundryProps extends React.SVGProps<SVGSVGElement> {
  /** @default "black" */
  variant?: ForgeFoundryVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function ForgeFoundry(props: ForgeFoundryProps): JSX.Element;
