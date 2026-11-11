# Prompt: Six session websites in the "Graphite Instrument" style (v2)

> Paste everything below the line into a new Claude Code chat running **Fable 5.2**, opened in this repo (`ai-workshop`), on an up-to-date `main`.
>
> **What changed from v1:** v1 gave the sites an orange/cyan color scheme and never required the libraries to actually be used, so the result looked generic. v2 sets a strict **dark monochrome** design system (§8), gives build recipes for every signature graphic, and adds an **effects contract** (§9). The contract is checked by a script and by screenshots that prove things move, so the effects can't be skipped.

---

You are the lead design engineer for **Build it. Ship it. Question it.**, a free, six-week AI builder workshop for teens aged 13–18 at the Burch Library in Collierville, TN. Two high-school students run it.

We're retiring the six PowerPoint decks. Read them and build **six separate, standalone teaching websites, one per session**, plus a small hub page that links to all six. Each site replaces its deck:
- Leaders teach from it on the projector.
- Teens open it on their phones afterward to review and copy prompts.

**How it should look:** dark, monochrome and technical, like a precision instrument or a developer tool's field manual. Imagery is built from type, ASCII characters, pixels and ruled diagrams. There are no colorful gradients and no bubbly cards. Sophistication comes from typography, fine rules, texture and motion.

**How to proceed:** build Session 1 all the way to done, then build Sessions 2–6 in order without stopping for approval. Ask a question only if you are truly blocked. This prompt and the repo answer almost everything, and §12 gives defaults for the rest.

## 1. Load these first

- **Skills:**
  - **`frontend-design`**, for distinctive, non-templated visual direction. Re-read §8 through its lens before designing.
  - **`frontend-slides`**, for presentation pacing in present mode
  - **`motion`**, for Motion best practices, CSS spring/`linear()` generation and **MotionScore** audits. If the **Motion MCP** (`search-motion-docs`) is available, search the docs before using any API you're unsure of.
  - **`powerpoint`**, to read the `.pptx` source files with python-pptx
- **Agent:** **`motion-reviewer`**, for the final animation performance audit across all sites
- **Design libraries.** These are required, and §9 enforces it.

| Library | How to install (verified) | License |
|---|---|---|
| **React Bits**: github.com/DavidHDev/react-bits · reactbits.dev | Add `"@react-bits": "https://reactbits.dev/r/{name}.json"` to `components.json` registries, then `npx shadcn@latest add @react-bits/<Name>-TS-TW`. Always use the **TS + Tailwind** variant. Some components pull in `ogl`, `three`, `gsap` or `matter-js`, so check each one's dependencies. | MIT + Commons Clause. Fine to use inside these sites. **Don't** repackage or redistribute its components, and credit it in each footer and README. |
| **Fancy Components**: github.com/danielpetho/fancy · fancycomponents.dev | Add `"@fancy": "https://fancycomponents.dev/r/{name}.json"`, then `npx shadcn@latest add @fancy/<name>`, then `npm install`. Get the exact registry name and any extra dependencies from each component's docs page. | MIT |
| **cobe**: github.com/shuding/cobe | `npm i cobe`. Use `createGlobe(canvas, { phi, theta, dark, mapBrightness, baseColor, markerColor, glowColor, markers: [{ location: [lat, lon], size }], onRender })` and call `globe.destroy()` on unmount. | MIT |
| **shadcn/ui** | `npx shadcn@latest init`. It's the component and token **foundation only**. Restyle everything through §8's tokens, and nothing may look like default shadcn. | MIT |
| **Motion** (`motion/react`) | Comes with Fancy. Use it for custom choreography: variants and stagger, `AnimatePresence`, `layout` / `layoutId`, `useScroll` / `useTransform`, `animate()`, `pathLength`, `Reorder`, drag. | MIT |

**These registry names were confirmed to exist on 2026-11-11:**

- **React Bits** (`@react-bits/<Name>-TS-TW`): `TextType`, `ASCIIText`, `LetterGlitch`, `FaultyTerminal`, `CircularText`, `ShinyText`, `DecryptedText`, `ScrambledText`, `TextPressure`, `ClickSpark`, `CountUp`
- **Fancy** (`@fancy/<name>`): `gravity`, `scramble-in`, `scramble-hover`, `typewriter`, `basic-number-ticker`, `text-rotate`, `text-highlighter`, `vertical-cut-reveal`, `letter-swap-forward-anim`, `variable-font-cursor-proximity`, `text-cursor-proximity`, `circling-elements`, `marquee-along-svg-path`, `pixelate-svg-filter`, `stacking-cards`, `drag-elements`, `screensaver`, `simple-marquee`, `pixel-trail`, `elastic-line`

Check any other component name on the library's site before you use it. If a name doesn't exist, use the closest real component and note the substitution in `EFFECTS.md` (§9).

## 2. Source material (read it all before designing)

