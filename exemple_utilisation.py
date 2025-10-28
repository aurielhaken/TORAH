#!/usr/bin/env python3
"""
Exemple d'utilisation de Torah AI - Rav Virtuel
Comment poser des questions au Rav et utiliser l'API
"""

import requests
import json


def exemple_simple():
    """Exemple le plus simple possible"""
    print("=== Exemple Simple ===\n")

    # L'API doit être lancée: uvicorn api.main:app --reload
    response = requests.post(
        "http://localhost:8000/api/v1/question",
        json={
            "question": "Qu'est-ce que le Shabbat?",
            "langue": "fr"
        }
    )

    result = response.json()
    default_question = "Qu'est-ce que le Shabbat?"
    print(f"Question: {result.get('question', default_question)}")
    print(f"\nRéponse du Rav:")
    print(result['reponse'])
    print()


def exemple_avec_niveau():
    """Question avec niveau de complexité"""
    print("=== Exemple avec Niveau ===\n")

    questions = [
        ("Qu'est-ce que la Torah?", "simple"),
        ("Expliquez la structure de la Mishna", "intermediaire"),
        ("Quelle est la signification kabbalistique du Shabbat?", "avance")
    ]

    for question, niveau in questions:
        response = requests.post(
            "http://localhost:8000/api/v1/question",
            json={
                "question": question,
                "langue": "fr",
                "niveau": niveau
            }
        )

        result = response.json()
        print(f"Question ({niveau}): {question}")
        print(f"Réponse: {result['reponse'][:200]}...")
        print()


def exemple_multilingue():
    """Même question en plusieurs langues"""
    print("=== Exemple Multilingue ===\n")

    questions = {
        "fr": "Qu'est-ce que le Shabbat?",
        "en": "What is Shabbat?",
        "he": "מה זה שבת?"
    }

    for langue, question in questions.items():
        response = requests.post(
            "http://localhost:8000/api/v1/question",
            json={
                "question": question,
                "langue": langue
            }
        )

        result = response.json()
        print(f"[{langue}] {question}")
        print(f"Réponse: {result['reponse'][:150]}...")
        print()


def exemple_glossaire():
    """Recherche dans le glossaire"""
    print("=== Exemple Glossaire ===\n")

    termes = ["Torah", "Shabbat", "Mitzva"]

    for terme in termes:
        response = requests.get(
            f"http://localhost:8000/api/v1/glossaire/{terme}"
        )

        result = response.json()
        print(f"Terme: {terme}")
        print(f"Hébreu: {result.get('terme_hebreu', 'N/A')}")
        print(f"Translittération: {result.get('transliteration', 'N/A')}")
        print(f"Traduction: {result.get('traduction', 'N/A')}")
        print()


def exemple_categories():
    """Lister les catégories disponibles"""
    print("=== Catégories Disponibles ===\n")

    response = requests.get("http://localhost:8000/api/v1/categories")
    result = response.json()

    print("Textes disponibles dans la base:")
    for cat in result['categories']:
        print(f"  📚 {cat['nom']} ({cat['nom_hebreu']})")
        print(f"     {cat['description']}")
        print()


def exemple_stats():
    """Statistiques de la base"""
    print("=== Statistiques ===\n")

    response = requests.get("http://localhost:8000/api/v1/stats")
    result = response.json()

    print("État actuel de la base de données:")
    print(f"  Passages: {result.get('passages', 0)}")
    print(f"  Commentaires: {result.get('commentaires', 0)}")
    print(f"  Questions posées: {result.get('questions_posees', 0)}")
    print(f"  Mitzvot: {result.get('mitzvot', 613)}")
    print(f"  Langues: {', '.join(result.get('langues_supportees', []))}")
    print()


def exemple_complet():
    """Exemple complet avec tout"""
    print("\n" + "="*70)
    print("  EXEMPLES D'UTILISATION - TORAH AI - RAV VIRTUEL")
    print("="*70 + "\n")

    try:
        # Vérifier que l'API est accessible
        health = requests.get("http://localhost:8000/health")
        if health.status_code != 200:
            print("❌ L'API n'est pas accessible!")
            print("   Lancez-la avec: uvicorn api.main:app --reload")
            return

        print("✓ API accessible\n")

        # Exemples
        exemple_stats()
        exemple_categories()
        exemple_simple()
        # exemple_avec_niveau()  # Décommenter quand l'IA sera activée
        # exemple_multilingue()   # Décommenter quand l'IA sera activée
        exemple_glossaire()

        print("="*70)
        print("\n💡 Pour plus d'informations:")
        print("   - Documentation: http://localhost:8000/docs")
        print("   - Guide: DEMARRAGE_RAPIDE.md")
        print("   - Architecture: ARCHITECTURE.md\n")

    except requests.exceptions.ConnectionError:
        print("❌ Erreur: L'API n'est pas accessible")
        print("\n   Démarrez l'API avec:")
        print("   uvicorn api.main:app --reload\n")
    except Exception as e:
        print(f"❌ Erreur: {e}\n")


if __name__ == "__main__":
    exemple_complet()
