import * as React from 'react';

export type IOConnectVariant = "black" | "white";

/** The IOConnect mark from the Faclon brand repository, 2 variants. */
export interface IOConnectProps extends React.SVGProps<SVGSVGElement> {
  /** @default "black" */
  variant?: IOConnectVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function IOConnect(props: IOConnectProps): JSX.Element;
