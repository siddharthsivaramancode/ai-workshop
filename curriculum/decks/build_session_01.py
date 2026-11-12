"""Session 1 deck: Kickoff — from zero to a live URL.

Run from repo root:
    uv run --with python-pptx python curriculum/decks/build_session_01.py
Slide numbers match the run of show in curriculum/session-01-kickoff.md.

Session 1 uses its own Keynote-style look (black / #F5F5F7 slides, rounded
hairline cards, one gradient phrase per slide), matching the browser presenter
in slideshows/session-01-kickoff.html. The tokens and helpers for that look live
in this file only, so the other sessions (which use deckkit's look) are unchanged.
Click steps (builds) match the HTML presenter one-for-one.

Layout is written in the HTML presenter's 1600x900 design units: px() converts
positions, and font sizes are given in the same units (x0.6 = points).
"""
import sys
from pathlib import Path

from lxml import etree
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.oxml.ns import qn
from pptx.util import Emu, Pt

sys.path.insert(0, str(Path(__file__).parent))
from deckkit import new_deck, blank, notes, set_transition, anim_steps, EFFECTS, OUT_DIR  # noqa: E402
from deckkit import _filter  # noqa: E402

# ---------- Session 1 tokens ----------
C = RGBColor.from_string
DARK = dict(bg=C("000000"), card=C("1D1D1F"), text=C("F5F5F7"), sec=C("86868B"), line=C("2C2C2E"),
            accent=C("2997FF"), red=C("FF453A"), green=C("30D158"), amber=C("FF9F0A"),
            grad=("4FA3FF", "9C6BFF", "F06BAA"))
LIGHT = dict(bg=C("F5F5F7"), card=C("FFFFFF"), text=C("1D1D1F"), sec=C("6E6E73"), line=C("E3E3E6"),
             accent=C("0066CC"), red=C("D70015"), green=C("248A3D"), amber=C("B25000"),
             grad=("0058C4", "6E3FD6", "C2306E"))
SILVER = ("FFFFFF", "A1A1A6")
INK = C("1D1D1F")
YELLOW = C("FFD60A")
REG, SEMI, MONO = "Segoe UI", "Segoe UI Semibold", "Consolas"
NATURAL_LINE = 1.33  # Segoe UI ascent+descent, in em: converts CSS line-height to PowerPoint "multiple"

X0, CW = 128, 1344  # content left edge and width (design units)
BODY_Y, BODY_B = 227, 780  # body top / bottom under a header

L, CTR, R = PP_ALIGN.LEFT, PP_ALIGN.CENTER, PP_ALIGN.RIGHT
TOP, MID, BOT = MSO_ANCHOR.TOP, MSO_ANCHOR.MIDDLE, MSO_ANCHOR.BOTTOM


def px(v):
    return Emu(int(round(v * 914400 / 120)))


# ---------- Session 1 animations (registered at runtime; deckkit.py is not modified) ----------
def _eased(cid, spid, attr, frm, to, dur):
    return (f'<p:anim calcmode="lin" valueType="num"><p:cBhvr additive="base"><p:cTn id="{cid}" '
            f'dur="{dur}" decel="100000" fill="hold"/><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl>'
            f'<p:attrNameLst><p:attrName>{attr}</p:attrName></p:attrNameLst></p:cBhvr><p:tavLst>'
            f'<p:tav tm="0"><p:val><p:strVal val="{frm}"/></p:val></p:tav>'
            f'<p:tav tm="100000"><p:val><p:strVal val="{to}"/></p:val></p:tav></p:tavLst></p:anim>')


# glide: fade in + rise 24 design units (headline build). settle: fade in + scale 0.96 -> 1 (card build).
EFFECTS["glide"] = (42, 0, lambda c, s: [_filter(c(), s, "fade", 900),
                                         _eased(c(), s, "ppt_x", "#ppt_x", "#ppt_x", 900),
                                         _eased(c(), s, "ppt_y", "#ppt_y+0.0267", "#ppt_y", 900)])
EFFECTS["settle"] = (53, 16, lambda c, s: [_eased(c(), s, "ppt_w", "#ppt_w*0.96", "#ppt_w", 800),
                                           _eased(c(), s, "ppt_h", "#ppt_h*0.96", "#ppt_h", 800),
                                           _filter(c(), s, "fade", 800)])


# ---------- helpers ----------
def _grad(run, stops, vertical=False):
    rPr = run._r.get_or_add_rPr()
    solid = rPr.find(qn("a:solidFill"))
    gs = "".join(f'<a:gs pos="{round(i * 100000 / (len(stops) - 1))}"><a:srgbClr val="{c}"/></a:gs>'
                 for i, c in enumerate(stops))
    el = etree.fromstring(
        f'<a:gradFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" rotWithShape="1">'
        f'<a:gsLst>{gs}</a:gsLst><a:lin ang="{5400000 if vertical else 0}" scaled="0"/></a:gradFill>')
    solid.addprevious(el)
    rPr.remove(solid)


