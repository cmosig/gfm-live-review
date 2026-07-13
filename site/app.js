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

/* ---- display names (fallbacks keep future keys working) ---- */
const MODEL_NAMES = {
  alphaearth: "AlphaEarth", tessera: "TESSERA", prithvi: "Prithvi", clay: "Clay",
  presto: "Presto", satclip: "SatCLIP", geoclip: "GeoCLIP", satmae: "SatMAE",
  scalemae: "Scale-MAE", dofa: "DOFA", croma: "CROMA", galileo: "Galileo",
  task_specific: "task-specific model",
};
function modelName(key) {
  if (key === null || key === undefined) return "—";
  return MODEL_NAMES[key] || key;
}
function taskName(key) { return String(key).replace(/_/g, " "); }

const AXIS_INFO = {
  G1_label_rich_parity: ["Label-rich parity", "Do foundation models match task-specific models when training labels are plentiful?"],
  G2_label_scarce_efficiency: ["Label efficiency", "Do foundation models win when only few labels are available?"],
  G3_spatial_transfer: ["Spatial transfer", "Do results hold in regions the downstream model never saw?"],
  G4_temporal_transfer: ["Temporal transfer", "Do results hold across time — different years or seasons?"],
  G5_cost: ["Cost", "Compute, inference and storage cost compared to alternatives."],
  G6_compactness: ["Compactness", "How small can the embeddings be before performance drops?"],
  G7_interpretability: ["Interpretability", "Can we understand what the embedding dimensions encode?"],
  G8_uncertainty: ["Uncertainty", "Are predictions calibrated? Is uncertainty quantified at all?"],
  G9_ecological_fine_scale: ["Fine-scale ecology", "Forests, mixed pixels, and fine-grained ecological structure."],
  G10_human_semantics: ["Human semantics", "Socioeconomic signals: wealth, slums, population, urban function."],
  G11_complementarity: ["Complementarity", "Do different foundation models improve when combined?"],
  G12_openness: ["Openness", "Open weights, open data, reproducibility."],
};
function axisTitle(axis) {
  const info = AXIS_INFO[axis];
  return info ? info[0] : axis;
}

const DIR_GLYPH = { better: "▲", worse: "▼", parity: "≈" };
const DIR_WORD = {
  better: "foundation model beats the baseline",
  worse: "baseline beats the foundation model",
  parity: "effectively equal",
};

const LIMITATION_INFO = {
  temporal_transfer: "Performance degrades across time (other years/seasons)",
  spatial_transfer: "Performance degrades in unseen regions",
  interpretability: "Embeddings are hard to interpret",
  uncertainty: "No or poor uncertainty quantification",
  mixed_pixels: "Coarse pixels mix multiple land covers",
  human_semantics: "Weak on socioeconomic / human signals",
  time_sensitivity: "Sensitive to acquisition timing",
  benchmark_narrowness: "Evaluated on too few / narrow benchmarks",
  compute_cost: "High compute or storage cost",
  data_bias: "Training or evaluation data is biased",
};

const DOI_STATUS_INFO = {
  verified: "DOI resolved and confirmed (journal DOIs are title-matched against Crossref; arXiv DOIs are derived 1:1 from the arXiv id)",
  no_doi_found: "No DOI exists in any metadata source for this paper",
  unresolved: "DOI found but the lookup failed — retried on the next run",
  mismatch: "DOI resolves to a different title — flagged for review",
};

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
function fmtRatio(x) {
  if (x === null || x === undefined) return "—";
  return (Math.round(x * 1000) / 10) + "%";
}

