import * as React from 'react';

export type OEMVariant = "idex" | "kSB";

/** OEM customer marks from the Faclon brand repository, 2 variants. Third-party trademark. */
export interface OEMProps extends React.SVGProps<SVGSVGElement> {
  /** @default "idex" */
  variant?: OEMVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function OEM(props: OEMProps): JSX.Element;
