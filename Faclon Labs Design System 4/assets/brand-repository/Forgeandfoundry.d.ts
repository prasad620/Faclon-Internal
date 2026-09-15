import * as React from 'react';

export type ForgeandfoundryVariant = "black" | "white";

/** The Forgeandfoundry mark from the Faclon brand repository, 2 variants. */
export interface ForgeandfoundryProps extends React.SVGProps<SVGSVGElement> {
  /** @default "black" */
  variant?: ForgeandfoundryVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function Forgeandfoundry(props: ForgeandfoundryProps): JSX.Element;
