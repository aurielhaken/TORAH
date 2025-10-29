# Torah AI - Rav Virtuel 📖✨

## Vision

Une intelligence artificielle dédiée à l'enseignement de la Torah, accessible au monde entier. Ce "Rav virtuel" s'appuie sur l'ensemble du savoir judaïque - Torah, Mishna, Guemara, Kabbalah et commentaires - pour éduquer avec amour et transmettre les valeurs du judaïsme.

## Caractéristiques

- **Base de connaissances complète**: Torah (Pentateuque), Mishna, Talmud (Guemara), Kabbalah, commentaires des Rishonim et Aharonim
- **IA conversationnelle**: Posez vos questions en langage naturel
- **Multilingue**: Support hébreu, français, anglais, et plus
- **Recherche sémantique**: Trouve les passages pertinents basés sur le sens, pas seulement les mots-clés
- **Codes cachés de la Torah**: Guématrie, ELS, Notarikon, At-Bash, Témourah
- **Accessible mondialement**: API REST disponible partout dans le monde
- **Valeurs juives**: Réponses imprégnées d'amour, sagesse et éthique juive

## Architecture

```
torah-ai/
├── database/           # Schémas et migrations de base de données
├── api/               # API REST FastAPI
├── ai/                # Moteur d'IA et embeddings
├── data/              # Textes sources (Torah, Mishna, etc.)
├── models/            # Modèles de données
└── docs/              # Documentation
```

## Technologies

- **Base de données**: PostgreSQL avec pgvector pour la recherche vectorielle
- **Backend**: Python 3.11+ avec FastAPI
- **IA**: Modèles de langage avec RAG (Retrieval-Augmented Generation)
- **Embeddings**: Sentence transformers pour la recherche sémantique

## Installation

```bash
# À venir
pip install -r requirements.txt
python scripts/init_db.py
```

## Utilisation

```python
# Exemple d'utilisation de l'API
from torah_ai import RavVirtuel

rav = RavVirtuel()
reponse = rav.poser_question("Quelle est la signification du Shabbat?")
print(reponse)
```

## Codes Cachés de la Torah

Découvrez les dimensions mystiques du texte sacré avec notre système d'analyse des codes :

- **Guématrie** : Valeurs numériques révélant des connexions cachées (ex: אהבה = אחד = 13)
- **ELS** : Séquences équidistantes de lettres
- **Notarikon** : Acronymes et expansions sacrés
- **At-Bash** : Substitution hébraïque (ex: בבל → ששך)
- **Témourah** : Permutations révélant de nouveaux sens

Voir [CODES_TORAH.md](CODES_TORAH.md) pour la documentation complète et des exemples.

## Contribution

Ce projet est ouvert à tous ceux qui souhaitent contribuer à l'éducation juive. Voir CONTRIBUTING.md

## Licence

À définir - pour usage éducatif et spirituel

---

*"Talmud Torah k'neged kulam" - L'étude de la Torah équivaut à toutes les autres mitzvot*