def tx(slide, x, y, w, h, paras, th, size=24, color="text", weight="reg", align=L, anchor=TOP,
       line=1.4, track=0.0, pad=0, shape=None, wrap=True, font=None):
    """paras: str | list of paragraphs. A paragraph is str | list of runs | dict(runs=..., size, color,
    weight, track, line, before, align, hang). A run is str | (str, {size, color, weight, font, track, grad})."""
    if shape is None:
        shape = slide.shapes.add_textbox(px(x), px(y), px(w), px(h))
    tf = shape.text_frame
    tf.word_wrap = wrap
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.vertical_anchor = anchor
    pl, pt_, pr, pb = (pad,) * 4 if isinstance(pad, (int, float)) else (pad[0], pad[1], pad[0], pad[1])
    tf.margin_left, tf.margin_top, tf.margin_right, tf.margin_bottom = px(pl), px(pt_), px(pr), px(pb)
    if not isinstance(paras, list):
        paras = [paras]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        po = para if isinstance(para, dict) else {"runs": para}
        runs = po["runs"]
        if isinstance(runs, (str, tuple)):
            runs = [runs]
        psize = po.get("size", size)
        p.alignment = po.get("align", align)
        p.line_spacing = round(po.get("line", line) / NATURAL_LINE, 3)
        if po.get("before"):
            p.space_before = Pt(po["before"] * 0.6)
        if po.get("hang"):
            pPr = p._p.get_or_add_pPr()
            pPr.set("marL", str(px(po["hang"])))
            pPr.set("indent", str(-px(po["hang"])))
        if po.get("marl"):
            p._p.get_or_add_pPr().set("marL", str(px(po["marl"])))
        for run in runs:
            t, o = (run, {}) if isinstance(run, str) else run
            o = {**{k: po[k] for k in ("size", "color", "weight", "track", "font") if k in po}, **o}
            r = p.add_run()
            r.text = t
            sz = o.get("size", psize)
            r.font.size = Pt(sz * 0.6)
            wt = o.get("weight", weight)
            r.font.name = o.get("font") or font or (SEMI if wt == "semi" else REG)
            r.font.bold = wt == "bold"
            col = o.get("color", color)
            r.font.color.rgb = th[col] if isinstance(col, str) else col
            tr = o.get("track", track)
            if tr:
                r._r.get_or_add_rPr().set("spc", str(int(round(tr * sz * 0.6 * 100))))
            g = o.get("grad")
            if g == "silver":
                _grad(r, SILVER, vertical=True)
            elif g:
                _grad(r, g if isinstance(g, tuple) else th["grad"])
    return shape


def card(slide, x, y, w, h, th, paras=None, fill=None, border=True, pad=40, anchor=TOP, radius=24, **kw):
    """Rounded card with a 1px hairline; text lives inside the card so it builds as one shape."""
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px(x), px(y), px(w), px(h))
    shp.adjustments[0] = min(0.5, radius / min(w, h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill if fill is not None else th["card"]
    if border:
        shp.line.color.rgb = th["line"]
        shp.line.width = Pt(0.75)
    else:
        shp.line.fill.background()
    shp.shadow.inherit = False
    tx(slide, 0, 0, 0, 0, paras if paras is not None else "", th, shape=shp, pad=pad, anchor=anchor, **kw)
    return shp


def dot(slide, x, y, d, th, label, fill, color, line=None, size=30):
    shp = slide.shapes.add_shape(MSO_SHAPE.OVAL, px(x), px(y), px(d), px(d))
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = Pt(0.75)
    shp.shadow.inherit = False
    tx(slide, 0, 0, 0, 0, label, th, shape=shp, size=size, weight="semi", color=color, align=CTR,
       anchor=MID, line=1.0)
    return shp


def bar(slide, x, y, w, h, fill, rounded=True):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE,
                                 px(x), px(y), px(w), px(h))
    if rounded:
        shp.adjustments[0] = 0.5
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    shp.line.fill.background()
    shp.shadow.inherit = False
    return shp


def arrow(slide, x1, y1, x2, y2, color):
    cx = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, px(x1), px(y1), px(x2), px(y2))
    cx.line.color.rgb = color
    cx.line.width = Pt(1.25)
    ln = cx.line._get_or_add_ln()
    etree.SubElement(ln, qn("a:tailEnd"), type="arrow", w="med", len="med")
    return cx


def header(slide, th, kicker, title, kcolor="accent"):
    k = tx(slide, X0, 80, CW, 36, kicker, th, size=22, color=kcolor, weight="semi", line=1.2)
    t = tx(slide, X0, 114, CW, 90, title, th, size=60, weight="bold", track=-0.03, line=1.05)
    return k, t


def section(prs, num, title, sub, num_grad=True, sub_grad=False):
    th = DARK
    s = blank(prs, th["bg"])
    n = tx(s, X0, 352, CW, 240, [[(num, {"grad": "silver"} if num_grad else {"color": "sec"})]], th,
           size=220, weight="bold", track=-0.05, line=1.0)
    t = tx(s, X0, 598, CW, 120, title, th, size=96, weight="bold", track=-0.03, line=1.05)
    st = tx(s, X0, 722, CW, 58, [[(sub, {"grad": True, "weight": "semi"} if sub_grad else {})]], th,
            size=36, color="sec", track=-0.01, line=1.3)
    set_transition(s, "fade")
    anim_steps(s, [("auto", [(n, "glide"), (t, "glide"), (st, "glide")])], stagger=150)
    return s


