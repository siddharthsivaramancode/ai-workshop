# Session 1: Kickoff — How AI works, where it goes wrong, and how to build with it

**Goal:** every teen leaves able to (1) explain in their own words how an LLM turns a prompt into an answer, step by step, (2) tell apart an LLM, other kinds of AI, a chatbot and an agent, (3) name the main ethical risks (bias, made-up answers, deepfakes, privacy, ownership) and how to check for them, and (4) start a real web page with an AI tutor, which they finish at home.

**Deck:** [`slideshows/session-01-kickoff.html`](../slideshows/session-01-kickoff.html) (40 slides, six sections). Open it in Chrome, press F for fullscreen, N for speaker notes, → to advance. The speaker notes on each slide hold the script and the deeper explanations. Slide numbers below are for this deck. The `.pptx` is the older 22-slide version.

## What they should understand by the end

The deck teaches these in order. Each one sets up the next, and later weeks build on them.

| Section | Idea | Plain version to say | Slide |
|---|---|---|---|
| 01 What AI is | Rules vs. examples | Normal code follows rules a person wrote. AI learns its rules from examples. That's machine learning. | 5 |
| | Training vs. inference | Training happens once: months of guessing the next word. Using it (inference) is prediction only, and it doesn't learn from your chat. | 6 |
| | Parameters | A model is billions of numbers (dials, or weights). Each wrong guess nudges them. Nobody typed in the rules. | 7 |
| 02 How it works | Step 1: tokens | Text is chopped into chunks, each with an ID number. It never sees letters. | 10 |
| | Step 2: embeddings | Each token becomes a long list of numbers, a spot on a map of meaning. Similar words sit close. | 11 |
| | Step 3: attention | Every word scores how much every other word changes its meaning ("river bank" vs. "bank account"). That's the transformer, the T in GPT. | 12 |
| | Step 4: scores | Every token in its vocabulary gets a probability. | 13 |
| | Step 5: pick, repeat | It picks one with some randomness (temperature), adds it, and runs all five steps again. | 14 |
| | Context window | It only knows the frozen patterns plus the text on the page right now. | 15 |
| 03 LLMs vs. other AI | Family tree | AI ⊃ machine learning ⊃ deep learning ⊃ generative AI ⊃ LLMs. | 17 |
| | Four jobs | Recommend, recognize, create images, create text. Different machines, same core idea. | 18 |
| | Image AI | Diffusion: start from noise and remove a little at a time, steered by the prompt. | 19 |
| 04 Model / chatbot / agent | Model → chatbot | A raw model just continues text. Coaching (example chats + human ratings) and an app turn it into a chatbot. | 23 |
| | Chatbot → agent | Tools (search, run code, see) plus a loop that decides its own next step = an agent. | 22, 24 |
| | The comparison | Same engine, more built around it, and more risk: agents can be wrong in actions, not just words. | 25 |
| 05 Ethics | Bias | Unfair examples make unfair patterns (Amazon hiring tool, Gender Shades). | 27 |
| | Truth | Fluent is not true. Why it hallucinates, and checking it. | 28–29 |
| | Deepfakes | Fake images and cloned voices. Check the source, and use a family code word. | 30 |
| | Privacy | Chats can be stored and used for training. Never share personal info. | 31 |
| | Big questions | Ownership, honesty, jobs, energy. | 32 |
| 06 Build with it | Tools | Learning modes first (guardrailed), then chat assistants, code helpers, app builders. Check age rules. | 34 |
| | Prompting | Goal, details, limits, check. The clear prompt *is* tutor mode. | 35 |
| | Habits | Explain-back, tutor mode, pair up, prompt journal. | 36 |

**Words to use out loud and define once:** machine learning, model, parameter (the dials), training, inference, token, embedding, attention, transformer, temperature, context window, base model, system prompt, tool, agent, diffusion, hallucination, bias, deepfake.

## Before the session

- [ ] Get every teen's parent permission form back, and confirm the library is holding them. The form names GitHub, GitHub Pages and ChatGPT.
- [ ] Email families 3–5 days ahead: "Create a GitHub account (13+) and a ChatGPT account (with your parent's permission) before Tuesday. Bring a charged laptop." This saves about 10 minutes of the build block.
- [ ] Check the age rules for every tool on slide 34. They change often. As of November 2026: ChatGPT 13+ with parent permission under 18; Claude 18+; Lovable 18 or parent permission; Replit's current terms require an adult.
- [ ] The adult sponsor rehearses the Claude Code demo (slide 21) and gets it under 3 minutes. Have a recording ready in case the Wi-Fi fails.
- [ ] Test the projector and Wi-Fi. Click through the deck once on the presenting laptop. Have loaner laptops ready.
- [ ] Print: sign-in sheet, the 4-habits card, the safety rules, prompt-journal sheets, and the **at-home handout**: the five GitHub steps (slide 37) plus the tutor-mode prompt (slide 35).
- [ ] Prepare the Checkpoint questions (slide 28). Look up the correct answers from official sources the day before, and try them in the teens' AI with web search on and off.
- [ ] For slide 14, pick one local fact question whose answer you've checked, to ask in two fresh chats.
- [ ] Find where the "use my chats to train the model" setting lives in ChatGPT, to show on slide 31.
- [ ] Both leaders read the speaker notes for sections 02 and 05. They hold the deeper explanations and the sources.

## Run of show (about 65 min: 45 teaching + 20 guided build)

