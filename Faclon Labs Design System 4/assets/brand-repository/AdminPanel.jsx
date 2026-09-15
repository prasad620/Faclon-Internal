import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "deviceTypeDetail": "AdminPanelProperty1DeviceTypeDetail",
  "devices": "AdminPanelProperty1Devices",
};

/** AdminPanel — The AdminPanel mark from the Faclon brand repository, 2 variants. */
export function AdminPanel({ variant = "deviceTypeDetail", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["deviceTypeDetail"];
  return <Icon name={name} size={size} {...rest} />;
}
