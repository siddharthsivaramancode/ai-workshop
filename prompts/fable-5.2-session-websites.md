# Prompt: Replace the six PowerPoints with six teaching websites

> Paste everything below the line into a new Claude Code chat running **Fable 5.2**, opened in this repo (`ai-workshop`), on an up-to-date `main`.

---

You are the lead design engineer for **Build it. Ship it. Question it.**, a free, six-week AI builder workshop for teens aged 13–18 at the Burch Library in Collierville, TN. Two high-school students run it.

The workshop currently uses six PowerPoint decks. **We are retiring PowerPoint completely.** Your job is to read those decks and build **six separate, standalone teaching websites, one per session**. Each one replaces its deck: leaders teach from it on the projector, and teens open it on their phones afterward to review and copy the prompts they need. Each site should feel like an award-winning interactive product page, and every fact from the deck has to survive.

**Start with Session 1, take it fully to done, then build Sessions 2–6 in order without stopping for approval.** Ask a question only if you are truly blocked. This prompt and the repo answer almost everything, and §11 gives defaults for the rest.

## 1. Load these first

- **Skills:**
  - **`frontend-slides`**, for presentation-grade visual design and pacing
  - **`motion`**, for Motion best practices, doc and example search, CSS spring generation and MotionScore performance audits. Search its docs instead of guessing at APIs.
  - **`powerpoint`**, to read the `.pptx` source files with python-pptx
- **Agent:** **`motion-reviewer`**, for the final animation performance audit across all six sites (§9)
- **The design libraries you must use.** Read each one's docs before installing anything:

| Library | What it's for | How to install | License |
|---|---|---|---|
| **React Bits**: github.com/DavidHDev/react-bits · reactbits.dev | Text animations, backgrounds (including WebGL/shader ones), cards and micro-interactions | shadcn registry: add `"@react-bits": "https://reactbits.dev/r/{name}.json"` to `components.json`, then `npx shadcn@latest add @react-bits/<Name>-TS-TW`. Always use the **TS + Tailwind** variant. | MIT + Commons Clause. Fine for use inside these sites. **Don't** extract its components into a separate reusable package, and credit it in each site's footer and README. |
| **Fancy Components**: github.com/danielpetho/fancy · fancycomponents.dev | Typography motion, **physics** (Gravity, Cursor Attractor, Elastic Line), blocks (Stacking Cards, Drag Elements, Screensaver, Marquee Along SVG Path, Circling Elements, Float) | Add `"@fancy": "https://fancycomponents.dev/r/{name}.json"` to `components.json`, then `npx shadcn@latest add @fancy/<name>`. Check each component's docs page for its exact registry name and any extra dependencies, then run `npm install`. | MIT |
| **cobe**: github.com/shuding/cobe | A ~5 KB WebGL globe: `createGlobe(canvas, { phi, theta, dark, mapBrightness, baseColor, markerColor, glowColor, markers: [{ location: [lat, lon], size }], onRender })`. Call `globe.destroy()` on unmount. | `npm i cobe`. Wrap it in your own React component. | MIT |
| **shadcn/ui**: ui.shadcn.com | The component and design-token foundation: Card, Badge, Button, Tabs, Accordion, Table, Dialog, Sheet, Tooltip, Kbd, Checkbox, Progress, Sonner (toasts) | `npx shadcn@latest init` | MIT |
| **Motion**: motion.dev, imported from `motion/react` | All custom animation: variants and stagger, `AnimatePresence`, `layout` / `layoutId`, springs, `useScroll` / `useTransform` / `useSpring`, `whileInView`, `animate()`, SVG `pathLength`, `Reorder`, drag | Already a Fancy dependency | MIT |

**Before you install a component, confirm its exact name on the library's site.** Every component suggested in this prompt is a starting point, so verify it exists, and pick the closest real one if it doesn't. When the same job can be done three ways, prefer Fancy or React Bits first, then Motion, then shadcn.

## 2. Source material (read everything before designing)

