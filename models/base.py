"""
Modèles de base pour Torah AI - Rav Virtuel
"""

from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector

Base = declarative_base()


class TimeStampMixin:
    """Mixin pour ajouter created_at et updated_at"""
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class Categorie(Base, TimeStampMixin):
    """Catégories de textes (Torah, Mishna, Talmud, etc.)"""
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    nom_hebreu = Column(String(100))
    description = Column(Text)
    parent_id = Column(Integer, ForeignKey('categories.id'))
    ordre = Column(Integer, default=0)

    # Relations
    livres = relationship("Livre", back_populates="categorie")
    parent = relationship("Categorie", remote_side=[id])

    def __repr__(self):
        return f"<Categorie(nom='{self.nom}', nom_hebreu='{self.nom_hebreu}')>"


class Livre(Base, TimeStampMixin):
    """Livres/Sfarim (Genèse, Mishna Berakhot, etc.)"""
    __tablename__ = 'livres'

    id = Column(Integer, primary_key=True)
    categorie_id = Column(Integer, ForeignKey('categories.id'))
    nom = Column(String(200), nullable=False)
    nom_hebreu = Column(String(200))
    nom_anglais = Column(String(200))
    auteur = Column(String(200))
    periode = Column(String(100))
    annee_composition = Column(Integer)
    description = Column(Text)
    ordre = Column(Integer, default=0)

    # Relations
    categorie = relationship("Categorie", back_populates="livres")
    chapitres = relationship("Chapitre", back_populates="livre")

    def __repr__(self):
        return f"<Livre(nom='{self.nom}', nom_hebreu='{self.nom_hebreu}')>"


class Chapitre(Base, TimeStampMixin):
    """Chapitres/Sections"""
    __tablename__ = 'chapitres'

    id = Column(Integer, primary_key=True)
    livre_id = Column(Integer, ForeignKey('livres.id'))
    numero = Column(Integer, nullable=False)
    nom = Column(String(200))
    nom_hebreu = Column(String(200))
    description = Column(Text)

    # Relations
    livre = relationship("Livre", back_populates="chapitres")
    passages = relationship("Passage", back_populates="chapitre")

    def __repr__(self):
        return f"<Chapitre(livre='{self.livre.nom if self.livre else ''}', numero={self.numero})>"


class Passage(Base, TimeStampMixin):
    """Versets/Passages individuels"""
    __tablename__ = 'passages'

    id = Column(Integer, primary_key=True)
    chapitre_id = Column(Integer, ForeignKey('chapitres.id'))
    numero = Column(Integer, nullable=False)
    texte_hebreu = Column(Text, nullable=False)
    texte_francais = Column(Text)
    texte_anglais = Column(Text)
    texte_arameen = Column(Text)
    transliteration = Column(Text)

    # Relations
    chapitre = relationship("Chapitre", back_populates="passages")
    commentaires = relationship("Commentaire", back_populates="passage")
    embeddings = relationship("Embedding", back_populates="passage")

    def __repr__(self):
        return f"<Passage(id={self.id}, numero={self.numero})>"

    def get_reference(self) -> str:
        """Retourne la référence complète du passage"""
        if self.chapitre and self.chapitre.livre:
            return f"{self.chapitre.livre.nom} {self.chapitre.numero}:{self.numero}"
        return f"Passage {self.id}"


class Commentaire(Base, TimeStampMixin):
    """Commentaires des Sages (Rashi, Ramban, etc.)"""
    __tablename__ = 'commentaires'

    id = Column(Integer, primary_key=True)
    passage_id = Column(Integer, ForeignKey('passages.id'))
    commentateur = Column(String(200), nullable=False)
    commentateur_hebreu = Column(String(200))
    epoque = Column(String(100))
    texte_hebreu = Column(Text)
    texte_francais = Column(Text)
    texte_anglais = Column(Text)
    type_commentaire = Column(String(50))  # pshat, remez, drash, sod

    # Relations
    passage = relationship("Passage", back_populates="commentaires")
    embeddings = relationship("Embedding", back_populates="commentaire")

    def __repr__(self):
        return f"<Commentaire(commentateur='{self.commentateur}', passage_id={self.passage_id})>"


