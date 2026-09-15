import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "10": "GTProperty110",
  "10A": "GTProperty110A",
};

/** GT — The GT mark from the Faclon brand repository, 2 variants. */
export function GT({ variant = "10", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["10"];
  return <Icon name={name} size={size} {...rest} />;
}
