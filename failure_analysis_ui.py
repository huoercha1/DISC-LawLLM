import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Failure Analysis Dashboard", layout="wide")

st.markdown(
    """
    <style>
        :root {
            --purple-100: #f5f3ff;
            --purple-200: #ede9fe;
            --purple-300: #ddd6fe;
            --purple-500: #8b5cf6;
            --purple-600: #7c3aed;
            --slate-50: #f8fafc;
            --slate-100: #f1f5f9;
            --slate-200: #e2e8f0;
            --slate-500: #64748b;
            --slate-700: #334155;
            --slate-900: #0f172a;
            --rose-500: #f43f5e;
            --rose-600: #e11d48;
            --amber-400: #facc15;
            --sky-400: #38bdf8;
            --emerald-500: #10b981;
        }

        .stApp {
            background: linear-gradient(180deg, #faf7ff 0%, #f7f6ff 100%);
        }

        .main .block-container {
            padding-top: 2.5rem;
            padding-bottom: 3rem;
            max-width: 1200px;
        }

        .dashboard-header {
            display: flex;
            justify-content: space-between;
            gap: 1.5rem;
            align-items: flex-start;
            margin-bottom: 1.5rem;
        }

        .dashboard-header h1 {
            font-size: 2rem;
            color: var(--slate-900);
            margin: 0.35rem 0 0 0;
            display: flex;
            gap: 0.5rem;
            align-items: center;
        }

        .dashboard-header h1 span {
            font-size: 1.1rem;
            font-weight: 500;
            color: var(--slate-500);
        }

        .header-eyebrow {
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--purple-600);
            text-transform: uppercase;
            letter-spacing: 0.18em;
        }

        .header-subtitle {
            color: var(--slate-500);
            margin-top: 0.65rem;
            font-size: 0.95rem;
        }

        .header-actions {
            display: flex;
            gap: 0.75rem;
        }

        .pill-button {
            background: white;
            color: var(--slate-700);
            border: 1px solid var(--purple-200);
            padding: 0.65rem 1.25rem;
            border-radius: 999px;
            font-weight: 600;
            font-size: 0.95rem;
            box-shadow: 0 1px 2px rgba(15, 23, 42, 0.08);
            cursor: pointer;
        }

        .pill-button.primary {
            background: linear-gradient(135deg, #f97316, #ef4444);
            color: white;
            border: none;
            box-shadow: 0 10px 18px -12px rgba(239, 68, 68, 0.8);
        }

        .card {
            background: white;
            border-radius: 20px;
            padding: 1.75rem;
            border: 1px solid var(--purple-200);
            box-shadow: 0 18px 30px -24px rgba(30, 41, 59, 0.45);
            margin-bottom: 1.5rem;
        }

        .card-header {
            font-size: 0.85rem;
            font-weight: 700;
            color: var(--purple-600);
            text-transform: uppercase;
            letter-spacing: 0.14em;
            margin-bottom: 1.2rem;
        }

        .meta-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
            gap: 1rem;
        }

        .meta-item {
            background: var(--purple-100);
            border-radius: 16px;
            padding: 1rem;
            border: 1px solid var(--purple-200);
        }

        .meta-label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            color: var(--slate-500);
            margin-bottom: 0.4rem;
        }

        .meta-value {
            font-size: 1rem;
            font-weight: 600;
            color: var(--slate-900);
            word-break: break-word;
        }

        .status-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            font-weight: 600;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.16em;
            padding: 0.4rem 0.9rem;
            border-radius: 999px;
            background: rgba(244, 63, 94, 0.1);
            color: var(--rose-600);
            border: 1px solid rgba(244, 63, 94, 0.25);
        }

        .status-row {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 1.4rem;
        }

        .status-caption {
            color: var(--slate-500);
            font-size: 0.9rem;
        }

        .highlight {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(16, 185, 129, 0.08);
            border: 1px solid rgba(16, 185, 129, 0.2);
            color: var(--emerald-500);
            border-radius: 999px;
            padding: 0.4rem 0.85rem;
            font-weight: 600;
            font-size: 0.85rem;
        }

        .tag-label {
            font-size: 0.78rem;
            color: var(--slate-500);
            text-transform: uppercase;
            letter-spacing: 0.14em;
        }

        .log-container {
            background: var(--slate-900);
            border-radius: 16px;
            padding: 1.2rem 1.4rem;
            border: 1px solid rgba(148, 163, 184, 0.35);
            font-family: "Source Code Pro", "SFMono-Regular", Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
            color: var(--slate-50);
            max-height: 320px;
            overflow: auto;
            box-shadow: inset 0 0 0 1px rgba(15, 23, 42, 0.35);
        }

        .log-section {
            color: var(--amber-400);
            font-weight: 600;
            margin: 0.8rem 0 0.5rem;
            text-transform: uppercase;
            letter-spacing: 0.16em;
            font-size: 0.8rem;
        }

        .log-line {
            display: grid;
            grid-template-columns: 120px 90px 1fr;
            gap: 1rem;
            font-size: 0.82rem;
            align-items: baseline;
            padding: 0.18rem 0;
            border-bottom: 1px solid rgba(148, 163, 184, 0.12);
        }

        .log-line:last-child {
            border-bottom: none;
        }

        .log-time {
            color: rgba(248, 250, 252, 0.62);
        }

        .log-level {
            text-transform: uppercase;
            letter-spacing: 0.16em;
            font-weight: 600;
        }

        .log-level.info {
            color: var(--sky-400);
        }

        .log-level.warn {
            color: var(--amber-400);
        }

        .log-level.error {
            color: var(--rose-500);
        }

        .log-message {
            color: rgba(241, 245, 249, 0.94);
            line-height: 1.5;
        }

        .side-stack {
            display: flex;
            flex-direction: column;
            gap: 1.2rem;
        }

        .info-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: var(--purple-100);
            border-radius: 14px;
            padding: 0.85rem 1rem;
            border: 1px solid var(--purple-200);
            margin-bottom: 0.65rem;
        }

        .info-label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            color: var(--slate-500);
        }

        .info-value {
            font-size: 1rem;
            font-weight: 600;
            color: var(--slate-900);
        }

        .warning-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.35rem 0.75rem;
            border-radius: 999px;
            background: rgba(234, 179, 8, 0.12);
            color: #ca8a04;
            border: 1px solid rgba(234, 179, 8, 0.25);
            font-size: 0.8rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.16em;
        }

        .primary-link {
            display: inline-flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #a855f7, #6366f1);
            color: white !important;
            padding: 0.85rem;
            border-radius: 12px;
            text-decoration: none;
            font-weight: 600;
            transition: transform 0.1s ease, box-shadow 0.1s ease;
            box-shadow: 0 12px 18px -14px rgba(99, 102, 241, 0.9);
            margin-top: 0.5rem;
        }

        .primary-link:hover {
            transform: translateY(-2px);
            box-shadow: 0 14px 22px -12px rgba(99, 102, 241, 0.9);
        }

        .download-group {
            display: flex;
            flex-direction: column;
            gap: 0.85rem;
        }

        .download-item {
            background: var(--purple-100);
            border-radius: 14px;
            padding: 0.9rem 1rem;
            border: 1px solid var(--purple-200);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .download-item .download-meta {
            font-size: 0.8rem;
            color: var(--slate-500);
            margin-top: 0.2rem;
        }

        .ghost-button {
            padding: 0.4rem 0.9rem;
            border-radius: 999px;
            border: 1px solid var(--purple-300);
            color: var(--purple-600) !important;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.85rem;
            background: rgba(139, 92, 246, 0.12);
        }

        .action-list {
            list-style: none;
            padding: 0;
            margin: 0;
            display: grid;
            gap: 0.75rem;
        }

        .action-list li {
            background: var(--purple-100);
            border-radius: 14px;
            padding: 0.85rem 1rem;
            border: 1px solid var(--purple-200);
        }

        .action-list strong {
            display: block;
            font-size: 0.9rem;
            margin-bottom: 0.35rem;
        }

        .action-meta {
            font-size: 0.78rem;
            color: var(--slate-500);
        }

        @media (max-width: 900px) {
            .dashboard-header {
                flex-direction: column;
                align-items: flex-start;
            }

            .header-actions {
                width: 100%;
                flex-wrap: wrap;
            }

            .header-actions .pill-button {
                flex: 1 1 auto;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

failure_snapshot = {
    "detected_at": datetime(2024, 9, 5, 16, 16, 35),
    "stage": "Model Evaluation",
    "strategy": "Token Generation",
    "fault_domain": "Output Token",
    "model": "copilot-eval-v2.3",
    "query_id": "query_20240905_161635_083203",
    "row_index": "sydney_trace_4f82a0b1c94e",
    "error_class": "ENDPOINT_TIMEOUT",
    "latency": "21152 ms",
    "confidence": 0.84,
}

header_html = f"""
<div class="dashboard-header">
    <div>
        <div class="header-eyebrow">Failure Analysis</div>
        <h1>Earliest Failure <span>(Preliminary)</span></h1>
        <div class="header-subtitle">Detected {failure_snapshot['detected_at'].strftime('%b %d, %Y at %H:%M:%S UTC')} · Row {failure_snapshot['row_index']}</div>
    </div>
    <div class="header-actions">
        <button class="pill-button">Pause Submissions</button>
        <button class="pill-button">Switch Tenant</button>
        <button class="pill-button primary">Submit ICM</button>
    </div>
</div>
"""

st.markdown(header_html, unsafe_allow_html=True)

status_html = f"""
<div class="card">
    <div class="card-header">Failure Snapshot</div>
    <div class="status-row">
        <span class="status-pill">{failure_snapshot['error_class']}</span>
        <span class="status-caption">Latency {failure_snapshot['latency']} · Confidence {failure_snapshot['confidence']:.0%}</span>
    </div>
    <div class="meta-grid">
        <div class="meta-item">
            <div class="meta-label">Stage</div>
            <div class="meta-value">{failure_snapshot['stage']}</div>
        </div>
        <div class="meta-item">
            <div class="meta-label">Strategy</div>
            <div class="meta-value">{failure_snapshot['strategy']}</div>
        </div>
        <div class="meta-item">
            <div class="meta-label">Fault Domain</div>
            <div class="meta-value">{failure_snapshot['fault_domain']}</div>
        </div>
        <div class="meta-item">
            <div class="meta-label">Model</div>
            <div class="meta-value">{failure_snapshot['model']}</div>
        </div>
        <div class="meta-item">
            <div class="meta-label">Query ID</div>
            <div class="meta-value">{failure_snapshot['query_id']}</div>
        </div>
        <div class="meta-item">
            <div class="meta-label">Row Index</div>
            <div class="meta-value">{failure_snapshot['row_index']}</div>
        </div>
    </div>
</div>
"""

log_entries = [
    {"section": "Before Error"},
    {
        "time": "16:16:32.812",
        "level": "info",
        "message": "[router] Dispatching request query_20240905_161635_083203 to output-token endpoint",
    },
    {
        "time": "16:16:33.104",
        "level": "info",
        "message": "[output-token] Allocated generation worker node syd-gpu-14 for task",
    },
    {
        "time": "16:16:34.522",
        "level": "warn",
        "message": "[output-token] Stream stalled for 3000ms waiting on upstream tokeniser",
    },
    {
        "time": "16:16:35.189",
        "level": "warn",
        "message": "[router] Retrying token emission chunk=42 due to upstream silence",
    },
    {"section": "At Failure"},
    {
        "time": "16:16:35.743",
        "level": "error",
        "message": "[output-token] Generation deadline exceeded (deadline=20s, observed=21.1s)",
    },
    {
        "time": "16:16:35.744",
        "level": "error",
        "message": "[router] query_20240905_161635_083203 terminated with ENDPOINT_TIMEOUT",
    },
    {
        "time": "16:16:35.754",
        "level": "info",
        "message": "[alerts] Published failure notification to model-eval.sev3",
    },
    {"section": "After Error"},
    {
        "time": "16:16:36.012",
        "level": "warn",
        "message": "[recovery] Attempting cold restart of worker syd-gpu-14",
    },
    {
        "time": "16:16:37.481",
        "level": "info",
        "message": "[recovery] Worker restart completed in 1.4s",
    },
    {
        "time": "16:16:38.004",
        "level": "info",
        "message": "[router] Request queue backlog now at 0 pending submissions",
    },
]

log_html = "<div class=\"card\"><div class=\"card-header\">Logs (last 100 lines)</div><div class=\"log-container\">"
for entry in log_entries:
    if "section" in entry:
        log_html += f"<div class='log-section'>{entry['section']}</div>"
    else:
        log_html += (
            f"<div class='log-line'><span class='log-time'>{entry['time']}</span>"
            f"<span class='log-level {entry['level']}'>{entry['level']}</span>"
            f"<span class='log-message'>{entry['message']}</span></div>"
        )
log_html += "</div></div>"

related_incident = {
    "icm": "icm 680115452",
    "platform": "Failure Analysis Platform STMP",
    "eta": "~45 minutes",
    "dri": "SEVAL DRI",
    "slack_channel": "seval-oncall",
}

downloads = [
    {
        "name": "SEVAL scraping service",
        "meta": "Generated 2 minutes ago",
    },
    {
        "name": "Streaming gateway",
        "meta": "SLO report • 7 KB",
    },
    {
        "name": "Scoring pipeline",
        "meta": "All attachments",
        "full": True,
    },
]

suggested_actions = [
    {
        "title": "Assigned investigators",
        "description": f"{related_incident['dri']} · Escalate if unresolved in 30 minutes",
    },
    {
        "title": "Follow-on playbook",
        "description": "Validate endpoint healthcheck and re-run shadow traffic",
    },
    {
        "title": "Quick links",
        "description": "Service status page · Restart job · Debug runbook",
    },
]

incident_html = f"""
<div class="card">
    <div class="card-header">Related Incident</div>
    <div class="info-row">
        <div>
            <div class="info-label">ICM Ticket</div>
            <div class="info-value">{related_incident['icm']}</div>
        </div>
        <span class="warning-pill">Time to mitigate · {related_incident['eta']}</span>
    </div>
    <div class="info-row">
        <div>
            <div class="info-label">Analysis Platform</div>
            <div class="info-value">{related_incident['platform']}</div>
        </div>
        <div>
            <div class="info-label">Slack Channel</div>
            <div class="info-value">#{related_incident['slack_channel']}</div>
        </div>
    </div>
    <a class="primary-link" href="#">Open ICM Ticket</a>
</div>
"""

download_html = "<div class=\"card\"><div class=\"card-header\">Download Logs</div><div class=\"download-group\">"
for item in downloads:
    button_label = "Download all" if item.get("full") else "Download"
    download_html += (
        "<div class='download-item'>"
        f"<div><div class='info-value'>{item['name']}</div>"
        f"<div class='download-meta'>{item['meta']}</div></div>"
        f"<a class='ghost-button' href='#'>{button_label}</a>"
        "</div>"
    )
download_html += "</div></div>"

actions_html = "<div class=\"card\"><div class=\"card-header\">Suggested Actions</div><ul class=\"action-list\">"
for action in suggested_actions:
    actions_html += (
        "<li>"
        f"<strong>{action['title']}</strong>"
        f"<span class='action-meta'>{action['description']}</span>"
        "</li>"
    )
actions_html += "</ul></div>"

col_main, col_side = st.columns((2.3, 1), gap="large")

with col_main:
    st.markdown(status_html, unsafe_allow_html=True)
    st.markdown(log_html, unsafe_allow_html=True)

with col_side:
    st.markdown(incident_html, unsafe_allow_html=True)
    st.markdown(download_html, unsafe_allow_html=True)
    st.markdown(actions_html, unsafe_allow_html=True)
