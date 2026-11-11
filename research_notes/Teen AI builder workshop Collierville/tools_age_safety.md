# AI Tool Age Restrictions, ToS, Privacy & Safety for a Teen (ages ~11–18) Library Workshop in Tennessee (as of Nov 10, 2026)

Research scope: 17 web searches and fetches on Nov 10, 2026. Most vendor age clauses were checked against primary ToS or help pages. Items marked "secondary" or "unverified" were not confirmed from a primary source.

## 1. Anthropic: Claude.ai, Claude Code, API, and provisions for minors

### Takeaway
Claude's consumer product (Claude.ai and apps) is strictly 18+. Since 2026 Anthropic enforces this with under-18 signal detection, account disabling, and Yoti age verification. No teen account or parental-consent route exists. The only sanctioned way for minors to use Claude models is an organization building a product on the API, with safeguards. That path (child-safety measures, COPPA compliance, mandatory AI disclosure, possible audits) is heavy for a one-off library workshop run by students. In practice, teens in this workshop should not use their own Claude.ai or Claude Code accounts.

### Cited Findings
- Consumer Terms, §2 "Account creation and access," Minimum age: "You must be at least 18 years old or the minimum age required to consent to use the Services in your location, whichever is higher." Effective Oct 8, 2025. — [Anthropic Consumer Terms](https://www.anthropic.com/legal/consumer-terms)
- Help Center "Age assurance on Claude" (dated May 18, 2026): "Claude, our consumer product, is only available to people over 18 years." Users confirm 18+ at signup. "When we detect signals that you may be under 18, we'll ask you to verify your age before you can continue using Claude." Accounts may be disabled based on indicators of minor activity. Reinstatement goes through Yoti (facial age estimation, ID document, or Yoti Digital ID "over 18" attribute), and Anthropic receives only pass/fail. — [Age assurance on Claude](https://support.claude.com/en/articles/15171100-age-assurance-on-claude)
- If the device's app store has identified the user as under 18, the Claude app shows a restriction message. — [Minimum age requirement / access restriction](https://support.claude.com/en/articles/13117299-minimum-age-requirement-access-restriction) (seen via search summary; not fetched in full)
- Secondary reports describe adults being wrongly flagged as minors and suspended, then reinstated after ID. — [Digit](https://www.digit.in/news/general/anthropic-under-scrutiny-as-claude-flags-users-as-minors-here-is-how-to-unlock-your-account.html); [Kompozy](https://kompozy.io/news/anthropic-claude-age-assurance-18-plus) (secondary)
- "Responsible Use of Anthropic's Models: Guidelines for Organizations Serving Minors" (updated Mar 16, 2026) applies to "organizations providing minors with the ability to directly interact with products that incorporate our API(s)." Organizations "should implement" safeguards such as age verification, content filtering, monitoring and reporting, and educational resources for minors. Anthropic "may provide a child-safety system prompt" for them to use. "It is the responsibility of organizations to comply with all applicable child safety and data privacy regulations" (COPPA is named). Organizations "must disclose to their users that they are interacting with an AI system rather than a human." Anthropic periodically audits for compliance. — [Anthropic Help Center: Guidelines for Organizations Serving Minors](https://support.claude.com/en/articles/9307344-responsible-use-of-anthropic-s-models-guidelines-for-organizations-serving-minors)
- This path dates from Anthropic's May 2024 usage-policy update, which allowed organizations to put the API into products for minors if they implement safety features and disclose AI use. — [TechCrunch, May 2024](https://techcrunch.com/2024/05/10/anthropic-now-lets-kids-use-its-ai-tech-within-limits); [Anthropic: Updating our usage policy](https://anthropic.com/news/updating-our-usage-policy)
- Anthropic also publishes "Child safety guidance for developers." — [support.claude.com 15591275](https://support.claude.com/en/articles/15591275-child-safety-guidance-for-developers) (found in search, not fetched)
- Common Sense Media's risk assessment (Mar 25, 2026) says Claude is built for adults. — [Common Sense Media risk assessment PDF](https://institute.commonsensemedia.org/sites/default/files/risk-assessments/csm-ai-risk-assessment-claude-03252026%20%281%29.pdf) (via search summary)

### Inferences
- Claude Code needs a Claude.ai subscription (Pro/Max) or an Anthropic Console/API account, so the 18+ consumer rule (or commercial-account adult status) effectively applies. A teen cannot legitimately hold their own Claude Code login.
- Compliant ways to use Claude in the workshop:
  - (a) An adult (librarian or adult sponsor) operates Claude or Claude Code on a presenter screen while teens direct prompts verbally ("instructor-operated demo").
  - (b) The organizers ship a small API-based app (adult-owned API key, server-side) for teens to use, following the minors guidelines: AI disclosure, child-safety system prompt, content filtering, no collection of personal info. This makes the organization the "organization serving minors" and carries real compliance responsibility. That is probably too heavy for two high-school organizers without an adult/institutional owner.
- The organizers are minors. If either is under 18, they cannot hold a Claude account themselves. An adult must own any Anthropic account used.

### Gaps
- Did not fetch the current Anthropic Usage Policy / Commercial Terms text to quote the exact minors clause. The Help Center article above is the primary source used.
- Could not confirm whether Claude for Education covers K-12 or under-18 students. None of the pages reviewed say it does. Assume it is for higher-ed and adult institutional users unless Anthropic sales confirms otherwise.
- Did not confirm whether Claude Code has its own age language beyond the Consumer/Commercial Terms.

## 2. Other likely tools: age requirements and "teen-OK" options

### Takeaway
The most clearly teen-OK stack for building and shipping a small site is **GitHub (13+) + GitHub Pages**, plus **GitHub Copilot via GitHub Education (13+, verified students)**, or **Replit** (parental responsibility for minors). **ChatGPT** allows 13–17 with parent/guardian permission, and teen protections apply automatically. **Gemini** is available to minors through school Workspace for Education accounts if the school admin enables it. **Vercel (16+)** and **Lovable (18+ or parental permission)** are only partially usable. Bolt, Cursor, Netlify, and Microsoft Copilot were not verified.

### Cited Findings
- **ChatGPT / OpenAI** (Terms of Use effective Jan 1, 2026): users must be at least 13 (or the country minimum), and users under 18 need a parent or guardian's permission. — [OpenAI Terms of Use](https://www.openai.com/policies/terms-of-use/) (via search summary, not fetched directly)
- ChatGPT for Teens applies stronger safeguards for ages 13–17. Under-18 status is set by account age, verified age, or OpenAI's age-prediction system. Linked parents can manage quiet hours, voice, image generation, memory, and training opt-out, but cannot read chats. OpenAI acknowledges age prediction can make mistakes. — [TechRepublic, Aug 2026](https://techrepublic.com/article/news-chatgpt-teens-safety-gaps/); [NBC parental controls coverage](https://www.nbcchicago.com/news/national-international/chatgpt-new-parental-controls/3830907/)
- **Google Gemini:** In 2024, Gemini was opened to teen students (13+) on Workspace for Education accounts, off by default until an admin enables it, with added data protection. — [Google Workspace Updates, Oct 2024](https://workspaceupdates.googleblog.com/2024/10/gemini-app-access-for-teen-students-workspace-education.html?hl=ar); [TechCrunch, Jun 2024](https://techcrunch.com/2024/06/24/google-is-bringing-gemini-access-to-teens-using-their-school-accounts/)
- The Gemini app was later made available to Workspace for Education students of all ages as a core service, with stricter content policies for under-18 users. Gemini for Education follows Workspace for Education data protection terms. — [Google blog, ISTE 2025](https://blog.google/products-and-platforms/products/education/gemini-iste-2025/); [Neowin](https://www.neowin.net/news/google-brings-gemini-to-all-workspace-for-education-subscribers/)
- **GitHub** ToS: "A User must be at least 13 years of age" (§A(11)) and "You must be age 13 or older" (§B(3)). Under-13 accounts are terminated on discovery. The ToS has no parental-consent process for ages 13–17. — [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service)
- **GitHub Copilot via GitHub Education:** verified students get free Copilot access, described as a Copilot Pro subscription and, per a March 2026 community FAQ, a "GitHub Copilot Student" plan. Microsoft Learn says Copilot is free for verified learners and educators 13+. Academic verification is required. — [GitHub Docs: Copilot for students](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students); [Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/embark-ai-journey-free-ai-tools-microsoft-education/improve-coding-skills-github-copilot); [GitHub community FAQ #111352](https://github.com/orgs/community/discussions/111352)
- **Replit** ToS (Feb 23, 2026), per search excerpt: "You must be an adult to use the Service. If you are younger than 13 we will allow you to use the Service if you first provide us with your parent or guardian's written consent." By allowing a child to use the Service, the parent is "subject to these Terms and responsible for your child's activity." The excerpt mixes "adult" and "under 13" language, so read the full clause before relying on it. — [Replit ToS, Feb 23, 2026](https://replit.com/terms-of-service-02-23-2026)
- **Vercel** ToS (last updated Oct 19, 2026), Age and Eligibility: "You certify that you are a person at least 16 years of age." This also covers v0. Vercel's separate AI Product Terms reportedly set 13+ in the US. — [Vercel Terms](https://vercel.com/legal/terms.md); [Vercel AI Product Terms](https://vercel.com/legal/ai-product-terms) (AI terms age via search summary)
- **Lovable:** terms (seen in the Indonesian-language version) require 18+ or age of majority, and under-18s need parent/guardian permission. English version not confirmed. — [Lovable terms](https://lovable.dev/terms) (via search summary); secondary blog agrees: [Olune comparison](https://getolune.com/vibe-coding/lovable-vs-bolt-vs-replit)

### Inferences
- Ranking of teen-OK build-and-deploy options for ages 13–17:
  1. GitHub account + GitHub Pages hosting (13+, free, no payment needed). Copilot is available only to teens who can complete GitHub Education student verification, which takes time; do it before the workshop.
  2. Replit, with parent consent/responsibility captured on the workshop permission form.
  3. ChatGPT with the parent permission captured on the form. Teen safeguards apply.
  4. Gemini via school Google accounts, only if the teens' school district has enabled it. Many TN districts may not have.
- Vercel excludes 13–15-year-olds. Lovable requires parental permission at minimum. Claude consumer products are out for everyone under 18.
- Under-13 participants (age 11–12): GitHub and ChatGPT are not allowed, and Replit needs written parental consent. Plan an offline or instructor-driven track, or set the program age floor at 13.

### Gaps
- Not verified: Microsoft Copilot consumer age (believed 13+ with teen protections, unconfirmed), Bolt.new, Cursor, Netlify, Glitch alternatives, Scratch, and Code.org AI tools. Check each vendor's current ToS directly.
- Did not verify whether GitHub Education student verification works for high schoolers without a school email. It reportedly requires proof of enrollment.

## 3. Practical workarounds when a tool is 18+

### Takeaway
The standard compliant patterns are an adult-operated presenter account (teens direct, the adult types), an adult- or library-owned organizational account or API key behind an app built with the safeguards above, or switching teens to tools with a 13+ teen path. A minor organizer sharing their own adult-tier account with teens is not compliant.

### Cited Findings
- Anthropic permits minors only through organizations that build on the API and implement safeguards plus AI disclosure. — [Anthropic minors guidelines](https://support.claude.com/en/articles/9307344-responsible-use-of-anthropic-s-models-guidelines-for-organizations-serving-minors)
- Anthropic actively detects and disables accounts that show signs of minor use, so a shared login used by teens risks suspension. — [Age assurance on Claude](https://support.claude.com/en/articles/15171100-age-assurance-on-claude)

### Inferences
- Recommended setup:
  - (1) An adult sponsor runs Claude Code on a projector to demonstrate the build-and-ship workflow.
  - (2) Teens build hands-on with 13+ tools (GitHub Pages, ChatGPT teen with parental permission, Replit), or with plain HTML/CSS/JS plus the AI assistance their parents approved.
  - (3) Any shared API key stays with the adult, server-side, never on teen machines.

### Gaps
- Found no published case study of a library or student-run workshop using an adult-owned Claude org account for minors.

## 4. COPPA, Tennessee law, and library privacy

### Takeaway
COPPA governs online services collecting data from under-13s. The amended COPPA Rule has been fully in force since Apr 22, 2026. It binds operators (vendors), but it is why most tools exclude under-13s. Tennessee has no enacted statute specifically regulating minors' use of AI chatbots as of Nov 2026: the 2026 CHAT Act was reduced to a TACIR study. TN's Protecting Children from Social Media Act (parental consent and age verification for minors' social media accounts) is in effect but under litigation, and it targets social media platforms, not this workshop.

### Cited Findings
- Amended COPPA Rule: published Apr 22, 2025, effective Jun 23, 2025, compliance required by Apr 22, 2026. It adds separate verifiable parental consent for disclosure to third parties for targeted advertising and requires a written information security policy. — [Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/coppa-rule-amendment-compliance-deadline-approaches); [Davis Polk](https://www.davispolk.com/insights/client-update/ftc-prioritizes-coppa-enforcement-new-compliance-obligations-take-effect); [Toy Association](https://www.toyassociation.org/PressRoom2/News/2026-News/updated-coppa-rule-requirements-take-effect-april-22.aspx)
- FTC Policy Statement (Feb 25, 2026) limiting COPPA enforcement when children's data is collected solely for age verification. — [Davis Polk](https://www.davispolk.com/insights/client-update/ftc-prioritizes-coppa-enforcement-new-compliance-obligations-take-effect) (via search summary)
- Tennessee CHAT Act (HB1946/SB1700) was signed Apr 21, 2026 as Public Chapter 1082. The minor-chatbot restrictions in the introduced version, including a companion-chatbot ban for minors, were stripped. The enacted law directs a TACIR study of AI chatbot regulation, including safeguards for minors. — [AI Laws USA](https://ailawsusa.com/protection/tn-tacir-ai-chatbot-regulation-study-pc1082-2026/); [Keeping Law Simple SB1700](https://www.keepinglawsimple.org/states/tennessee/bills/2026/SB1700) (secondary; verify against TN Secretary of State public chapter text)
- SB 1580 / Public Chapter 647 (effective Jul 1, 2026) bars advertising an AI system as a qualified mental health professional. — [Vensure](https://vensure.com/employment-law-updates/tennessee/tennessee-bans-ai-posing-as-licensed-therapists/) (secondary)
- 2026 TN legislative tracking of child-related bills: [TCCY 2026 Tracked Legislation](https://www.tn.gov/content/dam/tn/tccy/documents/legislative/2026-session/2026TrackedLegislation.pdf)
- Protecting Children from Social Media Act (HB1891, 2024; Tenn. Code Ann. §§ 47-18-5701 to -5706, effective Jan 1, 2025) requires social media companies to verify age, obtain parental consent for minors' accounts, and provide parental supervision tools. AG enforcement only. — [TN Attorney General](https://www.tn.gov/attorneygeneral/news/2026/2/4/pr26-7.html); [LegiScan chaptered text](https://legiscan.com/TN/text/HB1891/id/2996335/Tennessee-2023-HB1891-Chaptered.pdf)
- NetChoice v. Skrmetti: the Sixth Circuit (Aug 28, 2026) sent the preliminary-injunction question back to the district court, where it was pending as of Oct 2026. — [Bloomberg Law](https://news.bloomberglaw.com/states-of-play/tennessee-social-media-law-must-be-newly-parsed-6th-cir-says) (secondary trackers; verify docket)
- ALA: library users of all ages have privacy rights. Staff serving minors should understand FERPA, COPPA, and PPRA, and staff and volunteers should be trained on privacy and confidentiality of records. — [ALA Library Privacy Guidelines for Students in K-12](https://www.ala.org/advocacy/privacy/guidelines/students); [ALA K-12 Privacy Checklist](https://www.ala.org/advocacy/privacy/checklists/students); [ALA Students & Minors](https://www.ala.org/advocacy/privacy/students); [YALSA teens' privacy position paper](https://www.ala.org/yalsa/library%E2%80%99s-role-protecting-teens%E2%80%99-privacy-yalsa-position-paper)
- ALA: only parents or guardians should restrict their own children's access to library services. — [ALA Access for Minors interpretation](https://www.ala.org/advocacy/intfreedom/librarybill/interpretations/minors)

### Inferences
- The workshop itself is not a COPPA "operator" unless it builds a site or app that collects personal information from under-13s. Teen-built apps should not collect personal info from visitors (no sign-up forms, no analytics on kids).
- The TN social media law likely doesn't cover AI coding tools or GitHub, but this is a legal judgment, not something verified.
- Sign-up/registration data the library collects is likely covered by Tennessee's library-records confidentiality law, which I could not verify this session. Keep only what the library form requires.

### Gaps
- Did not retrieve the Tennessee library records confidentiality statute (believed to be T.C.A. § 10-8-101 et seq., unverified) or the specific Collierville (Lucius E. & Elsie C. Burch Jr.) Library policies on minors, photos, or programs. Ask the library.
- Did not verify the COPPA civil penalty amount for 2026.

## 5. Consent, waiver, photo release, and supervision paperwork

### Takeaway
Libraries typically require a signed parent/guardian photo/media release for minors. The library will likely require an adult sponsor (staff or vetted volunteer) present for a program run by minors. A practical packet: library program registration, a parent/guardian permission form (including consent for named AI tools/accounts per their ToS), a photo/media release, emergency contact, and a technology acceptable-use agreement.

### Cited Findings
- Example from a nearby West TN library (Tipton County Public Library): photos of minors (under 18) may be used in print, web, and video only when conditions are met, including a signed parent/guardian release. — [Tipton County Library photo policy PDF](https://tiptoncountylibrary.org/wp-content/uploads/2024/10/photo091624.pdf) (via search summary)
- ALA recommends training staff and volunteers on minors' privacy. — [ALA K-12 Privacy Checklist](https://www.ala.org/advocacy/privacy/checklists/students)
- OpenAI requires parent/guardian permission for under-18 users. Replit makes the parent responsible for a child's activity. — [OpenAI Terms](https://www.openai.com/policies/terms-of-use/); [Replit ToS](https://replit.com/terms-of-service-02-23-2026)

### Inferences
- Recommended forms:
  - (1) Parent/guardian permission naming each tool, its age rule, and that the teen will create or use an account (GitHub 13+, ChatGPT with parent permission, Replit).
  - (2) Photo/video release, opt-in, with no names published alongside faces.
  - (3) Teen code of conduct and AI acceptable-use pledge.
  - (4) Emergency contact and pickup info.
- Use the library's own forms where they exist.
- Organizers under 18 should work under the library's teen volunteer process with a staff liaison or adult sponsor present at all sessions. They should not collect or keep parent data themselves; the library holds it.

### Gaps
- Found no authoritative national standard (ALA or TN State Library) on minors running library programs, or on background-check requirements for adult sponsors. These are set by local library or city policy, so ask the Collierville library and the Town of Collierville volunteer office.

## 6. Safety and privacy rules to teach and enforce

### Takeaway
Core rules: no personal info in prompts or apps, AI disclosure, secrets never in client code or public repos, adult-held keys, age-appropriate content safeguards, and human review before shipping.

### Cited Findings
- Anthropic requires AI disclosure to minors and recommends content filtering, monitoring, age verification, and a child-safety system prompt for products serving minors. — [Anthropic minors guidelines](https://support.claude.com/en/articles/9307344-responsible-use-of-anthropic-s-models-guidelines-for-organizations-serving-minors)
- Common Sense Media found Claude's responses can be too complex or mature for teens even when age checks work. — [Common Sense Media Claude risk assessment](https://institute.commonsensemedia.org/sites/default/files/risk-assessments/csm-ai-risk-assessment-claude-03252026%20%281%29.pdf) (via search summary)
- ChatGPT's teen experience adds content safeguards. Parents can disable training on conversations. — [TechRepublic](https://techrepublic.com/article/news-chatgpt-teens-safety-gaps/)
- TACIR's 2026 AI and child-safety panel recommended age-appropriate defaults, clearer disclosures, testing, and human escalation pathways. — [Citizen Portal summary of TN hearing](https://citizenportal.ai/articles/10329712/Tennessee/2026-Legislature-TN/Experts-warn-of-AI-risks-to-children-urge-ageappropriate-defaults-testing-and-duty-of-care) (secondary)

### Inferences
- Teach and enforce:
  - Never paste your or others' real name, address, school, phone, photos, or passwords into AI.
  - Apps must not collect visitors' personal data.
  - API keys stay with the adult and never go in front-end code or GitHub (use .gitignore and env vars, and enable GitHub secret scanning).
  - Use synthetic or test data only.
  - Turn off "improve the model" / training where available.
  - An adult reviews every site before publishing.
  - Report anything upsetting to the adult sponsor.
  - AI output can be wrong; verify it.

### Gaps
- Did not find a library-specific AI acceptable-use template. Did not verify GitHub secret-scanning defaults for free personal accounts.
