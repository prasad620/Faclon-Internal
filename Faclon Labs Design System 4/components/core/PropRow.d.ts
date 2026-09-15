import * as React from 'react';

/**
 * One row of a component API table: name, description, type, allowed values, default.
 */
export interface PropRowProps extends React.HTMLAttributes<HTMLDivElement> {
  /** Render as the tinted header row. @default false */
  header?: boolean;
  name?: React.ReactNode;
  description?: React.ReactNode;
  type?: React.ReactNode;
  values?: React.ReactNode;
  defaultValue?: React.ReactNode;
}

export declare function PropRow(props: PropRowProps): JSX.Element;
