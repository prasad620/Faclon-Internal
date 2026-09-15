import * as React from 'react';

export type ConsumerdurablesVariant = "abGrasigm" | "havells" | "nerolac" | "supreme";

/** Consumerdurables customer marks from the Faclon brand repository, 4 variants. Third-party trademark. */
export interface ConsumerdurablesProps extends React.SVGProps<SVGSVGElement> {
  /** @default "abGrasigm" */
  variant?: ConsumerdurablesVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function Consumerdurables(props: ConsumerdurablesProps): JSX.Element;
