"""Session 1 deck: Kickoff — from zero to a live URL.

Run from repo root:
    uv run --with python-pptx python curriculum/decks/build_session_01.py
Slide numbers match the run of show in curriculum/session-01-kickoff.md.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from deckkit import *  # noqa: E402,F403

prs = new_deck()

# 1 ─ Title ──────────────────────────────────────────────────────────────
s = blank(prs, INK)
rect(s, 0, 0, 0.35, 7.5, ORANGE)
k = text(s, 0.9, 0.8, 8, 0.5, "SESSION 1 OF 6  ·  KICKOFF", size=16, color=CYAN, bold=True)
l1 = text(s, 0.85, 1.5, 11, 1.4, "Build it.", size=88, font=HEAD, color=WHITE)
l2 = text(s, 0.85, 2.75, 11, 1.4, "Ship it.", size=88, font=HEAD, color=ORANGE)
l3 = text(s, 0.85, 4.0, 11, 1.4, "Question it.", size=88, font=HEAD, color=WHITE)
sub = text(s, 0.9, 5.75, 11, 1.0,
           ["A free AI builder workshop for teens",
            ("Burch Library  ·  Collierville, TN", {"color": CYAN, "size": 20})],
           size=24, color=WHITE, bold=True)
set_transition(s, "fade", "slow")
anim_steps(s, [("auto", [(k, "fade"), (l1, "rise"), (l2, "rise"), (l3, "rise"), (sub, "fade")])],
           stagger=350)
notes(s, """
Welcome everyone in while people sit down. Let the title animate on its own.
"Welcome to Build it, Ship it, Question it. In six weeks every single one of you is
going to have a real website, live on the internet, that you built with AI —
and you'll know exactly where the AI messed up along the way."
""")

# 2 ─ Who we are ────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Who's running this", "We're students too.")
cards = []
for i, (role, color) in enumerate([("LEADER", ORANGE), ("LEADER", CYAN), ("ADULT SPONSOR", INK)]):
    x = 0.7 + i * 4.1
    c = boxed(s, x, 2.3, 3.8, 3.9, WHITE,
              [[(role, {"size": 13, "color": color, "bold": True})],
               [("[Name]", {"size": 36, "font": HEAD})], "",
               "[Grade · school]", "", "Something I built:", "[one line]"],
              line=color, size=21, color=SLATE, anchor=MSO_ANCHOR.TOP)
    cards.append(c)
set_transition(s, "fade")
anim_steps(s, [("click", [(c, "rise") for c in cards])], stagger=250)
notes(s, """
Each of you: name, grade, and ONE thing you've built (with or without AI).
Adult sponsor introduces themselves and explains why they're here:
"Some of the tools we'll show, like Claude, are 18+. I'm the adult who runs those
demos and I'm here every week."
Fill in the [brackets] before the session.
""")

# 3 ─ Icebreaker ────────────────────────────────────────────────────────
s = blank(prs, INK)
q = text(s, 0.8, 1.2, 11.7, 2.6,
         ["If you could build", [("ANY", {"color": ORANGE}), " website…"], "what would it be?"],
         size=54, font=HEAD, color=WHITE, spacing=0.95)
chips = []
for i, t in enumerate(["Your name", "Grade + school", "Dream site in 5 words"]):
    chips.append(boxed(s, 0.8 + i * 4.0, 5.2, 3.6, 1.0, [CYAN, YELLOW, ORANGE][i], t,
                       size=22, bold=True, color=INK, align=PP_ALIGN.CENTER))
set_transition(s, "fade")
anim_steps(s, [("auto", [(q, "rise")]), ("click", [(c, "rise") for c in chips])])
notes(s, """
Go around the room, fast — 20 seconds each. Write a few of the dream sites on a
whiteboard or sticky notes; we'll come back to them in Session 2 when people pick projects.
""")

# 4 ─ Section ───────────────────────────────────────────────────────────
s = section(prs, "01", "What is AI, really?", "Spoiler: it's a very, very good guesser.")
notes(s, "Transition: before we use AI, let's figure out what it actually is.")

# 5 ─ Guess the next word ───────────────────────────────────────────────
s = blank(prs)
heading(s, "Game", "Guess the next word.")
sent = text(s, 0.7, 2.5, 12, 1.6,
            "After school I grabbed a snack and turned on the",
            size=44, font=HEAD, color=INK)
blank_line = rect(s, 0.85, 4.55, 3.4, 0.14, ORANGE)
shout = boxed(s, 8.6, 4.9, 4.0, 1.3, YELLOW, "Shout it out!", size=30, font=HEAD,
              align=PP_ALIGN.CENTER)
set_transition(s, "wipe")
anim_steps(s, [("auto", [(sent, "wipe"), (blank_line, "wipe")]), ("click", [(shout, "zoom")])])
notes(s, """
Read the sentence out loud and pause. Let people shout guesses. Collect 4–5 answers.
Most people will say TV, Xbox/PlayStation, music… Nobody says "oven". Why? Because
you've seen thousands of sentences like this. Your brain predicted the next word.
""")

# 6 ─ Probability bars ──────────────────────────────────────────────────
s = blank(prs)
heading(s, "That's literally what a chatbot does", "It ranks every possible next word.")
words = [("TV", 41), ("Xbox", 22), ("music", 15), ("lights", 12), ("PlayStation", 7), ("oven", 1)]
bars = []
for i, (wd, pct) in enumerate(words):
    y = 2.25 + i * 0.72
    text(s, 0.7, y, 2.4, 0.6, wd, size=22, bold=True, align=PP_ALIGN.RIGHT,
         anchor=MSO_ANCHOR.MIDDLE)
    b = rect(s, 3.3, y + 0.08, max(0.15, pct / 41 * 5.4), 0.46, ORANGE if i == 0 else CYAN)
    lab = text(s, 3.4 + max(0.15, pct / 41 * 5.4), y, 1.2, 0.6, f"{pct}%", size=20,
               color=SLATE, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    bars.append((b, lab))
foot = text(s, 0.7, 6.75, 12, 0.4, "Numbers are made up to show the idea.", size=13, color=SLATE)
pick = boxed(s, 9.9, 4.4, 2.8, 1.6, INK,
             ["Then it picks one,", "adds it, and", "guesses again."],
             size=17, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [x for b, l in bars for x in ((b, "wipe"), (l, "fade"))]),
               ("click", [(pick, "rise")])], stagger=120)
notes(s, """
Click once: bars grow. "A chatbot gives every possible next word a score like this.
It picks one (usually a likely one, sometimes a surprising one), adds it to the
sentence, and does the whole thing again. Word by word. That's how it writes an essay,
a poem, or code."
Click again for the takeaway box.
""")

# 7 ─ Three steps ───────────────────────────────────────────────────────
s = blank(prs)
heading(s, "How a chatbot is made", "Three steps. No magic.")
steps = [("1", "Read", "a gigantic amount of text: websites, books, code."),
         ("2", "Learn patterns", "which words tend to follow which, in what situations."),
         ("3", "Predict", "the next word, one at a time, over and over.")]
cols = []
for i, (n, t, d) in enumerate(steps):
    x = 0.7 + i * 4.15
    c = boxed(s, x, 2.2, 3.8, 2.9, WHITE,
              [[(n, {"size": 60, "font": HEAD, "color": ORANGE})],
               [(t, {"size": 26, "font": HEAD})], [(d, {"size": 17, "color": SLATE})]],
              line=MIST, anchor=MSO_ANCHOR.TOP)
    cols.append(c)
punch = boxed(s, 0.7, 5.5, 11.95, 1.15, YELLOW,
              [["It predicts what ", ("sounds", {"font": HEAD}), " right — not what ",
                ("is", {"font": HEAD}), " right."]],
              size=28, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(cols[0], "rise")]), ("click", [(cols[1], "rise")]),
               ("click", [(cols[2], "rise")]), ("click", [(punch, "zoom")])])
notes(s, """
One click per step. Keep it short.
Last click is the most important sentence of today: "It predicts what SOUNDS right,
not what IS right." Ask them to remember it — we're going to prove it in 20 minutes.
""")

# 8 ─ Section ───────────────────────────────────────────────────────────
s = section(prs, "02", "Watch an AI build.", "One sentence in. A real website out.", bg=CYAN)
notes(s, "Hand off to the adult sponsor for the live demo.")

# 9 ─ Demo prompt ───────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Live demo · Claude Code", "What we're asking it to do", CYAN)
term = rect(s, 0.7, 2.1, 7.9, 4.6, INK)
bar = rect(s, 0.7, 2.1, 7.9, 0.4, SLATE)
for i, col in enumerate([RED, YELLOW, GREEN]):
    rect(s, 0.9 + i * 0.3, 2.22, 0.16, 0.16, col, shape=MSO_SHAPE.OVAL)
lines = ["> claude",
         "Build a one-page website for our teen AI",
         "workshop. Include a countdown to demo day,",
         "the list of 6 sessions, and a button that",
         "shows a random fun fact about AI.",
         "Then publish it on GitHub Pages."]
tlines = []
for i, ln in enumerate(lines):
    tlines.append(text(s, 0.95, 2.7 + i * 0.6, 7.5, 0.55, ln, size=19, font=MONO,
                       color=CYAN if i == 0 else WHITE, bold=i == 0))
call = boxed(s, 9.0, 2.1, 3.65, 4.6, ORANGE,
             [[("Your job:", {"font": HEAD, "size": 26})], "",
              "Call out changes!", "", "“Dark mode.”", "“Add confetti.”", "“Make it purple.”"],
             size=20, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("auto", [(t, "wipe") for t in tlines]), ("click", [(call, "rise")])], stagger=450)
notes(s, """
ADULT SPONSOR runs this live from their own Claude account on the projector.
(Claude is 18+, so the teens don't log in to Claude themselves. Say this out loud.)
1. Type the prompt shown. Narrate what Claude is doing: planning, creating files, running.
2. Open the result. Take 2–3 change requests from the room and make them.
3. Push / publish so the room sees a real URL.
Keep it to ~12 minutes. If Wi-Fi fails: play the backup recording.
""")

# 10 ─ Agent loop ───────────────────────────────────────────────────────
s = blank(prs)
heading(s, "What just happened?", "An AI agent works in a loop.", CYAN)
loop = [("Plan", 1.2, 2.2), ("Write code", 7.6, 2.2), ("Run it", 7.6, 4.7), ("Spot a problem & fix", 1.2, 4.7)]
nodes = [boxed(s, x, y, 4.5, 1.6, [ORANGE, CYAN, YELLOW, INK][i], t, size=26, font=HEAD,
               color=WHITE if i in (0, 3) else INK, align=PP_ALIGN.CENTER)
         for i, (t, x, y) in enumerate(loop)]
arrows = [rect(s, 5.9, 2.85, 1.5, 0.3, SLATE, shape=MSO_SHAPE.RIGHT_ARROW),
          rect(s, 9.7, 3.9, 0.3, 0.7, SLATE, shape=MSO_SHAPE.DOWN_ARROW),
          rect(s, 5.9, 5.35, 1.5, 0.3, SLATE, shape=MSO_SHAPE.LEFT_ARROW),
          rect(s, 3.3, 3.9, 0.3, 0.7, SLATE, shape=MSO_SHAPE.UP_ARROW)]
set_transition(s, "fade")
anim_steps(s, [("click", [(nodes[0], "zoom")]),
               ("click", [(arrows[0], "wipe"), (nodes[1], "zoom")]),
               ("click", [(arrows[1], "wipedown"), (nodes[2], "zoom")]),
               ("click", [(arrows[2], "fade"), (nodes[3], "zoom"), (arrows[3], "fade")])],
           stagger=250)
notes(s, """
"A chatbot answers once. An agent like Claude Code keeps going: plans, writes code,
runs it, sees what broke, fixes it, repeats. That's why it could build a whole site."
"You'll use the same loop — except YOU are the one checking each step."
""")

# 11 ─ Section ──────────────────────────────────────────────────────────
s = section(prs, "03", "AI Checkpoint", "Confident ≠ Correct.")
notes(s, "Every session has an AI Checkpoint. Today: catching the AI being confidently wrong.")

# 12 ─ Activity ─────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "With your partner · 8 minutes", "Ask your AI these. Then check.")
qs = ["What time does the Burch Library close on Saturdays?",
      "Who is the mayor of Collierville right now?",
      "What's the newest restaurant on the Town Square?"]
qcards = [boxed(s, 0.7, 2.1 + i * 1.15, 8.2, 0.95, WHITE,
                [[(f"Q{i + 1}  ", {"color": ORANGE, "font": HEAD}), q]],
                line=MIST, size=20, bold=True, anchor=MSO_ANCHOR.MIDDLE)
          for i, q in enumerate(qs)]
score = boxed(s, 9.3, 2.1, 3.35, 3.25, INK,
              [[("Score each:", {"font": HEAD, "size": 22})], "",
               [("✓ ", {"color": GREEN}), "right"], [("✗ ", {"color": RED}), "wrong"],
               [("? ", {"color": YELLOW}), "made up / can't tell"]],
              size=20, color=WHITE, bold=True, align=PP_ALIGN.LEFT)
check = boxed(s, 0.7, 5.75, 11.95, 0.95, CYAN,
              "Check against: the official website · a map app · a librarian",
              size=22, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(c, "rise") for c in qcards]), ("click", [(score, "rise")]),
               ("click", [(check, "wipe")])], stagger=200)
notes(s, """
Pairs use ChatGPT (or whatever AI they're allowed to use). Timer: 8 minutes.
LEADERS: look up the real answers the day before from official sources, and
swap in fresher questions if these become too easy.
Debrief: hands up — who got at least one ✗ or ? ... Ask a pair to read out the most
confident wrong answer. Did the AI sound unsure? (Usually no.)
""")

# 13 ─ Why ──────────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Why does that happen?", "Fluent is not the same as true.")
bubble = boxed(s, 0.7, 2.2, 5.6, 2.2, WHITE,
               ["“Great question! The Burch Library is open until 9 PM on Saturdays, "
                "so you have plenty of time to visit.”"],
               line=MIST, size=20, color=INK, anchor=MSO_ANCHOR.MIDDLE)
stamp = boxed(s, 3.0, 4.15, 3.2, 0.8, RED, "UNVERIFIED", size=26, font=HEAD, color=WHITE,
              align=PP_ALIGN.CENTER)
stamp.rotation = -6
reasons = [("It's guessing words,", "not looking things up (unless it searches)."),
           ("Its knowledge has a cutoff,", "so local + recent facts are weak."),
           ("It's trained to sound helpful,", "so it rarely says “I don't know.”")]
rs = [text(s, 7.0, 2.2 + i * 1.15, 5.7, 1.1, [[(a, {"bold": True})], b], size=19, color=INK)
      for i, (a, b) in enumerate(reasons)]
you = boxed(s, 0.7, 5.75, 11.95, 0.95, INK,
            [["So ", ("you", {"color": ORANGE}), " are the fact-checker. Always."]],
            size=26, font=HEAD, color=WHITE, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("auto", [(bubble, "fade")]), ("click", [(stamp, "zoom")]),
               ("click", [(r, "rise") for r in rs]), ("click", [(you, "wipe")])], stagger=250)
notes(s, """
The bubble is an example of a confident answer (we made it up for the slide — it's
the kind of thing AIs say). Click: stamp.
Then the three reasons. Connect back to slide 7: it predicts what SOUNDS right.
This is also why AI-written code can look perfect and still be broken.
""")

# 14 ─ Four habits ──────────────────────────────────────────────────────
s = blank(prs)
heading(s, "How we use AI here", "The 4 habits.")
habits = [("Explain-back", "No AI code goes in your project until you can explain it out loud."),
          ("Tutor mode", "Ask for hints and a plan first. Full code second."),
          ("Pair up", "The beginner types. The partner navigates. Leaders never grab your keyboard."),
          ("Prompt journal", "Write down what you asked, what came back, what broke.")]
hcards = []
for i, (t, d) in enumerate(habits):
    x, y = 0.7 + (i % 2) * 6.1, 2.05 + (i // 2) * 2.3
    hcards.append(boxed(s, x, y, 5.85, 2.05, WHITE,
                        [[(f"{i + 1}  ", {"color": [ORANGE, CYAN, YELLOW, INK][i]}), t],
                         [(d, {"font": BODY, "size": 18, "color": SLATE, "bold": False})]],
                        line=MIST, size=28, font=HEAD, anchor=MSO_ANCHOR.MIDDLE))
set_transition(s, "fade")
anim_steps(s, [("click", [(h, "rise")]) for h in hcards])
notes(s, """
One click per habit. These are the rules every week, not just today.
Why? Research on beginners using AI to code: the ones who let AI do everything end up
unable to fix or change their own project. The ones who use it like a tutor get better.
Hand out the printed habits card.
""")

# 15 ─ Safety ───────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Non-negotiable · not in prompts, not on your site", "Never share these online.", RED)
items = ["Your full name", "Your school", "Your address", "Phone numbers", "Photos of people",
         "Passwords or keys"]
chips = [boxed(s, 0.7 + (i % 3) * 4.05, 2.2 + (i // 3) * 1.35, 3.8, 1.1, WHITE,
               [[("✗  ", {"color": RED}), t]], line=RED, size=22, bold=True,
               anchor=MSO_ANCHOR.MIDDLE)
         for i, t in enumerate(items)]
always = boxed(s, 0.7, 5.3, 11.95, 1.35, INK,
               [[("And always: ", {"color": YELLOW}),
                 "an adult checks your site before you share the link."]],
               size=24, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(c, "zoom") for c in chips]), ("click", [(always, "rise")])],
           stagger=120)
notes(s, """
Use a nickname or first name only on your site. No sign-up forms, no collecting
other people's info. If you're not sure, ask a leader.
""")

# 16 ─ Section ──────────────────────────────────────────────────────────
s = section(prs, "04", "Your turn: ship a page.", "Goal: a live URL in 40 minutes.", bg=CYAN)
notes(s, "Energy up. Everyone opens their laptop now.")

# 17 ─ Steps ────────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "5 steps to live", "From nothing to on-the-internet.", CYAN)
st = [("Log in", "github.com"),
      ("New repo", "name it my-first-site · Public"),
      ("Ask your AI", "for index.html (use tutor mode →)"),
      ("Add file", "Add file → Create new file → index.html → Commit"),
      ("Turn on Pages", "Settings → Pages → Deploy from branch: main")]
line = rect(s, 1.3, 3.05, 10.8, 0.08, MIST)
dots, labels = [], []
for i, (t, d) in enumerate(st):
    x = 0.7 + i * 2.5
    dots.append(boxed(s, x + 0.55, 2.55, 1.0, 1.0, [ORANGE, CYAN, YELLOW, ORANGE, GREEN][i],
                      str(i + 1), size=30, font=HEAD, color=WHITE if i != 2 else INK,
                      align=PP_ALIGN.CENTER, line=None))
    labels.append(text(s, x, 3.75, 2.2, 2.5, [[(t, {"font": HEAD, "size": 21})], d],
                       size=16, color=SLATE, align=PP_ALIGN.CENTER))
set_transition(s, "fade")
anim_steps(s, [("auto", [(line, "wipe")])] +
           [("click", [(d, "zoom"), (l, "rise")]) for d, l in zip(dots, labels)], stagger=150)
notes(s, """
Walk through all five together, one click at a time, with the room following along.
Both leaders circulate. Remember: hands off the keyboard — point, don't type.
No GitHub account / no permission form? They pair with someone and watch today.
""")

# 18 ─ Tutor mode prompt ────────────────────────────────────────────────
s = blank(prs)
heading(s, "Copy this into your AI first", "Tutor mode.", CYAN)
p = boxed(s, 0.7, 2.05, 7.6, 4.65, INK,
          ["I'm a beginner learning to code.",
           "Help me build a single index.html file.", "",
           "Before giving code, explain your plan",
           "in 3 short bullet points.",
           "Keep the code short, with a comment",
           "above each part explaining it.",
           "After the code, ask me one question",
           "to check I understand it."],
          size=22, font=MONO, color=WHITE, anchor=MSO_ANCHOR.TOP)
first = boxed(s, 8.7, 2.05, 3.95, 4.65, YELLOW,
              [[("Your first ask:", {"font": HEAD, "size": 22})], "",
               "“Make a page that says Hi, I'm [first name], uses my favorite color, "
               "and has one button that does something fun.”"],
              size=19, bold=True, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP)
set_transition(s, "fade")
anim_steps(s, [("auto", [(p, "wipe")]), ("click", [(first, "rise")])])
notes(s, """
Put the tutor-mode text somewhere they can copy it (printed handout, or a shared link).
Before they paste the code into GitHub: explain-back to their partner. What does the
button do? Which part makes it that color?
""")

# 19 ─ Your URL ─────────────────────────────────────────────────────────
s = blank(prs, INK)
k = text(s, 0.8, 1.3, 11, 0.5, "YOUR SITE LIVES HERE", size=18, color=CYAN, bold=True)
url = text(s, 0.8, 2.0, 11.8, 1.6,
           [[("https://", {"color": SLATE}), ("YOUR-USERNAME", {"color": ORANGE}),
             (".github.io/", {"color": WHITE}), ("my-first-site", {"color": YELLOW})]],
           size=30, font=MONO, bold=True)
tips = [text(s, 0.8, 4.0 + i * 0.75, 11.5, 0.7, t, size=24, color=WHITE)
        for i, t in enumerate(["Takes 1–2 minutes. Refresh.",
                               "Open it on your phone. Text it to someone.",
                               "Stuck? Backup: drag your folder onto app.netlify.com/drop"])]
set_transition(s, "zoom")
anim_steps(s, [("auto", [(k, "fade"), (url, "wipe")]), ("click", [(t, "rise") for t in tips])],
           stagger=300)
notes(s, """
As people get live: have them type their URL into a shared doc / form so it can go
on the "wall of URLs" next.
""")

# 20 ─ Shipped ──────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Wall of URLs  →  then:", "What “shipped” means here.", GREEN)
crit = [("A public URL that loads on a phone", "✓ done today"),
        ("At least one interactive thing that works", "weeks 2–4"),
        ("A README: what the AI did, what you did", "week 5")]
rows = []
for i, (c, when) in enumerate(crit):
    y = 2.2 + i * 1.4
    rows.append(boxed(s, 0.7, y, 11.95, 1.15, WHITE,
                      [[(f"{i + 1}   ", {"color": GREEN, "font": HEAD}), c,
                        (f"     {when}", {"color": ORANGE if i else GREEN, "size": 18})]],
                      line=MIST, size=24, bold=True, anchor=MSO_ANCHOR.MIDDLE))
set_transition(s, "fade")
anim_steps(s, [("click", [(r, "wipe")]) for r in rows])
notes(s, """
First: show the shared list of everyone's URLs on the projector and click a few. Cheer.
Then the three criteria. Today you hit #1. By demo day you'll hit all three.
""")

# 21 ─ Roadmap ──────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "The next 6 weeks", "Where this is going.")
weeks = [("1", "Kickoff", "live URL"), ("2", "Idea + scope", "privacy"), ("3", "Build", "bug bounty"),
         ("4", "Build + debug", "bias"), ("5", "Polish + test", "who owns it?"),
         ("6", "DEMO DAY", "show the world")]
track = rect(s, 1.2, 3.35, 10.9, 0.1, INK)
wk = []
for i, (n, t, cp) in enumerate(weeks):
    x = 0.75 + i * 2.1
    last = i == 5
    d = rect(s, x + 0.35, 2.85, 1.1, 1.1, ORANGE if last else (CYAN if i == 0 else WHITE),
             None if (last or i == 0) else INK, shape=MSO_SHAPE.OVAL)
    text(s, 0, 0, 0, 0, n, shape=d, size=30, font=HEAD, align=PP_ALIGN.CENTER,
         anchor=MSO_ANCHOR.MIDDLE, color=WHITE if (last or i == 0) else INK)
    lab = text(s, x - 0.1, 4.15, 2.0, 1.6,
               [[(t, {"font": HEAD, "size": 19, "color": ORANGE if last else INK})],
                [("checkpoint: " + cp, {"size": 14, "color": SLATE})]],
               size=19, align=PP_ALIGN.CENTER)
    wk.append((d, lab))
set_transition(s, "fade")
anim_steps(s, [("auto", [(track, "wipe")] + [x for d, l in wk for x in ((d, "zoom"), (l, "fade"))])],
           stagger=180)
notes(s, """
Point at Demo Day: parents, library staff, and guests will see what you built.
Each week also has an AI Checkpoint like today's.
""")

# 22 ─ Closing ──────────────────────────────────────────────────────────
s = blank(prs, INK)
rect(s, 0, 0, 0.35, 7.5, ORANGE)
t = text(s, 0.9, 1.0, 11, 1.2, "Before next week", size=54, font=HEAD, color=WHITE)
hw = [("1", "Bring 3 project ideas.", "What would you actually use, or show off?"),
      ("2", "Journal: one thing the AI got wrong today.", "Be specific."),
      ("3", "Show your site to one person.", "Parent, friend, sibling.")]
hws = [text(s, 0.9, 2.6 + i * 1.15, 11.5, 1.1,
            [[(n + "   ", {"color": ORANGE, "font": HEAD}), (a, {"bold": True})],
             [("      " + b, {"color": CYAN, "size": 18})]], size=26, color=WHITE)
       for i, (n, a, b) in enumerate(hw)]
bye = text(s, 0.9, 6.3, 11, 0.7, "See you next week.  Build it. Ship it. Question it.",
           size=20, color=SLATE, bold=True)
set_transition(s, "fade", "slow")
anim_steps(s, [("auto", [(t, "rise")] + [(h, "rise") for h in hws] + [(bye, "fade")])],
           stagger=350)
notes(s, """
Hand out prompt-journal sheets; 3 minutes to write the first entry before leaving.
Exit ticket (optional): one word for how today felt.
""")

out = Path(__file__).parent / "session-01-kickoff.pptx"
prs.save(out)
print("saved", out, "slides:", len(prs.slides))
