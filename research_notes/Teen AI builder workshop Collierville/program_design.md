# Program Design: Peer-Led, Multi-Week "Idea to Shipped Project" AI Coding Workshop for Teens (ages ~11–18), as of Nov 2026

Scope: evidence and practices for a 4–8 session (weekly, 1.5–2 hr) free public-library workshop run by two high schoolers, ending in a demo day. Each section follows the required format. Research ran to about 20 search/fetch calls, so some areas are thin and are flagged in Gaps.

---

## 1. Teaching beginners to build with AI coding tools ("vibe coding"): risks and mitigations

### Takeaway
The best evidence says AI code generators help novices *produce* working code and need not hurt short-term learning when the learning is structured (Kazemitabaar 2023, ages 10–17). But weaker or less metacognitive students are the ones most likely to be harmed: they over-rely, drift between suggestions, and ship code they do not understand (Prather 2024). AI that is constrained to tutor rather than write code (CS50 duck, CodeAid), explain-back steps, and human pairing are the documented mitigations.

### Cited Findings
**Studies with young or novice learners**
- Kazemitabaar et al. (CHI 2023) ran a controlled study of 69 learners aged **10–17** with no prior text-based programming. Half used a Codex-based assistant to learn Python. The Codex group had a **1.15x higher completion rate and 1.8x higher scores** on code-authoring tasks, and their performance on manual code-modification tasks **did not drop**. — [arXiv 2302.07427](https://arxiv.org/abs/2302.07427v1); [UMD PDF](https://terpconnect.umd.edu/~weintrop/papers/Kazemitabaar_et_al_CHI_2023.pdf)
- In the same study, on a retention test one week later, the Codex group scored slightly higher, but **not significantly**. Learners with **higher prior Scratch scores** benefited significantly more, which suggests prior skill moderates the benefit. The authors flag over-reliance as a risk. — [arXiv 2302.07427](https://arxiv.org/abs/2302.07427v1)
- Prather et al., "The Widening Gap" (ICER 2024), was a lab study of 21 novices in an intro C++ course. Students who already struggled and lacked metacognitive awareness had significant difficulties with GenAI. Stronger students could tell helpful suggestions from unhelpful ones and stayed in control. All earlier metacognitive difficulties persisted and could be compounded, and new ones appeared, named **Interruption, Mislead, Progression**. The paper also describes **"shepherding"** (students rarely write their own code and are steered by the AI) and **"drifting"** (bouncing between suggestions without progress). — [arXiv 2405.17739](https://arxiv.org/html/2405.17739v1); [ICER 2024 listing](https://icer2024.acm.org/details/icer-2024-papers/26/The-Widening-Gap-The-Benefits-and-Harms-of-Generative-AI-for-Novice-Programmers)
- An earlier Copilot usability study with novices ("It's Weird That It Knows What I Want") found that participants themselves recognized over-reliance could hinder their learning and could worsen metacognitive skills. This was raised as a concern, not measured. — [arXiv 2304.02491](https://arxiv.org/pdf/2304.02491)
- "(Im)Paired Programming" (2026 preprint, n=54): coding agents helped initial task completion but **harmed code comprehension** and did not prepare users to extend their own code without the agent. This is preliminary and not peer reviewed. — [alphaXiv 2607.26375](https://www.alphaxiv.org/abs/2607.26375)
- A Copilot replication on brownfield (existing-codebase) tasks found that participants passed more test cases with Copilot but scored no higher on comprehension, a **"comprehension-performance gap"**. — [arXiv 2604.13277](https://arxiv.org/html/2604.13277)
- A qualitative study of 207 students' reflective diaries found that students who used GenAI **as a comprehension aid**, rather than a code producer, built deeper understanding. — [arXiv 2511.02922](https://arxiv.org/abs/2511.02922v1)

**"AI as tutor, not doer" systems**
- Harvard CS50's "duck" (Liu et al., SIGCSE 2024) was deployed to about 70 summer students, then thousands online, then about 500 on-campus students. It has "pedagogical guardrails" meant to guide students rather than hand them solutions. Students reported feeling like they had "a personal tutor." Questions asked of human TFs dropped from **0.89 to 0.28 per student** once AI was available. — [Liu et al. PDF](https://cs.harvard.edu/malan/publications/V1fp0567-liu.pdf); [SIGCSE 2024 demo](https://sigcse2024.sigcse.org/details/sigcse-ts-2024-demos/4/Demo-2A-Teaching-CS50-with-AI-Leveraging-Generative-Artificial-Intelligence-in-Comp); [CS50 AI docs](https://cs50.readthedocs.io/cs50.ai/)
- A 2025 CS50 follow-up acknowledged problems with the first integration, including the AI sometimes giving direct solutions instead of guidance. — [SIGCSE 2025 "Improving CS50 with AI"](https://rosetta.to/u/cs50/sigcse-2025-improving-cs50-with-ai)
- CodeAid (Kazemitabaar et al., CHI 2024) was deployed for 12 weeks with about 700 university students. It answers conceptual questions, gives pseudo-code with line-by-line explanations, and points to fixes **without revealing code solutions**. It almost never revealed direct code. Students mostly used it for conceptual understanding and debugging, and a minority tried to extract direct code. Educators worried about occasional incorrect feedback and about students defaulting to ChatGPT. One student said it "can lie to you and still sound confident." — [arXiv 2401.11314](https://arxiv.org/abs/2401.11314); [Austin Henley blog](https://austinhenley.com/blog/codeaid.html)

**Explain-back and metacognitive scripts**
- A 2026 preprint proposes an "Explanation Gate": a teach-back step, enforced by an LLM judge, that runs before generated code can be integrated. Its purpose is to reduce "epistemic debt." This is a design proposal without large-scale evidence. — [arXiv 2602.20206](https://arxiv.org/html/2602.20206v1)

**Pairing**
- A mixed-methods study of 39 undergraduates compared human pair programming, pair programming with GenAI, and solo programming with GenAI. Students valued LLMs as partners but saw limits compared with human teammates. — [arXiv 2505.08119](https://arxiv.org/abs/2505.08119?context=cs)
- A study with intact class sections found that AI-assisted pairing raised intrinsic motivation and lowered anxiety compared with working alone. **Human–human pairing** produced the highest sense of collaboration and social presence. — [arXiv 2501.10091](https://arxiv.org/html/2501.10091v2)

**Position statements**
- The Raspberry Pi Foundation's June 2025 position paper, "Why kids still need to learn to code in the age of AI," argues that vibe coding does not replace learning to program. Its reasons: judging whether AI code is correct, safe, and ethical requires understanding, and the "friction" of expressing logic precisely is where learning happens. — [The Register coverage](https://www.theregister.com/software/2025/06/05/raspberry-pi-generative-ai-cannot-replace-learning-to-code/459812); [position paper PDF](https://static.raspberrypi.org/files/about/Why-kids-still-need-to-learn-to-code-in-the-age-of-AI-2025-Raspberry-Pi-Foundation-position-paper.pdf)

**Tool access and age limits (major constraint for this audience)**
- **Claude (claude.ai consumer) requires users to be 18+.** Anthropic's terms set the minimum at "at least 18 years old or the minimum age required to consent… whichever is higher." A 2026 report says Anthropic began locking accounts it identified as belonging to under-18 users. — [ConductAtlas summary of Claude.ai ToS](https://conductatlas.com/platform/anthropic/claudeai-terms-of-service/minimum-age-and-coppa-compliance/); [AI Productivity news on lockouts](https://aiproductivity.ai/news/anthropic-enforces-age-policy-under-18-lockouts/); [Common Sense Media Claude risk assessment, Mar 2026](https://institute.commonsensemedia.org/sites/default/files/risk-assessments/csm-ai-risk-assessment-claude-03252026%20%281%29.pdf). These are third-party summaries; verify against anthropic.com/legal.
- Anthropic's usage policy has a separate section of additional requirements for products that serve minors, which suggests minors may only use Claude through an approved third-party product, not the consumer app. — [ConductAtlas usage policy](https://conductatlas.com/platform/anthropic/anthropic-usage-policy/products-serving-minors-additional-requirements/)
- ChatGPT is reported as **13+ with parental consent**, and a teen mode was reported launched on 18 Aug 2026. — [Tech Insider comparison](https://tech-insider.org/character-ai-vs-chatgpt-vs-claude-age-verification-2026/) (secondary source; verify with OpenAI)
- GitHub accounts require age **13+**. The GitHub Student Developer Pack is open to high-school and homeschool students, and Copilot must be activated separately after approval. — [GitHub Docs: Student Pack terms](https://docs.github.com/en/education/about-github-education/github-education-for-students/github-terms-and-conditions-for-the-student-developer-pack); [Community FAQ](https://github.com/orgs/community/discussions/111352)

### Inferences
- **Most important design constraint:** a workshop for ages 11–18 **cannot have most participants sign up for Claude.ai directly**, because of the 18+ rule. Options: (a) the two teen leaders, if 18+ or with an adult co-facilitator, demo Claude on a shared screen while participants use age-appropriate tools; (b) participants aged 13+ use tools with teen policies, such as GitHub Copilot via the Student Pack, or ChatGPT's teen mode with parental consent; (c) under-13s get no individual AI accounts and work in a pair with an older participant or the facilitator's projected session. Collect parent permission slips that name the tools. The report writer should flag this prominently.
- Prather's "widening gap" and Kazemitabaar's prior-skill moderation both point to the same risk: in a mixed-skill room, beginners are the ones most likely to "shepherd" and "drift." So the structure should protect beginners specifically. Ways to do that: required explain-backs, small scoped features, and a human partner.
- Concrete mitigation bundle, synthesized from the findings above:
  1. **Explain-back gate.** Before a chunk of AI code goes into the project, the student explains it aloud to their partner or a leader. A lightweight human version of the "Explanation Gate."
  2. **Prompt journal.** Keep a shared doc per student of the prompt, what came back, what they changed, and what broke. It builds metacognition, which Prather identifies as the gap, and doubles as demo-day "process" material.
  3. **Tutor-mode system prompt.** Give students a saved instruction that tells the AI to explain and give hints or pseudo-code before full code, modeled on the CS50 duck and CodeAid. Expect leakage: CS50 itself reported its AI sometimes gave solutions.
  4. **Driver/navigator pairing with an AI as the third member.** Human pairing gave the highest collaboration in the pairing studies.
  5. **"Modify before generate."** Students hand-edit AI code (change colors, text, a variable) before asking for more. In Kazemitabaar, manual modification skill held up.
  6. **Debug-first habit.** Read the error, form a guess, then ask the AI. This counters the "Mislead" and "drifting" patterns.

### Gaps
- No peer-reviewed study was found of middle-school or high-school students using *agentic* tools (Claude Code, Cursor, Replit Agent) in out-of-school settings. Most evidence is from university CS1 or from 2023-era Codex.
- No direct evaluation of "prompt journals" as an intervention was found. It is an inference from the metacognition literature.
- Formal guardrail-failure rates for the CS50 duck were not retrieved.
- Gemini's teen and education age policy for 2026 was not confirmed (search returned nothing).
- The official Anthropic terms page was not fetched directly. The 18+ claim rests on several consistent third-party summaries.

---

## 2. Realistic project types and free deployment paths

### Takeaway
For a 4–6 week arc with beginners, the most reliable path is a **static web project** (HTML/CSS/JS: personal site, quiz, browser game, tool or calculator) deployed free on **GitHub Pages or Netlify Drop**. Replit's free tier no longer appears to include deployments, and Vercel Hobby is free but limited to non-commercial use.

### Cited Findings
- Hack Club's YSWS model uses small, well-defined "ship" targets. Wisp, for example, rewards approved hardware ships with tiered prizes (sticker pack for one ship, shirt at four). Blot has students write code in a web editor that generates art. Many programs are short-lived and archived, so check what is live. — [ysws.hackclub.com](https://ysws.hackclub.com/); [Wisp](https://wisp.hackclub.com/); [YSWS readme](https://readme.hackclub.com/ysws)
- Hack Club offers "starter projects" for beginners in its Highway program. — [Highway starter projects](https://highway.hackclub.com/getting-started/starter-projects)
- Hack Club's "Why We Ship" essay (Feb 2025) argues for shipping fast and often and starting with small MVPs. It also reports a lesson from its Arcade program: rewarding participation regardless of quality produced many low-value "slop" projects, so the follow-up program, High Seas, required actually shipping to earn rewards. — [Why We Ship](https://essays.hackclub.com/why-we-ship/)
- **GitHub Pages:** free static hosting with about 1 GB storage and 100 GB/month bandwidth, a soft limit of 10 builds per hour, static files only, and not allowed for e-commerce or businesses. **Vercel Hobby:** free, about 100 GB bandwidth, personal and non-commercial use only. **Netlify:** free tier now uses a credit model (300 credits/month, sites pause at zero), and "Netlify Drop" lets you drag a folder in to deploy, the easiest setup for beginners. **Cloudflare Pages:** unlimited bandwidth and requests, 500 builds/month. — [cmaven comparison](https://cmaven.github.io/en/hosting/netlify-vercel-static-hosting-comparison/); [guptadeepak 2026](https://guptadeepak.com/tools/top-5-static-site-hosting-jamstack-platforms-2026/); [DEV comparison](https://dev.to/build996/vercel-vs-netlify-vs-cloudflare-pages-free-frontend-hosting-compared-3h9g). These are secondary 2026 blogs, and some numbers conflict between them; verify on vendor pages.
- **Replit:** the free Starter plan still exists in 2026, but **live deployment is listed under the paid Core tier**. Sources disagree on whether Core costs $20 or $25/month. — [Replit docs pricing](https://docs.replit.com/help/pricing-and-plans.md); [wearefounders 2026](https://www.wearefounders.uk/replit-pricing-what-you-actually-pay-to-build-apps/)

### Inferences
- **Tiered project menu**, chosen for ship-ability in about 4 build sessions:
  - *Tier 1 (default, nearly everyone ships):* single-page static site, such as a personal portfolio, a fan page or wiki for a hobby, a quiz or personality test, a flashcard tool, a calculator or converter, or a "choose-your-own-adventure" story. Deploy with GitHub Pages or Netlify Drop.
  - *Tier 2 (comfortable students):* a browser game in plain JS or canvas (clicker, snake, memory match, trivia), an app with localStorage (to-do, habit tracker), or a page using a free no-key public API (weather, Pokémon, jokes). Still static and deployed the same way.
  - *Tier 3 (advanced high schoolers only):* a Chrome extension (loaded unpacked for the demo; publishing to the Chrome Web Store costs a one-time developer fee — not verified in this research), a Discord bot (needs always-on hosting, which is hard to get free), or a full-stack app on Vercel.
- Avoid anything that needs a backend, API keys, logins, or a database in a 4–6 week beginner program. Keys leak into public repos, hosting costs money, and it adds privacy risk for minors.
- Netlify Drop works without git, so the first deploy can happen in Session 1 or 2. GitHub Pages teaches git and versioning but needs a GitHub account, which requires age 13+. Under-13s can deploy through a parent's or leader's account, or a shared "club" org, with consent.
- Define "shipped" up front: (1) a public URL that loads on a phone, (2) at least one interactive feature that works, (3) a README or "about" stating what AI did and what the student did. This applies Hack Club's lesson that rewards should require a real ship.

### Gaps
- Chrome Web Store fee and Discord bot free-hosting options for 2026 were not verified.
- No data was found on completion rates by project type for teens.

---

## 3. Peer-led / near-peer teaching; mixed ages and skill levels

### Takeaway
Near-peer mentoring has consistently positive but mostly small and qualitative evidence. It improves mentees' STEM attitudes, identity, and self-efficacy, and helps mentors' own learning and belonging. Programs that keep older teens tend to separate activities by age and give teens leadership roles, which matters for a mixed 11–18 room.

### Cited Findings
- A systematic review of near-peer mentoring in STEM/STEAM reported a positive effect on students' attitudes, perceptions, and beliefs, and improved STEM academic achievement. — [Texas A&M poster / review summary](https://srw.tamu.edu/wp-content/uploads/2021/03/Ling_Effects_on_Mentees_Poster.pdf)
- A NYC afterschool program pairing undergraduate STEM majors from similar neighborhoods with middle schoolers found that mentees could more easily imagine STEM futures, and mentors' identity and persistence grew. — [NSF PAR 10385561](https://par.nsf.gov/biblio/10385561)
- In a summer programming camp, participants' self-efficacy increased. High self-efficacy predicts persistence in STEM, especially for girls. Interest in STEM careers did not rise, likely because it was already high at the start. — [ASEE PEER](https://peer.asee.org/40697)
- Mentors at a STEM camp developed teaching skills and a stronger sense of belonging, and consolidated their own knowledge. The authors note that mentor benefits are less clear in the broader literature. — [ASEE: benefits of near-peer mentoring](https://peer.asee.org/educational-enrichment-the-benefits-of-near-peer-mentoring-for-undergraduate-engineering-students)
- High school students in a lab-based near-peer program reported benefits in science learning, educational planning, and life lessons. — [JSTEM](https://jstem.org/jstem/index.php/JSTEM/article/view/2185)
- High-retention out-of-school programs **separated activities by age**, set different attendance expectations for older teens, and offered **many leadership opportunities**. "How the program was offered was just as important as what was offered." — [Youth Today summary of HFRP/P/PV study](https://youthtoday.org/?p=6880); [Wallace Foundation report](https://www.wallacefoundation.org/sites/default/files/2023-08/Engaging-Older-Youth-City-Level-Strategies-Support-Sustained-Participation-Out-of-School-Time.pdf)
- The differing developmental needs of middle and high schoolers, and even of younger and older youth within each band, are described as key to retention. — [informalscience.org: Participation over time](https://informalscience.org/research/participation-over-time-keeping-youth-engaged-middle-school-high-school)

### Inferences
- **Benefits for the two teen leaders:** credibility and relatability with participants, and their own learning and resume value. **Pitfalls** (inferred, not directly sourced): limited authority with middle schoolers, burnout from also handling logistics, lack of training for safeguarding and behavior issues, and the tendency to "just fix it" for students (the human version of shepherding). Mitigations: a written facilitator script per session, a library staff member present for supervision and safeguarding, a "hands off the keyboard" rule for leaders, and recruiting 1–2 returning or advanced participants as "junior mentors." This also builds in the leadership roles that high-retention programs offered.
- **Mixed ages and skills:** group tables by age band (roughly 11–13 and 14–18) and pair within skill level, or pair a stronger student as navigator with a beginner as driver so the beginner types. Use the tiered project menu so everyone has the same "ship" bar but a different ceiling. Offer "stretch cards" for fast finishers.
- Treat older high-schoolers as apprentices or co-mentors. The Wallace and HFRP findings say older teens respond to job-like roles and leadership.

### Gaps
- No studies were found specifically on **teen-run** (high schooler as instructor) coding workshops. Evidence is mostly undergraduate mentors with middle or high schoolers.
- No source was found quantifying pitfalls of teen instructors, such as classroom management or safeguarding.

---

## 4. Engagement and retention in free multi-week out-of-school programs

### Takeaway
Free drop-in programs face real attendance decline, especially among older teens. Retention is linked to youth leadership roles, age-appropriate design, strong relationships with staff and peers, youth input, and skill-building that feels "real." Shipping requirements and tangible incentives (Hack Club) give a concrete goal, but incentives tied only to participation invite low-quality output.

### Cited Findings
- HFRP and Public/Private Ventures studied 198 programs. They defined high retention as keeping **50%+ of youth for 12+ months**. Programs with high retention shared five characteristics, including many youth leadership opportunities (at least five varied ones, sustained). — [EOY Study, Global FRP archive](https://archive.globalfrp.org/EOY-Study); [Youth Today](https://youthtoday.org/?p=6880)
- Practices reported as important, though not statistically tied to retention: a sense of community through staff and peer relationships, using peers as recruiters, and matching program features to what youth want. In one clubhouse initiative, 80% of teens reported having a caring adult available. — [YouthREX summary](https://youthrex.com/research-summary/engaging-older-youth-program-and-city-level-strategies-to-support-sustained-participation-in-out-of-school-time/)
- Older teens respond to job-like programming, apprenticeships, mentoring, and specific skills they want to learn. Asking teens what they want is described as critical. — [youth.gov: Engaging older youth](https://youth.gov/shared-resources/engaging-older-youth); [Wallace chapter 2](https://www.wallacefoundation.org/knowledge-center/pages/chapter-2-engaging-older-youth.aspx?p=2)
- Hack Club YSWS programs are free and reward *approved* ships with physical rewards (stickers, shirts, hardware). Hack Club learned that rewarding participation without a quality bar produced "slop," and moved to requiring a real ship. — [ysws.hackclub.com](https://ysws.hackclub.com/); [Why We Ship](https://essays.hackclub.com/why-we-ship/)

### Inferences
- **Retention levers for a no-budget library program:**
  - **Ship something in Session 1.** Even a "hello world" page live at a URL creates early momentum.
  - **A visible, public demo day with a real audience**: parents, library staff, and possibly a local official or tech professional. Announce the date in Session 1.
  - **Free incentives:** certificates, an online "gallery" page linking every shipped project, LinkedIn or college-application-ready descriptions for high schoolers, and volunteer-hour credit for junior mentors. Food and prizes could be sought as in-kind donations from local businesses or the library's Friends group, or through Hack Club programs (unverified for 2026). The researcher found no sourced data on food's effect on attendance.
  - **Leadership roles:** session "demo captain," "bug bounty hunter," junior mentor.
  - **Youth voice:** let participants choose projects from the menu and vote on stretch topics.
  - **Weekly reminders** to participants and parents, and a short "you missed this" recap so absences do not become dropouts.
- Expect declining attendance across sessions. Design so a student who misses one session can still ship: each session has its own self-contained goal, with catch-up checklists.
- Prefer a **4–6 session** arc over 8, given drop-off risk and the leaders' capacity. This is an inference; no direct evidence was found comparing program lengths.

### Gaps
- No recent (2023–2026) quantitative data was found on week-over-week attendance drop-off in free teen coding workshops. The main retention study dates from 2010.
- Afterschool Alliance's "America After 3PM" data was not retrieved in this pass.
- No evidence was found on the specific effects of food, certificates, or prizes on attendance.

---

## 5. Integrating critical AI literacy without lecturing

### Takeaway
Free, ready-to-use, activity-based materials exist, notably MIT-affiliated **Day of AI** units on bias, verification, and privacy, Google Teachable Machine, and Quick Draw. The most natural fit for a build program is to embed short critical-thinking "checkpoints" in the build itself: verify AI claims, inspect AI code for errors, audit the project's privacy, and credit AI in the README.

### Cited Findings
- Day of AI (created by MIT RAISE, independent nonprofit since 2024) has a free middle-grades unit. It covers predictions, data, machine learning, **bias and fairness** (a lesson where students investigate algorithmic bias and design ways to explain it), and **privacy**, and uses Google Quick Draw to show datasets and bias. — [Day of AI: AI Foundations for Middle Grades](https://dayofai.org/units/ai-foundations-for-middle-grades); [About](https://dayofai.org/about)
- The Day of AI unit "Truth, Tricks, and AI" teaches students to spot misinformation in AI output and verify it, stressing that AI "can sound confident even when it is not." — [Day of AI: Truth, Tricks, and AI](https://dayofai.org/units/truth-tricks-and-ai-learning-to-verify-information)
- Day of AI has launched a free grade-by-grade PreK–12 AI literacy curriculum. — [Day of AI news](https://dayofai.org/news/day-of-ai-launches-nations-first-free-grade-by-grade-prek-12-ai-literacy-curriculum)
- MIT RAISE has published a 2025 brief, "Establishing AI Literacy before Adopting AI." — [MIT RAISE PDF](https://raise.mit.edu/wp-content/uploads/2025/11/Establishing-AI-Literacy-before-Adopting-AI.pdf)
- Teachable Machine (hands-on bias via training data) and MIT Media Lab's Moral Machine are commonly recommended. AI4K12 is described as a comprehensive free K-12 resource. — [tutorials.technology framework](https://tutorials.technology/tutorials/teaching-ai-literacy-classroom.html) (secondary source)
- The Raspberry Pi Foundation's Experience AI program (with Google DeepMind) has a 2026 impact report. Raspberry Pi researchers propose a "data paradigms" framework for teaching AI and data-driven systems separately from traditional programming. — [Experience AI Impact Report 2026](https://static.raspberrypi.org/files/about/Experience_AI_Impact_report_2026.pdf); [EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/raspberry-pi-foundation-research-sets-out-new-framework-for-teaching-ai-and-data-science)
- Even well-designed tutor AIs give occasionally incorrect feedback while sounding confident (CodeAid student quote). That makes students' own projects a live source of AI errors to discuss. — [Austin Henley blog](https://austinhenley.com/blog/codeaid.html)

### Inferences (activity ideas; 10–15 min "AI checkpoint" per session)
- **Hallucinations: "Catch the AI lying."** Ask the AI about something local (the library's hours, a Collierville landmark) or for a citation, then verify. Or ask it which library function to use and check the docs. A score sheet tracks the room's "hallucination catches" across weeks.
- **Code errors: "Bug bounty."** Leaders plant an AI-generated snippet with a subtle bug, and pairs race to find it. This also trains debugging.
- **Bias: Teachable Machine or Quick Draw demo**, 10 min. Or ask an image or text model for "a programmer" or "a CEO" and discuss who appears. Day of AI's bias lesson can be adapted.
- **Privacy: "Privacy audit" of your own project.** What data does your app collect? Is there anything in the prompt you shouldn't paste (real names, school, address)? Did you commit a secret? This ties directly to minors' safety.
- **IP and attribution: "Credits roll."** Every README has an "AI used for…" and "I did…" section, plus asset licenses. Discuss who owns AI-generated code.
- **Environmental cost: "Estimate and debate."** Quick discussion of energy and water per query using a reputable figure the leaders pre-select (not sourced here). Ask whether it is worth using AI for a task you could do by hand.
- **Jobs: "Would you hire this AI?"** At demo-day prep, students identify what in their project the AI could *not* do: picking the idea, judging the result, fixing the weird bug. This connects to the Raspberry Pi argument that human judgment remains essential.
- Rotate one theme per session so literacy is spread across the arc rather than delivered as a lecture block. Demo-day presentations should include a "one thing AI got wrong" slide.

### Gaps
- No evaluation was found of embedding AI literacy *inside* a coding or build program, as opposed to standalone units.
- No vetted environmental-cost figure was retrieved. Leaders should source one before using it.
- "RAICA" (named in the assignment) was not found in search; Day of AI / MIT RAISE are the relevant MIT resources.

---

## 6. Measuring success (for grant applications)

### Takeaway
Combine simple counts (enrollment, attendance per session, % who ship a live URL, demo-day attendance) with a short validated or adapted pre/post survey on self-efficacy and engagement. A **retrospective pre/post** ("before this program I… / now I…") may suit youth better than separate pre and post surveys.

### Cited Findings
- The PEAR Institute's **Common Instrument** is a brief, valid, and reliable self-report survey of STEM engagement (14 items, about 5 minutes). PEAR also has the Dimensions of Success observation tool. — [NSTA: Common Instrument Suite](https://www.nsta.org/connected-science-learning/connected-science-learning-july-september-2019/common-instrument-suite)
- PEAR's ATIS is described as a free service, but whether the Common Instrument itself is free to small programs was not confirmed. — [NSTA](https://www.nsta.org/connected-science-learning/connected-science-learning-july-september-2019/common-instrument-suite)
- A free STEM Program Quality Assessment observation tool is available on request. — [WestEd CSAA](https://csaa.wested.org/resource/science-technology-engineering-and-mathematics-program-quality-assessment/)
- A maker-program study found that youth struggled to accurately judge their own change in traditional pre/post surveys, and compared that with a **retrospective** design. — [ASEE PEER 24064](https://peer.asee.org/24064.pdf)
- Afterschool engineering evaluations have used pre/post items on attitudes, career interest, and self-efficacy in design and presenting. — [ASEE NEMO paper](https://nemo.asee.org/public/conferences/374/papers/51388/download)
- The HFRP retention benchmark (50%+ retained) gives a vocabulary for reporting retention. — [EOY Study](https://archive.globalfrp.org/EOY-Study)

### Inferences (suggested metrics dashboard)
- **Reach:** registrations, unique attendees, age and grade mix, % first-time coders, % girls and underrepresented groups (collected optionally and anonymously).
- **Engagement:** attendance per session, the % who attended at least 75% of sessions (the program's own retention rate), and the drop-off curve.
- **Output:** % of participants who shipped a live URL meeting the "shipped" definition, plus a public gallery of links. Demo-day audience count.
- **Learning and attitude**, using a 5–8 item retrospective pre/post on a 1–5 scale. Example items: "I can build and publish a website," "I can explain what my code does," "I can tell when an AI answer is wrong," "I know what not to share with an AI tool," "I want to keep coding." Add one **explain-back rubric** score at demo day (can they explain one function they shipped?).
- **Qualitative:** 2–3 student quotes and a photo of demo day (with photo consent). Parent feedback.
- **Leader outcomes:** hours led and reflections. These are useful for the leaders' own applications and for near-peer grant framing.
- Keep surveys anonymous or minimally identifying, and use paper or Google Forms with parent consent for minors.

### Gaps
- Free access terms for the PEAR Common Instrument were not confirmed.
- No validated instrument specifically for "AI literacy" in teens was retrieved in this pass.
- Grant-funder expectations (e.g., local library foundations, Hack Club grants) were not researched.

---

### Cross-cutting synthesis notes for the report writer (inferences, not sourced)
**Suggested 6-session pattern (each about 2 hr):** 15 min check-in and demo of last week's progress, then 10–15 min AI-literacy checkpoint, then 60–75 min build in pairs with explain-back gates, then 10 min ship (push or deploy) and a prompt-journal entry.

1. **Kickoff:** a teen-leader demo of AI building something live; tool and consent setup; deploy a "hello" page on Netlify Drop or GitHub Pages; literacy topic: "AI is confident, not always correct."
2. **Idea and scope:** choose from the tier menu; write a one-sentence pitch and a 3-feature MVP; first real feature; literacy: privacy.
3. **Build:** the core feature; "modify before generate"; literacy: bug bounty / hallucination catch.
4. **Build and debug:** debugging with AI as tutor; literacy: bias.
5. **Polish and test:** user testing by a peer, mobile check, README with "AI credits"; literacy: IP and jobs.
6. **Demo day:** 2–3 minute demos covering what it does, one thing the AI got wrong, and what I learned; certificates; gallery link; post-survey.

For 4 sessions, merge 2+3 and 4+5. For 8, add a second build week and a "feature freeze plus practice demo" session.

**Top failure modes to warn about:** account and age blockers eating Session 1; scope creep, such as "I want to build a full social network"; projects that need backends or API keys; AI shepherding and drifting, where students cannot explain their own code; leaders fixing code for students; mixed-age friction; attendance drop after week 2–3; no shipped URL by demo day; privacy slip-ups (real names, faces, or keys in public repos).
