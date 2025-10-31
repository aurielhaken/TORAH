# 📖 Exemples d'utilisation de l'API Torah AI

Une fois votre API déployée, voici comment l'utiliser !

## 🌐 URL de base

Remplacez `YOUR_URL` par votre URL Deploy Now (ex: `https://torah-ai-xyz123.ionos.space`)

## 🧪 Tests rapides

### 1. Health Check

**Vérifier que l'API fonctionne**

```bash
curl https://YOUR_URL/health
```

**Réponse attendue :**
```json
{
  "status": "healthy",
  "message": "Le Rav virtuel est prêt à enseigner"
}
```

### 2. Page d'accueil

```bash
curl https://YOUR_URL/
```

**Réponse :** Liste des endpoints disponibles et valeurs de l'application

## 📱 Depuis votre navigateur

### Documentation interactive (RECOMMANDÉ)

Ouvrez dans votre navigateur :
```
https://YOUR_URL/docs
```

Vous verrez l'interface **Swagger UI** où vous pouvez tester tous les endpoints directement !

## 💬 Poser une question au Rav

### Exemple 1 : Question simple

**Requête :**
```bash
curl -X POST https://YOUR_URL/api/v1/question \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Quelle est la signification du Shabbat?",
    "langue": "fr",
    "niveau": "intermediaire"
  }'
```

**Réponse :**
```json
{
  "reponse": "Merci pour votre question. Le Rav virtuel est en cours d'initialisation...",
  "sources": [
    {
      "type": "torah",
      "reference": "Genèse 1:1",
      "texte": "Au commencement, Dieu créa le ciel et la terre",
      "pertinence": 0.95
    }
  ],
  "concepts_lies": ["Création", "Bereshit"],
  "mitzvot_liees": [],
  "suggestions_etude": [
    "Étudier le commentaire de Rashi sur ce passage"
  ],
  "langue": "fr",
  "niveau": "intermediaire"
}
```

### Exemple 2 : Question en anglais

```bash
curl -X POST https://YOUR_URL/api/v1/question \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is the meaning of Shabbat?",
    "langue": "en",
    "niveau": "simple"
  }'
```

### Exemple 3 : Question avancée en hébreu

```bash
curl -X POST https://YOUR_URL/api/v1/question \
  -H "Content-Type: application/json" \
  -d '{
    "question": "מה המשמעות של השבת בקבלה?",
    "langue": "he",
    "niveau": "avance"
  }'
```

## 📚 Explorer les catégories

**Liste des catégories de textes disponibles**

```bash
curl https://YOUR_URL/api/v1/categories
```

**Réponse :**
```json
{
  "categories": [
    {
      "nom": "Torah",
      "nom_hebreu": "תורה",
      "description": "Les cinq livres de Moïse"
    },
    {
      "nom": "Mishna",
      "nom_hebreu": "משנה",
      "description": "Première codification de la loi orale"
    },
    {
      "nom": "Talmud",
      "nom_hebreu": "תלמוד",
      "description": "Mishna + Guemara"
    },
    {
      "nom": "Kabbalah",
      "nom_hebreu": "קבלה",
      "description": "Tradition mystique"
    }
  ]
}
```

## 🔍 Rechercher dans les textes

```bash
curl -X POST https://YOUR_URL/api/v1/recherche \
  -H "Content-Type: application/json" \
  -d '{
    "query": "création du monde",
    "langue": "fr",
    "limite": 10
  }'
```

## 📅 Enseignement quotidien

```bash
curl "https://YOUR_URL/api/v1/enseignement-quotidien?langue=fr"
```

## 📖 Information sur une Parasha

```bash
curl "https://YOUR_URL/api/v1/parasha/bereshit?langue=fr"
```

## 📝 Consulter le glossaire

```bash
curl "https://YOUR_URL/api/v1/glossaire/shabbat?langue=fr"
```

## 🎯 Liste des 613 Mitzvot

**Toutes les mitzvot :**
```bash
curl "https://YOUR_URL/api/v1/mitzvot?limite=20"
```

**Mitzvot positives uniquement :**
```bash
curl "https://YOUR_URL/api/v1/mitzvot?type=positive&limite=10"
```

**Par catégorie :**
```bash
curl "https://YOUR_URL/api/v1/mitzvot?categorie=Shabbat"
```

## 📊 Statistiques

```bash
curl https://YOUR_URL/api/v1/stats
```

## 🐍 Exemples Python

### Installation

```bash
pip install requests
```

### Script simple

