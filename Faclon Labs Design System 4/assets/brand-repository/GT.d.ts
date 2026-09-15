import * as React from 'react';

export type GTVariant = "10" | "10A";

/** The GT mark from the Faclon brand repository, 2 variants. */
export interface GTProps extends React.SVGProps<SVGSVGElement> {
  /** @default "10" */
  variant?: GTVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function GT(props: GTProps): JSX.Element;