| Source | What to take from it |
|---|---|
| **`slideshows/*.pptx`** (the six session decks plus the certificates) | **The primary content source.** Use python-pptx to extract every slide's text, in reading order, and its **speaker notes** into `websites/_content/session-0N.json`. |
| `curriculum/decks/build_session_0N.py` | The scripts that generated the decks. Use them to **cross-check** the extraction, especially the order content appears on each click, since that order isn't stored as plain text in the `.pptx`. If the two disagree, the script wins. |
| `curriculum/session-0N-*.md` | The run of show for each session: timings, prep checklists, answer keys, "if things go wrong" notes. Leaders need this on their site (§5). |
| `curriculum/README.md`, `docs/decisions.md`, `docs/open-questions.md`, `README.md` | Program voice, the 4 habits, what "shipped" means, and decisions you must not contradict |
| `reports/Teen AI builder workshop Collierville.md` | Background and sources. You may cite it, but don't add claims that aren't in it. |
| `curriculum/demos/broken-coin-flip.html` | The Session 4 live-debug page with 3 deliberate bugs. It's been tested. **Copy it unchanged** into the Session 4 site's `public/` folder. |

v1 slide counts: **S1 22 · S2 20 · S3 19 · S4 20 · S5 20 · S6 = 14 fixed + 1 per demo** (17 in the file, which has 3 placeholder demos). Write a check that confirms every slide was captured.

## 3. The core idea: one site works two ways

Each session site is a single, long, chapter-based page:

- **Learn mode (the default):** a phone-first scrolling page. Content reveals as it scrolls into view (`whileInView`, `useScroll`). Explanations are fuller than the slide text, because a teen reading at home doesn't have a leader talking. Write them from the speaker notes and run of show (see §6). Teens use it after class to review, copy prompts and check off homework.
- **Present mode** (the `P` key, or a button in the header): a full-viewport projector layout.
  - The page snaps to one **beat** at a time.
  - **→ / Space** step through that beat's reveals in **exactly the v1 click order**, then move to the next beat. **←** goes back.
  - Type is bigger and the chrome is hidden. `F` is fullscreen, `B` is a black screen, `O` is an overview grid of all beats.
  - The URL follows along (`#beat-12/step-2`) so the presenter can deep-link.
- **Leader notes** (the `N` key, or `?leader` in the URL): a slide-over shadcn `Sheet` showing that beat's speaker notes, the session's run-of-show block and timer, and the answer keys. It's hidden by default, so a teen won't come across it by chance.

**Beats map one-to-one to v1 slides and keep their numbers** (beat 12 = old slide 12). That way every "slide 12" reference in the run-of-show docs stays correct, and present mode shows a small beat number in the corner. Section divider slides become chapter openers. Don't drop, merge or reorder beats.

Interactive widgets (physics, drag, counters, copy buttons) must **never** trigger navigation. Arrow keys and Space belong to present mode unless an input has focus.

## 4. Repo layout: six separate sites, one shared kit

Build everything in a new top-level folder, `websites/`, as an npm workspace:

```
websites/
  package.json            # workspaces: ["kit", "session-*", "hub"]
  kit/                    # shared: theme tokens, PresentMode engine, LeaderNotes, Beat, CopyPrompt, Checklist,
                          #   PhysicsStage wrappers, Globe (cobe) component, reduced-motion + perf utilities
  hub/                    # tiny landing page linking all six sessions (cobe globe hero, a marker on Collierville, TN)
  session-01-kickoff/     # standalone Vite app → builds to its own dist/
  session-02-idea-and-scope/
  session-03-build/
  session-04-debug-and-bias/
  session-05-polish-and-test/
  session-06-demo-day/
  _content/               # extracted JSON from the .pptx files (source for the sites' typed content)
```

- **Stack for each site:** Vite + React (latest stable) + TypeScript (strict) + Tailwind CSS v4 + shadcn/ui + Motion + React Bits + Fancy.
- Each session is its **own app with its own build**, so it can be deployed and shared on its own. Shared code lives only in `kit/`.
- Content lives in typed files: `session-0N/src/content.ts`, generated from `_content/`.
- Bundle fonts with `@fontsource`: **Bricolage Grotesque** (display), **Inter** (body), **JetBrains Mono** (code).

## 5. What each site must contain

Every session site has:

