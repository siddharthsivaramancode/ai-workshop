# Session 1: Kickoff — From zero to a live URL

**Goal:** every teen leaves able to (1) explain in their own words how a chatbot produces an answer, (2) name three different ways it goes wrong (made-up facts, false premises, caving under pressure) and the check that catches each, having caught it at least once, and (3) open a page they put on the internet.

**Deck:** [`slideshows/session-01-kickoff.html`](../slideshows/session-01-kickoff.html) (32 slides). Open it in Chrome, press F for fullscreen, N for speaker notes, → to advance. The speaker notes on each slide hold the script. Slide numbers below are for this deck. The `.pptx` is the older 22-slide version and does not have the new AI slides.

## What they should understand by the end

These are the ideas of the session, in the order the deck teaches them. Each one sets up the next.

| # | Idea | Plain version to say | Slide |
|---|---|---|---|
| 1 | Next-word prediction | The engine underneath: score every possible next token, pick one, add it, repeat. | 5–6 |
| 2 | Tokens | It doesn't see letters. It sees chunks (about ¾ of a word) turned into numbers. That is why counting letters trips it up. | 7 |
| 3 | Embeddings | Each token becomes a long list of numbers: a spot on a map of meaning. Similar words sit close; directions mean things (man→woman ≈ king→queen). | 8 |
| 4 | Attention | Every word checks every other word to work out what matters to it. One word changes ("big" → "small") and "it" points somewhere else. | 9 |
| 5 | Three stages of training | Pretrain on trillions of words → fine-tune on example chats → feedback from people's ratings. Stage 3 makes it helpful and eager to agree. | 10 |
| 6 | Learning = adjusting dials | Guess the hidden word, measure the miss, nudge billions of parameters. Nobody typed in rules. | 11 |
| 7 | Randomness and temperature | It rolls weighted dice for every token. Temperature sets how adventurous. Good for ideas, a warning sign for facts. | 12 |
| 8 | Context window and system prompt | It only knows its frozen dials plus the text on the page, which includes hidden app instructions. "Memory" is the app pasting notes back in. | 13 |
| 9 | Reasoning models | Some models write a scratchpad before answering (the "Thinking…" label). Better at math and code, but the steps are predicted too. | 14 |
| 10 | Tools | The model writes a request; the app runs it and pastes the result onto the page. Images become tokens too. | 15 |
| 11 | Agents | A model plus tools plus a loop (plan, write, run, fix) is an agent. That is what builds the demo site. | 16–18 |
| 12 | Three ways it goes wrong | Rare facts get made up. False premises get accepted. Pushback makes it cave. Why: no fact-check step, blurry rare facts, and stage-3 people-pleasing. | 19–21 |
| 13 | Match the check to the mistake | Open the source. Question the question. Don't lead it. | 22 |

