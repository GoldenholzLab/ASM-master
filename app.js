const CSV_URL = "ASM-list.csv";
const NAME_KEY = "generic_name";
const ALT_NAME_KEY = "alternate_generic_names";
const RCT_KEY = "pubmed_phase_ii_iii_rct_links";
const NOTES_KEY = "status_or_notes";
const EVIDENCE_KEY = "evidence_sources";
const REFRESH_KEY = "data_most_recently_refreshed";
const FILTER_PREFIX = "filter_";
const GRAPH_PREFIX = "diff_";
const INTERNAL_COLUMNS = new Set([
  ALT_NAME_KEY,
  EVIDENCE_KEY,
  "rct_pubmed_verification_notes",
  REFRESH_KEY,
  "pubmed_search_aliases"
]);
const ACRONYM_WORDS = new Set(["asm", "fda", "iv", "im", "moa", "mpc", "qt", "rct", "rr50", "tsc", "us"]);

const listEl = document.querySelector("#asmList");
const toolbarEl = document.querySelector("#toolbar");
const searchEl = document.querySelector("#search");
const symptomWordFieldEl = document.querySelector("#symptomWordField");
const symptomTextFilterEl = document.querySelector("#symptomTextFilter");
const symptomSuggestionsEl = document.querySelector("#symptomSuggestions");
const notSymptomFilterEl = document.querySelector("#notSymptomFilter");
const graphToggleEl = document.querySelector("#graphToggle");
const clearFiltersEl = document.querySelector("#clearFilters");
const selectAllAsmsEl = document.querySelector("#selectAllAsms");
const selectNoAsmsEl = document.querySelector("#selectNoAsms");
const asmChecksEl = document.querySelector("#asmChecks");
const selectAllColumnsEl = document.querySelector("#selectAllColumns");
const selectNoColumnsEl = document.querySelector("#selectNoColumns");
const columnChecksEl = document.querySelector("#columnChecks");
const summaryEl = document.querySelector("#summary");
const refreshDateEl = document.querySelector("#refreshDate");

const state = {
  headers: [],
  rows: [],
  displayColumns: [],
  filterColumns: [],
  filterInputs: new Map(),
  graphColumns: [],
  visibleRows: [],
  filterMatchedRows: [],
  selectedAsms: new Set(),
  hiddenColumns: new Set()
};

function parseCsv(text) {
  const rows = [];
  let row = [];
  let value = "";
  let inQuotes = false;

  for (let i = 0; i < text.length; i += 1) {
    const char = text[i];
    const next = text[i + 1];

    if (char === '"' && inQuotes && next === '"') {
      value += '"';
      i += 1;
    } else if (char === '"') {
      inQuotes = !inQuotes;
    } else if (char === "," && !inQuotes) {
      row.push(value);
      value = "";
    } else if ((char === "\n" || char === "\r") && !inQuotes) {
      if (char === "\r" && next === "\n") {
        i += 1;
      }
      row.push(value);
      if (row.some((cell) => cell.trim() !== "")) {
        rows.push(row);
      }
      row = [];
      value = "";
    } else {
      value += char;
    }
  }

  if (value || row.length) {
    row.push(value);
    rows.push(row);
  }

  const headers = rows.shift() || [];
  return {
    headers,
    rows: rows.map((cells) => Object.fromEntries(headers.map((header, index) => [header, cells[index] || ""])))
  };
}

function escapeHtml(value) {
  return String(value || "").replace(/[&<>"']/g, (char) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;"
  })[char]);
}

function normalizeText(value) {
  return String(value || "").replace(/\s+/g, " ").trim();
}

function labelFromKey(key) {
  return key
    .replace(new RegExp(`^${FILTER_PREFIX}`), "")
    .replace(/_/g, " ")
    .split(" ")
    .filter(Boolean)
    .map((word) => (ACRONYM_WORDS.has(word.toLowerCase()) ? word.toUpperCase() : word.charAt(0).toUpperCase() + word.slice(1)))
    .join(" ");
}

