import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "1": "MapProperty11",
  "2": "MapProperty12",
  "3": "MapProperty13",
};

/** Map — The Map mark from the Faclon brand repository, 3 variants. */
export function Map({ variant = "1", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["1"];
  return <Icon name={name} size={size} {...rest} />;
}
