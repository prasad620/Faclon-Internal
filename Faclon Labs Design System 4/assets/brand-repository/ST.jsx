import React from 'react';
import { Icon } from './Icon.jsx';

const VARIANTS = {
  "100": "STProperty1100",
  "120D": "STProperty1120D",
  "120D2": "STProperty1120D2",
  "120WD": "STProperty1120WD",
  "120WD2": "STProperty1120WD2",
  "50": "STProperty150",
  "51": "STProperty151",
  "52CW": "STProperty152CW",
  "52CW2": "STProperty152CW2",
  "52CW3": "STProperty152CW3",
  "52L": "STProperty152L",
  "52LEU": "STProperty152LEU",
  "52LEU2": "STProperty152LEU2",
  "52LR": "STProperty152LR",
  "52P": "STProperty152P",
  "52Pulse": "STProperty152Pulse",
  "53": "STProperty153",
  "54": "STProperty154",
  "54P": "STProperty154P",
  "56C": "STProperty156C",
  "65": "STProperty165",
  "92": "STProperty192",
  "94": "STProperty194",
  "98M": "STProperty198M",
  "98S": "STProperty198S",
};

/** ST — The ST mark from the Faclon brand repository, 25 variants. */
export function ST({ variant = "100", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["100"];
  return <Icon name={name} size={size} {...rest} />;
}
