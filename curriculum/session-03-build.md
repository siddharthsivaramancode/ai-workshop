# Session 3: Build — Make it work, then prove it

**Goal:** every teen leaves with (1) their Must feature working, or close to it, and live, (2) at least three edits made to their own code by hand, and (3) the habit of testing AI code by trying to break it instead of trusting it.

**Length:** 70 minutes · 10–15 teens, mostly beginners.

**Deck:** [`slideshows/session-03-build.pptx`](../slideshows/session-03-build.pptx). It was built for the old 2-hour format and hasn't been rebuilt in the Session 1 style yet. Follow the timings below and skip slides to fit.

## Builds on Session 1

| Session 1 idea | How it shows up today |
|---|---|
| "It predicts what sounds right, not what is right" | AI code *looks* correct because it's built from likely-looking tokens. The bug bounty proves it. |
| Fluent ≠ true (hallucination) | The AI says "this code works!" with full confidence. Confidence isn't evidence. |
| The agent loop: plan → write → run → fix | Today *you* are the loop. The AI writes; you run it, find what broke, and fix it. |
| Tools let it act | A chatbot can't run your page. You can. Running it is the check. |

**Words to recall out loud:** hallucination, agent loop, explain-back.

## Before the session

- [ ] Print the bug bounty code (below), one copy per pair, so teens can circle things on paper.
- [ ] **Run the buggy code yourself first.** Paste it into the browser console (Ctrl+Shift+J on Windows, Cmd+Option+J on Mac), then run `check(["B","A","C"])` twice. You should see `"2 / 3"`, then `"4 / 3"`. Every answer was right, so it should say 3 / 3; it says 2 because bug 1 skips question 1. The second result is bug 3: the score keeps adding up. Reload and run `check(["X","X","X"])`. It still says `"2 / 3"` although every answer is wrong. That's bug 2.
- [ ] Have small prizes or a points board for the bounty. Stickers work.
- [ ] Look through the Session 2 pitch sheets so you know who'll need scoping help.

## Run of show (70 min)

| Time | Block | What happens | Who leads |
|---|---|---|---|
| 0:00–0:05 | **Stand-up** | Each teen, one sentence: done, stuck, next. | Leader A |
| 0:05–0:20 | **AI Checkpoint: Bug Bounty** | "The AI says this code works." Pairs get 5 minutes to find 3 bugs worth 1, 2 and 3 points. Hints at minute 3. Reveal, run it live, show the fix. Land the lesson: it looked right because it's built from likely-looking code. | Leader B |
| 0:20–0:28 | **Hand first, AI second** | What HTML, CSS and JS each do (one sentence each). Find anything in your code with Ctrl+F. The challenge: three hand edits today (a color, a word, a size) before asking the AI for anything new. | Leader A |
| 0:28–0:52 | **Build your core feature** | Build, then test it like a troublemaker: click everything twice, leave fields empty, type silly input. When asking the AI, use the good-question template. | Both leaders circulate |
| 0:52–1:02 | **Build Lab 3: JavaScript** | See below. | Leader A teaches, both circulate |
| 1:02–1:10 | **Wrap** | Commit, check it live on a phone, journal, homework. "We're halfway through." | Leader B |

## Build Lab 3: JavaScript, making it do things (10 min)

**Teach (3 min):** JavaScript makes the page *react*. Most beginner features are three moves: **find** something, **wait** for something to happen, **change** the page.
```html
<button id="my-btn">Click me</button>

<!-- the script goes at the END of <body>, after the button, so the button exists when it runs -->
<script>
  const btn = document.getElementById("my-btn");   // find
  btn.addEventListener("click", () => {            // wait
    btn.textContent = "You clicked me!";           // change
  });
</script>
```
Connect it to this morning's bug bounty: that code was JavaScript too, and now they can read its shape.
**Do (6 min):** by hand, add this button to their page (or adapt it to their project: a quiz answer, a flashcard flip). The `id` in the HTML must match the one in `getElementById` exactly.
**Check (1 min):** "Point at the line that finds. The line that waits. The line that changes." If it doesn't work: open the Console and read the red error. (Usually the ids don't match, or the script is above the button.)
**Progress check:** Must feature working or nearly; 3 hand edits made.

## Bug bounty code and answer key

```js
1  let score = 0;                              // BUG 3 (3 pts): score lives outside the function,
2  const answers = ["B", "A", "C"];            //   so it never resets: check twice and you get 4 / 3
3
4  function check(choices) {
5    for (let i = 1; i < answers.length; i++) {   // BUG 1 (1 pt): starts at 1, so question 1 is skipped
6      if (choices[i] = answers[i]) {             // BUG 2 (2 pts): = assigns instead of compares (===),
7        score++;                                 //   so every answer counts as correct
8      }
9    }
10   return score + " / " + answers.length;
11 }
```

**Fixed:** move `let score = 0;` inside the function, start the loop at `i = 0`, and use `===`.

For the printout and for pasting into the console, use this clean version (no comments, no line numbers):

```js
let score = 0;
const answers = ["B", "A", "C"];

function check(choices) {
  for (let i = 1; i < answers.length; i++) {
    if (choices[i] = answers[i]) {
      score++;
    }
  }
  return score + " / " + answers.length;
}
```

**Before the hunt, explain the code in plain words (1 minute):** "It loops through 3 answers, compares each one to the right answer, and counts the score." Teens haven't learned JavaScript yet (that's today's Build Lab), so the hints carry them: a loop counts from a starting number; `=` sets a value while `===` compares; a variable outside the function keeps its value between runs.

## The good-question template

> **I'm trying to:** [what you want to happen]
> **What happens instead:** [what you see]
> **Here's my code:** [paste the part that matters]
> **What I already tried:** [your hand fix]
> Give me a hint first, not the full fix.

It's the context window lesson again: the AI only knows what's on the page.

## If things go wrong

- **Nobody finds bug 3:** run `check` twice in the console on the projector. Seeing 4 / 3 makes it click.
- **A teen wants the AI to fix everything:** the rule today is hand first. One edit by hand, test it, then ask with the template.
- **A teen is way ahead:** start a Nice feature, or try to break their partner's site and report the bugs.
- **A teen is far behind:** a leader sits with them, but the teen still types. Shrink the Must feature further if needed.

## Homework

1. Get your Must feature working and live.
2. Journal: the best bug you found this week, and whether you or the AI found it.
3. Ask someone at home to try to break your site. Write down what they did.
4. Add one more find → wait → change interaction to your own project.

## Measure

- Attendance and retention from Session 1
- How many pairs found all 3 bugs
- How many teens made 3 hand edits
- How many have their Must feature working and live
