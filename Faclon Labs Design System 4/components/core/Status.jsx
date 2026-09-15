import React from 'react';

const STATUSES = {
  published:     { label: 'Published',   bg: 'rgba(0,162,81,0.09)',   ring: 'rgba(0,108,54,0.09)',    fg: 'rgb(0,108,54)'    },
  version:       { label: 'v2.0',        bg: 'rgba(33,75,222,0.09)',  ring: 'rgba(23,44,120,0.09)',   fg: 'rgb(23,44,120)'   },
  foundation:    { label: 'Foundation',  bg: 'rgba(108,132,157,0.09)', ring: 'rgba(36,53,71,0.09)',   fg: 'rgb(36,53,71)'    },
  documentation: { label: 'Documentation', bg: 'rgba(108,132,157,0.09)', ring: 'rgba(36,53,71,0.09)', fg: 'rgb(36,53,71)'    },
};

/** Status — small tinted capsule marking a guide page's state. */
export function Status({ variant = 'published', children, style, ...rest }) {
  const s = STATUSES[variant] || STATUSES.published;
  return (
    <span
      {...rest}
      style={{
        display: 'inline-flex', alignItems: 'center', justifyContent: 'center', boxSizing: 'border-box',
        height: 26, padding: '4px 12px', borderRadius: 'var(--border-radius-max)',
        background: s.bg, boxShadow: 'inset 0 0 0 1px ' + s.ring,
        fontFamily: 'var(--font-body)', fontWeight: 400, fontSize: 12, lineHeight: '18px', color: s.fg, whiteSpace: 'nowrap',
        ...style,
      }}
    >
      {children || s.label}
    </span>
  );
}
