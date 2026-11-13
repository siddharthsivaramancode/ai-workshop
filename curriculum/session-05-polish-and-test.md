# Session 5: Polish and test — Hand it over, watch closely

**Goal:** every teen leaves with (1) their site tested by someone else and the top 2 problems fixed, (2) a site that works on a phone, (3) a README with "AI credits", and (4) a plan for a 2–3 minute demo. They also form their own view on who owns AI-made work and what the AI couldn't do for them.

**Length:** 70 minutes · 10–15 teens, mostly beginners.

**Deck:** [`slideshows/session-05-polish-and-test.pptx`](../slideshows/session-05-polish-and-test.pptx). It was built for the old 2-hour format and hasn't been rebuilt in the Session 1 style yet. Follow the timings below and skip slides to fit.

## Builds on Session 1

| Session 1 idea | How it shows up today |
|---|---|
| The big questions: ownership, honesty, jobs, energy | The agree/disagree walk turns those four cards into opinions teens defend. |
| Image AIs and LLMs learned from people's work | Why AI credits matter, and why their own changes matter. |
| Honesty: AI help is fine, hiding it isn't | The README's AI credits section is where they practice it. |
| Model vs. chatbot vs. agent | In the README, they name which tools they used and what kind each one is. |

**Words to recall out loud:** training data, copyright, AI credits.

## Before the session

- [ ] Print silent-test note sheets (3 columns: where they got stuck · what they said · what I'll fix), 1 per teen.
- [ ] Make signs for the agree/disagree walk: **AGREE** on one wall, **DISAGREE** on the opposite wall, **NOT SURE** in the middle. Check with library staff that the room can be used this way.
- [ ] Share the README template (below).
- [ ] Send families the demo day invite: date, time, room.
- [ ] Decide the demo order and length for Session 6. With 10–15 teens at 2.5–3 minutes each, demos take 30–45 minutes.

## Run of show (70 min)

| Time | Block | What happens | Who leads |
|---|---|---|---|
| 0:00–0:04 | **Check-in** | Two teens share what happened when someone outside the workshop tried their site. | Leader A |
| 0:04–0:20 | **Silent user testing** | Two 5-minute rounds with new partners from another table. The tester thinks out loud; the builder stays silent and writes. Then each teen circles their top 2 fixes. | Leader B keeps time |
| 0:20–0:32 | **AI Checkpoint: Who owns it?** | Four statements, one at a time. Teens walk to AGREE, DISAGREE or NOT SURE, and one person from each side says why. Then 2 minutes of facts (below). | Leader A runs it, Leader B keeps it moving |
| 0:32–0:46 | **Polish** | Make the top 2 fixes. Work down the polish checklist. | Both leaders circulate |
| 0:46–0:56 | **Build Lab 5: phones and everyone** | See below. | Leader A teaches, both circulate |
| 0:56–1:06 | **README with AI credits** | Fill in the template. A leader reads at least the AI credits section before they leave. | Both leaders circulate |
| 1:06–1:10 | **Demo day format** | The 4-part demo (below) and homework. | Leader B |

## Build Lab 5: phones and everyone (10 min)

**Teach (3 min):** three things make a site work for everyone.
- **Phones:** `<meta name="viewport" content="width=device-width, initial-scale=1">` in the `<head>`. Without it, phones show a tiny zoomed-out page. The phone icon in DevTools previews any screen size.
- **Layout:** `display: flex;` lines things up in a row. Add `flex-wrap: wrap;` so they wrap on small screens.
- **Accessibility:** `alt` text on images, enough color contrast, text at least 16px. Some visitors use screen readers or have low vision.
**Do (6 min):** DevTools → **Lighthouse** → tick Accessibility → Analyze. Fix one issue it reports, then run it again.
**Check (1 min):** "What was your score before and after? What did you fix?"
**Progress check:** site tested by someone else, top 2 fixes in progress, works on a phone.

## The four statements

1. "If an AI wrote the code, the code is mine."
2. "AI image generators should have to pay the artists they learned from."
3. "Using AI on homework is cheating."
4. "AI is worth the electricity it uses."

Statement 4 links back to Session 1's energy card: data centers used about 1.5% of the world's electricity in 2024 (IEA), and that's set to roughly double by 2030. Each prompt is small; billions add up.

## Notes on the ownership facts

Keep this light. **It's not legal advice, and the rules are still changing.** What's reasonably settled for a teen audience:

- AI companies' terms generally say the user owns the output. Check the terms of the specific tool before saying this.
- The U.S. Copyright Office's 2025 report says material generated purely by AI isn't protected by copyright. Human contributions can be: your own writing and code, meaningful changes, and creative selection and arrangement.
- Whether training on copyrighted work is allowed is still being fought in court (for example, The New York Times v. OpenAI).
- AI can reproduce code close to other people's existing code. That's why we credit what the AI did, and why the teens' own changes matter.

The goal isn't legal precision. It's the habit of saying honestly what the AI did.

## README template

```markdown
# [Project name]

[One-sentence pitch]

**Live site:** https://[username].github.io/[repo]

## What it does
- [Feature 1]
- [Feature 2]

## AI credits
- **Tools I used:** [e.g., ChatGPT in Study mode (a chatbot)]
- **What the AI did:** [e.g., wrote the first version of the quiz logic]
- **What I did:** [e.g., designed the layout, fixed the scoring bug, wrote all the questions]
- **One thing the AI got wrong:** [specific example, and how I caught it]

## What's next
- [A Someday feature]
```

## Demo format for Session 6 (2.5–3 minutes)

1. **What it is:** the one-sentence pitch.
2. **Show it:** click through the Must feature live.
3. **How one part works:** point at the code and explain it in your own words.
4. **What the AI got wrong:** one specific example and how you caught it.

## If things go wrong

- **A tester gets stuck and the builder jumps in:** the leader says "Freeze! Write it down." The moment someone gets confused is the most useful data in the test.
- **The agree/disagree walk gets heated:** fine. Make sure both sides talk, and keep it about ideas, not people. A teen who doesn't want to move can say "not sure" from their seat.
- **The site is broken the week before demo day:** a leader pairs with them. The Must feature has to work live. A Nice feature can be cut.
- **A teen wants to add a big new feature:** not this week. New ideas go on the Someday list and into "what's next".

## Homework

1. Finish your top 2 fixes and the README.
2. Practice your demo out loud once, with a timer.
3. Invite someone to demo day.

## Measure

- Attendance
- How many teens completed a silent test and fixed at least one issue from it
- How many have a README with AI credits
- Agree/disagree counts for each statement (useful as attitude data)
