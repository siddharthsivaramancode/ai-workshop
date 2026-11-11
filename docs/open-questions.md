# Open questions

Things we still need to decide. The research behind most of these is in `reports/Teen AI builder workshop Collierville.md`. When something is decided, move it to `decisions.md`.

## Big decisions (the two of us)

1. **Minimum age: 13?** Teens under 13 can't use almost any of the build tools: GitHub, ChatGPT, Copilot and Vercel all require 13 or older. The research recommends 13+ for the build series, and a separate AI-literacy-only track for 11–12-year-olds later. Do we agree?
2. **Who is our adult?** Claude (Claude.ai and Claude Code) is 18+, and Anthropic actively locks under-18 accounts. That means teens can't have their own Claude accounts, and that includes us. We need an adult who:
   - owns the Claude account and runs Claude on the projector for demos;
   - is at every session (the library will likely require this anyway);
   - can receive any grant money.

   The best fit is a Collierville High CS teacher. A free "Claude for Teachers" account is available to verified US K-12 teachers. Who do we ask?
3. **What do the teens build with?** The recommendation is GitHub plus GitHub Pages for hosting, Copilot through GitHub Education, and ChatGPT with parent permission. Claude appears only as the demo run by our adult. Are we OK with Claude not being the tool teens use themselves?
4. **How long, how many, when?** The proposal is 6 weekly sessions of 2 hours each, 15–20 teens, and a demo day. We still need to pick which weekday, which semester, and the start date.
5. **What counts as "shipped"?** The proposal is a public URL that works on a phone, at least one interactive feature, and a README that says what the AI did and what the teen did.

## To find out locally (calls and emails)

- [ ] Call Burch Library (901-457-2601):
  - Will they co-host the program, so we don't pay the $40/hr room fee charged to outside groups?
  - Can minors lead a program there?
  - Do they have a projector, and is the Wi-Fi strong enough for 20 laptops?
  - How many loaner laptops do they have?
- [ ] Ask a CHS CS teacher whether they'll sponsor us (see question 2).
- [ ] Check whether Claude for Teachers allows any supervised student use.
- [ ] Look into the Hack Club club starter grant (up to $100) and apply for the 2027 Collierville Rotary Foundation grant.
- [ ] Later: contact CLOUD901 (Memphis Central Library, ages 13–18) about running the program in Memphis.

## For the other Claude

- The curriculum overview and sessions 1–5 are drafted in `curriculum/`, each with a run-of-show doc and a deck in `curriculum/decks/`.
- Next, build the deck for session 6 the same way:
  - Write `curriculum/session-0N-*.md` with the run of show.
  - Write `curriculum/decks/build_session_0N.py`, importing `deckkit.py` for the shared colors, layouts and animations.
  - Build each deck with `uv run --with python-pptx python curriculum/decks/build_session_0N.py`.
  - Run `curriculum/decks/check_deck.py` on the new deck. It catches overflowing text and broken animations without opening PowerPoint.
  - Follow the session table in `curriculum/README.md`.
- Draft a one-page pitch to the Burch Library and a parent permission form in `outreach/`.
