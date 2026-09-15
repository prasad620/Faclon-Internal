import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "black": "BruceProperty1Black",
  "white": "BruceProperty1White",
};

/** Bruce — The Bruce mark from the Faclon brand repository, 2 variants. */
export function Bruce({ variant = "black", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["black"];
  return <Icon name={name} size={size} {...rest} />;
}
