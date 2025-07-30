#!/usr/bin/env python3
# Analyse des sessions utilisateur (lecture, nettoyage, enrichissement, agrégation, export)

import sys
import argparse
import pandas as pd
import os
from datetime import datetime

# 📁 Ajout du chemin racine pour import relatif
pipeline_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, pipeline_root)

# ==============================
# 🎯 Argument en ligne de commande
# ==============================

parser = argparse.ArgumentParser(description="Analyse des sessions web")
parser.add_argument('--input', required=True, help="Fichier CSV des sessions utilisateur")
args = parser.parse_args()
input_path = args.input

# ==============================
# 📥 Lecture du fichier
# ==============================

if not os.path.exists(input_path):
    print(f"❌ Fichier introuvable : {input_path}")
    sys.exit(1)

try:
    df = pd.read_csv(input_path)
except Exception as e:
    print(f"❌ Erreur de lecture CSV : {e}")
    sys.exit(1)

# ==============================
# 🧹 Nettoyage
# ==============================

from transformations.data_cleaner import clean_session_data
df = clean_session_data(df)

# ==============================
# 🧠 Enrichissement
# ==============================

from transformations.data_enricher import enrich_session_data
df = enrich_session_data(df,input_path)

# ==============================
# 📊 Agrégation
# ==============================

from transformations.data_aggregator import aggregate_session_data
# Liste des dimensions disponibles dans le fichier de sessions
dimensions = ["device_type", "browser", "referrer", "country", "city", "conversion"]

# Appel correct
df_agg = aggregate_session_data(df, dimensions)

# ==============================
# 💾 Export partitionné
# ==============================

from transformations.data_formatter import export_session_data_partitioned
export_session_data_partitioned(df_agg, input_path)

print("✅ Traitement des sessions terminé.")
sys.exit(0)
