import * as React from 'react';

/**
 * Heading (20/26 display) plus muted body copy (14/20) — the guide's standard prose block.
 */
export interface TextItemProps extends React.HTMLAttributes<HTMLDivElement> {
  heading?: React.ReactNode;
  /** Hide the bottom rule. @default true */
  borderLess?: boolean;
  children?: React.ReactNode;
}

export declare function TextItem(props: TextItemProps): JSX.Element;
