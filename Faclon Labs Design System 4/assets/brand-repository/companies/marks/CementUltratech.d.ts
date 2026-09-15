import * as React from 'react';

export type CementUltratechVariant = "default";

/** CementUltratech customer marks from the Faclon brand repository, 1 variant. Third-party trademark. */
export interface CementUltratechProps extends React.SVGProps<SVGSVGElement> {
  /** @default "default" */
  variant?: CementUltratechVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function CementUltratech(props: CementUltratechProps): JSX.Element;
