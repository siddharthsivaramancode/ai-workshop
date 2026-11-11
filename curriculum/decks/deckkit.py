"""Shared look-and-feel + animation helpers for workshop decks.

Every session deck imports this so all six sessions look the same.
Build a deck:  uv run --with python-pptx python curriculum/decks/build_session_01.py

Animations are written as raw PowerPoint timing XML (python-pptx has no
animation API). Use `anim_steps(slide, steps)` where each step is one click
(or the slide's auto-start) and holds a list of (shape, effect) pairs that
play together with a small stagger.
"""
from pathlib import Path

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from lxml import etree

# ---------- look ----------
INK = RGBColor(0x0F, 0x17, 0x2A)
ORANGE = RGBColor(0xFF, 0x5B, 0x14)
CYAN = RGBColor(0x00, 0xB8, 0xC9)
YELLOW = RGBColor(0xFF, 0xD2, 0x3F)
RED = RGBColor(0xE0, 0x2D, 0x3C)
GREEN = RGBColor(0x1F, 0xB2, 0x5A)
PAPER = RGBColor(0xF7, 0xF6, 0xF1)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
SLATE = RGBColor(0x47, 0x55, 0x69)
MIST = RGBColor(0xE6, 0xE4, 0xDC)

HEAD = "Arial Black"
BODY = "Arial"
MONO = "Courier New"

W, H = Inches(13.333), Inches(7.5)

# All finished decks go to <repo>/slideshows/
OUT_DIR = Path(__file__).resolve().parents[2] / "slideshows"


def new_deck():
    prs = Presentation()
    prs.slide_width, prs.slide_height = W, H
    return prs


def blank(prs, bg=PAPER):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    f = s.background.fill
    f.solid()
    f.fore_color.rgb = bg
    return s


def rect(slide, x, y, w, h, fill, line=None, shape=MSO_SHAPE.RECTANGLE):
    r = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    r.fill.solid()
    r.fill.fore_color.rgb = fill
    if line is None:
        r.line.fill.background()
    else:
        r.line.color.rgb = line
        r.line.width = Pt(2)
    r.shadow.inherit = False
    return r


def text(slide, x, y, w, h, paras, size=20, color=INK, font=BODY, bold=False,
         align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, shape=None, spacing=1.0):
    """paras: str | list of paragraphs; a paragraph is str or list of runs;
    a run is str or (str, {color, bold, font, size})."""
    if shape is None:
        shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = shape.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for side in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, side, Inches(0.08))
    if isinstance(paras, str):
        paras = [paras]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = spacing
        runs = [para] if isinstance(para, (str, tuple)) else para
        for run in runs:
            t, o = (run, {}) if isinstance(run, str) else run
            r = p.add_run()
            r.text = t
            r.font.size = Pt(o.get("size", size))
            r.font.bold = o.get("bold", bold)
            r.font.name = o.get("font", font)
            r.font.color.rgb = o.get("color", color)
    return shape


def boxed(slide, x, y, w, h, fill, paras, line=None, **kw):
    """Rectangle with text inside (one shape, so it animates as one)."""
    r = rect(slide, x, y, w, h, fill, line)
    kw.setdefault("anchor", MSO_ANCHOR.MIDDLE)
    text(slide, 0, 0, 0, 0, paras, shape=r, **kw)
    return r


def notes(slide, s):
    slide.notes_slide.notes_text_frame.text = s.strip()


def top_rule(slide, color=ORANGE):
    rect(slide, 0, 0, 13.333, 0.12, color)


def heading(slide, kicker, title, kcolor=ORANGE):
    top_rule(slide, kcolor)
    text(slide, 0.7, 0.45, 12, 0.4, kicker.upper(), size=14, color=kcolor, bold=True)
    return text(slide, 0.7, 0.8, 12, 1.0, title, size=36, font=HEAD, color=INK)


