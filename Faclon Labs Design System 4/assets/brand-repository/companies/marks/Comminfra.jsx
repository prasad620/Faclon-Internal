import React from 'react';
import { CompanyIcon } from '../CompanyIcon.jsx';

const VARIANTS = {
  "adani": "ComminfraProperty1Adani",
  "chhatrapati": "ComminfraProperty1Chhatrapati",
  "dLF": "ComminfraProperty1DLF",
  "flipkart": "ComminfraProperty1Flipkart",
  "iDEMIA": "ComminfraProperty1IDEMIA",
  "iITBombay": "ComminfraProperty1IITBombay",
  "icic": "ComminfraProperty1Icic",
};

/** Comminfra — Comminfra customer marks from the Faclon brand repository, 7 variants. Third-party trademark. */
export function Comminfra({ variant = "adani", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["adani"];
  return <CompanyIcon name={name} size={size} {...rest} />;
}