prs = new_deck()

# 1 ─ Title ─────────────────────────────────────────────── dark · 1 build
th = DARK
s = blank(prs, th["bg"])
k = tx(s, X0, 126, CW, 36, "SESSION 1 OF 6  ·  KICKOFF", th, size=22, color="accent", weight="semi", line=1.2)
lines = []
for i, (t, g) in enumerate([("Build it.", False), ("Ship it.", True), ("Question it.", False)]):
    lines.append(tx(s, X0, 182 + i * 143, CW, 165, [[(t, {"grad": True} if g else {})]], th,
                    size=140, weight="bold", track=-0.035, line=1.02))
sub = tx(s, X0, 660, CW, 90,
         ["A free AI builder workshop for teens",
          {"runs": "Burch Library  ·  Collierville, TN", "size": 24, "color": "sec", "weight": "reg"}],
         th, size=30, weight="semi", line=1.4)
set_transition(s, "fade", "slow")
anim_steps(s, [("auto", [(k, "glide")] + [(ln_, "glide") for ln_ in lines] + [(sub, "glide")])], stagger=170)
notes(s, """
Welcome everyone in while people sit down. Let the title animate on its own.
"Welcome to Build it, Ship it, Question it. In six weeks every single one of you is
going to have a real website, live on the internet, that you built with AI —
and you'll know exactly where the AI messed up along the way."
""")

# 2 ─ Who we are ────────────────────────────────────────── light · 2 builds
th = LIGHT
s = blank(prs, th["bg"])
k, t = header(s, th, "Who's running this", "We're students too.")
cards = []
for x, w, role in [(128, 326, "LEADER"), (474, 326, "LEADER"), (820, 652, "ADULT SPONSOR")]:
    cards.append(card(s, x, BODY_Y, w, BODY_B - BODY_Y, th,
                      [{"runs": role, "size": 18, "weight": "semi", "color": "accent", "track": 0.06},
                       {"runs": "[Name]", "size": 48, "weight": "semi", "track": -0.03, "before": 14, "line": 1.2},
                       {"runs": "[Grade · school]", "color": "sec", "before": 6},
                       {"runs": "Something I built:", "color": "sec", "before": 250},
                       "[one line]"]))
set_transition(s, "fade")
anim_steps(s, [("auto", [(k, "glide"), (t, "glide")]), ("click", [(c, "settle") for c in cards])], stagger=60)
notes(s, """
Each of you: name, grade, and ONE thing you've built (with or without AI).
Adult sponsor introduces themselves and explains why they're here:
"Some of the tools we'll show, like Claude, are 18+. I'm the adult who runs those
demos and I'm here every week."
Fill in the [brackets] before the session.
""")

# 3 ─ Icebreaker ────────────────────────────────────────── dark · 2 builds
th = DARK
s = blank(prs, th["bg"])
q = tx(s, X0, 104, CW, 330,
       ["If you could build", [("ANY", {"grad": True}), " website…"], "what would it be?"],
       th, size=96, weight="bold", track=-0.035, line=1.04)
chips = [card(s, x, 666, w, 114, th, label, size=30, weight="semi", track=-0.01, anchor=MID, pad=(40, 0))
         for x, w, label in [(128, 362, "Your name"), (510, 362, "Grade + school"),
                             (892, 580, "Dream site in 5 words")]]
set_transition(s, "fade")
anim_steps(s, [("auto", [(q, "glide")]), ("click", [(c, "settle") for c in chips])], stagger=60)
notes(s, """
Go around the room, fast — 20 seconds each. Write a few of the dream sites on a
whiteboard or sticky notes; we'll come back to them in Session 2 when people pick projects.
""")

# 4 ─ Section ───────────────────────────────────────────── dark · 1 build
s = section(prs, "01", "What is AI, really?", "Spoiler: it's a very, very good guesser.")
notes(s, "Transition: before we use AI, let's figure out what it actually is.")

# 5 ─ Guess the next word ───────────────────────────────── light · 2 builds
th = LIGHT
s = blank(prs, th["bg"])
k, t = header(s, th, "Game", "Guess the next word.")
box = card(s, 128, BODY_Y, 882, BODY_B - BODY_Y, th)
sent = tx(s, 184, 300, 770, 270, "After school I grabbed a snack and turned on the", th,
          size=60, weight="semi", track=-0.03, line=1.12, anchor=BOT)
blank_line = bar(s, 184, 600, 230, 8, th["accent"])
shout = card(s, 1030, 654, 442, 126, th, "Shout it out!", size=44, weight="semi", track=-0.03,
             line=1.05, anchor=MID)
set_transition(s, "fade")
anim_steps(s, [("auto", [(k, "glide"), (t, "glide"), (box, "settle"), (sent, "glide"), (blank_line, "wipe")]),
               ("click", [(shout, "settle")])], stagger=110)
notes(s, """
Read the sentence out loud and pause. Let people shout guesses. Collect 4–5 answers.
Most people will say TV, Xbox/PlayStation, music… Nobody says "oven". Why? Because
you've seen thousands of sentences like this. Your brain predicted the next word.
""")

