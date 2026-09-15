import * as React from 'react';

export type VectorVariant = "featureCircle" | "flowView" | "lighthouse" | "multiLevelRing" | "processCircle" | "processView" | "pyramid" | "semiCircle" | "splitFlow" | "stackedBlockTower" | "staircaseProgression1" | "staircaseProgression2" | "worldMap";

/** Vector customer marks from the Faclon brand repository, 13 variants. Third-party trademark. */
export interface VectorProps extends React.SVGProps<SVGSVGElement> {
  /** @default "featureCircle" */
  variant?: VectorVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function Vector(props: VectorProps): JSX.Element;
