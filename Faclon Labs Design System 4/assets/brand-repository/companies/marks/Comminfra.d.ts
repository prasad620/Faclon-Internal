import * as React from 'react';

export type ComminfraVariant = "adani" | "chhatrapati" | "dLF" | "flipkart" | "iDEMIA" | "iITBombay" | "icic";

/** Comminfra customer marks from the Faclon brand repository, 7 variants. Third-party trademark. */
export interface ComminfraProps extends React.SVGProps<SVGSVGElement> {
  /** @default "adani" */
  variant?: ComminfraVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function Comminfra(props: ComminfraProps): JSX.Element;
