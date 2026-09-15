import * as React from 'react';

export type MapVariant = "1" | "2" | "3";

/** The Map mark from the Faclon brand repository, 3 variants. */
export interface MapProps extends React.SVGProps<SVGSVGElement> {
  /** @default "1" */
  variant?: MapVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function Map(props: MapProps): JSX.Element;
