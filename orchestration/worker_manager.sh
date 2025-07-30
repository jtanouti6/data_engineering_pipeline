#!/bin/bash
# Script de gestion des workers pour lancer les traitements Python

# Arguments attendus : nombre de workers en parallèle
NB_WORKERS="$1"
[ -z "$NB_WORKERS" ] && NB_WORKERS=1  # Valeur par défaut si non précisé

PIPELINE_ROOT="$(dirname "$0")/.."
STAGING_DIR="$PIPELINE_ROOT/data/staging"
LOG_FILE="$PIPELINE_ROOT/logs/pipeline.log"

echo "⚙️ Lancement des workers ($NB_WORKERS)..." | tee -a "$LOG_FILE"

# Vérifie que le dossier de staging contient des fichiers à traiter
FILES_TO_PROCESS=$(find "$STAGING_DIR" -type f)
if [ -z "$FILES_TO_PROCESS" ]; then
    echo "ℹ️ Aucun fichier à traiter dans staging/" | tee -a "$LOG_FILE"
    exit 0
fi

# Fonction locale pour déterminer le type de traitement à appliquer selon le nom du fichier
process_file() {
    file="$1"
    filename=$(basename "$file")

    echo "▶️  Traitement de $filename" | tee -a "$LOG_FILE"

    case "$filename" in
        api_logs_*.json)
            python3 "$PIPELINE_ROOT/processing/api_log_processor.py" --input "$file"
            ;;
        sessions_*.csv)
            python3 "$PIPELINE_ROOT/processing/session_processor.py" --input "$file" 
            ;;
        users_database.csv)
            python3 "$PIPELINE_ROOT/processing/business_processor.py" --input "$file"
            ;;
        products_catalog.csv|products_catalog.xlsx)
            python3 "$PIPELINE_ROOT/processing/product_processor.py" --input "$file"
            ;;
        *)
            echo "⚠️  Type de fichier inconnu ou non pris en charge : $filename" | tee -a "$LOG_FILE"
            ;;
    esac
}

# Utilisation de xargs pour exécuter les traitements en parallèle
export -f process_file
export PIPELINE_ROOT LOG_FILE

find "$STAGING_DIR" -type f | xargs -P "$NB_WORKERS" -I{} bash -c 'process_file "$@"' _ {}

echo "✅ Tous les fichiers ont été traités." | tee -a "$LOG_FILE"
