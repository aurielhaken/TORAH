# Guide d'Installation - Torah AI - Rav Virtuel

## Bienvenue!

Ce guide vous accompagne pas à pas pour installer et utiliser votre propre Rav Virtuel, une IA dédiée à l'enseignement de la Torah avec amour et sagesse.

## Prérequis

### Logiciels requis

1. **Python 3.11+**
   ```bash
   python --version  # Vérifiez votre version
   ```

2. **PostgreSQL 14+** avec l'extension pgvector
   ```bash
   # Sur Ubuntu/Debian
   sudo apt update
   sudo apt install postgresql postgresql-contrib

   # Sur macOS avec Homebrew
   brew install postgresql@14
   ```

3. **Git**
   ```bash
   git --version
   ```

### Clés API (optionnelles pour commencer)

Pour utiliser pleinement l'IA, vous aurez besoin de:
- Clé API OpenAI (GPT-4) OU
- Clé API Anthropic (Claude)

## Installation Étape par Étape

### 1. Cloner le projet

```bash
git clone <votre-repo>
cd TORAH
```

### 2. Créer un environnement virtuel Python

```bash
python -m venv venv

# Activer l'environnement
# Sur Linux/macOS:
source venv/bin/activate

# Sur Windows:
venv\Scripts\activate
```

### 3. Installer les dépendances Python

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configuration de PostgreSQL

#### Démarrer PostgreSQL

```bash
# Sur Ubuntu/Debian
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Sur macOS
brew services start postgresql@14
```

#### Installer l'extension pgvector

```bash
# Se connecter à PostgreSQL
sudo -u postgres psql

# Dans psql:
CREATE EXTENSION vector;
\q
```

### 5. Configuration de l'application

#### Copier le fichier de configuration

```bash
cp .env.example .env
```

#### Éditer le fichier .env

```bash
nano .env  # ou votre éditeur préféré
```

Configurer au minimum:

```env
# Base de données
DATABASE_URL=postgresql://postgres:votre_mot_de_passe@localhost:5432/torah_ai

# IA (optionnel pour commencer)
OPENAI_API_KEY=sk-...
# OU
ANTHROPIC_API_KEY=sk-ant-...
```

### 6. Initialiser la base de données

```bash
python scripts/init_db.py
```

Cette commande va:
- Créer la base de données `torah_ai`
- Créer toutes les tables (passages, commentaires, etc.)
- Charger les données initiales (catégories, livres de la Torah)
- Charger quelques exemples de passages

### 7. Lancer l'API

```bash
# Depuis le répertoire racine du projet
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

### 8. Vérifier que tout fonctionne

Ouvrez votre navigateur et allez à:

- **Documentation interactive**: http://localhost:8000/docs
- **API Root**: http://localhost:8000/
- **Health check**: http://localhost:8000/health

## Utilisation de base

### Via l'interface web (Swagger UI)

1. Allez sur http://localhost:8000/docs
2. Cliquez sur `POST /api/v1/question`
3. Cliquez sur "Try it out"
4. Entrez votre question dans le JSON:
   ```json
   {
     "question": "Quelle est la signification du Shabbat?",
     "langue": "fr",
     "niveau": "intermediaire"
   }
   ```
5. Cliquez sur "Execute"

### Via Python

```python
import requests

url = "http://localhost:8000/api/v1/question"
data = {
    "question": "Quelle est la signification du Shabbat?",
    "langue": "fr",
    "niveau": "intermediaire"
}

response = requests.post(url, json=data)
print(response.json())
```

### Via curl

```bash
curl -X POST "http://localhost:8000/api/v1/question" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Quelle est la signification du Shabbat?",
    "langue": "fr",
    "niveau": "intermediaire"
  }'
```

## Importation des textes sacrés

### Option 1: Via l'API Sefaria (gratuit)

Sefaria.org offre une API gratuite avec une grande partie des textes:

```bash
# À venir: script d'import
python scripts/import_sefaria.py
```

### Option 2: Import manuel

Vous pouvez importer vos propres textes via SQL:

```sql
-- Exemple d'import d'un passage
INSERT INTO passages (chapitre_id, numero, texte_hebreu, texte_francais)
VALUES (1, 2, 'וְהָאָרֶץ הָיְתָה תֹהוּ וָבֹהוּ', 'La terre était informe et vide');
```

## Configuration avancée

### Activer les embeddings pour la recherche sémantique

1. Assurez-vous d'avoir installé le modèle:
   ```bash
   python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')"
   ```

2. Générer les embeddings:
   ```bash
   # À venir
   python scripts/generate_embeddings.py
   ```

### Configurer Redis pour le cache (optionnel)

```bash
# Installer Redis
sudo apt install redis-server

# Démarrer Redis
sudo systemctl start redis

# Dans .env
REDIS_URL=redis://localhost:6379/0
```

## Déploiement en production

### Avec Docker

```bash
# À venir: Dockerfile
docker build -t torah-ai .
docker run -p 8000:8000 torah-ai
```

### Sur un serveur

1. Utiliser Nginx comme reverse proxy
2. Utiliser systemd pour le service
3. Configuration SSL avec Let's Encrypt
4. Documentation complète à venir

## Dépannage

### Erreur de connexion à PostgreSQL

```bash
# Vérifier que PostgreSQL est démarré
sudo systemctl status postgresql

# Vérifier les connexions
sudo -u postgres psql -c "SELECT 1"
```

### Problème d'import des modules

```bash
# Vérifier que l'environnement virtuel est activé
which python  # Devrait pointer vers venv/bin/python

# Réinstaller les dépendances
pip install -r requirements.txt
```

### L'IA ne répond pas correctement

- Vérifiez que vous avez configuré une clé API valide
- Vérifiez les logs pour voir les erreurs
- L'IA nécessite des données dans la base pour fonctionner

## Contribuer

Ce projet est ouvert à tous! Pour contribuer:

1. Ajout de textes sacrés
2. Traductions
3. Amélioration de l'IA
4. Documentation
5. Tests

## Support

Pour toute question ou problème:
- Ouvrir une issue sur GitHub
- Documentation complète: [À venir]

## Licence

[À définir - Usage éducatif et spirituel]

---

*"Talmud Torah k'neged kulam" - L'étude de la Torah équivaut à toutes les autres mitzvot*

Que ce projet apporte sagesse, compréhension et élévation spirituelle à tous ceux qui l'utilisent.

**B'hatzla'ha!** (Bonne chance!)