function splitValues(value) {
  return String(value || "")
    .split(";")
    .map((item) => item.trim())
    .filter(Boolean);
}

function isInternalColumn(key) {
  return key.startsWith(FILTER_PREFIX) || INTERNAL_COLUMNS.has(key);
}

function isRequiredColumn(key) {
  return key === NAME_KEY;
}

function linkifyText(value) {
  const escaped = escapeHtml(value);
  return escaped.replace(/https?:\/\/[^\s<]+/g, (url) => `<a class="trial-link" href="${url}" target="_blank" rel="noopener">${url}</a>`);
}

function renderPubMedLinks(value, rowId) {
  const links = splitValues(value).map((item) => {
    const pipeMatch = item.match(/^(.*?)\|(https?:\/\/\S+)$/);
    const colonMatch = item.match(/^(.*?):\s*(https?:\/\/\S+)$/);
    const match = pipeMatch || colonMatch;
    if (!match) {
      return linkifyText(item);
    }
    return `<a class="trial-link" href="${escapeHtml(match[2])}" target="_blank" rel="noopener">${escapeHtml(match[1])}</a>`;
  });

  if (!links.length) {
    return "";
  }
  if (links.length <= 3) {
    return links.join("<br>");
  }

  return `
    ${links.slice(0, 3).join("<br>")}
    <button class="rct-toggle" type="button" data-rct-target="rct-${rowId}" aria-expanded="false" title="Show all RCT links">+</button>
    <span class="rct-extra" id="rct-${rowId}" hidden><br>${links.slice(3).join("<br>")}</span>
  `;
}

function symptomWords(row) {
  const stopWords = new Set(["and", "with", "for", "the", "data", "found", "usable", "current", "located", "evidence", "availability", "reliable", "quantified"]);
  const symptomColumns = state.headers.filter((key) => key.includes("symptom") || key.includes("adverse"));
  const words = symptomColumns
    .map((key) => row[key] || "")
    .join(" ")
    .toLowerCase()
    .replace(/>/g, " ")
    .match(/[a-z][a-z/-]{2,}/g) || [];
  return [...new Set(words.filter((word) => !stopWords.has(word) && !word.includes("fda/rct")))];
}

function allSymptomWords() {
  return [...new Set(state.rows.flatMap(symptomWords))].sort();
}

function updateSymptomSuggestions() {
  const query = symptomTextFilterEl.value.trim().toLowerCase();
  const matches = allSymptomWords()
    .filter((word) => !query || word.includes(query) || query.includes(word))
    .slice(0, 40);
  symptomSuggestionsEl.innerHTML = matches.map((word) => `<option value="${escapeHtml(word)}"></option>`).join("");
}

function makeFilterControl(key) {
  const label = document.createElement("label");
  label.className = "field";

  const text = document.createElement("span");
  text.className = "field-label";
  text.textContent = labelFromKey(key);

  const select = document.createElement("select");
  const empty = document.createElement("option");
  empty.value = "";
  empty.textContent = "All";
  select.append(empty);

  const values = [...new Set(state.rows.flatMap((row) => splitValues(row[key])))].sort((a, b) => a.localeCompare(b));
  values.forEach((value) => {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    select.append(option);
  });

  select.addEventListener("change", () => applyFilters());
  state.filterInputs.set(key, select);
  label.append(text, select);
  return label;
}

function populateFilters() {
  state.filterInputs.clear();
  state.filterColumns.forEach((key) => {
    toolbarEl.insertBefore(makeFilterControl(key), symptomWordFieldEl);
  });
  updateSymptomSuggestions();
}

function populateAsmChecks() {
  asmChecksEl.innerHTML = state.rows.map((row) => `
    <label class="check-item">
      <input type="checkbox" value="${escapeHtml(row[NAME_KEY])}" autocomplete="off" checked>
      <span>${escapeHtml(row[NAME_KEY])}</span>
    </label>
  `).join("");
}

