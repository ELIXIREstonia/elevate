#!/usr/bin/env python3
"""Build index-alt.html — implements the supplied mockup layout.

Assets come from logos/ so there is a single source of truth:
  opt-*.svg        partner logos (optimised)
  eu-emblem.svg    EU emblem, built to the official geometry
  partner-map.png  Europe basemap derived from the ELIXIR members map on
                   elixir.ut.ee, recoloured so EE/NL/FI read as the partners
"""
import re, json, base64, math, pathlib

P = pathlib.Path(__file__).parent
L = P / "logos"

# ------------------------------------------------------------------ assets
def _logo(fn, cls, label):
    """Inline a partner SVG. Strip width/height from the ROOT tag only —
    stripping globally collapses CSC's clipPath and the logo disappears."""
    g = (L / fn).read_text()
    m = re.match(r"<svg[^>]*>", g)
    root = re.sub(r'\s(?:width|height)="[^"]*"', "", m.group(0))
    root = root.replace("<svg", f'<svg class="{cls}" role="img" aria-label="{label}"', 1)
    return root + g[m.end():]

UT  = _logo("opt-ut-blue.svg",  "plogo plogo-ut",  "University of Tartu")
HRI = _logo("opt-healthri.svg", "plogo plogo-hri", "Health-RI")
CSC = _logo("opt-csc.svg",      "plogo plogo-csc", "CSC – IT Center for Science")
EU  = (L / "eu-emblem.svg").read_text()
MAP_B64 = (L / "partner-map.b64").read_text().strip()
MAPMETA = json.loads((L / "partner-map.json").read_text())

# ------------------------------------------------------------------ mark
def mark(cls, pillar, spark):
    def sp(cx, cy, r):
        k1, k2 = r * .13, r * .36
        return (f"M{cx} {cy-r}C{cx+k1} {cy-k2},{cx+k2} {cy-k1},{cx+r} {cy}"
                f"C{cx+k2} {cy+k1},{cx+k1} {cy+k2},{cx} {cy+r}"
                f"C{cx-k1} {cy+k2},{cx-k2} {cy+k1},{cx-r} {cy}"
                f"C{cx-k2} {cy-k1},{cx-k1} {cy-k2},{cx} {cy-r}Z")
    return (f'<svg class="{cls}" viewBox="0 0 152 92" role="img" aria-label="ELEVATE DM">'
            f'<g fill="{pillar}"><rect x="10" y="36" width="16" height="34"/>'
            f'<rect x="34" y="22" width="16" height="48"/><rect x="58" y="8" width="16" height="62"/>'
            f'<rect x="2" y="73" width="80" height="5"/><rect x="9" y="81" width="66" height="4"/></g>'
            f'<path d="M92 58 L136 14" stroke="{spark}" stroke-width="2.4" stroke-linecap="round" '
            f'stroke-dasharray="0 7" fill="none"/><g fill="{spark}">'
            f'<path d="{sp(94,56,7)}"/><path d="{sp(114,37,9.5)}"/><path d="{sp(136,13,13)}"/></g></svg>')

