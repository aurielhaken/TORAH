"""
Point d'entrée pour Vercel
"""
from api.main import app

# Vercel cherche un objet 'app' ou 'handler'
# Notre app FastAPI est déjà exportée depuis main.py
