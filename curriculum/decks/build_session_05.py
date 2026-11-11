"""Session 5 deck: Polish + test — hand it over, watch closely. Checkpoint: who owns it?

Run from repo root:
    uv run --with python-pptx python curriculum/decks/build_session_05.py
Slide numbers match the run of show in curriculum/session-05-polish-and-test.md.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from deckkit import *  # noqa: E402,F403

prs = new_deck()

# 1 ─ Title ──────────────────────────────────────────────────────────────
s = blank(prs, INK)
rect(s, 0, 0, 0.35, 7.5, ORANGE)
k = text(s, 0.9, 0.8, 8, 0.5, "SESSION 5 OF 6  ·  POLISH + TEST", size=16, color=CYAN, bold=True)
l1 = text(s, 0.85, 1.6, 11.5, 1.5, "Hand it over.", size=88, font=HEAD, color=WHITE)
l2 = text(s, 0.85, 3.1, 11.5, 1.5, "Watch closely.", size=88, font=HEAD, color=ORANGE)
sub = text(s, 0.9, 5.4, 11, 1.2,
           ["Today: real users, real fixes, and who owns AI code.",
            ("Build it. Ship it. Question it.", {"color": CYAN, "size": 18})],
           size=24, color=WHITE, bold=True)
set_transition(s, "fade", "slow")
anim_steps(s, [("auto", [(k, "fade"), (l1, "rise"), (l2, "rise"), (sub, "fade")])], stagger=400)
notes(s, "One week until demo day. Today is about making your site work for OTHER people.")

# 2 ─ Check-in ──────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Homework check-in", "Someone else tried your site.")
qs = [("Who tried it?", CYAN), ("Where did they get confused?", ORANGE), ("Did anything surprise you?", GREEN)]
qc = [boxed(s, 0.7 + i * 4.1, 2.2, 3.8, 2.8, WHITE, t, line=c, size=26, font=HEAD, color=c,
            align=PP_ALIGN.CENTER)
      for i, (t, c) in enumerate(qs)]
tip = boxed(s, 0.7, 5.5, 11.95, 1.1, INK, "Their confusion isn't their fault. It's your next fix.",
            size=22, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(c, "rise") for c in qc]), ("click", [(tip, "wipe")])], stagger=200)
notes(s, "3–4 quick shares. If nobody did the homework, that's fine — today's test covers it.")

# 3 ─ Section ───────────────────────────────────────────────────────────
s = section(prs, "01", "Silent user testing.", "Hand it over. Say nothing. Learn everything.", bg=CYAN)
notes(s, "This is how real product teams test. It's uncomfortable — that's why it works.")

# 4 ─ Rules ─────────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "The rules · 2 rounds · 5 minutes each", "Tester talks. Builder doesn't.", CYAN)
tester = boxed(s, 0.7, 2.0, 5.85, 3.4, WHITE,
               [[("TESTER", {"font": HEAD, "size": 28, "color": CYAN})], "",
                "• Gets your URL + one task", "  (“Try to get a perfect score”)",
                "• Thinks out loud the whole time", "• Is honest — that's the gift"],
               line=CYAN, size=19, bold=True, anchor=MSO_ANCHOR.TOP)
builder = boxed(s, 6.8, 2.0, 5.85, 3.4, INK,
                [[("BUILDER", {"font": HEAD, "size": 28, "color": ORANGE})], "",
                 "• Says nothing. Nothing!", "• No pointing, no hints",
                 "• Writes down everything", "• Says “thank you” at the end"],
                size=19, color=WHITE, bold=True, anchor=MSO_ANCHOR.TOP)
swap = boxed(s, 0.7, 5.75, 11.95, 0.9, YELLOW, "Then swap. Then find a new partner from another table.",
             size=21, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(tester, "rise")]), ("click", [(builder, "rise")]), ("click", [(swap, "wipe")])])
notes(s, """
Leader B keeps time: 5 minutes per test, then swap roles, then new partners for round 2.
If a builder starts explaining, call "Freeze! Write it down." — the moment of confusion
is the most valuable thing in the test.
""")

# 5 ─ Notes sheet ───────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Builder: write these down", "Your notes sheet.")
cols = [("Where they paused", "or looked lost", ORANGE),
        ("What they clicked", "that didn't do anything", CYAN),
        ("What they said", "word for word", GREEN)]
cc = [boxed(s, 0.7 + i * 4.1, 2.0, 3.8, 4.6, WHITE,
            [[(a, {"font": HEAD, "size": 22, "color": c})], [(b, {"size": 17, "color": SLATE})], "", "",
             [("______________", {"color": MIST})], [("______________", {"color": MIST})],
             [("______________", {"color": MIST})]],
            line=c, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.TOP)
      for i, (a, b, c) in enumerate(cols)]
set_transition(s, "fade")
anim_steps(s, [("click", [(c, "rise") for c in cc])], stagger=250)
notes(s, "Hand out the printed sheets. Quotes are gold: 'wait, what does this button do?'")

# 6 ─ Top 2 fixes ───────────────────────────────────────────────────────
s = blank(prs)
heading(s, "After both rounds", "Pick your top 2 fixes.")
grid = [("Confusing + easy to fix", "DO FIRST", GREEN), ("Confusing + hard to fix", "simplify it", ORANGE),
        ("Not confusing + easy", "if there's time", CYAN), ("New feature idea", "→ Someday list", SLATE)]
gc = [boxed(s, 0.7 + (i % 2) * 6.1, 1.95 + (i // 2) * 2.0, 5.85, 1.8, WHITE,
            [[(a, {"font": HEAD, "size": 22})], [(b, {"size": 20, "color": c, "font": HEAD})]],
            line=c, bold=True, align=PP_ALIGN.CENTER)
      for i, (a, b, c) in enumerate(grid)]
rule = boxed(s, 0.7, 6.0, 11.95, 0.75, INK, "Fix what confused people — not what you wish you'd added.",
             size=20, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(g, "zoom")]) for g in gc] + [("click", [(rule, "wipe")])])
notes(s, "Everyone circles their top 2 on the notes sheet. Leaders glance at each — these are today's build goals.")

# 7 ─ Section ───────────────────────────────────────────────────────────
s = section(prs, "02", "Who owns it?", "AI Checkpoint · and what couldn't the AI do?")
notes(s, "Everyone stand up. This one's physical.")

# 8 ─ Corners rules ─────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Stand up · pick a side", "Agree or disagree?")
sides = [("AGREE", GREEN, "this wall"), ("NOT SURE", YELLOW, "the middle"), ("DISAGREE", RED, "that wall")]
sd = [boxed(s, 0.7 + i * 4.1, 2.1, 3.8, 2.6, c,
            [[(a, {"font": HEAD, "size": 32})], "", [(b, {"size": 20})]],
            color=INK if c == YELLOW else WHITE, bold=True, align=PP_ALIGN.CENTER)
      for i, (a, c, b) in enumerate(sides)]
how = boxed(s, 0.7, 5.1, 11.95, 1.5, WHITE,
            ["After each statement: one person from each side says why.",
             [("You can switch sides if someone convinces you.", {"color": ORANGE})]],
            line=MIST, size=21, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(x, "zoom") for x in sd]), ("click", [(how, "rise")])], stagger=200)
notes(s, "Point to the actual walls / signs. Keep each statement to ~3 minutes.")

# 9–12 ─ Statements ─────────────────────────────────────────────────────
statements = [
    ("If the AI wrote most of the code, it's not really my project.",
     "Ask: what did YOU decide? The idea, the design, what to fix, what to cut?"),
    ("You should always tell people when AI helped you make something.",
     "Ask: does it matter if it's school, a job, or just for fun?"),
    ("The AI company owns the code it wrote for you.",
     "Don't reveal the answer yet — next slide."),
    ("Learning to code is pointless now that AI can do it.",
     "Ask: could you have fixed the bug bounty without knowing how to read code?"),
]
for i, (st, note) in enumerate(statements):
    s = blank(prs, INK)
    n = text(s, 0.8, 0.9, 6, 0.6, f"STATEMENT {i + 1} OF 4", size=18, color=CYAN, bold=True)
    q = text(s, 0.8, 1.7, 11.8, 3.6, [[("“", {"color": ORANGE}), st, ("”", {"color": ORANGE})]],
             size=46, font=HEAD, color=WHITE, spacing=0.95)
    legend = text(s, 0.8, 6.2, 11.8, 0.6,
                  [[("AGREE", {"color": GREEN}), "   ·   ", ("NOT SURE", {"color": YELLOW}), "   ·   ",
                    ("DISAGREE", {"color": RED})]], size=22, font=HEAD, color=WHITE)
    set_transition(s, "push")
    anim_steps(s, [("auto", [(n, "fade"), (q, "rise"), (legend, "fade")])], stagger=300)
    notes(s, f"Move to a side! Then one voice from each side.\n{note}\nOptional: count each side for the measurement sheet.")

# 13 ─ What we know ─────────────────────────────────────────────────────
s = blank(prs)
heading(s, "What we actually know", "So… who owns it?")
facts = [("You, usually.", "Most AI companies' terms say the output belongs to the user.", GREEN),
         ("But not all of it is protected.", "In the US, work made purely by AI can't be copyrighted. "
                                             "What you wrote, changed, or arranged can be.", ORANGE),
         ("And it might look like someone else's.", "AI can repeat code it learned from. Credit it honestly.", CYAN)]
fc = [boxed(s, 0.7, 1.95 + i * 1.45, 11.95, 1.3, WHITE,
            [[(a, {"font": HEAD, "color": c})], [(b, {"size": 17, "color": SLATE})]],
            line=c, size=23, bold=True, anchor=MSO_ANCHOR.MIDDLE)
      for i, (a, b, c) in enumerate(facts)]
foot = text(s, 0.7, 6.4, 12, 0.5, "Not legal advice — and the rules are still being figured out.",
            size=14, color=SLATE)
set_transition(s, "fade")
anim_steps(s, [("click", [(f, "wipe")]) for f in fc] + [("click", [(foot, "fade")])])
notes(s, """
Answer to statement 3: usually the user owns it under the tool's terms (check the specific
tool). The US Copyright Office says purely AI-generated material isn't copyrightable —
human contributions are. Takeaway: the parts YOU make are the parts that are truly yours,
and being honest about the rest is the right move. That's what the README credits are for.
""")

# 14 ─ What couldn't the AI do ──────────────────────────────────────────
s = blank(prs)
heading(s, "Check your prompt journal", "What couldn't the AI do for you?", GREEN)
did = [("Pick the idea", "it didn't know what YOU wanted"), ("Know who it's for", "your users, your friends"),
       ("Notice it was wrong", "you caught those bugs"), ("Test with real people", "you watched them today"),
       ("Decide “good enough”", "and what to cut")]
dc = [boxed(s, 0.7 + (i % 3) * 4.1, 1.95 + (i // 3) * 2.05, 3.8, 1.8, WHITE,
            [[(a, {"font": HEAD, "size": 21})], [(b, {"size": 16, "color": SLATE})]],
            line=GREEN, bold=True, align=PP_ALIGN.CENTER)
      for i, (a, b) in enumerate(did)]
job = boxed(s, 8.9, 4.0, 3.75, 1.8, INK, [[("That's the job.", {"font": HEAD, "size": 26, "color": YELLOW})]],
            color=WHITE, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(d, "rise") for d in dc]), ("click", [(job, "zoom")])], stagger=200)
notes(s, """
Ask the room first: flip through your journals — what did YOU have to do that the AI
couldn't? Take answers, THEN click to reveal. Whatever happens with AI and jobs, these
are the skills that stay valuable: judgment, taste, knowing people, catching mistakes.
""")

# 15 ─ Section ──────────────────────────────────────────────────────────
s = section(prs, "03", "Polish.", "Top 2 fixes. Phone check. Checklist.", bg=CYAN)
notes(s, "~40 minutes. Polish only — no big new features this week.")

# 16 ─ Phone check ──────────────────────────────────────────────────────
s = blank(prs)
heading(s, "The #1 phone fix", "Is this line in your <head>?", CYAN)
code = boxed(s, 0.7, 2.0, 11.95, 1.4, INK,
             [[("<meta ", {"color": WHITE}), ("name=", {"color": CYAN}), ("\"viewport\" ", {"color": YELLOW}),
               ("content=", {"color": CYAN}), ("\"width=device-width, initial-scale=1\"", {"color": YELLOW}),
               (">", {"color": WHITE})]],
             size=18, font=MONO, bold=True, align=PP_ALIGN.CENTER)
why = text(s, 0.7, 3.55, 12, 0.6, "Without it, phones shrink your whole page to look like a tiny desktop site.",
           size=19, color=SLATE, bold=True)
checks = [("Text readable", "without zooming"), ("Buttons big enough", "to tap with a thumb"),
          ("No sideways scrolling", "nothing wider than the screen")]
ck = [boxed(s, 0.7 + i * 4.1, 4.45, 3.8, 1.9, WHITE,
            [[("☐ " + a, {"font": HEAD, "size": 20})], [(b, {"size": 16, "color": SLATE})]],
            line=MIST, bold=True, align=PP_ALIGN.CENTER)
      for i, (a, b) in enumerate(checks)]
set_transition(s, "fade")
anim_steps(s, [("auto", [(code, "wipe")]), ("click", [(why, "fade")]), ("click", [(c, "rise") for c in ck])],
           stagger=200)
notes(s, "Most AI-generated pages include this, but check. Then test on your real phone, not just a narrow window.")

# 17 ─ Polish checklist ─────────────────────────────────────────────────
s = blank(prs)
heading(s, "Before demo day", "The polish checklist.")
items = ["Page title shows in the browser tab", "No spelling mistakes", "Colors are easy to read",
         "No red errors in the Console", "Works after a refresh", "No personal info anywhere"]
ic = [boxed(s, 0.7 + (i % 2) * 6.1, 1.95 + (i // 2) * 1.5, 5.85, 1.3, WHITE,
            [[("☐  ", {"color": ORANGE}), t]], line=MIST, size=21, bold=True, anchor=MSO_ANCHOR.MIDDLE)
      for i, t in enumerate(items)]
set_transition(s, "fade")
anim_steps(s, [("click", [(c, "rise") for c in ic])], stagger=150)
notes(s, "Partners check each other's sites against the list. A leader confirms 'no personal info' before demo day.")

# 18 ─ README ───────────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Last 15 minutes", "Write your README.", GREEN)
rd = boxed(s, 0.7, 1.95, 7.7, 4.75, INK,
           [[("# [Project name]", {"color": YELLOW})], "[Your one-sentence pitch]",
            "Live: [your URL]", "",
            [("## AI credits", {"color": YELLOW})],
            "The AI helped me: ...", "I did myself: ...", "The AI got this wrong: ...", "",
            [("## What's next", {"color": YELLOW})], "[Your Someday list]"],
           size=17, font=MONO, color=WHITE, bold=True, anchor=MSO_ANCHOR.TOP)
side = boxed(s, 8.8, 1.95, 3.85, 4.75, YELLOW,
             [[("Why “AI credits”?", {"font": HEAD, "size": 21})], "",
              "Real developers credit the tools and code they used.", "",
              "Honesty about the AI makes what YOU did stand out."],
             size=17, bold=True, anchor=MSO_ANCHOR.TOP)
set_transition(s, "fade")
anim_steps(s, [("auto", [(rd, "wipe")]), ("click", [(side, "rise")])])
notes(s, """
In GitHub: Add file → Create new file → README.md. The # makes a heading.
It shows up on your repo's front page. The AI-credits section is required for "shipped".
""")

# 19 ─ Demo format ──────────────────────────────────────────────────────
s = blank(prs)
heading(s, "Next week · 3 minutes max", "Your demo, in 4 parts.")
parts = [("Pitch", "15 sec", "your one sentence", ORANGE), ("Show it", "90 sec", "live, on the projector", CYAN),
         ("AI got it wrong", "30 sec", "one real example", RED), ("What's next", "15 sec", "your Someday list", GREEN)]
widths = [2.3, 4.4, 2.95, 2.4]
pc, x = [], 0.7
for (a, t, b, c), w in zip(parts, widths):
    pc.append(boxed(s, x, 2.1, w - 0.1, 2.6, c,
                    [[(a, {"font": HEAD, "size": 22})], [(t, {"size": 26, "font": HEAD})], "",
                     [(b, {"size": 15})]],
                    color=WHITE, bold=True, align=PP_ALIGN.CENTER))
    x += w - 0.1 + 0.1
prac = boxed(s, 0.7, 5.15, 11.95, 1.5, INK,
             ["Practice it out loud. Twice. With a timer.",
              [("Have a backup: a screenshot, in case the Wi-Fi dies.", {"color": YELLOW, "size": 19})]],
             size=22, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
set_transition(s, "fade")
anim_steps(s, [("click", [(p, "rise") for p in pc]), ("click", [(prac, "wipe")])], stagger=250)
notes(s, "Widths roughly match the time each part gets. 'AI got it wrong' is required — it's our signature.")

# 20 ─ Closing ──────────────────────────────────────────────────────────
s = closing(prs, [("Practice your demo out loud twice.", "Time it. Under 3 minutes."),
                  ("Invite someone to demo day.", "Family, friends, a teacher."),
                  ("Final fixes committed and live.", "Check it on your phone the night before.")])
notes(s, "Give out the demo-day invite with date, time and room. Remind: no big changes the night before!")

out = OUT_DIR / "session-05-polish-and-test.pptx"
prs.save(out)
print("saved", out, "slides:", len(prs.slides))
