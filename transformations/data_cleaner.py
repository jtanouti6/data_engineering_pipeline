import pandas as pd

def clean_api_logs(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoyage des logs API : suppression erreurs, nulls, doublons
    """
    df = df[df["status_code"] != 500]
    df = df.drop_duplicates(subset=["request_id"])
    df = df.dropna()
    return df

def clean_session_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoyage des données de session :
    - Suppression des lignes avec session_id, start_time ou end_time manquants
    - Conversion robuste des timestamps
    - Suppression des lignes avec timestamps invalides
    """

    # Supprimer les lignes sans identifiants essentiels
    df = df.dropna(subset=['session_id', 'start_time', 'end_time'])

    # Conversion des timestamps
    df['start_time'] = pd.to_datetime(df['start_time'], errors='coerce')
    df['end_time'] = pd.to_datetime(df['end_time'], errors='coerce')

    # Supprimer les lignes avec timestamps invalides
    df = df.dropna(subset=['start_time', 'end_time'])

    return df

def clean_product_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoyage des données produits :
    - Suppression des produits sans identifiant, prix ou stock
    - Suppression des doublons sur product_id
    - Normalisation des types de données
    """
    df = df.dropna(subset=["product_id", "price", "stock"])
    df = df.drop_duplicates(subset=["product_id"])

    # Conversions de types
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["cost"] = pd.to_numeric(df["cost"], errors="coerce")
    df["stock"] = pd.to_numeric(df["stock"], errors="coerce")
    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

    df = df.dropna(subset=["price", "cost", "stock", "created_at"])

    return df

# transformations/data_cleaner.py


def clean_user_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoyage des données utilisateurs :
    - Suppression des doublons
    - Conversion des dates
    - Gestion des valeurs manquantes
    - Uniformisation des types
    """
    df = df.drop_duplicates(subset=["user_id"])
    
    # Conversion des dates
    df["registration_date"] = pd.to_datetime(df["registration_date"], errors="coerce")
    df["last_login"] = pd.to_datetime(df["last_login"], errors="coerce")

    # Gestion des valeurs manquantes
    df = df.dropna(subset=["user_id", "registration_date", "last_login"])
    
    # Conversion des types
    df["is_premium"] = df["is_premium"].astype(bool)
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["total_orders"] = pd.to_numeric(df["total_orders"], errors="coerce")
    df["total_spent"] = pd.to_numeric(df["total_spent"], errors="coerce")

    return df