```python
import requests

# URL de votre API
API_URL = "https://YOUR_URL"

# Poser une question
def poser_question(question, langue="fr", niveau="intermediaire"):
    response = requests.post(
        f"{API_URL}/api/v1/question",
        json={
            "question": question,
            "langue": langue,
            "niveau": niveau
        }
    )
    return response.json()

# Test
reponse = poser_question("Quelle est la signification du Shabbat?")
print(reponse['reponse'])
print("\nSources:")
for source in reponse['sources']:
    print(f"- {source['reference']}: {source['texte']}")
```

### Script avec gestion d'erreurs

```python
import requests
from typing import Optional

class TorahAIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')

    def health_check(self) -> bool:
        """Vérifie que l'API fonctionne"""
        try:
            response = requests.get(f"{self.base_url}/health")
            return response.status_code == 200
        except:
            return False

    def poser_question(
        self,
        question: str,
        langue: str = "fr",
        niveau: str = "intermediaire"
    ) -> Optional[dict]:
        """Pose une question au Rav virtuel"""
        try:
            response = requests.post(
                f"{self.base_url}/api/v1/question",
                json={
                    "question": question,
                    "langue": langue,
                    "niveau": niveau
                },
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erreur: {e}")
            return None

    def get_categories(self) -> list:
        """Récupère les catégories disponibles"""
        response = requests.get(f"{self.base_url}/api/v1/categories")
        return response.json().get('categories', [])

# Utilisation
client = TorahAIClient("https://YOUR_URL")

# Vérifier que l'API fonctionne
if client.health_check():
    print("✅ API en ligne")

    # Poser une question
    reponse = client.poser_question(
        "Quelle est la signification du Shabbat dans la Kabbale?",
        niveau="avance"
    )

    if reponse:
        print(f"\n📖 Réponse:\n{reponse['reponse']}")
        print(f"\n🔗 Concepts liés: {', '.join(reponse['concepts_lies'])}")
else:
    print("❌ API hors ligne")
```

## 🌐 Exemples JavaScript

### Depuis un navigateur

```javascript
// Poser une question
async function poserQuestion(question) {
    const response = await fetch('https://YOUR_URL/api/v1/question', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            question: question,
            langue: 'fr',
            niveau: 'intermediaire'
        })
    });

    const data = await response.json();
    return data;
}

// Utilisation
poserQuestion("Quelle est la signification du Shabbat?")
    .then(reponse => {
        console.log('Réponse:', reponse.reponse);
        console.log('Sources:', reponse.sources);
    })
    .catch(err => console.error('Erreur:', err));
```

### Avec Node.js

```javascript
const axios = require('axios');

const API_URL = 'https://YOUR_URL';

async function poserQuestion(question, langue = 'fr', niveau = 'intermediaire') {
    try {
        const response = await axios.post(`${API_URL}/api/v1/question`, {
            question,
            langue,
            niveau
        });
        return response.data;
    } catch (error) {
        console.error('Erreur:', error.message);
        return null;
    }
}

// Test
(async () => {
    const reponse = await poserQuestion("Quelle est la signification du Shabbat?");
    if (reponse) {
        console.log('Réponse:', reponse.reponse);
    }
})();
```

## 📱 Test depuis mobile

### Via le navigateur

1. Ouvrez `https://YOUR_URL/docs` sur votre téléphone
2. Trouvez l'endpoint `POST /api/v1/question`
3. Cliquez sur "Try it out"
4. Entrez votre question
5. Cliquez sur "Execute"
6. Voyez la réponse !

### Via une app (React Native / Flutter)

Le même code JavaScript fonctionne dans React Native !

## 🔐 Bonnes pratiques

### 1. Toujours vérifier le status

```python
response = requests.post(url, json=data)
if response.status_code == 200:
    data = response.json()
else:
    print(f"Erreur {response.status_code}: {response.text}")
```

### 2. Utiliser des timeouts

```python
response = requests.post(url, json=data, timeout=30)
```

### 3. Gérer les erreurs réseau

```python
try:
    response = requests.post(url, json=data)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Erreur réseau: {e}")
```

## 📊 Codes de statut HTTP

- **200** : Succès
- **400** : Requête invalide (vérifier les paramètres)
- **404** : Endpoint non trouvé
- **500** : Erreur serveur
- **503** : Service temporairement indisponible

## 🎉 C'est tout !

Vous savez maintenant comment utiliser l'API Torah AI !

Pour plus d'informations, consultez la documentation interactive : `https://YOUR_URL/docs`

---

**Développé avec ❤️ pour l'enseignement de la Torah**
