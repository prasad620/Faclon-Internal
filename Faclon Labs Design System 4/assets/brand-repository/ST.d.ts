import * as React from 'react';

export type STVariant = "100" | "120D" | "120D2" | "120WD" | "120WD2" | "50" | "51" | "52CW" | "52CW2" | "52CW3" | "52L" | "52LEU" | "52LEU2" | "52LR" | "52P" | "52Pulse" | "53" | "54" | "54P" | "56C" | "65" | "92" | "94" | "98M" | "98S";

/** The ST mark from the Faclon brand repository, 25 variants. */
export interface STProps extends React.SVGProps<SVGSVGElement> {
  /** @default "100" */
  variant?: STVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function ST(props: STProps): JSX.Element;
