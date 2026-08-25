# ELEVATE-DM website — structure and content plan

Companion to the two draft layouts — `index.html` (editorial, serif) and `index-alt.html` (marketing, built from the supplied mockup). Annex 1 commits the site at **MS1, M3**, alongside the visual identity.

## Naming question — decide before anything is published

The identity PNG says **FAIR FUTURES — Data · People · Policy — "Better data. Better science. Together."** The grant is **ELEVATE-DM**. The draft page uses ELEVATE-DM as the name and borrows the identity's palette, strapline and pillar mark. Three options:

1. **ELEVATE-DM is the name; Fair Futures is retired.** Simplest. The grant agreement, all reporting, and every publication acknowledgement use ELEVATE-DM, so a second name is overhead.
2. **ELEVATE-DM is the project; Fair Futures is the public-facing programme brand.** Workable, but requires saying so on every page and in the EU acknowledgement, or reviewers will ask what Fair Futures is and why it is spending their money.
3. **Fair Futures becomes the name of a specific strand** — the community of practice (WP3), say, or the training programme. This is the most defensible use of a second brand: it names a thing that outlives the grant.

Recommendation: **option 1 or 3.** A project brand that differs from the grant acronym causes real friction at reporting time, and the EU emblem statement has to sit next to the funded project's name.

## Site map

| Page | Priority | Purpose | Status |
|:--|:--|:--|:--|
| **Home** | M3 | What, why, who, how much. Everything a first-time visitor needs without clicking. | Drafted, with sticky nav |
| **About** | M3 | The gap analysis at length, the five gaps, the Twinning logic, links to the partners. | Expand from home §01 |
| **Work packages** | M3 | One page, six anchored sections; tasks, deliverables, leads. | Markup preserved below |
| **Consortium** | M3 | Three partner profiles plus the people — name, role, ORCID, institution. | Cards drafted |
| **Training** | M6 | The public draw. Upcoming courses, registration, past materials. Most-visited page on any RDM project site. | Not started |
| **Outputs** | rolling | Deliverables, publications, datasets, software. Every item with a DOI. | Placeholder |
| **News** | rolling | Kick-off, then real items only. | Placeholder |
| **Contact** | M3 | One project address, not individual inboxes. | Placeholder |

Keep it to these. Widening project sites usually fail by having twelve pages, eight of them empty at M30.

## What the home page contains now

0. Sticky nav — About · Work packages · Training · Consortium · Outputs · News · Contact. Items that exist resolve to on-page anchors; Work packages and Training are marked "soon" because they are planned as separate pages
1. Masthead — acronym, pillar mark, strapline, tagline, key facts (duration, EU contribution, GA number, coordinator, partners)
2. **Latest** — news, in a cream band directly under the masthead so the newest thing is the first thing after the identity
3. **Why this project** — the gap, stated in plain terms
4. **Objectives** — SO1–SO7, one line each
5. **Consortium** — three partner cards
6. **Outputs** — placeholder, open-licensing commitment stated
7. **Contact** — placeholder
8. Footer — EU emblem, funding statement, disclaimer, GA number

Work packages have been lifted off the home page onto their own page — markup preserved at the end of this file.

## Mandatory elements (Article 17, HE MGA)

Already in the footer, do not remove or reword:

> Funded by the European Union. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Executive Agency (REA). Neither the European Union nor the granting authority can be held responsible for them.

Plus the EU emblem and the grant agreement number. The page currently shows **000000000** as a placeholder: 101341112 is the *proposal* number, and the GA number is only fixed at signature. Replace it before launch — and note it appears twice, in the facts strip and in the footer.

The emblem in the footer is now the real one, built to the official geometry (see below) — not a placeholder. The emblem's colours (`#003399` / `#FFCC00`) are prescribed and must not be restyled to the project palette, nor may its corners be rounded to match the cards.

## Design tokens (from the supplied identity)

| Token | Light | Dark | Use |
|:--|:--|:--|:--|
| White | `#FFFFFF` | — | Page ground |
| Navy | `#00295E` | ground `#001B3D`, surface `#00295E` | Primary ink; dark-theme ground |
| Orange | `#F45801` | `#FA7A31` | Single accent — section dots, sparks, links, the wordmark hyphen |
| Cream | `#F9F3ED` | text `#F9F3ED` | Card and band surfaces; dark-theme text |