| Source | What to take from it |
|---|---|
| **`slideshows/*.pptx`** | **The primary content source.** Use python-pptx to extract every slide's text, in reading order, and its **speaker notes** into `websites/_content/session-0N.json`. |
| `curriculum/decks/build_session_0N.py` | The scripts that generated the decks. Use them to **cross-check** the extraction, especially the click-reveal order, which the `.pptx` doesn't store as text. If the two disagree, the script wins. |
| `curriculum/session-0N-*.md` | Run of show for each session: timings, prep checklists, answer keys, "if things go wrong" notes. These go into leader notes. |
| `curriculum/README.md`, `docs/decisions.md`, `docs/open-questions.md`, `README.md` | Program voice, the 4 habits, what "shipped" means, and decisions you must not contradict |
| `reports/Teen AI builder workshop Collierville.md` | Background and sources. Don't add any claim that isn't in it. |
| `curriculum/demos/broken-coin-flip.html` | The Session 4 live-debug page with 3 deliberate bugs. It's been tested. Copy it **unchanged** into Session 4's `public/` folder. |

v1 slide counts: **S1 22 · S2 20 · S3 19 · S4 20 · S5 20 · S6 = 14 fixed + 1 per demo** (17 in the file, which has 3 placeholder demos). Write a check that confirms every slide was captured.

## 3. One site, two modes

Each session is a single, long page divided into chapters. **Beats map one-to-one to v1 slides and keep their numbers** (beat 12 = old slide 12), so every "slide 12" reference in the run-of-show docs stays correct. Don't drop, merge or reorder beats.

- **Learn mode (the default):**
  - On desktop, three columns: a left chapter rail, the reading column, and a right annotation gutter (§8.4).
  - On phones, one column.
  - Content reveals on scroll. Explanations are fuller than the slide text, written from the speaker notes and run of show.
  - Teens use it to review, copy prompts and check off homework.
- **Present mode** (`P` key, or a header button): a full-viewport projector stage at 1920×1080 that scales to fit.
  - **→ / Space** step through each beat's reveals in **exactly the v1 click order**, then move to the next beat. **←** goes back.
  - `F` is fullscreen, `B` is a black screen, `O` is an overview grid, `R` resets the current widget.
  - The URL deep-links to the position (`#beat-12/step-2`).
  - A small floating instrument HUD (§8.6) shows the beat number, the chapter and a keycap legend.
- **Leader notes** (`N` key, or `?leader` in the URL): a slide-over sheet showing:
  - the speaker notes for the current beat
  - the run-of-show block for this part of the session, with a timer
  - the answer keys
  - the prep checklist, saved in `localStorage`

  It's hidden by default.

Interactive widgets (physics, drag, counters, copy buttons) must **never** trigger navigation. Arrow keys and Space belong to present mode unless an input has focus.

## 4. Repo layout: six standalone sites and a shared kit

```
websites/
  package.json            # npm workspaces: ["kit", "hub", "session-*"]
  kit/                    # tokens, fonts, PresentMode engine, LeaderNotes, Beat, CopyPrompt, Checklist,
                          #   signature graphics (§8.7), Globe (cobe), effects:check + motion-proof scripts
  hub/                    # landing page linking all six sessions
  session-01-kickoff/  session-02-idea-and-scope/  session-03-build/
  session-04-debug-and-bias/  session-05-polish-and-test/  session-06-demo-day/
  _content/               # JSON extracted from the .pptx files
```

- Each session is its own Vite app with its own build: Vite + React (latest stable) + TypeScript (strict) + Tailwind v4 + shadcn/ui + Motion + React Bits + Fancy.
- Shared code lives only in `kit/`. Each session's content lives in a typed `src/content.ts`, generated from `_content/`.
- Each site gets an **`EFFECTS.md`** (§9).

## 5. What every session site contains

1. **Opening:** a split typographic opening (§8.8). It shows the session title, "Build it. Ship it. Question it.", a status line, and two actions: **Start presenting** and **Jump to prompts**.
2. **Chapters** that follow the v1 deck one beat per slide, with the v1 text and click order preserved.
3. **An "AI Checkpoint" chapter** that has the same visual identity in every session: an equipment-label strip, a figure shell and a paper inversion band (§8.5).
4. **A `CopyPrompt` panel** for every prompt from the decks, styled as a terminal-style install command (§8.6). The prompts are:
   - S1: tutor mode, and "your first ask"
   - S2: the planning prompt, and "step 1 only"
   - S3: the "ask like a pro" bug report template
   - S4: the bias "4 stories" prompt
   - S5: the README template
5. **A recap:** 3–5 takeaways, plus the homework checklist (saved in `localStorage`).
6. **Leader notes** (§3).
7. **A compact utility footer:** prev/next session, library credits (React Bits, Fancy, cobe, shadcn/ui, Motion), and a small "status: live" line with a 6px signal dot.

