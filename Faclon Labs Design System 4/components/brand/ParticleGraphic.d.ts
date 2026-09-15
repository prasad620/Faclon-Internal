import * as React from 'react';

/** The brand's dotted particle-field graphic. Decorative only — never place it over text. */
export interface ParticleGraphicProps extends React.ImgHTMLAttributes<HTMLImageElement> {
  /** Rendered width. Natural size is 743x763. @default 743 */
  width?: string | number;
  /** @default 1 */
  opacity?: number;
  /** Where the graphic files live. @default '/assets/graphics/' */
  basePath?: string;
}

export declare function ParticleGraphic(props: ParticleGraphicProps): JSX.Element;
