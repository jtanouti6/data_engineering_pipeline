# transformations/data_formatter.py

import os
import pandas as pd

def export_api_logs_partitioned(df_agg: pd.DataFrame, input_path: str):
    """
    Écrit les fichiers agrégés dans /data/processed/api_logs/YYYY-MM-DD/
    """
    processed_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data", "processed", "api_logs")
    )
    os.makedirs(processed_root, exist_ok=True)

    for date_str in df_agg["date"].unique():
        partition_path = os.path.join(processed_root, date_str)
        os.makedirs(partition_path, exist_ok=True)

        df_day = df_agg[df_agg["date"] == date_str].drop(columns=["date"])
        output_file = os.path.join(partition_path, f"api_logs_{date_str}_kpi.csv")
        df_day.to_csv(output_file, index=False)
        # print(f"✅ Fichier généré : {output_file}")

def export_session_data_partitioned(df: pd.DataFrame, input_path: str, data_type: str = "sessions") -> None:
    """
    Exporte un DataFrame analysé vers un fichier CSV partitionné par date.

    Args:
        df (pd.DataFrame): DataFrame contenant une colonne 'date' pour partition.
        input_path (str): Chemin du fichier source (utilisé pour nommer le fichier de sortie).
        data_type (str): Type de données (par défaut : 'sessions', peut être 'api_logs'...).
    """

    if df.empty:
        print("⚠️  Le DataFrame est vide, aucun fichier généré.")
        return

    if "date" not in df.columns:
        raise ValueError("❌ La colonne 'date' est requise pour effectuer un export partitionné.")

    processed_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data", "processed", "sessions")
    )
    os.makedirs(processed_root, exist_ok=True)

    # Nom de base du fichier (ex: sessions_20250723.csv → sessions_20250723_aggregated.csv)
    base_name = os.path.basename(input_path).replace(".csv", "").replace(".json", "")
    output_base = f"{base_name}_aggregated.csv"

    # Export pour chaque date
    for date_str in df["date"].unique():
        partition_path = os.path.join(processed_root, date_str)
        os.makedirs(partition_path, exist_ok=True)

        df_day = df[df["date"] == date_str].drop(columns=["date"])
        output_path = os.path.join(partition_path, output_base)
        df_day.to_csv(output_path, index=False)

        # print(f"✅ Fichier généré : {output_path}")

def export_product_data_partitioned(df_agg: pd.DataFrame, input_path: str):
    """
    Export des données produits agrégées dans /data/processed/products/YYYY-MM-DD/
    """
    if "date" not in df_agg.columns:
        raise ValueError("❌ La colonne 'date' est requise pour effectuer un export partitionné.")

    processed_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data", "processed", "products")
    )
    os.makedirs(processed_root, exist_ok=True)

    for date_str in df_agg["date"].unique():
        partition_path = os.path.join(processed_root, date_str)
        os.makedirs(partition_path, exist_ok=True)

        df_day = df_agg[df_agg["date"] == date_str].drop(columns=["date"])
        output_file = os.path.join(partition_path, f"products_{date_str}_summary.csv")
        df_day.to_csv(output_file, index=False)
        # print(f"✅ Fichier généré : {output_file}")

def export_user_data_partitioned(df_agg: pd.DataFrame, input_path: str):
    """
    Exporte les données agrégées des utilisateurs dans /data/processed/users/<country>/...
    """
    if "country" not in df_agg.columns:
        raise ValueError("❌ La colonne 'country' est requise pour effectuer un export partitionné.")

    processed_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data", "processed", "sales")
    )
    os.makedirs(processed_root, exist_ok=True)

    for country in df_agg["country"].unique():
        partition_path = os.path.join(processed_root, country)
        os.makedirs(partition_path, exist_ok=True)

        df_country = df_agg[df_agg["country"] == country].drop(columns=["country"])
        output_file = os.path.join(partition_path, f"users_{country}_summary.csv")
        df_country.to_csv(output_file, index=False)
        # print(f"✅ Fichier généré : {output_file}")