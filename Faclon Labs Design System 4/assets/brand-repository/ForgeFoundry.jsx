import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "black": "ForgeFoundryProperty1Black",
  "white": "ForgeFoundryProperty1White",
};

/** ForgeFoundry — The ForgeFoundry mark from the Faclon brand repository, 2 variants. */
export function ForgeFoundry({ variant = "black", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["black"];
  return <Icon name={name} size={size} {...rest} />;
}