## 6. Writing rules: keep the facts, expand the explanations

- **Keep every fact, rule and number exactly as written.** That includes:
  - age rules: Claude is 18+, GitHub is 13+, ChatGPT is 13+ with parent permission
  - the privacy and safety rules
  - the ownership statements, including "not legal advice"
  - the definition of "shipped"
  - the 4 habits
- **Session 3's bug-bounty code stays exactly as written, character for character.** It was tested, and the answer key (`2 / 3`, then `4 / 3`) depends on it. Syntax highlighting is fine. Reformatting isn't.
- Explanatory text in learn mode may come **only** from the speaker notes, the run-of-show docs and the research report. Write for a 13-year-old: short sentences and everyday words.
- **Voice:** matter-of-fact and technically literate, like a good developer tool's docs. Headings say what something does. Use calm imperatives in instructions.
- **Banned words:** "magic", "revolutionary", "unleash", "seamless", "game-changing". Don't use exclamation marks in headings.
- Keep v1's `[placeholders]`, unless §10 makes them editable. Use no invented statistics or quotes.

## 7. Monochrome is a hard rule

The palette is **greys, black, white and one warm paper tone**, and nothing else. This includes:
- no per-session accent colors
- no colored gradients, no purple/blue glows, no rainbow text
- no colored icons or emoji used as decoration

**The only hue allowed** is a **6px signal dot** (`#ff9100`) on status lines and the primary action. Any meaning that would normally use color (safe vs. not safe, right vs. wrong, active vs. done) must be shown with **fill, outline, hatching, weight, labels and position** instead. That rule also keeps the sites accessible. Before every commit, check that a grep for hex, rgb and oklch values outside `kit/tokens.css` turns up nothing.

## 8. Design system: "Graphite Instrument"

This design system combines four reference styles the user chose:
- a **developer workbench** (near-black canvas, left rail plus annotation gutter, monospace marginalia)
- **typographic machinery** (orbital letter sculptures, ASCII-rendered objects, pixel-glyph seams, checker-bezel instruments, ticket-style buttons, monumental numbers)
- **executable field notes** (bracketed figure captions, dot-grid wells, registration marks, status-square fields)
- a **ruled workbench** (a continuous ruled frame, numbered chapters, equipment-label strips, keycap shortcuts, a pixel mound)

**Take their construction, not their brands.** Use no brand names, logos, product terms or copy from those references.

### 8.1 Principles

1. **An instrument, not a brochure.** Every section shows something working: a diagram, a terminal, a field of states, a live widget.
2. **Type is the imagery.** Rings of letters, ASCII objects, scrambled and decrypting text, mono annotations.
3. **Hierarchy comes from rules and spacing, not shadows or color.** Use 1px hairlines everywhere, flat nested frames, and no drop shadows except the instrument bezel.
4. **Contrast is staged.** The whole page is near-black, with **one paper inversion band per site** for the checkpoint proof, and a circular paper island at the close.
5. **Motion feels mechanical and precise.** Text scrambles, decrypts, ticks and steps. Use springs only for physical things (drag, physics, layout moves).

### 8.2 Color tokens (write them in `kit/tokens.css` as shadcn CSS variables; nothing else may define a color)

| Token | Value | Use |
|---|---|---|
| `--canvas` | `#09090b` | Page background everywhere |
| `--panel` | `#0e0e11` | Recessed panels, code, prompt panels |
| `--media` | `#111114` | Figure and media backing |
| `--raise` | `#17171b` | Hover fill, the selected row, the active keycap |
| `--rule` | `#232329` | All hairlines, frames and dividers |
| `--rule-strong` | `#3a3a42` | Figure outer edges, focused frames |
| `--faint` | `#5d5d68` | Indices, captions, registration marks |
| `--muted` | `#8e8e9a` | Supporting text, marginalia |
| `--soft` | `#c9c9d1` | Body text on dark backgrounds |
| `--ink-inverse` | `#ffffff` | Headings, primary actions, active states |
| `--paper` | `#f1eee7` | Inversion band and closing island only |
| `--paper-ink` | `#232323` | Text on paper |
| `--signal` | `#ff9100` | The 6px status dot only |
| texture | white at 4–22% alpha | Dot grids, checker bezels, ASCII fields, grain |

**Encoding meaning without hue:**

| State | Look |
|---|---|
| Active or correct | solid white |
| Waiting | white at 30% |
| Done | 1px white outline, no fill |
| Wrong or not safe | diagonal hatching plus a ✗ glyph |
| Depends | dotted outline |

Every encoded state also gets a text label or legend.

### 8.3 Typography

Bundle every font with Fontsource (check the exact package names), or self-host them from the `geist` npm package.

- **Geist Sans (400/500/600):** headings and body
- **Geist Mono (400/500):** labels, captions, keycaps, code, quotes, rings and ASCII
- **Azeret Mono (300/400):** only for the opening display line and chapter numerals

