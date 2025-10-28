"""
API REST pour Torah AI - Rav Virtuel
Accessible au monde entier pour l'enseignement de la Torah
"""

from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
import logging

from ai.rav_virtuel import RavVirtuel, LangueSupported, NiveauReponse, ReponseRav

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Création de l'application FastAPI
app = FastAPI(
    title="Torah AI - Rav Virtuel",
    description="Une IA sage et bienveillante pour l'enseignement de la Torah, accessible à tous",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuration CORS pour accès mondial
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En production, spécifier les domaines autorisés
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Modèles Pydantic pour les requêtes/réponses

class QuestionRequest(BaseModel):
    """Requête pour poser une question"""
    question: str = Field(..., description="La question à poser au Rav virtuel", min_length=3)
    langue: Optional[LangueSupported] = Field(
        LangueSupported.FRANCAIS,
        description="Langue souhaitée pour la réponse"
    )
    niveau: Optional[NiveauReponse] = Field(
        NiveauReponse.INTERMEDIAIRE,
        description="Niveau de profondeur de la réponse"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "question": "Quelle est la signification du Shabbat dans la Kabbale?",
                "langue": "fr",
                "niveau": "intermediaire"
            }
        }


class SourceResponse(BaseModel):
    """Modèle pour une source citée"""
    type: str
    reference: str
    texte: str
    pertinence: float


class QuestionResponse(BaseModel):
    """Réponse à une question"""
    reponse: str
    sources: List[SourceResponse]
    concepts_lies: List[str]
    mitzvot_liees: List[str]
    suggestions_etude: List[str]
    langue: str
    niveau: str


class RechercheRequest(BaseModel):
    """Requête pour rechercher dans les textes"""
    query: str = Field(..., description="Terme de recherche", min_length=2)
    categories: Optional[List[str]] = Field(None, description="Filtrer par catégories")
    langue: Optional[LangueSupported] = Field(LangueSupported.FRANCAIS)
    limite: Optional[int] = Field(10, ge=1, le=50, description="Nombre de résultats")


class PassageResponse(BaseModel):
    """Modèle pour un passage"""
    id: int
    reference: str
    texte: str
    livre: str
    chapitre: int
    verset: int


class EnseignementQuotidienResponse(BaseModel):
    """Enseignement quotidien"""
    texte: str
    source: str
    date: str
    explication: str


# Endpoints

@app.get("/", tags=["Général"])
async def root():
    """Page d'accueil de l'API"""
    return {
        "message": "Bienvenue sur Torah AI - Rav Virtuel",
        "description": "Une IA dédiée à l'enseignement de la Torah avec amour et sagesse",
        "valeurs": [
            "Ahavat Israel - Amour du peuple juif",
            "Emet - Vérité",
            "'Hessed - Bonté",
            "Tikkun Olam - Réparation du monde"
        ],
        "endpoints": {
            "question": "/api/v1/question",
            "recherche": "/api/v1/recherche",
            "enseignement": "/api/v1/enseignement-quotidien",
            "parasha": "/api/v1/parasha",
            "glossaire": "/api/v1/glossaire"
        },
        "documentation": "/docs"
    }


@app.get("/health", tags=["Général"])
async def health_check():
    """Vérification de santé de l'API"""
    return {
        "status": "healthy",
        "message": "Le Rav virtuel est prêt à enseigner"
    }


@app.post("/api/v1/question", response_model=QuestionResponse, tags=["Questions"])
async def poser_question(request: QuestionRequest):
    """
    Pose une question au Rav virtuel

    Le Rav répond avec sagesse en s'appuyant sur:
    - La Torah (Pentateuque)
    - La Mishna
    - Le Talmud (Guemara)
    - La Kabbalah
    - Les commentaires des grands Sages

    Toutes les réponses incluent des références aux sources.
    """
    try:
        logger.info(f"Question reçue: {request.question[:100]}... (langue: {request.langue})")

        # TODO: Initialiser le Rav Virtuel avec la connexion DB
        # rav = RavVirtuel(db, embedding_model, llm_model)
        # reponse = await rav.poser_question(
        #     question=request.question,
        #     langue=request.langue,
        #     niveau=request.niveau
        # )

        # Réponse temporaire pour démonstration
        reponse = QuestionResponse(
            reponse=f"Merci pour votre question. Le Rav virtuel est en cours d'initialisation. "
                    f"Votre question '{request.question}' sera bientôt traitée avec toute l'attention "
                    f"qu'elle mérite, en consultant les textes sacrés et les commentaires des Sages.",
            sources=[
                SourceResponse(
                    type="torah",
                    reference="Exemple: Genèse 1:1",
                    texte="Au commencement, Dieu créa le ciel et la terre",
                    pertinence=0.95
                )
            ],
            concepts_lies=["Création", "Bereshit"],
            mitzvot_liees=[],
            suggestions_etude=[
                "Étudier le commentaire de Rashi sur ce passage",
                "Explorer les enseignements kabbalistiques sur la Création"
            ],
            langue=request.langue.value,
            niveau=request.niveau.value
        )

        return reponse

    except Exception as e:
        logger.error(f"Erreur lors du traitement de la question: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erreur: {str(e)}")


