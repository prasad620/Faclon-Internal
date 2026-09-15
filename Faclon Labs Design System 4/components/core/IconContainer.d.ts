import * as React from 'react';

/**
 * 24px padded slot for a resource-link glyph next to a FrameHeader link.
 */
export interface IconContainerProps extends React.HTMLAttributes<HTMLSpanElement> {
  /** @default 24 */
  size?: number;
  children?: React.ReactNode;
}

export declare function IconContainer(props: IconContainerProps): JSX.Element;
