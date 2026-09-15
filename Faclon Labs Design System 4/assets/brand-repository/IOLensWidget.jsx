import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "barChart": "IOLensWidgetProperty1BarChart",
  "dataCard": "IOLensWidgetProperty1DataCard",
  "dataTable": "IOLensWidgetProperty1DataTable",
};

/** IOLensWidget — The IOLensWidget mark from the Faclon brand repository, 3 variants. */
export function IOLensWidget({ variant = "barChart", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["barChart"];
  return <Icon name={name} size={size} {...rest} />;
}
