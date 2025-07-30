#!/bin/bash

echo "🔐 Réinitialisation des permissions sur le projet..."

# ============================
# 🔒 Permissions
# ============================

# Dossiers : 755 (rwxr-xr-x)
find . -type d -exec chmod 755 {} \;

# Fichiers : 644 (rw-r--r--) sauf scripts
find . -type f ! -name "*.sh" -exec chmod 644 {} \;

# Scripts *.sh et *.py : 755 (exécutables)
find . -type f \( -name "*.sh" -o -name "*.py" \) -exec chmod 755 {} \;

# ============================
# 🔄 Format Unix (anti-caractères Windows)
# ============================

# Convertit les fichiers texte au format Unix
find . -type f \( -name "*.sh" -o -name "*.py" -o -name "*.csv" -o -name "*.json" -o -name "*.yaml" \) -exec dos2unix {} \;

# ============================
# ✅ Résultat
# ============================

echo "✅ Permissions mises à jour :"
echo "   📁 Dossiers -> 755"
echo "   📄 Fichiers standards -> 644"
echo "   🧩 Scripts *.sh / *.py -> 755"
echo "   🔁 Conversion DOS -> Unix terminée"
