#!/usr/bin/env python3
# Analyse des rapports qualité et simulation d'alerte email enrichie


import os
import sys
import json
from datetime import datetime

QUALITY_DIR = os.path.join(os.path.dirname(__file__), "../data/quality")
ALERT_FILE = os.path.join(QUALITY_DIR, "quality_alert.txt")
EMAIL_DEST = "tanouti.jaouad@labom2iformation.fr"

failed_reports = []

# Parcours des fichiers de validation
for file in os.listdir(QUALITY_DIR):
    if file.startswith("validation_report_") and file.endswith(".json"):
        path = os.path.join(QUALITY_DIR, file)
        with open(path, "r") as f:
            try:
                report = json.load(f)
                if report.get("status") == "failed":
                    failed_reports.append(report)
            except:
                continue

# Génération d'une alerte si nécessaire
if failed_reports:
    with open(ALERT_FILE, "w") as alert:
        alert.write("🚨 ALERTE QUALITÉ - ÉCHEC DÉTECTÉ\n")
        alert.write(f"Date : {datetime.utcnow().isoformat()}Z\n")
        alert.write(f"Destinataire simulé : {EMAIL_DEST}\n\n")
        for r in failed_reports:
            alert.write(f"❌ {r['filename']}\n")
            alert.write(f"   - Complétude : {r['completeness']}% (Seuil : {r['threshold']}%)\n")
            if r.get("errors"):
                for err in r["errors"]:
                    alert.write(f"   - 📌 {err}\n")
            alert.write("\n")
    
    print(f"📩 Alerte générée : {ALERT_FILE}")
else:
    print("✅ Tous les fichiers ont passé les contrôles qualité.")
if failed_reports:
    sys.exit(1)
else:
    sys.exit(0)