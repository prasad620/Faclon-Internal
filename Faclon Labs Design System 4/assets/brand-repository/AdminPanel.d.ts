import * as React from 'react';

export type AdminPanelVariant = "deviceTypeDetail" | "devices";

/** The AdminPanel mark from the Faclon brand repository, 2 variants. */
export interface AdminPanelProps extends React.SVGProps<SVGSVGElement> {
  /** @default "deviceTypeDetail" */
  variant?: AdminPanelVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function AdminPanel(props: AdminPanelProps): JSX.Element;