function populateColumnChecks() {
  columnChecksEl.innerHTML = state.displayColumns.filter((column) => !column.required).map((column) => `
    <label class="check-item">
      <input type="checkbox" value="${escapeHtml(column.key)}" checked>
      <span>${escapeHtml(column.label)}</span>
    </label>
  `).join("");
}

function syncColumnChecks() {
  columnChecksEl.querySelectorAll("input").forEach((input) => {
    input.checked = !state.hiddenColumns.has(input.value);
  });
}

function syncAsmChecks(rows) {
  const matchingNames = new Set(rows.map((row) => row[NAME_KEY]));
  state.selectedAsms = new Set(matchingNames);
  asmChecksEl.querySelectorAll("input").forEach((input) => {
    input.checked = matchingNames.has(input.value);
  });
}

function outcomeRange(row, columnKey) {
  const source = row[columnKey] || "";
  const leadingText = source.split("(")[0];
  const numbers = [...leadingText.matchAll(/(-?\d+(?:\.\d+)?)(?:\s*-\s*(-?\d+(?:\.\d+)?))?\s*%/g)]
    .flatMap((match) => [match[1], match[2]].filter(Boolean).map(Number))
    .filter((value) => Number.isFinite(value));
  if (!numbers.length) {
    return null;
  }
  const min = Math.max(0, Math.min(100, Math.min(...numbers)));
  const max = Math.max(0, Math.min(100, Math.max(...numbers)));
  return {
    min,
    max,
    label: min === max ? `${max}%` : `${min}-${max}%`,
    source
  };
}

function graphData(rows, columnKey) {
  return rows
    .map((row) => ({ row, range: outcomeRange(row, columnKey) }))
    .filter((item) => item.range)
    .sort((a, b) => b.range.max - a.range.max || a.row[NAME_KEY].localeCompare(b.row[NAME_KEY]));
}

function activeFilterSummary() {
  const active = [];
  if (searchEl.value.trim()) {
    active.push(`Search: ${searchEl.value.trim()}`);
  }
  state.filterInputs.forEach((select, key) => {
    if (select.value) {
      active.push(`${labelFromKey(key)}: ${select.value}`);
    }
  });
  if (symptomTextFilterEl.value.trim()) {
    active.push(`${notSymptomFilterEl.checked ? "NOT " : ""}Symptom word: ${symptomTextFilterEl.value.trim()}`);
  }
  if (state.selectedAsms.size !== state.filterMatchedRows.length) {
    active.push(`Manual ASM selection: ${state.selectedAsms.size} of ${state.filterMatchedRows.length} selected`);
  }
  return active.length ? active.join("; ") : "No filters active";
}

