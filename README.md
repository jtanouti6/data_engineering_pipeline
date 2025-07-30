# 🚀 Data Pipeline E-Commerce

## 📅 Contexte

Ce projet met en œuvre un pipeline de données complet pour une plateforme e-commerce fictive. Il assure l'orchestration, la validation, l'enrichissement, l'agrégation et la surveillance de qualité des données issues de plusieurs sources (sessions utilisateurs, produits, utilisateurs, logs API).

## 🏠 Structure du Projet

```
.
├── config/                  # Schémas, règles métier et seuils de qualité
├── data/
│   ├── raw/                # Fichiers bruts
│   ├── staging/            # Fichiers pré-nettoyés en attente de validation
│   ├── processed/
│   │   ├── api_logs/       # Données apis_logs traitées
│   │   ├── enriched        # Données enrichies
│   │   ├── joined          # Données consolidées pour la BI par exemple
│   │   ├── products        # Données produits traités
│   │   ├── sales           # Données des ventes traitées
│   │   ├── sessions        # Données des sessions traitées
│   ├── quality/            # Rapports de qualité et alertes (json,html,csv,txt,etc..)
│   └── archive/            # Données archivées 
├── orchestration/
│   ├── pipeline_master.sh  # Orchestrateur principal
│   ├── data_discovery.sh   # Détection des sources entrantes
│   ├── worker_manager.sh   # Dispatch du traitement en parallèle
│   ├── quality_monitor.sh  # Lancement des contrôles de qualité
├── processing/
│   ├── data_validator.py   # Validation de qualité (schéma, règles, complétude)
│   ├── api_log_processor.py  # Traitement des données utilisateur
│   ├── busines_processor.py  # Traitement des données utilisateur
│   ├── product_processor.py  # Traitement des données utilisateur
│   ├── session_processor.py  # Traitement des données utilisateur
│   ├── data_validator.py  # Traitement des données utilisateur│   …
├── transformations/
│   ├── data_enricher.py    # Enrichissement (calculs, dérivées, KPI)
│   ├── data_aggregator.py  # Agrégation multi-dimensionnelle
│   ├── data_joiner.py      # Fusion des sources
│   ├── data_formatter.py   # Génération des rapports CSV/Excel
├── monitoring/
│   ├── alert_manager.py    # Simulation des alertes qualité
│   ├── dashboard_gen.py    # Génération du dashboard HTML
├── requirements.txt        # Librairies Python requises
├── Makefile                # Environnement virtuel, outils CLI
└── README.md               # Documentation
```

## 🚜 Workflow Global

1. **Initialisation** du pipeline (structure, variables, config)
2. **Scan** des nouvelles sources de données (raw -> staging)
3. **Traitement** des fichiers via workers Python
4. **Contrôles Qualité**
   - Validation de schéma (via `data_schemas.json`)
   - Règles métier (via `business_rules.yaml`)
   - Détection d'anomalies statistiques
   - Complétude et seuil de qualité (`quality_thresholds.yaml`)
5. **Alertes** en cas d'échec dans `quality_alert.txt`
6. **Dashboard** HTML des rapports dans `data/processed/final/dashboard.html`
7. (Optionnel) **Agrégation et reporting** CSV/Excel
8. (Prochainement) **Archivage** et **Reprise** intelligente

## ⚖️ Orchestration Bash

Le script principal `pipeline_master.sh` gère toutes les étapes :

```bash
./orchestration/pipeline_master.sh
```

## 🧰 Qualité de Données

- Fichiers validés uniquement si tous les critères sont respectés
- Rapports stockés au format JSON : `data/quality/validation_report_<file>.json`
- Fichiers rejetés listés dans : `quality_alert.txt`

## 📊 Dashboard Qualité

Un fichier HTML synthétique est généré dans `data/quality/dashboard.html` avec :

- Le statut de chaque fichier
- La complétude
- Les erreurs détectées

## ⚙️ Setup Environnement

```bash
make install      # Installe les dépendances dans un venv
source .venv/bin/activate
```

## 🚀 Pour aller plus loin

-

---

✉️ Auteur : Jaouad Tanouti

Formation M2i Data Engineer - Projet E-commerce pipeline de données

