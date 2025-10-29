# 🔯 Codes Cachés de la Torah

## Introduction

La Torah contient des **codes cachés** révélés par la tradition kabbalistique. Ces méthodes permettent de découvrir des connexions profondes et des enseignements cachés dans le texte sacré.

Ce module implémente les 5 principales méthodes d'analyse :

1. **Guématrie** (גימטריה) - Valeurs numériques des lettres
2. **ELS** (Equidistant Letter Sequences) - Codes à intervalles réguliers
3. **Notarikon** (נוטריקון) - Acronymes et expansions
4. **At-Bash** (אתב״ש) - Substitution inversée
5. **Témourah** (תמורה) - Permutations de lettres

---

## 📊 1. GUÉMATRIE (גימטריה)

### Principe

Chaque lettre hébraïque possède une valeur numérique. Des mots ayant la même valeur sont spirituellement connectés.

### Table des valeurs

```
א=1   ב=2   ג=3   ד=4   ה=5   ו=6   ז=7   ח=8   ט=9
י=10  כ=20  ל=30  מ=40  נ=50  ס=60  ע=70  פ=80  צ=90
ק=100 ר=200 ש=300 ת=400
```

### Découvertes célèbres

#### אהבה (Ahava - Amour) = 13

```
א(1) + ה(5) + ב(2) + ה(5) = 13
```

#### אחד (Ehad - Un) = 13

```
א(1) + ח(8) + ד(4) = 13
```

**Révélation** : L'amour et l'unité ont la même essence !

#### יהוה (Hashem - Le Nom) = 26

```
י(10) + ה(5) + ו(6) + ה(5) = 26
```

#### משיח (Mashiah - Messie) = 358

```
מ(40) + ש(300) + י(10) + ח(8) = 358
```

Étonnamment, **נחש (Nahash - Serpent) = 358** aussi !
→ Le serpent (mal) sera transformé en Messie (rédemption)

### Méthodes de calcul

1. **Standard** : Valeurs classiques (ci-dessus)
2. **Katan** : Réduction à un chiffre (1-9)
3. **Sidouri** : Ordre alphabétique (א=1, ב=2... ת=22)
4. **At-Bash** : Après substitution At-Bash

### Utilisation API

```bash
curl -X POST "http://localhost:8000/api/v1/codes/guematrie" \
  -H "Content-Type: application/json" \
  -d '{
    "texte_hebreu": "אהבה",
    "methode": "standard"
  }'
```

### Utilisation Python

```python
from ai.codes_torah import AnalyseurCodesTorah

analyseur = AnalyseurCodesTorah()
resultat = analyseur.calculer_guematrie("אהבה")
print(f"Valeur: {resultat.valeur}")
print(f"Correspondances: {resultat.correspondances}")
```

---

## 🔍 2. ELS - Equidistant Letter Sequences

### Principe

Recherche de mots dont les lettres apparaissent à **intervalles réguliers** dans le texte.

Rendu célèbre par "The Bible Code" (1997).

### Exemple

Chercher "תורה" (Torah) avec intervalle 7 :

```
Position 0:   ת
Position 7:   ו
Position 14:  ר
Position 21:  ה
→ TORAH trouvé !
```

### Signification

- **Intervalles courts** (1-10) : Très significatifs
- **Intervalles moyens** (11-50) : Intéressants
- **Intervalles longs** (>50) : Possibles coïncidences

### Utilisation API

```bash
curl -X POST "http://localhost:8000/api/v1/codes/els" \
  -H "Content-Type: application/json" \
  -d '{
    "texte_complet": "בראשיתבראאלהים...",
    "mot_recherche": "תורה",
    "intervalle_min": 1,
    "intervalle_max": 50
  }'
```

### Utilisation Python

```python
analyseur = AnalyseurCodesTorah()
resultats = analyseur.rechercher_els(
    texte_complet="בראשיתבראאלהים...",
    mot_recherche="תורה",
    intervalle_min=1,
    intervalle_max=50
)

for r in resultats:
    print(f"Trouvé à position {r.position_debut}, intervalle {r.intervalle}")
```

---

## 📝 3. NOTARIKON (נוטריקון)

