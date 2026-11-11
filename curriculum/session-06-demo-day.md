# Session 6: Demo Day — Built it. Shipped it. Questioned it.

**Goal:** every teen presents a live site to a real audience in under 3 minutes, including one thing the AI got wrong. We also collect the outcome data for future grants and for the Memphis Public Libraries pitch.

**Deck:** [`decks/session-06-demo-day.pptx`](decks/session-06-demo-day.pptx), plus printable [`decks/session-06-certificates.pptx`](decks/session-06-certificates.pptx).

## Personalize the deck (the night before)

Open [`decks/build_session_06.py`](decks/build_session_06.py) and fill in three things at the top:

- `DEMOS`: each presenter's **first name only** and their project title, in demo order. Every entry gets its own "Now presenting" slide and its own certificate.
- `STATS`: the real numbers. How many teens took part, how many sites shipped, and how many AI mistakes were caught. Count the AI mistakes from the prompt journals.
- `AI_FAILS`: 3 of the best "the AI got it wrong" moments from the journals. Ask each teen first, and don't include names.

Then rebuild and check the decks:

```bash
uv run --with python-pptx python curriculum/decks/build_session_06.py
uv run --with python-pptx python curriculum/decks/check_deck.py curriculum/decks/session-06-*.pptx
```

## Before guests arrive

- [ ] Use one presenting laptop. Open every teen's live URL in its own tab, in demo order. Have backup screenshots in a folder.
- [ ] Do a 15-minute tech check with teens: each one loads their site on the projector once.
- [ ] Print the certificates. Get the adult sponsor and library staff to sign them.
- [ ] Get the teen exit survey ready on paper or as a form, and keep it anonymous. The items are below.
- [ ] Print the demo rubric for leaders (below).
- [ ] Optional: snacks. The library may have rules about food in the room, so check first.
- [ ] **Photos:** take photos only of teens whose families signed the photo release. Check the list before the event.

## Run of show (120 min)

| Time | Slides | Block | Who leads |
|---|---|---|---|
| 0:00–0:15 | (none) | Tech check with teens only; guests arrive | Both |
| 0:15–0:25 | 1–6 | **Welcome guests**: what we did, the numbers, the 4 habits, how demos work | Leaders A and B |
| 0:25–1:25 | 7 → demos | **Demos**: 3 minutes each, with a short break halfway if there are more than 10 demos | Leader A emcees, Leader B keeps time and scores the rubric |
| 1:25–1:33 | highlight reel | **"The AI got it wrong"**: 3 of the best catches | Leader B |
| 1:33–1:43 | thanks, certificates | **Thank you, and certificates** | Leaders, adult sponsor, library staff |
| 1:43–1:55 | survey, what's next | Teens fill out the exit survey while guests walk around and try sites on teens' laptops | Both |
| 1:55–2:00 | closing | Closing | Leader A |

Timing: with N teens, demos take about N × 3.5 minutes. With more than 17 teens, cut the highlight reel or start 10 minutes earlier.

## Demo rubric (leaders, during demos)

Score each teen quietly. This is program data, not a grade, and it never gets shared with teens or families.

| | Score |
|---|---|
| Live URL works, including on a phone | yes / no |
| At least one interactive feature works | yes / no |
| README includes AI credits | yes / no (check the repo afterward) |
| Can explain how one feature works, in their own words | 0 = no · 1 = partly · 2 = clearly |
| Names a specific AI mistake and how they caught it | 0 = no · 1 = vague · 2 = specific |

If time allows, the emcee can ask one follow-up question: "Show us the code that makes [feature] work. What does it do?"

## Teen exit survey (anonymous, "before vs. now")

For each statement, the teen circles a number from 1 to 5 for **before the workshop** and again for **now**:

1. I can build a website and put it on the internet.
2. I can read an error message and figure out what it means.
3. I check what an AI tells me before I trust it.
4. I know what I should never share with an AI.
5. I can explain how a chatbot comes up with its answers.

Then three questions:

- What's one thing an AI got wrong that you caught?
- What would you change about this workshop?
- Would you tell a friend to join? (yes / maybe / no)

## After the event (organizers)

- [ ] Fill in the outcomes table in `docs/` (create it the first time):
  - teens enrolled vs. finished
  - attendance per session
  - sites shipped
  - rubric averages
  - before-and-after survey averages
- [ ] Debrief together within a week: what worked, what to cut, what to change. Record it in `docs/decisions.md`.
- [ ] Use the numbers for the Collierville Rotary 2027 application, the Hack Club club application, and the CLOUD901 / Memphis Library Foundation pitch.
- [ ] Ask 1–2 strong teens if they'd come back as junior mentors next season.
