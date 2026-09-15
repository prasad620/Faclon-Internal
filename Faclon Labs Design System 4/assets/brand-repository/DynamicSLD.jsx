import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "1": "DynamicSLDProperty11",
  "2": "DynamicSLDProperty12",
};

/** DynamicSLD — The DynamicSLD mark from the Faclon brand repository, 2 variants. */
export function DynamicSLD({ variant = "1", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["1"];
  return <Icon name={name} size={size} {...rest} />;
}