### Principe

Deux modes :

1. **Acronymes** : Première lettre de chaque mot
2. **Expansion** : Chaque lettre devient un mot

### Exemples d'acronymes

#### שמע ישראל (Shema Israel)

```
ש (de שמע) + י (de ישראל) = שי
```

### Exemples d'expansions

#### אמן (Amen)

```
א = אל (El - Dieu)
מ = מלך (Melekh - Roi)
ן = נאמן (Neeman - Fidèle)

→ "Dieu Roi Fidèle"
```

#### רמב״ם (Rambam)

```
ר = רבי (Rabbi)
מ = משה (Moshe)
ב = בן (ben - fils de)
ם = מימון (Maimon)

→ Rabbi Moshe ben Maimon (Maimonide)
```

### Utilisation API

```bash
curl -X POST "http://localhost:8000/api/v1/codes/notarikon" \
  -H "Content-Type: application/json" \
  -d '{
    "texte": "אמן",
    "mode": "expansion"
  }'
```

---

## 🔄 4. AT-BASH (אתב״ש)

### Principe

Substitution **symétrique** des lettres :
- Première ↔ Dernière
- Deuxième ↔ Avant-dernière
- etc.

### Table de substitution

```
א ↔ ת    ב ↔ ש    ג ↔ ר    ד ↔ ק
ה ↔ צ    ו ↔ פ    ז ↔ ע    ח ↔ ס
ט ↔ נ    י ↔ מ    כ ↔ ל
```

### Exemple biblique célèbre

#### בבל (Babel)

```
ב → ש
ב → ש
ל → כ

בבל → ששך (Sheshakh)
```

**Référence** : Jérémie 25:26 et 51:41 mentionnent "Sheshakh" comme nom codé de Babylone !

### Utilisation API

```bash
curl -X POST "http://localhost:8000/api/v1/codes/atbash" \
  -H "Content-Type: application/json" \
  -d '{
    "texte": "בבל"
  }'
```

### Utilisation Python

```python
analyseur = AnalyseurCodesTorah()
resultat = analyseur.appliquer_atbash("בבל")
print(f"At-Bash: {resultat}")  # → ששך
```

---

## 🔀 5. TÉMOURAH (תמורה)

### Principe

**Permutations** des lettres pour révéler de nouveaux sens.

### Types de permutations

1. **Simple** : Toutes les permutations possibles (pour mots courts)
2. **Cyclique** : Rotations (ABC → BCA → CAB)
3. **At-Bash** : Substitution inversée

### Exemple : אור (Or - Lumière)

Rotations cycliques :
```
אור → Original
ורא → Rotation 1
ראו → Rotation 2 ("Voyez" en hébreu!)
```

**Révélation** : La lumière (אור) permet de voir (ראו) !

### Utilisation API

```bash
curl -X POST "http://localhost:8000/api/v1/codes/temourah" \
  -H "Content-Type: application/json" \
  -d '{
    "texte": "אור",
    "type_permutation": "cyclique"
  }'
```

---

## 🎯 Analyse Complète

### Analyser un mot avec TOUTES les méthodes

```bash
curl -X POST "http://localhost:8000/api/v1/codes/analyser-tout" \
  -H "Content-Type: application/json" \
  -d '{
    "texte_hebreu": "שלום"
  }'
```

Retourne :
- Guématrie (standard, katan, sidouri)
- Notarikon (acronyme, expansion)
- At-Bash
- Témourah (cyclique)

---

## 📚 Références Kabbalistiques

Ces méthodes proviennent de :

### Sefer Yetzirah (ספר יצירה)
**Livre de la Formation** - IIe-VIe siècle
- Premier texte kabbalistique
- Décrit les 22 lettres hébraïques comme fondation de la Création
- Base de la guématrie

### Bahir (בהיר)
**Livre de la Clarté** - XIIe siècle
- Développe le notarikon et la témourah
- Première mention des Sephirot

### Zohar (זוהר)
**Livre de la Splendeur** - XIIIe siècle
- Œuvre maîtresse de la Kabbale
- Utilise extensivement ces méthodes
- Révèle les sens cachés de chaque lettre

