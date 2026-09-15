import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "default": "BruceAIProperty1Default",
  "default2": "BruceAIProperty1Default2",
  "default3": "BruceAIProperty1Default3",
};

/** BruceAI — The BruceAI mark from the Faclon brand repository, 3 variants. */
export function BruceAI({ variant = "default", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["default"];
  return <Icon name={name} size={size} {...rest} />;
}