Typography: Georgia for display and headings, system sans for body, monospace for codes, months and figures. All system-available, so nothing falls back silently. Orange is deliberately confined to structural markers and the mark — the identity uses it as a progression signal, not as a fill. Section markers are the identity's orange dot rather than numerals, since the sections are not a sequence.

Dark theme mirrors the identity's own navy panel treatment rather than being invented.

## Before launch

- [ ] Settle the naming question above
- [ ] Add the project start date once the GA is signed, and convert M1–M36 to real dates
- [ ] Decide the domain — subdomain of ut.ee, of elixir.ee, or standalone
- [ ] **Confirm logo permission with each partner.** The logos are embedded from each organisation's own site (see below), but consortium membership is not the same as brand approval — ask each partner's communications contact to confirm the version and any placement rules
- [ ] Accessibility pass: WCAG 2.1 AA. Orange `#F45801` on white is fine for large text and decoration but not for body copy — links already use the darker `#BF4301`
- [ ] Privacy notice and cookie policy if any analytics are added — the project is about data governance, so the site should model it
- [ ] Remove the orange "Draft — not for publication" banner

---

## Work packages — markup lifted off the home page

Removed from the home page (it made the first screen a work-plan document rather than an invitation). Reuse verbatim on the Work packages page; it needs no changes beyond dropping the outer `<section>` if the page has its own heading.

### CSS

```css
  /* ---------- work packages ---------- */
  .wp-scroll { overflow-x: auto; }
  table { border-collapse: collapse; width: 100%; min-width: 40rem; }
  caption { text-align: left; color: var(--muted); font-size: .9rem; padding-bottom: .9rem; }
  th, td { text-align: left; padding: .85rem .9rem; border-bottom: 1px solid var(--rule); vertical-align: top; }
  thead th {
    font-family: var(--mono); font-size: .68rem; letter-spacing: .12em; text-transform: uppercase;
    color: var(--muted); font-weight: 500; border-bottom: 1px solid var(--ink-soft);
  }
  tbody th { font-family: var(--mono); font-size: .85rem; color: var(--accent); font-weight: 500; width: 4rem; }
  td.span { font-family: var(--mono); font-size: .85rem; font-variant-numeric: tabular-nums; color: var(--muted); white-space: nowrap; }
  td.lead { font-size: .9rem; color: var(--ink-soft); white-space: nowrap; }
```

### Markup

```html
  <section>
    <div class="wrap">
      <div class="col">
        <div class="sec-head"><span class="sec-dot" aria-hidden="true">&bull;</span><h2>Work packages</h2></div>
        <p>Six work packages over three years. Research evidence drives training design and policy arguments; institutional change sustains the training; the community carries it outward.</p>
      </div>
      <div class="wp-scroll">
        <table>
          <caption>Months are counted from the project start date.</caption>
          <thead>
            <tr><th scope="col">WP</th><th scope="col">Title</th><th scope="col">Lead</th><th scope="col">Months</th></tr>
          </thead>
          <tbody>
            <tr><th scope="row">WP1</th><td>Research Component — measuring and demonstrating data value</td><td class="lead">UTARTU</td><td class="span">M1–M36</td></tr>
            <tr><th scope="row">WP2</th><td>Training, Curriculum and Professional Development</td><td class="lead">UTARTU · CSC</td><td class="span">M1–M36</td></tr>
            <tr><th scope="row">WP3</th><td>Communities of Practice and Ecosystem Building</td><td class="lead">Health-RI</td><td class="span">M4–M36</td></tr>
            <tr><th scope="row">WP4</th><td>Institutional Support Systems and Interoperable Workflows</td><td class="lead">UTARTU</td><td class="span">M6–M33</td></tr>
            <tr><th scope="row">WP5</th><td>Project Management and Strategic Coordination</td><td class="lead">UTARTU</td><td class="span">M1–M36</td></tr>
            <tr><th scope="row">WP6</th><td>Communication, Dissemination and Sustainability Planning</td><td class="lead">UTARTU</td><td class="span">M1–M36</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
```

---

## Partner logos

Embedded as inline SVG, taken from each organisation's own website — not from third-party logo aggregators, which routinely carry outdated or unofficial versions.

