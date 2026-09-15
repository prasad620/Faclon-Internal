import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "1": "DeviceLiveDataAndTrendProperty11",
  "2": "DeviceLiveDataAndTrendProperty12",
  "3": "DeviceLiveDataAndTrendProperty13",
};

/** DeviceLiveDataAndTrend — The DeviceLiveDataAndTrend mark from the Faclon brand repository, 3 variants. */
export function DeviceLiveDataAndTrend({ variant = "1", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["1"];
  return <Icon name={name} size={size} {...rest} />;
}
