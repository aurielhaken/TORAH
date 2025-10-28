-- Base de données pour Torah AI - Rav Virtuel
-- Schéma complet pour stocker les textes sacrés et leurs métadonnées

-- Extension pour la recherche vectorielle (embeddings)
CREATE EXTENSION IF NOT EXISTS vector;

-- Table principale des catégories de textes
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    nom_hebreu VARCHAR(100),
    description TEXT,
    parent_id INTEGER REFERENCES categories(id),
    ordre INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Exemples de catégories
COMMENT ON TABLE categories IS 'Torah (Pentateuque), Neviim (Prophètes), Ketouvim (Écrits), Mishna, Talmud, Kabbalah, Commentaires';

-- Table des livres (Sfarim)
CREATE TABLE livres (
    id SERIAL PRIMARY KEY,
    categorie_id INTEGER REFERENCES categories(id),
    nom VARCHAR(200) NOT NULL,
    nom_hebreu VARCHAR(200),
    nom_anglais VARCHAR(200),
    auteur VARCHAR(200),
    periode VARCHAR(100), -- Ex: "Tannaim", "Amoraim", "Rishonim", "Aharonim"
    annee_composition INTEGER,
    description TEXT,
    ordre INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_livres_categorie ON livres(categorie_id);

-- Table des chapitres/sections
CREATE TABLE chapitres (
    id SERIAL PRIMARY KEY,
    livre_id INTEGER REFERENCES livres(id),
    numero INTEGER NOT NULL,
    nom VARCHAR(200),
    nom_hebreu VARCHAR(200),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(livre_id, numero)
);

CREATE INDEX idx_chapitres_livre ON chapitres(livre_id);

-- Table des versets/passages (Pesukim)
CREATE TABLE passages (
    id SERIAL PRIMARY KEY,
    chapitre_id INTEGER REFERENCES chapitres(id),
    numero INTEGER NOT NULL,
    texte_hebreu TEXT NOT NULL,
    texte_francais TEXT,
    texte_anglais TEXT,
    texte_arameen TEXT, -- Pour le Talmud
    transliteration TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(chapitre_id, numero)
);

CREATE INDEX idx_passages_chapitre ON passages(chapitre_id);
CREATE INDEX idx_passages_texte_hebreu ON passages USING gin(to_tsvector('hebrew', texte_hebreu));
CREATE INDEX idx_passages_texte_francais ON passages USING gin(to_tsvector('french', texte_francais));

-- Table des commentaires (Perushim)
CREATE TABLE commentaires (
    id SERIAL PRIMARY KEY,
    passage_id INTEGER REFERENCES passages(id),
    commentateur VARCHAR(200) NOT NULL, -- Ex: "Rashi", "Ramban", "Ibn Ezra"
    commentateur_hebreu VARCHAR(200),
    epoque VARCHAR(100),
    texte_hebreu TEXT,
    texte_francais TEXT,
    texte_anglais TEXT,
    type_commentaire VARCHAR(50), -- "pshat", "remez", "drash", "sod" (PaRDeS)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_commentaires_passage ON commentaires(passage_id);
CREATE INDEX idx_commentaires_commentateur ON commentaires(commentateur);

-- Table des concepts/thèmes kabbalistiques
CREATE TABLE concepts_kabbalah (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(200) NOT NULL,
    nom_hebreu VARCHAR(200),
    description TEXT,
    description_hebreu TEXT,
    niveau VARCHAR(50), -- "nigleh" (révélé) ou "nistar" (caché)
    sefirah VARCHAR(100), -- Association avec les Sefirot si applicable
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table de liaison passages-concepts
CREATE TABLE passage_concepts (
    passage_id INTEGER REFERENCES passages(id),
    concept_id INTEGER REFERENCES concepts_kabbalah(id),
    pertinence FLOAT DEFAULT 1.0,
    explication TEXT,
    PRIMARY KEY (passage_id, concept_id)
);

-- Table des Mitzvot (613 commandements)
CREATE TABLE mitzvot (
    id SERIAL PRIMARY KEY,
    numero INTEGER UNIQUE NOT NULL, -- 1-613
    type VARCHAR(20) NOT NULL, -- "positive" ou "negative"
    nom VARCHAR(300) NOT NULL,
    nom_hebreu VARCHAR(300),
    description TEXT,
    description_hebreu TEXT,
    source_torah TEXT, -- Référence biblique
    categorie VARCHAR(100), -- Ex: "Shabbat", "Kashrut", "Prière"
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table de liaison passages-mitzvot
CREATE TABLE passage_mitzvot (
    passage_id INTEGER REFERENCES passages(id),
    mitzva_id INTEGER REFERENCES mitzvot(id),
    est_source_principale BOOLEAN DEFAULT FALSE,
    explication TEXT,
    PRIMARY KEY (passage_id, mitzva_id)
);

-- Table des embeddings pour la recherche sémantique
CREATE TABLE embeddings (
    id SERIAL PRIMARY KEY,
    passage_id INTEGER REFERENCES passages(id),
    commentaire_id INTEGER REFERENCES commentaires(id),
    embedding vector(1536), -- Dimension pour OpenAI embeddings, ajuster selon le modèle
    modele_utilise VARCHAR(100),
    langue VARCHAR(10), -- "he", "fr", "en"
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (
        (passage_id IS NOT NULL AND commentaire_id IS NULL) OR
        (passage_id IS NULL AND commentaire_id IS NOT NULL)
    )
);

CREATE INDEX idx_embeddings_passage ON embeddings(passage_id);
CREATE INDEX idx_embeddings_commentaire ON embeddings(commentaire_id);
-- Index pour la recherche vectorielle
CREATE INDEX idx_embeddings_vector ON embeddings USING ivfflat (embedding vector_cosine_ops);

-- Table des questions posées par les utilisateurs
CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question_texte TEXT NOT NULL,
    langue VARCHAR(10),
    utilisateur_id VARCHAR(100), -- Optionnel, pour tracking anonyme
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table des réponses générées par l'IA
CREATE TABLE reponses (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions(id),
    reponse_texte TEXT NOT NULL,
    sources_utilisees JSONB, -- Références aux passages, commentaires utilisés
    modele_ia VARCHAR(100),
    rating INTEGER, -- 1-5, feedback utilisateur
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_reponses_question ON reponses(question_id);

-- Table des sources Halakhiques (loi juive)
CREATE TABLE halakhot (
    id SERIAL PRIMARY KEY,
    sujet VARCHAR(300) NOT NULL,
    sujet_hebreu VARCHAR(300),
    decision_halakhique TEXT NOT NULL,
    source_talmudique TEXT,
    codification TEXT, -- Shulchan Arukh, Mishne Torah, etc.
    autorite VARCHAR(200), -- Rav qui a tranché
    niveau_obligation VARCHAR(50), -- "d'oraita" (biblique) ou "d'rabanan" (rabbinique)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table des traductions et translittérations
CREATE TABLE glossaire (
    id SERIAL PRIMARY KEY,
    terme_hebreu VARCHAR(200) NOT NULL UNIQUE,
    transliteration VARCHAR(200),
    traduction_francais VARCHAR(500),
    traduction_anglais VARCHAR(500),
    definition_courte TEXT,
    definition_longue TEXT,
    categorie VARCHAR(100), -- "terme halakhique", "concept kabbalistique", etc.
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Vues utiles pour simplifier les requêtes

-- Vue complète d'un passage avec son contexte
CREATE VIEW v_passages_complets AS
SELECT
    p.id,
    p.numero as numero_verset,
    p.texte_hebreu,
    p.texte_francais,
    p.texte_anglais,
    c.numero as numero_chapitre,
    c.nom as nom_chapitre,
    l.nom as nom_livre,
    l.nom_hebreu as nom_livre_hebreu,
    cat.nom as categorie
FROM passages p
JOIN chapitres c ON p.chapitre_id = c.id
JOIN livres l ON c.livre_id = l.id
JOIN categories cat ON l.categorie_id = cat.id;

-- Vue des mitzvot avec leurs sources
CREATE VIEW v_mitzvot_sources AS
SELECT
    m.numero,
    m.type,
    m.nom,
    m.nom_hebreu,
    m.description,
    m.source_torah,
    array_agg(DISTINCT p.texte_hebreu) as passages_sources
FROM mitzvot m
LEFT JOIN passage_mitzvot pm ON m.id = pm.mitzva_id
LEFT JOIN passages p ON pm.passage_id = p.id
GROUP BY m.id, m.numero, m.type, m.nom, m.nom_hebreu, m.description, m.source_torah;

-- Fonctions utiles

-- Fonction pour rechercher des passages par similarité sémantique
CREATE OR REPLACE FUNCTION recherche_semantique(
    query_embedding vector(1536),
    limite INTEGER DEFAULT 10,
    langue_cible VARCHAR(10) DEFAULT 'fr'
)
RETURNS TABLE (
    passage_id INTEGER,
    texte TEXT,
    livre VARCHAR,
    similarite FLOAT
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        e.passage_id,
        CASE
            WHEN langue_cible = 'he' THEN p.texte_hebreu
            WHEN langue_cible = 'en' THEN p.texte_anglais
            ELSE p.texte_francais
        END as texte,
        l.nom as livre,
        1 - (e.embedding <=> query_embedding) as similarite
    FROM embeddings e
    JOIN passages p ON e.passage_id = p.id
    JOIN chapitres c ON p.chapitre_id = c.id
    JOIN livres l ON c.livre_id = l.id
    WHERE e.langue = langue_cible
    ORDER BY e.embedding <=> query_embedding
    LIMIT limite;
END;
$$ LANGUAGE plpgsql;

-- Triggers pour updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_categories_updated_at BEFORE UPDATE ON categories
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_livres_updated_at BEFORE UPDATE ON livres
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_chapitres_updated_at BEFORE UPDATE ON chapitres
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_passages_updated_at BEFORE UPDATE ON passages
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Insertion des données initiales

-- Catégories principales
INSERT INTO categories (nom, nom_hebreu, description, ordre) VALUES
('Torah', 'תורה', 'Les cinq livres de Moïse (Pentateuque)', 1),
('Neviim', 'נביאים', 'Les Prophètes', 2),
('Ketouvim', 'כתובים', 'Les Écrits', 3),
('Mishna', 'משנה', 'Première codification de la loi orale', 4),
('Talmud Bavli', 'תלמוד בבלי', 'Talmud de Babylone (Guemara)', 5),
('Talmud Yerushalmi', 'תלמוד ירושלמי', 'Talmud de Jérusalem', 6),
('Kabbalah', 'קבלה', 'Enseignements mystiques du judaïsme', 7),
('Halakha', 'הלכה', 'Codes de loi juive', 8),
('Commentaires', 'פרושים', 'Commentaires des grands Sages', 9);

-- Les cinq livres de la Torah
INSERT INTO livres (categorie_id, nom, nom_hebreu, nom_anglais, ordre) VALUES
((SELECT id FROM categories WHERE nom = 'Torah'), 'Genèse', 'בראשית', 'Genesis', 1),
((SELECT id FROM categories WHERE nom = 'Torah'), 'Exode', 'שמות', 'Exodus', 2),
((SELECT id FROM categories WHERE nom = 'Torah'), 'Lévitique', 'ויקרא', 'Leviticus', 3),
((SELECT id FROM categories WHERE nom = 'Torah'), 'Nombres', 'במדבר', 'Numbers', 4),
((SELECT id FROM categories WHERE nom = 'Torah'), 'Deutéronome', 'דברים', 'Deuteronomy', 5);

-- Exemple de termes du glossaire
INSERT INTO glossaire (terme_hebreu, transliteration, traduction_francais, traduction_anglais, definition_courte, categorie) VALUES
('תורה', 'Torah', 'Torah/Enseignement', 'Torah/Teaching', 'Les cinq livres de Moïse et par extension tout l''enseignement juif', 'terme général'),
('הלכה', 'Halakha', 'Loi juive', 'Jewish Law', 'La loi juive, la manière de marcher dans la voie de Dieu', 'terme halakhique'),
('קבלה', 'Kabbalah', 'Réception/Tradition', 'Kabbalah/Received Tradition', 'La tradition mystique du judaïsme', 'concept kabbalistique'),
('משנה', 'Mishna', 'Répétition/Étude', 'Mishna', 'Première codification écrite de la loi orale', 'texte fondamental'),
('גמרא', 'Guemara', 'Achèvement/Étude', 'Gemara', 'Discussions et analyses de la Mishna', 'texte fondamental'),
('מצוה', 'Mitzva', 'Commandement', 'Commandment', 'Un des 613 commandements divins', 'terme halakhique'),
('תלמוד', 'Talmud', 'Étude', 'Talmud', 'Mishna + Guemara, corpus central de la loi orale', 'texte fondamental');

COMMENT ON DATABASE torah_ai IS 'Base de données complète pour le Rav Virtuel - Torah AI';
