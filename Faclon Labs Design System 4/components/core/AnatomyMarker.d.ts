import * as React from 'react';

/**
 * Italic caption on a thin orange leader line, used to annotate component anatomy diagrams.
 */
export interface AnatomyMarkerProps extends React.HTMLAttributes<HTMLSpanElement> {
  label?: string;
  /** Which side of the annotated element the marker sits on. @default 'top' */
  direction?: 'top' | 'bottom' | 'left' | 'right';
  /** Leader-line length in px. @default 40 */
  length?: number;
}

export declare function AnatomyMarker(props: AnatomyMarkerProps): JSX.Element;
