"""Session 2 deck: Idea and scope — big idea, small start.

Run from repo root:
    uv run --with python-pptx python curriculum/decks/build_session_02.py
Slide numbers match the run of show in curriculum/session-02-idea-and-scope.md.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from deckkit import *  # noqa: E402,F403

prs = new_deck()

# 1 ─ Title ──────────────────────────────────────────────────────────────
s = blank(prs, INK)
rect(s, 0, 0, 0.35, 7.5, ORANGE)
k = text(s, 0.9, 0.8, 8, 0.5, "SESSION 2 OF 6  ·  IDEA + SCOPE", size=16, color=CYAN, bold=True)
l1 = text(s, 0.85, 1.6, 11, 1.5, "Big idea.", size=88, font=HEAD, color=WHITE)
l2 = text(s, 0.85, 3.1, 11, 1.5, "Small start.", size=88, font=HEAD, color=ORANGE)
sub = text(s, 0.9, 5.4, 11, 1.2,
           ["Today: pick it, pitch it, scope it, build the first piece.",
            ("Build it. Ship it. Question it.", {"color": CYAN, "size": 18})],
           size=24, color=WHITE, bold=True)
set_transition(s, "fade", "slow")
anim_steps(s, [("auto", [(k, "fade"), (l1, "rise"), (l2, "rise"), (sub, "fade")])], stagger=400)
notes(s, """
Welcome back. Quick headcount. If anyone is new or doesn't have a live URL from
last week, a junior mentor helps them for the first 10 minutes.
""")

# 2 ─ Show & tell ───────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Show & tell · 10 minutes", "Show us what you shipped.")
prompts = [("1", "Open your URL", "on the projector (or hold up your phone)."),
           ("2", "One thing you changed", "after the AI gave you code."),
           ("3", "One thing the AI got wrong", "— read it from your journal.")]
pc = [boxed(s, 0.7 + i * 4.1, 2.3, 3.8, 3.2, WHITE,
            [[(n, {"size": 54, "font": HEAD, "color": [ORANGE, CYAN, YELLOW][i]})],
             [(t, {"size": 23, "font": HEAD})], [(d, {"size": 17, "color": SLATE})]],
            line=MIST, anchor=MSO_ANCHOR.TOP)
      for i, (n, t, d) in enumerate(prompts)]
clap = boxed(s, 0.7, 5.85, 11.95, 0.85, INK, "Everyone who shipped last week: you're already ahead of most adults.",
             size=20, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(c, "rise") for c in pc]), ("click", [(clap, "wipe")])], stagger=200)
notes(s, """
3–4 volunteers, about 2 minutes each. Celebrate every one.
Prompt 3 is the important one: we want "the AI got it wrong" to feel normal and
even cool to catch. Keep it light.
""")

# 3 ─ Section ───────────────────────────────────────────────────────────
s = section(prs, "01", "AI Checkpoint: Privacy", "Where do your words actually go?")
notes(s, "This week's checkpoint: what you should never tell an AI, or put on a public site.")

# 4 ─ Sort game ─────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "With your partner · 5 minutes", "Safe to type into an AI?")
cards = ["Your favorite band", "Your first name", "The name of your school",
         "A homework question", "Your pet's name", "A photo of your friend",
         "Your project idea", "Your city", "Your password"]
order = [0, 4, 2, 6, 1, 8, 3, 7, 5]  # shuffled visual order so the answer isn't obvious
cs = []
for slot, ci in enumerate(order):
    x, y = 0.7 + (slot % 3) * 4.05, 2.0 + (slot // 3) * 1.25
    cs.append(boxed(s, x, y, 3.8, 1.0, WHITE, cards[ci], line=INK, size=21, bold=True,
                    align=PP_ALIGN.CENTER))
legend = boxed(s, 0.7, 5.95, 11.95, 0.8, INK,
               [[("SAFE", {"color": GREEN}), "     ·     ", ("DEPENDS", {"color": YELLOW}),
                 "     ·     ", ("NOT SAFE", {"color": RED})]],
               size=24, font=HEAD, color=WHITE, align=PP_ALIGN.CENTER)
set_transition(s, "wipe")
anim_steps(s, [("auto", [(c, "zoom") for c in cs]), ("click", [(legend, "wipe")])], stagger=90)
notes(s, """
Hand each pair a set of the 9 printed cards. They sort into three piles:
SAFE, DEPENDS, NOT SAFE. 5 minutes. They have to agree as a pair.
Don't give answers yet — next slide.
""")

# 5 ─ Sort reveal ───────────────────────────────────────────────────────
s = blank(prs)
heading(s, "The answers", "How did you sort them?")
cols = [("SAFE", GREEN, [("Your favorite band", ""), ("A homework question", ""),
                         ("Your project idea", "")]),
        ("DEPENDS", YELLOW, [("Your first name", "nickname is safer on a site"),
                             ("Your pet's name", "common password question"),
                             ("Your city", "OK alone — risky combined")]),
        ("NOT SAFE", RED, [("Your school's name", "tells people where to find you"),
                           ("A photo of a friend", "they didn't say yes"),
                           ("Your password", "never. anywhere.")])]
steps = []
for i, (hdr, col, items) in enumerate(cols):
    x = 0.7 + i * 4.1
    h = boxed(s, x, 1.95, 3.8, 0.75, col, hdr, size=24, font=HEAD,
              color=INK if col == YELLOW else WHITE, align=PP_ALIGN.CENTER)
    group = [(h, "wipedown")]
    for j, (t, why) in enumerate(items):
        paras = [[(t, {"bold": True, "size": 19})]]
        if why:
            paras.append([(why, {"size": 15, "color": SLATE})])
        group.append((boxed(s, x, 2.85 + j * 1.3, 3.8, 1.15, WHITE, paras, line=col,
                            align=PP_ALIGN.CENTER), "rise"))
    steps.append(("click", group))
set_transition(s, "fade")
anim_steps(s, steps, stagger=180)
notes(s, """
One click per column. After each column ask: who sorted it differently? Why?
There's room to argue about DEPENDS — that's the point. The question to always ask:
"Could a stranger use this to find me, pretend to be me, or embarrass someone?"
""")

# 6 ─ Where your chat goes ──────────────────────────────────────────────
s = blank(prs)
heading(s, "Where your chat goes", "Hitting send isn't private.")
flow = [("You type", ORANGE, WHITE), ("The company's servers", CYAN, INK),
        ("Saved", YELLOW, INK)]
fl = []
for i, (t, c, tc) in enumerate(flow):
    fl.append(boxed(s, 0.7 + i * 4.25, 2.1, 3.5, 1.3, c, t, size=24, font=HEAD, color=tc,
                    align=PP_ALIGN.CENTER))
arr = [rect(s, 4.3 + i * 4.25, 2.55, 0.55, 0.4, SLATE, shape=MSO_SHAPE.RIGHT_ARROW) for i in range(2)]
maybe = [text(s, 9.2, 3.65, 3.6, 1.6,
              ["…and maybe:", "• used to train future AI", "• read by a human reviewer"],
              size=18, color=SLATE, bold=True)]
dos = boxed(s, 0.7, 5.2, 11.95, 1.5, INK,
            [[("So: ", {"color": ORANGE}), "turn off “improve the model” in settings, "],
             "and type like a stranger might read it."],
            size=24, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(fl[0], "zoom"), (arr[0], "wipe"), (fl[1], "zoom"), (arr[1], "wipe"),
                          (fl[2], "zoom")]),
               ("click", [(maybe[0], "rise")]), ("click", [(dos, "wipe")])], stagger=300)
notes(s, """
AI companies store your chats on their servers. Depending on the company and your
settings, chats may be used to train future models, and some may be reviewed by people
for safety. Show where the setting is in ChatGPT: Settings → Data controls →
"Improve the model for everyone" → off. (Check the current menu path before the session.)
Teen accounts get extra protections, but the rule is the same: type like a stranger
might read it.
""")

# 7 ─ Public repo ───────────────────────────────────────────────────────
s = blank(prs, INK)
k = text(s, 0.8, 1.0, 11, 0.5, "ONE MORE THING", size=18, color=CYAN, bold=True)
big = text(s, 0.8, 1.6, 11.8, 2.4,
           ["Your GitHub repo is public.", [("So is its ", {}), ("history.", {"color": ORANGE})]],
           size=44, font=HEAD, color=WHITE, spacing=0.95)
pts = [text(s, 0.8, 4.35 + i * 0.72, 11.6, 0.7, t, size=23, color=WHITE)
       for i, t in enumerate(["Anyone on the internet can read every file in it.",
                              "Deleting a file later doesn't erase it from old commits.",
                              "So: think before you commit. Nothing private, ever."])]
set_transition(s, "zoom")
anim_steps(s, [("auto", [(k, "fade"), (big, "rise")]), ("click", [(p, "rise") for p in pts])],
           stagger=300)
notes(s, """
Optional live demo: open someone's repo (with permission), click "History" / commits,
and show that old versions are still there. That's why the safety rules matter.
""")

# 8 ─ Section ───────────────────────────────────────────────────────────
s = section(prs, "02", "Pick your project.", "Something you'd use — or show off.", bg=CYAN)
notes(s, "Bring out the sticky notes of dream sites from Session 1.")

# 9 ─ Menu ──────────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "The menu", "Pick from a tier.", CYAN)
tiers = [("EVERYONE SHIPS", GREEN, ["About-me / portfolio", "Fan page", "Quiz", "Flashcards",
                                     "Calculator / converter", "Choose-your-own-adventure"]),
         ("STRETCH", ORANGE, ["Browser game", "To-do / habit tracker", "(saves in the browser)"]),
         ("ADVANCED", INK, ["Chrome extension", "A small tool for a real", "local club or group"])]
tc = []
for i, (h, c, items) in enumerate(tiers):
    x = 0.7 + i * 4.1
    tc.append(boxed(s, x, 2.0, 3.8, 3.6, WHITE,
                    [[(h, {"font": HEAD, "size": 20, "color": c})], ""] + items,
                    line=c, size=19, bold=True, anchor=MSO_ANCHOR.TOP))
off = boxed(s, 0.7, 5.85, 11.95, 0.85, RED,
            [[("OFF LIMITS:  ", {"font": HEAD}), "logins · databases · API keys · collecting anyone's info"]],
            size=20, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(t, "rise")]) for t in tc] + [("click", [(off, "wipe")])])
notes(s, """
Most people should pick from EVERYONE SHIPS — and that's not the "easy" tier, it's the
"actually finish" tier. You can always add more after demo day.
Off limits = anything that needs a server, accounts, or other people's data.
That's for safety and privacy, not because you can't do it.
""")

# 10 ─ The test ─────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Before you commit to an idea", "The 3-question test.", CYAN)
qs = [("Would you use it — or show it to someone?", "If not, you'll stop by week 4."),
      ("Can you say it in one sentence?", "If not, it's two projects."),
      ("Could a tiny version work in 2 weeks?", "If not, shrink it.")]
qc = [boxed(s, 0.7, 2.0 + i * 1.5, 11.95, 1.3, WHITE,
            [[(f"{i + 1}   ", {"color": CYAN, "font": HEAD}), (q, {"bold": True})],
             [("      " + a, {"size": 17, "color": SLATE})]],
            line=MIST, size=24, anchor=MSO_ANCHOR.MIDDLE)
      for i, (q, a) in enumerate(qs)]
set_transition(s, "fade")
anim_steps(s, [("click", [(q, "wipe")]) for q in qc])
notes(s, """
Give them ~5 minutes to choose. Three yeses = go. Circulate and help people shrink
big ideas — the big version becomes their "Someday" list.
""")

# 11 ─ Pitch formula ────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Write it down", "Your one-sentence pitch.")
parts = [("My site helps", INK, WHITE), ("[WHO]", ORANGE, WHITE), ("[DO WHAT]", CYAN, INK),
         ("by [HOW].", YELLOW, INK)]
widths = [3.3, 2.4, 3.0, 2.85]
pp, x = [], 0.7
for (t, c, tc_), w in zip(parts, widths):
    pp.append(boxed(s, x, 2.3, w, 1.3, c, t, size=28, font=HEAD, color=tc_, align=PP_ALIGN.CENTER))
    x += w + 0.13
ex = boxed(s, 0.7, 4.3, 11.95, 2.3, WHITE,
           [[("Example", {"font": HEAD, "color": ORANGE, "size": 18})], "",
            [("My site helps ", {}), ("8th graders in Spanish 1", {"color": ORANGE}),
             (" ", {}), ("study vocab", {"color": CYAN}), (" by ", {}),
             ("flipping flashcards and tracking which ones they missed.", {"color": SLATE})]],
           line=MIST, size=24, bold=True, anchor=MSO_ANCHOR.TOP)
set_transition(s, "fade")
anim_steps(s, [("click", [(p, "zoom") for p in pp]), ("click", [(ex, "rise")])], stagger=250)
notes(s, """
Everyone writes their pitch on the pitch sheet. Then read it out loud to your partner.
Partner's job: say back what they think the site does. If they get it wrong, rewrite it.
""")

# 12 ─ Example pitches ──────────────────────────────────────────────────
s = blank(prs)
heading(s, "More examples", "Pitches that work.")
exs = [("helps my friends pick a movie", "by answering 3 quick questions.", ORANGE),
       ("shows off my drawings", "in a gallery that zooms in when you click.", CYAN),
       ("helps my cross-country team", "convert mile times into pace per lap.", GREEN)]
ec = [boxed(s, 0.7, 2.0 + i * 1.5, 11.95, 1.3, WHITE,
            [[("My site ", {}), (a + " ", {"color": c}), (b, {"color": SLATE})]],
            line=c, size=24, bold=True, anchor=MSO_ANCHOR.MIDDLE)
      for i, (a, b, c) in enumerate(exs)]
set_transition(s, "fade")
anim_steps(s, [("click", [(e, "rise")]) for e in ec])
notes(s, "Notice: each one is small, specific, and something a real person would use.")

# 13 ─ Must / Nice / Someday ────────────────────────────────────────────
s = blank(prs)
heading(s, "Scope it", "Must · Nice · Someday.")
mc = [("MUST", ORANGE, "The one thing that makes it work.", "Cards flip to show the answer."),
      ("NICE", CYAN, "Makes it better. Week 4–5.", "Shuffle button. A score."),
      ("SOMEDAY", SLATE, "The dream. After demo day.", "Accounts. Share decks with friends.")]
mcs = [boxed(s, 0.7 + i * 4.1, 2.0, 3.8, 3.4, WHITE,
             [[(h, {"font": HEAD, "size": 30, "color": c})], [(d, {"size": 18, "bold": True})], "",
              [("e.g. " + e, {"size": 17, "color": SLATE})]],
             line=c, anchor=MSO_ANCHOR.TOP)
       for i, (h, c, d, e) in enumerate(mc)]
rule = boxed(s, 0.7, 5.75, 11.95, 0.95, YELLOW,
             [["Build ", ("only", {"font": HEAD}), " the MUST first. Ship it. Then add."]],
             size=26, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(m, "rise")]) for m in mcs] + [("click", [(rule, "zoom")])])
notes(s, """
Examples use the flashcard pitch. Everyone fills in their own three boxes.
"Someday" is where big ideas go to stay alive without blocking you.
""")

# 14 ─ Section ──────────────────────────────────────────────────────────
s = section(prs, "03", "Build feature 1.", "Your MUST. Smallest version. Live today.", bg=ORANGE)
notes(s, "Laptops open. ~45 minutes of building.")

# 15 ─ Build loop ───────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Every feature, every time", "The build loop.")
loop = [("Plan", "ask the AI for steps, not code"), ("Tiny version", "step 1 only"),
        ("Explain-back", "to your partner"), ("Commit", "with a real message"),
        ("Check live", "on your phone")]
track = rect(s, 1.3, 3.05, 10.8, 0.08, MIST)
nodes = []
for i, (t, d) in enumerate(loop):
    x = 0.7 + i * 2.5
    dot = rect(s, x + 0.55, 2.55, 1.0, 1.0, [ORANGE, CYAN, YELLOW, INK, GREEN][i], shape=MSO_SHAPE.OVAL)
    text(s, 0, 0, 0, 0, str(i + 1), shape=dot, size=30, font=HEAD, align=PP_ALIGN.CENTER,
         anchor=MSO_ANCHOR.MIDDLE, color=INK if i == 2 else WHITE)
    lab = text(s, x, 3.75, 2.2, 1.6, [[(t, {"font": HEAD, "size": 21})], d], size=16, color=SLATE,
               align=PP_ALIGN.CENTER)
    nodes.append((dot, lab))
again = boxed(s, 3.65, 5.7, 6.0, 0.9, INK, "↺  then repeat for the next step",
              size=22, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("auto", [(track, "wipe")])] + [("click", [(d, "zoom"), (l, "rise")]) for d, l in nodes]
           + [("click", [(again, "rise")])], stagger=150)
notes(s, """
This is the same loop the Claude Code agent used in Session 1 — except YOU are doing the
checking at every step. Leaders: enforce explain-back before every commit.
""")

# 16 ─ Planning prompt ──────────────────────────────────────────────────
s = blank(prs)
heading(s, "Copy this · then fill in the brackets", "The planning prompt.", CYAN)
p = boxed(s, 0.7, 2.0, 7.7, 4.7, INK,
          ["My project: [your pitch].", "",
           "My must-have feature is:", "[your MUST].", "",
           "Don't write code yet.",
           "Break this feature into 3",
           "tiny steps I can do one",
           "at a time."],
          size=22, font=MONO, color=WHITE, anchor=MSO_ANCHOR.TOP)
then = boxed(s, 8.8, 2.0, 3.85, 4.7, YELLOW,
             [[("Then:", {"font": HEAD, "size": 24})], "",
              "“Now help me with step 1 only. Keep it under 40 lines and explain each part.”"],
             size=20, bold=True, anchor=MSO_ANCHOR.TOP)
set_transition(s, "fade")
anim_steps(s, [("auto", [(p, "wipe")]), ("click", [(then, "rise")])])
notes(s, """
Asking for a plan first keeps YOU in charge of the project. If the AI dumps a huge file
anyway, reply: "Too much. Step 1 only, under 40 lines."
Keep using the tutor-mode prompt from Session 1 too.
""")

# 17 ─ Own the code ─────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Before you paste anything", "Make the code yours.")
chk = [("Read it first.", "All of it. Out loud if it helps."),
       ("Point to the part that does the thing.", "“This line makes the card flip.”"),
       ("Change one thing by hand.", "A color, some text, a size. Prove you can."),
       ("Then commit.", "")]
cc = [boxed(s, 0.7, 1.95 + i * 1.2, 11.95, 1.05, WHITE,
            [[("☐  ", {"color": ORANGE}), (a, {"bold": True}), ("   " + b, {"size": 18, "color": SLATE})]],
            line=MIST, size=23, anchor=MSO_ANCHOR.MIDDLE)
      for i, (a, b) in enumerate(chk)]
set_transition(s, "fade")
anim_steps(s, [("click", [(c, "wipe")]) for c in cc])
notes(s, """
"Change one thing by hand" is small but powerful: it proves you understand where things
live in the code, and it's the first step to not needing the AI for small edits.
""")

# 18 ─ Commit messages ──────────────────────────────────────────────────
s = blank(prs)
heading(s, "Commit messages", "Say what changed.")
bad = boxed(s, 0.7, 2.1, 5.8, 3.0, WHITE,
            [[("✗  Not this", {"font": HEAD, "color": RED, "size": 24})], "",
             [("update", {"font": MONO})], [("stuff", {"font": MONO})], [("asdfgh", {"font": MONO})]],
            line=RED, size=22, anchor=MSO_ANCHOR.TOP)
good = boxed(s, 6.85, 2.1, 5.8, 3.0, WHITE,
             [[("✓  This", {"font": HEAD, "color": GREEN, "size": 24})], "",
              [("Add flip animation to cards", {"font": MONO})],
              [("Fix button not showing on phone", {"font": MONO})],
              [("Change colors to team colors", {"font": MONO})]],
             line=GREEN, size=19, anchor=MSO_ANCHOR.TOP)
why = boxed(s, 0.7, 5.5, 11.95, 1.1, INK,
            "Your commit history becomes the story of how you built it — great for demo day.",
            size=21, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(bad, "rise")]), ("click", [(good, "rise")]), ("click", [(why, "wipe")])])
notes(s, """
In GitHub's web editor, the "Commit changes" box has a message field — use it.
Start with a verb: Add, Fix, Change, Remove.
""")

# 19 ─ Check live ───────────────────────────────────────────────────────
s = blank(prs, INK)
k = text(s, 0.8, 1.2, 11, 0.5, "LAST 10 MINUTES", size=18, color=CYAN, bold=True)
big = text(s, 0.8, 1.8, 11.8, 1.4, "Is it live?", size=72, font=HEAD, color=WHITE)
ck = [text(s, 0.8, 3.6 + i * 0.75, 11.5, 0.7, t, size=24, color=WHITE)
      for i, t in enumerate(["Open your URL on your phone. Does feature 1 work?",
                             "Journal: what did you ask? what came back? what broke?",
                             "Not live yet? That's fine — commit what you have."])]
set_transition(s, "zoom")
anim_steps(s, [("auto", [(k, "fade"), (big, "rise")]), ("click", [(c, "rise") for c in ck])],
           stagger=300)
notes(s, "Leaders: note who has feature 1 live (for the measurement sheet).")

# 20 ─ Closing ──────────────────────────────────────────────────────────
s = blank(prs, INK)
rect(s, 0, 0, 0.35, 7.5, ORANGE)
t = text(s, 0.9, 1.0, 11, 1.2, "Before next week", size=54, font=HEAD, color=WHITE)
hw = [("1", "Finish your MUST feature.", "Smallest version that works."),
      ("2", "Write down one bug you hit.", "What happened vs. what you expected."),
      ("3", "Next week: Bug Bounty.", "Can you spot what the AI got wrong in its code?")]
hws = [text(s, 0.9, 2.6 + i * 1.15, 11.5, 1.1,
            [[(n + "   ", {"color": ORANGE, "font": HEAD}), (a, {"bold": True})],
             [("      " + b, {"color": CYAN, "size": 18})]], size=26, color=WHITE)
       for i, (n, a, b) in enumerate(hw)]
bye = text(s, 0.9, 6.3, 11, 0.7, "See you next week.  Build it. Ship it. Question it.",
           size=20, color=SLATE, bold=True)
set_transition(s, "fade", "slow")
anim_steps(s, [("auto", [(t, "rise")] + [(h, "rise") for h in hws] + [(bye, "fade")])],
           stagger=350)
notes(s, "Collect pitch sheets (photo them, hand them back) so leaders can plan help for next week.")

out = OUT_DIR / "session-02-idea-and-scope.pptx"
prs.save(out)
print("saved", out, "slides:", len(prs.slides))
