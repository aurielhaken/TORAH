"""
Initialisation de la base de données SQLite pour Torah AI
Version simplifiée pour démarrage rapide
"""

import sys
import os
from pathlib import Path

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import logging

# Import des modèles
from models.base import Base, Categorie, Livre, Chapitre, Passage, Glossaire

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_database():
    """Initialise la base de données SQLite"""

    db_path = Path(__file__).parent.parent / "torah_ai.db"
    database_url = f"sqlite:///{db_path}"

    logger.info(f"Création de la base de données: {db_path}")

    # Créer l'engine
    engine = create_engine(database_url, echo=False)

    # Créer toutes les tables
    logger.info("Création des tables...")
    Base.metadata.create_all(engine)

    # Créer une session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Vérifier si déjà initialisé
        count = session.query(Categorie).count()
        if count > 0:
            logger.info("Base de données déjà initialisée")
            return

        logger.info("Insertion des données initiales...")

        # Catégories principales
        categories_data = [
            ("Torah", "תורה", "Les cinq livres de Moïse (Pentateuque)", 1),
            ("Neviim", "נביאים", "Les Prophètes", 2),
            ("Ketouvim", "כתובים", "Les Écrits", 3),
            ("Mishna", "משנה", "Première codification de la loi orale", 4),
            ("Talmud Bavli", "תלמוד בבלי", "Talmud de Babylone (Guemara)", 5),
            ("Talmud Yerushalmi", "תלמוד ירושלמי", "Talmud de Jérusalem", 6),
            ("Kabbalah", "קבלה", "Enseignements mystiques du judaïsme", 7),
            ("Halakha", "הלכה", "Codes de loi juive", 8),
            ("Commentaires", "פרושים", "Commentaires des grands Sages", 9),
        ]

        categories = {}
        for nom, nom_hebreu, description, ordre in categories_data:
            cat = Categorie(
                nom=nom,
                nom_hebreu=nom_hebreu,
                description=description,
                ordre=ordre
            )
            session.add(cat)
            session.flush()
            categories[nom] = cat
            logger.info(f"  Catégorie créée: {nom}")

        # Les cinq livres de la Torah
        livres_torah = [
            ("Genèse", "בראשית", "Genesis", 1),
            ("Exode", "שמות", "Exodus", 2),
            ("Lévitique", "ויקרא", "Leviticus", 3),
            ("Nombres", "במדבר", "Numbers", 4),
            ("Deutéronome", "דברים", "Deuteronomy", 5),
        ]

        livres = {}
        for nom, nom_hebreu, nom_anglais, ordre in livres_torah:
            livre = Livre(
                categorie_id=categories["Torah"].id,
                nom=nom,
                nom_hebreu=nom_hebreu,
                nom_anglais=nom_anglais,
                ordre=ordre
            )
            session.add(livre)
            session.flush()
            livres[nom] = livre
            logger.info(f"  Livre créé: {nom}")

        # Premier chapitre de la Genèse
        chapitre1 = Chapitre(
            livre_id=livres["Genèse"].id,
            numero=1,
            nom="Création",
            nom_hebreu="בראשית"
        )
        session.add(chapitre1)
        session.flush()
        logger.info("  Chapitre créé: Genèse 1")

        # Premiers versets de la Genèse
        versets = [
            (1, "בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ",
             "Au commencement, Dieu créa le ciel et la terre",
             "In the beginning, God created the heavens and the earth"),
            (2, "וְהָאָרֶץ הָיְתָה תֹהוּ וָבֹהוּ וְחֹשֶׁךְ עַל־פְּנֵי תְהוֹם וְרוּחַ אֱלֹהִים מְרַחֶפֶת עַל־פְּנֵי הַמָּיִם",
             "La terre était informe et vide, et les ténèbres couvraient la surface de l'abîme, et l'esprit de Dieu planait au-dessus des eaux",
             "The earth was formless and empty, and darkness was over the surface of the deep, and the Spirit of God was hovering over the waters"),
            (3, "וַיֹּאמֶר אֱלֹהִים יְהִי אוֹר וַיְהִי־אוֹר",
             "Dieu dit: Que la lumière soit! Et la lumière fut",
             "And God said, Let there be light, and there was light"),
        ]

        for numero, hebreu, francais, anglais in versets:
            passage = Passage(
                chapitre_id=chapitre1.id,
                numero=numero,
                texte_hebreu=hebreu,
                texte_francais=francais,
                texte_anglais=anglais
            )
            session.add(passage)
            logger.info(f"  Verset créé: Genèse 1:{numero}")

        # Termes du glossaire
        glossaire_termes = [
            ("תורה", "Torah", "Torah/Enseignement", "Torah/Teaching", "Les cinq livres de Moïse et par extension tout l'enseignement juif", "terme général"),
            ("הלכה", "Halakha", "Loi juive", "Jewish Law", "La loi juive, la manière de marcher dans la voie de Dieu", "terme halakhique"),
            ("קבלה", "Kabbalah", "Réception/Tradition", "Kabbalah/Received Tradition", "La tradition mystique du judaïsme", "concept kabbalistique"),
            ("משנה", "Mishna", "Répétition/Étude", "Mishna", "Première codification écrite de la loi orale", "texte fondamental"),
            ("גמרא", "Guemara", "Achèvement/Étude", "Gemara", "Discussions et analyses de la Mishna", "texte fondamental"),
            ("מצוה", "Mitzva", "Commandement", "Commandment", "Un des 613 commandements divins", "terme halakhique"),
            ("תלמוד", "Talmud", "Étude", "Talmud", "Mishna + Guemara, corpus central de la loi orale", "texte fondamental"),
            ("שבת", "Shabbat", "Repos", "Sabbath", "Le jour de repos, septième jour de la semaine", "mitzva"),
        ]

        for terme_hebreu, translit, trad_fr, trad_en, definition, categorie in glossaire_termes:
            terme = Glossaire(
                terme_hebreu=terme_hebreu,
                transliteration=translit,
                traduction_francais=trad_fr,
                traduction_anglais=trad_en,
                definition_courte=definition,
                categorie=categorie
            )
            session.add(terme)
            logger.info(f"  Terme du glossaire créé: {translit}")

        # Commit toutes les modifications
        session.commit()
        logger.info("✓ Base de données initialisée avec succès!")
        logger.info(f"✓ Fichier créé: {db_path}")

        # Afficher les statistiques
        stats = {
            "Catégories": session.query(Categorie).count(),
            "Livres": session.query(Livre).count(),
            "Chapitres": session.query(Chapitre).count(),
            "Passages": session.query(Passage).count(),
            "Termes glossaire": session.query(Glossaire).count(),
        }

        logger.info("\n=== Statistiques ===")
        for key, value in stats.items():
            logger.info(f"  {key}: {value}")

    except Exception as e:
        session.rollback()
        logger.error(f"Erreur lors de l'initialisation: {e}")
        raise
    finally:
        session.close()


if __name__ == "__main__":
    logger.info("=== Initialisation Torah AI - Rav Virtuel (SQLite) ===\n")
    init_database()
    logger.info("\n=== Prêt à lancer l'API! ===")
    logger.info("Commande: uvicorn api.main:app --reload")
