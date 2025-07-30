# transformations/data_aggregator.py

import pandas as pd
from typing import List

def aggregate_api_logs(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrège les logs API par date, catégorie, méthode, pays
    """
    df_agg = df.groupby(["date", "category", "method", "country_code"]).agg(
        count_requests=("request_id", "count"),
        avg_response_time_ms=("response_time_ms", "mean"),
        avg_payload_bytes=("payload_size_bytes", "mean"),
        nb_cache_hits=("cache_hit", "sum")
    ).reset_index()
    return df_agg


def aggregate_session_data(df: pd.DataFrame, dimensions: List[str]) -> pd.DataFrame:
    """
    Agrégation des sessions utilisateur selon les dimensions fournies.
    """
    if "date" not in dimensions:
        dimensions = ["date"] + dimensions
    if not set(dimensions).issubset(df.columns):
        missing = list(set(dimensions) - set(df.columns))
        raise ValueError(f"Colonnes manquantes pour l'aggrégation : {missing}")

    grouped = df.groupby(dimensions).agg(
        nb_sessions=('session_id', 'count'),
        avg_duration_min=('duration_min', 'mean'),
        avg_pages_visited=('pages_visited', 'mean'),
        avg_products_viewed=('products_viewed', 'mean'),
        avg_products_added=('products_added_to_cart', 'mean'),
        conversion_rate=('is_conversion', 'mean'),
        bounce_rate=('is_bounce', 'mean'),
        avg_total_spent=('total_spent', 'mean'),
        cart_abandonment_rate=('abandoned_cart', 'mean')
    ).reset_index()

    return grouped

import pandas as pd

import pandas as pd

def aggregate_product_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrège les données produits par date, catégorie et état de stock.
    """
    required_columns = [
        "date", "category", "stock_status", "is_active",
        "price", "cost", "margin_pct", "rating", "review_count"
    ]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"❌ Colonne manquante : {col}")

    grouped = df.groupby(["date", "category", "stock_status", "is_active"]).agg(
        nb_products=('product_id', 'count'),
        avg_price=('price', 'mean'),
        avg_cost=('cost', 'mean'),
        avg_margin_pct=('margin_pct', 'mean'),
        avg_rating=('rating', 'mean'),
        avg_review_count=('review_count', 'mean')
    ).reset_index()

    return grouped


def aggregate_user_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrège les données utilisateurs par pays, type de client et statut premium.
    """
    required_columns = [
        "country", "customer_type", "is_premium",
        "age", "total_orders", "total_spent",
        "loyalty_score", "days_since_last_login"
    ]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"❌ Colonne manquante : {col}")

    grouped = df.groupby(["country", "customer_type", "is_premium"]).agg(
        nb_users=("user_id", "count"),
        avg_age=("age", "mean"),
        avg_total_orders=("total_orders", "mean"),
        avg_total_spent=("total_spent", "mean"),
        avg_loyalty_score=("loyalty_score", "mean"),
        avg_days_since_login=("days_since_last_login", "mean"),
    ).reset_index()

    return grouped