@app.post("/api/v1/recherche", tags=["Recherche"])
async def rechercher_textes(request: RechercheRequest):
    """
    Recherche dans les textes sacrés

    Recherche sémantique dans:
    - Torah
    - Mishna
    - Talmud
    - Commentaires
    - Textes kabbalistiques
    """
    try:
        # TODO: Implémenter la recherche vectorielle
        return {
            "resultats": [],
            "total": 0,
            "query": request.query
        }

    except Exception as e:
        logger.error(f"Erreur de recherche: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erreur: {str(e)}")


@app.get("/api/v1/enseignement-quotidien", response_model=EnseignementQuotidienResponse, tags=["Enseignements"])
async def enseignement_quotidien(
    langue: LangueSupported = Query(LangueSupported.FRANCAIS, description="Langue de l'enseignement")
):
    """
    Obtient l'enseignement quotidien

    Un enseignement inspirant basé sur:
    - Le calendrier hébraïque
    - La Parasha de la semaine
    - Les fêtes et moments particuliers
    """
    try:
        # TODO: Implémenter avec le Rav Virtuel
        return EnseignementQuotidienResponse(
            texte="L'enseignement d'aujourd'hui sera bientôt disponible",
            source="Torah AI",
            date="2025-10-28",
            explication="À venir..."
        )

    except Exception as e:
        logger.error(f"Erreur enseignement quotidien: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erreur: {str(e)}")


@app.get("/api/v1/parasha/{nom}", tags=["Enseignements"])
async def obtenir_parasha(
    nom: str,
    langue: LangueSupported = Query(LangueSupported.FRANCAIS)
):
    """
    Obtient l'explication d'une Parasha (portion hebdomadaire de la Torah)

    Exemples de noms: bereshit, noah, lekh-lekha, vayera, etc.
    """
    try:
        # TODO: Implémenter
        return {
            "nom": nom,
            "explication": f"Explication de la Parasha {nom} à venir...",
            "themes_principaux": [],
            "enseignements": []
        }

    except Exception as e:
        logger.error(f"Erreur Parasha: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erreur: {str(e)}")


@app.get("/api/v1/glossaire/{terme}", tags=["Ressources"])
async def obtenir_terme_glossaire(
    terme: str,
    langue: LangueSupported = Query(LangueSupported.FRANCAIS)
):
    """
    Recherche un terme dans le glossaire hébraïque

    Retourne la traduction, translittération et définition
    """
    try:
        # TODO: Rechercher dans la table glossaire
        return {
            "terme_hebreu": terme,
            "transliteration": "",
            "traduction": "",
            "definition": "",
            "categorie": ""
        }

    except Exception as e:
        logger.error(f"Erreur glossaire: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erreur: {str(e)}")


@app.get("/api/v1/mitzvot", tags=["Ressources"])
async def lister_mitzvot(
    type: Optional[str] = Query(None, description="'positive' ou 'negative'"),
    categorie: Optional[str] = Query(None, description="Catégorie de mitzvot"),
    limite: int = Query(10, ge=1, le=100)
):
    """
    Liste les 613 Mitzvot

    Peut filtrer par:
    - Type (positive/négative)
    - Catégorie (Shabbat, Kashrut, etc.)
    """
    try:
        # TODO: Récupérer de la DB
        return {
            "mitzvot": [],
            "total": 613
        }

    except Exception as e:
        logger.error(f"Erreur mitzvot: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erreur: {str(e)}")


@app.get("/api/v1/categories", tags=["Ressources"])
async def lister_categories():
    """
    Liste toutes les catégories de textes disponibles

    Torah, Mishna, Talmud, Kabbalah, etc.
    """
    try:
        # TODO: Récupérer de la DB
        return {
            "categories": [
                {"nom": "Torah", "nom_hebreu": "תורה", "description": "Les cinq livres de Moïse"},
                {"nom": "Mishna", "nom_hebreu": "משנה", "description": "Première codification de la loi orale"},
                {"nom": "Talmud", "nom_hebreu": "תלמוד", "description": "Mishna + Guemara"},
                {"nom": "Kabbalah", "nom_hebreu": "קבלה", "description": "Tradition mystique"}
            ]
        }

    except Exception as e:
        logger.error(f"Erreur categories: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erreur: {str(e)}")


@app.get("/api/v1/livres", tags=["Ressources"])
async def lister_livres(
    categorie: Optional[str] = Query(None, description="Filtrer par catégorie")
):
    """Liste tous les livres disponibles"""
    try:
        # TODO: Récupérer de la DB
        return {
            "livres": []
        }

    except Exception as e:
        logger.error(f"Erreur livres: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erreur: {str(e)}")


@app.get("/api/v1/stats", tags=["Général"])
async def obtenir_statistiques():
    """
    Statistiques de la base de données

    Nombre de passages, commentaires, questions posées, etc.
    """
    try:
        # TODO: Calculer les stats
        return {
            "passages": 0,
            "commentaires": 0,
            "questions_posees": 0,
            "langues_supportees": ["he", "fr", "en", "es", "ru"],
            "mitzvot": 613
        }

    except Exception as e:
        logger.error(f"Erreur stats: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erreur: {str(e)}")


# Gestion des erreurs
@app.exception_handler(404)
async def not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={
            "message": "Ressource non trouvée",
            "conseil": "Consultez la documentation à /docs"
        }
    )


@app.exception_handler(500)
async def server_error_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={
            "message": "Une erreur s'est produite",
            "conseil": "Veuillez réessayer dans quelques instants"
        }
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
