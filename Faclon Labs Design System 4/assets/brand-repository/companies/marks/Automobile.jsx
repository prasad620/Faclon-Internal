import React from 'react';
import { CompanyIcon } from '../CompanyIcon.jsx';

const VARIANTS = {
  "eicher": "AutomobileProperty1Eicher",
  "kubotaProperty2": "AutomobileProperty1KubotaProperty2",
  "tOYODAGOSEI": "AutomobileProperty1TOYODAGOSEI",
  "uNOMINDA": "AutomobileProperty1UNOMINDA",
};

/** Automobile — Automobile customer marks from the Faclon brand repository, 4 variants. Third-party trademark. */
export function Automobile({ variant = "eicher", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["eicher"];
  return <CompanyIcon name={name} size={size} {...rest} />;
}
