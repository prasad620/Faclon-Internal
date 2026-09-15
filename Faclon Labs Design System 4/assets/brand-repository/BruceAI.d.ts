import * as React from 'react';

export type BruceAIVariant = "default" | "default2" | "default3";

/** The BruceAI mark from the Faclon brand repository, 3 variants. */
export interface BruceAIProps extends React.SVGProps<SVGSVGElement> {
  /** @default "default" */
  variant?: BruceAIVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function BruceAI(props: BruceAIProps): JSX.Element;