class ConceptKabbalah(Base, TimeStampMixin):
    """Concepts kabbalistiques"""
    __tablename__ = 'concepts_kabbalah'

    id = Column(Integer, primary_key=True)
    nom = Column(String(200), nullable=False)
    nom_hebreu = Column(String(200))
    description = Column(Text)
    description_hebreu = Column(Text)
    niveau = Column(String(50))  # nigleh (révélé) ou nistar (caché)
    sefirah = Column(String(100))

    def __repr__(self):
        return f"<ConceptKabbalah(nom='{self.nom}', sefirah='{self.sefirah}')>"


class Mitzva(Base, TimeStampMixin):
    """Les 613 Mitzvot"""
    __tablename__ = 'mitzvot'

    id = Column(Integer, primary_key=True)
    numero = Column(Integer, unique=True, nullable=False)
    type = Column(String(20), nullable=False)  # positive ou negative
    nom = Column(String(300), nullable=False)
    nom_hebreu = Column(String(300))
    description = Column(Text)
    description_hebreu = Column(Text)
    source_torah = Column(Text)
    categorie = Column(String(100))

    def __repr__(self):
        return f"<Mitzva(numero={self.numero}, nom='{self.nom}')>"


class Embedding(Base, TimeStampMixin):
    """Embeddings vectoriels pour la recherche sémantique"""
    __tablename__ = 'embeddings'

    id = Column(Integer, primary_key=True)
    passage_id = Column(Integer, ForeignKey('passages.id'), nullable=True)
    commentaire_id = Column(Integer, ForeignKey('commentaires.id'), nullable=True)
    embedding = Column(Vector(768))  # Dimension pour sentence-transformers
    modele_utilise = Column(String(100))
    langue = Column(String(10))

    # Relations
    passage = relationship("Passage", back_populates="embeddings")
    commentaire = relationship("Commentaire", back_populates="embeddings")

    def __repr__(self):
        return f"<Embedding(id={self.id}, langue='{self.langue}')>"


class Question(Base, TimeStampMixin):
    """Questions posées par les utilisateurs"""
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question_texte = Column(Text, nullable=False)
    langue = Column(String(10))
    utilisateur_id = Column(String(100))

    # Relations
    reponses = relationship("Reponse", back_populates="question")

    def __repr__(self):
        return f"<Question(id={self.id}, langue='{self.langue}')>"


class Reponse(Base, TimeStampMixin):
    """Réponses générées par l'IA"""
    __tablename__ = 'reponses'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    reponse_texte = Column(Text, nullable=False)
    sources_utilisees = Column(JSON)
    modele_ia = Column(String(100))
    rating = Column(Integer)

    # Relations
    question = relationship("Question", back_populates="reponses")

    def __repr__(self):
        return f"<Reponse(id={self.id}, rating={self.rating})>"


class Halakha(Base, TimeStampMixin):
    """Décisions halakhiques"""
    __tablename__ = 'halakhot'

    id = Column(Integer, primary_key=True)
    sujet = Column(String(300), nullable=False)
    sujet_hebreu = Column(String(300))
    decision_halakhique = Column(Text, nullable=False)
    source_talmudique = Column(Text)
    codification = Column(Text)
    autorite = Column(String(200))
    niveau_obligation = Column(String(50))

    def __repr__(self):
        return f"<Halakha(sujet='{self.sujet}')>"


class Glossaire(Base, TimeStampMixin):
    """Glossaire de termes hébreux"""
    __tablename__ = 'glossaire'

    id = Column(Integer, primary_key=True)
    terme_hebreu = Column(String(200), unique=True, nullable=False)
    transliteration = Column(String(200))
    traduction_francais = Column(String(500))
    traduction_anglais = Column(String(500))
    definition_courte = Column(Text)
    definition_longue = Column(Text)
    categorie = Column(String(100))

    def __repr__(self):
        return f"<Glossaire(terme='{self.terme_hebreu}', transliteration='{self.transliteration}')>"
