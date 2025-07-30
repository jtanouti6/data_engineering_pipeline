#!/usr/bin/env python3
# Génère un tableau HTML à partir des rapports qualité JSON

import os
import json

QUALITY_DIR = os.path.join(os.path.dirname(__file__), "../data/quality")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "../data/quality/dashboard.html")

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

rows = []

for file in os.listdir(QUALITY_DIR):
    if file.startswith("validation_report_") and file.endswith(".json"):
        path = os.path.join(QUALITY_DIR, file)
        with open(path) as f:
            try:
                report = json.load(f)
                rows.append({
                    "filename": report.get("filename", ""),
                    "completeness": report.get("completeness", 0),
                    "threshold": report.get("threshold", 0),
                    "status": report.get("status", "unknown"),
                    "errors": report.get("errors", [])
                })
            except:
                continue

# Construction du tableau HTML
html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Rapport Qualité - Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
        table { border-collapse: collapse; width: 100%; background: white; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        thead th {
            background-color: #eeeeee;
            position: sticky;
            top: 0;
            z-index: 2;
        }
        .passed { background-color: #d4edda; }
        .failed { background-color: #f8d7da; }
        .error-list { color: #a94442; font-size: 0.9em; margin: 0; padding-left: 15px; }
    </style>
</head>
<body>
    <h1>📊 Dashboard de Qualité des Données</h1>
    <table>
        <thead>
            <tr>
                <th>Fichier</th>
                <th>Complétude (%)</th>
                <th>Seuil</th>
                <th>Statut</th>
                <th>Erreurs</th>
            </tr>
        </thead>
        <tbody>
"""

for r in rows:
    status_class = "passed" if r["status"] == "passed" else "failed"
    html += f"<tr class='{status_class}'>"
    html += f"<td>{r['filename']}</td>"
    html += f"<td>{r['completeness']}</td>"
    html += f"<td>{r['threshold']}</td>"
    html += f"<td>{r['status'].capitalize()}</td>"
    html += "<td><ul class='error-list'>" + "".join([f"<li>{e}</li>" for e in r["errors"] or []]) + "</ul></td>"
    html += "</tr>"

html += """        </tbody>
    </table>
</body>
</html>
"""

# Écriture du fichier
with open(OUTPUT_FILE, "w") as f:
    f.write(html)

print(f"✅ Dashboard HTML généré : {OUTPUT_FILE}")