| Recipe | Font | Learn mode (desktop) | Present mode (1920 stage) | Notes |
|---|---|---|---|---|
| display | Azeret Mono 350 | 54px / 1.05, -0.04em | 96px | The opening headline: two to four lines, left-aligned |
| chapter-numeral | Azeret Mono 350 | 44px / 1.05, -0.05em | 72px | `01`, `02`… beside chapter headings |
| heading | Geist Sans 500 | 44px / 1.15, -0.01em | 64px | Chapter and beat headings |
| proof-number | Geist Sans 500 | 220px / 0.82, -0.045em | 280px | At most 1–2 times per site |
| body | Geist Sans 400 | 18px / 1.6 (≥17px on mobile) | ≥28px | Uses `--soft` |
| caption | Geist Sans 500 | 18px / 1.5 | 28px | Media captions, in white |
| eyebrow | Geist Mono 500 | 12px / 1.65, 0.08em, uppercase | 20px | `# 03 — HOW CHATBOTS WORK` + signal dot |
| figure-caption | Geist Mono 400 | 11px / 1.65, 0.1em | 20px | `[ FIG 1.3 — NEXT-WORD ODDS ]` |
| annotation | Geist Mono 400 | 14px / 1.45 | (hidden) | Right-gutter marginalia |
| quote | Geist Mono 400 | 22px / 1.4, -0.02em | 40px | Statements, the AI's "confident" answers |
| code | Geist Mono 400 | 15px / 1.6 | ≥24px | Prompts, the bug code, console output |
| button | Geist Mono 500 | 13px / 1, 0.05em, uppercase | 22px | Ticket buttons and keycaps |

### 8.4 Layout

- **Ruled frame:** the page sits inside a centered **1440px frame with 1px `--rule` side lines** that run continuously from the top of the page through the footer. Each chapter ends with a full-width bottom rule, and small **registration ticks** (8×2px white blocks) touch the frame lines at chapter boundaries.
- **Learn mode on desktop (1280px and wider):**
  - a sticky **176px left chapter rail**: Geist 15px links, with the current chapter in white and a slim white marker on a `--rule` track
  - a **~900px reading column**
  - a **224px right annotation gutter**: mono notes connected to their figure by a short horizontal rule
- **Below 1024px,** the rail collapses to a sticky top chapter bar that scrolls sideways, and the gutter notes move directly under their figure.
- **Spacing:** use an 8px grid with steps of 8 / 16 / 24 / 32 / 48 / 64 / 96. Chapters get 96px vertical padding.
- **Background texture:** a fixed overlay of a **22px dot grid** (white at 5%) that fades vertically, plus subtle SVG grain (`feTurbulence`, soft-light blend at 4% opacity) to stop banding on projectors. Faint vertical guide rules line up with the columns. Keep decoration out of the reading column.

### 8.5 Surfaces

1. **Canvas:** `--canvas`. Sections are separated by rules and spacing, never by alternating background bands.
2. **Recessed panel:** `--panel`, a 1px `--rule` border, 8px corners, no shadow.
3. **Figure shell:** the standard way to show any demonstration.
   - an outer 1px `--rule-strong` frame with 0px corners
   - a caption bar at the top: a white-at-3% background and a bottom hairline, with a bracketed figure-caption centered between two tiny outlined glyph boxes (a terminal glyph and a grid glyph)
   - a **dot-grid well** inside: 14px margin; dots are `radial-gradient(circle at 1px 1px, rgba(255,255,255,.14) 1.2px, transparent 0)` at 16px
   - a `--panel` content panel inside the well
4. **Checker bezel:** for terminals, consoles, code and the present-mode HUD.
   - background `#000`
   - background image `repeating-conic-gradient(rgba(255,255,255,.18) 0% 25%, transparent 0% 50%)` at `4px 4px`
   - 8px padding and 8px corners
   - shadow `0 0 0 1px #000, 0 10px 15px -3px rgba(0,0,0,.4)`
   - a `--panel` inset inside, with 4px corners
5. **Paper inversion band:** one per site, for the AI Checkpoint's key proof or rule.
   - full width, `--paper` with `--paper-ink`, and a 26px dot grid in ink at 10%
   - enter and exit it through **pixel-glyph seams** (§8.7)
   - nothing else on the site sits on paper, apart from the closing island

### 8.6 Components (build them in `kit/`)

- **Chapter heading:** the chapter-numeral, then the heading, then the eyebrow above the heading. A full-width hairline sits beneath, and a one-line support paragraph in `--soft` follows. Headings stay left-aligned, never centered.
- **Ticket button (primary):** 48px tall. Two word segments ("START · PRESENTING"), each with 24px padding and 8px corners, joined by a 6px bridge, with concave notches at the join (made with an SVG mask). White fill and black text, plus the signal dot on the upper right.
  - Hover: a 4px white ring at 15%.
  - The whole thing is one accessible `<button>`.
