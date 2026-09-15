import React from 'react';
import { CompanyIcon } from '../CompanyIcon.jsx';

const VARIANTS = {
  "featureCircle": "VectorProperty1FeatureCircle",
  "flowView": "VectorProperty1FlowView",
  "lighthouse": "VectorProperty1Lighthouse",
  "multiLevelRing": "VectorProperty1MultiLevelRing",
  "processCircle": "VectorProperty1ProcessCircle",
  "processView": "VectorProperty1ProcessView",
  "pyramid": "VectorProperty1Pyramid",
  "semiCircle": "VectorProperty1SemiCircle",
  "splitFlow": "VectorProperty1SplitFlow",
  "stackedBlockTower": "VectorProperty1StackedBlockTower",
  "staircaseProgression1": "VectorProperty1StaircaseProgression1",
  "staircaseProgression2": "VectorProperty1StaircaseProgression2",
  "worldMap": "VectorProperty1WorldMap",
};

/** Vector — Vector customer marks from the Faclon brand repository, 13 variants. Third-party trademark. */
export function Vector({ variant = "featureCircle", size = 32, ...rest }) {
  const name = VARIANTS[variant] || VARIANTS["featureCircle"];
  return <CompanyIcon name={name} size={size} {...rest} />;
}
