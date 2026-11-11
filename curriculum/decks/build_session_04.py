"""Session 4 deck: Build + debug — break it, fix it. AI Checkpoint: bias.

Run from repo root:
    uv run --with python-pptx python curriculum/decks/build_session_04.py
Slide numbers match the run of show in curriculum/session-04-debug-and-bias.md.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from deckkit import *  # noqa: E402,F403

prs = new_deck()


# 1 ─ Title ──────────────────────────────────────────────────────────────
s = blank(prs, INK)
rect(s, 0, 0, 0.35, 7.5, ORANGE)
k = text(s, 0.9, 0.8, 8, 0.5, "SESSION 4 OF 6  ·  BUILD + DEBUG", size=16, color=CYAN, bold=True)
l1 = text(s, 0.85, 1.6, 11, 1.5, "Break it.", size=88, font=HEAD, color=WHITE)
l2 = text(s, 0.85, 3.1, 11, 1.5, "Fix it.", size=88, font=HEAD, color=ORANGE)
sub = text(s, 0.9, 5.4, 11, 1.2,
           ["Today: read errors like a detective, and catch AI bias.",
            ("Build it. Ship it. Question it.", {"color": CYAN, "size": 18})],
           size=24, color=WHITE, bold=True)
set_transition(s, "fade", "slow")
anim_steps(s, [("auto", [(k, "fade"), (l1, "rise"), (l2, "rise"), (sub, "fade")])], stagger=400)
notes(s, "Welcome back. Today is about getting unstuck on your own.")

# 2 ─ Bug of the week ───────────────────────────────────────────────────
s = blank(prs)
heading(s, "Bug of the week · 3–4 volunteers", "What broke?")
bw = [("I expected…", "what should have happened", CYAN),
      ("Instead…", "what actually happened", RED),
      ("I fixed it by…", "or: I'm still stuck", GREEN)]
bc = [boxed(s, 0.7 + i * 4.1, 2.2, 3.8, 3.0, WHITE,
            [[(a, {"font": HEAD, "size": 28, "color": c})], "", [(b, {"size": 18, "color": SLATE})]],
            line=c, bold=True, align=PP_ALIGN.CENTER)
      for i, (a, b, c) in enumerate(bw)]
tip = boxed(s, 0.7, 5.6, 11.95, 1.0, INK, "Every bug you've hit is practice for the next one.",
            size=21, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(c, "rise") for c in bc]), ("click", [(tip, "wipe")])], stagger=200)
notes(s, "Use the homework from Session 3. Celebrate 'still stuck' too — we'll fix it today.")

# 3 ─ Section ───────────────────────────────────────────────────────────
s = section(prs, "01", "Debug like a detective.", "The computer is telling you what's wrong. Read it.", bg=CYAN)
notes(s, "Most beginners never look at the error. Today you will.")

# 4 ─ The Console ───────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Meet the Console", "Where errors show up.", CYAN)
keys = [("Mac", "⌘ + Option + J"), ("Windows / Chromebook", "Ctrl + Shift + J")]
kc = [boxed(s, 0.7 + i * 6.1, 1.95, 5.85, 1.2, WHITE,
            [[(a + ":   ", {"color": SLATE, "size": 18}), (b, {"font": MONO, "size": 24})]],
            line=CYAN, bold=True, align=PP_ALIGN.CENTER)
      for i, (a, b) in enumerate(keys)]
con = rect(s, 0.7, 3.45, 11.95, 2.2, INK)
err = text(s, 0.95, 3.7, 11.5, 0.6,
           [[("✖ ", {"color": RED}), ("Uncaught ReferenceError: ", {"color": RED}),
             ("scroe is not defined", {"color": WHITE})]], size=22, font=MONO, bold=True)
where = text(s, 0.95, 4.45, 11.5, 0.6,
             [[("    at index.html", {"color": SLATE}), (":42", {"color": YELLOW})]],
             size=22, font=MONO, bold=True)
lab = boxed(s, 0.7, 5.9, 11.95, 0.85, YELLOW,
            [["Red = error.  It tells you ", ("what", {"font": HEAD}), " and ", ("which line", {"font": HEAD}), "."]],
            size=22, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(k, "rise") for k in kc]), ("click", [(err, "wipe")]),
               ("click", [(where, "wipe")]), ("click", [(lab, "zoom")])], stagger=200)
notes(s, """
Everyone opens their own live site and the Console right now. (Chrome. On Safari you
have to enable the Develop menu first — easier to use Chrome today.)
In this example: "scroe" is a typo for "score", on line 42.
""")

# 5 ─ 4-step habit ──────────────────────────────────────────────────────
s = blank(prs)
heading(s, "The debug-first habit", "4 steps before you ask anyone.")
st = [("Read", "the whole error message"), ("Find", "the line number it gives"),
      ("Guess", "why — say it out loud"), ("Try one fix", "then refresh and check")]
track = rect(s, 1.6, 3.05, 10.2, 0.08, MIST)
nodes = []
for i, (t, d) in enumerate(st):
    x = 0.9 + i * 3.1
    dot = rect(s, x + 0.65, 2.55, 1.0, 1.0, [CYAN, ORANGE, YELLOW, GREEN][i], shape=MSO_SHAPE.OVAL)
    text(s, 0, 0, 0, 0, str(i + 1), shape=dot, size=30, font=HEAD, align=PP_ALIGN.CENTER,
         anchor=MSO_ANCHOR.MIDDLE, color=INK if i == 2 else WHITE)
    lab = text(s, x, 3.75, 2.3, 1.4, [[(t, {"font": HEAD, "size": 24})], d], size=17, color=SLATE,
               align=PP_ALIGN.CENTER)
    nodes.append((dot, lab))
then = boxed(s, 2.4, 5.6, 8.5, 1.0, INK, "Still stuck after 2 tries?  Now ask the AI — with the error.",
             size=21, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("auto", [(track, "wipe")])] + [("click", [(d, "zoom"), (l, "rise")]) for d, l in nodes]
           + [("click", [(then, "rise")])], stagger=150)
notes(s, """
Step 3 is the one people skip. Even a wrong guess helps — it tells you where to look next.
When you DO ask the AI, paste the exact error message and the line it points to.
""")

# 6 ─ Error decoder ─────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Error decoder", "What the message usually means.")
dec = [("… is not defined", "A typo in a name, or you used it before creating it."),
       ("Cannot read properties of null", "JS couldn't find the HTML element. Check the id matches."),
       ("Unexpected token / missing )", "A bracket, quote, or comma is missing or extra."),
       ("… is not a function", "A typo in a function name, or calling the wrong thing.")]
rows = []
for i, (m, d) in enumerate(dec):
    y = 1.95 + i * 1.18
    rows.append(boxed(s, 0.7, y, 11.95, 1.02, WHITE,
                      [[(m, {"font": MONO, "color": RED, "size": 19}), " →  ",
                        (d, {"size": 18, "color": INK})]],
                      line=MIST, bold=True, anchor=MSO_ANCHOR.MIDDLE))
set_transition(s, "fade")
anim_steps(s, [("click", [(r, "wipe")]) for r in rows])
notes(s, """
These four cover most beginner bugs. Have teens photograph this slide.
"null" almost always means: the id in your JavaScript doesn't match the id in your HTML.
""")

# 7 ─ No error but broken ───────────────────────────────────────────────
s = blank(prs)
heading(s, "No red error, but it's still broken?", "Check these first.")
chk = [("Did you commit?", "Changes in the editor aren't live until you commit."),
       ("Waited 1–2 minutes?", "GitHub Pages takes a moment to update."),
       ("Hard refresh?", "⌘ + Shift + R  /  Ctrl + Shift + R"),
       ("Right file?", "Editing index.html in the right repo?")]
cc = [boxed(s, 0.7 + (i % 2) * 6.1, 1.95 + (i // 2) * 2.35, 5.85, 2.1, WHITE,
            [[("☐  ", {"color": ORANGE}), (a, {"font": HEAD, "size": 24})], [(b, {"size": 18, "color": SLATE})]],
            line=MIST, bold=True, anchor=MSO_ANCHOR.MIDDLE)
      for i, (a, b) in enumerate(chk)]
set_transition(s, "fade")
anim_steps(s, [("click", [(c, "rise")]) for c in cc])
notes(s, "Half of all 'my code doesn't work' moments are actually 'my change isn't live yet.'")

# 8 ─ console.log ───────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Detective trick", "Leave yourself clues.")
code = boxed(s, 0.7, 2.0, 7.4, 3.4, INK,
             ['button.addEventListener("click", () => {',
              [("  console.log(\"clicked!\");", {"color": YELLOW})],
              '  // ...the rest of your code',
              '});'],
             size=18, font=MONO, color=WHITE, bold=True, anchor=MSO_ANCHOR.MIDDLE)
ex = boxed(s, 8.5, 2.0, 4.15, 3.4, YELLOW,
           [[("console.log", {"font": MONO, "size": 20})], "",
            "prints a message to the Console.", "",
            "See “clicked!”?  The code ran.", "",
            "Don't see it?  It never got there."],
           size=17, bold=True, anchor=MSO_ANCHOR.TOP)
tip = boxed(s, 0.7, 5.75, 11.95, 0.9, INK, "Print a variable to see what it really is:  console.log(score)",
            size=21, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("auto", [(code, "wipe")]), ("click", [(ex, "rise")]), ("click", [(tip, "wipe")])])
notes(s, "This is how professional developers debug too. Delete the console.logs when you're done.")

# 9 ─ Rubber duck ───────────────────────────────────────────────────────
s = blank(prs, YELLOW)
k = text(s, 0.8, 1.0, 11, 0.5, "REAL TECHNIQUE, REALLY USED", size=18, color=INK, bold=True)
big = text(s, 0.8, 1.6, 11.8, 2.4, ["Explain your code,", "line by line,", "to a rubber duck."],
           size=48, font=HEAD, color=INK, spacing=0.95)
why = [text(s, 0.8, 4.6 + i * 0.7, 11.6, 0.65, t, size=22, color=INK, bold=True)
       for i, t in enumerate(["Saying it out loud makes you notice what you skipped.",
                              "Harvard's CS50 even built an AI duck that gives hints — not answers."])]
set_transition(s, "push")
anim_steps(s, [("auto", [(k, "fade"), (big, "rise")]), ("click", [(w, "rise") for w in why])],
           stagger=300)
notes(s, "Hand out ducks if you brought them. Your partner can be the duck — their job is to listen, not fix.")

# 10 ─ Live debug ───────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Live · together", "Let's fix a broken page.", RED)
pg = boxed(s, 0.7, 2.0, 5.8, 4.6, INK,
           [[("Coin Flip", {"font": HEAD, "size": 30})], "", [("[ Flip! ]", {"font": MONO, "size": 24})], "",
            [("(nothing happens)", {"color": SLATE, "size": 18})]],
           color=WHITE, bold=True, align=PP_ALIGN.CENTER)
plan = [("3 bugs are hiding.", ORANGE), ("Open the Console.", CYAN),
        ("Use the 4 steps.", YELLOW), ("Fix one. Refresh. Repeat.", GREEN)]
pc = [boxed(s, 6.85, 2.0 + i * 1.18, 5.8, 1.0, c, t, size=22, font=HEAD,
            color=INK if c == YELLOW else WHITE, align=PP_ALIGN.CENTER)
      for i, (t, c) in enumerate(plan)]
set_transition(s, "fade")
anim_steps(s, [("auto", [(pg, "fade")]), ("click", [(p, "rise") for p in pc])], stagger=200)
notes(s, """
Switch to Chrome: curriculum/demos/broken-coin-flip.html with the Console open.
The room calls out each step (Read, Find, Guess, Try). Order the errors appear:
1. SyntaxError: missing ) after argument list → change "};" to "});"
2. Cannot read properties of null (line 26) → "flip-btn" should be "flipBtn"
3. Click Flip! → reslt is not defined (line 28) → change to resultText
Point out: fixing one error revealed the next. That's normal.
""")

# 11 ─ Section ──────────────────────────────────────────────────────────
s = section(prs, "02", "AI Checkpoint: Bias", "Who does the AI imagine?")
notes(s, "Switch gears. This checkpoint is about what AI assumes about people.")

# 12 ─ Activity ─────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "With your partner · 5 minutes", "Ask your AI this. Exactly.")
p = boxed(s, 0.7, 1.95, 7.6, 3.2, INK,
          ["Write 4 one-sentence stories:",
           "one about a programmer, one about",
           "a nurse, one about a CEO, and one",
           "about a kindergarten teacher.",
           "Give each person a name."],
          size=20, font=MONO, color=WHITE, bold=True, anchor=MSO_ANCHOR.MIDDLE)
tally = boxed(s, 8.7, 1.95, 3.95, 3.2, YELLOW,
              [[("Then tally:", {"font": HEAD, "size": 22})], "",
               "For each job, did the AI say", "he, she, or they?"],
              size=18, bold=True, anchor=MSO_ANCHOR.TOP)
rule = boxed(s, 0.7, 5.55, 11.95, 1.1, WHITE,
             "Don't change the prompt — we want to compare everyone's results.",
             line=MIST, size=21, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("auto", [(p, "wipe")]), ("click", [(tally, "rise")]), ("click", [(rule, "wipe")])])
notes(s, "Put the prompt somewhere copyable. Leader B draws the tally grid (next slide) on the board.")

# 13 ─ Tally board ──────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Room results", "What did the AI pick?")
roles = ["Programmer", "Nurse", "CEO", "Kindergarten teacher"]
cols = ["he", "she", "they"]
cells = []
hdrs = [boxed(s, 4.6 + j * 2.7, 1.95, 2.55, 0.75, [CYAN, ORANGE, GREEN][j], c, size=24, font=HEAD,
              color=WHITE, align=PP_ALIGN.CENTER) for j, c in enumerate(cols)]
for i, r in enumerate(roles):
    y = 2.85 + i * 0.98
    rl = boxed(s, 0.7, y, 3.75, 0.85, INK, r, size=20, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    row = [rl] + [rect(s, 4.6 + j * 2.7, y, 2.55, 0.85, WHITE, MIST) for j in range(3)]
    cells.append(row)
foot = text(s, 0.7, 6.85, 12, 0.4, "Fill in the counts on the whiteboard as pairs report.", size=14, color=SLATE)
set_transition(s, "fade")
anim_steps(s, [("auto", [(h, "zoom") for h in hdrs])] + [("click", [(c, "wipe") for c in row]) for row in cells],
           stagger=80)
notes(s, """
Go pair by pair. Then ask: any patterns? Were some jobs almost always "he" or "she"?
If results were balanced: that's interesting too — many AI companies now tune models to
avoid stereotypes. Who decides what's fair? Results change model to model.
""")

# 14 ─ Why ──────────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Where bias comes from", "AI copies the patterns it learned.")
flow = [("Text written by people", "including old stereotypes", CYAN),
        ("Patterns", "“nurse” often near “she”", ORANGE),
        ("Output", "repeated millions of times", RED)]
fb = [boxed(s, 0.7 + i * 4.25, 2.2, 3.5, 2.2, c,
            [[(a, {"font": HEAD, "size": 22})], "", [(b, {"size": 16})]],
            color=WHITE, bold=True, align=PP_ALIGN.CENTER)
      for i, (a, b, c) in enumerate(flow)]
arr = [rect(s, 4.3 + i * 4.25, 3.1, 0.55, 0.4, SLATE, shape=MSO_SHAPE.RIGHT_ARROW) for i in range(2)]
key = boxed(s, 0.7, 5.0, 11.95, 1.6, INK,
            [["The AI isn't trying to be unfair.", ],
             [("It's predicting what's ", {}), ("common", {"color": ORANGE}), (" — and common isn't always ", {}),
              ("fair", {"color": CYAN}), (".", {})]],
            size=24, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(fb[0], "zoom"), (arr[0], "wipe"), (fb[1], "zoom"), (arr[1], "wipe"),
                          (fb[2], "zoom")]), ("click", [(key, "rise")])], stagger=300)
notes(s, """
Connect to Session 1: it predicts what SOUNDS right — and what sounds right comes from
what was common in the training data. At scale, small patterns become big ones:
hiring tools, image search, face recognition have all had real bias problems.
""")

# 15 ─ Teachable Machine ────────────────────────────────────────────────
s = blank(prs)
heading(s, "Leader demo · 7 minutes", "Train an AI in 2 minutes.", CYAN)
steps = [("1", "Train 👍 and 👎", "using ONE person's hand, ONE spot."),
         ("2", "Test with the trainer", "It works great!"),
         ("3", "Test with other people", "Different hands, sleeves, distance, light…")]
sc = [boxed(s, 0.7 + i * 4.1, 2.0, 3.8, 2.9, WHITE,
            [[(n, {"font": HEAD, "size": 44, "color": [CYAN, GREEN, ORANGE][i]})],
             [(a, {"font": HEAD, "size": 20})], [(b, {"size": 16, "color": SLATE})]],
            line=MIST, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.TOP)
      for i, (n, a, b) in enumerate(steps)]
q = boxed(s, 0.7, 5.3, 11.95, 1.35, INK,
          [[("What happened? ", {"color": YELLOW}), "The AI only knows what it was shown."]],
          size=26, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
url = text(s, 0.7, 6.8, 12, 0.4, "teachablemachine.withgoogle.com  ·  runs in the browser  ·  leader laptop only",
           size=14, color=SLATE)
set_transition(s, "fade")
anim_steps(s, [("click", [(c, "rise")]) for c in sc] + [("click", [(q, "wipe"), (url, "fade")])])
notes(s, """
On the leader laptop + projector. Image Project → Standard. ~30 webcam samples per class.
Don't save the project or images. Ask the room: if you trained a face-unlock on only
some kinds of faces, who would it fail for? That's a real thing that has happened.
""")

# 16 ─ So what ──────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "So what do we do?", "Notice. Test. Fix.")
w = [("Notice", "Ask: who's missing? Who's assumed?", CYAN),
     ("Test", "Try it with different people and inputs.", ORANGE),
     ("Fix", "Change the data, the prompt, or the design.", GREEN)]
wc = [boxed(s, 0.7 + i * 4.1, 2.0, 3.8, 2.6, c,
            [[(a, {"font": HEAD, "size": 34})], "", [(b, {"size": 18})]],
            color=WHITE, bold=True, align=PP_ALIGN.CENTER)
      for i, (a, b, c) in enumerate(w)]
yours = boxed(s, 0.7, 5.0, 11.95, 1.65, WHITE,
              [[("Your site: ", {"font": HEAD, "color": ORANGE}),
                "can everyone use it? Readable colors, works on phones, words a 7th grader gets."]],
              line=ORANGE, size=21, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(c, "rise")]) for c in wc] + [("click", [(yours, "wipe")])])
notes(s, "Bring it home: bias isn't just an AI problem — it's a design problem. Your site has users too.")

# 17 ─ Section ──────────────────────────────────────────────────────────
s = section(prs, "03", "Build.", "Finish your MUST. Start a NICE.", bg=CYAN)
notes(s, "~48 minutes of build time.")

# 18 ─ Debug-first rule ─────────────────────────────────────────────────
s = blank(prs)
heading(s, "Today's rule", "Debug first. Then ask.", ORANGE)
r = boxed(s, 0.7, 2.0, 11.95, 2.4, YELLOW,
          [["Before you ask the AI ", ("or", {"font": HEAD}), " a leader for help:"], "",
           [("show us the error + your guess.", {"font": HEAD, "size": 34})]],
          size=24, bold=True, align=PP_ALIGN.CENTER)
nice = boxed(s, 0.7, 4.8, 11.95, 1.8, WHITE,
             [[("MUST done? ", {"font": HEAD, "color": GREEN}), "Start a NICE feature from your scope sheet."],
              [("Way ahead? ", {"font": HEAD, "color": CYAN}), "Swap sites with your partner and try to break theirs."]],
             line=MIST, size=21, bold=True, anchor=MSO_ANCHOR.MIDDLE)
set_transition(s, "fade")
anim_steps(s, [("auto", [(r, "zoom")]), ("click", [(nice, "rise")])])
notes(s, "Leaders: ask questions, don't type. 'What does the error say? Which line? What's your guess?'")

# 19 ─ Commit + live ────────────────────────────────────────────────────
dark_list(prs, "LAST 10 MINUTES", "Commit. Check. Write.",
          ["Commit with a real message — and delete stray console.logs.",
           "Open your live URL on your phone. Still working?",
           "Journal: one error message you read today, and what it meant."])
notes(prs.slides[-1], "Leaders: record who has MUST done and who started a NICE feature.")

# 20 ─ Closing ──────────────────────────────────────────────────────────
s = closing(prs, [("Keep building your NICE feature.", "Smallest working version first."),
                  ("Have someone outside the workshop try your site.", "Don't explain. Write down where they got confused."),
                  ("Next week: polish, test, README.", "Plus: who owns code an AI wrote?")])
notes(s, "Remind them: two weeks to demo day.")

out = Path(__file__).parent / "session-04-debug-and-bias.pptx"
prs.save(out)
print("saved", out, "slides:", len(prs.slides))