1. **A hero:** the session's title line as kinetic type (React Bits `SplitText` / `BlurText`, or Fancy `VerticalCutReveal`), over the session's signature background (§7). Show the session number, "Build it. Ship it. Question it.", and a "Present" button.
2. **Chapters** that follow the v1 deck: one beat per slide. Every beat carries the v1 text and keeps its click-reveal order for present mode.
3. **An "AI Checkpoint" chapter** with one visual identity that repeats across all six sessions.
4. **Copyable prompts.** Every prompt from the decks gets a `CopyPrompt` card (a code block, a copy button, and a Sonner toast saying "Copied"). These are among the most useful things on the site. They include:
   - S1: tutor mode and "your first ask"
   - S2: the planning prompt and "step 1 only"
   - S3: the "ask like a pro" bug report template
   - S4: the bias "4 stories" prompt
   - S5: the README template
5. **A recap:** 3–5 key takeaways, plus the homework as a shadcn `Checkbox` checklist saved in `localStorage`.
6. **Leader notes** (§3), including the "Before the session" checklist from the run-of-show doc, also saved in `localStorage`.
7. **Prev/next session links,** and a footer crediting React Bits, Fancy, cobe, shadcn/ui and Motion.

## 6. Writing rules: keep the facts, expand the explanations

- **Keep every fact, rule and number exactly as written.** That covers:
  - age rules: Claude is 18+; GitHub is 13+; ChatGPT is 13+ with parent permission
  - the privacy rules and the safety list
  - the ownership and copyright statements, including the "not legal advice" line
  - the definition of "shipped"
  - the 4 habits
- **Session 3's bug-bounty code must stay exactly as written, character for character.** It was tested in Node, and the answer key (`2 / 3`, then `4 / 3`) depends on it. Syntax highlighting is fine. Reformatting isn't.
- In learn mode you may **add explanatory text**, but only from the speaker notes, the run-of-show docs and the research report. Write for a 13-year-old: short sentences, everyday words, and no padding. Use no invented statistics, studies or quotes.
- Keep v1's `[placeholders]` as placeholders, unless §8 says to make them editable.

## 7. Design system: "Midnight Launch"

- **Tokens:** start from the v1 palette and write it as shadcn CSS variables in oklch:

  | Token | Hex | Role |
  |---|---|---|
  | ink | `#0F172A` | |
  | orange | `#FF5B14` | primary |
  | cyan | `#00B8C9` | accent |
  | yellow | `#FFD23F` | |
  | green | `#1FB25A` | |
  | red | `#E02D3C` | |
  | paper | `#F7F6F1` | |

  The page is dark-first. Dense reading sections can sit on paper-colored panels.
- **Each session gets its own signature background and accent** (React Bits backgrounds; check the exact names on reactbits.dev):

  | Session | Background feel | Accent |
  |---|---|---|
  | S1 | aurora / flowing gradient | orange + cyan |
  | S2 | soft particles | cyan |
  | S3 | grid / squares | red |
  | S4 | waves / threads | yellow |
  | S5 | silk / iridescent | green |
  | S6 | celebratory: particles, plus the cobe globe | full palette |

- **Reusable effects across all sites:**
  - gradient text with a shine sweep (React Bits `ShinyText` / `GradientText`) on hero words
  - spotlight or glare cards for key concepts (`SpotlightCard`, `GlareHover`)
  - star or conic animated borders on the most important card in each chapter
  - `ClickSpark` on buttons
  - Fancy `Underline Animation` and `Text Highlighter` for emphasis
  - Fancy `Basic Number Ticker` for numbers
  - a subtle grain overlay to stop gradient banding on projectors
- **Motion language:** shared spring presets (`snappy`, `gentle`, `bouncy`) in `kit/motion.ts`. Entrances move up 12–24px with a fade and a small blur. Exits are faster than entrances. Never more than about 3 simultaneous animations per step.
- **The cobe globe:**
  - The hub hero, with a glowing marker at Collierville, TN (35.0420, −89.6645) and one at Memphis (35.1495, −90.0490). Our co-founder describes the mission as reaching "students across the globe," so a slowly spinning globe fits.
  - S2's "Where your chat goes" beat: your words leaving Collierville for faraway servers. Label the server markers "illustrative": we don't know where any specific company's servers are, so don't name real locations as fact.
  - S6 demo day: "Shipped from Collierville."

## 8. A signature moment for each session

Build these to feel special. Where a moment says interactive, make it work for a volunteer at the projector and for a teen on a phone.

