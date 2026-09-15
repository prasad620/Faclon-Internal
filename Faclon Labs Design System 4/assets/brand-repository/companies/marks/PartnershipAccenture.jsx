import React from 'react';
import { CompanyIcon } from '../CompanyIcon.jsx';

const VARIANTS = {
  "default": "PartnershipAccenture",
};

/** PartnershipAccenture — PartnershipAccenture customer marks from the Faclon brand repository, 1 variant. Third-party trademark. */
export function PartnershipAccenture({ variant = "default", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["default"];
  return <CompanyIcon name={name} size={size} {...rest} />;
}
