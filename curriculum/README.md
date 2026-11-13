# Curriculum: Build It. Ship It. Question It.

**Format:** 6 weekly sessions of about 70 minutes each, for ages 13–18, 10–15 teens (mostly beginners). The last session is a demo day.

**By the end, every teen has:**
1. A live website at a public URL that they built with AI help and can explain line by line.
2. One specific example of the AI being wrong, and how they caught it.
3. A real understanding of how AI works (tokens, embeddings, attention, training, context), how an LLM differs from other AI and from chatbots and agents, and where AI can be unfair or harmful.

**The track:** Session 1 teaches the concepts in depth. Every later session reuses them: each lesson plan opens with a "Builds on Session 1" table, and each week's AI Checkpoint goes deeper on one Session 1 ethics topic.

All 6 sessions have a run-of-show doc (`session-0N-*.md`). Session 1's deck is the 3D browser presenter [`slideshows/session-01-kickoff.html`](../slideshows/session-01-kickoff.html); Sessions 2–6 still use the older `.pptx` decks built by the scripts in `decks/`, which were made for the 2-hour format. This is still a draft. It assumes the decisions in `docs/open-questions.md` go the way the research recommends: a minimum age of 13, an adult sponsor, and static websites only.

## Which AI tools the teens use

Claude (Claude.ai and Claude Code) is 18+, so the teens can't use it with their own accounts. The curriculum is written so the specific AI tool doesn't matter. Every activity works with whichever chat AI a teen is allowed to use.

| Role | Tool | Why | Age rule |
|---|---|---|---|
| **Live demo on the projector** | Claude Code, run by our adult sponsor | Shows what an AI coding agent can do, end to end | 18+, so only the adult uses it |
| **Code storage and publishing** | GitHub, with GitHub Pages for hosting | Free, permanent, and the teen keeps it after the workshop | 13+ |
| **Learning mode (start here)** | ChatGPT Study mode, Gemini Guided Learning, or the CS50 Duck | Coaches with hints and questions instead of handing over answers. Matches our tutor-mode habit. | Same as the app it's in; CS50 Duck needs a GitHub login |
| **Default AI helper** | ChatGPT (free) | Easiest to start, works in a browser, and puts under-18 users in a teen mode with extra safety settings | 13+, with parent permission |
| **AI inside a code editor (after the workshop)** | GitHub Copilot, free with the student plan | We edit in the browser, so it isn't used in sessions. It's on the Session 6 "keep building" sheet for teens who move to VS Code. | 13+. Student verification takes days. |
| **AI that edits code on its own (stretch, advanced teens)** | OpenAI Codex | Can make changes to a teen's GitHub project by itself. That's the closest thing to Claude Code a teen can legally use. | Uses the teen's ChatGPT account. Free access is limited and may be temporary, so it isn't a requirement. |

**Why Codex isn't the default:** it runs on a ChatGPT login, so teens 13–17 can use it with a parent's permission. But free Codex access was launched as a "limited-time" offer with usage caps that aren't published, so it could run out mid-session or disappear. It also works best in a terminal or desktop app, which is a lot for a first-time coder. Use it as a step up for teens who are already comfortable.

## How teens edit their site (every session)

Everything happens in the browser. No installs.

1. Ask the AI (in learning mode / tutor mode) in one tab.
2. Edit `index.html` on github.com in another tab: open the file → pencil icon → paste or type → **Commit changes**.
3. Wait about a minute, then refresh the live URL (`username.github.io/repo`). GitHub Pages republishes on every commit.

**Devices:** school-managed Chromebooks usually block ChatGPT and DevTools, which Sessions 3–5 need. Ask families for a personal laptop, and keep library loaners ready.

## The six sessions

Every session has the same rhythm:

