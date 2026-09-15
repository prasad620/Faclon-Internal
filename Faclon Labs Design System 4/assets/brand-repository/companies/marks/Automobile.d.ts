import * as React from 'react';

export type AutomobileVariant = "eicher" | "kubotaProperty2" | "tOYODAGOSEI" | "uNOMINDA";

/** Automobile customer marks from the Faclon brand repository, 4 variants. Third-party trademark. */
export interface AutomobileProps extends React.SVGProps<SVGSVGElement> {
  /** @default "eicher" */
  variant?: AutomobileVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function Automobile(props: AutomobileProps): JSX.Element;
