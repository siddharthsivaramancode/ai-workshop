# Session 2: Idea and scope — Big idea, small start

**Goal:** every teen leaves with (1) a live URL from Session 1, (2) a one-sentence pitch, (3) features split into Must, Nice and Someday, (4) a first version of their Must feature committed, and (5) a clear picture of where their words and photos go once they hit send.

**Length:** 70 minutes · 10–15 teens, mostly beginners.

**Deck:** [`slideshows/session-02-idea-and-scope.pptx`](../slideshows/session-02-idea-and-scope.pptx). It was built for the old 2-hour format and hasn't been rebuilt in the Session 1 style yet. Follow the timings below and skip slides to fit.

## Builds on Session 1

| Session 1 idea | How it shows up today |
|---|---|
| Context window and app "memory" | Privacy: what you paste is on the page, the app may save notes about you, and chats can be stored. |
| Training vs. inference | Your chat doesn't change the model now, but it may be used to train a *future* one. |
| Prompting: goal, details, limits, check | The planning prompt for feature 1 is built the same way. |
| Tutor mode, explain-back | Required before the first commit. |

**Words to recall out loud:** context window, training data, inference, tutor mode.

## Before the session

- [ ] Look at the Session 1 URL list. Message anyone who isn't live yet. They'll get the first 10 minutes of build time with a leader.
- [ ] Print the privacy sorting cards (9 cards, listed below), one set per pair.
- [ ] Print pitch sheets: the pitch formula, a Must / Nice / Someday box, and room for a sketch.
- [ ] Put the planning prompt (below) in the shared doc or on a QR code.
- [ ] Bring the dream-site sticky notes from Session 1.
- [ ] Open one AI app's privacy or data-controls page so you can show it on the projector.

## Run of show (70 min)

| Time | Block | What happens | Who leads |
|---|---|---|---|
| 0:00–0:05 | **Check-in** | Two volunteers show their Session 1 page, and one reads an "AI got it wrong" journal entry. | Leader A |
| 0:05–0:17 | **AI Checkpoint: Privacy** | Pairs sort 9 cards into Safe, Depends and Not safe (4 min). Reveal the answers. Then a 3-minute recap: chats are stored, may train future models, and your GitHub repo is public forever. Show the data-controls page. | Leader B |
| 0:17–0:30 | **Pick and pitch** | Menu tiers, then the 3-question test. Each teen writes a one-sentence pitch and a Must / Nice / Someday list, then reads the pitch to their partner. | Leader A |
| 0:30–0:52 | **Build feature 1** | Paste the planning prompt, ask for step 1 only, build the smallest version, explain it back to the partner, and commit with a clear message. Teens without a live URL finish that first. | Both leaders circulate |
| 0:52–1:02 | **Build Lab 2: HTML + CSS** | See below. | Leader A teaches, both circulate |
| 1:02–1:10 | **Wrap** | Check the site on a phone, write a journal entry, then homework. | Leader B |

## Build Lab 2: HTML and CSS, the skeleton and the look (10 min)

**Teach (3 min):** every page is a tree of *tags*: `<h1>` a big heading, `<p>` a paragraph, `<a href="…">` a link, `<img src="…" alt="…">` an image, `<button>` a button. Right-click any website → **View page source**: every site is made of these. Then the look: CSS rules are *selector* `{ property: value; }`, like `h1 { color: tomato; }`. Right-click → **Inspect** opens DevTools, where you can change any style live.
**Do (6 min):** by hand, in their own `index.html`: add one link and one image (a free image URL or an icon, **never a photo of a person**) with a real `alt` description. Then try a color change in DevTools and type the keeper into their real `<style>`. Commit.
**Check (1 min):** "Which tag made your link? Why did your DevTools change vanish when you refreshed?" (DevTools only changes your browser's copy, not the file on GitHub.)
**Progress check:** every teen is live and has a repo with at least 2 commits.

## The planning prompt

Same shape as Session 1's tutor mode:

> **Goal:** I'm building [your one-sentence pitch].
> **Details:** My Must feature is [feature]. It should [what it does when someone uses it].
> **Limits:** I'm a beginner. Don't write code yet. Give me a plan of 3–5 small steps. Each step should be under 40 lines of code.
> **Check:** Ask me one question about my idea before you plan.

Then: "Now help me with step 1 only. Explain it before showing code."

## Privacy sort: the 9 cards and answers

| Safe | Depends | Not safe |
|---|---|---|
| Your favorite band | Your first name. Fine to use, but a nickname is safer on a public site. | The name of your school |
| A homework question | Your pet's name. It's a common answer to password security questions. | A photo of a friend. They didn't agree to it. |
| Your project idea | Your city. Fine alone, but combined with other details it can identify you. | Your password |

**The point to land:** "Depends" is the most important column. Small details add up. A first name, a city and a photo of your street can together point to one person. And photos can carry hidden location data, or show landmarks that give away where they were taken.

## If things go wrong

- **A teen still has no live URL:** that's their whole build block. A live "Hi, I'm…" page beats a half-built feature.
- **A teen can't pick an idea:** suggest flashcards for a class they're taking. It can be built in two weeks and they'll actually use it.
- **The idea is too big** (logins, a database, AI inside the app, multiplayer): the dream goes in the Someday column. Ask: "What's the one screen that would prove it's cool?" Build that screen.
- **The AI writes 300 lines at once:** back to the planning prompt. Step 1 only, under 40 lines.
- **A teen copies AI code without reading it:** explain-back before the commit. "Point at the line that makes X happen."

## Homework

1. Finish feature 1 if it isn't done, and make sure it's live.
2. Open View page source on one website you use. Find one `<a>` tag and one `<img>` tag. Then use Inspect to change its headline color (only on your screen).
3. Journal: one thing you asked the AI this week and whether its plan was any good.
4. Show your Must feature to one person and ask them what they expected it to do.

## Measure

- Attendance, and how many returned from Session 1
- How many teens are live (target: everyone by the end of today)
- How many wrote a pitch and a Must / Nice / Someday list
- How many committed feature 1