| Minutes | Block |
|---|---|
| 5 | Check-in or stand-up |
| 12–15 | **AI Checkpoint**: one ethics or reliability topic, hands-on |
| 5–10 | A short skill lesson (prompting, hand edits, debugging, testing) |
| 20–25 | Paired building (partners side by side, each on their own site, checking each other's work) |
| 10 | **Build Lab**: one new piece of web tech, used right away on their project (see the ladder below) |
| 7–8 | Commit, check it on a phone, prompt-journal entry, homework |

Session 1 is different: about 45 minutes of teaching (six sections) and a 20-minute guided build that teens finish at home.

| # | Build goal | AI Checkpoint | Deck |
|---|---|---|---|
| 1 | **Kickoff.** What AI is, how LLMs work step by step, LLMs vs. other AI, model vs. chatbot vs. agent, AI ethics, and how to build with AI. Everyone goes live with a placeholder page; the real page is built at home. | *How AI works + ethics overview*: bias, fact-checking a confident AI, deepfakes, privacy, ownership and energy | [`slideshows/session-01-kickoff.html`](../slideshows/session-01-kickoff.html) |
| 2 | **Idea and scope.** Pick a project from the menu, write a one-sentence pitch, list 3 features, build the first one. | *Privacy*: where your words go (context, storage, training) and what never goes in a prompt or on your site | [`slideshows/session-02-idea-and-scope.pptx`](../slideshows/session-02-idea-and-scope.pptx) |
| 3 | **Build.** Get the core feature working, and change AI-written code by hand before asking for more. | *Bug bounty*: AI code looks right because it's built from likely tokens; find the 3 planted bugs | [`slideshows/session-03-build.pptx`](../slideshows/session-03-build.pptx) |
| 4 | **Build and debug.** Practice the debug-first habit: read the error, guess the cause, then ask the AI. | *Bias*: the "4 stories" tally and Teachable Machine, tied back to training data and embeddings | [`slideshows/session-04-debug-and-bias.pptx`](../slideshows/session-04-debug-and-bias.pptx) |
| 5 | **Polish and test.** Have a peer test your site, check it on a phone, and write a README with "AI credits." | *Who owns it?*: an agree/disagree walk on ownership, artists, homework honesty and energy | [`slideshows/session-05-polish-and-test.pptx`](../slideshows/session-05-polish-and-test.pptx) |
| 6 | **Demo day.** Each teen gives a 2–3 minute demo to parents, library staff and guests. | Every demo includes "one thing the AI got wrong" | [`slideshows/session-06-demo-day.pptx`](../slideshows/session-06-demo-day.pptx) + [certificates](../slideshows/session-06-certificates.pptx) |

## Build Lab: the six-week tech ladder

Sessions 2–5 end with a 10-minute **Build Lab**: one new piece of real web tech, taught in 3 minutes and then used right away on the teen's own project. In Session 1 it's woven into the guided build; in Session 6 it's a take-home sheet. It climbs one rung a week, so by demo day they understand every layer of the site they built.

| Session | Build Lab rung | They leave able to |
|---|---|---|
| 1 | **How the web works**: browser → URL → server → files. Repo, commit, GitHub Pages. | Say what happens when someone opens their link |
| 2 | **HTML + CSS**: tags and structure, then style rules. View source, and live-edit in DevTools (Inspect). | Add a link and an image by hand, and restyle the page |
| 3 | **JavaScript**: find → wait → change. Events, `textContent`, where the `<script>` goes. | Make a button change the page, by hand |
| 4 | **The Console + Git history**: `console.log` to trace code, reading History, going back to an older version. | Trace a bug with `console.log`, and undo a bad change |
| 5 | **Phones and everyone**: the viewport tag, flexbox, alt text, contrast, Lighthouse. | Run Lighthouse and fix one accessibility issue |
| 6 | **Where to go next**: custom domains, saving data in the browser, free APIs, VS Code, frameworks, agents. | Pick their next thing to learn, with a free resource for it |

## The 4 habits (taught in session 1, enforced every week)

1. **Explain-back.** No AI-written code goes into your project until you can explain it out loud to someone.
2. **Tutor mode.** Ask the AI for hints first and the full code second. The prompt to paste is in the session 1 deck.
3. **Pair up.** Partners sit side by side, each building their own site, and review each other's work. Leaders never take over a teen's keyboard.
4. **Prompt journal.** Each week, write down what you asked, what came back, and what broke.

## What counts as "shipped"

- A public URL that loads on a phone
- At least one interactive feature that works (a button, a quiz, a game, a calculator)
- A README that says what the AI did and what you did

## Project menu (chosen in session 2)

- **Everyone can ship these:** a portfolio or about-me page, a fan page, a quiz, flashcards, a calculator or converter, a choose-your-own-adventure story
- **Stretch:** a browser game, or a to-do or habit tracker that saves in the browser (localStorage)
- **Advanced:** a Chrome extension, or a small tool for a local group (a club, the library, a local business)
- **Not allowed:** logins, databases, API keys, or collecting anyone's personal info
