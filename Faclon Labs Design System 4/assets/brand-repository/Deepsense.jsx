import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "black": "DeepsenseProperty1Black",
  "white": "DeepsenseProperty1White",
};

/** Deepsense — The Deepsense mark from the Faclon brand repository, 2 variants. */
export function Deepsense({ variant = "black", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["black"];
  return <Icon name={name} size={size} {...rest} />;
}
