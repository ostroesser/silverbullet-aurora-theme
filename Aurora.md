#meta

# Aurora theme
A polished, modern style for SilverBullet. Inter for prose, JetBrains Mono for code, soft indigo→violet accents, glassy chrome and card-like blocks.

```space-style
@import url("https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400..800&family=JetBrains+Mono:wght@400;500;600&display=swap");

/* ───────────────────────── Tokens: light ───────────────────────── */
html {
  --au-bg: #f7f7fb;
  --au-bg-glow-1: rgba(99, 102, 241, 0.10);
  --au-bg-glow-2: rgba(236, 72, 153, 0.06);
  --au-surface: #ffffff;
  --au-surface-2: #f1f1f8;
  --au-border: #e4e4ef;
  --au-text: #1b1b2b;
  --au-text-soft: #4a4a63;
  --au-muted: #8b8ba3;
  --au-accent: #5b5bf0;
  --au-accent-2: #a24ef0;
  --au-accent-soft: rgba(91, 91, 240, 0.10);
  --au-accent-ring: rgba(91, 91, 240, 0.28);
  --au-shadow: 0 1px 2px rgba(20, 20, 50, .04), 0 8px 24px -8px rgba(20, 20, 50, .10);
  --au-shadow-lg: 0 24px 64px -12px rgba(20, 20, 60, .28), 0 2px 6px rgba(20, 20, 60, .06);
  --au-radius: 12px;

  --ui-font: "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --editor-font: "Inter", ui-sans-serif, system-ui, sans-serif;
  --au-mono: "JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace;
  --editor-width: 760px;

  --ui-accent-color: var(--au-accent);
  --ui-accent-text-color: var(--au-accent);
  --root-background-color: var(--au-bg);
  --root-color: var(--au-text);
  --top-background-color: color-mix(in srgb, var(--au-bg) 72%, transparent);
  --top-color: var(--au-text);
  --top-border-color: color-mix(in srgb, var(--au-border) 70%, transparent);
  --subtle-color: var(--au-muted);
  --meta-color: var(--au-muted);
  --meta-subtle-color: color-mix(in srgb, var(--au-muted) 60%, transparent);

  --link-color: var(--au-accent);
  --editor-link-color: var(--au-accent);
  --editor-link-url-color: var(--au-muted);
  --editor-link-meta-color: var(--au-muted);
  --editor-naked-url-color: var(--au-accent);
  --editor-wiki-link-page-color: var(--au-accent);
  --editor-wiki-link-page-background-color: transparent;
  --editor-wiki-link-page-missing-color: #d9480f;
  --editor-wiki-link-color: var(--au-muted);
  --editor-meta-color: var(--au-muted);
  --editor-line-meta-color: var(--au-muted);
  --editor-heading-color: #11111f;
  --editor-heading-meta-color: color-mix(in srgb, var(--au-accent) 45%, transparent);
  --editor-list-bullet-color: var(--au-accent);
  --editor-caret-color: var(--au-accent);
  --editor-selection-background-color: rgba(91, 91, 240, 0.16);
  --editor-ruler-color: var(--au-border);
  --editor-hashtag-color: #5040d8;
  --editor-hashtag-background-color: rgba(91, 91, 240, 0.09);
  --editor-hashtag-border-color: rgba(91, 91, 240, 0.18);
  --editor-highlight-background-color: rgba(250, 204, 21, 0.38);
  --highlight-color: rgba(250, 204, 21, 0.38);
  --editor-code-background-color: #f3f3f9;
  --editor-code-color: #2b2b44;
  --editor-code-comment-color: #8d8da6;
  --editor-code-string-color: #0f8a5f;
  --editor-code-number-color: #c2410c;
  --editor-code-variable-color: #4338ca;
  --editor-code-typename-color: #0e7490;
  --editor-code-operator-color: #9333ea;
  --editor-code-atom-color: #be185d;
  --editor-code-info-color: var(--au-muted);
  --editor-blockquote-background-color: transparent;
  --editor-blockquote-color: var(--au-text-soft);
  --editor-blockquote-border-color: var(--au-accent);
  --editor-table-head-background-color: var(--au-surface-2);
  --editor-table-head-color: var(--au-text);
  --editor-table-even-background-color: color-mix(in srgb, var(--au-surface-2) 55%, transparent);
  --editor-frontmatter-background-color: var(--au-surface-2);
  --editor-widget-background-color: var(--au-surface);
  --editor-task-marker-color: var(--au-muted);

  --modal-background-color: color-mix(in srgb, var(--au-surface) 88%, transparent);
  --modal-color: var(--au-text);
  --modal-border-color: var(--au-border);
  --modal-backdrop-color: rgba(20, 20, 40, 0.28);
  --modal-header-label-color: var(--au-accent);
  --modal-selected-option-background-color: var(--au-accent-soft);
  --modal-selected-option-color: var(--au-text);
  --modal-help-background-color: transparent;
  --modal-help-color: var(--au-muted);
  --modal-hint-background-color: var(--au-accent);
  --modal-hint-color: #fff;
  --modal-hint-inactive-background-color: var(--au-surface-2);
  --modal-hint-inactive-color: var(--au-muted);
  --modal-description-color: var(--au-muted);
  --button-background-color: var(--au-surface);
  --button-border-color: var(--au-border);
  --button-color: var(--au-text);
  --button-hover-background-color: var(--au-surface-2);
  --text-field-background-color: var(--au-surface);
  --action-button-color: var(--au-muted);
  --action-button-hover-color: var(--au-accent);
  --panel-background-color: var(--au-surface);
  --panel-border-color: var(--au-border);
}

/* ───────────────────────── Tokens: dark ───────────────────────── */
html[data-theme="dark"] {
  --au-bg: #0c0d14;
  --au-bg-glow-1: rgba(99, 102, 241, 0.16);
  --au-bg-glow-2: rgba(168, 85, 247, 0.08);
  --au-surface: #151622;
  --au-surface-2: #1c1d2c;
  --au-border: #2a2b3e;
  --au-text: #e7e7f2;
  --au-text-soft: #b8b8cf;
  --au-muted: #7d7e9a;
  --au-accent: #8f8dff;
  --au-accent-2: #d08cff;
  --au-accent-soft: rgba(143, 141, 255, 0.14);
  --au-accent-ring: rgba(143, 141, 255, 0.35);
  --au-shadow: 0 1px 2px rgba(0, 0, 0, .3), 0 8px 24px -8px rgba(0, 0, 0, .5);
  --au-shadow-lg: 0 24px 64px -12px rgba(0, 0, 0, .7), 0 0 0 1px rgba(255, 255, 255, .04);

  --ui-accent-color: var(--au-accent);
  --ui-accent-text-color: var(--au-accent);
  --root-background-color: var(--au-bg);
  --root-color: var(--au-text);
  --top-background-color: color-mix(in srgb, var(--au-bg) 70%, transparent);
  --top-color: var(--au-text);
  --top-border-color: rgba(255, 255, 255, 0.06);
  --subtle-color: var(--au-muted);
  --meta-color: var(--au-muted);
  --link-color: var(--au-accent);
  --editor-link-color: var(--au-accent);
  --editor-naked-url-color: var(--au-accent);
  --editor-wiki-link-page-color: var(--au-accent);
  --editor-wiki-link-page-background-color: transparent;
  --editor-wiki-link-page-missing-color: #ff9a5c;
  --editor-wiki-link-color: var(--au-muted);
  --editor-meta-color: var(--au-muted);
  --editor-line-meta-color: var(--au-muted);
  --editor-link-url-color: var(--au-muted);
  --editor-link-meta-color: var(--au-muted);
  --editor-heading-color: #f4f4ff;
  --editor-heading-meta-color: color-mix(in srgb, var(--au-accent) 45%, transparent);
  --editor-list-bullet-color: var(--au-accent);
  --editor-caret-color: var(--au-accent);
  --editor-selection-background-color: rgba(143, 141, 255, 0.24);
  --editor-ruler-color: var(--au-border);
  --editor-hashtag-color: #b9b7ff;
  --editor-hashtag-background-color: rgba(143, 141, 255, 0.13);
  --editor-hashtag-border-color: rgba(143, 141, 255, 0.24);
  --editor-highlight-background-color: rgba(250, 204, 21, 0.32);
  --highlight-color: rgba(250, 204, 21, 0.32);
  --editor-code-background-color: #12131d;
  --editor-code-color: #d6d6ea;
  --editor-code-comment-color: #6d6e8a;
  --editor-code-string-color: #5eead4;
  --editor-code-number-color: #fdba74;
  --editor-code-variable-color: #a5b4fc;
  --editor-code-typename-color: #67e8f9;
  --editor-code-operator-color: #d8b4fe;
  --editor-code-atom-color: #f9a8d4;
  --editor-blockquote-background-color: transparent;
  --editor-blockquote-color: var(--au-text-soft);
  --editor-blockquote-border-color: var(--au-accent);
  --editor-table-head-background-color: var(--au-surface-2);
  --editor-table-head-color: var(--au-text);
  --editor-table-even-background-color: rgba(255, 255, 255, 0.02);
  --editor-frontmatter-background-color: var(--au-surface-2);
  --editor-widget-background-color: var(--au-surface);
  --editor-task-marker-color: var(--au-muted);

  --modal-background-color: color-mix(in srgb, var(--au-surface) 86%, transparent);
  --modal-color: var(--au-text);
  --modal-border-color: var(--au-border);
  --modal-backdrop-color: rgba(0, 0, 0, 0.5);
  --modal-header-label-color: var(--au-accent);
  --modal-selected-option-background-color: var(--au-accent-soft);
  --modal-selected-option-color: var(--au-text);
  --modal-help-background-color: transparent;
  --modal-help-color: var(--au-muted);
  --modal-hint-background-color: var(--au-accent);
  --modal-hint-color: #0c0d14;
  --modal-hint-inactive-background-color: var(--au-surface-2);
  --modal-hint-inactive-color: var(--au-muted);
  --modal-description-color: var(--au-muted);
  --button-background-color: var(--au-surface-2);
  --button-border-color: var(--au-border);
  --button-color: var(--au-text);
  --button-hover-background-color: var(--au-border);
  --text-field-background-color: var(--au-surface);
  --action-button-color: var(--au-muted);
  --action-button-hover-color: var(--au-accent);
  --panel-background-color: var(--au-surface);
  --panel-border-color: var(--au-border);
}

/* ───────────────────────── Canvas ───────────────────────── */
body, #sb-root {
  background:
    radial-gradient(1200px 600px at 15% -10%, var(--au-bg-glow-1), transparent 60%),
    radial-gradient(900px 500px at 100% 0%, var(--au-bg-glow-2), transparent 55%),
    var(--au-bg);
  background-attachment: fixed;
  -webkit-font-smoothing: antialiased;
  font-feature-settings: "cv11", "ss01", "ss03";
}
#sb-main, #sb-main .cm-editor, #sb-main .cm-scroller { background: transparent; }

/* ───────────────────────── Top bar (glass) ───────────────────────── */
#sb-top {
  backdrop-filter: saturate(180%) blur(16px);
  -webkit-backdrop-filter: saturate(180%) blur(16px);
}
#sb-top .main .inner { font-size: 22px; padding: 14px 0 12px; }
#sb-top .main #sb-current-page .sb-input {
  font-weight: 700;
  letter-spacing: -0.025em;
}
#sb-top .sb-page-prefix { color: var(--au-muted); }
#sb-top .sb-actions button {
  border: 0;
  background: transparent;
  color: var(--au-muted);
  border-radius: 9px;
  padding: 6px 8px;
  margin-left: 2px;
  transition: background .15s ease, color .15s ease;
}
#sb-top .sb-actions button:hover {
  background: var(--au-accent-soft);
  color: var(--au-accent);
}
#sb-top .sb-actions button svg { stroke-width: 1.8; display: block; }
#sb-top .sb-actions { align-items: center; gap: 2px; transform: translateY(-3px); }
#sb-top .main .inner .wrapper { align-items: center; }

/* ───────────────────────── Editor typography ───────────────────────── */
#sb-main .cm-editor {
  font-family: var(--editor-font);
  font-size: 17px;
  color: var(--au-text);
}
#sb-main .cm-editor .cm-content {
  padding: 28px 20px 120px;
  line-height: 1.72;
  caret-color: var(--au-accent);
}
#sb-main .cm-editor .sb-line-h1,
#sb-main .cm-editor .sb-line-h2,
#sb-main .cm-editor .sb-line-h3,
#sb-main .cm-editor .sb-line-h4 {
  letter-spacing: -0.022em;
  line-height: 1.25;
  font-weight: 750;
}
#sb-main .cm-editor .sb-line-h1 { font-size: 2.15em; padding-bottom: 10px !important; font-weight: 800; letter-spacing: -0.035em; }
#sb-main .cm-editor .sb-line-h2 { font-size: 1.45em; padding-top: 22px !important; padding-bottom: 4px !important; }
#sb-main .cm-editor .sb-line-h3 { font-size: 1.18em; padding-top: 14px !important; }
#sb-main .cm-editor .sb-line-h4 { font-size: 1em; padding-top: 10px !important; text-transform: uppercase; letter-spacing: 0.06em; color: var(--au-muted); font-size: .82em; }

/* page title: accent bar beneath the H1 */
#sb-main .cm-editor .cm-line.sb-line-h1 {
  background-image: linear-gradient(90deg, var(--au-accent), var(--au-accent-2));
  background-size: 44px 4px;
  background-repeat: no-repeat;
  background-position: calc(var(--sb-indent, 0px)) calc(100% - 8px);
  padding-bottom: 26px !important;
}
#sb-main .cm-editor .sb-line-h1 .sb-meta,
#sb-main .cm-editor .sb-line-h2 .sb-meta,
#sb-main .cm-editor .sb-line-h3 .sb-meta { font-weight: 500; }

#sb-main .cm-editor .sb-strong { font-weight: 650; color: var(--editor-heading-color); }
#sb-main .cm-editor .sb-emphasis { font-style: italic; }

/* inline code */
#sb-main .cm-editor .sb-code:not(.sb-line-fenced-code .sb-code) {
  font-family: var(--au-mono);
  font-size: .86em;
  background: var(--au-surface-2);
  border: 1px solid var(--au-border);
  border-radius: 6px;
  padding: 1px 5px;
}

/* highlight: marker-pen look */
#sb-main .cm-editor .sb-highlight {
  background: linear-gradient(transparent 38%, var(--editor-highlight-background-color) 38%, var(--editor-highlight-background-color) 92%, transparent 92%);
  border-radius: 2px;
  padding: 0 2px;
}

/* links */
#sb-main .cm-editor .sb-wiki-link,
#sb-main .cm-editor a.sb-wiki-link {
  font-weight: 550;
  margin: 0;
  padding: 0;
  border-radius: 0;
  text-decoration: none;
  background-image: linear-gradient(var(--au-accent-ring), var(--au-accent-ring));
  background-size: 100% 1.5px;
  background-position: 0 100%;
  background-repeat: no-repeat;
  transition: background-size .2s ease, color .2s ease;
}
#sb-main .cm-editor .sb-wiki-link:hover {
  background-image: linear-gradient(var(--au-accent-soft), var(--au-accent-soft));
  background-size: 100% 100%;
}
#sb-main .cm-editor .sb-wiki-link-missing .sb-wiki-link,
#sb-main .cm-editor a.sb-wiki-link-missing {
  background-image: none;
  text-decoration: underline dashed 1.5px;
  text-underline-offset: 4px;
  text-decoration-color: color-mix(in srgb, var(--editor-wiki-link-page-missing-color) 55%, transparent);
}
#sb-main .cm-editor .sb-link:not(.sb-meta) {
  color: var(--au-accent);
  text-decoration: underline 1.5px;
  text-decoration-color: var(--au-accent-ring);
  text-underline-offset: 4px;
}

/* hashtags as pills */
#sb-main .cm-editor .sb-hashtag {
  border-radius: 999px;
  padding: 1px 9px;
  font-size: .78em;
  font-weight: 600;
  letter-spacing: .01em;
  vertical-align: 1px;
}

/* ───────────────────────── Lists & tasks ───────────────────────── */
#sb-main .cm-editor .cm-list-bullet { font-weight: 700; }
#sb-main .cm-editor .sb-line-ol .cm-list-bullet { font-variant-numeric: tabular-nums; color: var(--au-muted); font-weight: 600; }

:is(#sb-main .cm-editor input.sb-checkbox, #sb-main .cm-editor .sb-checkbox input[type="checkbox"], .sb-nav-content input[type="checkbox"], .sb-markdown-widget input[type="checkbox"]) {
  appearance: none;
  -webkit-appearance: none;
  width: 17px;
  height: 17px;
  border-radius: 6px;
  border: 1.6px solid color-mix(in srgb, var(--au-muted) 70%, transparent);
  background: var(--au-surface);
  vertical-align: -3px;
  display: inline-grid;
  place-content: center;
  transition: all .15s ease;
  margin: 0;
}
:is(#sb-main .cm-editor input.sb-checkbox, #sb-main .cm-editor .sb-checkbox input[type="checkbox"], .sb-nav-content input[type="checkbox"], .sb-markdown-widget input[type="checkbox"]):hover {
  border-color: var(--au-accent);
  box-shadow: 0 0 0 3px var(--au-accent-soft);
}
:is(#sb-main .cm-editor input.sb-checkbox, #sb-main .cm-editor .sb-checkbox input[type="checkbox"], .sb-nav-content input[type="checkbox"], .sb-markdown-widget input[type="checkbox"]):checked {
  border-color: transparent;
  background: linear-gradient(135deg, var(--au-accent), var(--au-accent-2));
}
:is(#sb-main .cm-editor input.sb-checkbox, #sb-main .cm-editor .sb-checkbox input[type="checkbox"], .sb-nav-content input[type="checkbox"], .sb-markdown-widget input[type="checkbox"]):checked::after {
  content: "";
  width: 9px;
  height: 5px;
  border: 2px solid #fff;
  border-top: 0;
  border-right: 0;
  transform: rotate(-45deg) translate(1px, -1px);
}
#sb-main .cm-editor .sb-line-task:has(.cm-task-checked),
#sb-main .cm-editor .cm-task-checked { color: var(--au-muted); }
#sb-main .cm-editor .cm-task-checked { text-decoration-color: color-mix(in srgb, var(--au-muted) 70%, transparent) !important; }

/* ───────────────────────── Blockquote ───────────────────────── */
#sb-main .cm-editor .sb-line-blockquote {
  --blockquote-bar: 3px;
  background-image: linear-gradient(var(--au-accent), var(--au-accent-2));
  background-size: 3px 100%;
  background-repeat: no-repeat;
  background-color: color-mix(in srgb, var(--au-accent-soft) 45%, transparent);
  font-style: italic;
  font-size: 1.04em;
  padding-left: 22px !important;
  padding-right: 16px !important;
}
#sb-main .cm-editor .sb-line-blockquote:not(.sb-line-blockquote + .sb-line-blockquote) {
  border-top-right-radius: var(--au-radius); padding-top: 10px !important;
}
#sb-main .cm-editor .sb-line-blockquote:not(:has(+ .sb-line-blockquote)) {
  border-bottom-right-radius: var(--au-radius); padding-bottom: 10px !important;
}
#sb-main .cm-editor .sb-line-blockquote .sb-quote.sb-meta { color: transparent; }

/* ───────────────────────── Code blocks as cards ───────────────────────── */
#sb-main .cm-editor .sb-line-fenced-code {
  font-family: var(--au-mono);
  font-size: 14.5px;
  line-height: 1.7;
  padding-left: 20px !important;
  padding-right: 16px !important;
  border-left: 1px solid var(--au-border);
  border-right: 1px solid var(--au-border);
}
#sb-main .cm-editor .sb-line-fenced-code:not(.sb-line-fenced-code + .sb-line-fenced-code) {
  border-top: 1px solid var(--au-border);
  border-radius: var(--au-radius) var(--au-radius) 0 0;
  padding-top: 14px !important;
}
#sb-main .cm-editor .sb-line-fenced-code:not(:has(+ .sb-line-fenced-code)) {
  border-bottom: 1px solid var(--au-border);
  border-radius: 0 0 var(--au-radius) var(--au-radius);
  padding-bottom: 14px !important;
}
#sb-main .cm-editor .sb-line-code-outside { color: var(--au-muted); }
#sb-main .cm-editor .sb-code-info,
#sb-main .cm-editor .sb-code-copy-button { color: var(--au-muted); font-family: var(--au-mono); font-size: 12px; }
#sb-main .cm-editor .sb-keyword { color: var(--editor-code-operator-color); font-weight: 600; }

/* ───────────────────────── Tables ───────────────────────── */
#sb-main .cm-editor .sb-table-widget table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  border: 1px solid var(--au-border);
  border-radius: var(--au-radius);
  overflow: hidden;
  background: var(--au-surface);
  box-shadow: var(--au-shadow);
  font-size: .94em;
  margin: 6px 0;
}
#sb-main .cm-editor .sb-table-widget thead tr {
  background: var(--editor-table-head-background-color) !important;
  color: var(--au-muted) !important;
}
#sb-main .cm-editor .sb-table-widget thead td,
#sb-main .cm-editor .sb-table-widget th {
  font-size: .78em;
  font-weight: 650;
  text-transform: uppercase;
  letter-spacing: .07em;
  padding: 10px 16px !important;
  border-bottom: 1px solid var(--au-border);
}
#sb-main .cm-editor .sb-table-widget tbody td { padding: 10px 16px !important; }
#sb-main .cm-editor .sb-table-widget tbody tr + tr td { border-top: 1px solid color-mix(in srgb, var(--au-border) 60%, transparent); }
#sb-main .cm-editor .sb-table-widget tbody tr:nth-child(even) { background: var(--editor-table-even-background-color); }
#sb-main .cm-editor .sb-table-widget tbody tr:hover { background: var(--au-accent-soft); }

/* ───────────────────────── Horizontal rule ───────────────────────── */
#sb-main .cm-editor .sb-line-hr {
  border-top: 0;
  padding: 1.4em 0 .4em;
  background: linear-gradient(90deg, transparent, var(--au-border) 20%, var(--au-accent-ring) 50%, var(--au-border) 80%, transparent) no-repeat 0 1.4em / 100% 1px;
}

/* ───────────────────────── Page widgets (linked mentions, tasks…) ───────────────────────── */
.sb-page-widget {
  border: 1px solid var(--au-border) !important;
  border-radius: var(--au-radius) !important;
  background: var(--au-surface);
  box-shadow: var(--au-shadow);
  overflow: hidden;
  margin: 4px 0 18px !important;
}
.sb-page-widget-bar {
  background: transparent !important;
  border-bottom: 1px solid var(--au-border);
  padding: 9px 14px !important;
  border-radius: 0 !important;
}
.sb-page-widget-title {
  font-family: var(--ui-font);
  font-size: 12px;
  font-weight: 650;
  text-transform: uppercase;
  letter-spacing: .08em;
  color: var(--au-muted);
}
.sb-page-widget-fold { color: var(--au-muted); background: transparent; border: 0; }
.sb-page-widget-tools button { color: var(--au-muted); border-radius: 7px; background: transparent; border: 0; }
.sb-page-widget-tools button:hover { color: var(--au-accent); background: var(--au-accent-soft); }
.sb-page-widget .sb-nav-content { padding: 12px 18px !important; font-size: 15px; line-height: 1.6; }
.sb-page-widget .sb-nav-content ul { padding-left: 1.1em !important; }
.sb-page-widget .sb-nav-content a.wiki-link { font-weight: 550; }
.sb-page-widget .sb-nav-content input[type="checkbox"] { vertical-align: -3px !important; margin-right: .5em !important; }

/* ───────────────────────── Modal / page picker / command palette ───────────────────────── */
.sb-modal-backdrop {
  backdrop-filter: blur(4px) saturate(120%);
  -webkit-backdrop-filter: blur(4px) saturate(120%);
}
.sb-modal,
.sb-modal-box {
  border-radius: 18px !important;
  border: 1px solid var(--modal-border-color) !important;
  box-shadow: var(--au-shadow-lg) !important;
  overflow: hidden;
}
.sb-modal.sb-modal-centered { max-width: 680px !important; margin-inline: auto !important; top: 96px !important; }
.sb-nav-root-modal,
.sb-modal-box {
  background: color-mix(in srgb, var(--au-surface) 94%, transparent) !important;
  backdrop-filter: blur(24px) saturate(160%);
  -webkit-backdrop-filter: blur(24px) saturate(160%);
}
.sb-nav-root { font-size: 15px; }
.sb-nav-root-modal .sb-nav-header {
  padding: 16px 16px 12px !important;
  gap: 12px !important;
  border-bottom: 1px solid var(--au-border) !important;
}
.sb-nav-root-modal .sb-nav-header-row { align-items: center; gap: 8px; }
.sb-nav-root-modal .sb-nav-header .sb-nav-title {
  color: var(--au-accent);
  font-weight: 700;
  font-size: 17px;
}
.sb-nav-root-modal .sb-nav-input { box-shadow: none !important; font-size: 18px; font-weight: 500; letter-spacing: -0.01em; }
.sb-nav-root-modal .sb-nav-input::placeholder { color: var(--au-muted); opacity: .7; }
.sb-nav-header button, .sb-nav-close, .sb-dock-button {
  color: var(--au-muted); border-radius: 8px; border: 0; background: transparent;
}
.sb-nav-header button:hover { color: var(--au-accent); background: var(--au-accent-soft); }

.sb-segments {
  background: var(--au-surface-2) !important;
  border-radius: 10px !important;
  padding: 3px !important;
  gap: 2px;
}
.sb-segment {
  border-radius: 7px !important;
  padding: 4px 10px !important;
  font-weight: 550;
  transition: background .15s ease, color .15s ease;
}
.sb-segment-active {
  background: var(--au-surface) !important;
  color: var(--au-text) !important;
  box-shadow: 0 1px 2px rgba(0,0,0,.08), 0 0 0 1px var(--au-border);
}
html[data-theme="dark"] .sb-segment-active { background: var(--au-border) !important; }

.sb-nav-help {
  border-bottom: 0 !important;
  padding: 8px 18px 2px !important;
  font-size: 12px !important;
  color: var(--au-muted) !important;
}
.sb-nav-root-modal .sb-nav-body { padding: 6px 8px 8px; }
.sb-nav-root-modal .sb-nav-row {
  border-radius: 10px;
  padding: 8px 10px;
  align-items: center;
  transition: background .12s ease;
}
.sb-nav-root-modal .sb-nav-row:hover:not(.sb-nav-selected) { background: color-mix(in srgb, var(--au-surface-2) 70%, transparent); }
.sb-nav-root-modal .sb-nav-selected {
  background: var(--au-accent-soft) !important;
  color: var(--au-text) !important;
}
.sb-nav-root-modal .sb-nav-icon { color: var(--au-muted); }
.sb-nav-root-modal .sb-nav-selected .sb-nav-icon { color: var(--au-accent); }
.sb-nav-create { border-top: 1px solid var(--au-border) !important; }
.sb-nav-root .sb-hint, .sb-nav-root .sb-nav-chip-hint, .sb-nav-root .sb-nav-trailing .sb-nav-chip {
  border-radius: 999px !important;
  font-size: 12px;
  font-weight: 600;
  padding: 2px 10px;
}
.sb-nav-chip.sb-hashtag { border-radius: 999px !important; padding: 0 8px !important; font-weight: 600; }

/* legacy modal box (prompts, confirms) */
.sb-modal-box { margin-top: 96px; font-family: var(--ui-font); }
.sb-modal-box .sb-header { padding: 16px 18px 12px; font-size: 17px; }
.sb-modal-box .sb-header .sb-input, .sb-modal-box .sb-input { font-family: var(--ui-font); font-size: 17px; }
.sb-modal-box .sb-option, .sb-modal-box .sb-selected-option { border-radius: 10px; margin: 2px 8px; }

/* ───────────────────────── Notifications & buttons ───────────────────────── */
.sb-notifications > div {
  border-radius: var(--au-radius);
  box-shadow: var(--au-shadow-lg);
  backdrop-filter: blur(16px);
}
.sb-button, button.sb-button-primary { border-radius: 10px; font-family: var(--ui-font); font-weight: 550; }

/* scrollbars */
::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-thumb { background: color-mix(in srgb, var(--au-muted) 35%, transparent); border-radius: 999px; border: 3px solid transparent; background-clip: padding-box; }
::-webkit-scrollbar-track { background: transparent; }
::selection { background: var(--editor-selection-background-color); }

/* ───────────────────────── Small screens ───────────────────────── */
@media (max-width: 600px) {
  #sb-main .cm-editor { font-size: 16px; }
  #sb-main .cm-editor .cm-content { padding-top: 18px; }
  #sb-main .cm-editor .sb-line-h1 { font-size: 1.8em; }
  #sb-main .cm-editor .sb-line-h2 { font-size: 1.3em; }
  #sb-top .main .inner { font-size: 19px; }
  .sb-modal.sb-modal-centered { top: 64px !important; border-radius: 14px !important; }
}
```
