import * as React from 'react';

export type BruceVariant = "black" | "white";

/** The Bruce mark from the Faclon brand repository, 2 variants. */
export interface BruceProps extends React.SVGProps<SVGSVGElement> {
  /** @default "black" */
  variant?: BruceVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function Bruce(props: BruceProps): JSX.Element;
