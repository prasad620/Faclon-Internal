import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "black": "FaclonmonoProperty1Black",
  "blue": "FaclonmonoProperty1Blue",
  "white": "FaclonmonoProperty1White",
};

/** Faclonmono — The Faclonmono mark from the Faclon brand repository, 3 variants. */
export function Faclonmono({ variant = "black", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["black"];
  return <Icon name={name} size={size} {...rest} />;
}
