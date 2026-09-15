import React from 'react';
import { CompanyIcon } from '../CompanyIcon.jsx';

const VARIANTS = {
  "mainkind": "PharmaProperty1Mainkind",
  "zydus": "PharmaProperty1Zydus",
};

/** Pharma — Pharma customer marks from the Faclon brand repository, 2 variants. Third-party trademark. */
export function Pharma({ variant = "mainkind", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["mainkind"];
  return <CompanyIcon name={name} size={size} {...rest} />;
}