# ------------------------------------------------------------------ icons
ICON = {
 "research":  '<circle cx="11" cy="11" r="7"/><path d="M16.5 16.5 21 21"/>',
 "curriculum":'<path d="M2 8 12 3l10 5-10 5L2 8Z"/><path d="M6 10.5V16c0 1.7 2.7 3 6 3s6-1.3 6-3v-5.5"/>',
 "network":   '<circle cx="12" cy="5" r="2.4"/><circle cx="5" cy="18" r="2.4"/><circle cx="19" cy="18" r="2.4"/><path d="M12 7.4 6.5 15.6M12 7.4l5.5 8.2M7.4 18h9.2"/>',
 "support":   '<path d="M3 20h18M5 20V10M9.5 20V10M14.5 20V10M19 20V10M2.5 10 12 4l9.5 6"/>',
 "manage":    '<rect x="4" y="4" width="16" height="16" rx="2"/><path d="M8 9.5h8M8 13h8M8 16.5h5"/>',
 "outreach":  '<path d="M4 9v6h3l6 4V5L7 9H4Z"/><path d="M17.5 8.5a5 5 0 0 1 0 7"/>',
 "partners":  '<circle cx="9" cy="8" r="3"/><path d="M3 19c0-3.3 2.7-5 6-5s6 1.7 6 5"/><circle cx="17" cy="9" r="2.4"/><path d="M15.5 14.2c3 .2 5.5 1.8 5.5 4.8"/>',
 "question":  '<circle cx="12" cy="12" r="9"/><path d="M9.3 9.3a2.8 2.8 0 1 1 3.4 3.3v1.6"/><circle cx="12.4" cy="17.4" r=".9" fill="currentColor" stroke="none"/>',
 "levels":    '<path d="m12 2.6 2 4.6 5 .4-3.8 3.3 1.2 4.9L12 13.2 7.6 15.8l1.2-4.9L5 7.6l5-.4 2-4.6Z"/>',
 "sectors":   '<circle cx="12" cy="12" r="2.6"/><circle cx="5" cy="6" r="2.2"/><circle cx="19" cy="6" r="2.2"/><circle cx="12" cy="21" r="2.2"/><path d="M10.3 10.3 6.6 7.5M13.7 10.3l3.7-2.8M12 14.6V18.8"/>',
 "in":        '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M7.5 10v6M7.5 7.4v.1M11.5 16v-3.4a2.1 2.1 0 0 1 4.2 0V16"/>',
 "x":         '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="m8 8 8 8M16 8l-8 8"/>',
 "mail":      '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m4 7 8 5.5L20 7"/>',
}
def icon(n, cls="ico"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[n]}</svg>')

# ------------------------------------------------------------------ content (verified against Annex 1)
STATS = [
 ("partners", "3 partners",           "Estonia, the Netherlands and Finland"),
 ("question", "3 research questions", "What data management investment actually returns"),
 ("levels",   "3 levels of change",   "Individual skills, university policy, national policy"),
 ("sectors",  "3 sectors connected",  "Academic, public sector and private sector"),
]
WORK = [
 ("manage",     "Project management",        "WP5"),
 ("research",   "Research &amp; evidence",   "WP1"),
 ("curriculum", "Curriculum development",    "WP2"),
 ("network",    "Network building",          "WP3"),
 ("support",    "Institutional support",     "WP4"),
 ("outreach",   "Communication &amp; outreach","WP6"),
]
COUNTRIES = [   # key, country, institution, role
 ("FI", "Finland",         "CSC – IT Center for Science", "Advanced partner"),
 ("EE", "Estonia",         "University of Tartu",         "Coordinator"),
 ("NL", "The Netherlands", "Health-RI",                   "Advanced partner"),
]
PARTNERS = [
 ("EE", "Estonia", UT,  "University of Tartu", "Coordinator",
  "Estonia's leading research university and host of the ELIXIR Estonia node since 2013."),
 ("NL", "The Netherlands", HRI, "Health-RI", "Advanced partner",
  "The Dutch national coordination point for health and life sciences data infrastructure, hosting ELIXIR-NL."),
 ("FI", "Finland", CSC, "CSC — IT Center for Science", "Advanced partner",
  "Finland's national IT centre for research and host of ELIXIR Finland."),
]
NEWS = [
 (False, "News", "20 July 2026", "ELEVATE DM is going ahead",
  "Selected for funding in the 2026 Horizon Europe Twinning call. The project starts on 1 January 2027."),
 (True, "Event", "Early 2027", "Kick-off meeting",
  "Placeholder — replace once the date and venue are fixed."),
 (True, "Training", "2027", "First training round",
  "Placeholder — the programme is designed in WP2 during the opening months."),
]

# ------------------------------------------------------------------ map overlay geometry
# block viewBox is 1000 x 700; the map fills the left MAP_W of it, preserving aspect
MW, MH = MAPMETA["size"]
MAP_W = 700.0
MAP_H = MAP_W * MH / MW
C = MAPMETA["centroids"]
dot = {k: (MAP_W * C[k][0] / 100, MAP_H * C[k][1] / 100) for k in C}
anchor = {"FI": (762, 118), "EE": (762, 300), "NL": (762, 486)}

