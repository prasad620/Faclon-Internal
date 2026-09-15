import * as React from 'react';

export type ThemeChoice = 'light' | 'dark' | 'system';

/** Applies a theme to a root element by setting `data-theme` and toggling `.dark`. Returns the resolved theme. */
export declare function applyTheme(theme: ThemeChoice, root?: HTMLElement): 'light' | 'dark';

/** Reads the stored preference. Defaults to `'system'`. */
export declare function getStoredTheme(): ThemeChoice;

/**
 * Segmented control letting the user pick Light, Dark or System. Persists to localStorage
 * and applies the choice to the document root, which flips every role token.
 */
export interface ThemeToggleProps extends React.HTMLAttributes<HTMLDivElement> {
  /** Which choices to offer. @default ['light','dark','system'] */
  options?: ThemeChoice[];
  /** Controlled value. Omit to let the component manage its own state. */
  value?: ThemeChoice;
  onChange?: (theme: ThemeChoice) => void;
  /** Element to theme. @default document.documentElement */
  root?: HTMLElement;
  /** Write the choice to localStorage. @default true */
  persist?: boolean;
}

export declare function ThemeToggle(props: ThemeToggleProps): JSX.Element;
