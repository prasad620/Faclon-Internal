import * as React from 'react';

export type IOLensWidgetVariant = "barChart" | "dataCard" | "dataTable";

/** The IOLensWidget mark from the Faclon brand repository, 3 variants. */
export interface IOLensWidgetProps extends React.SVGProps<SVGSVGElement> {
  /** @default "barChart" */
  variant?: IOLensWidgetVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function IOLensWidget(props: IOLensWidgetProps): JSX.Element;
