#!/usr/bin/env python3
"""
Script de test pour l'API Torah AI - Rav Virtuel
"""

import requests
import json


BASE_URL = "http://localhost:8000"


def test_health():
    """Test du health check"""
    print("=== Test Health Check ===")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


def test_root():
    """Test de la page d'accueil"""
    print("=== Test Page d'accueil ===")
    response = requests.get(f"{BASE_URL}/")
    data = response.json()
    print(f"Message: {data['message']}")
    print(f"Description: {data['description']}")
    print(f"Valeurs: {data['valeurs']}\n")


def test_categories():
    """Test de la liste des catégories"""
    print("=== Test Catégories ===")
    response = requests.get(f"{BASE_URL}/api/v1/categories")
    data = response.json()
    print(f"Nombre de catégories: {len(data['categories'])}")
    for cat in data['categories']:
        print(f"  - {cat['nom']} ({cat['nom_hebreu']})")
    print()


def test_glossaire(terme="Torah"):
    """Test du glossaire"""
    print(f"=== Test Glossaire: {terme} ===")
    response = requests.get(f"{BASE_URL}/api/v1/glossaire/{terme}")
    print(f"Response: {response.json()}\n")


def test_question(question="Quelle est la signification du Shabbat?"):
    """Test de question au Rav"""
    print(f"=== Test Question au Rav ===")
    print(f"Question: {question}\n")

    data = {
        "question": question,
        "langue": "fr",
        "niveau": "intermediaire"
    }

    response = requests.post(
        f"{BASE_URL}/api/v1/question",
        json=data,
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 200:
        result = response.json()
        print(f"Réponse du Rav:")
        print(f"{result['reponse']}\n")

        if result['sources']:
            print("Sources citées:")
            for source in result['sources']:
                print(f"  - {source['reference']}")
                print(f"    {source['texte'][:100]}...")
                print(f"    Pertinence: {source['pertinence']}\n")

        if result['concepts_lies']:
            print(f"Concepts liés: {', '.join(result['concepts_lies'])}")

        if result['suggestions_etude']:
            print("\nSuggestions d'étude:")
            for suggestion in result['suggestions_etude']:
                print(f"  - {suggestion}")
    else:
        print(f"Erreur: {response.status_code}")
        print(f"Response: {response.text}")

    print()


def test_stats():
    """Test des statistiques"""
    print("=== Test Statistiques ===")
    response = requests.get(f"{BASE_URL}/api/v1/stats")
    data = response.json()
    print("Statistiques de la base:")
    for key, value in data.items():
        if key != "langues_supportees":
            print(f"  {key}: {value}")
    print(f"  Langues supportées: {', '.join(data['langues_supportees'])}\n")


def main():
    """Execute tous les tests"""
    print("\n" + "="*60)
    print("  TESTS API TORAH AI - RAV VIRTUEL")
    print("="*60 + "\n")

    try:
        test_health()
        test_root()
        test_categories()
        test_stats()
        test_glossaire("Torah")
        test_question("Quelle est la signification du Shabbat?")

        print("="*60)
        print("  Tous les tests sont passés avec succès! ✓")
        print("="*60 + "\n")

        print("💡 Pour explorer l'API interactivement:")
        print(f"   Ouvrez votre navigateur à: {BASE_URL}/docs\n")

    except requests.exceptions.ConnectionError:
        print("❌ Erreur: L'API n'est pas accessible")
        print("   Assurez-vous que le serveur est lancé:")
        print("   uvicorn api.main:app --reload\n")
    except Exception as e:
        print(f"❌ Erreur: {e}\n")


if __name__ == "__main__":
    main()
