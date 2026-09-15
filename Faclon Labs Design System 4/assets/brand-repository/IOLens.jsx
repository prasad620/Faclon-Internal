import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "dashboardOuput": "IOLensProperty1DashboardOuput",
  "dashboardOuput2": "IOLensProperty1DashboardOuput2",
  "processOverviewDashboard": "IOLensProperty1ProcessOverviewDashboard",
};

/** IOLens — The IOLens mark from the Faclon brand repository, 3 variants. */
export function IOLens({ variant = "dashboardOuput", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["dashboardOuput"];
  return <Icon name={name} size={size} {...rest} />;
}