# 6 ─ Probability bars ──────────────────────────────────── light · 3 builds
th = LIGHT
s = blank(prs, th["bg"])
k, t = header(s, th, "That's literally what a chatbot does", "It ranks every possible next word.")
chart = card(s, 128, BODY_Y, 897, BODY_B - BODY_Y, th)
words = [("TV", 41), ("Xbox", 22), ("music", 15), ("lights", 12), ("PlayStation", 7), ("oven", 1)]
labels, bars = [], []
for i, (wd, pct) in enumerate(words):
    y = 330 + i * 54
    labels.append(tx(s, 150, y, 196, 40, wd, th, size=24, weight="semi", align=R, anchor=MID, line=1.2))
    bw = max(13, round(pct / 41 * 480))
    b = bar(s, 370, y + 7, bw, 26, th["accent"] if i == 0 else C("C7C7CC"))
    lab = tx(s, 370 + bw + 14, y, 90, 40, f"{pct}%", th, size=22, weight="semi", color="sec", anchor=MID, line=1.2)
    bars.append((b, lab))
foot = tx(s, 176, 652, 700, 30, "Numbers are made up to show the idea.", th, size=18, color="sec", line=1.3)
pick = card(s, 1045, 588, 427, 192, th, ["Then it picks one,", "adds it, and", "guesses again."],
            size=34, weight="semi", track=-0.02, line=1.1, anchor=MID)
set_transition(s, "fade")
anim_steps(s, [("auto", [(k, "glide"), (t, "glide"), (chart, "settle")] + [(x, "fade") for x in labels]
                + [(foot, "fade")]),
               ("click", [x for b, lab in bars for x in ((b, "wipe"), (lab, "fade"))]),
               ("click", [(pick, "settle")])], stagger=45)
notes(s, """
Click once: bars grow. "A chatbot gives every possible next word a score like this.
It picks one (usually a likely one, sometimes a surprising one), adds it to the
sentence, and does the whole thing again. Word by word. That's how it writes an essay,
a poem, or code."
Click again for the takeaway box.
""")

# 7 ─ Three steps ───────────────────────────────────────── dark · 5 builds
th = DARK
s = blank(prs, th["bg"])
k, t = header(s, th, "How a chatbot is made", "Three steps. No magic.")
steps = [("1", "Read", "a gigantic amount of text: websites, books, code."),
         ("2", "Learn patterns", "which words tend to follow which, in what situations."),
         ("3", "Predict", "the next word, one at a time, over and over.")]
cols = [card(s, 128 + i * 455, BODY_Y, 434, 410, th,
             [{"runs": n, "size": 96, "weight": "semi", "track": -0.04, "line": 1.0},
              {"runs": ti, "size": 34, "weight": "semi", "track": -0.02, "line": 1.1, "before": 18},
              {"runs": d, "size": 22, "color": "sec", "before": 10}])
        for i, (n, ti, d) in enumerate(steps)]
punch = card(s, 128, 657, CW, 123, th,
             [[("It predicts what ", {"color": "sec"}), ("sounds", {"weight": "bold"}),
               (" right — not what ", {"color": "sec"}), ("is", {"weight": "bold"}), (" right.", {"color": "sec"})]],
             size=46, track=-0.025, line=1.1, anchor=MID, pad=(48, 0))
set_transition(s, "fade")
anim_steps(s, [("auto", [(k, "glide"), (t, "glide")]), ("click", [(cols[0], "settle")]),
               ("click", [(cols[1], "settle")]), ("click", [(cols[2], "settle")]),
               ("click", [(punch, "settle")])], stagger=90)
notes(s, """
One click per step. Keep it short.
Last click is the most important sentence of today: "It predicts what SOUNDS right,
not what IS right." Ask them to remember it — we're going to prove it in 20 minutes.
""")

# 8 ─ Section ───────────────────────────────────────────── dark · 1 build
s = section(prs, "02", "Watch an AI build.", "One sentence in. A real website out.")
notes(s, "Hand off to the adult sponsor for the live demo.")

# 9 ─ Demo prompt ───────────────────────────────────────── light · 2 builds
th = LIGHT
s = blank(prs, th["bg"])
k, t = header(s, th, "Live demo · Claude Code", "What we're asking it to do")
term = card(s, 128, BODY_Y, 897, BODY_B - BODY_Y, th, fill=INK, border=False)
tdots = [dot(s, 152 + i * 21, 247, 12, th, "", C("48484A"), th["text"]) for i in range(3)]
rule = bar(s, 129, 279, 895, 1, C("2C2C2E"), rounded=False)
code = ["> claude",
        "Build a one-page website for our teen AI",
        "workshop. Include a countdown to demo day,",
        "the list of 6 sessions, and a button that",
        "shows a random fun fact about AI.",
        "Then publish it on GitHub Pages."]
tlines = [tx(s, 172, 312 + i * 44, 830, 44, ln_, th, size=25, font=MONO, line=1.6, wrap=False,
             color=DARK["accent"] if i == 0 else DARK["text"], weight="bold" if i == 0 else "reg")
          for i, ln_ in enumerate(code)]
