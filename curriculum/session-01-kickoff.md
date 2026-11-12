# Session 1: Kickoff — From zero to a live URL

**Goal:** every teen leaves able to (1) explain in their own words how a chatbot produces an answer, (2) name three ways to catch it being wrong, having caught it at least once, and (3) open a page they put on the internet.

**Deck:** [`slideshows/session-01-kickoff.html`](../slideshows/session-01-kickoff.html) (29 slides). Open it in Chrome, press F for fullscreen, N for speaker notes, → to advance. The speaker notes on each slide hold the script. Slide numbers below are for this deck. The `.pptx` is the older 22-slide version and does not have the new AI slides.

## What they should understand by the end

These are the ideas of the session, in the order the deck teaches them. Each one sets up the next.

| # | Idea | Plain version to say | Slide |
|---|---|---|---|
| 1 | Next-word prediction | A chatbot writes by guessing the next word, adding it, and guessing again. | 5–6 |
| 2 | Scores, not facts | Every possible next word gets a score. It usually picks a likely one. | 6 |
| 3 | Tokens | It doesn't see letters. It sees chunks of words turned into numbers. That is why spelling and counting letters trip it up. | 7 |
| 4 | Training | It learned by playing guess-the-next-word billions of times. Each miss nudged billions of dials (parameters). Nobody typed in rules. | 8–9 |
| 5 | Randomness | It doesn't always pick the top word, so the same question can get different answers. | 10 |
| 6 | Context window | When it answers, it has only two things: patterns from training, and the text in the chat right now. New chat, blank page. | 11 |
| 7 | Tools | The model alone only predicts text. Apps can give it tools: search, running code, seeing images. With tools it is reading, and it can still misread. | 12 |
| 8 | Agents | A model plus tools plus a loop (plan, write, run, fix) is an agent. That is what builds the demo site. | 13–15 |
| 9 | Fluent is not true | It is built to sound right. Sounding sure costs it nothing. | 16–18 |
| 10 | Catching it | Ask twice. Ask for the source and open it. Check the real thing. | 19 |

**Words to use out loud and define once:** model, token, training, parameter (the dials), context window, tool, agent, hallucination (a confident answer that is made up).

## Before the session

- [ ] Get every teen's parent permission form back, and confirm the library is holding them. The form names GitHub, GitHub Pages and ChatGPT.
- [ ] Email families 3–5 days ahead: "Create a GitHub account (13+) and a ChatGPT account (with your parent's permission) before Tuesday. Bring a charged laptop." This saves about 20 minutes on the day.
- [ ] The adult sponsor rehearses the Claude Code demo at least once, using the prompt in the deck (slide 14). Have a recording ready in case the Wi-Fi fails.
- [ ] Test the projector and Wi-Fi. Open the deck on the presenting laptop and click through it once. Have the library's loaner laptops ready for anyone without one.
- [ ] Print: sign-in sheet, the 4-habits card, the safety rules, and prompt-journal sheets.
- [ ] Prepare the Checkpoint questions (slide 17). Look up the correct answers yourself from official sources the day before. Try the questions in the AI the teens will use, once with web search on and once with it off, so you know what to expect.
- [ ] For slide 10, pick one local fact question whose answer you have checked, to ask in two fresh chats.
- [ ] Both leaders read the "Questions teens ask" list below.

## Run of show (120 min)

| Time | Slides | Block | Who leads |
|---|---|---|---|
| 0:00–0:08 | 1–3 | Welcome and icebreaker: "If you could build any website, what would it be?" 15 seconds each. | Leader A |
| 0:08–0:33 | 4–12 | **What is AI, really?** See the breakdown below. | Leader B |
| 0:33–0:46 | 13–15 | **Live demo.** The adult sponsor runs Claude Code, which builds a site from one prompt and publishes it. Teens call out changes. Then the agent loop. | Adult sponsor |
| 0:46–1:02 | 16–19 | **AI Checkpoint: Confident ≠ Correct.** Pairs ask their AI 3 local questions, check the answers, then learn the three ways to catch it. | Leader A |
| 1:02–1:10 | 20–21 | The 4 habits and the safety rules | Leader B |
| 1:10–1:47 | 22–26 | **Ship a page:** GitHub repo, a clear prompt, tutor mode, `index.html`, turn on Pages, live URL | Both leaders circulate |
| 1:47–1:56 | 27–28 | Wall of URLs, what "shipped" means, the 6-week map | Leader A |
| 1:56–2:00 | 29 | First prompt-journal entry. Homework: bring 3 project ideas. | Leader B |

