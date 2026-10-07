# Report structure (same every time)

Plain, simple language. Short sentences. One idea per table cell. No jargon in the main text;
screen codes only in brackets or folded sections.

## Top
- Title: "{Module or Platform}: synthetic usability report"
- One-minute box: the main finding (2 sentences), two numbers (tasks fully done, trust),
  and "Fix first" with exactly 3 items.

## The five tables
| # | Section | Columns |
|---|---|---|
| 1 | Summary by user type | User type, Users (name chips), What they did, What we saw, Tasks fully done ("1 of 4" + "2 couldn't"), Trust (bar + x/5) |
| 2 | How they felt | Feeling (coloured dot + word: Relieved, Unsure, Worried, Frustrated, Scared/Upset), What happened, Users, In one line (a quote) |
| 3 | Patterns | Pattern, Users, What we saw, What to design |
| 4 | Where they got stuck | Letter + Problem (links to proof), Users, What they did, What to change, Impact (High/Medium/Low with shape, not colour alone) |
| 5 | What we learned | #, What we learned, Users, What to do, Priority (only 3 High) |

Under table 4: "Proof from the designs", one annotated screenshot per lettered problem
(orange boxes with short labels), each with a caption and "Back to table".

## Section 6: Low effort, high impact
3–6 cards right after table 5. Each card: the fix, why it matters (persona evidence), why it's
quick, which problem it fixes, who it helped. Only changes that are both: they fix a High or
Medium problem (or the worst moment), and they are wording, styling, existing data, a label, a
count or a default. See the rules in report-data-schema.md.

## Section 7: Everything by impact and effort
Four groups: Do now, Plan next, Fill in, Later. Effort is an estimate, to confirm with developers.

## The four metrics (in "How we measured it", and on the deck)
- **Completion:** X of N tasks fully done (partly, not at all)
- **Time on task:** "Not measured" on static screens; measure on the demo branch
- **Errors:** count of wrong actions across all tasks, with 2–3 examples
- **Satisfaction:** trust x/5; peak worried or judged score and where. SUS and NPS need real users.

## Impact versus effort (details for section 7)
Four groups: Do now (big impact, small effort), Plan next (big impact, big effort), Fill in
(small impact, small effort), Later (small impact, big effort). Each item: evidence from personas,
who it affected, why the effort guess. Label: "Effort is my estimate, to confirm with the dev team".

## Bottom
- "Before acting on this": pretend users, not real ones; check the High items with 3–5 real users;
  list mock-data fixes and missing screens to design before real testing.
- Folded: How we measured it, How this test was done (cite Duan et al. CHI 2024 for verifying AI
  feedback), Tasks the users tried (with "x of y fully done").

## Output
- Build with `assets/build_report.py report-data.json`; no slides unless asked.
- `{module}-usability-report.html`: standalone, dark and light, works on a phone
- PDF via Chrome print, checked page by page (render each page and look; fix overflow before delivery)