leaders = []
for k in ("FI", "EE", "NL"):
    (x1, y1), (x2, y2) = dot[k], anchor[k]
    bend = x1 + (x2 - x1) * .45
    leaders.append(f'<path d="M{x1:.1f} {y1:.1f} H{bend:.1f} V{y2:.1f} H{x2-8:.1f}"/>')
dots = "".join(f'<circle cx="{dot[k][0]:.1f}" cy="{dot[k][1]:.1f}" r="9"/>' for k in dot)

labels_html = "".join(
 f'<div class="mlabel" style="left:{anchor[k][0]/1000*100:.2f}%;top:{anchor[k][1]/700*100:.2f}%">'
 f'<b>{country}</b><strong>{inst}</strong><em>{role}</em></div>'
 for k, country, inst, role in COUNTRIES)

# ------------------------------------------------------------------ fragments
stats_html = "".join(f'<div class="stat">{icon(k)}<h3>{t}</h3><p>{d}</p></div>' for k,t,d in STATS)
work_html  = "".join(f'<div class="witem">{icon(k)}<h3>{t}</h3><span>{n}</span></div>' for k,t,n in WORK)
pcards_html = "".join(
 f'<article class="pcard"><div class="plate">{lg}</div><div class="pbody">'
 f'<span class="cc">{cc} — {cn.upper()}</span><h3>{nm}</h3><span class="role">{role}</span>'
 f'<p>{d}</p></div></article>' for cc,cn,lg,nm,role,d in PARTNERS)
news_html = "".join(
 f'<article class="ncard{" pending" if pend else ""}"><div class="nbody">'
 f'<span class="ntag">{tag}</span><span class="ndate">{date}</span><h3>{title}</h3><p>{txt}</p></div>'
 f'<div class="nimg">{"Placeholder" if pend else "Image to be added"}</div></article>'
 for pend,tag,date,title,txt in NEWS)