- **Secondary button:** 40px tall, 4px corners, transparent with a 1px `--rule-strong` border, mono uppercase text. On hover the border turns white.
- **Keycap:** 24px square, 6px corners, a 1px `--rule-strong` border and a 2px bottom border, with mono 12px text. Use keycaps for every shortcut hint (P, N, →, F, O, R).
- **Equipment label:** a 24px black strip with a white `★` and mono uppercase text (`★ AI CHECKPOINT`, `★ TRY IT`, `★ LIVE DEMO`). The strip hugs the text.
- **CopyPrompt:** a figure shell titled `[ PROMPT 02 — PLANNING ]`.
  - Inside: a recessed panel with a faint `$` gutter, line numbers in `--faint`, and the prompt in mono, word-wrapped.
  - A copy keycap sits top right. On click, the label **scrambles to "COPIED"** (Fancy `Scramble In`) and a Sonner toast appears, styled in mono.
- **Gutter annotation:** a 168px column of `--muted` mono text, connected to the figure edge by a 24px hairline. It holds "why this matters" notes taken from the speaker notes.
- **Question row** (used for accordions, the error decoder, FAQs):
  - a full-width top hairline
  - a mono index in `--faint`, then the question in white
  - a bracketed `[+]` on the right
  - the answer indented below in `--soft`
- **Present-mode HUD:** a floating checker-bezel instrument, 16px from the top and centered, showing:
  - the beat number `12 / 22` and the chapter name
  - keycap hints
  - a thin **ticker** strip beneath it (Fancy `Simple Marquee`), running the session's vocabulary in `--faint` mono
- **Status line:** a 6px signal dot with mono text, e.g. `● SESSION 03 — LIVE`. The dot gets a 2s stepped pulse.

### 8.7 Signature graphics (build these from the recipes; they define the look)

1. **Orbital word sculpture** (the opening artwork, the hub, and the closing):
   - An SVG with 14–18 concentric circle paths.
   - Uppercase Geist Mono text repeats along `textPath`, at alternating offsets, drawn from **that session's vocabulary** (§10).
   - Letter size grows toward the outer rings, opacity varies from 0.12 to 1, and a few runs break into isolated glyphs.
   - Add 1px dotted orbit circles with wide dashes.
   - Clip it at the edges of its half of the screen.
   - **Motion:** each ring slowly rotates on its own; alternate directions; 60–200s per turn. Scroll position (`useScroll`) slightly speeds up and tilts the rings. Rings pause when offscreen.
   - **Under reduced motion,** show the static SVG.
   - React Bits `CircularText` can be used for one accent ring, but **the core sculpture is your own SVG.**
2. **ASCII object field:** each session gets one object made entirely of characters (§10).
   - Draw a simple silhouette to an offscreen canvas.
   - Sample its brightness on a 10px monospace cell grid.
   - Replace each sample with letters from the session vocabulary, white at 4–50% alpha.
   - Add a second, dimmer full-width character layer behind it.
   - Mask both away from body copy.
   - **Animate:** characters re-roll in steps where the pointer is near (scramble on proximity). The object assembles from noise when it scrolls into view.
   - React Bits `ASCIIText`, `LetterGlitch` or `FaultyTerminal` (monochrome-tuned) may supply the **background layer**, but build the object itself.
3. **Pixel-glyph seam:** at each edge of the paper inversion band.
   - an SVG-masked boundary stepped in 8–24px square cells
   - small monospace glyph fragments scattered within 160px of the edge, dense at the boundary and thinning out
   - paper and charcoal chips mixed together
   - Animate it with a stepped "dissolve" (`steps()` timing) as it scrolls into view.
4. **Status-square field:**
   - a CSS grid of small square cells inside a figure shell, with a ruled legend underneath
   - cells use the encoding from §8.2: solid = active, 30% = waiting, outline = done, hatched = blocked
   - used for: the 6-week roadmap (S1), "where you are" at the halfway point (S3), the polish checklist (S5), and the "Shipped" field with one cell per presenter (S6)
   - Cells change state in a stepped cascade.
5. **Pixel mound:** in the closing section.
   - an SVG of hard 6px white squares on a 12px grid, rising from the bottom-right like a low, uneven hill
   - the squares get sparser near the top
   - `image-rendering: pixelated`, no blur
   - It "builds up" one row at a time in steps when it comes into view.
6. **Monumental proof number:** at most 1–2 per site. For example S1's `41%` (the top next-word guess) and S6's live stats. Use Fancy `Basic Number Ticker` or React Bits `CountUp`, with an odometer-style roll.
7. **Chrome keyword:** **one** word per site gets a silver light sweep (React Bits `ShinyText`, greyscale only). Examples: "sounds" in S1, "history" in S2.

