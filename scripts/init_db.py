"""
Script d'initialisation de la base de données Torah AI
"""

import sys
import os
from pathlib import Path

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent.parent))

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_database(db_name: str = "torah_ai", user: str = "postgres", password: str = "postgres", host: str = "localhost"):
    """Crée la base de données si elle n'existe pas"""
    try:
        # Connexion à la base postgres par défaut
        conn = psycopg2.connect(
            dbname="postgres",
            user=user,
            password=password,
            host=host
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        # Vérifier si la base existe
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname='{db_name}'")
        exists = cursor.fetchone()

        if not exists:
            cursor.execute(f"CREATE DATABASE {db_name}")
            logger.info(f"Base de données '{db_name}' créée avec succès")
        else:
            logger.info(f"Base de données '{db_name}' existe déjà")

        cursor.close()
        conn.close()

    except Exception as e:
        logger.error(f"Erreur lors de la création de la base: {str(e)}")
        raise


def init_schema(db_name: str = "torah_ai", user: str = "postgres", password: str = "postgres", host: str = "localhost"):
    """Initialise le schéma de la base de données"""
    try:
        # Connexion à la base torah_ai
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host
        )
        cursor = conn.cursor()

        # Lire le fichier schema.sql
        schema_path = Path(__file__).parent.parent / "database" / "schema.sql"

        if not schema_path.exists():
            logger.error(f"Fichier schema.sql non trouvé: {schema_path}")
            return

        with open(schema_path, 'r', encoding='utf-8') as f:
            schema_sql = f.read()

        # Exécuter le schéma
        cursor.execute(schema_sql)
        conn.commit()

        logger.info("Schéma de base de données initialisé avec succès")

        cursor.close()
        conn.close()

    except Exception as e:
        logger.error(f"Erreur lors de l'initialisation du schéma: {str(e)}")
        raise


def load_sample_data(db_name: str = "torah_ai", user: str = "postgres", password: str = "postgres", host: str = "localhost"):
    """Charge des données d'exemple"""
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host
        )
        cursor = conn.cursor()

        # Les catégories et livres de base sont déjà dans le schema.sql
        # Ici on peut ajouter quelques passages d'exemple

        # Exemple: Genèse 1:1
        cursor.execute("""
            INSERT INTO chapitres (livre_id, numero, nom, nom_hebreu)
            VALUES (
                (SELECT id FROM livres WHERE nom_hebreu = 'בראשית'),
                1,
                'Création',
                'בראשית'
            )
            ON CONFLICT (livre_id, numero) DO NOTHING
            RETURNING id
        """)

        result = cursor.fetchone()
        if result:
            chapitre_id = result[0]

            cursor.execute("""
                INSERT INTO passages (chapitre_id, numero, texte_hebreu, texte_francais, texte_anglais)
                VALUES (%s, 1, %s, %s, %s)
                ON CONFLICT (chapitre_id, numero) DO NOTHING
            """, (
                chapitre_id,
                'בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ',
                'Au commencement, Dieu créa le ciel et la terre',
                'In the beginning, God created the heavens and the earth'
            ))

        conn.commit()
        logger.info("Données d'exemple chargées")

        cursor.close()
        conn.close()

    except Exception as e:
        logger.error(f"Erreur lors du chargement des données: {str(e)}")
        raise


def main():
    """Fonction principale"""
    logger.info("=== Initialisation de Torah AI - Rav Virtuel ===")

    # Configuration (à adapter selon votre environnement)
    DB_NAME = os.getenv("DB_NAME", "torah_ai")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
    DB_HOST = os.getenv("DB_HOST", "localhost")

    try:
        # 1. Créer la base de données
        logger.info("Étape 1: Création de la base de données")
        create_database(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST)

        # 2. Initialiser le schéma
        logger.info("Étape 2: Initialisation du schéma")
        init_schema(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST)

        # 3. Charger des données d'exemple
        logger.info("Étape 3: Chargement des données d'exemple")
        load_sample_data(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST)

        logger.info("=== Initialisation terminée avec succès! ===")
        logger.info(f"Base de données '{DB_NAME}' prête à l'emploi")
        logger.info("Vous pouvez maintenant lancer l'API avec: uvicorn api.main:app --reload")

    except Exception as e:
        logger.error(f"Échec de l'initialisation: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
