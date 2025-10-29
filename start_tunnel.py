#!/usr/bin/env python3
"""
Crée un tunnel public pour accéder à l'API Torah AI depuis n'importe où
"""
from pyngrok import ngrok
import time
import requests

print("🕎 Torah AI - Création du tunnel public...")
print("=" * 60)

# Arrêter tous les tunnels existants
ngrok.kill()
time.sleep(1)

# Créer le tunnel sur le port 8000
print("\n⏳ Démarrage du tunnel ngrok...")
public_url = ngrok.connect(8000, bind_tls=True)

print("\n✅ Tunnel créé avec succès !")
print("=" * 60)
print(f"\n📱 ACCÉDEZ À L'APPLICATION DEPUIS VOTRE TÉLÉPHONE :")
print(f"\n   {public_url}")
print(f"\n📚 Documentation interactive :")
print(f"   {public_url}/docs")
print(f"\n🏠 Page d'accueil :")
print(f"   {public_url}/")
print("\n" + "=" * 60)

# Tester le tunnel
print("\n🔍 Test du tunnel...")
try:
    response = requests.get(f"{public_url}/health", timeout=5)
    if response.status_code == 200:
        print("✅ Le tunnel fonctionne parfaitement !")
        data = response.json()
        print(f"   Message: {data.get('message', '')}")
    else:
        print(f"⚠️  Status: {response.status_code}")
except Exception as e:
    print(f"⚠️  Erreur lors du test: {e}")

print("\n" + "=" * 60)
print("📌 GARDEZ CETTE FENÊTRE OUVERTE")
print("   Le tunnel restera actif tant que ce script tourne")
print("   Appuyez sur Ctrl+C pour arrêter le tunnel")
print("=" * 60)

try:
    # Garder le tunnel actif
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n\n🛑 Arrêt du tunnel...")
    ngrok.kill()
    print("✅ Tunnel fermé.")
