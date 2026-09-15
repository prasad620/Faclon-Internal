import React from 'react';
import { CompanyIcon } from '../CompanyIcon.jsx';

const VARIANTS = {
  "abGrasigm": "ConsumerdurablesProperty1AbGrasigm",
  "havells": "ConsumerdurablesProperty1Havells",
  "nerolac": "ConsumerdurablesProperty1Nerolac",
  "supreme": "ConsumerdurablesProperty1Supreme",
};

/** Consumerdurables — Consumerdurables customer marks from the Faclon brand repository, 4 variants. Third-party trademark. */
export function Consumerdurables({ variant = "abGrasigm", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["abGrasigm"];
  return <CompanyIcon name={name} size={size} {...rest} />;
}
