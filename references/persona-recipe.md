# Persona recipe

## Multi-role platforms (role hierarchy)
Most platforms have several roles, each with its own panel and permissions, for example
user → manager → admin → super admin. Build the panel role by role:
- **Every role gets its own group of personas** (at least 3 for main roles, 2 for small ones),
  each group spread across mood, tech comfort, trust and accessibility.
- Each card starts with `Role: {role} · reports to {role} · manages {role or nobody}`.
- Add **hand-off pairs**: two personas in connected roles (a manager who assigns practice, and the
  user who receives it; an admin who removes a manager, and the manager's team).

Watch for role-specific problems in every run:
- the same item shown differently to different roles (labels, numbers, names do not match)
- permissions: buttons a role sees but cannot use, or cannot find
- hand-offs between roles: who is told, what the other role sees afterwards
- people who hold two roles (a manager who also sells)
- admin actions that change what lower roles see (delete, reassign, settings)

## Multitenant platforms (optional)
If the platform is multitenant, build the panel in two layers:
1. **Tenant profiles (3–5):** fictional organisations that differ in what matters: size, industry,
   plan or tier, settings switched on, region and language, how mature their setup is (new vs
   long-time customer). Give each a short card: name, size, plan, settings, what is unusual about it.
2. **Personas, each tied to a tenant:** spread the personas across the tenant profiles so every
   tenant has at least one end user and one admin. Add platform-level personas (super admin,
   vendor support) who work across tenants, and one person who belongs to two organisations if
   that happens in real life.

Each card then starts with `Tenant: {tenant name, size, plan}` or `Level: platform (all tenants)`.

Watch for multitenant-specific problems in every run:
- which organisation am I in, and is it obvious (switching, branding, headers)
- features that differ by plan or setting (hidden vs disabled vs upsell)
- empty or default states for a brand-new tenant vs a busy, long-time one
- limits and billing messages (seats, minutes, tokens) per tenant
- data isolation cues: could anyone think they see another organisation's data
- cross-tenant roles: super admin acting inside a tenant, impersonation, audit trail

## Panel size and coverage
12–18 personas per platform. Cover every user type first, then make sure the panel spans:

| Dimension | Values to spread across the panel |
|---|---|
| Age | at least two bands, plus one older user if the platform has them |
| Tech comfort | 1–5, with at least one 2 and one 5 |
| Familiarity | first-time, occasional, power user (incl. of a competitor) |
| Device | the main device, plus phone or tablet if anyone uses one |
| Mood | eager, calm, anxious, frustrated, hostile or apathetic, impatient |
| Trust in the system or AI | over-trusts, balanced, doubtful, hostile |
| Standing | new with no data, average, top performer, senior |
| Moment | fresh, rushed, tired, unhurried |
| Language | every language mix the users really have |
| Accessibility | at least one: colour blind, low vision, keyboard-only, or motor |
| Role | every role in the hierarchy, main roles with at least 3 personas |
| Tenant (if multitenant) | every tenant profile; small and large; new and long-time; basic and top plan |

No two personas share the same combination of role, mood and trust.
Base traits on realistic behaviour, never stereotypes about age or ability.

## Persona card (platform-specific)

```
### {n}. {Name}, {role}, {one-line situation}
Tenant: {tenant name, size, plan}   (or: Level: platform, all tenants)
{age}, Tech {1–5}, {First-time | Occasional | Power user}, {device and setting}
- **Mood:** {usual mood}. **Trigger:** {what on this platform sets them off}.
  **Shift:** {mood → mood; what they do then}. **What settles them:** {what would calm them}.
- **Their data:** {what they would have in the product: counts, ranks, items, history}
- **Arrives via:** {how they usually get into the platform}
- **Uses:** {the areas they actually use}
- **Reads the numbers as:** {how they understand or misread the platform's key numbers or labels}
- **Likely to break at:** {a type of problem, not a specific screen}
- **Thinks aloud:** "{a line in their own voice}"
```

## After the cards
1. **Coverage table:** Name | Role | Tenant (if any) | Age | Tech | Familiarity | Device | Mood | Trust.
2. **Filter table:** Mood | Feedback stance (growth-seeking, threat-sensitive, dismissive) |
   Trust | Driven by | Standing | Moment | Language | Device.
3. **Same person, two moments:** two or three personas written in a calm and a stressed state.
4. **Product tensions to watch:** 3–6 places where the platform's design could work against
   its users (from the intake answers).
5. **Assumptions:** list every trait that came from an assumption, not from the user.

## Picking personas for a run
6–11 per run. Always include: one rushed, one doubtful, one first-time, one accessibility
persona, and every role that uses the screens. Give each one 1–2 tasks.
Multi-role: if the screens belong to one role, test that role; if they hand off between roles,
include a persona from each side.
Multitenant: include personas from at least two different tenants (one small or new, one large or
long-time), and a platform-level persona if the screens touch cross-tenant features.