| Time | Slides | Block | Who leads |
|---|---|---|---|
| 0:00–0:03 | 1–3 | Welcome, who we are, icebreaker (10 seconds each) | Leader A |
| 0:03–0:08 | 4–7 | **01 What AI really is:** rules vs. examples, training vs. using, parameters | Leader B |
| 0:08–0:18 | 8–15 | **02 How it works:** the guessing game, then the five steps, then the context window | Leader B |
| 0:18–0:22 | 16–19 | **03 LLMs vs. other AI:** family tree, four jobs, image AI | Leader A |
| 0:22–0:30 | 20–25 | **04 Model, chatbot, agent:** 3-minute live demo, the loop, coaching, tools, comparison | Adult sponsor, then Leader A |
| 0:30–0:41 | 26–32 | **05 Ethics:** bias, 3-minute Checkpoint activity, hallucination, deepfakes, privacy, big questions | Leader B |
| 0:41–0:45 | 33–36 | **06 Build with it:** pick the tool, prompting / tutor mode, the 4 habits | Leader A |
| 0:45–1:05 | 37–40 | **Guided build:** GitHub steps 1–3 together, then "your site lives here", the 6-week map, homework | Both leaders circulate |

**If you're running late, cut in this order:** the slide-14 live demo of two chats (just describe it) → the slide-19 image AI (one sentence) → the slide-32 discussion (read the cards, no opinions) → shorten the demo to just the prompt and the result. Don't cut slides 6, 12, 15, 23 or 29: later weeks depend on them.

**The build block is about starting, not finishing.** Target for today: everyone has a repo (steps 1–2) and has sent the tutor-mode prompt (step 3). Steps 4–5 go home on the handout.

### Check for understanding

Ask these at the end of section 04, before ethics. Take answers from the room, not from the leaders.

1. "Name the five steps an LLM takes to write one word." (Tokens, embeddings, attention, scores, pick. Then repeat.)
2. "Why can two chats give different answers to the same question?" (It picks with some randomness: temperature.)
3. "Is a TikTok feed an LLM?" (No: it's a recommender. Same core idea of learning from examples, different job.)
4. "What turns a raw model into a chatbot? Into an agent?" (Coaching plus an app. Then tools plus a loop.)
5. "Your AI forgot something you told it an hour ago. What happened?" (It fell out of the context window. Tell it again.)

## Questions teens ask

- **"Is it thinking?"** It's doing a huge amount of math to predict text. Whether that counts as thinking is a real debate among researchers. You don't need to settle it to use it well.
- **"Does it know everything on the internet?"** No. It learned patterns from a lot of text up to a cutoff date. It doesn't store pages. With search turned on, it can read pages right now.
- **"Does it learn from my chats?"** The model you're talking to doesn't change during your chat (that's inference). The company may use saved chats to train a *future* model, depending on your settings.
- **"Why did it get the strawberry question right?"** That riddle went viral, so newer AIs have seen the answer. That's memorizing, not seeing letters. Use a fresh word.
- **"If it searched the web, isn't it right?"** More often, yes. It can still choose a bad page or misread a good one. Open the source.
- **"Does it remember me?"** The model doesn't. Some apps save notes about you and paste them onto the page. You can usually view and delete those in settings.
- **"Can it tell if a picture is fake?"** Not reliably, and neither can detector apps. Check where it came from.
- **"Will it take programmers' jobs?"** Nobody knows yet. What we can see: people who can explain and check what the AI wrote get much more out of it. That's what this workshop practices.
- **"Is using it cheating?"** Here, no: it's the tool. The rules are explain-back and say what the AI did. School rules are your teacher's call.

## If things go wrong

- **A teen has no GitHub account or no permission form:** they pair with someone and watch. Follow up with the parent.
- **The Wi-Fi is too slow for the demo:** play the backup recording.
- **Every AI gets all three Checkpoint questions right:** good. Score the sources instead: each pair opens one link and checks that it says what the AI claimed.
- **Pages doesn't go live right away:** it can take 1–2 minutes. Netlify Drop is the backup: drag the folder onto its page.
- **A teen finishes early:** challenge them to add a button that does something and explain it back. Then: ask the same thing in a new chat and compare the two versions.
- **The deck stutters on the projector laptop:** close other tabs and apps. The deck lowers its own detail automatically if the machine is slow.

## Sources for the facts in the deck

- Parameter counts: OpenAI GPT-2 (2019, 1.5B) and GPT-3 (2020, 175B) papers; Meta Llama 3.1 (2024, 405B).
- Transformer: Vaswani et al., "Attention Is All You Need" (Google, 2017).
- Amazon hiring tool: Reuters, October 2018.
- Face analysis error rates: Buolamwini & Gebru, "Gender Shades" (2018).
- Data center electricity: IEA, *Energy and AI* (April 2025): about 415 TWh (~1.5%) in 2024, about 945 TWh projected for 2030.
- Energy per prompt: Google, "Measuring the environmental impact of AI inference" (August 2025): median Gemini text prompt about 0.24 Wh.
- Copyright: U.S. Copyright Office, *Copyright and Artificial Intelligence*, Part 2 (January 2025).
- Tool age rules: each tool's terms of service (check before each cohort).

## Measure (for future grant applications)

- Attendance count
- How many teens started a repo today, and how many have a live URL by Session 2 (target: 80% or more)
- From the prompt journals: how many wrote down a specific AI mistake
- Exit question, hands up: "Who can name the five steps?" Count the hands.
