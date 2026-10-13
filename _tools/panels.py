# WHYNOT · Trial 03 — "Panel & Ink"
#
# The icon and decoration set for the anime/manga direction.
#
# Deliberately NOT the same drawings as Trial 02: those are wobbly, hand-drawn
# pen lines. These are crisp, geometric and symmetrical — straight strokes,
# sharp joins, flat shapes — because a manga panel is ruled with a straightedge,
# not a pen. Same catalogue, completely different hand.
#
# Symbols use viewBox 0 0 64 64 and inherit colour via stroke="currentColor",
# so one icon works on white, on a tinted panel or knockout on a dark bar.

STROKE = "4.2"      # heavier than trial 02: these are read at sticker size
JOIN = "miter"      # sharp corners, not rounded

ICONS = {
    # ---------------------------------------------------------- appliances
    "i-tv": '''
      <rect x="6" y="12" width="52" height="34" rx="3"/>
      <path d="M6 38h52"/>
      <path d="M22 52h20M32 46v6"/>
      <path d="M14 20h14"/>
      <path d="M26 6 18 13M38 6l8 7"/>''',

    "i-ac": '''
      <rect x="6" y="10" width="52" height="20" rx="3"/>
      <path d="M6 22h52"/>
      <path d="M16 38v12M32 38v14M48 38v11"/>
      <path d="M22 38c0 6 4 6 4 12M38 38c0 7 4 6 4 12"/>
      <path d="M14 16h18"/>''',

    "i-fridge": '''
      <rect x="16" y="4" width="32" height="56" rx="4"/>
      <path d="M16 24h32"/>
      <path d="M42 12v6M42 30v8"/>
      <path d="M10 60h44"/>''',

    "i-washer": '''
      <rect x="12" y="6" width="40" height="52" rx="4"/>
      <path d="M12 18h40"/>
      <circle cx="32" cy="39" r="12"/>
      <path d="M24 39c0 4 3.6 7 8 7M40 39c0-4-3.6-7-8-7"/>
      <path d="M42 12h4"/>
      <path d="M8 58h48"/>''',

    "i-mixer": '''
      <path d="M22 8h20l-3 20H25z"/>
      <path d="M18 46h28l-2 12H20z"/>
      <path d="M25 28h29c0 6-4 10-10 10h-19"/>
      <path d="M32 52v6M26 58h12"/>
      <path d="M22 14h10"/>''',

    "i-micro": '''
      <rect x="4" y="14" width="56" height="34" rx="3"/>
      <rect x="10" y="20" width="30" height="22" rx="2"/>
      <path d="M48 22v2M48 30v2M48 38v2"/>
      <path d="M16 26h14"/>
      <path d="M32 54H12"/>''',

    "i-grinder": '''
      <path d="M14 30h36v14H14z"/>
      <path d="M20 30c0-8 5-13 12-13s12 5 12 13"/>
      <path d="M32 10v6"/>
      <path d="M18 44c0 6-2 8-4 10M46 44c0 6 2 8 4 10"/>
      <path d="M22 36h20"/>''',

    "i-droplet": '''
      <path d="M32 6c9 12 16 19 16 27a16 16 0 0 1-32 0c0-8 7-15 16-27Z"/>
      <path d="M24 36c0 4 3 7 7 8"/>
      <path d="M44 14l4-6M20 14l-4-6"/>''',

    "i-geyser": '''
      <rect x="14" y="18" width="36" height="30" rx="6"/>
      <path d="M26 18V8h12v10"/>
      <path d="M20 48v8M44 48v8"/>
      <circle cx="32" cy="33" r="6"/>
      <path d="M32 27v6l4 3"/>''',

    "i-bulb": '''
      <path d="M32 6a18 18 0 0 1 10 32.8V44H22v-5.2A18 18 0 0 1 32 6Z"/>
      <path d="M23 50h18M26 56h12"/>
      <path d="M32 34v10"/>
      <path d="M14 12 8 6M50 12l6-6M6 30h-4M62 30h-4"/>''',

    "i-speaker": '''
      <rect x="18" y="6" width="28" height="52" rx="4"/>
      <circle cx="32" cy="40" r="10"/>
      <circle cx="32" cy="19" r="4"/>
      <path d="M52 20c4 6 4 18 0 24M12 20c-4 6-4 18 0 24"/>''',

    "i-vacuum": '''
      <circle cx="24" cy="40" r="16"/>
      <path d="M38 32 52 12"/>
      <path d="M14 40h20M24 30v20"/>
      <path d="M46 24l6-8 6 4-6 8z"/>
      <path d="M8 56h32"/>''',

    "i-phone": '''
      <rect x="18" y="4" width="28" height="56" rx="5"/>
      <path d="M18 14h28"/>
      <path d="M28 52h8"/>
      <path d="M40 8v4M40 20v12"/>
      <rect x="24" y="20" width="16" height="22" rx="2"/>''',

    # ------------------------------------------------------------- interface
    "i-cart": '''
      <path d="M4 10h8l7 28h32l6-22H12"/>
      <circle cx="22" cy="50" r="5"/>
      <circle cx="44" cy="50" r="5"/>
      <path d="M24 22h22"/>''',

    "i-call": '''
      <path d="M18 6c1.6 0 3 1 3.4 2.6l2 8c.4 1.6-.4 3-1.8 3.6l-4 1.8c3 7 8.4 12.4 15.4 15.4l1.8-4c.6-1.4 2-2.2 3.6-1.8l8 2c1.6.4 2.6 1.8 2.6 3.4v5.4c0 2-1.6 3.6-3.6 3.6C26 49 15 38 16.4 16.6 16.4 14.6 18 13 20 13z"/>''',

    "i-whatsapp": '''
      <path d="M12 52c-2-3.4-3.2-7.4-3.2-11.6C8.8 26 19.6 15 33 15s24 11 24 25.4S46.4 65.8 33 65.8c-4.4 0-8.6-1.2-12.2-3.4z" transform="translate(-1,-7)"/>
      <path d="M25 25c.8-.6 1.8-.2 2.4.8l2.4 4.4c.6 1 0 2.2-1 3l-2 1.6c2 4.4 5.4 7.8 9.8 9.8l1.6-2c.8-1 2-1.6 3-1l4.4 2.4c1 .6 1.4 1.6.8 2.4l-1.6 2.4c-1 1.4-2.4 2.2-4 2-11-1.4-20-10.4-21.4-21.4-.2-1.6.6-3 2-4z" transform="translate(-1,-7)"/>''',

    "i-pin": '''
      <path d="M32 6c9.4 0 17 7.6 17 17 0 12-17 35-17 35S15 35 15 23c0-9.4 7.6-17 17-17Z"/>
      <circle cx="32" cy="23" r="6.4"/>
      <path d="M6 58h52"/>''',

    "i-search": '''
      <circle cx="27" cy="27" r="19"/>
      <path d="M41 41l16 16"/>
      <path d="M18 22h18"/>''',

    "i-sparkle": '''
      <path d="M32 4c2.6 10 7 14.4 17 17-10 2.6-14.4 7-17 17-2.6-10-7-14.4-17-17 10-2.6 14.4-7 17-17Z"/>
      <path d="M52 42c1.2 4.6 3.2 6.6 7.8 7.8-4.6 1.2-6.6 3.2-7.8 7.8-1.2-4.6-3.2-6.6-7.8-7.8 4.6-1.2 6.6-3.2 7.8-7.8Z"/>
      <path d="M12 40c.8 3.2 2.2 4.6 5.4 5.4-3.2.8-4.6 2.2-5.4 5.4-.8-3.2-2.2-4.6-5.4-5.4 3.2-.8 4.6-2.2 5.4-5.4Z"/>''',

    "i-star": '''
      <path d="M32 4l8.4 18.6L60 25.4 44.8 39.4l4.6 21.2L32 50.2 14.6 60.6l4.6-21.2L4 25.4l19.6-2.8z"/>''',

    "i-bolt": '''
      <path d="M38 4 14 36h14l-4 24 26-34H36z"/>''',

    "i-clock": '''
      <circle cx="32" cy="32" r="26"/>
      <path d="M32 14v18l14 8"/>
      <path d="M32 6v-4M32 62v-4"/>''',

    "i-check": '''<path d="M8 34 24 50 56 12"/>''',

    "i-menu": '''<path d="M6 16h52M6 32h52M6 48h52"/>''',

    "i-close": '''<path d="M12 12l40 40M52 12 12 52"/>''',

    "i-copy": '''
      <rect x="6" y="6" width="34" height="44" rx="3"/>
      <path d="M18 18h40v42H18z"/>
      <path d="M26 34h24M26 44h16"/>''',

    "i-shield": '''
      <path d="M32 4c6.4 4 14.4 6.4 22 8 1.2 12-3.2 27.2-22 37.6C13.2 39.2 8.8 24 10 12c7.6-1.6 15.6-4 22-8Z"/>
      <path d="M22 30l8 8 13-15"/>''',

    "i-truck": '''
      <path d="M2 14h34v30H2z"/>
      <path d="M36 22h12l12 12v10H36z"/>
      <circle cx="14" cy="50" r="6"/>
      <circle cx="46" cy="50" r="6"/>
      <path d="M8 22h14"/>''',

    "i-wrench": '''
      <path d="M46 6 34 18l-4 12-16 16a6 6 0 0 0 8 8l16-16 12-4L62 22l-8-2-2-8-6-6z" transform="scale(.94) translate(2,2)"/>
      <circle cx="20" cy="50" r="3"/>''',

    "i-people": '''
      <circle cx="22" cy="20" r="11"/>
      <path d="M2 58c2-12 10-19 20-19s18 7 20 19"/>
      <circle cx="47" cy="22" r="8"/>
      <path d="M40 40c9-2 18 4 21 18"/>''',

    "i-store": '''
      <path d="M6 24 12 6h40l6 18z"/>
      <path d="M6 24c0 4 4 7 9 7s9-3 9-7c0 4 3 7 8 7s8-3 8-7c0 4 4 7 9 7s9-3 9-7"/>
      <path d="M12 32v26h40V32"/>
      <path d="M26 58V42h12v16"/>''',

    "i-tag": '''
      <path d="M6 30 30 6h28v28L34 58z"/>
      <circle cx="46" cy="18" r="5"/>
      <path d="M20 26l18 18"/>''',

    "i-box": '''
      <path d="M6 20 32 6l26 14v24L32 58 6 44z"/>
      <path d="M6 20l26 14 26-14M32 34v24"/>
      <path d="M19 13l26 14"/>''',

    "i-heart": '''
      <path d="M32 56C16 46 6 38 6 26 6 16 14 10 22 10c4.4 0 8 2.4 10 6 2-3.6 5.6-6 10-6 8 0 16 6 16 16 0 12-10 20-26 30Z"/>''',

    "i-sun": '''
      <circle cx="32" cy="32" r="14"/>
      <path d="M32 6v8M32 50v8M6 32h8M50 32h8M13 13l6 6M45 45l6 6M51 13l-6 6M19 45l-6 6"/>''',

    # ------------------------------------------------- decoration / panels
    # Radial speed lines: a starburst, used behind the hero and in empty states.
    "d-speed": '''
      <g stroke-width="2.4">
        <path d="M32 32 8 4M32 32 24 2M32 32 44 2M32 32 62 6M32 32 64 20M32 32 62 34M32 32 60 50M32 32 46 62M32 32 32 64M32 32 18 62M32 32 4 48M32 32 0 34M32 32 4 18M32 32 20 6"/>
      </g>''',

    # A jagged "impact" star, the classic manga shout shape.
    "d-burst": '''
      <path d="M32 2l6 12 8-9-1 14 12-5-6 12 14 0-11 9 12 8-14 0 6 12-12-5 1 14-8-9-6 12-6-12-8 9 1-14-12 5 6-12-14 0 12-8-11-9 14 0-6-12 12 5-1-14 8 9z"/>''',

    # Motion lines for a panel edge.
    "d-lines": '''
      <g stroke-width="2.6">
        <path d="M2 10h40M2 20h52M2 30h30M2 40h46M2 50h34"/>
      </g>''',

    "d-arrow": '''
      <path d="M4 32h44M36 18l16 14-16 14"/>''',
}

