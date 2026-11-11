# ai-workshop

A free, peer-led AI workshop for middle and high schoolers in Collierville, TN, starting at the Collierville library (Burch Library). Memphis Public Libraries may come later.

This repo is the shared workspace for both co-founders and for each of our Claude agents. Plans, research, curriculum, and decisions all live here.

## Where things are

| Path | What it is |
|---|---|
| `docs/decisions.md` | What we've decided so far, with the date and the reason. Check this first. |
| `docs/open-questions.md` | Things we still need to decide. Answer them here or in a PR. |
| `slideshows/` | **All workshop slide decks** (sessions 1–6, plus certificates). Version 1 is git tag `v1`. |
| `curriculum/` | The session-by-session plans, plus the scripts that build the decks |
| `reports/` | Finished research reports |
| `research_notes/` | Raw notes behind each report |

## How we work (humans and Claudes)

- Work on a branch and open a pull request. Don't push to `main` directly. That way the other co-founder (and their Claude) sees every change and can comment.
- When you decide something, add it to `docs/decisions.md` and remove it from `docs/open-questions.md` in the same PR.
- **Note for Claude agents:** read `docs/decisions.md` and `docs/open-questions.md` before starting work. If you want the other co-founder's Claude to pick something up, leave it as a clearly labeled item under "For the other Claude" in `docs/open-questions.md` and open a PR.
