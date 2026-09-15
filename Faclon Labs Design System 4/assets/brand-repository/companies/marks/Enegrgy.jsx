import React from 'react';
import { CompanyIcon } from '../CompanyIcon.jsx';

const VARIANTS = {
  "cairn": "EnegrgyProperty1Cairn",
  "haldiapetrochemicals": "EnegrgyProperty1Haldiapetrochemicals",
  "indianOIL": "EnegrgyProperty1IndianOIL",
  "jSWEnergy": "EnegrgyProperty1JSWEnergy",
  "tatapower": "EnegrgyProperty1Tatapower",
};

/** Enegrgy — Enegrgy customer marks from the Faclon brand repository, 5 variants. Third-party trademark. */
export function Enegrgy({ variant = "cairn", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["cairn"];
  return <CompanyIcon name={name} size={size} {...rest} />;
}
