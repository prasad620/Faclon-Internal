import * as React from 'react';

/** Horizontal rule between sections. Thick (2px) is the documentation default. */
export interface SectionDividerProps extends React.HTMLAttributes<HTMLHRElement> {
  /** @default 'thick' */
  weight?: 'thin' | 'thick';
}

export declare function SectionDivider(props: SectionDividerProps): JSX.Element;
