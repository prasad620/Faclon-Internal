import * as React from 'react';

/**
 * The brand's hand-drawn gradient underline. Place it directly under a title — that is the
 * only sanctioned use; it is not a divider, a rule, or a decorative flourish elsewhere.
 */
export interface SignatureStrokeProps extends React.ImgHTMLAttributes<HTMLImageElement> {
  /** Rendered width. The stroke's natural size is 483x9. @default 483 */
  width?: string | number;
  /** Where the graphic files live. @default '/assets/graphics/' */
  basePath?: string;
}

export declare function SignatureStroke(props: SignatureStrokeProps): JSX.Element;
