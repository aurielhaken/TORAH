"""
WSGI configuration pour IONOS
Torah AI - Rav Virtuel
"""

from api.main import app

# Pour les serveurs WSGI (Apache, etc.)
application = app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
