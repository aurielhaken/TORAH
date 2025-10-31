#!/bin/bash
# Script de déploiement pour IONOS
# Torah AI - Rav Virtuel

echo "🕎 Torah AI - Déploiement sur IONOS"
echo "===================================="

# Configuration
export PORT=${PORT:-8000}
export HOST="0.0.0.0"

# Installer les dépendances
echo "📦 Installation des dépendances..."
pip3 install --user -r requirements-minimal.txt

# Démarrer le serveur
echo "🚀 Démarrage du serveur..."
python3 -m uvicorn api.main:app \
    --host $HOST \
    --port $PORT \
    --workers 2 \
    --log-level info

echo "✅ Serveur démarré sur $HOST:$PORT"