---

## 🧪 Tests et Exemples

### Lancer les tests

```bash
python test_codes_torah.py
```

### Exemples interactifs

```bash
python ai/codes_torah.py
```

### Tests avec l'API

1. Démarrer le serveur :
```bash
uvicorn api.main:app --reload
```

2. Accéder à la documentation interactive :
```
http://localhost:8000/docs
```

3. Tester les endpoints dans la section **"Codes Torah"**

---

## 💡 Découvertes Célèbres

### 1. Amour = Unité

```
אהבה (Ahava - Amour) = 13
אחד (Ehad - Un) = 13
```

**Enseignement** : L'amour véritable crée l'unité

### 2. Le Nom Divin

```
יהוה (Hashem) = 26
26 = 2 × 13 (Ahava × 2)
```

**Enseignement** : Dieu est amour multiplié

### 3. Messie et Serpent

```
משיח (Mashiah - Messie) = 358
נחש (Nahash - Serpent) = 358
```

**Enseignement** : Le Messie transformera le mal (serpent) en bien

### 4. Israël et Jacob

```
ישראל (Israel) = 541
יעקב (Yaakov - Jacob) = 182
541 - 182 = 359
```

Quand Jacob devient Israel, il gagne 359 = נ'ס'ט (miracle) !

---

## 🔧 API Endpoints Disponibles

| Endpoint | Méthode | Description |
|----------|---------|-------------|
| `/api/v1/codes/guematrie` | POST | Calcul guématrique |
| `/api/v1/codes/els` | POST | Recherche ELS |
| `/api/v1/codes/notarikon` | POST | Analyse notarikon |
| `/api/v1/codes/atbash` | POST | Substitution At-Bash |
| `/api/v1/codes/temourah` | POST | Permutations |
| `/api/v1/codes/analyser-tout` | POST | Analyse complète |
| `/api/v1/codes/exemples` | GET | Exemples célèbres |

---

## ⚠️ Notes Importantes

### Utilisation Spirituelle

Ces méthodes sont des **outils d'étude** sacrés, pas de la divination.

**Utilisations appropriées** :
- ✅ Approfondir la compréhension du texte
- ✅ Découvrir des connexions spirituelles
- ✅ Méditer sur les enseignements cachés

**À éviter** :
- ❌ Prédire l'avenir
- ❌ Chercher des messages personnels
- ❌ Utiliser pour des décisions halakhiques

### Validité Scientifique

- Les codes ELS sont **controversés** scientifiquement
- La guématrie est **acceptée** dans la tradition juive
- Ces méthodes ont une valeur **spirituelle et pédagogique**

### Respect du Sacré

La Torah est le texte le plus sacré du judaïsme.
Approchez ces codes avec :
- 🙏 Respect
- 💙 Humilité
- 📖 Désir sincère d'apprendre

---

## 🚀 Pour Aller Plus Loin

### Livres Recommandés

1. **"The Wisdom in the Hebrew Alphabet"** - Michael Munk
2. **"Sefer Yetzirah: The Book of Creation"** - Aryeh Kaplan
3. **"The Bahir"** - Aryeh Kaplan (traduction et commentaire)
4. **"Inner Space"** - Rabbi Aryeh Kaplan

### Ressources en Ligne

- [Sefaria.org](https://www.sefaria.org) - Textes sources
- [Chabad.org](https://www.chabad.org/kabbalah) - Enseignements kabbalistiques
- [Aish.com](https://www.aish.com) - Articles pédagogiques

---

## 🙏 Conclusion

> "Les secrets de la Torah sont révélés à ceux qui l'étudient avec amour et pureté de cœur"
>
> — Zohar

Ces codes ne sont pas des "tricks" ou des curiosités, mais des **portes d'entrée** vers les dimensions profondes de la Torah.

Chaque découverte doit renforcer :
- L'émerveillement devant la sagesse divine
- L'amour de l'étude
- L'humilité face au mystère

**B'hatzla'ha** (Bonne chance) dans votre exploration ! 🔯

---

*"Tourne-la et retourne-la, car tout est en elle"* — Pirke Avot 5:22
