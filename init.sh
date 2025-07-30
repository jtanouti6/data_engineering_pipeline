#!/bin/bash

# Script d'initialisation de l'arborescence du projet data_engineering_pipeline

set -e

BASE_DIR="data_engineering_pipeline"

echo "Création de l'arborescence du projet dans $BASE_DIR..."

mkdir -p $BASE_DIR/{orchestration,processing,transformations,data/{raw,staging,processed,quality,archive},config,monitoring}

# Fichiers de scripts Bash (orchestration)
touch $BASE_DIR/orchestration/{pipeline_master.sh,data_discovery.sh,worker_manager.sh,quality_monitor.sh,resource_monitor.sh}

# Fichiers de traitement Python (processing)
touch $BASE_DIR/processing/{api_log_processor.py,session_analyzer.py,business_calculator.py,data_validator.py,data_enricher.py}

# Fichiers de transformation Python (transformations)
touch $BASE_DIR/transformations/{data_cleaner.py,data_joiner.py,data_aggregator.py,data_formatter.py}

# Fichiers de configuration (config)
touch $BASE_DIR/config/{data_schemas.json,business_rules.yaml,quality_thresholds.yaml,pipeline_config.yaml}

# Scripts de monitoring (monitoring)
touch $BASE_DIR/monitoring/{data_metrics.py,alert_manager.py,dashboard_gen.py}


# 🔧 Réinitialise les droits sur tous les fichiers et dossiers du projet

echo "🔐 Réinitialisation des permissions sur le projet..."

# Droits sur les dossiers : 755
find . -type d -exec chmod 755 {} \;

# Droits sur les fichiers : 755
find . -type f -exec chmod 755 {} \;

# Mettre au format unix
find . -type f -exec dos2unix {} \;

echo "✅ Permissions réinitialisées à 755 pour tous les fichiers et dossiers."


echo "✅ Structure de projet initialisée avec succès !"

