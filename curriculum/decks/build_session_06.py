"""Session 6 deck: Demo Day — built it, shipped it, questioned it.

FILL IN the three blocks below the night before, then run from repo root:
    uv run --with python-pptx python curriculum/decks/build_session_06.py
Produces session-06-demo-day.pptx and session-06-certificates.pptx.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from deckkit import *  # noqa: E402,F403

# ═══ FILL THESE IN ═══════════════════════════════════════════════════════
# First names only (privacy). In demo order.
DEMOS = [
    ("[First name]", "[Project title]"),
    ("[First name]", "[Project title]"),
    ("[First name]", "[Project title]"),
]
STATS = {"teens": "[#]", "sites": "[#]", "mistakes": "[#]"}
# Best "AI got it wrong" moments from journals (ask permission; no names).
AI_FAILS = [
    ("[What the AI said or did]", "[What was actually true / how they caught it]"),
    ("[What the AI said or did]", "[What was actually true / how they caught it]"),
    ("[What the AI said or did]", "[What was actually true / how they caught it]"),
]
EVENT = "Burch Library  ·  Collierville, TN  ·  [Date]"
SIGNERS = ["Workshop leader", "Workshop leader", "Adult sponsor"]
# ═════════════════════════════════════════════════════════════════════════

prs = new_deck()

# 1 ─ Title ──────────────────────────────────────────────────────────────
s = blank(prs, INK)
rect(s, 0, 0, 0.35, 7.5, ORANGE)
k = text(s, 0.9, 0.8, 8, 0.5, "SESSION 6 OF 6  ·  DEMO DAY", size=16, color=CYAN, bold=True)
l1 = text(s, 0.85, 1.5, 11, 1.4, "Built it.", size=88, font=HEAD, color=WHITE)
l2 = text(s, 0.85, 2.75, 11, 1.4, "Shipped it.", size=88, font=HEAD, color=ORANGE)
l3 = text(s, 0.85, 4.0, 11.5, 1.4, "Questioned it.", size=88, font=HEAD, color=WHITE)
sub = text(s, 0.9, 5.75, 11, 1.0,
           ["A free AI builder workshop for teens", (EVENT, {"color": CYAN, "size": 20})],
           size=24, color=WHITE, bold=True)
set_transition(s, "fade", "slow")
anim_steps(s, [("auto", [(k, "fade"), (l1, "rise"), (l2, "rise"), (l3, "rise"), (sub, "fade")])],
           stagger=350)
notes(s, """
Leave this up while guests arrive. Remind the room: same title as Week 1 —
but now it's past tense.
""")

# 2 ─ Welcome ───────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Welcome, families & friends", "Six weeks. Zero to live.")
what = [("Every teen built a real website", "with AI help — and it's live right now.", ORANGE),
        ("Every teen caught the AI being wrong", "and you'll hear exactly how.", CYAN),
        ("You can try every site", "on your phone, after the demos.", GREEN)]
wc = [boxed(s, 0.7, 2.25 + i * 1.45, 11.95, 1.25, WHITE,
            [[(a, {"font": HEAD, "color": c}), ("  " + b, {"size": 19, "color": SLATE})]],
            line=c, size=23, bold=True, anchor=MSO_ANCHOR.MIDDLE)
      for i, (a, b, c) in enumerate(what)]
set_transition(s, "fade")
anim_steps(s, [("click", [(w, "rise")]) for w in wc])
notes(s, "Leaders introduce themselves in one line each. Thank everyone for coming.")

# 3 ─ What we did ───────────────────────────────────────────────────────
s = blank(prs)
heading(s, "What we did", "Six weeks, six steps.")
weeks = [("Kickoff", "a live URL"), ("Idea + scope", "privacy"), ("Build", "bug bounty"),
         ("Debug", "bias"), ("Polish + test", "who owns it?"), ("Demo Day", "today!")]
track = rect(s, 1.2, 3.35, 10.9, 0.1, INK)
wk = []
for i, (t, cp) in enumerate(weeks):
    x = 0.75 + i * 2.1
    last = i == 5
    d = rect(s, x + 0.35, 2.85, 1.1, 1.1, ORANGE if last else GREEN, shape=MSO_SHAPE.OVAL)
    text(s, 0, 0, 0, 0, "★" if last else "✓", shape=d, size=30, font=HEAD, align=PP_ALIGN.CENTER,
         anchor=MSO_ANCHOR.MIDDLE, color=WHITE)
    lab = text(s, x - 0.1, 4.15, 2.0, 1.6,
               [[(t, {"font": HEAD, "size": 19, "color": ORANGE if last else INK})],
                [(("AI checkpoint: " if not last else "") + cp, {"size": 14, "color": SLATE})]],
               size=19, align=PP_ALIGN.CENTER)
    wk.append((d, lab))
set_transition(s, "fade")
anim_steps(s, [("auto", [(track, "wipe")] + [x for d, l in wk for x in ((d, "zoom"), (l, "fade"))])],
           stagger=180)
notes(s, """
Every week paired building with an "AI Checkpoint" — a hands-on activity about
how AI fails: made-up facts, privacy, buggy code, bias, and who owns AI work.
""")

# 4 ─ By the numbers ────────────────────────────────────────────────────
s = blank(prs, INK)
k = text(s, 0.8, 0.9, 11, 0.5, "BY THE NUMBERS", size=18, color=CYAN, bold=True)
nums = [(STATS["teens"], "teen builders", ORANGE), (STATS["sites"], "live websites", CYAN),
        (STATS["mistakes"], "AI mistakes caught", YELLOW)]
nc = [text(s, 0.8 + i * 4.1, 1.9, 3.8, 4.0,
           [[(n, {"size": 96, "font": HEAD, "color": c})], [(l, {"size": 24, "bold": True})]],
           color=WHITE, align=PP_ALIGN.CENTER)
      for i, (n, l, c) in enumerate(nums)]
set_transition(s, "zoom")
anim_steps(s, [("auto", [(k, "fade")])] + [("click", [(n, "zoom")]) for n in nc], stagger=200)
notes(s, "Fill in STATS in build_session_06.py. 'AI mistakes caught' = count from prompt journals.")

# 5 ─ How we used AI ────────────────────────────────────────────────────
s = blank(prs)
heading(s, "How we used AI", "Tutor, not ghostwriter.")
habits = [("Explain-back", "No AI code went in unless the builder could explain it."),
          ("Tutor mode", "Hints and plans first. Full code second."),
          ("Pair up", "The beginner typed. Leaders never took the keyboard."),
          ("Prompt journal", "What we asked, what came back, what broke.")]
hc = [boxed(s, 0.7 + (i % 2) * 6.1, 2.05 + (i // 2) * 2.3, 5.85, 2.05, WHITE,
            [[(f"{i + 1}  ", {"color": [ORANGE, CYAN, YELLOW, INK][i]}), t],
             [(d, {"font": BODY, "size": 18, "color": SLATE, "bold": False})]],
            line=MIST, size=28, font=HEAD, anchor=MSO_ANCHOR.MIDDLE)
      for i, (t, d) in enumerate(habits)]
set_transition(s, "fade")
anim_steps(s, [("click", [(h, "rise") for h in hc])], stagger=250)
notes(s, "For parents: this is why your teen can explain what they built — not just show it.")

# 6 ─ How demos work ────────────────────────────────────────────────────
s = blank(prs)
heading(s, "How demos work · 3 minutes each", "Every demo has 4 parts.")
parts = [("Pitch", "one sentence", ORANGE), ("Show it", "live", CYAN),
         ("AI got it wrong", "one real example", RED), ("What's next", "the Someday list", GREEN)]
widths = [2.3, 4.4, 2.95, 2.4]
pc, x = [], 0.7
for (a, b, c), w in zip(parts, widths):
    pc.append(boxed(s, x, 2.1, w - 0.1, 2.2, c, [[(a, {"font": HEAD, "size": 22})], "", [(b, {"size": 17})]],
                    color=WHITE, bold=True, align=PP_ALIGN.CENTER))
    x += w
aud = boxed(s, 0.7, 4.75, 11.95, 1.85, INK,
            [[("Audience: ", {"color": YELLOW}), "cheer loud. The “AI got it wrong” part is our favorite."],
             [("Want to try a site? ", {"color": CYAN}), "Every builder will have it open after the demos."]],
            size=21, color=WHITE, bold=True, anchor=MSO_ANCHOR.MIDDLE)
set_transition(s, "fade")
anim_steps(s, [("click", [(p, "rise") for p in pc]), ("click", [(aud, "wipe")])], stagger=250)
notes(s, "Then hand off to the first presenter.")

# 7 ─ Section ───────────────────────────────────────────────────────────
s = section(prs, "▶", "Demos.", f"{len(DEMOS)} builders. 3 minutes each.", bg=ORANGE)
notes(s, "Leader A emcees. Leader B runs the timer and fills in the rubric quietly.")

# 8.. ─ One slide per demo ─────────────────────────────────────────────
half = len(DEMOS) // 2 if len(DEMOS) > 10 else None
for i, (name, proj) in enumerate(DEMOS):
    if half is not None and i == half:
        s = blank(prs, CYAN)
        b = text(s, 0.8, 2.3, 11.8, 2.0, ["2-minute stretch.", "Back in a sec."], size=64, font=HEAD,
                 color=WHITE, spacing=0.95)
        set_transition(s, "push")
        anim_steps(s, [("auto", [(b, "rise")])])
        notes(s, "Halfway break (only appears with more than 10 demos).")
    s = blank(prs, INK)
    rect(s, 0, 0, 0.35, 7.5, [ORANGE, CYAN, YELLOW, GREEN][i % 4])
    k = text(s, 0.9, 1.0, 11, 0.5, f"NOW PRESENTING  ·  {i + 1} OF {len(DEMOS)}", size=18, color=CYAN, bold=True)
    nm = text(s, 0.85, 1.7, 11.5, 1.6, name, size=80, font=HEAD, color=WHITE)
    pj = text(s, 0.9, 3.4, 11.5, 1.2, proj, size=36, bold=True, color=ORANGE)
    legend = text(s, 0.9, 6.2, 11.5, 0.6,
                  [[("Pitch", {"color": ORANGE}), "  →  ", ("Show it", {"color": CYAN}), "  →  ",
                    ("AI got it wrong", {"color": RED}), "  →  ", ("What's next", {"color": GREEN})]],
                  size=20, bold=True, color=SLATE)
    set_transition(s, "push")
    anim_steps(s, [("auto", [(k, "fade"), (nm, "rise"), (pj, "rise"), (legend, "fade")])], stagger=250)
    notes(s, f"""
{name} — {proj}. Switch to their browser tab. Start the 3:00 timer.
At 2:30 give the "wrap up" signal. Lead the applause.
Rubric (Leader B): URL works? interactive feature? explains a feature (0-2)? names a specific AI error (0-2)?
""")

# ─ Highlight reel ──────────────────────────────────────────────────────
s = section(prs, "★", "The AI got it wrong.", "Our favorite catches from six weeks of journals.", bg=RED)
notes(s, "Leader B reads these out. Fill AI_FAILS in the build script. Ask teens' permission; no names.")
s = blank(prs)
heading(s, "Highlight reel", "Caught it.", RED)
fc = [boxed(s, 0.7, 2.0 + i * 1.55, 11.95, 1.35, WHITE,
            [[("The AI: ", {"color": RED, "font": HEAD}), a],
             [("Actually: ", {"color": GREEN, "font": HEAD}), (b, {"color": SLATE})]],
            line=MIST, size=20, bold=True, anchor=MSO_ANCHOR.MIDDLE)
      for i, (a, b) in enumerate(AI_FAILS)]
set_transition(s, "fade")
anim_steps(s, [("click", [(f, "wipe")]) for f in fc])
notes(s, "This is the 'Question it' part of the workshop, made visible. Pause after each for laughs.")

# ─ Thank you ───────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Thank you", "This happened because of…")
th = [("Burch Library", "for hosting us", CYAN), ("[Adult sponsor]", "for being in the room every week", ORANGE),
      ("Families", "for the permission slips and the rides", GREEN), ("[Other supporters]", "[for what]", YELLOW)]
tc = [boxed(s, 0.7 + (i % 2) * 6.1, 2.05 + (i // 2) * 2.3, 5.85, 2.05, WHITE,
            [[(a, {"font": HEAD, "size": 26, "color": c})], [(b, {"size": 18, "color": SLATE})]],
            line=c, bold=True, align=PP_ALIGN.CENTER)
      for i, (a, b, c) in enumerate(th)]
set_transition(s, "fade")
anim_steps(s, [("click", [(t, "rise")]) for t in tc])
notes(s, "Fill in the brackets. Invite library staff / the sponsor to say a few words if they'd like.")

# ─ Certificates ────────────────────────────────────────────────────────
s = blank(prs, GREEN)
b = text(s, 0.8, 1.4, 11.8, 3.2, ["Shipped.", [("Every one of you.", {"color": INK, "size": 54})]], size=80, font=HEAD,
         color=WHITE, spacing=0.95)
c = text(s, 0.8, 5.0, 11.8, 1.0, "Come up when you hear your name.", size=28, bold=True, color=INK)
set_transition(s, "zoom")
anim_steps(s, [("auto", [(b, "zoom")]), ("click", [(c, "rise")])])
notes(s, "Read names in demo order. Hand certificates. Photos only for teens with a signed photo release.")

# ─ Survey + gallery ────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Last 12 minutes", "Two things at once.", CYAN)
teen = boxed(s, 0.7, 2.0, 5.85, 4.6, INK,
             [[("BUILDERS", {"font": HEAD, "size": 26, "color": YELLOW})], "",
              "Fill out the exit survey.", "", "Anonymous. 3 minutes.", "Be honest — it makes next time better."],
             size=21, color=WHITE, bold=True, anchor=MSO_ANCHOR.TOP)
guests = boxed(s, 6.8, 2.0, 5.85, 4.6, WHITE,
               [[("GUESTS", {"font": HEAD, "size": 26, "color": CYAN})], "",
                "Walk around and try the sites.", "", "Ask a builder:",
                [("“What did the AI get wrong?”", {"color": ORANGE})]],
               line=CYAN, size=21, bold=True, anchor=MSO_ANCHOR.TOP)
set_transition(s, "fade")
anim_steps(s, [("click", [(teen, "rise")]), ("click", [(guests, "rise")])])
notes(s, "Hand out paper surveys or show the form link. Builders open their laptops for the gallery walk after.")

# ─ What's next ─────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "For the builders", "What's next?")
nx = [("Keep building", "Your GitHub and your site are yours. Add your Someday list.", ORANGE),
      ("Hack Club", "A community of teen coders, with programs that reward shipping projects.", CYAN),
      ("CodeCrew", "Memphis's youth coding nonprofit: classes, camps, hackathons.", GREEN),
      ("Come back as a mentor", "Help run the next season. Volunteer hours included.", YELLOW)]
nc = [boxed(s, 0.7 + (i % 2) * 6.1, 2.05 + (i // 2) * 2.3, 5.85, 2.05, WHITE,
            [[(a, {"font": HEAD, "size": 24, "color": c})], [(b, {"size": 17, "color": SLATE})]],
            line=c, bold=True, anchor=MSO_ANCHOR.MIDDLE)
      for i, (a, b, c) in enumerate(nx)]
set_transition(s, "fade")
anim_steps(s, [("click", [(n, "rise")]) for n in nc])
notes(s, "hackclub.com · codecrew.us — check both links before the event and put them on the handout.")

# ─ Closing ─────────────────────────────────────────────────────────────
s = blank(prs, INK)
rect(s, 0, 0, 0.35, 7.5, ORANGE)
l1 = text(s, 0.85, 1.2, 11, 1.4, "Built it.", size=80, font=HEAD, color=WHITE)
l2 = text(s, 0.85, 2.4, 11, 1.4, "Shipped it.", size=80, font=HEAD, color=ORANGE)
l3 = text(s, 0.85, 3.6, 11.5, 1.4, "Questioned it.", size=80, font=HEAD, color=WHITE)
ty = text(s, 0.9, 5.5, 11, 1.0, [["Thank you for coming.", ("   See you next season.", {"color": CYAN})]],
          size=26, bold=True, color=WHITE)
set_transition(s, "fade", "slow")
anim_steps(s, [("auto", [(l1, "rise"), (l2, "rise"), (l3, "rise"), (ty, "fade")])], stagger=400)
notes(s, "Leave this up during the gallery walk.")

out = Path(__file__).parent / "session-06-demo-day.pptx"
prs.save(out)
print("saved", out, "slides:", len(prs.slides))

# ═══ Certificates (one page per builder) ═════════════════════════════════
cert = new_deck()
for name, proj in DEMOS:
    s = blank(cert, WHITE)
    rect(s, 0.3, 0.3, 12.733, 6.9, WHITE, ORANGE)
    rect(s, 0.3, 0.3, 12.733, 0.25, ORANGE)
    text(s, 0.8, 1.0, 11.7, 0.5, "BUILD IT · SHIP IT · QUESTION IT", size=18, color=CYAN, bold=True,
         align=PP_ALIGN.CENTER)
    text(s, 0.8, 1.6, 11.7, 0.9, "Certificate of Shipping", size=44, font=HEAD, align=PP_ALIGN.CENTER)
    text(s, 0.8, 2.6, 11.7, 0.5, "This certifies that", size=20, color=SLATE, align=PP_ALIGN.CENTER)
    text(s, 0.8, 3.1, 11.7, 1.0, name, size=54, font=HEAD, color=ORANGE, align=PP_ALIGN.CENTER)
    text(s, 0.8, 4.2, 11.7, 0.9,
         ["built and shipped a live website with AI as a tutor —", [("and caught the AI being wrong.", {"bold": True})]],
         size=20, color=INK, align=PP_ALIGN.CENTER)
    text(s, 0.8, 5.05, 11.7, 0.5, f"Project: {proj}", size=18, color=SLATE, bold=True, align=PP_ALIGN.CENTER)
    for j, who in enumerate(SIGNERS):
        x = 1.2 + j * 3.9
        rect(s, x, 6.25, 3.2, 0.03, INK)
        text(s, x, 6.32, 3.2, 0.4, who, size=13, color=SLATE, align=PP_ALIGN.CENTER)
    text(s, 0.8, 5.5, 11.7, 0.5, EVENT, size=14, color=SLATE, align=PP_ALIGN.CENTER)
cout = Path(__file__).parent / "session-06-certificates.pptx"
cert.save(cout)
print("saved", cout, "pages:", len(cert.slides))