| Partner | Source | Notes |
|:--|:--|:--|
| University of Tartu | `ut.ee/themes/utheme/assets/img/UT_website_logo_blue_eng.svg` | English version. A white variant (`..._white_eng.svg`) is saved in `logos/` if a dark lockup is ever needed |
| Health-RI | `health-ri.nl/themes/custom/health_ri/assets/images/logo.svg` | Full-colour. A white footer variant is saved in `logos/` |
| CSC — IT Center for Science | `csc.fi/app/uploads/2023/09/CSC_logo_no_tagline.svg` | No-tagline version; only a colour variant exists |

**Why they sit on a white band.** CSC publishes only a colour logo, whose teal and magenta would be near-invisible on the dark navy ground — and recolouring another organisation's logo is not ours to do. A white band across the top of each card keeps every logo in its approved colours in both themes. It runs full card width rather than floating as an inset tile, so it reads as part of the card rather than a rectangle dropped on top.

**Optical sizing.** Heights are normalised by appearance, not by number: 22px for the wide UT wordmark, 26px for Health-RI, 40px for the near-square CSC mark. Matching raw heights would make CSC look tiny.

**One gotcha, recorded so it is not repeated.** The CSC SVG clips its artwork to a `<clipPath>` rect. Any optimisation that strips `width`/`height` attributes globally will collapse that rect to zero and the logo silently disappears — strip them only from the root `<svg>` element.

---

## Navigation — how it is meant to evolve

The home page carries the whole story on one scroll, which is right at M3 when there is little to say. The nav is built so that growing out of a single page is a link change, not a rebuild.

| Nav item | Today | At launch |
|:--|:--|:--|
| About | `#about` on this page | own page; expand from the "Why this project" section |
| Work packages | marked *soon* | own page; markup preserved at the end of this file |
| Training | marked *soon* | own page; the most-visited page on any RDM project site |
| Consortium | `#consortium` | own page, with people, roles and ORCIDs |
| Outputs | `#outputs` | own page, one row per deliverable with DOIs |
| News | `#latest` | index page; the home band keeps the three most recent items |
| Contact | `#contact` | stays a section, or folds into the footer |

The two *soon* items are deliberately not links: a nav item that goes nowhere is worse than one that admits it is not ready. Replace the `<span class="soon">` with an `<a href="...">` when each page exists — the styling then applies automatically.

**Also fixed:** the home page briefly had two news sections, the new "Latest" band at the top and the original placeholder at the bottom. Only the top one remains.

---

## Notes on two layout decisions

**Objectives are unnumbered.** SO1–SO7 is proposal numbering; it means something to an evaluator reading against the work plan and nothing to a researcher deciding whether to attend a course. Dropping the labels and setting the seven in a three-column grid cut the section to about a third of its former height.

**They are not boxed.** Seven items never fill a column grid evenly — three columns leaves one item alone on the last row, and any boxed treatment turns that into a conspicuous gap. Two attempts confirmed it: a gap-background grid painted the unused cells as solid blocks, and switching to cell borders just drew a lone rectangle with a hole beside it. Removing the boxes altogether solves it — each item gets a short orange rule above its title, and a short last row reads as the list simply ending. Adding an eighth objective would not change the treatment, which is the point.

**The news item now names a start date.** Copy is written for a reader rather than a reviewer, and the facts strip reads `Jan 2027 – Dec 2029` instead of `36 months`, which says the same thing while answering the question people actually have. Both need revisiting if the start date moves during grant agreement preparation — the date appears in the news item and in the facts strip.

**Corner radius.** Two tokens: `--r: 14px` for cards and panels (partner cards, facts strip, funding block, placeholder boxes), `--r-sm: 8px` for small elements and focus rings. The EU emblem placeholder keeps a tighter 5px, since the official emblem is a square-cornered flag and should not read as a rounded card.

Cards that contain edge-to-edge children — the partner cards with their white logo band, and the facts strip built from 1px gaps — carry `overflow: hidden` so those children are clipped to the curve rather than poking through the corner.

---

## The EU emblem

Built from the official geometric description in the Interinstitutional Style Guide, Annex A1, rather than copied from a third-party file:

- fly is 1.5 × the hoist → 900 × 600
- twelve stars, centres on an invisible circle of radius **hoist ÷ 3**
- each star's five points on an invisible circle of radius **hoist ÷ 18**
- all stars upright, top point vertical, positioned as the hours of a clock
- Pantone Reflex Blue field `#003399`, Pantone Yellow stars `#FFCC00`