# A manga "action" title treatment: the WHYNOT mark knocked out of a burst,
# used once per page at large size. Kept as a symbol so the pages stay small.
PANEL_BADGE = '''
  <symbol id="d-badge" viewBox="0 0 120 120">
    <path d="M60 4l10 20 14-16-2 22 22-8-11 19 23 1-18 14 19 13-23 1 11 19-22-8 2 22-14-16-10 20-10-20-14 16 2-22-22 8 11-19-23-1 18-13-19-14 23-1-11-19 22 8-2-22 14 16z"
          fill="#ff2e88" stroke="#0e1230" stroke-width="5" stroke-linejoin="miter"/>
  </symbol>
'''

SPRITE_OPEN = ('<svg xmlns="http://www.w3.org/2000/svg" style="position:absolute;width:0;height:0;overflow:hidden" '
               'aria-hidden="true" focusable="false">')
SPRITE_CLOSE = "</svg>"


def sprite():
    """The whole icon and decoration set, inline, once per page."""
    parts = [SPRITE_OPEN]
    # These two are backgrounds, not icons: they must stretch to whatever box
    # they are placed in, so the symbol itself carries preserveAspectRatio.
    STRETCHY = {"d-speed", "d-lines"}

    for name, body in ICONS.items():
        filled = name.startswith("d-burst")
        par = ' preserveAspectRatio="none"' if name in STRETCHY else ""
        if filled:
            parts.append('<symbol id="%s" viewBox="0 0 64 64"%s><g fill="currentColor" stroke="currentColor" '
                         'stroke-width="3" stroke-linejoin="miter">%s</g></symbol>' % (name, par, body.strip()))
        else:
            parts.append('<symbol id="%s" viewBox="0 0 64 64"%s><g fill="none" stroke="currentColor" '
                         'stroke-width="%s" stroke-linejoin="%s" stroke-linecap="butt">%s</g></symbol>'
                         % (name, par, STROKE, JOIN, body.strip()))
    parts.append(PANEL_BADGE)
    parts.append(SPRITE_CLOSE)
    return "\n".join(parts)