call = card(s, 1045, BODY_Y, 427, BODY_B - BODY_Y, th,
            [{"runs": "Your job:", "size": 34, "weight": "semi", "track": -0.02, "line": 1.1},
             {"runs": "Call out changes!", "size": 26, "weight": "semi", "before": 26},
             {"runs": "“Dark mode.”", "size": 26, "color": "sec", "before": 6},
             {"runs": "“Add confetti.”", "size": 26, "color": "sec", "before": 6},
             {"runs": "“Make it purple.”", "size": 26, "color": "sec", "before": 6}])
set_transition(s, "fade")
anim_steps(s, [("auto", [(k, "glide"), (t, "glide"), (term, "settle")] + [(d, "fade") for d in tdots]
                + [(rule, "fade")] + [(x, "glide") for x in tlines]),
               ("click", [(call, "settle")])], stagger=110)
notes(s, """
ADULT SPONSOR runs this live from their own Claude account on the projector.
(Claude is 18+, so the teens don't log in to Claude themselves. Say this out loud.)
1. Type the prompt shown. Narrate what Claude is doing: planning, creating files, running.
2. Open the result. Take 2–3 change requests from the room and make them.
3. Push / publish so the room sees a real URL.
Keep it to ~12 minutes. If Wi-Fi fails: play the backup recording.
""")

# 10 ─ Agent loop ───────────────────────────────────────── light · 5 builds
th = LIGHT
s = blank(prs, th["bg"])
k, t = header(s, th, "What just happened?", "An AI agent works in a loop.")
NW, NH = 505, 228
pos = [(220, 227), (875, 227), (875, 551), (220, 551)]  # Plan, Write code, Run it, Spot a problem & fix
nodes = []
for i, (label, (x, y)) in enumerate(zip(["Plan", "Write code", "Run it", "Spot a problem & fix"], pos)):
    nodes.append(card(s, x, y, NW, NH, th, label, size=40, weight="semi", track=-0.025, anchor=MID,
                      pad=(44, 0), fill=INK if i == 0 else None, border=i != 0,
                      color=DARK["text"] if i == 0 else "text"))
arrows = [arrow(s, 749, 341, 851, 341, th["sec"]),     # Plan -> Write code
          arrow(s, 1127, 469, 1127, 537, th["sec"]),   # Write code -> Run it
          arrow(s, 851, 665, 749, 665, th["sec"]),     # Run it -> Spot a problem
          arrow(s, 472, 537, 472, 469, th["sec"])]     # Spot a problem -> Plan
set_transition(s, "fade")
anim_steps(s, [("auto", [(k, "glide"), (t, "glide")]),
               ("click", [(nodes[0], "settle")]),
               ("click", [(arrows[0], "fade"), (nodes[1], "settle")]),
               ("click", [(arrows[1], "fade"), (nodes[2], "settle")]),
               ("click", [(arrows[2], "fade"), (nodes[3], "settle"), (arrows[3], "fade")])], stagger=120)
notes(s, """
"A chatbot answers once. An agent like Claude Code keeps going: plans, writes code,
runs it, sees what broke, fixes it, repeats. That's why it could build a whole site."
"You'll use the same loop — except YOU are the one checking each step."
""")

# 11 ─ Section ──────────────────────────────────────────── dark · 1 build
s = section(prs, "03", "AI Checkpoint", "Confident ≠ Correct.", num_grad=False, sub_grad=True)
notes(s, "Every session has an AI Checkpoint. Today: catching the AI being confidently wrong.")

# 12 ─ Activity ─────────────────────────────────────────── light · 4 builds
th = LIGHT
s = blank(prs, th["bg"])
k, t = header(s, th, "With your partner · 8 minutes", "Ask your AI these. Then check.")
qs = ["What time does the Burch Library close on Saturdays?",
      "Who is the mayor of Collierville right now?",
      "What's the newest restaurant on the Town Square?"]
qcards = [card(s, 128, BODY_Y + i * 152, 934, 136, th,
               [[(f"Q{i + 1}", {"color": "accent", "weight": "bold"}), "   " + q]],
               size=26, weight="semi", track=-0.01, anchor=MID, pad=(36, 0))
          for i, q in enumerate(qs)]
score = card(s, 1082, BODY_Y, 390, 441, th,
             [{"runs": "Score each:", "size": 30, "weight": "semi", "line": 1.1},
              {"runs": [("✓", {"color": "green", "weight": "bold"}), " right"], "before": 26},
              {"runs": [("✗", {"color": "red", "weight": "bold"}), " wrong"], "before": 14},
              {"runs": [("?", {"color": "amber", "weight": "bold"}), " made up / can't tell"], "before": 14}],
             size=26)
check = card(s, 128, 688, CW, 92, th,
             [[("Check against:", {"weight": "semi"}), " the official website · a map app · a librarian"]],
             size=26, anchor=MID, pad=(40, 0))
set_transition(s, "fade")
anim_steps(s, [("auto", [(k, "glide"), (t, "glide")]), ("click", [(c, "settle") for c in qcards]),
               ("click", [(score, "settle")]), ("click", [(check, "settle")])], stagger=60)
