# Session 4: Build and debug — Break it, fix it, question it

**Goal:** every teen leaves with (1) the debug-first habit: read the error, find the line, guess why, try one fix, and only then ask the AI; (2) a first-hand look at bias in AI output and a clear answer to "where does it come from?"; and (3) their Must feature done and a Nice feature started.

**Length:** 70 minutes · 10–15 teens, mostly beginners.

**Deck:** [`slideshows/session-04-debug-and-bias.pptx`](../slideshows/session-04-debug-and-bias.pptx). It was built for the old 2-hour format and hasn't been rebuilt in the Session 1 style yet. Follow the timings below and skip slides to fit.

## Builds on Session 1

| Session 1 idea | How it shows up today |
|---|---|
| Bias: "it learned from us, biases too" | Today they catch it themselves instead of hearing about it. |
| Embeddings: a map of meaning | If training text keeps putting "nurse" near "she" and "engineer" near "he", the map learns that, and so do the answers. |
| Parameters: the dials copy the data | Nobody typed "assume engineers are men". The pattern was in the examples. |
| Coaching (human ratings) and the system prompt | Some apps now deliberately balance answers. That's a choice people made, which raises its own question: who decides? |
| Context window | When you ask the AI about a bug, paste the error. It can't see your Console. |

**Words to recall out loud:** bias, training data, embedding, parameters.

## Before the session

- [ ] **Practice the live debug** with [`demos/broken-coin-flip.html`](demos/broken-coin-flip.html). Open it in Chrome with the Console open and fix the 3 bugs in the order below. Zoom in on the projector.
- [ ] **Practice Teachable Machine** on the leader laptop (teachablemachine.withgoogle.com → Image Project). It needs a webcam. Only the leader's laptop is used, so teens don't share webcam images.
- [ ] Whiteboard or big paper for the bias tally.
- [ ] Optional, but popular: a rubber duck or two.

## Run of show (70 min)

| Time | Block | What happens | Who leads |
|---|---|---|---|
| 0:00–0:05 | **Bug of the week** | Two teens share a bug from homework: what they expected, and what happened. | Leader A |
| 0:05–0:20 | **Debug like a detective** | Open the Console. The 4-step habit: read it, find the line, guess why, try one fix. Then the live debug of the coin-flip page: fix one bug, watch the next error appear. | Leader B |
| 0:20–0:35 | **AI Checkpoint: Bias** | Pairs run the "4 stories" prompt and the room tallies results (6 min). Connect it to Session 1: training data → the map of meaning → the answer. Teachable Machine demo: trained in one condition, it fails in others. What we can do about it. | Leader A, with Leader B at the board |
| 0:35–0:53 | **Build** | Finish the Must feature, start a Nice one. Debug-first rule: before asking a leader or the AI, say the error and your guess out loud. | Both leaders circulate |
| 0:53–1:03 | **Build Lab 4: the Console + Git history** | See below. | Leader A teaches, both circulate |
| 1:03–1:10 | **Wrap** | Commit, check it live, journal, homework. | Leader B |

## Build Lab 4: the Console and Git history (10 min)

**Teach (3 min):** two tools that make you a real debugger.
- **`console.log`:** drop `console.log("got here", score);` inside your code. If it never shows in the Console, that line never ran. If it shows the wrong value, the bug is above it. It's how you see inside code that has no error message.
- **Git history:** on GitHub, open your file → **History** (the clock icon) to see every commit. If a change broke things, open the last working version and copy it back. Nothing you commit is ever truly lost.
**Do (6 min):** add one `console.log` to their own feature and watch it in the Console as they click. Then open their file's History, find their very first commit, and look at how far they've come.
**Check (1 min):** "Your button does nothing and there's no error. What do you do first?" (Add a `console.log` inside the click handler and see whether it runs.)
**Progress check:** Must feature done; a Nice feature started; every teen can open the Console.

## Live debug answer key (`demos/broken-coin-flip.html`)

Fix them one at a time. Each fix uncovers the next error, which is the lesson.

| # | When it shows | Console says | Cause | Fix |
|---|---|---|---|---|
| 1 | When the page loads | `SyntaxError: missing ) after argument list` | The end of the click handler is `};` but should be `});` | Add the `)` |
| 2 | On load, after fix 1 | `TypeError: Cannot read properties of null (reading 'addEventListener')`, line 26 | The JS looks for `"flip-btn"` but the HTML id is `"flipBtn"` | Make the ids match |
| 3 | When you click Flip!, after fix 2 | `ReferenceError: reslt is not defined`, line 28 | Typo in the variable name | Change it to `resultText` |

All three were tested in Chrome: each error appears exactly as listed, and with all three fixed the page works.

## Bias activity notes

- **The "4 stories" prompt:** "Write one sentence each about a nurse, an engineer, a CEO and a kindergarten teacher, each doing their job." Pairs tally which pronoun the AI used for each job: he, she, they, or none.
- Results vary by model and change over time. Some models now deliberately mix genders. **Either result is a good discussion.** If it was balanced, ask: why would a company add that on purpose, and who decides what "balanced" means? (That's coaching and the system prompt from Session 1.)
- **Teachable Machine:** train two classes, 👍 and 👎, using **one leader's hand in one spot**. Then change the conditions *with the same leader's hand*: roll up a sleeve, wear a glove, step back, dim the lights. Watch accuracy drop. **Don't use teens' hands or faces**: comparing teens' bodies in front of the room can single someone out. Then make the link out loud: fewer training examples of some conditions (or some people, as in the 2018 face-analysis study) means worse results for them. Teachable Machine runs in the browser; don't save the project or the images.
- **What we can do:** test with different kinds of users, ask "who is this unfair to?", and in your own project, don't assume what your users look like or call themselves.
- Keep the discussion about patterns in data, not about individual people in the room.

## If things go wrong

- **No webcam, or Teachable Machine won't load:** skip it and spend the time on the discussion.
- **The AI refuses or adds a disclaimer about stereotypes:** that's data too. Ask why it might do that.
- **A teen asks a leader to fix their bug:** first they say the error and their guess out loud. Then the leader asks questions without touching the keyboard.

## Homework

1. Must feature done; one Nice feature started.
2. Journal: one error message you read and fixed yourself.
3. Ask an AI the "4 stories" prompt at home with different jobs. Bring one surprising result.
4. Look at your repo's History on GitHub. Read your own commit messages: would future-you understand them?

## Measure

- Attendance
- How many teens can open the Console and read an error (spot-check during build time)
- How many have their Must feature done and a Nice feature started