# ------------------------------------------------------------------ page
html = f"""<title>ELEVATE DM</title>
<style>
:root {{
  --paper:#FFFFFF; --surface:#F9F3ED; --band:#00295E; --band-ink:#F9F3ED;
  --ink:#00295E; --ink-soft:#2A4A76; --muted:#6B7A93; --rule:#E3DACE;
  --accent:#F45801; --accent-ink:#BF4301; --on-accent:#FFFFFF; --card:#FFFFFF;
  --shadow:0 1px 2px rgba(0,41,94,.06),0 10px 30px rgba(0,41,94,.07);
  --r:16px; --r-sm:9px;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace;
}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{
  --paper:#001B3D; --surface:#00234F; --band:#001129; --ink:#F9F3ED; --ink-soft:#DCD3C6;
  --muted:#9EAFC8; --rule:#17427D; --accent:#FA7A31; --accent-ink:#FF9C5C; --on-accent:#2A1000;
  --card:#00295E; --shadow:0 1px 2px rgba(0,0,0,.45),0 10px 30px rgba(0,0,0,.35);
}}}}
:root[data-theme="dark"]{{
  --paper:#001B3D; --surface:#00234F; --band:#001129; --ink:#F9F3ED; --ink-soft:#DCD3C6;
  --muted:#9EAFC8; --rule:#17427D; --accent:#FA7A31; --accent-ink:#FF9C5C; --on-accent:#2A1000;
  --card:#00295E; --shadow:0 1px 2px rgba(0,0,0,.45),0 10px 30px rgba(0,0,0,.35);
}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:16.5px;
  line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}}
.wrap{{width:min(100% - 2.5rem,72rem);margin-inline:auto}}
h1,h2,h3{{margin:0;text-wrap:balance}} p{{margin:0}}
a{{color:var(--accent-ink)}}
a:focus-visible,button:focus-visible{{outline:2px solid var(--accent);outline-offset:3px;border-radius:var(--r-sm)}}
.eyebrow{{font-size:.71rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);margin-bottom:.7rem}}
h2{{font-size:clamp(1.6rem,3.3vw,2.25rem);line-height:1.14;letter-spacing:-.025em;font-weight:750}}
.lede{{color:var(--ink-soft);margin-top:1.1rem}}
.arrow{{display:inline-flex;align-items:center;gap:.45rem;margin-top:1.5rem;font-size:.78rem;font-weight:700;
  letter-spacing:.09em;text-transform:uppercase;text-decoration:none;color:var(--accent-ink)}}
.arrow:hover{{gap:.72rem}}
.draft{{background:var(--accent);color:var(--on-accent);font-family:var(--mono);font-size:.67rem;
  letter-spacing:.1em;text-transform:uppercase;padding:.45rem 0}}
.draft .wrap{{display:flex;justify-content:space-between;flex-wrap:wrap;gap:.6rem}}
.skip{{position:absolute;left:-9999px;background:var(--accent);color:var(--on-accent);padding:.6rem 1rem;z-index:60;border-radius:var(--r-sm)}}
.skip:focus{{left:.75rem;top:.75rem}}

/* header */
.hdr{{position:sticky;top:0;z-index:30;background:var(--paper);border-bottom:1px solid var(--rule)}}
.hdr .wrap{{display:flex;align-items:center;gap:2rem;padding:.8rem 0}}
.brand{{display:flex;align-items:center;gap:.65rem;text-decoration:none;flex:none}}
.brand .bm{{width:42px}}
.brand-name{{font-size:1.45rem;font-weight:700;letter-spacing:-.02em;color:var(--ink);line-height:1}}
.brand-name b{{color:var(--accent)}}
.brand-tag{{font-size:.48rem;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--muted);margin-top:.3rem}}
.mainnav{{margin-left:auto;display:flex;gap:1.5rem;list-style:none;padding:0;margin:0;overflow-x:auto;scrollbar-width:none}}
.mainnav::-webkit-scrollbar{{display:none}}
.mainnav a,.mainnav .soon{{font-size:.87rem;font-weight:600;white-space:nowrap;text-decoration:none;
  color:var(--ink-soft);padding:.3rem 0;border-bottom:2px solid transparent;display:inline-block}}
.mainnav a:hover{{color:var(--accent-ink);border-bottom-color:var(--accent)}}
.mainnav .soon{{color:var(--muted);cursor:default}}
.mainnav .soon::after{{content:"soon";font-family:var(--mono);font-size:.5rem;letter-spacing:.1em;
  text-transform:uppercase;color:var(--accent);vertical-align:super;margin-left:.25rem}}

/* hero — art bleeds to the right edge, as in the mockup */
.hero{{border-bottom:1px solid var(--rule)}}
.hero .wrap{{display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center;padding:4.25rem 0}}
.hero h1{{font-size:clamp(2.2rem,5vw,3.5rem);line-height:1.06;letter-spacing:-.03em;font-weight:750}}
.hero .sub{{font-size:1.05rem;color:var(--ink-soft);max-width:42ch;margin-top:1.2rem}}
.cta{{display:flex;gap:.8rem;flex-wrap:wrap;margin-top:2rem}}
.btn{{display:inline-flex;align-items:center;gap:.5rem;font-size:.78rem;font-weight:700;letter-spacing:.09em;
  text-transform:uppercase;text-decoration:none;padding:.88rem 1.3rem;border-radius:var(--r-sm);border:2px solid transparent}}
.btn-fill{{background:var(--accent);color:var(--on-accent)}} .btn-fill:hover{{background:var(--accent-ink)}}
.btn-out{{border-color:var(--ink);color:var(--ink)}} .btn-out:hover{{border-color:var(--accent);color:var(--accent-ink)}}
.hero-art{{position:relative;margin-right:calc(50% - 50vw);min-height:340px;display:grid;place-items:center;
  border-radius:var(--r) 0 0 var(--r);overflow:hidden;background:var(--surface)}}
.hero-art::before{{content:"";position:absolute;width:150%;aspect-ratio:1;right:-12%;top:-28%;border-radius:50%;
  background:var(--paper);opacity:.55}}
.hero-art .bm{{position:relative;width:min(62%,340px)}}
.hero-art figcaption{{position:absolute;bottom:.65rem;left:1rem;font-family:var(--mono);font-size:.58rem;
  letter-spacing:.09em;text-transform:uppercase;color:var(--muted)}}

/* stats band */
.band{{background:var(--band);color:var(--band-ink)}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(13rem,1fr))}}
.stat{{padding:2rem 1.3rem;text-align:center;display:flex;flex-direction:column;align-items:center;gap:.5rem;
  border-left:1px solid rgba(249,243,237,.18)}}
.stat:first-child{{border-left:0}}
.stat .ico{{width:32px;height:32px;opacity:.9}}
.stat h3{{font-size:.83rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}}
.stat p{{font-size:.86rem;opacity:.85;max-width:22ch}}

/* about + map */
section{{padding:4.25rem 0;scroll-margin-top:4.5rem}}
.split{{display:grid;grid-template-columns:.9fr 1.1fr;gap:3rem;align-items:center}}
.mapblock{{position:relative;aspect-ratio:1000/700}}
.mapblock img{{position:absolute;left:0;top:0;width:{MAP_W/10:.0f}%;height:auto}}
.mapblock .leaders{{position:absolute;inset:0;width:100%;height:100%}}
.leaders path{{fill:none;stroke:var(--accent);stroke-width:2;stroke-dasharray:1 6;stroke-linecap:round}}
.leaders circle{{fill:var(--accent);stroke:var(--paper);stroke-width:3}}
.mlabel{{position:absolute;transform:translateY(-50%);max-width:26%}}
.mlabel b{{display:block;font-size:.64rem;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);font-weight:700}}
.mlabel strong{{display:block;font-size:.92rem;line-height:1.25;margin-top:.15rem}}
.mlabel em{{font-style:normal;font-size:.75rem;color:var(--muted)}}

/* our work — horizontal icon strip */
.work{{background:var(--surface);border-block:1px solid var(--rule)}}
.worksplit{{display:grid;grid-template-columns:.85fr 1.15fr;gap:3rem;align-items:center}}
.wstrip{{display:grid;grid-template-columns:repeat(6,1fr)}}
.witem{{padding:.5rem .7rem;text-align:center;border-left:1px solid var(--rule);display:flex;
  flex-direction:column;align-items:center;gap:.5rem}}
.witem:first-child{{border-left:0}}
.witem .ico{{width:30px;height:30px;color:var(--accent)}}
.witem h3{{font-size:.79rem;font-weight:700;line-height:1.3}}
.witem span{{font-family:var(--mono);font-size:.62rem;color:var(--muted)}}

/* partners */
.pcards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(16rem,1fr));gap:1.15rem;margin-top:2.25rem}}
.pcard{{background:var(--card);border:1px solid var(--rule);border-radius:var(--r);overflow:hidden;
  box-shadow:var(--shadow);display:flex;flex-direction:column}}
.pcard .plate{{background:#FFF;min-height:76px;display:flex;align-items:center;padding:1rem 1.35rem;border-bottom:1px solid var(--rule)}}
.plogo{{display:block;width:auto}} .plogo-ut{{height:21px}} .plogo-hri{{height:25px}} .plogo-csc{{height:40px}}
.pbody{{padding:1.25rem 1.35rem;display:flex;flex-direction:column;gap:.35rem}}
.pcard .cc{{font-family:var(--mono);font-size:.66rem;letter-spacing:.13em;color:var(--accent)}}
.pcard h3{{font-size:1.02rem;font-weight:700}}
.pcard .role{{font-family:var(--mono);font-size:.64rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}}
.pcard p{{font-size:.87rem;color:var(--muted);margin-top:.3rem}}

/* news — text left, image right, scroll-snap row with arrows */
.nhead{{display:flex;justify-content:space-between;align-items:flex-end;gap:1rem;flex-wrap:wrap}}
.nrail{{position:relative;margin-top:2rem}}
.nrow{{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(19rem,1fr);gap:1.15rem;
  overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;padding-bottom:.25rem}}
.nrow::-webkit-scrollbar{{display:none}}
.ncard{{scroll-snap-align:start;background:var(--card);border:1px solid var(--rule);border-radius:var(--r);
  overflow:hidden;box-shadow:var(--shadow);display:grid;grid-template-columns:1fr 38%}}
.nbody{{padding:1.2rem 1.25rem;display:flex;flex-direction:column;gap:.35rem}}
.ntag{{font-family:var(--mono);font-size:.6rem;letter-spacing:.13em;text-transform:uppercase;color:var(--accent)}}
.ndate{{font-family:var(--mono);font-size:.72rem;color:var(--muted)}}
.ncard h3{{font-size:.99rem;font-weight:700;line-height:1.32}}
.ncard p{{font-size:.85rem;color:var(--muted)}}
.nimg{{display:grid;place-items:center;text-align:center;padding:.5rem;border-left:1px solid var(--rule);
  background:repeating-linear-gradient(135deg,var(--surface),var(--surface) 10px,transparent 10px,transparent 20px);
  color:var(--muted);font-family:var(--mono);font-size:.56rem;letter-spacing:.1em;text-transform:uppercase}}
.pending{{opacity:.72}}
.narrow{{position:absolute;top:50%;transform:translateY(-50%);width:38px;height:38px;border-radius:50%;
  border:1px solid var(--rule);background:var(--paper);color:var(--ink);cursor:pointer;display:grid;place-items:center;
  box-shadow:var(--shadow);z-index:2}}
.narrow.prev{{left:-19px}} .narrow.next{{right:-19px}}
.narrow:hover{{border-color:var(--accent);color:var(--accent-ink)}}

.note{{border:1px dashed var(--rule);background:var(--surface);border-radius:var(--r);padding:1.05rem 1.25rem;
  color:var(--muted);font-size:.86rem;margin-top:1.75rem}}
.note strong{{color:var(--ink-soft)}}

/* footer — four columns as in the mockup */
footer{{background:var(--band);color:var(--band-ink);padding:3.25rem 0 1.75rem}}
.fgrid{{display:grid;grid-template-columns:1.35fr .8fr 1.25fr 1fr;gap:2.5rem}}
footer h4{{font-size:.7rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;margin-bottom:.9rem;opacity:.75}}
footer p{{font-size:.86rem;opacity:.85;margin-bottom:.85rem}}
footer ul{{list-style:none;margin:0;padding:0;display:grid;gap:.5rem}}
footer ul a{{color:var(--band-ink);text-decoration:none;font-size:.86rem;opacity:.85}}
footer ul a:hover{{opacity:1;text-decoration:underline}}
.social{{display:flex;gap:.55rem;margin-top:.4rem}}
.social a{{width:34px;height:34px;border-radius:50%;border:1px solid rgba(249,243,237,.35);display:grid;
  place-items:center;color:var(--band-ink)}}
.social .ico{{width:17px;height:17px}}
.social a:hover{{border-color:var(--accent);color:var(--accent)}}
.sub-form{{display:flex;gap:.5rem;flex-wrap:wrap;margin-top:.5rem}}
.sub-form input{{flex:1;min-width:9rem;padding:.6rem .75rem;border-radius:var(--r-sm);border:1px solid rgba(249,243,237,.35);
  background:transparent;color:var(--band-ink);font:inherit;font-size:.85rem}}
.sub-form input::placeholder{{color:var(--band-ink);opacity:.5}}
.sub-form button{{padding:.6rem 1.1rem;border:0;border-radius:var(--r-sm);background:var(--accent);
  color:var(--on-accent);font:inherit;font-size:.72rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase}}
.sub-note{{font-family:var(--mono);font-size:.58rem;letter-spacing:.08em;text-transform:uppercase;opacity:.6;margin-top:.55rem}}
.fbrand{{display:flex;align-items:center;gap:.65rem}}
.fbrand .bm{{width:42px}} .fbrand .brand-name{{color:var(--band-ink)}} .fbrand .brand-tag{{color:var(--band-ink);opacity:.6}}
.eu{{display:flex;gap:1.1rem;align-items:flex-start;border-top:1px solid rgba(249,243,237,.2);margin-top:2.5rem;padding-top:1.6rem}}
.eu-flag{{flex:none;width:78px;height:auto;display:block}}
.eu p{{font-size:.78rem;opacity:.85;margin-bottom:.5rem}}
.fbot{{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;border-top:1px solid rgba(249,243,237,.2);
  margin-top:1.4rem;padding-top:1.15rem;font-size:.76rem;opacity:.7}}
.fbot a{{color:var(--band-ink);text-decoration:none}} .fbot a:hover{{text-decoration:underline}}

@media (max-width:62rem){{
  .hero .wrap,.split,.worksplit{{grid-template-columns:1fr;gap:2.25rem}}
  .hero-art{{order:-1;margin-right:0;border-radius:var(--r);min-height:250px}}
  .wstrip{{grid-template-columns:repeat(3,1fr);row-gap:1.5rem}}
  .witem:nth-child(4){{border-left:0}}
  .fgrid{{grid-template-columns:1fr 1fr}}
  .mapblock{{aspect-ratio:auto}}
  .mapblock img{{position:static;width:100%}}
  .mapblock .leaders{{display:none}}
  .mlabel{{position:static;transform:none;max-width:none;margin-top:1rem;padding-left:.9rem;
    border-left:3px solid var(--accent)}}
}}
@media (max-width:40rem){{
  .wstrip{{grid-template-columns:repeat(2,1fr)}}
  .witem:nth-child(3),.witem:nth-child(5){{border-left:0}}
  .fgrid{{grid-template-columns:1fr}}
  .ncard{{grid-template-columns:1fr}} .nimg{{border-left:0;border-top:1px solid var(--rule);min-height:120px}}
}}
@media (prefers-reduced-motion:no-preference){{html{{scroll-behavior:smooth}}}}
</style>

<a class="skip" href="#about">Skip to content</a>
<div class="draft"><div class="wrap"><span>Draft — alternative layout</span><span>Placeholders marked in dashed boxes</span></div></div>

<header class="hdr">
  <div class="wrap">
    <a class="brand" href="#top">{mark("bm","var(--ink)","var(--accent)")}
      <span><span class="brand-name">elevate <b>dm</b></span>
      <span class="brand-tag" style="display:block">Better data &bull; Better research &bull; Better futures</span></span></a>
    <ul class="mainnav">
      <li><a href="#about">About</a></li><li><a href="#work">Our Work</a></li>
      <li><a href="#partners">Partners</a></li><li><a href="#news">News &amp; Events</a></li>
      <li><span class="soon">Resources</span></li><li><a href="#contact">Contact</a></li>
    </ul>
  </div>
</header>

<main id="top">
  <div class="hero">
    <div class="wrap">
      <div>
        <h1>Elevating data management.<br>Elevating research.</h1>
        <p class="sub">ELEVATE DM builds professionalised, institution-wide research data management capacity at the University of Tartu — embedded in policy, training and everyday practice.</p>
        <div class="cta">
          <a class="btn btn-fill" href="#about">About the project &rarr;</a>
          <a class="btn btn-out" href="#work">Our work &rarr;</a>
        </div>
      </div>
      <figure class="hero-art" style="margin:0 calc(50% - 50vw) 0 0">
        {mark("bm","var(--ink)","var(--accent)")}
        <figcaption>Hero image to be added</figcaption>
      </figure>
    </div>
  </div>

  <div class="band"><div class="wrap"><div class="stats">{stats_html}</div></div></div>

  <section id="about">
    <div class="wrap split">
      <div>
        <p class="eyebrow">About ELEVATE DM</p>
        <h2>Stronger foundations for better science</h2>
        <p class="lede">ELEVATE DM is a Horizon Europe Twinning project that builds research data management capacity at the University of Tartu, working with two of Europe's leading research data infrastructures.</p>
        <p class="lede">Estonia is among the most digitally advanced countries in Europe. Its research data management is not: fewer than ten people support more than 2,200 academic staff, there is no institutional data management policy, and no accepted way to measure what good data management is worth.</p>
        <a class="arrow" href="#work">Learn more about the project &rarr;</a>
      </div>
      <div class="mapblock">
        <img src="data:image/png;base64,{MAP_B64}" alt="Map of Europe with Estonia, the Netherlands and Finland highlighted; other ELIXIR member countries lightly tinted">
        <svg class="leaders" viewBox="0 0 1000 700" aria-hidden="true">{"".join(leaders)}{dots}</svg>
        {labels_html}
      </div>
    </div>
  </section>

  <section class="work" id="work">
    <div class="wrap worksplit">
      <div>
        <p class="eyebrow">Our work</p>
        <h2>Building change together</h2>
        <p class="lede">Our work is structured around six interconnected work packages that enable systemic change in research data management.</p>
        <a class="arrow" href="#partners">Explore our work packages &rarr;</a>
      </div>
      <div class="wstrip">{work_html}</div>
    </div>
  </section>

  <section id="partners">
    <div class="wrap">
      <p class="eyebrow">Partners</p>
      <h2>Three institutions, one network</h2>
      <p class="lede" style="max-width:58ch">All three are ELIXIR nodes, connected long before the project began. The advanced partners bring mature national data ecosystems; Tartu brings the widening-country context in which the models have to work.</p>
      <div class="pcards">{pcards_html}</div>
    </div>
  </section>

  <section id="news" style="background:var(--surface);border-block:1px solid var(--rule)">
    <div class="wrap">
      <div class="nhead">
        <div><p class="eyebrow">News &amp; events</p><h2>Stay informed</h2></div>
        <a class="arrow" href="#news" style="margin:0">View all news &rarr;</a>
      </div>
      <div class="nrail">
        <button class="narrow prev" aria-label="Previous">&#8249;</button>
        <div class="nrow" id="nrow">{news_html}</div>
        <button class="narrow next" aria-label="Next">&#8250;</button>
      </div>
      <div class="note"><strong>Note.</strong> The mockup carried three sample items dated 2025, before the project exists. Only the funding decision is real; the other two are marked as placeholders.</div>
    </div>
  </section>

  <section id="contact">
    <div class="wrap">
      <p class="eyebrow">Contact</p>
      <h2>Get in touch</h2>
      <div class="note"><strong>Placeholder.</strong> Needs one project email address, the coordinator contact, and the ELIXIR Estonia channels already in use. One address survives staff changes; individual inboxes do not.</div>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    <div class="fgrid">
      <div>
        <h4>About ELEVATE DM</h4>
        <p>Building professionalised, institution-wide research data management capacity at the University of Tartu, with Health-RI and CSC.</p>
        <div class="social">
          <a href="#contact" aria-label="LinkedIn">{icon("in")}</a>
          <a href="#contact" aria-label="X">{icon("x")}</a>
          <a href="#contact" aria-label="Email">{icon("mail")}</a>
        </div>
      </div>
      <div>
        <h4>Quick links</h4>
        <ul><li><a href="#about">About</a></li><li><a href="#work">Our work</a></li>
        <li><a href="#partners">Partners</a></li><li><a href="#news">News &amp; events</a></li>
        <li><a href="#contact">Contact</a></li></ul>
      </div>
      <div>
        <h4>Stay updated</h4>
        <p>Subscribe for training announcements and project news.</p>
        <form class="sub-form" onsubmit="return false">
          <input type="email" placeholder="Your email address" aria-label="Your email address" disabled>
          <button type="submit" disabled>Subscribe</button>
        </form>
        <p class="sub-note">Disabled — needs a mailing-list service and a privacy notice</p>
      </div>
      <div>
        <div class="fbrand">{mark("bm","var(--band-ink)","var(--accent)")}
          <span><span class="brand-name">elevate <b>dm</b></span>
          <span class="brand-tag" style="display:block">Better data &bull; Better research &bull; Better futures</span></span></div>
        <ul style="margin-top:1.1rem">
          <li>Jan 2027 – Dec 2029</li><li>&euro;1,379,617.50</li>
          <li>Grant agreement 000000000</li><li>HORIZON-WIDERA-2026-02-WIDENING-01</li>
        </ul>
      </div>
    </div>

    <div class="eu">{EU}
      <div>
        <p><strong>Funded by the European Union.</strong> Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Executive Agency (REA). Neither the European Union nor the granting authority can be held responsible for them.</p>
      </div>
    </div>

    <div class="fbot">
      <span>&copy; 2026 ELEVATE DM</span>
      <span><a href="#contact">Privacy policy</a> &nbsp;|&nbsp; <a href="#contact">Terms of use</a> &mdash; to be added</span>
    </div>
  </div>
</footer>

<script>
(function(){{
  var row=document.getElementById('nrow');
  if(!row) return;
  document.querySelector('.narrow.prev').onclick=function(){{row.scrollBy({{left:-row.clientWidth*.8,behavior:'smooth'}})}};
  document.querySelector('.narrow.next').onclick=function(){{row.scrollBy({{left: row.clientWidth*.8,behavior:'smooth'}})}};
}})();
</script>
"""

(P / "index-alt.html").write_text(html)
print("index-alt.html written:", len(html), "bytes")
