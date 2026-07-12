/* GFM Live Review dashboard renderer.
 *
 * SECURITY: every value that originates from a paper (titles, spans, datasets,
 * proposed tags, …) is untrusted. This file NEVER assigns to innerHTML. All
 * text reaches the DOM through textContent / createTextNode, so an injected
 * `<img onerror=…>` in a span renders as literal characters, not markup.
 */
"use strict";

const DATA = JSON.parse(document.getElementById("gfm-data").textContent);
let excludeSelf = false;

/* ---- tiny DOM helpers (textContent only) ---- */
function el(tag, opts = {}, children = []) {
  const n = document.createElement(tag);
  if (opts.class) n.className = opts.class;
  if (opts.text !== undefined) n.textContent = opts.text;
  if (opts.title) n.title = opts.title;
  if (opts.attrs) for (const [k, v] of Object.entries(opts.attrs)) n.setAttribute(k, v);
  if (opts.onclick) n.addEventListener("click", opts.onclick);
  for (const c of children) if (c) n.appendChild(c);
  return n;
}
function txt(s) { return document.createTextNode(s === null || s === undefined ? "" : String(s)); }

function currentView() {
  return excludeSelf ? DATA.views.no_self_eval : DATA.views.all;
}

const LABEL_ORDER = { consensus: 0, contested: 1, thin: 2, gap: 3 };

/* ---- link helpers ---- */
function paperLink(claim) {
  if (!claim.link) return txt(claim.paper_title || claim.paper_key);
  return el("a", { text: claim.paper_title || claim.paper_key,
                   attrs: { href: claim.link, target: "_blank", rel: "noopener noreferrer" } });
}

function fmtNum(x) {
  if (x === null || x === undefined) return "—";
  return (Math.round(x * 1000) / 1000).toString();
}

/* ---- claim table (used inside the modal) ---- */
function claimTable(claims) {
  const head = el("tr", {}, ["Paper", "Model", "vs baseline", "Metric", "Value",
    "Baseline", "Dataset", "Labels", "Dir", "Loc"].map(h => el("th", { text: h })));
  const rows = claims.map(c => {
    const cells = [];
    cells.push(el("td", {}, [paperLink(c), c.self_evaluation ? el("span", { class: "badge self", text: "self" }) : null]));
    cells.push(el("td", { text: c.model }));
    cells.push(el("td", { text: c.baseline || "—" }));
    cells.push(el("td", { text: c.metric }));
    cells.push(el("td", { text: fmtNum(c.value) }));
    cells.push(el("td", { text: fmtNum(c.baseline_value) }));
    cells.push(el("td", { text: c.dataset }));
    cells.push(el("td", { text: c.label_ratio === null ? "—" : c.label_ratio }));
    cells.push(el("td", {}, [el("span", { class: "dir dir-" + c.direction, text: c.direction })]));
    cells.push(el("td", { text: c.locator }));
    const tr = el("tr", {}, cells);
    const spanRow = el("tr", { class: "span-row" }, [
      el("td", { attrs: { colspan: "10" } }, [
        el("span", { class: "quote-label", text: "quote: " }),
        el("span", { class: "quote", text: c.span })  // textContent -> literal
      ])
    ]);
    return [tr, spanRow];
  }).flat();
  return el("table", { class: "claims" }, [el("thead", {}, [head]), el("tbody", {}, rows)]);
}

/* ---- modal ---- */
function openModal(title, node) {
  document.getElementById("modalTitle").textContent = title;
  const body = document.getElementById("modalBody");
  body.textContent = "";
  body.appendChild(node);
  document.getElementById("modal").classList.remove("hidden");
}
function closeModal() { document.getElementById("modal").classList.add("hidden"); }

/* ---- label chip ---- */
function labelChip(label, extra) {
  const t = extra ? `${label} · ${extra}` : label;
  return el("span", { class: "chip chip-" + label, text: t });
}

/* =====================  VIEWS  ===================== */

function renderMatrix(root) {
  const m = currentView().matrix;
  root.appendChild(el("p", { class: "lede", text:
    "Model × task. Cell colour = consensus across papers (numbers are never pooled across datasets). Click a cell for the underlying claims." }));
  if (!m.tasks.length) { root.appendChild(el("p", { text: "No claims yet." })); return; }
  const wrap = el("div", { class: "scroll" });
  const table = el("table", { class: "matrix" });
  const header = el("tr", {}, [el("th", { text: "" })].concat(
    m.tasks.map(t => el("th", { class: "rot", text: t }))));
  const body = [header];
  for (const model of m.models) {
    const cells = [el("th", { class: "rowhead", text: model })];
    for (const task of m.tasks) {
      const cell = m.cells[model + "\t" + task];
      if (!cell) { cells.push(el("td", { class: "cell empty" })); continue; }
      const td = el("td", { class: "cell chip-" + cell.label,
        title: `${cell.label} — ${cell.n_papers} paper(s), ${cell.n_claims} claim(s)`,
        onclick: () => openModal(`${model} — ${task}`, claimTable(cell.claims)) },
        [txt(cell.n_papers)]);
      cells.push(td);
    }
    body.push(el("tr", {}, cells));
  }
  table.appendChild(el("tbody", {}, body));
  wrap.appendChild(table);
  root.appendChild(wrap);
}

