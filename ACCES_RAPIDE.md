# 🔯 Accès Rapide - Codes Torah

## 📍 OÙ CONSULTER LE SYSTÈME ?

### 1. 🌐 Sur GitHub (Recommandé)
**Branche :** `claude/cleanup-emergency-code-011CUbmtD3BW34TZaCehseLT`

**Lien direct :**
```
https://github.com/aurielhaken/TORAH/tree/claude/cleanup-emergency-code-011CUbmtD3BW34TZaCehseLT
```

**Fichiers importants :**
- 📖 `CODES_TORAH.md` - Documentation complète (600+ lignes)
- 🐍 `ai/codes_torah.py` - Module d'analyse (405 lignes)
- 🧪 `test_codes_torah.py` - Tests complets
- 🎮 `demo_codes.py` - Démo interactive (NOUVEAU !)
- 🔌 `api/main.py` - Endpoints API (lignes 384-637)

---

## 🚀 UTILISATION SANS SERVEUR

### Option 1 : Démo Interactive (Le plus simple !)

```bash
python demo_codes.py
```

**Menu interactif :**
- ✅ Guématrie
- ✅ At-Bash
- ✅ Notarikon
- ✅ Analyse complète
- ✅ Exemples célèbres

### Option 2 : Tests Automatiques

```bash
python test_codes_torah.py
```

Affiche tous les tests avec résultats colorés.

### Option 3 : Exemples Prêts

```bash
python ai/codes_torah.py
```

Lance les exemples de base.

### Option 4 : Utilisation dans votre code Python

```python
from ai.codes_torah import AnalyseurCodesTorah

analyseur = AnalyseurCodesTorah()

# Guématrie
result = analyseur.calculer_guematrie("אהבה")
print(f"Valeur: {result.valeur}")  # → 13

# At-Bash
babel = analyseur.appliquer_atbash("בבל")
print(f"At-Bash: {babel}")  # → ששך

# Analyse complète
tout = analyseur.analyser_tout("שלום")
print(tout)
```

---

## 🔌 AVEC SERVEUR API

### Démarrer le serveur :

```bash
python -m uvicorn api.main:app --reload
```

### Accéder à la documentation interactive :

```
http://localhost:8000/docs
```

### 7 Endpoints disponibles :

```
POST /api/v1/codes/guematrie       - Guématrie
POST /api/v1/codes/els              - Codes ELS
POST /api/v1/codes/notarikon        - Notarikon
POST /api/v1/codes/atbash           - At-Bash
POST /api/v1/codes/temourah         - Témourah
POST /api/v1/codes/analyser-tout    - Analyse complète
GET  /api/v1/codes/exemples         - Exemples célèbres
```

### Exemple cURL :

```bash
curl -X POST "http://localhost:8000/api/v1/codes/guematrie" \
  -H "Content-Type: application/json" \
  -d '{"texte_hebreu": "אהבה", "methode": "standard"}'
```

---

## 📱 DEPUIS N'IMPORTE OÙ (Si serveur déployé)

Une fois déployé sur Vercel/Render :

```bash
curl -X POST "https://votre-app.vercel.app/api/v1/codes/guematrie" \
  -H "Content-Type: application/json" \
  -d '{"texte_hebreu": "משיח"}'
```

---

## 🎯 DÉMOS RAPIDES

### 1. Découverte : Amour = Un

```python
python -c "
from ai.codes_torah import AnalyseurCodesTorah
a = AnalyseurCodesTorah()
ahava = a.calculer_guematrie('אהבה')
ehad = a.calculer_guematrie('אחד')
print(f'אהבה (Amour) = {ahava.valeur}')
print(f'אחד (Un) = {ehad.valeur}')
print('→ Identiques !' if ahava.valeur == ehad.valeur else '')
"
```

### 2. At-Bash de Babel

```python
python -c "
from ai.codes_torah import AnalyseurCodesTorah
a = AnalyseurCodesTorah()
print(f'בבל → {a.appliquer_atbash(\"בבל\")}')
print('📖 Voir Jérémie 25:26')
"
```

### 3. Analyse complète de Shalom

```python
python -c "
from ai.codes_torah import AnalyseurCodesTorah
import json
a = AnalyseurCodesTorah()
result = a.analyser_tout('שלום')
print(json.dumps(result, ensure_ascii=False, indent=2))
"
```

---

## 📖 DOCUMENTATION COMPLÈTE

**Lire :** `CODES_TORAH.md`

Contient :
- ✅ Explications détaillées de chaque méthode
- ✅ Tables de valeurs guématriques
- ✅ 15+ découvertes célèbres
- ✅ Références bibliques
- ✅ Sources kabbalistiques (Sefer Yetzirah, Zohar, Bahir)
- ✅ Guide d'utilisation API et Python
- ✅ Notes sur l'utilisation spirituelle

---

## 🔑 DÉCOUVERTES PRINCIPALES

| Mot Hébreu | Valeur | Connexion | Signification |
|------------|--------|-----------|---------------|
| אהבה (Amour) | 13 | = אחד (Un) | L'amour crée l'unité |
| יהוה (Hashem) | 26 | = 2×13 | Dieu est amour × 2 |
| משיח (Messie) | 358 | = נחש (Serpent) | Transformation du mal |
| שלום (Paix) | 376 | Katan = 7 | Perfection spirituelle |
| תורה (Torah) | 611 | +2 (lecture) = 613 | Les 613 mitzvot |

---

## 📞 SUPPORT

**Questions :** Voir `CODES_TORAH.md` section "Pour Aller Plus Loin"

**Bugs :** GitHub Issues sur le repo

**Documentation API :** `/docs` quand serveur lancé

---

## ✨ EN RÉSUMÉ

**Pour consulter rapidement :**
```bash
python demo_codes.py
```

**Pour voir tous les tests :**
```bash
python test_codes_torah.py
```

**Pour lire la documentation :**
```bash
cat CODES_TORAH.md
```

**Sur GitHub :**
```
https://github.com/aurielhaken/TORAH/tree/claude/cleanup-emergency-code-011CUbmtD3BW34TZaCehseLT
```

---

🔯 **B'hatzla'ha !**