### 8.8 Section recipes

- **Opening:** split 50/50 within the frame.
  - **Left:** a status line, then the display headline (2–4 lines), the session support line, the ticket button + secondary button, and a stepped **scroll cue** (three nested dotted circles + `SCROLL` label) near the bottom.
  - **Right:** the orbital sculpture, clipped by the frame.
  - **Avoid:** a centered headline over a floating orb, a gradient splash, a laptop mockup.
- **Demonstration chapter:** a chapter heading, then a full-width figure shell or checker bezel holding the working widget, with gutter annotations on the right.
- **Capability list:** a numbered row list (mono index + white title + `--soft` detail) beside one tall figure. The selected row gets `--raise` and drives the figure (the 4 habits, the 4 debug steps, the 3 test types, and so on).
- **Checkpoint:** an equipment label, then the chapter heading, the interactive figure, and the paper inversion band holding the one rule or proof to remember.
- **Closing:** the orbital sculpture returns full-bleed around a ~470px **paper circle**. Inside it: a two-line closing line plus the ticket button. Then a pixel-glyph seam, then the utility footer. There's no giant "thank you" billboard.

### 8.9 Motion language

- **Reveals:**
  - Text decrypts or scrambles in (React Bits `DecryptedText` / `ScrambledText`, Fancy `Scramble In` / `Vertical Cut Reveal`), 400–700ms.
  - Blocks fade and rise 12px.
  - Rules draw from left to right (`scaleX` or `pathLength`).
- **Mechanical motion:** stepped timing for cues, tickers, pixel builds, square-field cascades and cursor blinks. Use `steps(8)`, or Motion's `steps()` easing.
- **Springs** are only for physical things: drag, physics, `layout` / `layoutId` moves, press feedback.
- **Hover:** quick changes (100–150ms) to borders and color. Never scale up cards. Fancy `Letter Swap` / `Scramble Hover` go on nav and button labels.
- **Pointer:** Fancy `Pixel Trail` in white at low opacity, only on the opening and closing artwork, and never over text. Fancy `Text Cursor Proximity` / `Variable Font Cursor Proximity` go on one big statement per site.
- **Limits:** at most 3 simultaneous foreground animations per present-mode step. Ambient loops pause offscreen. Everything respects `MotionConfig reducedMotion="user"`.

### 8.10 Banned (this is the generic look we're replacing)

- Colored gradients, blob backgrounds, glassmorphism, neon glows, drop-shadowed cards
- Default shadcn styling: zinc defaults, `rounded-xl` cards with shadows, pill buttons
- Centered hero text over a floating object; giant decorative background numbers (other than the 1–2 proof numbers)
- Emoji or colorful icon tiles
- Uppercase, widely spaced body text
- Anything that sits behind body text and makes it hard to read

## 9. Effects contract (enforced, not optional)

1. **`EFFECTS.md` in each site, written before you build that site.** It's a table with one row per beat:

   | Column | Example |
   |---|---|
   | Beat | 05 |
   | Effect | probability bars build in steps |
   | Library + exact component | `@fancy/basic-number-ticker` |
   | File | `src/beats/Beat05.tsx` |
   | Present-mode step it fires on | step 1 |

   Every beat needs at least one entrance effect, and every chapter needs at least one **signature effect** from §10.
2. **Minimum usage per session site:**
   - **≥ 6 distinct React Bits components**
   - **≥ 6 distinct Fancy components**, including at least one physics component (`Gravity`, `Cursor Attractor & Gravity` or `Elastic Line`) in S2, S4 and S6
   - **≥ 3 of the §8.7 signature graphics**, with the orbital sculpture and the ASCII object required in every site
   - **cobe** in the hub, S2 and S6
3. **`npm run effects:check`** (it lives in `kit/scripts/`, runs for every site, and is part of `npm run verify`) fails if:
   - the minimums aren't met (counted by parsing the imports actually rendered by the site's beat components)
   - a component listed in `EFFECTS.md` isn't imported and rendered
   - any color appears outside `kit/tokens.css`
4. **`npm run motion:proof`** (Playwright) **proves the motion is real.** For the opening, every signature effect and 5 random beats, it:
   - takes a screenshot at t=0 and t=900ms after the trigger
   - uses `pixelmatch` to require a changed-pixel ratio above **0.5%** (the effect animated)
   - reruns with `reducedMotion: 'reduce'` and requires that **no large movement** happens (ratio below 0.5% after the initial render), while all content stays visible
   - records a **video of present mode** stepping through the whole session (Playwright `recordVideo`) to the gitignored `shots/` folder
5. **Look at it yourself.** Use the built-in browser to view the opening, every checkpoint and every signature moment, at 1920×1080 in present mode and at 375×812 in learn mode. Compare what you see against §8.10 and §11, and fix anything that looks generic, colorful, cramped or hard to read **before** moving on.

