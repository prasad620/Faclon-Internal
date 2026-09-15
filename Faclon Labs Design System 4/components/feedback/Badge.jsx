import React from 'react';

const COLORS = {
  primary:     { subtleBg: 'rgba(48,94,255,0.09)',  subtleFg: 'rgb(48,94,255)',  intenseBg: 'rgb(48,94,255)'  },
  positive:    { subtleBg: 'rgba(0,162,81,0.09)',   subtleFg: 'rgb(0,135,67)',   intenseBg: 'rgb(0,162,81)'   },
  negative:    { subtleBg: 'rgba(217,45,32,0.09)',  subtleFg: 'rgb(217,45,32)',  intenseBg: 'rgb(217,45,32)'  },
  notice:      { subtleBg: 'rgba(233,105,12,0.09)', subtleFg: 'rgb(198,92,16)',  intenseBg: 'rgb(233,105,12)' },
  information: { subtleBg: 'rgba(18,145,208,0.09)', subtleFg: 'rgb(15,120,173)', intenseBg: 'rgb(18,145,208)' },
  neutral:     { subtleBg: 'rgba(108,132,157,0.09)',subtleFg: 'rgb(36,53,71)',   intenseBg: 'rgb(47,66,86)'   },
};

const SIZES = {
  small:  { height: 16, padding: '0 4px',  gap: 2, icon: 8,  fontSize: 10, lineHeight: '14px' },
  medium: { height: 20, padding: '0 8px',  gap: 4, icon: 12, fontSize: 12, lineHeight: '18px' },
  large:  { height: 24, padding: '0 12px', gap: 4, icon: 16, fontSize: 12, lineHeight: '18px' },
};

/** Badge — pill status label. 6 colors x 3 sizes x 2 emphasis levels. */
export function Badge({ color = 'neutral', size = 'medium', emphasis = 'subtle', icon, children, style, ...rest }) {
  const c = COLORS[color] || COLORS.neutral;
  const s = SIZES[size] || SIZES.medium;
  const intense = emphasis === 'intense';
  const fg = intense ? 'rgb(255,255,255)' : c.subtleFg;
  return (
    <span
      {...rest}
      style={{
        display: 'inline-flex', alignItems: 'center', boxSizing: 'border-box',
        height: s.height, padding: s.padding, gap: s.gap,
        borderRadius: 'var(--border-radius-max)',
        background: intense ? c.intenseBg : c.subtleBg,
        color: fg,
        fontFamily: 'var(--font-body)',
        fontSize: s.fontSize, lineHeight: s.lineHeight,
        fontWeight: intense ? 400 : 500,
        whiteSpace: 'nowrap',
        ...style,
      }}
    >
      {icon ? (
        <span style={{ width: s.icon, height: s.icon, display: 'inline-flex', alignItems: 'center', justifyContent: 'center', color: fg, flexShrink: 0 }}>
          {typeof icon === 'function' ? React.createElement(icon, { size: s.icon, color: fg }) : icon}
        </span>
      ) : null}
      {children}
    </span>
  );
}
