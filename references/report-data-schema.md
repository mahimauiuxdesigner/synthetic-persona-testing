# report-data.json

One file per test. `assets/build_report.py` turns it into the HTML report.
Full working example: `assets/example-report-data.json` (fictional Shiftly example, Manager deletion).
Image paths are relative to the JSON file.

| Field | Type | What it is |
|---|---|---|
| `file_name` | text | output file, e.g. `manager-deletion-usability-report.html` |
| `short_title` | text | browser tab title, 2–4 words |
| `meta` | text | "{Platform} usability test, {area}: {flow}, {date}" |
| `title` | text | "{Flow}: synthetic usability report" |
| `lead` | text | one sentence: who tried what |
| `people_word` | text | plural word for the testers: "admins", "reps", "users" |
| `main_finding` | text | two sentences, plain language |
| `headline_numbers` | list of `{value, label}` | usually tasks fully done, and trust |
| `fix_first` | list of text | exactly 3 |
| `cast` | list of `{name, about}` | who each persona is, one line |
| `summary` | list of `{type, people[], did, saw, done, done_note, trust}` | table 1, one row per user type or role |
| `feelings` | list of `{feeling, tone, what, people[], line}` | table 2; tone = positive, neutral, concerned, frustrated, negative |
| `patterns` | list of `{pattern, people[], saw, design}` | table 3 |
| `stuck` | list of `{letter, problem, people[], did, change, impact, proof?, caption?}` | table 4; impact = High, Medium, Low; `proof` = annotated image path |
| `learned` | list of `{learned, people[], todo, priority}` | table 5; only 3 High |
| `quick_wins` | list of `{fix, impact, effort, fixes, people[]}` | section 6, low effort and high impact, 3–6 cards; `fixes` like "Fixes A (High)" |
| `impact_effort` | `{ "Do now": [], "Plan next": [], "Fill in": [], "Later": [] }` | section 7 |
| `metrics` | `{Completion, Time on task, Errors, Satisfaction}` each `{value, note}` | "How we measured it" |
| `before_acting` | list of text | mock-data fixes, missing screens, decisions needed |
| `method` | text | one paragraph: who, how many tasks, screens, expert check |
| `tasks` | list of `{task, result}` | e.g. `{"task": "Remove a manager who left", "result": "2 of 5 fully done"}` |

## Rules for quick wins
A quick win must be **both**:
- **high impact:** it fixes a High or Medium problem, or a problem many personas hit, or the moment
  people felt most worried;
- **low effort:** wording, styling, showing data that already exists, removing a step, a label, a
  count, a default. No new backend, no new flow.
Say why it matters (persona evidence) and why it is quick (in plain words). Everything in
`quick_wins` must also appear under "Do now" in `impact_effort`.