def section(prs, num, title, sub, bg=ORANGE, transition="push"):
    s = blank(prs, bg)
    n = text(s, 0.7, 1.2, 6, 2.4, num, size=150, font=HEAD, color=WHITE)
    bar = rect(s, 0.8, 3.9, 2.2, 0.1, INK)
    t = text(s, 0.7, 4.15, 11.5, 1.4, title, size=48, font=HEAD, color=WHITE)
    st = text(s, 0.7, 5.5, 11.5, 0.8, sub, size=22, color=INK, bold=True)
    set_transition(s, transition)
    anim_steps(s, [("auto", [(n, "zoom"), (bar, "wipe"), (t, "rise"), (st, "fade")])])
    return s


# ---------- shared slide layouts ----------
def closing(prs, items):
    s = blank(prs, INK)
    rect(s, 0, 0, 0.35, 7.5, ORANGE)
    t = text(s, 0.9, 1.0, 11, 1.2, "Before next week", size=54, font=HEAD, color=WHITE)
    hws = [text(s, 0.9, 2.6 + i * 1.15, 11.5, 1.1,
                [[(f"{i + 1}   ", {"color": ORANGE, "font": HEAD}), (a, {"bold": True})],
                 [("      " + b, {"color": CYAN, "size": 18})]], size=26, color=WHITE)
           for i, (a, b) in enumerate(items)]
    bye = text(s, 0.9, 6.3, 11, 0.7, "See you next week.  Build it. Ship it. Question it.",
               size=20, color=SLATE, bold=True)
    set_transition(s, "fade", "slow")
    anim_steps(s, [("auto", [(t, "rise")] + [(h, "rise") for h in hws] + [(bye, "fade")])],
               stagger=350)
    return s


def dark_list(prs, kicker, title, lines, title_size=60):
    s = blank(prs, INK)
    k = text(s, 0.8, 1.2, 11, 0.5, kicker, size=18, color=CYAN, bold=True)
    big = text(s, 0.8, 1.8, 11.8, 1.4, title, size=title_size, font=HEAD, color=WHITE)
    ck = [text(s, 0.8, 3.6 + i * 0.75, 11.5, 0.7, t, size=24, color=WHITE) for i, t in enumerate(lines)]
    set_transition(s, "zoom")
    anim_steps(s, [("auto", [(k, "fade"), (big, "rise")]), ("click", [(c, "rise") for c in ck])],
               stagger=300)
    return s


# ---------- transitions ----------
_P = "http://schemas.openxmlformats.org/presentationml/2006/main"
_TRANS = {
    "fade": '<p:fade/>',
    "push": '<p:push dir="u"/>',
    "wipe": '<p:wipe dir="r"/>',
    "cover": '<p:cover dir="l"/>',
    "zoom": '<p:zoom/>',
}


def set_transition(slide, kind="fade", speed="med"):
    xml = f'<p:transition xmlns:p="{_P}" spd="{speed}">{_TRANS[kind]}</p:transition>'
    el = etree.fromstring(xml)
    sld = slide._element
    # transition must come right after clrMapOvr (before timing)
    anchor = sld.find(f"{{{_P}}}clrMapOvr")
    anchor.addnext(el)


# ---------- entrance animations ----------
# effect name -> (presetID, presetSubtype, behaviour xml builder)
def _set_visible(cid, spid):
    return (f'<p:set><p:cBhvr><p:cTn id="{cid}" dur="1" fill="hold"><p:stCondLst>'
            f'<p:cond delay="0"/></p:stCondLst></p:cTn><p:tgtEl><p:spTgt spid="{spid}"/>'
            f'</p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName>'
            f'</p:attrNameLst></p:cBhvr><p:to><p:strVal val="visible"/></p:to></p:set>')


def _filter(cid, spid, flt, dur):
    return (f'<p:animEffect transition="in" filter="{flt}"><p:cBhvr><p:cTn id="{cid}" '
            f'dur="{dur}"/><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>')


def _prop(cid, spid, attr, frm, to, dur):
    return (f'<p:anim calcmode="lin" valueType="num"><p:cBhvr additive="base"><p:cTn id="{cid}" '
            f'dur="{dur}" fill="hold"/><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst>'
            f'<p:attrName>{attr}</p:attrName></p:attrNameLst></p:cBhvr><p:tavLst>'
            f'<p:tav tm="0"><p:val><p:strVal val="{frm}"/></p:val></p:tav>'
            f'<p:tav tm="100000"><p:val><p:strVal val="{to}"/></p:val></p:tav></p:tavLst></p:anim>')