notes(s, """
Pairs use ChatGPT (or whatever AI they're allowed to use). Timer: 8 minutes.
LEADERS: look up the real answers the day before from official sources, and
swap in fresher questions if these become too easy.
Debrief: hands up — who got at least one ✗ or ? ... Ask a pair to read out the most
confident wrong answer. Did the AI sound unsure? (Usually no.)
""")

# 13 ─ Why ──────────────────────────────────────────────── light · 4 builds
th = LIGHT
s = blank(prs, th["bg"])
k, t = header(s, th, "Why does that happen?", "Fluent is not the same as true.")
bubble = card(s, 128, BODY_Y, 644, 425, th,
              ["“Great question! The Burch Library is open until 9 PM on Saturdays, "
               "so you have plenty of time to visit.”"],
              size=30, track=-0.01, line=1.35, anchor=MID, pad=44)
stamp = card(s, 472, 556, 260, 62, th, "UNVERIFIED", size=30, weight="bold", color="red", track=0.08,
             align=CTR, anchor=MID, pad=(8, 0), radius=12, border=False)
stamp.line.color.rgb = th["red"]
stamp.line.width = Pt(1.8)
stamp.rotation = -6
reasons = [("It's guessing words,", "not looking things up (unless it searches)."),
           ("Its knowledge has a cutoff,", "so local + recent facts are weak."),
           ("It's trained to sound helpful,", "so it rarely says “I don't know.”")]
rs = [tx(s, 828, 300 + i * 104, 644, 90,
         [{"runs": a, "size": 28, "weight": "semi", "track": -0.015, "line": 1.3}, {"runs": b, "color": "sec"}],
         th, size=24, line=1.35)
      for i, (a, b) in enumerate(reasons)]
you = card(s, 128, 672, CW, 108, th,
           [["So ", ("you", {"grad": DARK["grad"]}), " are the fact-checker. Always."]],
           size=40, weight="semi", track=-0.025, anchor=MID, pad=(44, 0), fill=INK, border=False,
           color=DARK["text"])
set_transition(s, "fade")
anim_steps(s, [("auto", [(k, "glide"), (t, "glide"), (bubble, "settle")]), ("click", [(stamp, "settle")]),
               ("click", [(r, "glide") for r in rs]), ("click", [(you, "settle")])], stagger=90)
notes(s, """
The bubble is an example of a confident answer (we made it up for the slide — it's
the kind of thing AIs say). Click: stamp.
Then the three reasons. Connect back to slide 7: it predicts what SOUNDS right.
This is also why AI-written code can look perfect and still be broken.
""")

# 14 ─ Four habits ──────────────────────────────────────── dark · 5 builds
th = DARK
s = blank(prs, th["bg"])
k, t = header(s, th, "How we use AI here", [[("The 4 habits.", {"grad": "silver"})]])
habits = [("Explain-back", "No AI code goes in your project until you can explain it out loud."),
          ("Tutor mode", "Ask for hints and a plan first. Full code second."),
          ("Pair up", "The beginner types. The partner navigates. Leaders never grab your keyboard."),
          ("Prompt journal", "Write down what you asked, what came back, what broke.")]
geo = [(128, 227, 776), (924, 227, 548), (128, 513, 548), (696, 513, 776)]
hcards = []
for i, ((ti, d), (x, y, w)) in enumerate(zip(habits, geo)):
    lines_ = 1 if len(d) * 10.5 < min(w - 80, 560) else 2
    hcards.append(card(s, x, y, w, 267, th,
                       [{"runs": str(i + 1), "size": 22, "weight": "semi", "color": "sec"},
                        {"runs": ti, "size": 36, "weight": "semi", "track": -0.02, "line": 1.1,
                         "before": 92 if lines_ == 1 else 58},
                        {"runs": d, "size": 22, "color": "sec", "before": 10}],
                       pad=(40, 40)))
set_transition(s, "fade")
anim_steps(s, [("auto", [(k, "glide"), (t, "glide")])] + [("click", [(h, "settle")]) for h in hcards])
notes(s, """
One click per habit. These are the rules every week, not just today.
Why? Research on beginners using AI to code: the ones who let AI do everything end up
unable to fix or change their own project. The ones who use it like a tutor get better.
Hand out the printed habits card.
""")

# 15 ─ Safety ───────────────────────────────────────────── light · 3 builds
th = LIGHT
s = blank(prs, th["bg"])
k, t = header(s, th, "Non-negotiable · not in prompts, not on your site", "Never share these online.", "red")
items = ["Your full name", "Your school", "Your address", "Phone numbers", "Photos of people",
         "Passwords or keys"]
