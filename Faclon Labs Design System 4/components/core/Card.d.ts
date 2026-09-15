import * as React from 'react';

/**
 * The UI card from the brand file. One component covering all 16 source layouts —
 * supply only the parts the content needs and the rest collapse away.
 */
export interface CardProps extends React.HTMLAttributes<HTMLElement> {
  /** 7px label above the title. */
  eyebrow?: React.ReactNode;
  /** 15px TASA Orbiter heading. */
  title?: React.ReactNode;
  /** 10px supporting line under the title. */
  subtitle?: React.ReactNode;
  /** 10px paragraph below the header block. */
  body?: React.ReactNode;
  /** Small capitalised tag pinned to the end of the header row. */
  chip?: React.ReactNode;
  /**
   * 30x30 slot. The grey square in the Figma frames is a PLACEHOLDER — fill it with an icon,
   * a product/company mark, or a short highlight such as a metric or keyword ("98%", "NEW").
   * Pass `null` to omit it entirely.
   */
  media?: React.ReactNode;
  /** Which side of the header the media sits on. @default 'leading' */
  mediaPosition?: 'leading' | 'trailing';
  /** Row pinned under the body — actions, metadata, indicators. */
  footer?: React.ReactNode;
  /** @default 'none' */
  elevation?: 'none' | 'low' | 'mid';
  /** Render as a different element, e.g. `'a'` or `'article'`. @default 'div' */
  as?: keyof JSX.IntrinsicElements;
  children?: React.ReactNode;
}

export declare function Card(props: CardProps): JSX.Element;
