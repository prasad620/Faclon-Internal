import React from 'react';

/**
 * Card — the UI card from the brand file. One component covering the 16 source layouts.
 *
 * Spacing is transcribed frame by frame:
 *   card            radius 10, padding 18, gap 10
 *   inner stack     gap 14 (no chip) / 12 (chip present)
 *   header row      gap 10 leading media; space-between for trailing media or a chip
 *   text column     gap 0, or 1 when an eyebrow is present
 *   chip row        gap 20, then title→body gap 9
 *   footer row      gap 8
 *
 * Surface: the card stays PALE in both themes — #FFFFFF on light, #E3EAF3 on dark — so its
 * text, chip and media tokens are card-scoped (--card-*) rather than the theme's text roles.
 * Border: 1px --card-border — #CBD5E2 on light, #B1C1D2 on dark.
 *
 * The 30x30 grey square in the source frames is a PLACEHOLDER, not a literal swatch — it holds
 * an icon, a mark, or a short highlight value (a metric, a count, a keyword).
 */
export function Card({
  eyebrow,
  title,
  subtitle,
  body,
  chip,
  media,
  mediaPosition = 'leading',
  footer,
  elevation = 'none',
  as: Tag = 'div',
  style,
  children,
  ...rest
}) {
  const trailing = mediaPosition === 'trailing';
  const hasMedia = media !== undefined && media !== null;

  const mediaEl = hasMedia ? (
    <span style={{ width: 30, height: 30, flexShrink: 0, borderRadius: 'var(--border-radius-medium)', background: 'var(--card-media)', display: 'inline-flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden', color: 'var(--card-body)' }}>
      {media}
    </span>
  ) : null;

  const eyebrowEl = eyebrow ? (
    <span style={{ fontFamily: 'var(--font-body)', fontWeight: 400, fontSize: 7, lineHeight: '100%', color: 'var(--card-eyebrow)' }}>{eyebrow}</span>
  ) : null;

  const titleEl = title ? (
    <span style={{ fontFamily: 'var(--font-heading)', fontWeight: 700, fontSize: 15, lineHeight: '100%', color: 'var(--card-heading)' }}>{title}</span>
  ) : null;

  const subtitleEl = subtitle ? (
    <span style={{ fontFamily: 'var(--font-body)', fontWeight: 400, fontSize: 10, lineHeight: '100%', color: 'var(--card-body)' }}>{subtitle}</span>
  ) : null;

  const bodyEl = body ? (
    <p style={{ margin: 0, alignSelf: 'stretch', fontFamily: 'var(--font-body)', fontWeight: 400, fontSize: 10, lineHeight: '120%', color: 'var(--card-body)', textWrap: 'pretty' }}>{body}</p>
  ) : null;

  const chipEl = chip ? (
    <span style={{
      display: 'inline-flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0,
      height: 12.809, padding: '3.202px 3.843px', gap: 3.2023332118988037,
      borderRadius: 2.5618667602539062,
      background: 'var(--card-chip-bg)',
      color: 'var(--card-chip-text)',
      fontFamily: 'var(--font-body)', fontWeight: 500, fontSize: 7.685600280761719,
      lineHeight: '100%', textTransform: 'capitalize', whiteSpace: 'nowrap',
    }}>{chip}</span>
  ) : null;

  const footerEl = footer ? (
    <div style={{ display: 'flex', alignItems: 'center', gap: 8, alignSelf: 'stretch' }}>{footer}</div>
  ) : null;

  const shell = {
    display: 'flex', flexDirection: 'column', gap: 10, boxSizing: 'border-box',
    padding: 18,
    borderRadius: 'var(--border-radius-max)',
    border: '1px solid var(--card-border)',
    background: 'var(--card-surface)',
    boxShadow: elevation === 'low' ? 'var(--shadow-low-raised)' : elevation === 'mid' ? 'var(--shadow-mid-raised)' : 'none',
    ...style,
  };

  // Chip layout (Frames 12–15): eyebrow + chip share a row (gap 20), then title → body at gap 9.
  if (chipEl) {
    return (
      <Tag {...rest} style={shell}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 12, alignItems: 'flex-start', alignSelf: 'stretch' }}>
          <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', gap: 20, alignSelf: 'stretch', justifyContent: 'space-between' }}>
            {trailing ? null : mediaEl}
            <span style={{ display: 'flex', flexDirection: 'column', gap: 9, minWidth: 0, flex: '1 1 auto' }}>{eyebrowEl}</span>
            {chipEl}
            {trailing ? mediaEl : null}
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 9, alignItems: 'flex-start', alignSelf: 'stretch' }}>
            {titleEl}
            {subtitleEl}
            {bodyEl}
          </div>
          {children}
          {footerEl}
        </div>
      </Tag>
    );
  }

  // Header layout (Frames 1–11): media + text column, then body at gap 14.
  const textCol = (eyebrowEl || titleEl || subtitleEl) ? (
    <span style={{ display: 'flex', flexDirection: 'column', gap: eyebrowEl ? 1 : 0, minWidth: 0, flex: '1 1 auto' }}>
      {eyebrowEl}
      {titleEl}
      {subtitleEl}
    </span>
  ) : null;

  return (
    <Tag {...rest} style={shell}>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 14, alignItems: 'flex-start', alignSelf: 'stretch' }}>
        {(mediaEl || textCol) ? (
          <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', gap: 10, alignSelf: 'stretch', justifyContent: trailing ? 'space-between' : 'flex-start' }}>
            {trailing ? null : mediaEl}
            {textCol}
            {trailing ? mediaEl : null}
          </div>
        ) : null}
        {bodyEl}
        {children}
        {footerEl}
      </div>
    </Tag>
  );
}
