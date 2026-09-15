import React from 'react';

const SHAPES = { square: 4, pill: 10 };

/**
 * Chip — the marketing lockup from the brand file. Three configurations:
 * a squared uppercase chip, and a pill badge with or without shadow.
 */
export function Chip({
  shape = 'square',
  uppercase,
  shadow = false,
  size = 'large',
  style,
  children,
  ...rest
}) {
  const isSquare = shape === 'square';
  const caps = uppercase ?? isSquare;
  const large = size === 'large';
  return (
    <span
      {...rest}
      style={{
        display: 'inline-flex', alignItems: 'center', justifyContent: 'center', boxSizing: 'border-box',
        gap: 10,
        padding: large ? '10px 12px' : '7px 10px',
        borderRadius: SHAPES[shape] ?? SHAPES.square,
        background: 'var(--chip-bg)',
        color: 'var(--chip-text)',
        fontFamily: 'var(--font-body)',
        fontWeight: caps ? 600 : 500,
        fontSize: large ? (caps ? 24 : 20.189125061035156) : (caps ? 18 : 16),
        lineHeight: '100%',
        letterSpacing: caps ? '2.24px' : 'normal',
        textTransform: caps ? 'uppercase' : 'none',
        boxShadow: shadow ? 'var(--action-shadow)' : 'none',
        whiteSpace: 'nowrap',
        ...style,
      }}
    >
      {children}
    </span>
  );
}
