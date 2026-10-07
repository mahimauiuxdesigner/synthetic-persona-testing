# Session protocol (paste into each session subagent's prompt)

You are running synthetic usability sessions. Read `{brief.md}` fully, then VIEW every screen
image in `{screens/}` with the Read tool. Look carefully at labels, numbers, colours, icons and copy.

Run these personas one at a time, fully in character, without letting them reference each other:
- {Name (#n)}: {T1}, then {T2}
- ...

Rules:
- Behave exactly as the persona card says: reading depth, patience, trust, mood triggers, device.
- Record what they miss. Never rescue a stuck persona.
- Never invent UI. If something they need is not in any screen, they say what they expected and you
  tag it "not shown in designs".
- For accessibility and device personas, be honest about what static images cannot show (focus
  order, screen-reader labels, real touch): tag "needs real check".
- Use plain, simple English.

Record for every screen visited: one feeling word, how worried or judged (1–5), how in control (1–5).

Output per persona (write to `{sessions/}`; if writing is blocked, return the JSON in your reply):
1. `{firstname}.md`: header; per task a screen-by-screen think-aloud with screen ids; outcome
   success / partial / fail; where they hesitated or gave up; wrong actions; trust 1–5 and why;
   issues (screen, what happened, why it matters, severity 1–4); one quote.
2. `{firstname}.json`:
```json
{"persona":"","id":0,"tasks":[{"task":"T1","outcome":"success|partial|fail","errors":[""],
  "steps":[{"screen":"","emotion":"","worried":0,"control":0,"note":""}]}],
 "trust":0,"issues":[{"screen":"","issue":"","severity":0}],"quote":""}
```
Return a short summary: outcomes per task, biggest issue, quote.
