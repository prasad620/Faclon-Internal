import React from 'react';
import { CompanyIcon } from '../CompanyIcon.jsx';

const VARIANTS = {
  "cocacola": "ConsumerGoodsProperty1Cocacola",
  "dabur": "ConsumerGoodsProperty1Dabur",
  "iTC": "ConsumerGoodsProperty1ITC",
  "marico": "ConsumerGoodsProperty1Marico",
  "mondelez": "ConsumerGoodsProperty1Mondelez",
};

/** ConsumerGoods — ConsumerGoods customer marks from the Faclon brand repository, 5 variants. Third-party trademark. */
export function ConsumerGoods({ variant = "cocacola", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["cocacola"];
  return <CompanyIcon name={name} size={size} {...rest} />;
}
