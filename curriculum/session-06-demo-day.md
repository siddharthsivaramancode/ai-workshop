# Session 6: Demo Day — Built it. Shipped it. Questioned it.

**Goal:** every teen (10–15 of them) presents a live site to a real audience in about 3 minutes, including one thing the AI got wrong. We also collect the outcome data for future grants and for the Memphis Public Libraries pitch.

**Deck:** [`slideshows/session-06-demo-day.pptx`](../slideshows/session-06-demo-day.pptx), plus printable [`slideshows/session-06-certificates.pptx`](../slideshows/session-06-certificates.pptx).

## Personalize the deck (the night before)

Open [`decks/build_session_06.py`](decks/build_session_06.py) and fill in three things at the top:

- `DEMOS`: each presenter's **first name only** and their project title, in demo order. Every entry gets its own "Now presenting" slide and its own certificate.
- `STATS`: the real numbers. How many teens took part, how many sites shipped, and how many AI mistakes were caught. Count the AI mistakes from the prompt journals.
- `AI_FAILS`: 3 of the best "the AI got it wrong" moments from the journals. Ask each teen first, and don't include names.

Then rebuild and check the decks:

```bash
uv run --with python-pptx python curriculum/decks/build_session_06.py
uv run --with python-pptx python curriculum/decks/check_deck.py slideshows/session-06-*.pptx
```

## Before guests arrive

- [ ] Use one presenting laptop. Open every teen's live URL in its own tab, in demo order. Have backup screenshots in a folder.
- [ ] Do a 15-minute tech check with teens: each one loads their site on the projector once.
- [ ] Print the certificates. Get the adult sponsor and library staff to sign them.
- [ ] Get the teen exit survey ready on paper or as a form, and keep it anonymous. The items are below.
- [ ] Print the demo rubric for leaders (below).
- [ ] Optional: snacks. The library may have rules about food in the room, so check first.
- [ ] **Photos:** take photos only of teens whose families signed the photo release. Check the list before the event.

## Run of show (about 75 min)

Teens arrive 15 minutes before guests for the tech check, so the guest part runs about an hour.

| Time | Slides | Block | Who leads |
|---|---|---|---|
| −0:15–0:00 | (none) | Tech check, teens only: each loads their site on the projector once | Both |
| 0:00–0:06 | 1–6 | **Welcome guests**: what we did, the numbers, the 4 habits, how demos work | Leaders A and B |
| 0:06–0:46 | 7 → demos | **Demos**: about 3 minutes each, in the 4-part format from Session 5 | Leader A emcees, Leader B keeps time and scores the rubric |
| 0:46–0:51 | highlight reel | **"The AI got it wrong"**: 3 of the best catches | Leader B |
| 0:51–0:57 | thanks, certificates | **Thank you, and certificates** | Leaders, adult sponsor, library staff |
| 0:57–1:05 | survey, what's next | Teens fill out the exit survey while guests try sites on teens' laptops. Hand out the **Build Lab 6: keep building** sheet (below). | Both |

Timing: budget about 3 minutes per demo **plus 40 seconds of changeover** (switching tabs, walking up). 10 teens ≈ 37 min, 12 ≈ 44 min, 15 ≈ 55 min. From 12 teens up, cap demos at 2.5 minutes; at 15, also cut the highlight reel. Keep the tabs pre-opened in order to make changeovers fast.

## Build Lab 6: keep building (handout, not a lecture)

Demo day has no time for teaching, so the last rung of the ladder is a one-page sheet teens take home. Each row: what it is, and one free place to learn it.

| Next step | What it is | Free place to learn |
|---|---|---|
| Your own domain | A name like `yourname.dev` instead of `github.io`. Costs money, so ask a parent. | GitHub Pages docs: "custom domain" |
| Saving data | `localStorage` keeps a to-do list or high score in the visitor's browser | MDN: "Web Storage API" |
| Free APIs | Pull in live data (jokes, space photos, weather) from public APIs that need no key | MDN: "Fetching data from the server" |
| A real code editor | VS Code on your own computer, with GitHub Copilot (free Pro for verified students) | VS Code docs |
| Frameworks | React and friends: how big sites are built. Learn plain HTML/CSS/JS first. | The Odin Project, freeCodeCamp |
| Computer science | How it all works underneath, with the CS50 Duck as a tutor | Harvard CS50x (free online) |
| AI agents | Tools like Claude Code that build with you (18+), and what you'd need to check | Come back as a junior mentor and see the demo again |

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
5. I can explain the steps an AI like ChatGPT takes to write an answer.
6. I can explain the difference between an AI model, a chatbot and an agent.
7. I can spot ways an AI might be unfair or wrong.

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
