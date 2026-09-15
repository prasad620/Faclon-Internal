import * as React from 'react';

/**
 * Capsule marking a guide page's state — the source kit's 4-variant status badge set:
 * Published, Version Number, Foundation, Documentation.
 */
export interface StatusProps extends React.HTMLAttributes<HTMLSpanElement> {
  /** @default 'published' */
  variant?: 'published' | 'version' | 'foundation' | 'documentation';
  /** Override the label (e.g. the actual version string). */
  children?: React.ReactNode;
}

export declare function Status(props: StatusProps): JSX.Element;
