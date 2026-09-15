import React from 'react';
import { CompanyIcon } from '../CompanyIcon.jsx';

const VARIANTS = {
  "idex": "OEMProperty1Idex",
  "kSB": "OEMProperty1KSB",
};

/** OEM — OEM customer marks from the Faclon brand repository, 2 variants. Third-party trademark. */
export function OEM({ variant = "idex", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["idex"];
  return <CompanyIcon name={name} size={size} {...rest} />;
}