/* ---- claim table (used inside the modal) ---- */
function claimTable(claims) {
  const heads = [
    ["Paper", "The paper this claim comes from"],
    ["Model", "The foundation model being evaluated"],
    ["Baseline", "What it is compared against"],
    ["Metric", ""],
    ["Value", "The foundation model's score"],
    ["Baseline value", "The baseline's score"],
    ["Dataset", "Results are never pooled across datasets"],
    ["Labels used", "Fraction of training labels used downstream"],
    ["Direction", "better = foundation model wins, worse = baseline wins"],
    ["Where", "Location in the paper"],
  ];
  const head = el("tr", {}, heads.map(([h, t]) => el("th", { text: h, title: t })));
  const rows = claims.map(c => {
    const cells = [];
    cells.push(el("td", {}, [paperLink(c), c.self_evaluation
      ? el("span", { class: "badge self", text: "self-eval",
                     title: "Authors helped create the model they evaluate" }) : null]));
    cells.push(el("td", { text: modelName(c.model) }));
    cells.push(el("td", { text: modelName(c.baseline) }));
    cells.push(el("td", { text: c.metric }));
    cells.push(el("td", { text: fmtNum(c.value) }));
    cells.push(el("td", { text: fmtNum(c.baseline_value) }));
    cells.push(el("td", { text: c.dataset }));
    cells.push(el("td", { text: fmtRatio(c.label_ratio) }));
    cells.push(el("td", {}, [el("span", { class: "dir dir-" + c.direction,
      text: (DIR_GLYPH[c.direction] || "") + " " + c.direction, title: DIR_WORD[c.direction] || "" })]));
    cells.push(el("td", { text: c.locator }));
    const tr = el("tr", {}, cells);
    const spanRow = el("tr", { class: "span-row" }, [
      el("td", { attrs: { colspan: "10" } }, [
        el("span", { class: "quote-label", text: "verbatim quote: " }),
        el("span", { class: "quote", text: "“" + c.span + "”" })  // textContent -> literal
      ])
    ]);
    return [tr, spanRow];
  }).flat();
  return el("div", { class: "scroll" }, [
    el("table", { class: "claims" }, [el("thead", {}, [head]), el("tbody", {}, rows)])]);
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

/* ---- shared bits ---- */
function labelChip(label, extra) {
  const t = extra ? `${label} · ${extra}` : label;
  const titles = {
    consensus: "At least 3 papers and ≥80% agree vs a task-specific model",
    contested: "At least 3 papers, but they disagree vs a task-specific model",
    thin: "Only 1–2 papers vs a task-specific model so far",
    gap: "No paper has produced evidence here yet",
    nobaseline: "Papers exist, but none compares against a task-specific model yet",
  };
  return el("span", { class: "chip chip-" + label, text: t, title: titles[label] || "" });
}

function directionLegend() {
  const items = [
    ["sw-better", "▲", "better — the foundation model beats the task-specific model"],
    ["sw-worse", "▼", "worse — the task-specific model wins"],
    ["sw-parity", "≈", "parity — effectively equal"],
    ["sw-mixed", "±", "mixed — papers disagree (contested)"],
    ["sw-none", "·", "no task-specific comparison yet (only model-vs-model results)"],
  ];
  const legend = el("div", { class: "legend" }, [
    el("span", { class: "lg-title", text: "Direction — foundation model vs task-specific / index:" }),
    ...items.map(([cls, glyph, label]) => el("span", { class: "lg-item" }, [
      el("span", { class: "lg-swatch " + cls, text: glyph }),
      txt(label),
    ])),
    el("span", { class: "lg-item" }, [
      el("span", { class: "lg-swatch sw-ring", text: "" }),
      txt("ring = consensus (≥3 papers, ≥80% agree); no ring = 1–2 papers"),
    ]),
  ]);
  return legend;
}

function verdictDir(v) {
  if (!v.n_papers) return { cls: "none", glyph: "·", word: "no task-specific comparison" };
  if (v.label === "contested") return { cls: "mixed", glyph: "±", word: "papers disagree" };
  const d = v.direction || "parity";
  return { cls: d, glyph: DIR_GLYPH[d] || "", word: DIR_WORD[d] || "" };
}

/* =====================  VIEWS  ===================== */

function renderVerdicts(root) {
  root.appendChild(el("p", { class: "lede", text:
    "The headline question: do geospatial foundation models beat the task-specific alternative — a bespoke " +
    "supervised model or a classical index like NDVI — that a practitioner would otherwise use? Each row is " +
    "one task, pooling every paper that ran that comparison (we count which way each paper landed, never " +
    "averaging incomparable metrics). Contested tasks come first. Click a row for the evidence and quotes." }));
  root.appendChild(directionLegend());
  const verdicts = currentView().task_verdicts;
  if (!verdicts.length) {
    root.appendChild(el("p", { class: "empty-note", text:
      "No foundation-model-vs-task-specific comparisons extracted yet." }));
    return;
  }
  for (const v of verdicts) {
    const dl = verdictDir(v);
    const card = el("div", { class: "vcard",
      title: "Click for the underlying results and verbatim quotes",
      onclick: () => openModal(`${taskName(v.task)} — foundation models vs task-specific`, claimTable(v.claims)) });

    card.appendChild(el("div", { class: "vcard-head" }, [
      el("div", { class: "vcard-title" }, [
        el("span", { class: "vdir dir-cell-" + dl.cls, text: dl.glyph }),
        el("span", { class: "vtask", text: taskName(v.task) }),
      ]),
      labelChip(v.label, `${v.n_papers} paper${v.n_papers === 1 ? "" : "s"}`),
    ]));

    const nD = v.datasets.length, nM = v.n_models;
    card.appendChild(el("div", { class: "vcard-sub", text:
      `${dl.word} · ${nM} model${nM === 1 ? "" : "s"} · ${nD} dataset${nD === 1 ? "" : "s"}` +
      (v.agreement !== null && v.n_papers >= 3 ? ` · ${Math.round(v.agreement * 100)}% of papers agree` : "") }));

    // Per-model breakdown, flagged when models disagree.
    const bd = el("div", { class: "vmodels" });
    if (v.models_differ) bd.appendChild(el("span", { class: "vdiff", text: "differs by model:" }));
    for (const m of v.models) {
      const md = verdictDir(m);
      bd.appendChild(el("span", { class: "vmodel",
        title: `${modelName(m.model)}: ${md.word} — ${m.n_papers} paper(s)` }, [
        el("span", { class: "vdir-sm dir-cell-" + md.cls, text: md.glyph }),
        el("span", { text: modelName(m.model) }),
        el("span", { class: "vmodel-n", text: m.n_papers }),
      ]));
    }
    card.appendChild(bd);
    root.appendChild(card);
  }
}

function renderBenchmarks(root) {
  root.appendChild(el("p", { class: "lede", text:
    "The same results grouped by the exact benchmark they were measured on. Holding the dataset fixed is the " +
    "only way a disagreement between two papers is a real disagreement rather than an artefact of different " +
    "data — so these groups are the apples-to-apples cut. Benchmarks that more than one paper has run come " +
    "first; those are the only ones where a cross-paper comparison is possible at all. Click any row for the " +
    "underlying results and verbatim quotes." }));
  root.appendChild(directionLegend());

  const benches = currentView().benchmarks || [];
  if (!benches.length) {
    root.appendChild(el("p", { class: "empty-note", text: "No benchmark results extracted yet." }));
    return;
  }

  const shared = benches.filter(b => b.n_papers > 1);
  const single = benches.filter(b => b.n_papers <= 1);

  root.appendChild(el("p", { class: "bm-stat", text:
    `${benches.length} distinct benchmarks · ${shared.length} evaluated by more than one paper` }));

  const openBench = (b) => openModal(
    `${b.name} — every extracted result on this benchmark`, claimTable(b.claims));

  const card = (b) => {
    const dl = verdictDir(b.verdict);
    const c = el("div", { class: "vcard",
      title: "Click for the underlying results and verbatim quotes",
      onclick: () => openBench(b) });
    c.appendChild(el("div", { class: "vcard-head" }, [
      el("div", { class: "vcard-title" }, [
        el("span", { class: "vdir dir-cell-" + dl.cls, text: dl.glyph }),
        el("span", { class: "vtask", text: b.name }),
      ]),
      labelChip(b.verdict.label, `${b.n_papers} paper${b.n_papers === 1 ? "" : "s"}`),
    ]));
    c.appendChild(el("div", { class: "vcard-sub", text:
      `${dl.word} · ${b.n_claims} claim${b.n_claims === 1 ? "" : "s"} · ` +
      `${b.models.length} model${b.models.length === 1 ? "" : "s"} · ` +
      b.tasks.map(taskName).join(", ") }));

    const bd = el("div", { class: "vmodels" });
    for (const m of b.models) {
      bd.appendChild(el("span", { class: "vmodel" }, [el("span", { text: modelName(m) })]));
    }
    c.appendChild(bd);

    // The exact strings the papers used. Variants are splits/sensors of the same
    // benchmark, folded together for grouping but never rewritten.
    if (b.variants.length > 1) {
      c.appendChild(el("div", { class: "bm-variants",
        title: "The exact dataset strings the papers used, folded into this benchmark",
        text: "variants: " + b.variants.join(" · ") }));
    }
    return c;
  };

  for (const b of shared) root.appendChild(card(b));

  if (single.length) {
    const det = el("details", { class: "bm-tail" });
    det.appendChild(el("summary", { text:
      `${single.length} benchmark${single.length === 1 ? "" : "s"} evaluated by a single paper ` +
      `(no cross-paper comparison possible yet)` }));
    const rows = single.map(b => {
      const dl = verdictDir(b.verdict);
      return el("tr", { class: "clickable", onclick: () => openBench(b) }, [
        el("td", {}, [el("span", { class: "dir dir-" + (dl.cls === "mixed" || dl.cls === "none" ? "parity" : dl.cls), text: dl.glyph })]),
        el("td", { text: b.name }),
        el("td", { text: b.tasks.map(taskName).join(", ") }),
        el("td", { text: b.models.map(modelName).join(", ") }),
        el("td", { text: b.n_claims }),
      ]);
    });
    const table = el("table", { class: "board" }, [
      el("thead", {}, [el("tr", {}, [
        el("th", { text: "" }), el("th", { text: "Benchmark" }), el("th", { text: "Task" }),
        el("th", { text: "Models" }), el("th", { text: "Claims" }),
      ])]),
      el("tbody", {}, rows),
    ]);
    det.appendChild(el("div", { class: "scroll" }, [table]));
    root.appendChild(det);
  }
}

function renderMatrix(root) {
  const m = currentView().matrix;
  root.appendChild(el("p", { class: "lede", text:
    "The same question broken down by individual model: for each foundation model and task, does it beat the " +
    "task-specific alternative? The number is how many papers ran that comparison; the colour is the " +
    "direction vs task-specific. Cells with only model-vs-model results are left neutral (·). Click any cell " +
    "for the underlying results and verbatim quotes. Numbers are never averaged across datasets." }));
  root.appendChild(directionLegend());
  if (!m.tasks.length) { root.appendChild(el("p", { class: "empty-note", text: "No claims yet." })); return; }

  const table = el("table");
  const header = el("tr", {}, [el("th", { text: "" })].concat(
    m.tasks.map(t => el("th", { class: "colhead", text: taskName(t) }))));
  const body = [header];
  for (const model of m.models) {
    const cells = [el("th", { class: "rowhead", text: modelName(model) })];
    for (const task of m.tasks) {
      const cell = m.cells[model + "\t" + task];
      if (!cell) {
        cells.push(el("td", { class: "cell empty", title: "No evidence yet" }));
        continue;
      }
      // Direction/consensus reflect ONLY foundation-model-vs-task-specific
      // claims. cell.n_papers is that subset; n_papers_all is total evidence.
      const hasTS = cell.n_papers > 0;
      const mixed = cell.label === "contested";
      let dirCls, glyph, dirText;
      if (!hasTS) {
        dirCls = "none"; glyph = "·";
        dirText = "only model-vs-model results so far — no task-specific comparison";
      } else if (mixed) {
        dirCls = "mixed"; glyph = "±"; dirText = "papers disagree vs a task-specific model";
      } else {
        dirCls = cell.direction || "parity";
        glyph = DIR_GLYPH[cell.direction] || "";
        dirText = DIR_WORD[cell.direction] || "";
      }
      const nPapers = cell.n_papers_all !== undefined ? cell.n_papers_all : cell.n_papers;
      const tsNote = hasTS
        ? `${cell.n_papers} vs task-specific${cell.agreement !== null ? `, ${Math.round(cell.agreement * 100)}% agree` : ""}`
        : "no task-specific comparison yet";
      const td = el("td", {
        class: `cell dir-cell-${dirCls} ev-${hasTS ? cell.label : "none"}`,
        title: `${modelName(model)} on ${taskName(task)}: ${nPapers} paper(s), ${cell.n_claims} result(s) — ` +
               `${dirText} (${tsNote}). Click for details.`,
        onclick: () => openModal(`${modelName(model)} — ${taskName(task)}`, claimTable(cell.claims)),
      }, [
        el("span", { class: "glyph", text: glyph }),
        el("span", { class: "n", text: nPapers }),
      ]);
      cells.push(td);
    }
    body.push(el("tr", {}, cells));
  }
  const t = el("div", { class: "matrix scroll" }, [el("table", {}, [el("tbody", {}, body)])]);
  root.appendChild(t);
}

function renderChallenges(root) {
  root.appendChild(el("p", { class: "lede", text:
    "What do papers themselves say is still broken? Each paper's stated limitations are tagged against a " +
    "fixed vocabulary; this counts distinct papers per limitation. The bars rank today's most-cited open " +
    "challenges; the mini-columns show how often each was raised per month." }));
  const lim = DATA.limitations;
  const tags = Object.keys(lim.totals).sort((a, b) => lim.totals[b] - lim.totals[a]);
  if (!tags.length) { root.appendChild(el("p", { class: "empty-note", text: "No limitations recorded yet." })); return; }
  const maxTotal = Math.max(...tags.map(t => lim.totals[t]));
  const allMonths = [...new Set(tags.flatMap(t => Object.keys(lim.series[t] || {})))].sort();
  const maxMonthly = Math.max(1, ...tags.flatMap(t => Object.values(lim.series[t] || {})));

  const table = el("table", { class: "board" }, [
    el("thead", {}, [el("tr", {}, [
      el("th", { text: "Limitation" }),
      el("th", { text: "Papers citing it" }),
      el("th", { text: "Per month", title: "Distinct papers raising this limitation, by publication month" })])]),
    el("tbody", {}, tags.map(tag => {
      const series = lim.series[tag] || {};
      const trend = el("span", { class: "trend" }, allMonths.map(mm => {
        const v = series[mm] || 0;
        const col = el("span", { class: "tcol", title: `${mm}: ${v} paper(s)` });
        col.style.height = Math.max(2, Math.round((v / maxMonthly) * 22)) + "px";
        return col;
      }));
      const bar = el("span", { class: "bar" });
      bar.style.width = Math.round((lim.totals[tag] / maxTotal) * 240) + "px";
      return el("tr", {}, [
        el("td", {}, [
          el("div", { class: "lim-name", text: taskName(tag) }),
          el("div", { class: "lim-desc", text: LIMITATION_INFO[tag] || "" }),
        ]),
        el("td", { class: "barcell" }, [el("span", { class: "bar-wrap" }, [
          bar, el("span", { class: "bar-n", text: lim.totals[tag] })])]),
        el("td", {}, [trend]),
      ]);
    }))
  ]);
  root.appendChild(el("div", { class: "scroll" }, [table]));
}

function renderAxes(root) {
  root.appendChild(el("p", { class: "lede", text:
    "Twelve standing research questions (G1–G12) that the corpus is graded against. Every extracted result " +
    "is assigned to the question it answers; axes with no evidence yet are explicit gaps — they are what " +
    "nobody has measured, which is as informative as what everybody has." }));
  const axes = currentView().axes;
  for (const a of axes) {
    const info = AXIS_INFO[a.axis] || [a.axis, ""];
    const row = el("div", { class: "axis-row" });
    const left = el("div", {}, [
      el("span", { class: "axis-code", text: a.axis.split("_")[0] }),
      el("span", { class: "axis-name", text: info[0] }),
      el("p", { class: "axis-q", text: info[1] }),
    ]);
    // Consensus label reflects vs-task-specific claims; the count reflects all
    // evidence. An axis with papers but no task-specific comparison is neither a
    // gap nor a consensus — it's "no baseline".
    const total = a.n_papers_all !== undefined ? a.n_papers_all : a.n_papers;
    let chipLabel, chipExtra;
    if (total === 0) {
      chipLabel = "gap"; chipExtra = "no evidence";
    } else if (a.n_papers === 0) {
      chipLabel = "nobaseline";
      chipExtra = `${total} paper${total === 1 ? "" : "s"}, none vs task-specific`;
    } else {
      chipLabel = a.label;
      chipExtra = `${a.n_papers} vs task-specific` +
        (total > a.n_papers ? ` of ${total}` : "");
    }
    const right = el("div", { class: "axis-right" }, [labelChip(chipLabel, chipExtra)]);
    const head = el("div", { class: "axis-head" }, [left, right]);
    if (a.claims.length) {
      row.style.cursor = "pointer";
      row.title = "Click to see the evidence for this question";
      row.addEventListener("click", () => openModal(`${a.axis.split("_")[0]} · ${info[0]}`, claimTable(a.claims)));
    }
    row.appendChild(head);
    root.appendChild(row);
  }
}

function renderRegistry(root) {
  const r = DATA.registry;
  root.appendChild(el("p", { class: "lede", text:
    "Every paper in the corpus. \"DOI status\" is the result of mechanical verification: DOIs are taken " +
    "only from Crossref/OpenAlex/arXiv metadata (never from the language model) and checked before being " +
    "shown. Quarantined = a paper whose extraction failed validation; it is kept aside with its raw " +
    "output for inspection and never enters the statistics." }));

  const stats = el("div", { class: "stats" }, [
    el("div", { class: "stat" }, [
      el("div", { class: "v", text: r.n_papers }), el("div", { class: "k", text: "papers" })]),
    ...Object.entries(r.doi_status_counts).map(([k, v]) =>
      el("div", { class: "stat", title: DOI_STATUS_INFO[k] || "" }, [
        el("div", { class: "v", text: v }), el("div", { class: "k", text: "DOI " + k.replace(/_/g, " ") })])),
    el("div", { class: "stat" + (r.quarantine_count ? " warn" : "") ,
                title: "Extractions that failed validation — kept aside, never counted" }, [
      el("div", { class: "v", text: r.quarantine_count }), el("div", { class: "k", text: "quarantined" })]),
  ]);
  root.appendChild(stats);

  const table = el("table", { class: "registry" }, [
    el("thead", {}, [el("tr", {}, [
      el("th", { text: "Title" }),
      el("th", { text: "Date" }),
      el("th", { text: "Venue" }),
      el("th", { text: "DOI" }),
      el("th", { text: "DOI status", title: "verified: resolved & confirmed · no doi found: none exists in metadata · unresolved: lookup failed, retried next run · mismatch: resolves to a different title" }),
      el("th", { text: "Results", title: "Number of verified quantitative claims extracted" })])]),
    el("tbody", {}, r.papers.map(p => el("tr", {}, [
      el("td", {}, [p.link ? el("a", { text: p.title, attrs: { href: p.link, target: "_blank", rel: "noopener noreferrer" } }) : txt(p.title),
        p.self_evaluation ? el("span", { class: "badge self", text: "self-eval",
          title: "Authors helped create the model they evaluate" }) : null]),
      el("td", { text: p.date }),
      el("td", { text: p.venue || "—" }),
      el("td", {}, [p.doi
        ? el("a", { text: p.doi, attrs: { href: "https://doi.org/" + encodeURIComponent(p.doi).replace(/%2F/gi, "/"), target: "_blank", rel: "noopener noreferrer" } })
        : txt("—")]),
      el("td", {}, [el("span", { class: "doi doi-" + p.doi_status,
        text: p.doi_status.replace(/_/g, " "), title: DOI_STATUS_INFO[p.doi_status] || "" })]),
      el("td", { text: p.n_claims })
    ])))
  ]);
  root.appendChild(el("div", { class: "scroll" }, [table]));
}

const TABS = [
  { id: "verdicts", label: "GFM vs task-specific", render: renderVerdicts },
  { id: "benchmarks", label: "By benchmark", render: renderBenchmarks },
  { id: "bymodel", label: "By model", render: renderMatrix },
  { id: "axes", label: "Research axes", render: renderAxes },
  { id: "challenges", label: "Open challenges", render: renderChallenges },
  { id: "registry", label: "Paper registry", render: renderRegistry },
];
// Deep-linkable tabs: #bymodel, #registry, … (falls back to the verdicts view).
let activeTab = TABS.some(t => t.id === location.hash.slice(1))
  ? location.hash.slice(1) : "verdicts";

function renderTabs() {
  const nav = document.getElementById("tabs");
  nav.textContent = "";
  for (const t of TABS) {
    nav.appendChild(el("button", {
      class: "tab" + (t.id === activeTab ? " active" : ""),
      text: t.label,
      onclick: () => { activeTab = t.id; history.replaceState(null, "", "#" + t.id); render(); }
    }));
  }
}

function renderSubtitle() {
  const sub = document.getElementById("subtitle");
  sub.textContent = `A self-updating review of the evidence · ${DATA.meta.n_papers} papers · ` +
    `corpus through ${DATA.corpus_through || "—"}` +
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
