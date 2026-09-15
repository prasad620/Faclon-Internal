import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "blue": "IOSenseProperty1Blue",
  "white": "IOSenseProperty1White",
};

/** IOSense — The IOSense mark from the Faclon brand repository, 2 variants. */
export function IOSense({ variant = "blue", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["blue"];
  return <Icon name={name} size={size} {...rest} />;
}
