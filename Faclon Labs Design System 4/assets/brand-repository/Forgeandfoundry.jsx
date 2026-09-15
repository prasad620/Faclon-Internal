import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "black": "ForgeandfoundryProperty1Black",
  "white": "ForgeandfoundryProperty1White",
};

/** Forgeandfoundry — The Forgeandfoundry mark from the Faclon brand repository, 2 variants. */
export function Forgeandfoundry({ variant = "black", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["black"];
  return <Icon name={name} size={size} {...rest} />;
}