### The AI block, minute by minute (25 min)

| Min | Slide | What happens | The room does |
|---|---|---|---|
| 2 | 5 | Guess the next word | Shouts guesses. Nobody says "oven". |
| 3 | 6 | Every word gets a score. The wheel lands on a word. | Predicts where the wheel lands next. |
| 3 | 7 | Tokens | Tries the letter-counting question on a phone, or watches you. |
| 2 | 8 | Three steps: read, learn patterns, predict | Repeats the key line: "sounds right, not is right." |
| 3 | 9 | Guess, check, adjust: how it learned | One volunteer explains it back in a sentence. |
| 3 | 10 | Same question, different answer | Watches two fresh chats disagree. |
| 3 | 11 | Context window | Answers: "What would it need on the page to fix your broken site?" |
| 3 | 12 | Tools | Hands up: whose AI shows a "searched the web" label? |
| 3 | — | Buffer and questions | |

If you are running late, shorten slide 7 and slide 10 to one minute each. Do not cut 9, 11 or 12: the Checkpoint and the build both depend on them.

### Check for understanding

Ask these before the demo. Take answers from the room, not from the leaders.

1. "In one sentence, how does a chatbot write a paragraph?" (It guesses the next word, over and over.)
2. "Why can two chats give different answers to the same question?" (It picks from the likely words with some randomness.)
3. "Your AI forgot something you told it an hour ago. What happened, and what do you do?" (It dropped out of the context window. Tell it again.)
4. "Your AI gave you a link as its source. Are you done?" (No. Open the link and check that it says that.)

## Questions teens ask

- **"Is it thinking?"** It is doing a huge amount of math to predict text. Whether that counts as thinking is a real debate among researchers. You don't need to settle it to use it well.
- **"Does it know everything on the internet?"** No. It learned patterns from a lot of text up to a cutoff date. It does not store pages. With search turned on, it can read pages right now.
- **"Why did it get the strawberry question right?"** That riddle became famous, so newer AIs have seen the answer. That is memorizing, not seeing letters. Use a fresh word.
- **"If it searched the web, isn't it right?"** More often, yes. It can still choose a bad page or misread a good one. Open the source.
- **"Does it remember me?"** The model doesn't. Some apps save notes about you and put them back on the page. You can usually view and delete those in settings.
- **"Will it take programmers' jobs?"** Nobody knows yet. What we can see: people who can explain and check what the AI wrote get much more out of it than people who can't. That is what this workshop practices.
- **"Is using it cheating?"** Here, no: it is the tool. The rule is explain-back. If you can't explain it, it doesn't go in your project. School rules are your teacher's call.

## If things go wrong

- **A teen has no GitHub account or no permission form:** they pair with someone and watch. They don't get an account that day. Follow up with the parent.
- **The Wi-Fi is too slow for the demo:** play the backup recording.
- **Every AI gets all three Checkpoint questions right:** good. Switch to scoring the sources: each pair opens one link and checks that the page says what the AI claimed. Then ask the same question in a new chat with search turned off and compare.
- **Pages doesn't go live right away:** it can take 1–2 minutes. Move on and come back to it. Netlify Drop is the backup: drag the folder onto its page.
- **A teen finishes early:** challenge them to add a button that does something, and to explain it back to you. Second challenge: ask the AI the same thing in a new chat and compare the two versions.
- **The deck stutters on the projector laptop:** close other tabs and apps. The deck lowers its own detail automatically if the machine is slow.

## Measure (for future grant applications)

- Attendance count
- How many teens left with a live URL (target: 80% or more)
- From the prompt journals: how many wrote down a specific AI mistake
- Exit question, hands up: "Who can explain how a chatbot picks its next word?" Count the hands.