**S1 Kickoff:**
- **Guess the next word:** a blinking caret, probability bars that grow on springs, and a **"Sample again"** button that picks a word weighted by the bars and types it in with Fancy `Typewriter`.
- **"It predicts what sounds right, not what is right":** Fancy `Text Highlighter` sweeps across "sounds" and "is".
- **The Claude Code demo prompt:** a realistic terminal that types the prompt in.
- **The agent loop:** Plan → Write → Run → Fix, built with Fancy `Circling Elements` or `Marquee Along SVG Path`, with a glowing dot traveling the loop.
- **The UNVERIFIED stamp** slams in with a bouncy spring.
- **The live-URL beat:** the URL types out, then a `ClickSpark` / confetti burst.
- **The roadmap:** the path draws itself with `pathLength`.

**S2 Idea and scope:**
- **The privacy sort, with physics:** the 9 cards fall into Fancy `Gravity`, and a volunteer drags them into Safe / Depends / Not safe bins. On the reveal step each card springs into its correct bin and recolors, and the "why" text appears.
- **The pitch formula:** [WHO] [DO WHAT] [HOW] rotate with Fancy `Text Rotate` until they land on the example.
- **Must / Nice / Someday:** cards you can reorder with Motion `Reorder` or Fancy `Drag Elements`.
- **Where your chat goes:** the cobe globe, plus animated packets moving along a path.

**S3 Build:**
- **Bug bounty:** the code, unchanged, with team point counters stored in local state. On each reveal step a line gets highlighted and a 1 / 2 / 3-point badge springs out.
- **The fix:** each line morphs from buggy to fixed with `layoutId`.
- **HTML / CSS / JS** shown as three stacked layers you can toggle: skeleton, clothes, muscles.
- **Halfway:** a progress bar that fills on a spring, with a shine.

**S4 Debug and bias:**
- **A realistic DevTools console:** the error types in with Fancy `Scramble In`, then the line reference pulses.
- **Error decoder:** a shadcn `Accordion`.
- **The rubber duck:** Fancy `Screensaver`, or a duck you can throw around with `Gravity`.
- **The live debug beat:** links to `/broken-coin-flip.html` in this site's `public/` folder, which opens in a new tab.
- **Bias tally:** a shadcn `Table` of clickable ±1 counters the presenter fills in live, with animated bars and an `R` key to reset.
- **Data → patterns → output:** text particles stream from one box to the next.

**S5 Polish and test:**
- **The silent-test rules:** a built-in 5:00 countdown with a Motion progress ring that can be started from the leader notes.
- **Agree / Disagree statements:** each statement is huge kinetic type (React Bits `TextPressure` / `ScrollVelocity`, or Fancy variable-font effects), with an optional live three-way tally.
- **Top 2 fixes:** a 2×2 grid with draggable sample sticky notes.
- **README template:** typed out with `Typewriter`, then a `CopyPrompt` card.
- **Polish checklist:** checkboxes saved in `localStorage`.

**S6 Demo Day:**
- **Settings:** a shadcn `Sheet`, opened with the gear button or the `S` key, where leaders enter the presenter list (first name + project), the stats, the 3 "AI got it wrong" quotes and the event date. It's stored in `localStorage` only, with JSON import and export. **Never commit it.**
- The site generates one "Now presenting" beat per presenter, each with a 3:00 countdown ring that turns yellow at 0:30 and red at 0:00. It adds a "2-minute stretch" beat when there are more than 10 presenters.
- **By the numbers:** stats roll in with `Basic Number Ticker`.
- **"Shipped. Every one of you.":** a confetti cannon, and the names cascade in.
- **Certificates:** a print route (`#certificates`) with a print stylesheet that lays out one certificate per page, one per presenter name. This replaces the `.pptx` certificates.

## 9. Non-negotiables and quality gates

**Always:**

- **Readability:**
  - **Present mode:** body text at least 28px at 1920×1080, labels at least 20px, code at least 22px. Test at 1280×720 too.
  - **Learn mode:** body text at least 17px on a 375px-wide phone.
  - WCAG AA contrast everywhere, including over animated backgrounds. Put a scrim behind text where needed.