EFFECTS = {
    # name: (presetID, subtype, list of behaviour builders, duration ms)
    "fade": (10, 0, lambda c, s: [_filter(c(), s, "fade", 500)]),
    "rise": (42, 0, lambda c, s: [_filter(c(), s, "fade", 600),
                                  _prop(c(), s, "ppt_x", "#ppt_x", "#ppt_x", 600),
                                  _prop(c(), s, "ppt_y", "#ppt_y+.1", "#ppt_y", 600)]),
    "wipe": (22, 8, lambda c, s: [_filter(c(), s, "wipe(left)", 600)]),
    "wipedown": (22, 1, lambda c, s: [_filter(c(), s, "wipe(up)", 500)]),
    "zoom": (53, 16, lambda c, s: [_prop(c(), s, "ppt_w", "0", "#ppt_w", 500),
                                   _prop(c(), s, "ppt_h", "0", "#ppt_h", 500),
                                   _filter(c(), s, "fade", 500)]),
}


def anim_steps(slide, steps, stagger=150):
    """steps: list of (trigger, [(shape, effect), ...]); trigger 'click' or 'auto'.
    'auto' is only allowed as the first step (plays when the slide appears)."""
    ids = iter(range(3, 10000))
    c = lambda: next(ids)
    groups, bld = [], []
    for si, (trigger, items) in enumerate(steps):
        assert trigger == "click" or si == 0, "auto only as first step"
        outer, inner = c(), c()
        effs = []
        for i, (shp, eff) in enumerate(items):
            pid, sub, build = EFFECTS[eff]
            spid = shp.shape_id
            ecid = c()
            node = ("clickEffect" if trigger == "click" else "afterEffect") if i == 0 else "withEffect"
            beh = _set_visible(c(), spid) + "".join(build(c, spid))
            effs.append(f'<p:par><p:cTn id="{ecid}" presetID="{pid}" presetClass="entr" '
                        f'presetSubtype="{sub}" fill="hold" grpId="0" nodeType="{node}">'
                        f'<p:stCondLst><p:cond delay="{i * stagger}"/></p:stCondLst>'
                        f'<p:childTnLst>{beh}</p:childTnLst></p:cTn></p:par>')
            if spid not in bld:
                bld.append(spid)
        start = ('<p:cond delay="indefinite"/>' if trigger == "click" else
                 '<p:cond delay="indefinite"/><p:cond evt="onBegin" delay="0"><p:tn val="2"/></p:cond>')
        groups.append(f'<p:par><p:cTn id="{outer}" fill="hold"><p:stCondLst>{start}</p:stCondLst>'
                      f'<p:childTnLst><p:par><p:cTn id="{inner}" fill="hold"><p:stCondLst>'
                      f'<p:cond delay="0"/></p:stCondLst><p:childTnLst>{"".join(effs)}'
                      f'</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par>')
    bldxml = "".join(f'<p:bldP spid="{s}" grpId="0" animBg="1"/>' for s in bld)
    xml = (f'<p:timing xmlns:p="{_P}"><p:tnLst><p:par><p:cTn id="1" dur="indefinite" '
           f'restart="never" nodeType="tmRoot"><p:childTnLst><p:seq concurrent="1" nextAc="seek">'
           f'<p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>{"".join(groups)}'
           f'</p:childTnLst></p:cTn><p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl>'
           f'<p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst><p:nextCondLst><p:cond evt="onNext" '
           f'delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst></p:seq>'
           f'</p:childTnLst></p:cTn></p:par></p:tnLst><p:bldLst>{bldxml}</p:bldLst></p:timing>')
    el = etree.fromstring(xml)
    sld = slide._element
    trans = sld.find(f"{{{_P}}}transition")
    (trans if trans is not None else sld.find(f"{{{_P}}}clrMapOvr")).addnext(el)
