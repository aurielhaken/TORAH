"""
Analyse des Codes Cachés de la Torah
Méthodes de déchiffrement et d'analyse kabbalistique
"""

from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import re
import logging

logger = logging.getLogger(__name__)


class MethodeCode(str, Enum):
    """Méthodes d'analyse des codes Torah"""
    GUEMATRIE = "guematrie"
    ELS = "els"  # Equidistant Letter Sequences
    NOTARIKON = "notarikon"
    TEMOURAH = "temourah"
    ATBASH = "atbash"


# Table de guématrie hébraïque standard
GUEMATRIE_STANDARD = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 10, 'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40, 'נ': 50, 'ן': 50,
    'ס': 60, 'ע': 70, 'פ': 80, 'ף': 80, 'צ': 90, 'ץ': 90, 'ק': 100,
    'ר': 200, 'ש': 300, 'ת': 400
}

# Table At-Bash (inversion alphabet)
ATBASH_TABLE = {
    'א': 'ת', 'ב': 'ש', 'ג': 'ר', 'ד': 'ק', 'ה': 'צ', 'ו': 'פ', 'ז': 'ע',
    'ח': 'ס', 'ט': 'נ', 'י': 'מ', 'כ': 'ל', 'ל': 'כ', 'מ': 'י', 'נ': 'ט',
    'ס': 'ח', 'ע': 'ז', 'פ': 'ו', 'צ': 'ה', 'ק': 'ד', 'ר': 'ג', 'ש': 'ב', 'ת': 'א',
    'ך': 'ל', 'ם': 'י', 'ן': 'ט', 'ף': 'ו', 'ץ': 'ה'
}


@dataclass
class ResultatGuematrie:
    """Résultat d'analyse guématrique"""
    texte: str
    valeur: int
    methode: str
    correspondances: List[str]  # Autres mots avec même valeur


@dataclass
class ResultatELS:
    """Résultat de recherche ELS"""
    mot_trouve: str
    position_debut: int
    intervalle: int
    contexte: str
    pertinence: float


@dataclass
class ResultatNotarikon:
    """Résultat d'analyse notarikon"""
    texte_source: str
    acronyme: str
    expansion: Optional[str]
    type: str  # "acronyme" ou "expansion"


