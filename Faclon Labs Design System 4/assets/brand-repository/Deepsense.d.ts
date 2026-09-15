import * as React from 'react';

export type DeepsenseVariant = "black" | "white";

/** The Deepsense mark from the Faclon brand repository, 2 variants. */
export interface DeepsenseProps extends React.SVGProps<SVGSVGElement> {
  /** @default "black" */
  variant?: DeepsenseVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function Deepsense(props: DeepsenseProps): JSX.Element;