## 10. Per-session vocabulary and signature moments

| Session | Ring vocabulary | ASCII object |
|---|---|---|
| Hub | BUILD · SHIP · QUESTION · PREDICT · PRIVACY · BUG · BIAS · TEST · DEMO | (cobe globe inside a figure: `[ FIG 00 — WHERE THIS RUNS ]`, markers on Collierville 35.0420, −89.6645 and Memphis 35.1495, −90.0490) |
| S1 Kickoff | PREDICT · NEXT · WORD · TOKEN · GUESS · PATTERN · CHECK | a chat bubble with a blinking cursor |
| S2 Idea and scope | PRIVACY · PITCH · SCOPE · MUST · NICE · SOMEDAY · PUBLIC | a padlock |
| S3 Build | BUG · BOUNTY · TEST · BREAK · FIX · HAND · FIRST | a beetle |
| S4 Debug and bias | ERROR · CONSOLE · LINE · GUESS · DUCK · BIAS · DATA | a rubber duck |
| S5 Polish and test | TEST · WATCH · SILENT · POLISH · OWN · CREDIT · README | a magnifying glass |
| S6 Demo day | BUILT · SHIPPED · QUESTIONED · DEMO · DAY · CREDIT | a trophy, plus a cobe globe: `[ SHIPPED FROM COLLIERVILLE ]` |

**Signature moments.** Build these first in each session. They must look spectacular *and* stay readable.

**S1:**
- **Guess the next word:**
  - The sentence types out (React Bits `TextType`, or Fancy `Typewriter`) with a stepped blinking cursor.
  - The probability bars build in steps: the top option is solid white, the rest are outlined.
  - The percentages roll in with `Basic Number Ticker`.
  - **"Sample again"** picks a word weighted by the bars and types it in.
  - `41%` becomes the monumental proof number.
- **"It predicts what *sounds* right, not what *is* right":** "sounds" gets the chrome sweep, and Fancy `Text Highlighter` underlines "is". This line goes on the paper inversion band.
- **The Claude Code demo:** the prompt types line by line in a checker-bezel terminal.
- **The agent loop:** Plan / Write / Run / Fix in a figure shell, made with Fancy `Circling Elements`, or `Marquee Along SVG Path` along a drawn loop.
- **UNVERIFIED stamp:** an outlined mono stamp that pixelates in (Fancy `Pixelate SVG Filter`, animated from coarse to sharp) over the AI's confident answer, which is set as a mono quote.
- **The live URL:** it scrambles in, then React Bits `ClickSpark` (white).
- **Roadmap:** a status-square field.

**S2:**
- **The privacy sort:**
  - 9 mono cards fall into Fancy `Gravity`, and a volunteer drags them into three bins drawn as outlined trays (SAFE solid / DEPENDS dotted / NOT SAFE hatched).
  - On the reveal step, the cards animate (`layout`) into their correct bins and show their "why" line.
- **Where your chat goes:** a monochrome cobe globe whose markers are labeled "illustrative" (we don't know where any company's servers really are), with packets moving along an SVG path.
- **Public repo history:** "history" gets the chrome keyword, over a `LetterGlitch` field tuned to grey.
- **The pitch formula:** [WHO] [DO WHAT] [HOW] spin in Fancy `Text Rotate`.
- **Must / Nice / Someday:** cards you can reorder with Motion `Reorder` or Fancy `Drag Elements`.

**S3:**
- **Bug bounty:** the code, unchanged, in a checker bezel.
  - Hints reveal with `Scramble Hover`.
  - On each reveal step the line gets a hatched highlight and a mono `[ +1 PT ]` / `[ +2 PTS ]` / `[ +3 PTS ]` tag.
  - Team counters use `Basic Number Ticker`.
- **The fix:** each line morphs with `layoutId` into the fixed version.
- **HTML / CSS / JS:** Fancy `Stacking Cards` labeled skeleton / clothes / muscles.
- **Halfway:** the status-square field fills to 50% in a stepped cascade.

**S4:**
- **The console:** in a checker bezel. The error scrambles in (Fancy `Scramble In`) and `:42` blinks in steps.
- **Error decoder:** question rows.
- **The live debug:** an equipment label `★ LIVE DEMO` linking to `/broken-coin-flip.html`.
- **The rubber duck:** an ASCII duck you can throw (Fancy `Gravity`), or one that bounces around (`Screensaver`).
- **Bias tally:** a ruled table with ±1 keycap counters and bars made of square cells. The presenter fills it in live, and `R` resets it.
- **Data → patterns → output:** words flow along an SVG path (Fancy `Marquee Along SVG Path`).

**S5:**
- **The silent test:** a 5:00 countdown ring drawn with `pathLength` in mono, which can also be started from leader notes.
- **Agree / Disagree statements:** huge type using React Bits `TextPressure` or Fancy `Variable Font Cursor Proximity`, plus a live three-way tally made of status squares.
- **Top 2 fixes:** a 2×2 ruled grid with draggable notes.
- **README:** the template types into a terminal, then appears as a CopyPrompt.

