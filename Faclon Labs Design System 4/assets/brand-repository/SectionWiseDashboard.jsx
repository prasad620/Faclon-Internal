import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "1": "SectionWiseDashboardProperty11",
  "2": "SectionWiseDashboardProperty12",
};

/** SectionWiseDashboard — The SectionWiseDashboard mark from the Faclon brand repository, 2 variants. */
export function SectionWiseDashboard({ variant = "1", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["1"];
  return <Icon name={name} size={size} {...rest} />;
}