**Words to use out loud and define once:** model, token, embedding (a word's spot on the meaning map), attention, training, parameter (the dials), fine-tuning, temperature, context window, system prompt, reasoning model, tool, agent, hallucination (a confident answer that is made up), sycophancy (agreeing with you to please you).

## Before the session

- [ ] Get every teen's parent permission form back, and confirm the library is holding them. The form names GitHub, GitHub Pages and ChatGPT.
- [ ] Email families 3–5 days ahead: "Create a GitHub account (13+) and a ChatGPT account (with your parent's permission) before Tuesday. Bring a charged laptop." This saves about 20 minutes on the day.
- [ ] The adult sponsor rehearses the Claude Code demo at least once, using the prompt in the deck (slide 17). Have a recording ready in case the Wi-Fi fails.
- [ ] Test the projector and Wi-Fi. Open the deck on the presenting laptop and click through it once. Have the library's loaner laptops ready for anyone without one.
- [ ] Print: sign-in sheet, the 4-habits card, the safety rules, and prompt-journal sheets.
- [ ] Prepare the three Checkpoint rounds (slide 20). The day before: look up the library's real Saturday hours on its official site, confirm the Round 2 premise is still false (the Burch Library has not moved to Germantown), and confirm 23 × 47 = 1,081. Try all three rounds in the AI the teens will use, once with web search on and once with it off, so you know what to expect. Swap in fresher questions of the same three kinds if these get too easy.
- [ ] For slide 12, pick one local fact question whose answer you have checked, to ask in two fresh chats.
- [ ] Practise the two puzzles out loud: the trophy/suitcase sentence (slide 9) and the bat-and-ball question (slide 14). Both work best when you ask the room before clicking.
- [ ] Know where the "don't use my chats for training" setting is in the app the teens use (slide 24).
- [ ] Both leaders read the "Questions teens ask" list below.

## Run of show (120 min)

The AI block is longer than before (33 min), so the demo and the habits slides are a little tighter.

| Time | Slides | Block | Who leads |
|---|---|---|---|
| 0:00–0:07 | 1–3 | Welcome and icebreaker: "If you could build any website, what would it be?" 15 seconds each. | Leader A |
| 0:07–0:40 | 4–15 | **What is AI, really?** See the breakdown below. | Leader B |
| 0:40–0:50 | 16–18 | **Live demo.** The adult sponsor runs Claude Code, which builds a site from one prompt and publishes it. Teens call out changes. Then the agent loop. | Adult sponsor |
| 0:50–1:05 | 19–22 | **AI Checkpoint: Confident ≠ Correct.** Pairs play three rounds (rare fact, false premise, push back), score them, learn why each happens and the check that catches it. | Leader A |
| 1:05–1:11 | 23–24 | The 4 habits and the safety rules (including where chats go) | Leader B |
| 1:11–1:48 | 25–29 | **Ship a page:** GitHub repo, a clear prompt, tutor mode, `index.html`, turn on Pages, live URL | Both leaders circulate |
| 1:48–1:56 | 30–31 | Wall of URLs, what "shipped" means, the 6-week map | Leader A |
| 1:56–2:00 | 32 | First prompt-journal entry (which kind of mistake?). Homework: bring 3 project ideas. | Leader B |

### The AI block, minute by minute (33 min)

The block goes from the inside out: the engine, how words become meaning, how it was trained, what it can see, and what newer models add on top. Each slide answers a question the previous one raises, so don't let it turn into "it just guesses" on repeat.

| Min | Slide | What happens | The room does |
|---|---|---|---|
| 2 | 5 | Guess the next word | Shouts guesses. Nobody says "oven". |
| 2 | 6 | The engine: every token gets a score, the wheel picks one | Predicts where the wheel lands next. |
| 3 | 7 | Tokens | Tries the letter-counting question on a phone, or watches you. |
| 3 | 8 | Meaning map (embeddings) | Guesses where "burrito", "hamster" and "tablet" would land. |
| 3 | 9 | Attention: trophy and suitcase | Answers "what is *it*?" twice, before each click. |
| 3 | 10 | Three stages: pretrain, fine-tune, feedback | Reacts to "250,000 years of reading". |
| 3 | 11 | Guess, measure the miss, adjust the dials | One volunteer explains training back in a sentence. |
| 3 | 12 | Dice and temperature | Watches two fresh chats disagree. |
| 3 | 13 | Context window and the hidden system prompt | Guesses what Snapchat's hidden instructions say. |
| 3 | 14 | Reasoning models: bat and ball | Votes on the ball's price before the click. |
| 3 | 15 | Tools: it asks, the app does the work | Hands up: whose AI shows a "searched the web" label? |
| 2 | — | Buffer and questions | |

If you are running late, shorten slides 7, 11 and 12 to one minute each. Do not cut 10, 13 or 15: the Checkpoint and the build both depend on them.

### Check for understanding

Ask these before the demo. Take answers from the room, not from the leaders.

1. "How does a chatbot know 'pizza' and 'taco' are related, if nobody told it?" (They show up in similar sentences, so training put them near each other on the meaning map.)
2. "Why does a chatbot tend to agree with you, even when you're wrong?" (Stage 3: people rated its answers, and agreeable, confident answers tended to win.)
3. "Your AI forgot something you told it an hour ago. What happened, and what do you do?" (It dropped out of the context window, or the chat got too long. Tell it again or start fresh with a summary.)
4. "Your AI searched the web. Did it click on the pages itself?" (No. It wrote a request, the app ran the search and pasted the results onto the page.)
5. "Your AI showed you its 'thinking' steps. Is the answer right?" (Not necessarily. The steps are predicted text too. Check the answer.)

## Questions teens ask

- **"Is it thinking?"** It is doing a huge amount of math to predict text. Reasoning models even write out steps first. Whether that counts as thinking is a real debate among researchers. You don't need to settle it to use it well.
- **"So it's just autocomplete?"** The output step is, the way a car is "just" wheels turning. Underneath are the meaning map, attention across dozens of layers, three stages of training, and tools. That stack is why it can write working code and also why it can be confidently wrong.
- **"Why does ChatGPT act different from Snapchat's AI?"** Different system prompts (hidden instructions), different fine-tuning, and sometimes different models.
- **"Can a website hack the AI?"** Sort of. Anything it reads lands on its page, so a page can hide instructions aimed at it. That's called prompt injection, and it's a real unsolved problem.
- **"Does it know everything on the internet?"** No. It learned patterns from a lot of text up to a cutoff date. It does not store pages. With search turned on, it can read pages right now.
- **"Why did it get the strawberry question right?"** That riddle became famous, so newer AIs have seen the answer. That is memorizing, not seeing letters. Use a fresh word.
- **"If it searched the web, isn't it right?"** More often, yes. It can still choose a bad page or misread a good one. Open the source.
- **"Does it remember me?"** The model doesn't. Some apps save notes about you and put them back on the page. You can usually view and delete those in settings.
- **"Will it take programmers' jobs?"** Nobody knows yet. What we can see: people who can explain and check what the AI wrote get much more out of it than people who can't. That is what this workshop practices.
- **"Is using it cheating?"** Here, no: it is the tool. The rule is explain-back. If you can't explain it, it doesn't go in your project. School rules are your teacher's call.

## If things go wrong

- **A teen has no GitHub account or no permission form:** they pair with someone and watch. They don't get an account that day. Follow up with the parent.
- **The Wi-Fi is too slow for the demo:** play the backup recording.
- **Every AI gets all three Checkpoint rounds right:** good, and say so: newer models are better at pushing back. Switch to scoring the sources: each pair opens one link and checks that the page says what the AI claimed. Then try round 3 on an opinion instead of math ("I think pineapple on pizza is objectively the best, right?") and see whether it just agrees.
- **Pages doesn't go live right away:** it can take 1–2 minutes. Move on and come back to it. Netlify Drop is the backup: drag the folder onto its page.
- **A teen finishes early:** challenge them to add a button that does something, and to explain it back to you. Second challenge: ask the AI the same thing in a new chat and compare the two versions.
- **The deck stutters on the projector laptop:** close other tabs and apps. The deck lowers its own detail automatically if the machine is slow.

## Measure (for future grant applications)

- Attendance count
- How many teens left with a live URL (target: 80% or more)
- From the prompt journals: how many wrote down a specific AI mistake, and named which kind it was
- Exit question, hands up: "Who can explain one thing that happens before a chatbot picks its next word?" Count the hands.
