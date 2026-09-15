import * as React from 'react';

export interface FrameHeaderLink { label: string; href?: string }

/**
 * Title block that opens every page of the style guide: name, status chip, blurb and resource links.
 */
export interface FrameHeaderProps extends React.HTMLAttributes<HTMLElement> {
  title?: string;
  description?: string;
  /** @default 'foundation' */
  variant?: 'foundation' | 'component' | 'documentation' | 'published';
  /** Optional version chip, e.g. "v1.2.0". */
  version?: string;
  links?: FrameHeaderLink[];
}

export declare function FrameHeader(props: FrameHeaderProps): JSX.Element;
