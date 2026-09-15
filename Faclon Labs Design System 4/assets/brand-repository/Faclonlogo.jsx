import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "black": "FaclonlogoProperty1Black",
  "blue": "FaclonlogoProperty1Blue",
  "white": "FaclonlogoProperty1White",
};

/** Faclonlogo — The Faclonlogo mark from the Faclon brand repository, 3 variants. */
export function Faclonlogo({ variant = "black", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["black"];
  return <Icon name={name} size={size} {...rest} />;
}
