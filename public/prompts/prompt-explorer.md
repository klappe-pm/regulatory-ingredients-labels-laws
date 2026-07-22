---
domain: regulatory-ingredients-labels-laws
category: regulatory-labeling
sub-category: overview
types:
  - dashboard
date-created: 2026-07-22
date-revised: 2026-07-22
status: DONE
topic: beverage-label-compliance
use-case: filter-prompts-by-property
visibility: private
aliases:
  - dataview dashboard
  - filter prompts
  - find a prompt
  - prompt explorer
  - prompt finder
  - search prompts by property
tags:
  - dashboard
  - dataview
  - prompt-library
  - regulatory-labeling
---

# prompt-explorer

An interactive way to find a prompt: pick values from the dropdowns below and the matching prompts appear. It starts empty on purpose. Choose a category, sub-category, use case, or visibility, or type words into the search box (it matches the prompt name and its aliases), and the list fills in. This is an alternative to the Bases tables on [[regulatory-labeling]]; use whichever you prefer.

Requires the Dataview community plugin with JavaScript queries enabled (Settings, Community plugins, install "Dataview", then in its options turn on "Enable JavaScript Queries"). If the block below shows as code instead of controls, Dataview is not installed or JS queries are off. The Bases view on [[regulatory-labeling]] needs no plugin and always works.

## explorer

```dataviewjs
// Prompt explorer: empty until a property is chosen. Filters prompts and skills
// by frontmatter properties, plus a free-text search over name and aliases.
const pages = dv.pages('"public/prompts"').where(p => {
  const t = p.types ?? p.type;
  const arr = Array.isArray(t) ? Array.from(t) : (t ? [t] : []);
  return arr.includes("prompt") || arr.includes("skill");
});

const PROPS = [
  { key: "category", label: "Category" },
  { key: "sub-category", label: "Sub-category" },
  { key: "use-case", label: "Use case" },
  { key: "visibility", label: "Visibility" },
];

function valuesFor(key) {
  const s = new Set();
  for (const p of pages) {
    const v = p[key];
    if (v !== null && v !== undefined && String(v).length) s.add(String(v));
  }
  return Array.from(s).sort();
}

const selected = {};
let textQuery = "";

const controls = dv.container.createEl("div");
controls.style.display = "flex";
controls.style.flexWrap = "wrap";
controls.style.gap = "0.75rem";
controls.style.margin = "0.5rem 0 1rem 0";

function labeledControl(labelText) {
  const wrap = controls.createEl("label");
  wrap.style.display = "flex";
  wrap.style.flexDirection = "column";
  wrap.style.fontSize = "0.8em";
  wrap.style.gap = "0.2rem";
  wrap.createEl("span", { text: labelText });
  return wrap;
}

for (const prop of PROPS) {
  const wrap = labeledControl(prop.label);
  const sel = wrap.createEl("select");
  sel.createEl("option", { text: "any", value: "" });
  for (const v of valuesFor(prop.key)) sel.createEl("option", { text: v, value: v });
  sel.addEventListener("change", () => { selected[prop.key] = sel.value; render(); });
}

const searchWrap = labeledControl("Search name or alias");
const search = searchWrap.createEl("input", { type: "text" });
search.placeholder = "e.g. sodium claim";
search.addEventListener("input", () => { textQuery = search.value; render(); });

const resetWrap = labeledControl(" ");
const reset = resetWrap.createEl("button", { text: "clear" });
reset.addEventListener("click", () => {
  for (const k of Object.keys(selected)) selected[k] = "";
  textQuery = "";
  render();
});

const results = dv.container.createEl("div");

function matches(p) {
  for (const prop of PROPS) {
    const want = selected[prop.key];
    if (want && String(p[prop.key] ?? "") !== want) return false;
  }
  if (textQuery.trim()) {
    const q = textQuery.trim().toLowerCase();
    const aliases = p.aliases ? Array.from(p.aliases) : [];
    const hay = [p.file.name, ...aliases].join(" ").toLowerCase();
    if (!hay.includes(q)) return false;
  }
  return true;
}

function render() {
  results.replaceChildren();
  const anyFilter = PROPS.some(pr => selected[pr.key]) || textQuery.trim().length > 0;
  if (!anyFilter) {
    results.createEl("p", { text: "Choose a property value or type a search term to list matching prompts." })
      .style.opacity = "0.7";
    return;
  }
  const hits = pages.where(matches).sort(p => p.file.name, "asc");
  results.createEl("p", { text: `${hits.length} prompt(s)` }).style.opacity = "0.7";
  if (!hits.length) return;
  const table = results.createEl("table");
  const head = table.createEl("thead").createEl("tr");
  for (const h of ["Prompt", "Category", "Sub-category", "Use case"]) head.createEl("th", { text: h });
  const body = table.createEl("tbody");
  for (const p of hits) {
    const tr = body.createEl("tr");
    const a = tr.createEl("td").createEl("a", { cls: "internal-link", text: p.file.name });
    a.dataset.href = p.file.path;
    a.href = p.file.path;
    tr.createEl("td", { text: String(p.category ?? "") });
    tr.createEl("td", { text: String(p["sub-category"] ?? "") });
    tr.createEl("td", { text: String(p["use-case"] ?? "") });
  }
}

render();
```

Related: [[regulatory-labeling]], [[prompt-library-user-guide]].
