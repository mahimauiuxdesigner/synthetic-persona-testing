#!/usr/bin/env python3
"""Build the synthetic persona usability report from one JSON data file.

Usage:
  python3 build_report.py report-data.json [output.html]

Paths for proof images in the JSON are relative to the JSON file.
Styles come from report-template.html next to this script (dark and light themes).
See ../references/report-data-schema.md for every field.
"""
import base64, html, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
e = html.escape
PRI = {'High': 'high', 'Medium': 'med', 'Low': 'low'}
SENTI = {'positive': 's-pos', 'neutral': 's-neu', 'concerned': 's-con', 'frustrated': 's-fru', 'negative': 's-neg'}
ICON = {
    'people': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.8-3.6 3.4-5.5 6.5-5.5s5.7 1.9 6.5 5.5"/><circle cx="17" cy="9" r="2.5"/><path d="M17 14.5c2.3.2 4 1.8 4.5 4.5"/>',
    'pulse': '<path d="M3 12h4l2-5 4 10 2-5h6"/>',
    'pattern': '<circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="7" r="2.5"/><circle cx="12" cy="17" r="2.5"/><path d="M8.3 7.2l7.4-.2M7.4 8.2l3.4 6.6M16.8 9.3l-3.6 5.6"/>',
    'warn': '<path d="M12 3l9.5 17h-19z"/><path d="M12 10v4.5M12 17.5v.5"/>',
    'bulb': '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
    'bolt': '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
    'grid': '<rect x="3" y="3" width="8" height="8" rx="1.5"/><rect x="13" y="3" width="8" height="8" rx="1.5"/><rect x="3" y="13" width="8" height="8" rx="1.5"/><rect x="13" y="13" width="8" height="8" rx="1.5"/>',
}

EXTRA_CSS = """
<style>
.qw { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 14px; }
.qwc { border: 1px solid var(--rule); border-radius: 14px; padding: 16px 18px; display: flex; flex-direction: column; gap: 8px; background: var(--bg); }
.qwc .top { display: flex; justify-content: space-between; gap: 10px; align-items: baseline; }
.qwc h3 { font-size: 17px; line-height: 1.3; }
.qwc .n { font: 500 13px "IBM Plex Mono", monospace; color: var(--muted); }
.qwc p { font-size: 14.5px; color: var(--muted); }
.qwc p b { color: var(--ink); font-weight: 600; }
.qwc .tags { display: flex; gap: 6px; flex-wrap: wrap; margin-top: auto; }
.qwc .tag { font-size: 12.5px; border-radius: 999px; padding: 2px 10px; background: var(--surface); }
.mx { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.quad { border-radius: 14px; padding: 14px 16px; background: var(--surface); }
.quad.now { background: var(--ink); color: var(--bg); }
.quad h3 { font-size: 16px; display: flex; justify-content: space-between; gap: 8px; margin-bottom: 8px; }
.quad h3 small { font: 400 12.5px "IBM Plex Sans", sans-serif; opacity: .75; }
.quad ul { margin-left: 18px; font-size: 14.5px; }
.quad li + li { margin-top: 4px; }
.metrics4 { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; }
.metrics4 div { border-top: 2px solid var(--ink); padding-top: 10px; }
.metrics4 b { display: block; font: 500 24px "IBM Plex Mono", monospace; }
.metrics4 small { display: block; font-size: 13px; color: var(--muted); font-weight: 600; }
.metrics4 span { font-size: 13.5px; color: var(--muted); }
@media (max-width: 760px) { .mx, .metrics4 { grid-template-columns: 1fr; } }
@media print { .qwc, .quad { break-inside: avoid; } }
</style>
"""


def names(ws):
    return '<div class="names">' + ''.join(f'<span>{e(w)}</span>' for w in ws) + '</div>'


def trust(v):
    return f'<span class="meter"><span class="bar"><i style="width:{float(v)/5*100:.0f}%"></i></span><span class="mono">{float(v):.1f} / 5</span></span>'


def chip(p):
    return f'<span class="chip {PRI[p]}">{e(p)}</span>'


def block(n, icon, title, sub, inner, bid=None):
    bid = bid or f's{n}'
    return f'''
  <section class="block" aria-labelledby="{bid}">
    <div class="bhead"><span class="badge" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICON[icon]}</svg></span><h2 id="{bid}">{e(title)}</h2></div>
    <p class="bsub">{e(sub)}</p>
    {inner}
  </section>'''


def table(head, rows):
    th = ''.join(f'<th style="width:{w}">{e(h)}</th>' if w else f'<th>{e(h)}</th>' for h, w in head)
    return f'<div class="tw"><table><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div>'