chips = [card(s, 128 + (i % 2) * 434, BODY_Y + (i // 2) * 191, 414, 171, th,
              [[("✗", {"color": "red", "weight": "bold"}), "   " + it]],
              size=27, weight="semi", track=-0.01, anchor=MID, pad=(32, 0))
         for i, it in enumerate(items)]
always = card(s, 996, BODY_Y, 476, BODY_B - BODY_Y, th,
              [[("And always:", {"color": YELLOW}), " an adult checks your site before you share the link."]],
              size=38, weight="semi", track=-0.025, line=1.15, anchor=BOT, pad=44, fill=INK, border=False,
              color=DARK["text"])
set_transition(s, "fade")
anim_steps(s, [("auto", [(k, "glide"), (t, "glide")]), ("click", [(c, "settle") for c in chips]),
               ("click", [(always, "settle")])], stagger=60)
notes(s, """
Use a nickname or first name only on your site. No sign-up forms, no collecting
other people's info. If you're not sure, ask a leader.
""")

# 16 ─ Section ──────────────────────────────────────────── dark · 1 build
s = section(prs, "04", "Your turn: ship a page.", "Goal: a live URL in 40 minutes.")
notes(s, "Energy up. Everyone opens their laptop now.")

# 17 ─ Steps ────────────────────────────────────────────── light · 6 builds
th = LIGHT
s = blank(prs, th["bg"])
k, t = header(s, th, "5 steps to live", "From nothing to on-the-internet.")
st = [("Log in", "github.com"),
      ("New repo", "name it my-first-site · Public"),
      ("Ask your AI", "for index.html (use tutor mode →)"),
      ("Add file", "Add file → Create new file → index.html → Commit"),
      ("Turn on Pages", "Settings → Pages → Deploy from branch: main")]
track = bar(s, 164, 434, 1098, 2, C("D9D9DC"), rounded=False)
sdots, slabels = [], []
for i, (ti, d) in enumerate(st):
    x = 128 + i * 274.4
    sdots.append(dot(s, x, 399, 72, th, str(i + 1), INK, DARK["text"]))
    slabels.append(tx(s, x, 501, 250, 180,
                      [{"runs": ti, "size": 30, "weight": "semi", "track": -0.02, "line": 1.1},
                       {"runs": d, "size": 22, "color": "sec", "before": 10}], th))
set_transition(s, "fade")
anim_steps(s, [("auto", [(k, "glide"), (t, "glide"), (track, "wipe")])] +
           [("click", [(d, "settle"), (lab, "glide")]) for d, lab in zip(sdots, slabels)], stagger=90)
notes(s, """
Walk through all five together, one click at a time, with the room following along.
Both leaders circulate. Remember: hands off the keyboard — point, don't type.
No GitHub account / no permission form? They pair with someone and watch today.
""")

# 18 ─ Tutor mode prompt ────────────────────────────────── light · 2 builds
th = LIGHT
s = blank(prs, th["bg"])
k, t = header(s, th, "Copy this into your AI first", "Tutor mode.")
p = card(s, 128, BODY_Y, 868, BODY_B - BODY_Y, th,
         [[(ln_, {"font": MONO})] if ln_ else [(" ", {"font": MONO})] for ln_ in
          ["I'm a beginner learning to code.",
           "Help me build a single index.html file.", "",
           "Before giving code, explain your plan",
           "in 3 short bullet points.",
           "Keep the code short, with a comment",
           "above each part explaining it.",
           "After the code, ask me one question",
           "to check I understand it."]],
         size=25, line=1.6, pad=(48, 44), fill=INK, border=False, color=DARK["text"])
first = card(s, 1016, BODY_Y, 456, BODY_B - BODY_Y, th,
             [{"runs": "Your first ask:", "size": 30, "weight": "semi", "track": -0.02, "line": 1.1},
              {"runs": "“Make a page that says Hi, I'm [first name], uses my favorite color, "
                       "and has one button that does something fun.”", "before": 22}],
             size=26, line=1.4)
set_transition(s, "fade")
anim_steps(s, [("auto", [(k, "glide"), (t, "glide"), (p, "settle")]), ("click", [(first, "settle")])], stagger=90)
notes(s, """
Put the tutor-mode text somewhere they can copy it (printed handout, or a shared link).
Before they paste the code into GitHub: explain-back to their partner. What does the
button do? Which part makes it that color?
""")

# 19 ─ Your URL ─────────────────────────────────────────── dark · 2 builds
th = DARK
s = blank(prs, th["bg"])
k = tx(s, X0, 190, CW, 36, "YOUR SITE LIVES HERE", th, size=22, color="accent", weight="semi", line=1.2)
url = card(s, 128, 236, CW, 148, th,
           [[("https://", {"color": "sec"}), ("YOUR-USERNAME", {"grad": True}), (".github.io/", {}),
             ("my-first-site", {"color": "accent"})]],
           size=50, weight="bold", font=MONO, track=-0.02, line=1.2, anchor=MID, pad=(48, 0))
tips, rules = [], []
for i, tip in enumerate(["Takes 1–2 minutes. Refresh.",
                         "Open it on your phone. Text it to someone.",
                         "Stuck? Backup: drag your folder onto app.netlify.com/drop"]):
    if i:
        rules.append(bar(s, 128, 436 + i * 78, CW, 1, C("1F1F1F"), rounded=False))
    tips.append(tx(s, X0, 436 + i * 78, CW, 78, tip, th, size=32, track=-0.01, line=1.3, anchor=MID))
set_transition(s, "fade")
anim_steps(s, [("auto", [(k, "glide"), (url, "settle")]),
               ("click", [(tips[0], "glide"), (rules[0], "fade"), (tips[1], "glide"), (rules[1], "fade"),
                          (tips[2], "glide")])], stagger=90)
notes(s, """
As people get live: have them type their URL into a shared doc / form so it can go
on the "wall of URLs" next.
""")

# 20 ─ Shipped ──────────────────────────────────────────── light · 4 builds
th = LIGHT
s = blank(prs, th["bg"])
k, t = header(s, th, "Wall of URLs  →  then:", "What “shipped” means here.", "green")
r1 = card(s, 128, BODY_Y, 761, BODY_B - BODY_Y, th,
          [{"runs": "1", "size": 96, "weight": "semi", "color": "sec", "track": -0.04, "line": 1.0},
           {"runs": "A public URL that loads on a phone", "size": 48, "weight": "semi", "track": -0.03,
            "line": 1.08, "before": 190},
           {"runs": "✓ done today", "size": 28, "weight": "semi", "color": "green", "before": 18}],
          pad=48)
rows = [r1]
for i, (c_, when) in enumerate([("At least one interactive thing that works", "weeks 2–4"),
                                ("A README: what the AI did, what you did", "week 5")]):
    rows.append(card(s, 909, BODY_Y + i * 286.5, 563, 266.5, th,
                     [{"runs": str(i + 2), "size": 22, "weight": "semi", "color": "sec"},
                      {"runs": c_, "size": 30, "weight": "semi", "track": -0.02, "line": 1.15, "before": 62},
                      {"runs": when, "size": 22, "weight": "semi", "color": "amber", "before": 8}]))
set_transition(s, "fade")
anim_steps(s, [("auto", [(k, "glide"), (t, "glide")])] + [("click", [(r, "settle")]) for r in rows])
notes(s, """
First: show the shared list of everyone's URLs on the projector and click a few. Cheer.
Then the three criteria. Today you hit #1. By demo day you'll hit all three.
""")

# 21 ─ Roadmap ──────────────────────────────────────────── light · 1 build
th = LIGHT
s = blank(prs, th["bg"])
k, t = header(s, th, "The next 6 weeks", "Where this is going.")
weeks = [("1", "Kickoff", "live URL"), ("2", "Idea + scope", "privacy"), ("3", "Build", "bug bounty"),
         ("4", "Build + debug", "bias"), ("5", "Polish + test", "who owns it?"),
         ("6", "DEMO DAY", "show the world")]
road = bar(s, 168, 470, 1137, 2, C("DBDBDE"), rounded=False)
wk = []
for i, (n, ti, cp) in enumerate(weeks):
    x = 128 + i * 227.3
    if i == 0:
        d = dot(s, x, 431, 80, th, n, INK, DARK["text"], size=32)
    elif i == 5:
        d = dot(s, x, 431, 80, th, n, th["accent"], C("FFFFFF"), size=32)
    else:
        d = dot(s, x, 431, 80, th, n, th["card"], th["text"], line=C("DBDBDE"), size=32)
    lab = tx(s, x, 541, 215, 120,
             [{"runs": [(ti, {"grad": True} if i == 5 else {})], "size": 26, "weight": "semi",
               "track": -0.02, "line": 1.2},
              {"runs": "checkpoint: " + cp, "size": 19, "color": "sec", "before": 8}], th)
    wk.append((d, lab))
set_transition(s, "fade")
anim_steps(s, [("auto", [(k, "glide"), (t, "glide"), (road, "wipe")] +
                [x for d, lab in wk for x in ((d, "settle"), (lab, "glide"))])], stagger=70)
notes(s, """
Point at Demo Day: parents, library staff, and guests will see what you built.
Each week also has an AI Checkpoint like today's.
""")

# 22 ─ Closing ──────────────────────────────────────────── dark · 1 build
th = DARK
s = blank(prs, th["bg"])
t = tx(s, X0, 146, CW, 120, [[("Before next week", {"grad": "silver"})]], th, size=96, weight="bold",
       track=-0.035, line=1.05)
hw = [("1", "Bring 3 project ideas.", "What would you actually use, or show off?"),
      ("2", "Journal: one thing the AI got wrong today.", "Be specific."),
      ("3", "Show your site to one person.", "Parent, friend, sibling.")]
hws = [tx(s, X0, 308 + i * 111, CW, 100,
          [{"runs": [(n, {"color": "sec", "size": 34}), "\t" + a], "hang": 56, "size": 36, "weight": "semi",
            "track": -0.02, "line": 1.2},
           {"runs": b, "size": 24, "color": "sec", "marl": 56, "before": 4}], th)
       for i, (n, a, b) in enumerate(hw)]
bye = tx(s, X0, 648, CW, 44, "See you next week.  Build it. Ship it. Question it.", th, size=24,
         weight="semi", color="sec", line=1.3)
set_transition(s, "fade", "slow")
anim_steps(s, [("auto", [(t, "glide")] + [(h, "glide") for h in hws] + [(bye, "glide")])], stagger=180)
notes(s, """
Hand out prompt-journal sheets; 3 minutes to write the first entry before leaving.
Exit ticket (optional): one word for how today felt.
""")

out = OUT_DIR / "session-01-kickoff.pptx"
prs.save(out)
print("saved", out, "slides:", len(prs.slides))
