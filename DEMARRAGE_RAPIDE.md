# Démarrage Rapide - Torah AI ⚡

## En 5 minutes chrono!

### 1. Cloner le projet

```bash
git clone <votre-repo>
cd TORAH
```

### 2. Créer l'environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements-minimal.txt
```

### 4. Initialiser la base de données

```bash
python database/init_sqlite.py
```

Vous devriez voir:
```
✓ Base de données initialisée avec succès!
=== Statistiques ===
  Catégories: 9
  Livres: 5
  Chapitres: 1
  Passages: 3
  Termes glossaire: 8
```

### 5. Lancer l'API

```bash
uvicorn api.main:app --reload
```

L'API est maintenant accessible sur http://localhost:8000

### 6. Tester

**Méthode 1: Script de test**
```bash
python test_api.py
```

**Méthode 2: Interface web**
Ouvrez http://localhost:8000/docs dans votre navigateur

**Méthode 3: Curl**
```bash
# Poser une question
curl -X POST "http://localhost:8000/api/v1/question" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Quelle est la signification du Shabbat?",
    "langue": "fr",
    "niveau": "intermediaire"
  }'
```

## Endpoints principaux

| Endpoint | Description |
|----------|-------------|
| `GET /` | Page d'accueil |
| `GET /health` | Health check |
| `GET /docs` | Documentation interactive |
| `POST /api/v1/question` | Poser une question au Rav |
| `GET /api/v1/categories` | Liste des catégories |
| `GET /api/v1/stats` | Statistiques de la base |
| `GET /api/v1/glossaire/{terme}` | Rechercher un terme |

## Exemple de question

```python
import requests

response = requests.post(
    "http://localhost:8000/api/v1/question",
    json={
        "question": "Qu'est-ce que le Shabbat?",
        "langue": "fr",
        "niveau": "simple"
    }
)

print(response.json()['reponse'])
```

## Structure de la base de données

Après initialisation, vous avez:
- **9 catégories**: Torah, Mishna, Talmud, Kabbalah, etc.
- **5 livres de la Torah**: Genèse, Exode, Lévitique, Nombres, Deutéronome
- **3 premiers versets** de la Genèse (en hébreu, français, anglais)
- **8 termes** dans le glossaire

## Prochaines étapes

### Ajouter plus de contenu

1. **Importer depuis Sefaria** (gratuit):
   ```bash
   # À venir
   python scripts/import_sefaria.py
   ```

2. **Ajouter manuellement**:
   Utilisez SQLite Browser ou des requêtes SQL directes sur `torah_ai.db`

### Activer l'IA complète

1. Obtenir une clé API (OpenAI ou Anthropic)

2. Éditer `.env`:
   ```env
   OPENAI_API_KEY=sk-...
   # OU
   ANTHROPIC_API_KEY=sk-ant-...
   ```

3. Installer les dépendances IA:
   ```bash
   pip install -r requirements.txt  # Version complète
   ```

### Passer à PostgreSQL (production)

1. Installer PostgreSQL + pgvector

2. Éditer `.env`:
   ```env
   DATABASE_URL=postgresql://user:pass@localhost/torah_ai
   ```

3. Initialiser:
   ```bash
   python scripts/init_db.py
   ```

## Dépannage

### Port 8000 déjà utilisé
```bash
uvicorn api.main:app --reload --port 8080
```

### Environnement virtuel non activé
```bash
source venv/bin/activate  # Toujours activer avant de travailler
```

### Base de données corrompue
```bash
rm torah_ai.db
python database/init_sqlite.py
```

## Arrêter le serveur

Appuyez sur `Ctrl+C` dans le terminal où tourne uvicorn

## Documentation complète

- **Installation détaillée**: [GUIDE_INSTALLATION.md](GUIDE_INSTALLATION.md)
- **Architecture**: [ARCHITECTURE.md](ARCHITECTURE.md)
- **Contribution**: [CONTRIBUTING.md](CONTRIBUTING.md)

---

**B'hatzla'ha!** (Bonne chance!)

*"עשה לך רב" - "Fais-toi un maître" (Pirke Avot 1:6)*
