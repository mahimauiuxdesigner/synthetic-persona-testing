# Intake questions (platform-level)

Ask in **two rounds**. Each question feeds one or more persona traits. Nothing here is about a
single task or module.

## Round 1: ask only question 1
Ask question 1 on its own, in one short message. The user answers in their own words.

## Round 2: questions 2 to 11, with suggested answers
From the round 1 answer, predict the most likely answers for this kind of platform and offer them
as options, so the user mostly picks instead of typing.

How to build the options:
- Read what the platform is, its industry and who it serves, and use everything already known
  (memory, earlier projects, screens if shared).
- For each question give **3–4 specific options for this platform**, not generic ones
  (for a sales coaching tool: "Sales rep", "Sales manager", "Org admin", "Super admin";
  not "User", "Admin").
- Mark the option you think is most likely with "(likely)".
- Allow several picks where answers are not exclusive (roles, devices, moods, languages,
  accessibility). Always allow "Other" for their own words.
- Per-role questions (4 to 8): ask them per role in one compact block, each role with its own options.

How to ask:
- Use the AskUserQuestion tool, up to 4 questions per call, in this order:
  call 1: questions 2, 3, 9, 10 (panels and roles, who not to forget, real-user evidence)
  call 2: questions 4–8 for the main role (device, stakes, tech comfort, mood; trust if AI)
  call 3+: the same for each other role; question 11 last, only if the platform could be multitenant
- If the tool is not available, send one message with lettered options per question
  (a, b, c, d, e = other) so they can reply "2: a, c · 3: b".
- Keep option labels short (1–5 words) with a one-line description.

## The questions

> Round 1 message: "I'll build a reusable panel of pretend users for your platform. First, in a
> line or two: what is the platform, what does it help people do, and who uses it day to day?"
>
> Round 2: suggested options for each remaining question; skip anything and I'll mark it assumed.

## Part A. The platform

1. **What is the platform, and what does it help people do?**
   One or two lines. Who pays for it, and who uses it day to day?
   → product context, what "success" means

2. **Is it a multi-role, multi-panel platform?**
   Does each type of user get their own panel or view (for example a User panel, a Manager panel,
   an Admin panel, a Super admin panel)? List every panel.
   → whether to build the panel role by role

3. **For each role: what is it called, roughly how many people, and how do the roles connect?**
   - who reports to whom (user → manager → admin → super admin)
   - what each role can see and do that the others cannot
   - what one role does that another role then sees or receives (a manager assigns, a user gets it;
     an admin deletes, a team gets reassigned)
   - can one person hold two roles (a manager who also sells)?
   → one persona group per role, hand-off pairs, permission checks

## Part B. The people in each role (answer per role)

4. **Where and how do they use it?**
   Desk or on the move, laptop, phone or tablet, how often, how much time, interrupted or not.
   → device, setting, time pressure

5. **What's at stake for them?**
   Pay, targets, reputation, customers, data, compliance, someone above them watching.
   → stakes, mood triggers, fears

6. **How comfortable are they with technology, and how familiar with this kind of product?**
   From "never used anything like it" to "power users of a competitor" (name it).
   → tech comfort 1–5, familiarity

7. **How do they usually feel when they open it?**
   Rushed, worried, sceptical, eager, bored, under pressure, tired at month-end.
   → mood, what sets them off, what calms them

8. **Does the platform score, decide or suggest things for them (AI or automation)? How much do
   they trust it?**
   → trust: over-trusts, balanced, doubtful, hostile

## Part C. Coverage and evidence

9. **Who must we not forget?**
   Age range, languages (for example Hindi and English), accessibility needs (low vision, colour
   blind, keyboard only), new joiners, very senior people, phone-only users.
   → edge-case personas

10. **What do you already know from real users?**
    Complaints, support tickets, analytics, interview notes, or "nothing yet".
    → grounding; anything here outranks assumptions

11. **Optional: is it multitenant?** Do many separate organisations use the same platform, each with
    its own data? If yes, how do they differ: size, industry, plan, settings, region.
    → tenant profiles

## After the answers
- Restate the platform in two lines, then list the roles and panels as a small hierarchy:
  `User → Manager → Admin → Super admin`, with the hand-offs you heard.
- Mark every gap as **assumed**.
- Build the panel role by role (see persona-recipe.md) and show it for approval.

## Example of round 2 options (a fictional AI call coaching platform)
- **Q2 Panels** (multi-select): Sales rep panel (likely) · Manager panel (likely) · Org admin panel ·
  Super admin panel
- **Q3 Hand-offs** (multi-select): Manager assigns practice to reps (likely) · Admin moves teams
  between managers · Rep disputes an AI flag, manager reviews · Super admin manages organisations
- **Q4 Rep device** (multi-select): Office laptop between calls (likely) · Phone at events · Tablet
- **Q5 Rep stakes:** Monthly targets and incentive (likely) · Leaderboard rank · Compliance flags ·
  Manager reviews
- **Q7 Rep mood:** Rushed between calls (likely) · Anxious about being judged · Doubtful of AI scores ·
  Eager to improve
- **Q8 Trust in AI:** Mixed: new reps over-trust, seniors doubt it (likely) · Mostly trust · Mostly doubt
- **Q9 Don't forget** (multi-select): Hindi and English calls (likely) · New joiners · Colour blind or
  low vision · Phone-only field reps
- **Q10 Evidence:** Nothing yet (likely) · Support tickets · Manager feedback · Analytics
