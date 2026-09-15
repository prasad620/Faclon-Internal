import * as React from 'react';

/** The marketing call-to-action: pill fill, label, trailing arrow, raised shadow. */
export interface ActionButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  /** `'arrow'` uses the brand arrow from assets/icons. Pass a node for a different glyph, or `null` for none. @default 'arrow' */
  icon?: 'arrow' | React.ReactNode | null;
  /** @default true */
  shadow?: boolean;
  /** Render as a different element, e.g. `'a'` for a link. @default 'button' */
  as?: keyof JSX.IntrinsicElements;
  children?: React.ReactNode;
}

export declare function ActionButton(props: ActionButtonProps): JSX.Element;