function renderChart(column, rows) {
  const data = graphData(rows, column.key);
  const missingCount = rows.length - data.length;
  const title = labelFromKey(column.key);
  const filterSummary = activeFilterSummary();
  if (!data.length) {
    return `
      <section class="chart">
        <div class="chart-head">
          <h2>${escapeHtml(title)}</h2>
          <div class="chart-counts" aria-label="Chart counts">
            <span class="chart-pill">${rows.length} filtered</span>
            <span class="chart-pill">0 plotted</span>
          </div>
        </div>
        <p class="chart-meta">Values are read from the CSV column named ${escapeHtml(column.key)}. Axis is fixed at 0-100%.</p>
        <p class="chart-filter-summary"><strong>Displayed set:</strong> ${escapeHtml(filterSummary)}</p>
        <p class="chart-empty">No numeric values are available for the current filters.</p>
      </section>
    `;
  }

  const left = 210;
  const right = 112;
  const top = 34;
  const rowHeight = 34;
  const width = 920;
  const height = top + data.length * rowHeight + 46;
  const scale = (value) => left + (value / 100) * (width - left - right);
  const ticks = [0, 25, 50, 75, 100];

  const bars = data.map((item, index) => {
    const y = top + index * rowHeight;
    const x1 = scale(item.range.min);
    const x2 = scale(item.range.max);
    return `
      <text x="0" y="${y + 13}" font-size="12" font-weight="700" fill="#18212f">${escapeHtml(item.row[NAME_KEY])}</text>
      <line x1="${left}" y1="${y + 15}" x2="${width - right}" y2="${y + 15}" stroke="#dbe3ee" stroke-width="8" stroke-linecap="round" />
      <line x1="${x1}" y1="${y + 15}" x2="${x2}" y2="${y + 15}" stroke="#0f766e" stroke-width="8" stroke-linecap="round" />
      <circle cx="${x1}" cy="${y + 15}" r="4" fill="#0f766e" />
      <circle cx="${x2}" cy="${y + 15}" r="4" fill="#0f766e" />
      <text x="${width - right + 14}" y="${y + 19}" font-size="11.5" font-weight="700" fill="#334155">${escapeHtml(item.range.label)}</text>
    `;
  }).join("");

  const axis = ticks.map((tick) => `
    <line x1="${scale(tick)}" y1="24" x2="${scale(tick)}" y2="${height - 30}" stroke="#d8dee8" />
    <text x="${scale(tick)}" y="14" font-size="11" text-anchor="middle" fill="#637083">${tick}%</text>
    <text x="${scale(tick)}" y="${height - 10}" font-size="11" text-anchor="middle" fill="#637083">${tick}%</text>
  `).join("");

  return `
    <section class="chart">
      <div class="chart-head">
        <h2>${escapeHtml(title)}</h2>
        <div class="chart-counts" aria-label="Chart counts">
          <span class="chart-pill">${rows.length} filtered</span>
          <span class="chart-pill">${data.length} plotted</span>
          <span class="chart-pill">${missingCount} no numeric value</span>
        </div>
      </div>
      <p class="chart-meta">Values are read from the CSV column named ${escapeHtml(column.key)}. Axis is fixed at 0-100%; rows are sorted by highest plotted value.</p>
      <p class="chart-filter-summary"><strong>Displayed set:</strong> ${escapeHtml(filterSummary)}</p>
      <div class="chart-legend" aria-label="Chart legend">
        <span class="legend-item"><span class="legend-swatch legend-track"></span>0-100% scale</span>
        <span class="legend-item"><span class="legend-swatch"></span>reported range</span>
      </div>
      <svg viewBox="0 0 ${width} ${height}" role="img" aria-label="${escapeHtml(title)} chart">
        <text x="0" y="14" font-size="11" fill="#637083">Differential %</text>
        ${axis}
        ${bars}
        <text x="${left}" y="${height - 32}" font-size="11" fill="#637083">0%</text>
        <text x="${width - right}" y="${height - 32}" font-size="11" text-anchor="end" fill="#637083">100%</text>
      </svg>
    </section>
  `;
}

function renderGraphs(rows) {
  if (!state.graphColumns.length) {
    listEl.innerHTML = '<p class="empty">No graphable differential columns are present in the CSV.</p>';
    return;
  }
  listEl.innerHTML = `<div class="graph-panel">${state.graphColumns.map((column) => renderChart(column, rows)).join("")}</div>`;
}

function visibleColumns() {
  return state.displayColumns.filter((column) => column.required || !state.hiddenColumns.has(column.key));
}

function sampleLength(value) {
  return normalizeText(value).replace(/https?:\/\/\S+/g, "").length;
}

function columnWidth(column) {
  const lengths = state.rows
    .map((row) => sampleLength(row[column.key]))
    .sort((a, b) => a - b);
  const percentile = lengths[Math.floor(lengths.length * 0.8)] || 0;
  const basis = Math.max(labelFromKey(column.key).length, percentile);
  return Math.max(140, Math.min(520, Math.round(basis * 7.2 + 72)));
}

function tableWidth(activeColumns) {
  return Math.max(activeColumns.reduce((sum, column) => sum + column.width, 0), listEl.clientWidth || 0);
}

