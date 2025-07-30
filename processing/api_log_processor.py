#!/usr/bin/env python3
# Traitement des logs API - version modulaire

import os
import sys
import argparse
import pandas as pd
from datetime import datetime

# Ajout du chemin racine pour import des modules de transformations
pipeline_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, pipeline_root)


# ==============================
# 🔁 Traitements en modules
# ==============================
from transformations.data_cleaner import clean_api_logs
from transformations.data_enricher import enrich_api_logs
from transformations.data_aggregator import aggregate_api_logs
from transformations.data_formatter import export_api_logs_partitioned



# ==============================
# 🎯 Arguments CLI
# ==============================
parser = argparse.ArgumentParser(description="Traitement des logs API")
parser.add_argument('--input', required=True, help="Fichier JSON des logs API (ligne par ligne)")
args = parser.parse_args()
input_path = args.input

# ==============================
# 📥 Lecture du fichier JSON
# ==============================
if not os.path.exists(input_path):
    print(f"❌ Fichier introuvable : {input_path}")
    sys.exit(1)

try:
    df = pd.read_json(input_path)  # JSON liste (pas lines=True)
except Exception as e:
    print(f"❌ Erreur de lecture JSON : {e}")
    sys.exit(1)


df = clean_api_logs(df)
df = enrich_api_logs(df,input_path)
df_agg = aggregate_api_logs(df)
export_api_logs_partitioned(df_agg, input_path)
