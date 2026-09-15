import React from 'react';
import { CompanyIcon } from '../CompanyIcon.jsx';

const VARIANTS = {
  "basf": "ChemicalsProperty1Basf",
  "sRF": "ChemicalsProperty1SRF",
};

/** Chemicals — Chemicals customer marks from the Faclon brand repository, 2 variants. Third-party trademark. */
export function Chemicals({ variant = "basf", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["basf"];
  return <CompanyIcon name={name} size={size} {...rest} />;
}
