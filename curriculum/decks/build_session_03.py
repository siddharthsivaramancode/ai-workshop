"""Session 3 deck: Build — make it work, then prove it.

Run from repo root:
    uv run --with python-pptx python curriculum/decks/build_session_03.py
Slide numbers match the run of show in curriculum/session-03-build.md.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from deckkit import *  # noqa: E402,F403

prs = new_deck()


def outline(slide, x, y, w, h, color, weight=3.5):
    """Hollow rectangle (for highlighting code lines)."""
    r = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    r.fill.background()
    r.line.color.rgb = color
    r.line.width = Pt(weight)
    r.shadow.inherit = False
    return r


CODE = ['let score = 0;',
        'const answers = ["B", "A", "C"];',
        '',
        'function check(choices) {',
        '  for (let i = 1; i < answers.length; i++) {',
        '    if (choices[i] = answers[i]) {',
        '      score++;',
        '    }',
        '  }',
        '  return score + " / " + answers.length;',
        '}']
FIXED = ['const answers = ["B", "A", "C"];',
         '',
         'function check(choices) {',
         '  let score = 0;',
         '  for (let i = 0; i < answers.length; i++) {',
         '    if (choices[i] === answers[i]) {',
         '      score++;',
         '    }',
         '  }',
         '  return score + " / " + answers.length;',
         '}']
CX, CY, LH = 0.7, 2.0, 0.42  # code box origin + line height (inches)


def code_box(slide, lines, w=8.0, size=19, numbered=True):
    rect(slide, CX, CY - 0.15, w, LH * len(lines) + 0.3, INK)
    shapes = []
    for i, ln in enumerate(lines):
        runs = []
        if numbered:
            runs.append((f"{i + 1:>2}  ", {"color": SLATE}))
        runs.append((ln or " ", {"color": WHITE}))
        shapes.append(text(slide, CX + 0.1, CY + i * LH - 0.04, w - 0.2, LH, [runs],
                           size=size, font=MONO, bold=True))
    return shapes


# 1 ─ Title ──────────────────────────────────────────────────────────────
s = blank(prs, INK)
rect(s, 0, 0, 0.35, 7.5, ORANGE)
k = text(s, 0.9, 0.8, 8, 0.5, "SESSION 3 OF 6  ·  BUILD", size=16, color=CYAN, bold=True)
l1 = text(s, 0.85, 1.6, 11, 1.5, "Make it work.", size=88, font=HEAD, color=WHITE)
l2 = text(s, 0.85, 3.1, 11.5, 1.5, "Then prove it.", size=88, font=HEAD, color=ORANGE)
sub = text(s, 0.9, 5.4, 11, 1.2,
           ["Today: hunt AI bugs, edit by hand, build your core feature.",
            ("Build it. Ship it. Question it.", {"color": CYAN, "size": 18})],
           size=24, color=WHITE, bold=True)
set_transition(s, "fade", "slow")
anim_steps(s, [("auto", [(k, "fade"), (l1, "rise"), (l2, "rise"), (sub, "fade")])], stagger=400)
notes(s, "Welcome back. Halfway point is today — by the end, your MUST feature should work.")

# 2 ─ Stand-up ──────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Stand-up · at your table · 1 sentence each", "Where are you?")
su = [("DONE", GREEN, "What works on your site right now?"),
      ("STUCK", RED, "What's blocking you?"),
      ("NEXT", CYAN, "What will you build today?")]
sc = [boxed(s, 0.7 + i * 4.1, 2.2, 3.8, 3.0, WHITE,
            [[(h, {"font": HEAD, "size": 40, "color": c})], "", [(q, {"size": 20, "bold": True})]],
            line=c, align=PP_ALIGN.CENTER)
      for i, (h, c, q) in enumerate(su)]
tip = boxed(s, 0.7, 5.6, 11.95, 1.0, INK, "Stuck is normal. Saying it out loud is how you get unstuck.",
            size=21, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(c, "rise") for c in sc]), ("click", [(tip, "wipe")])], stagger=200)
notes(s, """
Real software teams do this every morning. Keep it fast — under 1 minute per person.
Leaders: write down every STUCK so you know who to visit first during build time.
""")

# 3 ─ Section ───────────────────────────────────────────────────────────
s = section(prs, "01", "AI Checkpoint: Bug Bounty", "The AI says it works. Does it?")
notes(s, "Energy up — this one's a competition.")

# 4 ─ Setup ─────────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "The setup", "An AI wrote a quiz scorer.")
ask = boxed(s, 0.7, 2.0, 5.6, 1.5, WHITE,
            [[("Student: ", {"color": ORANGE}),
              "“Write a function that checks my 3-question quiz and returns the score.”"]],
            line=MIST, size=19, bold=True)
said = boxed(s, 6.9, 2.0, 5.75, 1.5, INK,
             [[("AI: ", {"color": CYAN}),
               "“Here you go! This function correctly checks every answer and returns the score.”"]],
             size=19, color=WHITE, bold=True)
mission = text(s, 0.7, 4.0, 12, 0.8, "Your mission: find the 3 bugs.", size=34, font=HEAD)
pts = [boxed(s, 0.7 + i * 4.1, 5.0, 3.8, 1.5, c, [[(p, {"font": HEAD, "size": 34})], d],
             size=16, color=WHITE if c != YELLOW else INK, bold=True, align=PP_ALIGN.CENTER)
       for i, (p, d, c) in enumerate([("1 pt", "easy to spot", CYAN), ("2 pts", "sneaky", ORANGE),
                                      ("3 pts", "only shows up later", RED)])]
set_transition(s, "fade")
anim_steps(s, [("auto", [(ask, "rise")]), ("click", [(said, "rise")]),
               ("click", [(mission, "wipe")]), ("click", [(p, "zoom") for p in pts])], stagger=200)
notes(s, """
Stress the AI's sentence: "correctly checks every answer." It sounds sure. Remember
Session 1: it predicts what SOUNDS right.
""")

# 5 ─ The code ──────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "With your partner · 7 minutes", "Find the bugs.", RED)
lines = code_box(s, CODE)
side = boxed(s, 9.1, 1.85, 3.55, 4.9, YELLOW,
             [[("What it should do:", {"font": HEAD, "size": 19})], "",
              "answers holds the correct answers.", "",
              "choices holds what the player picked.", "",
              "Return how many match, like “2 / 3”."],
             size=17, bold=True, anchor=MSO_ANCHOR.TOP)
set_transition(s, "wipe")
anim_steps(s, [("auto", [(ln, "wipe") for ln in lines]), ("click", [(side, "rise")])], stagger=120)
notes(s, """
Hand out the printed code. Pairs circle what they think is wrong and write WHY.
Start a 7-minute timer. You don't need to know JavaScript to find these — read it like
a puzzle. Use the hints slide if the room is stuck after 4 minutes.
""")

# 6 ─ Hints ─────────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Stuck? Hints", "One at a time.", RED)
hints = [("Hint 1", "Computers count from 0. Which question does the loop start at?", CYAN),
         ("Hint 2", "In JavaScript, =  sets a value.  ===  compares two values.", ORANGE),
         ("Hint 3", "Run check() twice in a row. What happens to the score?", RED)]
hc = [boxed(s, 0.7, 2.0 + i * 1.55, 11.95, 1.35, WHITE,
            [[(h + "   ", {"font": HEAD, "color": c}), (t, {"bold": True})]],
            line=c, size=22, anchor=MSO_ANCHOR.MIDDLE)
      for i, (h, t, c) in enumerate(hints)]
set_transition(s, "fade")
anim_steps(s, [("click", [(h, "rise")]) for h in hc])
notes(s, "Only click a hint when most pairs are stuck. Each hint lowers that bug's points by 1 if you want to be strict.")

# 7 ─ Reveal ────────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "The reveal", "Here's what was wrong.", RED)
code_box(s, CODE)
bugs = [(4, "1 pt", "Starts at 1, so question 1 is never checked.", CYAN),
        (5, "2 pts", "= sets instead of compares. Every answer counts as correct.", ORANGE),
        (0, "3 pts", "score lives outside, so it never resets. Check twice → 4 / 3.", RED)]
steps = []
for i, (ln, p, why, c) in enumerate(bugs):
    hl = outline(s, CX + 0.05, CY + ln * LH - 0.06, 7.9, LH + 0.02, c)
    lab = boxed(s, 9.1, 1.85 + i * 1.65, 3.55, 1.5, c,
                [[(p, {"font": HEAD, "size": 22})], why],
                size=15, color=WHITE, bold=True, anchor=MSO_ANCHOR.TOP)
    steps.append(("click", [(hl, "zoom"), (lab, "rise")]))
set_transition(s, "fade")
anim_steps(s, steps, stagger=200)
notes(s, """
One click per bug. After each, ask: who found it? Award points.
For bug 3, if possible demo it live in the browser console (see the session doc).
Notice: with the right answers B, A, C the function says "2 / 3" — close enough that a
quick glance might miss it. That's what makes AI bugs dangerous.
""")

# 8 ─ Fixed ─────────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "The fix", "Three tiny changes.", GREEN)
code_box(s, FIXED)
fixes = [(3, "score moved inside → resets every time"), (4, "start at 0"), (5, "=== compares")]
fsteps = []
for ln, t in fixes:
    hl = outline(s, CX + 0.05, CY + ln * LH - 0.06, 7.9, LH + 0.02, GREEN)
    fsteps.append(hl)
note = boxed(s, 9.1, 1.85, 3.55, 4.9, WHITE,
             [[("Fixed:", {"font": HEAD, "size": 22, "color": GREEN})], ""] +
             [[("✓ ", {"color": GREEN}), t] for _, t in fixes] +
             ["", [("Each fix is one line. Finding it was the hard part.", {"color": SLATE, "size": 15})]],
             line=GREEN, size=17, bold=True, anchor=MSO_ANCHOR.TOP)
set_transition(s, "fade")
anim_steps(s, [("click", [(h, "zoom") for h in fsteps] + [(note, "rise")])], stagger=250)
notes(s, "Point out: three bugs, three one-line fixes. Debugging is mostly FINDING, not fixing.")

# 9 ─ Lesson ────────────────────────────────────────────────────────────
s = blank(prs, INK)
k = text(s, 0.8, 1.0, 11, 0.5, "THE LESSON", size=18, color=CYAN, bold=True)
big = text(s, 0.8, 1.6, 11.8, 1.4, [["Looks right ", ("≠", {"color": ORANGE}), " works."]],
           size=56, font=HEAD, color=WHITE)
pts = [text(s, 0.8, 3.5 + i * 0.85, 11.6, 0.8, t, size=24, color=WHITE)
       for i, t in enumerate(["AI code can look clean and still be wrong.",
                              "The AI said it worked. It never actually ran it.",
                              "So you test it — like you're trying to break it."])]
set_transition(s, "zoom")
anim_steps(s, [("auto", [(k, "fade"), (big, "rise")]), ("click", [(p, "rise") for p in pts])],
           stagger=300)
notes(s, """
Chatbots usually don't run the code they write (agents like Claude Code can, which is
why they're better at this). Either way: you're the tester.
""")

# 10 ─ Section ──────────────────────────────────────────────────────────
s = section(prs, "02", "Hand first, AI second.", "Today you edit your own code before you ask for more.", bg=CYAN)
notes(s, "If you can change it by hand, you own it.")

# 11 ─ Three parts ──────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Your page has 3 parts", "HTML · CSS · JS", CYAN)
parts = [("HTML", "the skeleton", "what's on the page", '<button>Flip</button>', ORANGE),
         ("CSS", "the clothes", "how it looks", 'button { color: red; }', CYAN),
         ("JS", "the muscles", "what it does", 'button.onclick = flip;', YELLOW)]
pc = [boxed(s, 0.7 + i * 4.1, 2.0, 3.8, 4.6, WHITE,
            [[(n, {"font": HEAD, "size": 44, "color": c})], [(a, {"font": HEAD, "size": 22})],
             [(b, {"size": 18, "color": SLATE})], "", [(code, {"font": MONO, "size": 15})]],
            line=c, anchor=MSO_ANCHOR.TOP)
      for i, (n, a, b, code, c) in enumerate(parts)]
set_transition(s, "fade")
anim_steps(s, [("click", [(p, "rise")]) for p in pc])
notes(s, """
Want to change WHAT is on the page? HTML. HOW it looks? CSS. WHAT happens when you click?
JavaScript. Knowing which part to look in is half of editing by hand.
""")

# 12 ─ Find anything ────────────────────────────────────────────────────
s = blank(prs)
heading(s, "How to find anything in your code", "Search, don't scroll.", CYAN)
tools = [("⌘F  /  Ctrl+F", "Search for a word you can see on your page."),
         ("Read the comments", "Lines starting with // or <!-- are signposts."),
         ("Change → commit → refresh", "Make one change, then check it actually changed.")]
tc = [boxed(s, 0.7, 2.0 + i * 1.5, 11.95, 1.3, WHITE,
            [[(a + "     ", {"font": HEAD, "color": CYAN}), (b, {"bold": True})]],
            line=MIST, size=22, anchor=MSO_ANCHOR.MIDDLE)
      for i, (a, b) in enumerate(tools)]
set_transition(s, "fade")
anim_steps(s, [("click", [(t, "wipe")]) for t in tc])
notes(s, """
Quick demo: open someone's index.html, search for their page title text, change it,
commit, refresh the live site. Takes 60 seconds and makes it real.
""")

# 13 ─ Challenge ────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Challenge · before you ask the AI anything new", "3 edits. By hand.", ORANGE)
ch = [("Change a color", "Find it in the CSS."), ("Change some words", "Find them in the HTML."),
      ("Change a number", "A size, a time, a score, a speed.")]
cc = [boxed(s, 0.7 + i * 4.1, 2.1, 3.8, 3.2, [ORANGE, CYAN, YELLOW][i],
            [[(f"{i + 1}", {"font": HEAD, "size": 56})], [(a, {"font": HEAD, "size": 22})], b],
            size=17, bold=True, color=WHITE if i != 2 else INK, align=PP_ALIGN.CENTER)
      for i, (a, b) in enumerate(ch)]
show = boxed(s, 0.7, 5.65, 11.95, 1.0, INK, "Done? Show a leader the 3 changes live. Then build.",
             size=22, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(c, "zoom") for c in cc]), ("click", [(show, "wipe")])], stagger=250)
notes(s, "10 minutes max. Leaders check off each teen — that's a measurable win for the day.")

# 14 ─ Section ──────────────────────────────────────────────────────────
s = section(prs, "03", "Build your core feature.", "Your MUST. Working. Live. Today.")
notes(s, "~55 minutes of build time. Leaders start with the people who said STUCK at stand-up.")

# 15 ─ Test like a troublemaker ─────────────────────────────────────────
s = blank(prs)
heading(s, "Every time you add something", "Test like a troublemaker.")
tests = [("The normal way", "Does it do what it should?", GREEN),
         ("The weird way", "Empty box? Huge number? Click 10 times fast?", ORANGE),
         ("On a phone", "Does it fit? Can you tap it?", CYAN),
         ("Someone else", "Hand it to your partner. Don't explain. Watch.", RED)]
tc = [boxed(s, 0.7 + (i % 2) * 6.1, 2.0 + (i // 2) * 2.3, 5.85, 2.05, WHITE,
            [[(t, {"font": HEAD, "size": 26, "color": c})], [(d, {"size": 18, "color": SLATE})]],
            line=c, size=18, bold=True, anchor=MSO_ANCHOR.MIDDLE)
      for i, (t, d, c) in enumerate(tests)]
set_transition(s, "fade")
anim_steps(s, [("click", [(t, "rise")]) for t in tc])
notes(s, """
The quiz bug only showed up when you ran it twice — "the weird way." Real users do weird
things. Find the bugs before they do.
""")

# 16 ─ Good question ────────────────────────────────────────────────────
s = blank(prs)
heading(s, "When you do ask the AI", "Ask like a pro.")
bad = boxed(s, 0.7, 2.0, 4.4, 4.6, WHITE,
            [[("✗  Not this", {"font": HEAD, "color": RED, "size": 24})], "", "",
             [("“it doesn't work fix it”", {"font": MONO, "size": 20})]],
            line=RED, size=20, anchor=MSO_ANCHOR.TOP)
good = boxed(s, 5.45, 2.0, 7.2, 4.6, INK,
             [[("✓  This", {"font": HEAD, "color": GREEN, "size": 24})], "",
              "Here's my code for [feature].", "",
              "I expected: [what should happen]", "Instead: [what actually happens]",
              "I already tried: [what you tried]", "",
              "Explain what's wrong before you fix it."],
             size=18, font=MONO, color=WHITE, anchor=MSO_ANCHOR.TOP)
set_transition(s, "fade")
anim_steps(s, [("click", [(bad, "rise")]), ("click", [(good, "wipe")])])
notes(s, """
"Expected vs. instead" is how every professional bug report is written.
"Explain before you fix" keeps the AI in tutor mode — you learn why, not just what.
""")

# 17 ─ Commit + live ────────────────────────────────────────────────────
s = blank(prs, INK)
k = text(s, 0.8, 1.2, 11, 0.5, "LAST 10 MINUTES", size=18, color=CYAN, bold=True)
big = text(s, 0.8, 1.8, 11.8, 1.4, "Commit. Check. Write.", size=60, font=HEAD, color=WHITE)
ck = [text(s, 0.8, 3.6 + i * 0.75, 11.5, 0.7, t, size=24, color=WHITE)
      for i, t in enumerate(["Commit with a real message (“Add …”, “Fix …”).",
                             "Open your live URL on your phone. Test it the weird way.",
                             "Journal: one bug you found today, and how."])]
set_transition(s, "zoom")
anim_steps(s, [("auto", [(k, "fade"), (big, "rise")]), ("click", [(c, "rise") for c in ck])],
           stagger=300)
notes(s, "Leaders: record who has their MUST feature working + live.")

# 18 ─ Halfway ──────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Progress check", "You're halfway there.")
track = rect(s, 0.7, 3.0, 11.95, 0.5, MIST)
fill = rect(s, 0.7, 3.0, 5.975, 0.5, ORANGE)
lab = [text(s, 0.7 + i * 1.99, 3.65, 1.99, 0.5, f"Week {i + 1}", size=16, bold=True,
            color=ORANGE if i < 3 else SLATE, align=PP_ALIGN.CENTER) for i in range(6)]
now = boxed(s, 0.7, 4.6, 5.8, 1.9, WHITE,
            [[("Done", {"font": HEAD, "size": 24, "color": ORANGE})],
             "Live URL · a pitch · a MUST feature"], line=ORANGE, size=19, bold=True)
nxt = boxed(s, 6.85, 4.6, 5.8, 1.9, WHITE,
            [[("Next", {"font": HEAD, "size": 24, "color": CYAN})],
             "Debug · a NICE feature · polish · demo day"], line=CYAN, size=19, bold=True)
set_transition(s, "fade")
anim_steps(s, [("auto", [(fill, "wipe")] + [(l, "fade") for l in lab]),
               ("click", [(now, "rise"), (nxt, "rise")])], stagger=120)
notes(s, "Celebrate. If someone's MUST isn't working yet, that's next week's first job — not a failure.")

# 19 ─ Closing ──────────────────────────────────────────────────────────
s = blank(prs, INK)
rect(s, 0, 0, 0.35, 7.5, ORANGE)
t = text(s, 0.9, 1.0, 11, 1.2, "Before next week", size=54, font=HEAD, color=WHITE)
hw = [("1", "Get your MUST feature working.", "Smallest version is fine."),
      ("2", "Try to break your own site.", "Write down one bug — expected vs. instead."),
      ("3", "Next week: debugging + bias.", "Who does the AI imagine when it pictures “a programmer”?")]
hws = [text(s, 0.9, 2.6 + i * 1.15, 11.5, 1.1,
            [[(n + "   ", {"color": ORANGE, "font": HEAD}), (a, {"bold": True})],
             [("      " + b, {"color": CYAN, "size": 18})]], size=26, color=WHITE)
       for i, (n, a, b) in enumerate(hw)]
bye = text(s, 0.9, 6.3, 11, 0.7, "See you next week.  Build it. Ship it. Question it.",
           size=20, color=SLATE, bold=True)
set_transition(s, "fade", "slow")
anim_steps(s, [("auto", [(t, "rise")] + [(h, "rise") for h in hws] + [(bye, "fade")])],
           stagger=350)
notes(s, "Award bug bounty prizes on the way out.")

out = OUT_DIR / "session-03-build.pptx"
prs.save(out)
print("saved", out, "slides:", len(prs.slides))
