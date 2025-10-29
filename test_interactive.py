#!/usr/bin/env python3
"""
Script interactif pour tester l'API Torah AI
"""
import requests
import json

API_URL = "http://localhost:8000"

def test_api():
    print("=" * 60)
    print("🕎 Torah AI - Test de l'API")
    print("=" * 60)
    
    # Test Health
    print("\n1. Test Health Check...")
    try:
        response = requests.get(f"{API_URL}/health")
        print(f"   Status: {response.status_code}")
        print(f"   Réponse: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    # Test Root
    print("\n2. Test Page d'accueil...")
    try:
        response = requests.get(f"{API_URL}/")
        print(f"   Status: {response.status_code}")
        data = response.json()
        print(f"   Message: {data['message']}")
        print(f"   Endpoints disponibles: {list(data['endpoints'].keys())}")
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    # Test Question
    print("\n3. Test Question...")
    try:
        response = requests.post(
            f"{API_URL}/api/v1/question",
            json={
                "question": "Quelle est la signification du Shabbat?",
                "langue": "fr",
                "niveau": "intermediaire"
            }
        )
        print(f"   Status: {response.status_code}")
        data = response.json()
        print(f"   Réponse: {data['reponse'][:150]}...")
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    # Test Categories
    print("\n4. Test Catégories...")
    try:
        response = requests.get(f"{API_URL}/api/v1/categories")
        print(f"   Status: {response.status_code}")
        data = response.json()
        for cat in data['categories']:
            print(f"   - {cat['nom']} ({cat['nom_hebreu']})")
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    print("\n" + "=" * 60)
    print("✅ Tests terminés!")
    print("=" * 60)

if __name__ == "__main__":
    test_api()
