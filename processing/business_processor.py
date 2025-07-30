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

parser = argparse.ArgumentParser(description="Analyse des ventes web")
parser.add_argument('--input', required=True, help="Fichier CSV des ventes utilisateur")
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

# ============================
# 🧹 Nettoyage
# ============================
from transformations.data_cleaner import clean_user_data
df = clean_user_data(df)
print("🧹 Nettoyage OK")
# ============================
# ✨ Enrichissement
# ============================
from transformations.data_enricher import enrich_user_data
df = enrich_user_data(df,input_path)
print("✨ Enrichissement OK")
# ============================
# 📊 Agrégation
# ============================
from transformations.data_aggregator import aggregate_user_data
df_agg = aggregate_user_data(df)
print("📊 Agrégation OK")
# ============================
# 💾 Export partitionné
# ============================

from transformations.data_formatter import export_user_data_partitioned
export_user_data_partitioned(df_agg, input_path)
print("💾 Export OK")
print("✅ Traitement des ventes terminé.")
sys.exit(0)