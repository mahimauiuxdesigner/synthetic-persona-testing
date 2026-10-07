# Synthetic persona usability testing

A Claude Code skill that runs usability tests with **synthetic personas**: pretend users, built on
purpose to act like your real ones, walking your real screens.

Use it when you have designs (a prototype or a module on a demo branch) but no real users to test
with yet. It catches the obvious problems early, so real users meet a better product.

## What it does
1. **Asks about your platform** in two rounds: first what the platform is, then the rest with
   suggested answers you can pick from (roles and panels, devices, stakes, mood, trust in AI, who
   not to forget).
2. **Builds a persona panel role by role** (for example user → manager → admin → super admin),
   12–18 personas, and saves it so you reuse it for every test on that platform.
3. **Asks for the screens and the task:** upload a PDF (a Figma flow board export works best) or
   paste a URL, and say which task to test first.
4. **Runs the test:** each persona walks the tasks in character, an expert check reviews the same
   screens, and every finding is checked against the real screens.
5. **Writes a plain-language report** (HTML, dark and light, plus PDF):
   - one-minute summary
   - 1 Summary by user type · 2 How they felt · 3 Patterns · 4 Where they got stuck (with proof
     screenshots) · 5 What we learned
   - 6 **Low effort, high impact** fixes · 7 Everything by impact and effort
   - four metrics: completion, time on task, errors, satisfaction

## Install
```bash
git clone https://github.com/mahimauiuxdesigner/synthetic-persona-testing ~/.claude/skills/synthetic-persona-testing
```
Then in Claude Code type `/synthetic-persona-testing`, or just ask for a usability test with
synthetic personas.

Needs Python 3 with Pillow, poppler (`pdftoppm`) for PDFs, and Google Chrome for the PDF export.

## Files
| Path | What it is |
|---|---|
| `SKILL.md` | the full workflow |
| `references/intake-questions.md` | the platform questions, with suggested-answer rules |
| `references/persona-recipe.md` | how personas are built (multi-role, optional multitenant) |
| `references/session-protocol.md` | rules for each persona session |
| `references/report-structure.md` | the report, section by section |
| `references/report-data-schema.md` | the data file the report is built from |
| `assets/build_report.py` | builds the HTML report from `report-data.json` |
| `assets/report-template.html` | report styles, light and dark |
| `assets/example-report-data.json` | a full example (fictional product "Shiftly") |
| `assets/example-brief.md` | an example test brief |

Try the builder:
```bash
python3 assets/build_report.py assets/example-report-data.json example-report.html
```

## Honest limits
These are pretend users, not real people. They show where a design is likely to break, not how
often. AI design feedback alone is right about half the time (Duan et al., CHI 2024), so the skill
checks every finding against the screens. Confirm the high-priority findings with 3 to 5 real users.

Made by Mahima Pandey, product designer.
