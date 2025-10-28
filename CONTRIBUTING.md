# Guide de Contribution - Torah AI

## Bienvenue!

Merci de votre intérêt pour contribuer à Torah AI - Rav Virtuel! Ce projet vise à rendre l'enseignement de la Torah accessible à tous, et chaque contribution compte.

## Valeurs du projet

Avant de contribuer, veuillez vous aligner sur nos valeurs:

1. **Respect de la tradition**: Fidélité aux sources authentiques
2. **Amour et bienveillance**: Ahavat Israel dans chaque ligne de code
3. **Excellence**: Code de qualité, bien testé
4. **Accessibilité**: Penser à tous les niveaux d'utilisateurs
5. **Collaboration**: Respect mutuel et patience

## Comment contribuer?

### 1. Rapporter des bugs

Utilisez GitHub Issues avec le template:

```markdown
**Description du bug**
Description claire et concise.

**Pour reproduire**
1. Aller à '...'
2. Cliquer sur '...'
3. Voir l'erreur

**Comportement attendu**
Ce qui devrait se passer.

**Screenshots**
Si applicable.

**Environnement**
- OS: [ex: Ubuntu 22.04]
- Python: [ex: 3.11]
- Version: [ex: 1.0.0]
```

### 2. Proposer des améliorations

Ouvrez une issue avec le label `enhancement`:
- Décrivez la fonctionnalité souhaitée
- Expliquez pourquoi elle est utile
- Proposez une implémentation si possible

### 3. Ajouter du contenu

#### Textes sacrés
- Assurez-vous de la fiabilité de la source
- Incluez les références complètes
- Respectez les droits d'auteur

#### Traductions
- Précision avant tout
- Consultez plusieurs sources
- Indiquez votre source de traduction

#### Commentaires
- Citez le commentateur correctement
- Vérifiez l'authenticité
- Ajoutez les métadonnées (époque, etc.)

### 4. Améliorer le code

#### Processus

1. **Fork** le repository
2. **Créer une branche**:
   ```bash
   git checkout -b feature/ma-super-fonctionnalite
   ```
3. **Coder** en suivant les standards
4. **Tester** votre code
5. **Commit** avec messages clairs
6. **Push** et créer une Pull Request

#### Standards de code

##### Python

```python
# Utilisez Black pour le formatting
black .

# Vérifiez avec Ruff
ruff check .

# Type hints obligatoires
def ma_fonction(param: str) -> int:
    """
    Docstring claire avec description.

    Args:
        param: Description du paramètre

    Returns:
        Description du retour
    """
    return len(param)

# Nommage
class MaClasse:  # PascalCase
    pass

def ma_fonction():  # snake_case
    pass

CONSTANTE = "valeur"  # UPPER_CASE
```

##### Tests

Tous les nouveaux features doivent avoir des tests:

```python
# tests/test_rav_virtuel.py
import pytest
from ai.rav_virtuel import RavVirtuel

def test_poser_question_simple():
    """Test qu'une question simple obtient une réponse"""
    rav = RavVirtuel(...)
    reponse = await rav.poser_question("Qu'est-ce que le Shabbat?")
    assert reponse is not None
    assert len(reponse.sources) > 0
```

Lancer les tests:
```bash
pytest tests/ -v --cov
```

##### Documentation

- Docstrings pour toutes les fonctions publiques
- Commentaires pour la logique complexe
- README.md à jour
- Exemples d'utilisation

#### Structure des commits

Format:
```
type(scope): Description courte

Description détaillée si nécessaire.

Refs: #123 (si lié à une issue)
```

Types:
- `feat`: Nouvelle fonctionnalité
- `fix`: Correction de bug
- `docs`: Documentation
- `refactor`: Refactoring
- `test`: Ajout de tests
- `chore`: Maintenance

Exemples:
```
feat(api): Ajouter endpoint pour recherche de Halakhot

Permet de rechercher dans les décisions halakhiques
par sujet et autorite.

Refs: #45

---

fix(embeddings): Corriger erreur dimension vecteur

Le modèle retournait 768D mais la DB attendait 1536D.
Mise à jour du schéma.

Refs: #67
```

