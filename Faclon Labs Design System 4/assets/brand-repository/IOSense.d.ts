import * as React from 'react';

export type IOSenseVariant = "blue" | "white";

/** The IOSense mark from the Faclon brand repository, 2 variants. */
export interface IOSenseProps extends React.SVGProps<SVGSVGElement> {
  /** @default "blue" */
  variant?: IOSenseVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function IOSense(props: IOSenseProps): JSX.Element;