def img_b64(path, base):
    p = path if os.path.isabs(path) else os.path.join(base, path)
    ext = os.path.splitext(p)[1].lower().lstrip('.')
    mime = 'jpeg' if ext in ('jpg', 'jpeg') else ext
    return f'data:image/{mime};base64,' + base64.b64encode(open(p, 'rb').read()).decode()


def build(d, base):
    tpl = open(os.path.join(HERE, 'report-template.html')).read()
    head = tpl[:tpl.index('</head>')]
    head = head[:head.index('<title>')] + f'<title>{e(d["short_title"])}</title>' + head[head.index('</title>') + 8:]
    who = d.get('people_word', 'users')
    Who = who[:1].upper() + who[1:]

    # header and one-minute box
    nums = ''.join(f'<div><b>{e(n["value"])}</b><span>{e(n["label"])}</span></div>' for n in d['headline_numbers'])
    fix = ''.join(f'<li>{e(x)}</li>' for x in d['fix_first'])
    top = f'''<header class="wrap">
  <div class="topbar">
    <p class="meta">{e(d["meta"])}</p>
    <button class="toggle" id="themeToggle" type="button">Dark theme</button>
  </div>
  <h1>{e(d["title"])}</h1>
  <p class="lead">{e(d["lead"])}</p>
  <div class="minute">
    <div><h3>The main finding</h3><p>{e(d["main_finding"])}</p><div class="nums">{nums}</div></div>
    <div><h3>Fix first</h3><ol>{fix}</ol></div>
  </div>
</header>
<main class="wrap">'''

    out = [top]
    # 1 summary
    rows = ''.join(f'<tr><td class="first">{e(g["type"])}</td><td>{names(g["people"])}</td><td>{e(g["did"])}</td><td>{e(g["saw"])}</td>'
                   f'<td class="done"><b>{e(g["done"])}</b><span>{e(g.get("done_note",""))}</span></td><td>{trust(g["trust"])}</td></tr>' for g in d['summary'])
    key = ''.join(f'<div><b>{e(k["name"])}</b> <span>{e(k["about"])}</span></div>' for k in d.get('cast', []))
    inner = table([('User type', '16%'), (Who, '13%'), ('What they did', '21%'), ('What we saw', '27%'), ('Tasks fully done', '11%'), ('Trust', '')], rows)
    if key:
        inner += f'<details class="key"><summary>Who the {e(who)} are</summary><div class="keygrid">{key}</div></details>'
    out.append(block(1, 'people', '1. Summary by user type', f'How each type of {who[:-1] if who.endswith("s") else who} used it, and how far they got.', inner))
    # 2 feelings
    rows = ''.join(f'<tr><td><span class="senti {SENTI[f["tone"]]}">{e(f["feeling"])}</span></td><td>{e(f["what"])}</td><td>{names(f["people"])}</td><td class="signal"><b>{e(f["line"])}</b></td></tr>' for f in d['feelings'])
    out.append(block(2, 'pulse', f'2. How {who} felt', 'From the words they used on each screen.',
                     table([('Feeling', '15%'), ('What happened', '35%'), (Who, '20%'), ('In one line', '')], rows)))
    # 3 patterns
    rows = ''.join(f'<tr><td class="first">{e(p["pattern"])}</td><td>{names(p["people"])}</td><td>{e(p["saw"])}</td><td>{e(p["design"])}</td></tr>' for p in d['patterns'])
    out.append(block(3, 'pattern', '3. Patterns', 'The same problems came up for different people. Each points to one thing to design.',
                     table([('Pattern', '18%'), (Who, '18%'), ('What we saw', '30%'), ('What to design', '')], rows)))
    # 4 stuck + proof
    has_img = {s['letter'] for s in d['stuck'] if s.get('proof')}
    rows = ''.join(f'<tr><td class="first">' + (f'<a class="letter" href="#proof-{s["letter"].lower()}">{e(s["letter"])}.</a>' if s['letter'] in has_img else f'<span class="mono">{e(s["letter"])}.</span>')
                   + f' {e(s["problem"])}</td><td>{names(s["people"])}</td><td>{e(s["did"])}</td><td>{e(s["change"])}</td><td>{chip(s["impact"])}</td></tr>' for s in d['stuck'])
    figs = ''.join(f'''<figure id="proof-{s["letter"].lower()}" class="wide">
          <h3 style="font-size:16px;margin-bottom:8px"><span class="mono">{e(s["letter"])}.</span> {e(s["problem"])}<a class="back" href="#s4">Back to table</a></h3>
          <div class="shot"><img src="{img_b64(s["proof"], base)}" alt="{e(s["problem"])}, with the problem marked"></div>
          <figcaption>{e(s.get("caption", ""))}</figcaption>
        </figure>''' for s in d['stuck'] if s.get('proof'))
    inner = table([('Problem', '22%'), (Who, '16%'), ('What they did', '20%'), ('What to change', '30%'), ('Impact', '')], rows)
    if figs:
        inner += f'<div class="proof"><h3>Proof from the designs</h3><p class="muted" style="font-size:15px">The orange boxes mark the exact problem.</p><div class="proofgrid">{figs}</div></div>'
    out.append(block(4, 'warn', '4. Where they got stuck', 'Where they got stuck or gave up. Click a letter to see the screenshot that proves it.', inner))
    # 5 learned
    rows = ''.join(f'<tr><td class="rank">{i}</td><td class="first">{e(l["learned"])}</td><td>{names(l["people"])}</td><td>{e(l["todo"])}</td><td>{chip(l["priority"])}</td></tr>' for i, l in enumerate(d['learned'], 1))
    out.append(block(5, 'bulb', '5. What we learned, and priority', 'In order. Only three are High, so the team knows where to start.',
                     table([('#', '5%'), ('What we learned', '28%'), (Who, '18%'), ('What to do', '36%'), ('Priority', '')], rows)))
    # 6 quick wins
    cards = ''.join(f'''<div class="qwc"><div class="top"><h3>{e(q["fix"])}</h3><span class="n">{i}</span></div>
      <p><b>Why it matters:</b> {e(q["impact"])}</p><p><b>Why it's quick:</b> {e(q["effort"])}</p>
      <div class="tags"><span class="tag">{e(q.get("fixes","")) or "Fixes a High problem"}</span><span class="tag">{e(", ".join(q["people"]))}</span></div></div>''' for i, q in enumerate(d['quick_wins'], 1))
    out.append(block(6, 'bolt', '6. Low effort, high impact', 'Small changes that fix big problems. Start here: most are wording, styling or showing data we already have.',
                     f'<div class="qw">{cards}</div>', 's6'))
    # 7 impact vs effort
    Q = [('Do now', 'now', 'High impact, low effort'), ('Plan next', '', 'High impact, high effort'), ('Fill in', '', 'Low impact, low effort'), ('Later', '', 'Low impact, high effort')]
    quads = ''.join(f'<div class="quad {c}"><h3>{q}<small>{sub}</small></h3><ul>' + ''.join(f'<li>{e(x)}</li>' for x in d['impact_effort'].get(q, [])) + '</ul></div>' for q, c, sub in Q)
    out.append(block(7, 'grid', '7. Everything by impact and effort', 'Every fix in one view. Effort is an estimate, to confirm with the developers.',
                     f'<div class="mx">{quads}</div>', 's7'))
    # metrics + caution + folded
    m = d['metrics']
    met = ''.join(f'<div><small>{e(k)}</small><b>{e(m[k]["value"])}</b><span>{e(m[k]["note"])}</span></div>' for k in ('Completion', 'Time on task', 'Errors', 'Satisfaction'))
    caution = ''.join(f'<li>{e(x)}</li>' for x in d['before_acting'])
    tasks = ''.join(f'<li>{e(t["task"])} ({e(t["result"])})</li>' for t in d['tasks'])
    out.append(f'''
  <section class="block">
    <h2 style="margin-bottom:14px">How we measured it</h2>
    <div class="metrics4">{met}</div>
  </section>
  <section class="block">
    <div class="caution read">
      <h3>Before acting on this</h3>
      <p style="margin-top:6px">These {e(who)} were pretend users built to act like real ones. They show where the design is likely to break, not how often. Check the High items with 3 to 5 real {e(who)} first.</p>
      <ul>{caution}</ul>
    </div>
    <div style="margin-top:24px">
      <details class="more"><summary>How this test was done</summary><p>{e(d["method"])} Every finding was checked against the real screens, because AI-generated design feedback alone is right only about half the time (Duan and others, CHI 2024).</p></details>
      <details class="more"><summary>Tasks tested</summary><ul>{tasks}</ul></details>
    </div>
  </section>
</main>
<footer><div class="wrap">Detailed files in this folder: <span class="mono">sessions/</span>, <span class="mono">findings-expert.md</span>, <span class="mono">brief.md</span>.</div></footer>''')

    script = tpl[tpl.index('<script>'):tpl.rindex('</script>') + 9]
    return head + EXTRA_CSS + '</head>\n<body>\n' + '\n'.join(out) + '\n' + script + '\n</body>\n</html>\n'


if __name__ == '__main__':
    src = sys.argv[1]
    d = json.load(open(src))
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(src)), d.get('file_name', 'usability-report.html'))
    open(out, 'w').write(build(d, os.path.dirname(os.path.abspath(src))))
    print('wrote', out)
