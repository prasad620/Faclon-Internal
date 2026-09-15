import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "black": "IOConnectProperty1Black",
  "white": "IOConnectProperty1White",
};

/** IOConnect — The IOConnect mark from the Faclon brand repository, 2 variants. */
export function IOConnect({ variant = "black", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["black"];
  return <Icon name={name} size={size} {...rest} />;
}
