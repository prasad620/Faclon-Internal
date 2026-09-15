import * as React from 'react';

export type PartnershipAccentureVariant = "default";

/** PartnershipAccenture customer marks from the Faclon brand repository, 1 variant. Third-party trademark. */
export interface PartnershipAccentureProps extends React.SVGProps<SVGSVGElement> {
  /** @default "default" */
  variant?: PartnershipAccentureVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function PartnershipAccenture(props: PartnershipAccentureProps): JSX.Element;
