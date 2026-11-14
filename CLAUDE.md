# CLAUDE.md

Guidance for Claude agents working in this repo. Read this first, then `docs/decisions.md` and `docs/open-questions.md`.

## What this is

**Build it. Ship it. Question it.** is a free, peer-led AI builder workshop for teens (13–18) at Burch Library in Collierville, TN. It runs 6 weekly sessions of about 70 minutes for 10–15 mostly beginner teens and ends with a demo day. Each teen builds one small website with AI help and learns how AI works, where it fails, and the ethics around it.

**People**
- **Siddharth** (co-founder): frontend designer, conducting research in AI ethics.
- **Sai** (co-founder): tool builder, conducting research in AI geolocation.
- **Adult sponsor:** not chosen yet. They run all 18+ tools (Claude, Claude Code) on the projector.

## Repo map

| Path | What it is |
|---|---|
| `curriculum/README.md` | The course overview: week-by-week table, tool table, how teens edit, Build Lab ladder, 4 habits. Start here for course questions. |
| `curriculum/session-0N-*.md` | Lesson plan for each session: run of show, AI Checkpoint, Build Lab, prep, answer keys, homework, contingencies |
| `curriculum/decks/` | Python scripts that build the old `.pptx` decks (`build_session_0N.py`, `check_deck.py`) |
| `curriculum/demos/` | Demo files used in sessions (e.g. `broken-coin-flip.html` for Session 4) |
| `slideshows/session-01-kickoff.html` | **The current Session 1 deck**: a single-file 3D browser presenter (40 slides) |
| `slideshows/*.pptx` | Older decks. Sessions 2–6 still use these; they were built for a 2-hour format and haven't been rebuilt. |
| `docs/decisions.md` · `docs/open-questions.md` | What's decided and what isn't |
| `reports/`, `research_notes/` | Background research (age rules, tools, local landscape, program design) |
| `prompts/` | Long prompts for other Claude sessions |

## The course track

Session 1 teaches the concepts in depth; every later session reuses them. Each lesson plan opens with a **"Builds on Session 1"** table. Keep that link alive when editing.

| Session | Main lesson | AI Checkpoint | Build Lab |
|---|---|---|---|
| 1 | What AI is, how LLMs work (tokens → embeddings → attention → scores → pick), LLMs vs. other AI, model vs. chatbot vs. agent, ethics, building with AI | How AI works + ethics overview | How the web works (woven into the guided build) |
| 2 | Pitch, Must/Nice/Someday, feature 1 | Privacy | HTML + CSS |
| 3 | Core feature, 3 hand edits | Bug bounty | JavaScript |
| 4 | Debug-first habit | Bias | Console + Git history |
| 5 | Silent user testing, README with AI credits | Who owns it? | Phones + accessibility |
| 6 | Demo day | "One thing the AI got wrong" | Take-home "keep building" sheet |

Session rhythm (2–5): check-in 5 · Checkpoint 12–15 · skill lesson 5–10 · build 20–25 · **Build Lab 10 (at the end of the session, by Siddharth's choice)** · wrap 7–8.

## Hard rules

- **Minors' privacy.** The repo is public. First names only for teens and leaders, in slides *and* speaker notes. No schools, grades, photos of people, or personal details. Teens never use their real name as a GitHub username.
- **Leaders' bios.** Siddharth and Sai are *conducting research* in AI ethics / AI geolocation. Never say they wrote or published a research paper. Use "Sai", not his full first name.
- **Age rules.** Claude and Claude Code are 18+: teens never log in; only the adult sponsor demos them. Teens use ChatGPT (13+, parent permission under 18), Gemini teen accounts, learning modes (ChatGPT Study mode, Gemini Guided Learning, CS50 Duck), and GitHub/Pages (13+). Lovable and Replit are adults-only or need a parent; leaders demo those. Recheck age rules before stating them; they change.
- **Static sites only.** No logins, databases, API keys, or collecting anyone's info.
- **Facts need sources.** Numbers in the deck and plans are sourced in `curriculum/session-01-kickoff.md` ("Sources for the facts"). Don't add a statistic without one.

## Editing the Session 1 deck (`slideshows/session-01-kickoff.html`)

It's ~1 MB because three.js and fonts are inlined on a few huge lines. **Never read the whole file.** Grep for `data-title=` to map slides, and read only the region you need.

- **Slides** are `<section class="slide …">` blocks with `data-g` build groups and an `<aside class="note">` holding the speaker script. Dividers use class `sec`; each one starts a new section color (`BASE` array in the JS).
- **3D heroes** are set per slide by `station(i, {...})`. The index is the slide's position, so inserting or removing a slide means renumbering the station list. `kind: 'morph'` with `morphFrom` glides one object between adjacent slides; a laptop morph triggers the lid-opening transition.
- **Live device screens** are canvas functions in `SCR` (e.g. `SCR.rules`, `SCR.attn`). Laptops, phones, tablets and `phones2` take a `screen:` name.
- **Do not change the existing 3D models** (`HERO.*` geometry or materials). The owner explicitly forbids it. New slides may reuse models or duplicate laptops/phones/tablets with a *new* screen.
- **Design direction:** relevant 3D objects, flat 2D charts, bold 3D transitions, a different light color per section, dark Apple-keynote feel.
- **Keep 35–40 slides.** Watch title length and list text: long titles collide with the 3D hero on the right, and list slides fit about 3 items with 2-line descriptions plus a short punchline.
- **Verify visually.** Open it in headless Chrome over CDP (`KickoffDeck.goTo(i, 99, true)`, then screenshot), check for console errors, and look at every slide you touched. `node --check` the extracted module script after JS edits.

## Writing style

Plain, short sentences, written for busy teen leaders who may run a session cold. Concrete steps over theory. Speaker notes say what to say and do, with a time budget (`~2 min.`). Timings in each run-of-show table must add up to the session length.

## Git workflow

The README's convention is to work on a branch and open a PR so the other co-founder (and their Claude) sees each change. Siddharth has been asking for changes to be committed straight to `main` and pushed to GitHub. Follow what the person you're working with asks. When they say "commit to main", push it too and confirm it's on `origin/main`, not just local.

The GitHub repo moved to `github.com/siddharthsivaramancode/ai-workshop`; the old remote URL still redirects.
