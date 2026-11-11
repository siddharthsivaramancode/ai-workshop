# Session 3: Build — Make it work, then prove it

**Goal:** every teen leaves with (1) their Must feature working, or close to it, and live, (2) at least three edits they made to their own code by hand, and (3) the habit of testing AI code by trying to break it instead of trusting it.

**Deck:** [`decks/session-03-build.pptx`](decks/session-03-build.pptx). The speaker notes on each slide hold the script.

## Before the session

- [ ] Print the bug bounty code from slide 5, one copy per pair, so teens can circle things on paper.
- [ ] **Run the buggy code yourself first** so you can show the bugs live. Paste it into the browser console (Cmd+Option+J), then run `check(["B","A","C"])` twice. You should see `"2 / 3"`, then `"4 / 3"`. Every answer was right, so the first result should have been 3 / 3; it's 2 because bug #1 skips question 1. The second result is bug #3: the score keeps adding up. Reload the page and run `check(["X","X","X"])`. It still says `"2 / 3"` even though every answer is wrong. That's bug #2.
- [ ] Have small prizes or a points board ready for the bounty. Stickers work fine.
- [ ] Look through the pitch sheets from session 2 so you know who will need help scoping today.

## Run of show (120 min)

| Time | Slides | Block | Who leads |
|---|---|---|---|
| 0:00–0:10 | 1–2 | **Stand-up.** At each table, everyone says what they've done, where they're stuck, and what's next, one sentence each. | Leader A |
| 0:10–0:32 | 3–9 | **AI Checkpoint: Bug Bounty.** The AI says its code works. Pairs have 7 minutes to find 3 bugs worth 1, 2 and 3 points. Give hints, reveal the bugs, show the fix, then the lesson. | Leader B |
| 0:32–0:47 | 10–13 | **Hand first, AI second.** What HTML, CSS and JS each do, how to find anything in your code, and the 3-hand-edit challenge | Leader A |
| 0:47–1:45 | 14–16 | **Build your core feature.** Test it like a troublemaker, and learn how to ask the AI a good question. | Both leaders circulate |
| 1:45–1:55 | 17–18 | Commit, check the site live, journal. We're halfway through the program. | Leader A |
| 1:55–2:00 | 19 | Homework | Leader B |

## Bug bounty answer key

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

## If things go wrong

- **Nobody finds bug 3:** give the third hint. The best way to show it is live: run `check` twice in the console.
- **A teen wants the AI to just fix everything:** remind them the rule today is hand first. They make one edit by hand, test it, and only then ask the AI, using the good-question template on slide 16.
- **A teen is way ahead:** they can start a Nice feature, or try to break their partner's site and report the bugs they find.
- **A teen is far behind:** a junior mentor pairs with them, but the teen still types. Shrink their Must feature further if needed.

## Measure

- Attendance and retention from session 1
- How many pairs found all 3 bugs
- How many teens have their Must feature working and live