function renderContested(root) {
  root.appendChild(el("p", { class: "lede", text:
    "Where papers measuring the same dataset disagree on direction — the most valuable page." }));
  const groups = currentView().groups.filter(g => g.label === "contested");
  if (!groups.length) { root.appendChild(el("p", { text: "No contested groups at current thresholds." })); return; }
  for (const g of groups) {
    const card = el("div", { class: "gcard" });
    card.appendChild(el("div", { class: "gcard-head" }, [
      el("strong", { text: `${g.task} · ${g.dataset}` }),
      labelChip("contested", `${g.n_papers} papers, ${Math.round(g.agreement*100)}% agree`)
    ]));
    card.appendChild(el("div", { class: "gcard-sub", text:
      `${g.model} vs ${g.baseline || "—"} · ${g.metric} · ${g.label_regime}` }));
    card.appendChild(claimTable(g.claims));
    root.appendChild(card);
  }
}

function renderChallenges(root) {
  root.appendChild(el("p", { class: "lede", text:
    "Open challenges by evidence volume, and how often each limitation is raised over time." }));
  const lim = DATA.limitations;
  const tags = Object.keys(lim.totals).sort((a, b) => lim.totals[b] - lim.totals[a]);
  if (!tags.length) { root.appendChild(el("p", { text: "No limitations recorded yet." })); return; }
  const table = el("table", { class: "board" }, [
    el("thead", {}, [el("tr", {}, [
      el("th", { text: "Limitation" }), el("th", { text: "Papers" }), el("th", { text: "Trend" })])]),
    el("tbody", {}, tags.map(tag => {
      const series = lim.series[tag] || {};
      const months = Object.keys(series).sort();
      const spark = months.map(mm => `${mm}:${series[mm]}`).join("  ");
      return el("tr", {}, [
        el("td", { text: tag }),
        el("td", { text: lim.totals[tag] }),
        el("td", { class: "spark", text: spark || "—" })
      ]);
    }))
  ]);
  root.appendChild(table);
}

function renderAxes(root) {
  root.appendChild(el("p", { class: "lede", text:
    "Research-goal rubric G1–G12. Explicit gap rows mark axes nobody has evidence on yet." }));
  const axes = currentView().axes;
  for (const a of axes) {
    const row = el("div", { class: "axis-row" });
    const head = el("div", { class: "axis-head" }, [
      el("span", { class: "axis-name", text: a.axis }),
      labelChip(a.label, a.n_papers ? `${a.n_papers} papers` : "no evidence")
    ]);
    if (a.claims.length) {
      head.style.cursor = "pointer";
      head.addEventListener("click", () => openModal(a.axis, claimTable(a.claims)));
    }
    row.appendChild(head);
    root.appendChild(row);
  }
}

function renderRegistry(root) {
  const r = DATA.registry;
  const bar = el("div", { class: "stats" });
  bar.appendChild(el("span", { class: "stat", text: `${r.n_papers} papers` }));
  for (const [k, v] of Object.entries(r.doi_status_counts)) {
    bar.appendChild(el("span", { class: "stat", text: `${k}: ${v}` }));
  }
  bar.appendChild(el("span", { class: "stat warn", text: `quarantined: ${r.quarantine_count}` }));
  root.appendChild(bar);

  const table = el("table", { class: "registry" }, [
    el("thead", {}, [el("tr", {}, ["Title", "Date", "Venue", "DOI", "Status", "Claims"]
      .map(h => el("th", { text: h })))]),
    el("tbody", {}, r.papers.map(p => el("tr", {}, [
      el("td", {}, [p.link ? el("a", { text: p.title, attrs: { href: p.link, target: "_blank", rel: "noopener noreferrer" } }) : txt(p.title),
        p.self_evaluation ? el("span", { class: "badge self", text: "self" }) : null]),
      el("td", { text: p.date }),
      el("td", { text: p.venue || "—" }),
      el("td", { text: p.doi || "—" }),
      el("td", {}, [el("span", { class: "doi doi-" + p.doi_status, text: p.doi_status })]),
      el("td", { text: p.n_claims })
    ])))
  ]);
  root.appendChild(el("div", { class: "scroll" }, [table]));
}

const TABS = [
  { id: "matrix", label: "Model × Task", render: renderMatrix },
  { id: "contested", label: "Contested", render: renderContested },
  { id: "challenges", label: "Open Challenges", render: renderChallenges },
  { id: "axes", label: "Axes G1–G12", render: renderAxes },
  { id: "registry", label: "Registry", render: renderRegistry },
];
let activeTab = "matrix";

function renderTabs() {
  const nav = document.getElementById("tabs");
  nav.textContent = "";
  for (const t of TABS) {
    nav.appendChild(el("button", {
      class: "tab" + (t.id === activeTab ? " active" : ""),
      text: t.label,
      onclick: () => { activeTab = t.id; render(); }
    }));
  }
}

function renderSubtitle() {
  const sub = document.getElementById("subtitle");
  sub.textContent = `${DATA.meta.n_papers} papers · corpus through ${DATA.corpus_through || "—"} · ` +
    `consensus = ≥${DATA.meta.consensus_rule.min_papers} papers, ` +
    `≥${Math.round(DATA.meta.consensus_rule.agreement*100)}% agreeing` +
    (excludeSelf ? " · self-evaluations excluded" : "");
}

function render() {
  renderTabs();
  renderSubtitle();
  const view = document.getElementById("view");
  view.textContent = "";
  const tab = TABS.find(t => t.id === activeTab);
  tab.render(view);
}

document.getElementById("excludeSelf").addEventListener("change", (e) => {
  excludeSelf = e.target.checked;
  render();
});
document.getElementById("modalClose").addEventListener("click", closeModal);
document.getElementById("modal").addEventListener("click", (e) => {
  if (e.target.id === "modal") closeModal();
});
document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeModal(); });

render();
