import * as React from 'react';

export type MetalsVariant = "jSW" | "tata" | "vedanta";

/** Metals customer marks from the Faclon brand repository, 3 variants. Third-party trademark. */
export interface MetalsProps extends React.SVGProps<SVGSVGElement> {
  /** @default "jSW" */
  variant?: MetalsVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function Metals(props: MetalsProps): JSX.Element;