function rowId(row, index) {
  return `${index}-${String(row[NAME_KEY] || "row").replace(/[^a-z0-9]+/gi, "-")}`;
}

function renderCell(column, row, index) {
  let content = escapeHtml(row[column.key] || "");
  if (column.key === NAME_KEY) {
    const alt = row[ALT_NAME_KEY] ? `<p class="alt">${escapeHtml(row[ALT_NAME_KEY])}</p>` : "";
    content = `<p class="generic">${escapeHtml(row[NAME_KEY])}</p>${alt}`;
  } else if (column.key === RCT_KEY) {
    content = renderPubMedLinks(row[column.key], rowId(row, index));
  } else if (column.key === NOTES_KEY && row[EVIDENCE_KEY]) {
    content = `${escapeHtml(row[column.key] || "")}<p class="evidence">${escapeHtml(row[EVIDENCE_KEY])}</p>`;
  } else if (/https?:\/\//.test(row[column.key] || "")) {
    content = linkifyText(row[column.key]);
  }
  return `<td data-column="${escapeHtml(column.key)}">${content}</td>`;
}

function render(rows) {
  state.visibleRows = rows;
  summaryEl.textContent = `${rows.length} of ${state.rows.length} ASMs`;

  if (!rows.length) {
    listEl.innerHTML = '<p class="empty">No ASMs match the current search.</p>';
    return;
  }

  if (graphToggleEl.checked) {
    renderGraphs(rows);
    return;
  }

  const activeColumns = visibleColumns();
  const body = rows.map((row, index) => `
    <tr>
      ${activeColumns.map((column) => renderCell(column, row, index)).join("")}
    </tr>
  `).join("");

  listEl.innerHTML = `
    <table class="asm-table" style="width: ${tableWidth(activeColumns)}px;">
      <colgroup>
        ${activeColumns.map((column) => `<col style="width: ${column.width}px;">`).join("")}
      </colgroup>
      <thead>
        <tr>
          ${activeColumns.map((column) => `<th data-column="${escapeHtml(column.key)}">${escapeHtml(column.label)}</th>`).join("")}
        </tr>
      </thead>
      <tbody>${body}</tbody>
    </table>
  `;
}

function rowsMatchingCriteria() {
  const query = searchEl.value.trim().toLowerCase();
  const symptomText = symptomTextFilterEl.value.trim().toLowerCase();
  const notSymptom = notSymptomFilterEl.checked;

  return state.rows.filter((row) => {
    const matchesText = !query || Object.values(row).join(" ").toLowerCase().includes(query);
    const matchesDynamicFilters = [...state.filterInputs.entries()].every(([key, select]) => (
      !select.value || splitValues(row[key]).includes(select.value)
    ));
    const hasSymptomWord = !symptomText || symptomWords(row).some((word) => word.includes(symptomText) || symptomText.includes(word));
    const matchesSymptomWord = !symptomText || (notSymptom ? !hasSymptomWord : hasSymptomWord);
    return matchesText && matchesDynamicFilters && matchesSymptomWord;
  });
}

function applyFilters(syncManualSelection = true) {
  state.filterMatchedRows = rowsMatchingCriteria();
  if (syncManualSelection) {
    syncAsmChecks(state.filterMatchedRows);
  }
  render(state.filterMatchedRows.filter((row) => state.selectedAsms.has(row[NAME_KEY])));
}

function clearBrowserRestoredFilters() {
  searchEl.value = "";
  state.filterInputs.forEach((select) => {
    select.value = "";
  });
  symptomTextFilterEl.value = "";
  notSymptomFilterEl.checked = false;
}