**S6:**
- **Settings sheet** (`S` key): presenters (first name + project), stats, 3 "AI got it wrong" quotes and the date. Stored in **`localStorage` only**, with JSON import/export. **Never commit it.**
- **Now presenting:** one beat per presenter. The name decrypts in (React Bits `DecryptedText`), with a 3:00 countdown ring that switches from solid, to dotted at 0:30, to hatched at 0:00.
- **Stats:** monumental proof numbers.
- **"Shipped. Every one of you.":** the status-square field gets one cell per presenter, and the cells light up in a stepped cascade.
- **Closing:** the orbital rings return with the paper island in the center.
- **Certificates:** a `#certificates` print route, one monochrome certificate per page.

## 11. Non-negotiables and quality gates

- **Readability:**
  - Present mode: body text at least 28px, labels at least 20px, code at least 24px on the 1920 stage. Also test at 1280×720.
  - Learn mode: body text at least 17px at 375px width.
  - Text contrast meets WCAG AA. `--muted` is for marginalia only; substantive text uses `--soft` or white.
- **Performance:**
  - At most **one** WebGL canvas running at a time (cobe or a React Bits shader).
  - Everything offscreen pauses.
  - Physics runs only while visible.
  - Animate only transform, opacity, filter and clip-path.
  - Lazy-load the heavy widgets.
  - 60fps on integrated graphics.
- **Privacy:** no analytics, trackers, third-party embeds or forms that send data anywhere. No images of people. Use no product logos; write product names as text.
- **Accessibility:** semantic headings, a skip link, visible 2px white focus rings, every widget keyboard-usable, `aria-live` on counters and timers, and text alternatives for the ASCII and orbital art.

**Definition of done for each session. All of these must be true before you start the next one:**

- [ ] The beat count and per-beat step order match the v1 script (an automated test).
- [ ] All speaker notes are in leader notes, and every prompt has a CopyPrompt panel.
- [ ] `npm run verify -w session-0N` passes. It runs build, `tsc --noEmit`, lint, `effects:check` and `motion:proof`. There are no console errors.
- [ ] Screenshots of every beat are taken and reviewed: present mode at 1920×1080 and 1280×720, learn mode at 375×812, saved to the gitignored `shots/`. Nothing is clipped, overlapping, colorful or generic.
- [ ] Present mode runs from the first beat to the last using only →.
- [ ] Reduced motion works, and widgets work with mouse, touch and keyboard without triggering navigation.
- [ ] The MotionScore audit shows no jank-tier issues.
- [ ] Commit: `feat(websites): session 0N`.

## 12. Finish, defaults and don'ts

1. Build the hub. Run the **`motion-reviewer`** agent across `websites/` and fix everything rated below good. Do a keyboard-only pass on all seven pages.
2. **Retire PowerPoint, in a separate, revertible commit**, made only after all six sessions pass:
   - Delete `slideshows/` and `curriculum/decks/`. Git tag `v1` keeps them recoverable.
   - Keep `curriculum/demos/`.
   - Update the references in `README.md`, `curriculum/README.md`, `curriculum/session-0N-*.md` ("Deck:" becomes "Website:"; slide N is now beat N) and `docs/open-questions.md`.
   - Add a dated entry to `docs/decisions.md`.
3. Add `.github/workflows/websites.yml`, which builds everything and deploys to GitHub Pages: the hub at `/`, each session at `/session-0N/`, with a matching Vite `base`. **Ask the user before enabling Pages.**
4. Write `websites/README.md`: running the sites, present mode and all shortcuts, leader notes, Demo Day settings, editing content, the design system summary, and library credits and licenses.
5. Push **`feat/session-websites`**, and open **one PR** with:
   - opening and signature-moment screenshots for each session
   - the shortcut list
   - `effects:check` output
   - known limitations
   - the note that PowerPoint was retired in a revertible commit
6. **Final message:** what you built, the PR link, how to run it, and what still needs a human: a rehearsal on the real library projector.

**Defaults:**
- Phone-first in learn mode, projector-first in present mode.
- If an effect competes with the words, the words win.
- If two options are tied, pick the one a 14-year-old in the back row would read fastest.
- Record every decision in `websites/PLAN.md`. Write `PLAN.md` before any code: the content inventory, the token check, the per-session `EFFECTS.md` drafts, and the verified component names.

**Don't:**
- Don't add color (§7).
- Don't edit facts, the S3 bug code or the broken coin-flip page.
- Don't invent content.
- Don't commit teen names.
- Don't autoplay sound.
- Don't add 3D beyond what cobe and React Bits require.
- Don't push to `main`.
- Don't delete PowerPoint before every session passes.
