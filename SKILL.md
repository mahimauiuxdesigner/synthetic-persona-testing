---
name: synthetic-persona-testing
description: Usability testing with synthetic personas on any platform, including multi-role, multi-panel platforms (user, manager, admin, super admin). Asks a short intake (what the platform is, then suggested answers), builds a reusable persona panel role by role, asks for the screens (PDF upload or Figma/URL) and which task to test first, runs persona sessions and an expert check, and delivers a plain-language usability report with five tables, four metrics, a "low effort, high impact" section and an impact-versus-effort view. No slides. Use when someone asks for a "usability test", "synthetic personas", "test this flow/module/platform", or shares screens of a product to test.
---

# synthetic-persona-testing

Pretend users, built on purpose, walking real screens. The method and the report never change.
Only the personas change, and they belong to the **platform**, not to a task.

## The flow

```
1. Intake questions   →  2. Persona panel  →  3. Screens + task  →  4. Sessions
   (2 rounds)              (approve, save)       (PDF or URL;           (subagents, in
                                                  which task first)      character)
→  5. Expert check  →  6. Verify on screen  →  7. Report (HTML + PDF)  →  8. Hand-off
```

If a panel already exists for this platform (`~/Documents/usability/{platform}/persona-panel.md`),
say so in one line and jump to step 3. Ask if they want to update the panel first.

---

## 1. Intake questions (two rounds)
Follow `references/intake-questions.md`.
- **Round 1:** one message, one question: what is the platform, what does it help people do, who
  uses it day to day.
- **Round 2:** predict likely answers for that platform and ask the rest with options
  (AskUserQuestion, up to 4 per call, multi-select where it fits, "(likely)" on the best guess):
  panels and roles, hand-offs, then per-role device, stakes, tech comfort, mood, trust in AI;
  who not to forget; real-user evidence; multitenant last and only if relevant.
- Restate the roles as a hierarchy (`Sales rep → Manager → Org admin → Super admin`) with hand-offs.
- Mark every gap **assumed**. Never invent real-user evidence.

## 2. Persona panel
Follow `references/persona-recipe.md`.
- Role by role: every role gets its own group (main roles at least 3), spread across tech comfort,
  familiarity, device, mood, trust, standing, language, accessibility. Add hand-off pairs.
- 12–18 personas. Real-sounding names. Plain English. No real people.
- Show a short table (name, role, age, tech, familiarity, device, mood, trust), ask for approval or
  changes, then save `~/Documents/usability/{platform}/persona-panel.md`. Platform data may be
  confidential: never inside a GitHub-synced repo.

## 3. Screens and task
Ask in one message:
> Now share the screens: **upload a PDF** (a Figma flow board export works best) **or paste a URL**
> (Figma link or a live page). And tell me **which task you want to test first**, for example
> "deleting a manager" or "uploading a call". You can name more than one.

Then:
- **PDF:** render small, find the frames on the board (grey background, connected components),
  render each frame alone at 80–90 dpi into `screens/`, and check gaps for designer notes.
- **Figma URL:** `get_metadata` then `get_screenshot` per frame; the Starter plan runs out fast, so
  for more than ~10 frames ask for a PDF export instead.
- **Live URL:** open it in the browser, screenshot each step of the task.
- View every screen. Then turn their task into 3–5 concrete test tasks: the main goal, a "check before
  acting" task, a "fix a mistake or back out" task, and one that crosses roles if the screens do.
  Show them in a few lines with the personas you picked; proceed unless they object.
- Pick 6–11 personas: every role that uses these screens, plus one rushed, one doubtful, one
  first-time and one accessibility persona. Each does 1–2 tasks.
- Write `brief.md` (see `assets/example-brief.md`): screens table with ids, tasks, personas, rules.

## 4. Sessions
Parallel subagents, 2–3 personas each, briefed with `references/session-protocol.md`.
Subagents may be blocked from writing files: they return the JSON, you save it to `sessions/`.

## 5. Expert check
One subagent, one pass (repeat passes get worse, Duan et al. CHI 2024). Nielsen's 10, plus what fits:
Human-AI guidelines for AI features, safe-delete patterns, bulk operations, WCAG 2.2 from images,
states and content. Evidence = screen id + exact text. Save `findings-expert.md`.

## 6. Verify
Check every persona and expert finding on the actual screen. Tag: seen on screen, simulated, needs a
real check. Keep mock-data problems (placeholders, repeated names) separate from design problems.
Make annotated proof images for each High and Medium problem: orange boxes and short labels, saved in
`annotated/` (Pillow; Arial Bold labels; avoid symbols the font lacks, like ⋮).

## 7. Report (HTML + PDF, no slides)
Follow `references/report-structure.md`.
1. Write `report-data.json` (schema: `references/report-data-schema.md`; full example:
   `assets/example-report-data.json`). Every number must come from the session JSON.
2. Build: `python3 ~/.claude/skills/synthetic-persona-testing/assets/build_report.py report-data.json`
3. Check it: render in headless Chrome at 1440 px in light and dark, look at every part.
4. PDF: print with Chrome (`--print-to-pdf`, `--no-pdf-header-footer`); render the pages and look
   for broken layouts before delivering.

Report sections: one-minute summary, 1 Summary by user type, 2 How they felt, 3 Patterns,
4 Where they got stuck (with proof), 5 What we learned (3 High), **6 Low effort, high impact**,
7 Everything by impact and effort, How we measured it (completion, time on task, errors,
satisfaction), Before acting on this.

## 8. Hand-off
Save everything in `~/Documents/usability/{platform}/{flow}/`: `screens/`, `annotated/`,
`sessions/`, `brief.md`, `findings-expert.md`, `report-data.json`, the HTML and the PDF.
Open the report. Reply in a few lines: the main finding, the low-effort high-impact fixes, the
four metrics, file paths. Then ask which task to test next (back to step 3, same panel).

---

## Always
- Plain, simple language in the report. Short sentences. One idea per table cell.
- The honest limit in every report: pretend users, not real ones; confirm High items with 3–5 real users.
- Effort is an estimate; say so.
- If a run shows a missing user type, add it to the panel and say so.

## Never
- Call a screenshot review "testing". Personas walk tasks in character.
- Rescue a stuck persona, or invent UI that isn't on the screens.
- Make slides unless they ask.
- Put platform data in a GitHub-synced repo.
