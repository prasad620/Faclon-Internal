import React from 'react';
import { CompanyIcon } from '../CompanyIcon.jsx';

const VARIANTS = {
  "jSW": "MetalsProperty1JSW",
  "tata": "MetalsProperty1Tata",
  "vedanta": "MetalsProperty1Vedanta",
};

/** Metals — Metals customer marks from the Faclon brand repository, 3 variants. Third-party trademark. */
export function Metals({ variant = "jSW", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["jSW"];
  return <CompanyIcon name={name} size={size} {...rest} />;
}
