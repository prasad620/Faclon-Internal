import * as React from 'react';

export type ConsumerGoodsVariant = "cocacola" | "dabur" | "iTC" | "marico" | "mondelez";

/** ConsumerGoods customer marks from the Faclon brand repository, 5 variants. Third-party trademark. */
export interface ConsumerGoodsProps extends React.SVGProps<SVGSVGElement> {
  /** @default "cocacola" */
  variant?: ConsumerGoodsVariant;
  /** Rendered size in px. @default 32 */
  size?: number | string;
}

export declare function ConsumerGoods(props: ConsumerGoodsProps): JSX.Element;
