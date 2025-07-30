# product_processor.py

import argparse
import os
import sys
import pandas as pd

# 📁 Ajout du chemin racine pour import relatif
pipeline_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, pipeline_root)

# === CLI ===
parser = argparse.ArgumentParser(description="Traitement des données produits")
parser.add_argument('--input', required=True, help="Fichier CSV ou Excel contenant les données produits")
args = parser.parse_args()
input_path = args.input

# === Lecture ===
if not os.path.exists(input_path):
    print(f"❌ Fichier introuvable : {input_path}")
    sys.exit(1)

try:
    if input_path.endswith(".csv"):
        df = pd.read_csv(input_path)
    elif input_path.endswith(".xlsx"):
        df = pd.read_excel(input_path)
    else:
        raise ValueError("Format de fichier non supporté (CSV ou XLSX attendu)")
except Exception as e:
    print(f"❌ Erreur de lecture du fichier : {e}")
    sys.exit(1)

# ==============================
# 🧹 Nettoyage
# ==============================
from transformations.data_cleaner import clean_product_data
df = clean_product_data(df)
print("✅ Lecture et nettoyage effectués.")
# ==============================
# 🧠 Enrichissement
# ==============================

from transformations.data_enricher import enrich_product_data
df = enrich_product_data(df,input_path)

# ==============================
# 📊 Agrégation
# ==============================

from transformations.data_aggregator import aggregate_product_data
df_agg = aggregate_product_data(df)
# ==============================
# 💾 Export partitionné
# ==============================
from transformations.data_formatter import export_product_data_partitioned
export_product_data_partitioned(df_agg, input_path)

print("✅ Traitement des produits terminé.")
sys.exit(0)


