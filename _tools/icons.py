# WHYNOT redesign — the icon set for Trials 04, 05 and 06.
#
# Trials 02 and 03 each hand-wrote a full icon set, which is 60+ SVG paths of
# output per trial. From Trial 04 the *geometry* is shared and the *hand* changes:
# a heavy square-capped brutalist cut, a hairline rounded glass cut, and a soft
# pastel cut with a translucent underlay, all derived from the canonical paths in
# panels.py. Same catalogue, same symbols, three different pens.
#
# This is what a real design system does with icons, and it means all three new
# trials keep the same symbol ids — so one set of JavaScript drives all of them.

from panels import ICONS

CUTS = {
    # neo-brutalism: thick, square, no compromise
    "brutal": dict(stroke="6.6", cap="square", join="miter", halo=None, scale=1.0),
    # glassmorphism: hairline, rounded, weightless
    "glass": dict(stroke="1.8", cap="round", join="round", halo=None, scale=1.0),
    # painting: soft, rounded, with a translucent bloom underneath
    "paint": dict(stroke="2.7", cap="round", join="round", halo="10", scale=1.0),
    # slate: the professional cut — even weight, round joins, nothing decorative
    # (Trial 07). Same geometry as the others, so one script still drives it.
    "slate": dict(stroke="3.2", cap="round", join="round", halo=None, scale=1.0),
}

# The two "background" symbols stretch, so they keep their own aspect handling.
STRETCHY = {"d-speed", "d-lines"}


def _symbol(name, body, cut):
    filled = name == "d-burst"
    par = ' preserveAspectRatio="none"' if name in STRETCHY else ""
    g = []
    if cut["halo"]:
        # a wide, translucent copy of the same path: the "painted" soft edge
        g.append('<g fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="%s" '
                 'stroke-linejoin="%s" opacity=".22">%s</g>' % (cut["halo"], cut["cap"], cut["join"], body.strip()))
    if filled:
        g.append('<g fill="currentColor" stroke="currentColor" stroke-width="3" stroke-linejoin="miter">%s</g>'
                 % body.strip())
    else:
        g.append('<g fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="%s" '
                 'stroke-linejoin="%s">%s</g>' % (cut["stroke"], cut["cap"], cut["join"], body.strip()))
    return '<symbol id="%s" viewBox="0 0 64 64"%s>%s</symbol>' % (name, par, "".join(g))


def sprite(cut_name, extra=(), only=None):
    """The whole icon set, inline, once per page. `extra` holds design ornaments."""
    cut = CUTS[cut_name]
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" style="position:absolute;width:0;height:0;overflow:hidden" '
             'aria-hidden="true" focusable="false">']
    for name, body in ICONS.items():
        if only and name not in only:
            continue
        parts.append(_symbol(name, body, cut))
    for name, body in extra:
        parts.append('<symbol id="%s" viewBox="0 0 64 64">%s</symbol>' % (name, body.strip()))
    parts.append("</svg>")
    return "\n".join(parts)


def doodle(name, cls=""):
    """The markup for one icon, used by the page builders."""
    return '<svg class="doodle %s" aria-hidden="true"><use href="#%s"></use></svg>' % (cls, name)


def picture(base, alt, w, h, extra_class="", avif=True, webp=True, eager=False, sizes=None):
    """<picture> with AVIF → WebP → JPEG. Every new trial ships all three."""
    srcs = '<source srcset="assets/img/%s.avif" type="image/avif">\n' % base if avif else ""
    if webp:
        srcs += '<source srcset="assets/img/%s.webp" type="image/webp">\n' % base
    load = ' fetchpriority="high"' if eager else ' loading="lazy"'
    dims = ' width="%d" height="%d"' % (w, h) if w and h else ""
    cls = ' class="%s"' % extra_class if extra_class else ""
    return ('<picture%s>\n%s<img src="assets/img/%s.jpg"%s%s decoding="async" alt="%s">\n</picture>'
            % (cls, srcs, base, dims, load, alt))