- **`prefers-reduced-motion`:** use `MotionConfig reducedMotion="user"`. WebGL backgrounds and the globe fall back to a static gradient or image. Physics starts paused and becomes click-to-play.
- **Performance:**
  - At most **one** WebGL canvas running at a time, whether a React Bits shader or cobe.
  - Pause anything offscreen or on an inactive beat, using `IntersectionObserver` or the beat state.
  - Physics runs only while visible.
  - Animate only transform, opacity, filter and clip-path.
  - Lazy-load the heavy widgets.
  - Target 60fps on integrated graphics.
- **Privacy:** no analytics, trackers or third-party embeds. No forms that send data anywhere. No photos or AI-generated images of people. Use no product logos (Claude, OpenAI, GitHub and so on); write the names as text.
- **Accessibility:** semantic headings, a skip link, visible focus, every widget usable from the keyboard, `aria-live` for counters and timers, and alt text.

**Definition of done for each session. All of these must be true before you start the next one:**

- [ ] The beat count and per-beat step order match the v1 script, checked by an automated test.
- [ ] Every beat's speaker notes are in leader notes, and every prompt from the deck has a `CopyPrompt` card.
- [ ] `npm run build -w session-0N`, `tsc --noEmit` and lint all pass, with no console errors or warnings.
- [ ] **You have looked at it.** Run the dev server and use the built-in browser to screenshot every beat:
  - present mode at 1920×1080 and 1280×720
  - learn mode at 375×812

  Fix anything clipped, overlapping, low-contrast or too small. Commit a Playwright script, `npm run shots -w session-0N`, that saves those screenshots to a gitignored `shots/` folder.
- [ ] Present mode runs from the first beat to the last, using only →, with every reveal in the right order.
- [ ] Reduced motion works, and every widget works by mouse, touch and keyboard without triggering navigation.
- [ ] The `motion` skill's MotionScore audit shows no jank-tier problems.
- [ ] Commit: `feat(websites): session 0N`.

## 10. Finish

1. Build the hub page. Then run the **`motion-reviewer`** agent across `websites/` and fix everything rated below good. Do a keyboard-only pass on all six sites.
2. **Retire PowerPoint, in its own separate commit** so it's easy to revert:
   - Delete `slideshows/` and `curriculum/decks/`. Git tag `v1` keeps them recoverable, so mention that in the commit message.
   - Keep `curriculum/demos/broken-coin-flip.html`.
   - Update every reference in `README.md`, `curriculum/README.md`, `curriculum/session-0N-*.md` ("Deck:" lines become "Website:"; slide N is now beat N) and `docs/open-questions.md`.
   - Add a dated entry to `docs/decisions.md`: "Retired PowerPoint; each session is now a standalone website (`websites/`)."
3. Add a GitHub Actions workflow, `.github/workflows/websites.yml`, that builds the hub and all six sites and deploys them to GitHub Pages under `/` (hub) and `/session-0N/`. Set each Vite `base` to match. **Ask the user before enabling GitHub Pages**, because that publishes the sites.
4. Write `websites/README.md`. It covers:
   - running one site or all of them
   - present mode and every keyboard shortcut
   - leader notes and `?leader`
   - the Demo Day settings
   - how to edit content
   - library credits and licenses
5. Push the branch **`feat/session-websites`** and open **one PR**. The description includes:
   - a hero screenshot and one signature-moment screenshot for each session
   - the list of keyboard shortcuts
   - known limitations
   - the note that PowerPoint was retired in a separate, revertible commit
6. Your final message to the user: what you built, the PR link, how to run it, and what still needs a human check, such as a rehearsal on the actual library projector.

## 11. Defaults, and what not to do

- **Defaults:**
  - Phone first for learn mode, projector first for present mode.
  - If an effect competes with the words, the words win.
  - If two good options are tied, choose the one a 14-year-old in the back row would understand fastest, and record the choice in `websites/PLAN.md`.
  - Write `PLAN.md` in Phase 0, before any code. It covers the content inventory, design tokens, the component choices with each one's verified library name, and how each signature moment will be built.
- **Don't:**
  - Don't edit facts, the S3 bug code or the broken coin-flip page.
  - Don't invent content.
  - Don't commit teen names.
  - Don't autoplay sound. Optional sound effects start muted.
  - Don't add three.js or other heavy 3D beyond what React Bits and cobe already need, unless you've measured that it holds 60fps.
  - Don't push to `main`.
  - Don't delete PowerPoint before all six sites pass their quality gates.