### 5. Pull Requests

#### Checklist avant PR

- [ ] Code formaté (Black)
- [ ] Linting passé (Ruff)
- [ ] Tests écrits et passent
- [ ] Documentation à jour
- [ ] Pas de secrets/clés API dans le code
- [ ] Messages de commit clairs
- [ ] Branche à jour avec `develop`

#### Template de PR

```markdown
## Description
Décrivez les changements et leur motivation.

## Type de changement
- [ ] Bug fix
- [ ] Nouvelle fonctionnalité
- [ ] Breaking change
- [ ] Documentation

## Tests
Décrivez les tests ajoutés/modifiés.

## Checklist
- [ ] Mon code suit les standards du projet
- [ ] J'ai commenté le code complexe
- [ ] J'ai mis à jour la documentation
- [ ] Mes changements ne génèrent pas de warnings
- [ ] J'ai ajouté des tests
- [ ] Tous les tests passent

## Screenshots
Si applicable.
```

## Domaines de contribution

### 💻 Développement

- **Backend**: Python, FastAPI, SQLAlchemy
- **Base de données**: PostgreSQL, requêtes optimisées
- **IA**: Amélioration des prompts, fine-tuning
- **API**: Nouveaux endpoints, optimisation

### 📚 Contenu

- **Textes**: Import de nouveaux textes sacrés
- **Traductions**: Français, anglais, espagnol, etc.
- **Commentaires**: Ajout de Perushim
- **Kabbalah**: Concepts mystiques

### 🌍 Internationalisation

- **Traductions UI**: Fichiers de langue
- **Contenu**: Traduction des textes
- **Documentation**: Traduction des guides

### 📖 Documentation

- **Guides**: Tutoriels, how-to
- **API**: Documentation des endpoints
- **Architecture**: Diagrammes, explications
- **Vidéos**: Tutoriels vidéo

### 🧪 Tests

- **Tests unitaires**: Couverture du code
- **Tests d'intégration**: Flux complets
- **Tests de charge**: Performance
- **Tests utilisateur**: UX/UI

### 🎨 Design

- **Interface web**: Si frontend développé
- **UX**: Amélioration de l'expérience
- **Accessibilité**: A11y

## Setup développement

### Première fois

```bash
# Clone
git clone <repo>
cd TORAH

# Environnement virtuel
python -m venv venv
source venv/bin/activate

# Dépendances
pip install -r requirements.txt

# Pre-commit hooks
pip install pre-commit
pre-commit install

# Base de données
python scripts/init_db.py

# Tests
pytest
```

### Workflow quotidien

```bash
# Activer venv
source venv/bin/activate

# Nouvelle branche
git checkout -b feature/mon-feature

# Coder...

# Formatter
black .

# Linter
ruff check .

# Tests
pytest

# Commit
git add .
git commit -m "feat(scope): Description"

# Push
git push origin feature/mon-feature
```

## Code of Conduct

### Nos engagements

Nous nous engageons à:
- Être accueillants et inclusifs
- Respecter les différentes opinions
- Accepter les critiques constructives
- Faire preuve d'empathie
- Se concentrer sur le bien de la communauté

### Comportements inacceptables

- Harcèlement sous toute forme
- Langage ou images inappropriés
- Attaques personnelles
- Trolling
- Divulgation d'informations privées

### Application

Les mainteneurs du projet appliqueront ce code de conduite et peuvent:
- Avertir
- Supprimer des commentaires/commits
- Bannir temporairement ou définitivement

## Questions?

- **GitHub Issues**: Pour bugs et features
- **Discussions**: Pour questions générales
- **Email**: [À définir]

## Remerciements

Merci à tous ceux qui contribuent à rendre la Torah accessible au monde entier!

**"כל ישראל ערבים זה בזה" - "Tout Israël est responsable l'un de l'autre"**

---

*Guide de contribution avec amour et gratitude* 🙏
