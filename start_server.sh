#!/bin/bash
# Script de démarrage du serveur Torah AI

echo "Démarrage du serveur Torah AI..."

# Arrêter les instances existantes
pkill -f uvicorn 2>/dev/null

# Démarrer le serveur
cd /home/user/TORAH
python3 -m uvicorn api.main:app \
    --host 0.0.0.0 \
    --port 8000 \
    --reload \
    --log-level info

echo "Serveur démarré sur http://0.0.0.0:8000"
