# Curriculum: Build It. Ship It. Question It.

**Format:** 6 weekly sessions of 2 hours each, for ages 13–18, 15–20 teens. The last session is a demo day.

**By the end, every teen has:**
1. A live website at a public URL that they built with AI help and can explain line by line.
2. One specific example of the AI being wrong, and how they caught it.

This is a draft. It assumes the decisions in `docs/open-questions.md` go the way the research recommends: a minimum age of 13, an adult sponsor, and static websites only.

## Which AI tools the teens use

Claude (Claude.ai and Claude Code) is 18+, so the teens can't use it with their own accounts. The curriculum is written so the specific AI tool doesn't matter. Every activity works with whichever chat AI a teen is allowed to use.

| Role | Tool | Why | Age rule |
|---|---|---|---|
| **Live demo on the projector** | Claude Code, run by our adult sponsor | Shows what an AI coding agent can do, end to end | 18+, so only the adult uses it |
| **Code storage and publishing** | GitHub, with GitHub Pages for hosting | Free, permanent, and the teen keeps it after the workshop | 13+ |
| **Default AI helper** | ChatGPT (free) | Easiest to start, works in a browser, and puts under-18 users in a teen mode with extra safety settings | 13+, with parent permission |
| **AI inside the code editor (optional)** | GitHub Copilot, free with the student plan | Free for verified students. Its "Auto" mode sometimes uses Claude Sonnet behind the scenes. | 13+. Student verification takes days, so start before session 1. |
| **AI that edits code on its own (stretch, advanced teens)** | OpenAI Codex | Can make changes to a teen's GitHub project by itself. That's the closest thing to Claude Code a teen can legally use. | Uses the teen's ChatGPT account. Free access is limited and may be temporary, so it isn't a requirement. |

**Why Codex isn't the default:** it runs on a ChatGPT login, so teens 13–17 can use it with a parent's permission. But free Codex access was launched as a "limited-time" offer with usage caps that aren't published, so it could run out mid-session or disappear. It also works best in a terminal or desktop app, which is a lot for a first-time coder. Use it as a step up for teens who are already comfortable.

## The six sessions

Every session has the same rhythm:

| Minutes | Block |
|---|---|
| 15 | Check-in and show-and-tell |
| 10–15 | **AI Checkpoint**: catch the AI being wrong |
| 60–75 | Paired building (the beginner types, the partner guides) |
| 10 | Publish the work and write a prompt-journal entry |

| # | Build goal | AI Checkpoint | Deck |
|---|---|---|---|
| 1 | **Kickoff.** Watch the live Claude Code demo, then get a "hello" page live at a URL. | *Confident ≠ Correct*: ask the AI about Collierville and catch what it gets wrong | [`decks/session-01-kickoff.pptx`](decks/session-01-kickoff.pptx) |
| 2 | **Idea and scope.** Pick a project from the menu, write a one-sentence pitch, list 3 features, build the first one. | *Privacy*: what never goes in a prompt or on your site | [`decks/session-02-idea-and-scope.pptx`](decks/session-02-idea-and-scope.pptx) |
| 3 | **Build.** Get the core feature working, and change AI-written code by hand before asking for more. | *Bug bounty*: find the bug planted in AI-written code | [`decks/session-03-build.pptx`](decks/session-03-build.pptx) |
| 4 | **Build and debug.** Practice the debug-first habit: read the error, guess the cause, then ask the AI. | *Bias*: use Teachable Machine, or ask an AI to describe "a programmer" and look at who it assumes | not made yet |
| 5 | **Polish and test.** Have a peer test your site, check it on a phone, and write a README with "AI credits." | *Ownership and jobs*: who owns AI-written code, and what couldn't the AI do? | not made yet |
| 6 | **Demo day.** Each teen gives a 2–3 minute demo to parents, library staff and guests. | Every demo includes "one thing the AI got wrong" | not made yet |

## The 4 habits (taught in session 1, enforced every week)

1. **Explain-back.** No AI-written code goes into your project until you can explain it out loud to someone.
2. **Tutor mode.** Ask the AI for hints first and the full code second. The prompt to paste is in the session 1 deck.
3. **Pair up.** The beginner types and the partner guides. Leaders never take over a teen's keyboard.
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