function initializeFromCsv(text) {
  const parsed = parseCsv(text);
  state.headers = parsed.headers;
  state.rows = parsed.rows.sort((a, b) => a[NAME_KEY].localeCompare(b[NAME_KEY]));
  state.filterColumns = state.headers.filter((key) => key.startsWith(FILTER_PREFIX));
  state.displayColumns = state.headers
    .filter((key) => !isInternalColumn(key))
    .map((key) => ({
      key,
      label: labelFromKey(key),
      required: isRequiredColumn(key)
    }));
  state.displayColumns.forEach((column) => {
    column.width = columnWidth(column);
  });
  state.graphColumns = state.displayColumns.filter((column) => column.key.startsWith(GRAPH_PREFIX));

  const refreshDate = state.rows.find((row) => row[REFRESH_KEY])?.[REFRESH_KEY] || "Unknown";
  refreshDateEl.textContent = `Data was most recently refreshed on: ${refreshDate}`;
  populateFilters();
  populateAsmChecks();
  populateColumnChecks();
  clearBrowserRestoredFilters();
  applyFilters();
}

function csvRequestUrl() {
  const url = new URL(CSV_URL, window.location.href);
  url.searchParams.set("v", Date.now().toString());
  return url.href;
}

fetch(csvRequestUrl(), { cache: "no-store" })
  .then((response) => {
    if (!response.ok) {
      throw new Error(`Could not load ${CSV_URL} (${response.status})`);
    }
    return response.text();
  })
  .then(initializeFromCsv)
  .catch((error) => {
    summaryEl.textContent = "CSV unavailable";
    listEl.innerHTML = `<p class="error">${escapeHtml(error.message)}</p>`;
  });

searchEl.addEventListener("input", () => applyFilters());
symptomTextFilterEl.addEventListener("input", () => {
  updateSymptomSuggestions();
  applyFilters();
});
notSymptomFilterEl.addEventListener("change", () => applyFilters());
graphToggleEl.addEventListener("change", () => render(state.visibleRows));
listEl.addEventListener("click", (event) => {
  const button = event.target.closest(".rct-toggle");
  if (!button) {
    return;
  }
  const extra = document.getElementById(button.dataset.rctTarget);
  if (!extra) {
    return;
  }
  const expanded = extra.hidden;
  extra.hidden = !expanded;
  button.textContent = expanded ? "-" : "+";
  button.setAttribute("aria-expanded", String(expanded));
});
clearFiltersEl.addEventListener("click", () => {
  searchEl.value = "";
  state.filterInputs.forEach((select) => {
    select.value = "";
  });
  symptomTextFilterEl.value = "";
  notSymptomFilterEl.checked = false;
  updateSymptomSuggestions();
  applyFilters();
});
asmChecksEl.addEventListener("change", () => {
  state.selectedAsms = new Set([...asmChecksEl.querySelectorAll("input:checked")].map((input) => input.value));
  applyFilters(false);
});
selectAllAsmsEl.addEventListener("click", () => {
  state.selectedAsms = new Set(state.filterMatchedRows.map((row) => row[NAME_KEY]));
  asmChecksEl.querySelectorAll("input").forEach((input) => {
    input.checked = state.selectedAsms.has(input.value);
  });
  applyFilters(false);
});
selectNoAsmsEl.addEventListener("click", () => {
  state.selectedAsms = new Set();
  asmChecksEl.querySelectorAll("input").forEach((input) => {
    input.checked = false;
  });
  applyFilters(false);
});
columnChecksEl.addEventListener("change", () => {
  state.hiddenColumns.clear();
  columnChecksEl.querySelectorAll("input:not(:checked)").forEach((input) => {
    state.hiddenColumns.add(input.value);
  });
  render(state.visibleRows);
});
selectAllColumnsEl.addEventListener("click", () => {
  state.hiddenColumns.clear();
  syncColumnChecks();
  render(state.visibleRows);
});
selectNoColumnsEl.addEventListener("click", () => {
  state.hiddenColumns.clear();
  state.displayColumns.filter((column) => !column.required).forEach((column) => {
    state.hiddenColumns.add(column.key);
  });
  syncColumnChecks();
  render(state.visibleRows);
});
