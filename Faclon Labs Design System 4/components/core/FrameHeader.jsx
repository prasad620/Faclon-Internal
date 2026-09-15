import React from 'react';

const VARIANT_LABEL = { foundation: 'Foundation', component: 'Component', documentation: 'Documentation', published: 'Published' };

/** FrameHeader — title block that opens every page of the style guide. */
export function FrameHeader({ title = 'Title', description, variant = 'foundation', version, links = [], style, ...rest }) {
  return (
    <header {...rest} style={{ display: 'flex', flexDirection: 'column', gap: 8, ...style }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
        <h2 style={{ margin: 0, fontFamily: 'var(--font-display)', fontWeight: 600, fontSize: 'var(--heading-large-size)', lineHeight: 'var(--heading-large-line)', color: 'rgb(59,65,72)' }}>{title}</h2>
        <Chip>{VARIANT_LABEL[variant] || variant}</Chip>
        {version ? <Chip>{version}</Chip> : null}
      </div>
      {description ? (
        <p style={{ margin: 0, maxWidth: 640, fontFamily: 'var(--font-body)', fontWeight: 400, fontSize: 'var(--body-medium-size)', lineHeight: 'var(--body-medium-line)', color: 'var(--text-muted)' }}>{description}</p>
      ) : null}
      {links.length ? (
        <nav style={{ display: 'flex', gap: 16, marginTop: 8 }}>
          {links.map((l) => (
            <a key={l.label} href={l.href || '#'} style={{ fontFamily: 'var(--font-body)', fontWeight: 600, fontSize: 'var(--body-medium-size)', lineHeight: 'var(--body-medium-line)', color: 'var(--text-link)', textDecoration: 'none' }}>{l.label}</a>
          ))}
        </nav>
      ) : null}
    </header>
  );
}

function Chip({ children }) {
  return (
    <span style={{ display: 'inline-flex', alignItems: 'center', height: 20, padding: '0 8px', borderRadius: 'var(--border-radius-max)', background: 'var(--interactive-background-gray-default)', fontFamily: 'var(--font-body)', fontSize: 'var(--label-medium-size)', lineHeight: 'var(--label-medium-line)', fontWeight: 500, color: 'var(--text-subtle)' }}>{children}</span>
  );
}
