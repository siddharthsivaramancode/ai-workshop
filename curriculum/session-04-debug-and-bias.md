# Session 4: Build and debug — Break it, fix it

**Goal:** every teen leaves with (1) the debug-first habit: read the error, find the line, guess why, and try one fix before asking the AI; (2) a first-hand look at bias in AI output and an understanding of where it comes from; and (3) their Must feature done and a Nice feature started.

**Deck:** [`slideshows/session-04-debug-and-bias.pptx`](../slideshows/session-04-debug-and-bias.pptx). The speaker notes on each slide hold the script.

## Before the session

- [ ] **Practice the live debug** with [`demos/broken-coin-flip.html`](demos/broken-coin-flip.html). Open it in Chrome with the Console open, and fix the 3 bugs in the order below. Use the projector with the zoom turned up.
- [ ] **Practice Teachable Machine** on the leader laptop (teachablemachine.withgoogle.com → Image Project). It needs a webcam. Only the leader's laptop is used, so teens don't share webcam images.
- [ ] Have a whiteboard or a big sheet of paper ready for the bias tally on slide 13.
- [ ] Optional, but popular: bring a rubber duck, or a few of them.

## Run of show (120 min)

| Time | Slides | Block | Who leads |
|---|---|---|---|
| 0:00–0:10 | 1–2 | **Bug of the week.** 3–4 teens share a bug from homework, saying what they expected and what happened instead. | Leader A |
| 0:10–0:35 | 3–10 | **Debug like a detective.** How to open the Console, the 4-step habit, decoding common error messages, what to do when there's no error, `console.log`, the rubber duck, and the live debug of the coin flip page | Leader B |
| 0:35–0:57 | 11–16 | **AI Checkpoint: Bias.** Pairs run the "4 stories" prompt and the room tallies results on the board. Then why bias happens, a Teachable Machine demo, and what we can do about it. | Leader A, with Leader B at the board |
| 0:57–1:45 | 17–18 | **Build.** Finish the Must feature and start a Nice one. The debug-first rule applies: show the error and your guess before asking for help. | Both leaders circulate |
| 1:45–1:55 | 19 | Commit, check the site live, journal | Leader A |
| 1:55–2:00 | 20 | Homework | Leader B |

## Live debug answer key (`demos/broken-coin-flip.html`)

Fix them one at a time. Each fix uncovers the next error, which is the lesson.

| # | When it shows | Console says | Cause | Fix |
|---|---|---|---|---|
| 1 | When the page loads | `SyntaxError: missing ) after argument list` | The end of the click handler is `};` but should be `});` | Add the `)` |
| 2 | When the page loads, after fix 1 | `TypeError: Cannot read properties of null (reading 'addEventListener')`, line 26 | The JS looks for `"flip-btn"` but the HTML id is `"flipBtn"` | Make the ids match |
| 3 | When you click Flip!, after fix 2 | `ReferenceError: reslt is not defined`, line 28 | Typo in the variable name | Change it to `resultText` |

All three were tested in Chrome: each error appears exactly as listed, and with all three fixed the page works.

## Bias activity notes

- The prompt to use is on slide 12. Pairs tally which pronoun the AI used for each job: he, she, they, or no pronoun.
- Results vary by model and change over time. Some models now deliberately mix genders. **Either result is a good discussion.** If the AI was balanced, ask why a company would add that on purpose, and who decides what "balanced" means.
- For Teachable Machine: train two classes, 👍 and 👎, using **only one person's hand in one spot**. Then have volunteers with different hands, sleeves, distances or lighting try it, and watch the accuracy drop. Teachable Machine runs in the browser, so don't save the project or the images.
- Keep the discussion about patterns in data, not about individual people in the room.

## If things go wrong

- **No webcam, or Teachable Machine won't load:** skip it and spend the time on discussion (slide 16).
- **The AI refuses or adds a disclaimer about stereotypes:** that's data too. Ask why it might do that.
- **A teen asks a leader to fix their bug:** first they say the error and their guess out loud. Then the leader asks questions without touching the keyboard.

## Measure

- Attendance
- How many teens can open the Console and read an error (spot-check during build time)
- How many teens have their Must feature done and a Nice feature started
