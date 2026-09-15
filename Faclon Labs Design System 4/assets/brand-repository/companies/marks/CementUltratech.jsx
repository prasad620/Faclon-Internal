import React from 'react';
import { CompanyIcon } from '../CompanyIcon.jsx';

const VARIANTS = {
  "default": "CementUltratech",
};

/** CementUltratech — CementUltratech customer marks from the Faclon brand repository, 1 variant. Third-party trademark. */
export function CementUltratech({ variant = "default", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["default"];
  return <CompanyIcon name={name} size={size} {...rest} />;
}