class AnalyseurCodesTorah:
    """
    Analyseur des codes cachés dans la Torah

    Implémente les principales méthodes kabbalistiques:
    - Guématrie (valeurs numériques)
    - ELS (séquences équidistantes)
    - Notarikon (acronymes)
    - Témourah (permutations)
    - At-Bash (substitution)
    """

    def __init__(self):
        self.guematrie_table = GUEMATRIE_STANDARD
        self.atbash_table = ATBASH_TABLE
        logger.info("Analyseur de codes Torah initialisé")

    # ========== GUÉMATRIE ==========

    def calculer_guematrie(
        self,
        texte_hebreu: str,
        methode: str = "standard"
    ) -> ResultatGuematrie:
        """
        Calcule la valeur guématrique d'un texte hébreu

        Méthodes disponibles:
        - standard: Guématrie classique
        - gadol: Valeurs étendues (milliers)
        - katan: Réduction à un chiffre
        - sidouri: Ordre alphabétique simple (1-22)
        - atbash: Après substitution At-Bash

        Args:
            texte_hebreu: Texte en hébreu
            methode: Méthode de calcul

        Returns:
            ResultatGuematrie avec valeur et correspondances
        """
        # Nettoyer le texte (garder uniquement lettres hébraïques)
        texte_propre = self._nettoyer_hebreu(texte_hebreu)

        if methode == "standard":
            valeur = self._guematrie_standard(texte_propre)
        elif methode == "katan":
            valeur = self._guematrie_katan(texte_propre)
        elif methode == "sidouri":
            valeur = self._guematrie_sidouri(texte_propre)
        elif methode == "atbash":
            texte_atbash = self.appliquer_atbash(texte_propre)
            valeur = self._guematrie_standard(texte_atbash)
        else:
            valeur = self._guematrie_standard(texte_propre)

        # Chercher des correspondances (mots avec même valeur)
        correspondances = self._trouver_correspondances_guematrie(valeur)

        return ResultatGuematrie(
            texte=texte_hebreu,
            valeur=valeur,
            methode=methode,
            correspondances=correspondances
        )

    def _guematrie_standard(self, texte: str) -> int:
        """Calcul standard de guématrie"""
        return sum(self.guematrie_table.get(lettre, 0) for lettre in texte)

    def _guematrie_katan(self, texte: str) -> int:
        """Guématrie réduite (réduction à un chiffre)"""
        valeur = self._guematrie_standard(texte)
        while valeur > 9:
            valeur = sum(int(d) for d in str(valeur))
        return valeur

    def _guematrie_sidouri(self, texte: str) -> int:
        """Guématrie selon ordre alphabétique simple (1-22)"""
        alphabet_ordre = 'אבגדהוזחטיכלמנסעפצקרשת'
        return sum(alphabet_ordre.index(lettre) + 1
                   for lettre in texte if lettre in alphabet_ordre)

    def _trouver_correspondances_guematrie(self, valeur: int) -> List[str]:
        """Trouve des mots/concepts célèbres avec cette valeur"""
        # Base de données de correspondances connues
        correspondances_celebres = {
            13: ["אהבה (Ahava - Amour)", "אחד (Ehad - Un)"],
            26: ["יהוה (Hashem - Le Nom)", "הוי (Hava - Être)"],
            86: ["אלהים (Elohim - Dieu)"],
            358: ["משיח (Mashiah - Messie)", "נחש (Nahash - Serpent)"],
            314: ["שדי (Shaddai)", "מטטרון (Métatron)"],
            620: ["כתר (Keter - Couronne)"],
            207: ["אור (Or - Lumière)"],
            64: ["דין (Din - Jugement)"],
            72: ["חסד (Hessed - Bonté)"],
            216: ["גבורה (Guevoura - Force)"],
            273: ["אברהם (Avraham)"],
            208: ["יצחק (Yitzhak)"],
            181: ["יעקב (Yaakov)"],
            345: ["משה (Moshe)"],
            541: ["ישראל (Israel)"],
            80: ["יסוד (Yesod - Fondation)"],
            640: ["שמע (Shema - Écoute)"],
            1480: ["משיח בן דוד (Mashiah ben David)"]
        }

        return correspondances_celebres.get(valeur, [])

    # ========== ELS (Equidistant Letter Sequences) ==========

    def rechercher_els(
        self,
        texte_complet: str,
        mot_recherche: str,
        intervalle_min: int = 1,
        intervalle_max: int = 100
    ) -> List[ResultatELS]:
        """
        Recherche des séquences équidistantes (codes Bible)

        Cherche un mot dont les lettres apparaissent à intervalles réguliers

        Args:
            texte_complet: Texte complet à analyser (sans espaces)
            mot_recherche: Mot à rechercher en ELS
            intervalle_min: Intervalle minimum à tester
            intervalle_max: Intervalle maximum à tester

        Returns:
            Liste de ResultatELS trouvés
        """
        resultats = []
        texte_propre = self._nettoyer_hebreu(texte_complet)
        mot_propre = self._nettoyer_hebreu(mot_recherche)

        if not mot_propre or len(mot_propre) < 2:
            return resultats

        # Tester différents intervalles
        for intervalle in range(intervalle_min, min(intervalle_max, len(texte_propre) // len(mot_propre)) + 1):
            # Tester chaque position de départ possible
            for debut in range(len(texte_propre)):
                trouve = True
                positions = []

                # Vérifier si le mot peut être formé avec cet intervalle
                for i, lettre in enumerate(mot_propre):
                    pos = debut + (i * intervalle)
                    if pos >= len(texte_propre):
                        trouve = False
                        break
                    if texte_propre[pos] != lettre:
                        trouve = False
                        break
                    positions.append(pos)

                if trouve:
                    # Extraire le contexte
                    pos_fin = positions[-1]
                    contexte_debut = max(0, debut - 20)
                    contexte_fin = min(len(texte_propre), pos_fin + 20)
                    contexte = texte_propre[contexte_debut:contexte_fin]

                    # Calculer pertinence (intervalles plus courts = plus pertinents)
                    pertinence = 1.0 / (intervalle ** 0.5)

                    resultats.append(ResultatELS(
                        mot_trouve=mot_recherche,
                        position_debut=debut,
                        intervalle=intervalle,
                        contexte=contexte,
                        pertinence=pertinence
                    ))

        # Trier par pertinence
        resultats.sort(key=lambda x: x.pertinence, reverse=True)
        return resultats[:10]  # Top 10 résultats

    # ========== NOTARIKON ==========

    def analyser_notarikon(
        self,
        texte: str,
        mode: str = "acronyme"
    ) -> ResultatNotarikon:
        """
        Analyse notarikon (acronymes et expansions)

        Mode "acronyme": Prend première lettre de chaque mot
        Mode "expansion": Chaque lettre devient un mot

        Args:
            texte: Texte hébreu à analyser
            mode: "acronyme" ou "expansion"

        Returns:
            ResultatNotarikon avec l'analyse
        """
        if mode == "acronyme":
            # Prendre première lettre de chaque mot
            mots = texte.split()
            acronyme = ''.join(
                self._nettoyer_hebreu(mot)[0]
                for mot in mots if self._nettoyer_hebreu(mot)
            )

            return ResultatNotarikon(
                texte_source=texte,
                acronyme=acronyme,
                expansion=None,
                type="acronyme"
            )

        elif mode == "expansion":
            # Chercher des expansions connues
            expansions_connues = {
                'אמן': 'אל מלך נאמן (El Melekh Neeman)',
                'ארי': 'אליהו רבי יוסף (Eliyahu Rabbi Yossef)',
                'רמב״ם': 'רבי משה בן מימון (Rabbi Moshe ben Maimon)',
                'רש״י': 'רבי שלמה יצחקי (Rabbi Shlomo Yitzhaki)',
            }

            texte_propre = self._nettoyer_hebreu(texte)
            expansion = expansions_connues.get(texte_propre)

            return ResultatNotarikon(
                texte_source=texte,
                acronyme=texte_propre,
                expansion=expansion,
                type="expansion"
            )

        return ResultatNotarikon(texte, "", None, mode)

    # ========== AT-BASH ==========

    def appliquer_atbash(self, texte: str) -> str:
        """
        Applique la substitution At-Bash (א↔ת, ב↔ש, etc.)

        Args:
            texte: Texte hébreu

        Returns:
            Texte après substitution At-Bash
        """
        resultat = []
        for lettre in texte:
            resultat.append(self.atbash_table.get(lettre, lettre))
        return ''.join(resultat)

    def decoder_atbash(self, texte: str) -> str:
        """
        Décode un texte At-Bash (même opération qu'encoder)

        Args:
            texte: Texte encodé en At-Bash

        Returns:
            Texte décodé
        """
        return self.appliquer_atbash(texte)  # At-Bash est symétrique

    # ========== TÉMOURAH ==========

    def analyser_temourah(
        self,
        texte: str,
        type_permutation: str = "simple"
    ) -> List[str]:
        """
        Analyse Témourah (permutations de lettres)

        Types de permutations:
        - simple: Permutations directes
        - cyclique: Rotations
        - atbash: Substitution inversée

        Args:
            texte: Texte hébreu
            type_permutation: Type de permutation

        Returns:
            Liste de variantes possibles
        """
        texte_propre = self._nettoyer_hebreu(texte)
        variantes = []

        if type_permutation == "simple":
            # Générer quelques permutations intéressantes
            # (pas toutes pour éviter explosion combinatoire)
            from itertools import permutations
            if len(texte_propre) <= 4:  # Uniquement pour mots courts
                perms = list(permutations(texte_propre))
                variantes = [''.join(p) for p in perms[:10]]

        elif type_permutation == "cyclique":
            # Rotations cycliques
            for i in range(len(texte_propre)):
                variantes.append(texte_propre[i:] + texte_propre[:i])

        elif type_permutation == "atbash":
            variantes.append(self.appliquer_atbash(texte_propre))

        return variantes

    # ========== UTILITAIRES ==========

    def _nettoyer_hebreu(self, texte: str) -> str:
        """Garde uniquement les lettres hébraïques"""
        # Garder lettres hébraïques (U+0590 à U+05FF)
        return ''.join(c for c in texte if '\u0590' <= c <= '\u05FF')

    def analyser_tout(
        self,
        texte_hebreu: str
    ) -> Dict:
        """
        Analyse complète avec toutes les méthodes

        Args:
            texte_hebreu: Texte hébreu à analyser

        Returns:
            Dictionnaire avec tous les résultats
        """
        resultats = {}

        try:
            # Guématrie
            resultats['guematrie'] = {
                'standard': self.calculer_guematrie(texte_hebreu, "standard").__dict__,
                'katan': self.calculer_guematrie(texte_hebreu, "katan").__dict__,
                'sidouri': self.calculer_guematrie(texte_hebreu, "sidouri").__dict__,
            }
        except Exception as e:
            logger.error(f"Erreur guématrie: {e}")
            resultats['guematrie'] = None

        try:
            # Notarikon
            resultats['notarikon'] = {
                'acronyme': self.analyser_notarikon(texte_hebreu, "acronyme").__dict__,
                'expansion': self.analyser_notarikon(texte_hebreu, "expansion").__dict__,
            }
        except Exception as e:
            logger.error(f"Erreur notarikon: {e}")
            resultats['notarikon'] = None

        try:
            # At-Bash
            resultats['atbash'] = {
                'texte_original': texte_hebreu,
                'texte_atbash': self.appliquer_atbash(self._nettoyer_hebreu(texte_hebreu))
            }
        except Exception as e:
            logger.error(f"Erreur atbash: {e}")
            resultats['atbash'] = None

        try:
            # Témourah
            resultats['temourah'] = {
                'cyclique': self.analyser_temourah(texte_hebreu, "cyclique"),
                'atbash': self.analyser_temourah(texte_hebreu, "atbash")
            }
        except Exception as e:
            logger.error(f"Erreur témourah: {e}")
            resultats['temourah'] = None

        return resultats


# ========== EXEMPLES DE DÉCOUVERTES CÉLÈBRES ==========

DECOUVERTES_CELEBRES = {
    "בראשית (Bereshit - Au commencement)": {
        "guematrie": 913,
        "signification": "Première parole de la Torah",
        "correspondances": ["Équivaut à 'Et craignez' (ויראת) = 913"]
    },
    "שמע (Shema - Écoute)": {
        "guematrie": 410,
        "signification": "Déclaration de foi centrale",
        "notarikon": "Expansion en 'Écoute Israël, l'Éternel notre Dieu, l'Éternel est Un'"
    },
    "משיח (Mashiah - Messie)": {
        "guematrie": 358,
        "signification": "Le Messie attendu",
        "correspondances": ["נחש (Nahash - Serpent) = 358", "Transformation du serpent en rédemption"]
    }
}


def exemples_codes():
    """Exemples d'utilisation de l'analyseur"""
    analyseur = AnalyseurCodesTorah()

    print("=== EXEMPLES D'ANALYSE DES CODES TORAH ===\n")

    # Exemple 1: Guématrie de "Amour" et "Un"
    print("1. Guématrie: אהבה (Ahava - Amour) et אחד (Ehad - Un)")
    ahava = analyseur.calculer_guematrie("אהבה")
    ehad = analyseur.calculer_guematrie("אחד")
    print(f"   אהבה = {ahava.valeur}")
    print(f"   אחד = {ehad.valeur}")
    print(f"   → Les deux valent {ahava.valeur} ! L'amour et l'unité sont liés.\n")

    # Exemple 2: At-Bash sur "Babel"
    print("2. At-Bash: בבל (Babel)")
    babel = "בבל"
    babel_atbash = analyseur.appliquer_atbash(babel)
    print(f"   Original: {babel}")
    print(f"   At-Bash: {babel_atbash}")
    print(f"   → Révèle des significations cachées\n")

    # Exemple 3: Notarikon
    print("3. Notarikon: Shema Israel")
    shema = analyseur.analyser_notarikon("שמע ישראל")
    print(f"   Acronyme: {shema.acronyme}\n")


if __name__ == "__main__":
    exemples_codes()