**Why not just use the common file.** The Wikimedia "Flag of Europe" SVG — the one most search results lead to — draws its stars at a radius of hoist ÷ 16, about 12% larger than the specification's hoist ÷ 18. It is everywhere, but it is not to spec. Ours is generated from the written geometry, so it is correct by construction.

**The white surround is deliberate.** The specification's own remedy for placing the emblem on a coloured background is a white border of 1/25 the rectangle's height. That is what lets the same file sit correctly on the cream funding block in the light theme and on navy in the dark theme, where an unbordered blue flag would nearly disappear.

Do not restyle the colours, round the corners, or place the emblem on a busy background.

---

## Two layouts to choose between

| | `index.html` | `index-alt.html` |
|:--|:--|:--|
| Origin | Built from the brand PNG | Implements the supplied full-page mockup layout |
| Type | Georgia display over system sans | System sans throughout, heavy display weights |
| Structure | One scroll, sticky section nav | Mockup layout: bleeding hero, navy stats band, about + annotated map, horizontal work strip, partner cards, news carousel, four-column footer |
| Feel | Institutional, quiet | Outward-facing, more confident |
| Build | Hand-edited HTML | Generated by `alt.build.py`, so content lives in Python lists |

`alt.build.py` regenerates `index-alt.html` and pulls the partner logos and EU emblem from `logos/`, so there is one source of truth for them. Edit the `STATS`, `WPS`, `PARTNERS` and `OBJECTIVES` lists and re-run it.

### What was corrected from the mockup

The mockup is a visual design, not a content source. These were fixed:

| Mockup | Corrected to |
|:--|:--|
| News: "Kick-off meeting in Tartu, 12 May 2025", "DATAREX Meeting, Ghent, 22–24 Sept 2025", "Nordic Computational Biology Conference, Tallinn, 23–24 Oct 2025" | Removed. All three predate a project starting 1 January 2027. One real item (the funding decision) plus two clearly-marked placeholders |
| "© 2025 ELEVATE DM Project" | © 2026 |
| "Netherlands Health-RI" | Health-RI |
| Six generic work-package names | The six real WP titles from Annex 1, with their real month spans |
| "3 SECTORS CONNECTED — Public sector, private sector, citizen science" | Academic, public sector and private sector — matching the cross-sector engagement actually described in Annex 1 |
| Europe map with three highlighted countries | Implemented. Derived from the ELIXIR members map on elixir.ut.ee — see below |
| Newsletter sign-up form | Present but disabled, labelled "needs a mailing-list service and a privacy notice" — the layout is there without pretending it works |
| Photography in hero and news cards | Marked "image to be added" |

### Third tagline

The mockup's lockup reads **BETTER DATA • BETTER RESEARCH • BETTER FUTURES**. The identity PNG gave two others: **DATA • PEOPLE • POLICY** and **"Better data. Better science. Together."** That is three taglines for one project. `index.html` uses the first PNG's, `index-alt.html` uses the mockup's. Pick one before launch — this needs deciding alongside the naming question at the top of this file.

The mockup does settle the naming question in one respect: it says **elevate dm**, not Fair Futures.

---

## The partner map

Built from `ELIXIR-members-map_2026-01_White-01.png` on elixir.ut.ee — our own asset, which avoids the licensing problem. The obvious alternatives on Wikimedia are CC BY-SA 3.0, whose attribution and share-alike terms are awkward on an official project site. (One public-domain option exists, `Europe_blank_map.svg`, if a fallback is ever needed.)

Processing, reproducible via `alt.build.py` and the steps recorded in git:

1. Identify the three partner countries as connected components of the ELIXIR orange, then verify each visually before use — the seed coordinates were wrong on the first attempt and Netherlands landed in the North Sea.
2. Recolour: sea to transparent, non-member land to a slate tint at 22% alpha, ELIXIR member states at 36%, and Estonia, the Netherlands and Finland to solid brand orange.
3. Crop to Europe, resize to 1000px wide, embed as a data URI.

Transparency is what makes one file work in both themes: on white the land reads pale grey, on navy it reads a lighter navy, and the orange holds against both. The faint tint on other ELIXIR members is deliberate and truthful — all three partners are ELIXIR nodes, and the map shows that network without claiming those countries are in the project.

Country centroids are computed during the build and written to `logos/partner-map.json`, so the dotted leader lines and labels stay aligned if the map is ever re-cropped.
