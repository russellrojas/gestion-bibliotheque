-- Suppression du schéma biblio s'il existe déjà
DROP SCHEMA IF EXISTS biblio CASCADE;

-- Création du schéma biblio
CREATE SCHEMA biblio;

-- Définition des types ENUM dans le schéma biblio
CREATE TYPE biblio.EtatExemplaire AS ENUM ('neuf', 'bon', 'abime', 'perdu');
CREATE TYPE biblio.RoleUtilisateur AS ENUM ('personnel', 'adhérent');
CREATE TYPE biblio.StatutPret AS ENUM ('en cours', 'rendu');

-- Table Ressource
CREATE TABLE biblio.Ressource (
    codeRessource VARCHAR(20) PRIMARY KEY,
    titre VARCHAR(100) NOT NULL,
    dateApparition DATE NOT NULL,
    editeur VARCHAR(100),
    genre VARCHAR(50),
    codeClassification VARCHAR(20) UNIQUE
);

-- Table Livre
CREATE TABLE biblio.Livre (
    codeRessource VARCHAR(20) PRIMARY KEY,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    resume TEXT,
    langue VARCHAR(50),
    FOREIGN KEY (codeRessource) REFERENCES biblio.Ressource(codeRessource) ON DELETE CASCADE
);

-- Table Film
CREATE TABLE biblio.Film (
    codeRessource VARCHAR(20) PRIMARY KEY,
    longueur INT NOT NULL,
    langue VARCHAR(50),
    synopsis TEXT,
    FOREIGN KEY (codeRessource) REFERENCES biblio.Ressource(codeRessource) ON DELETE CASCADE
);

-- Table OeuvreMusicale
CREATE TABLE biblio.OeuvreMusicale (
    codeRessource VARCHAR(20) PRIMARY KEY,
    longueur INT NOT NULL,
    FOREIGN KEY (codeRessource) REFERENCES biblio.Ressource(codeRessource) ON DELETE CASCADE
);

-- Table Exemplaire avec ENUM pour etat
CREATE TABLE biblio.Exemplaire (
    id_exemplaire SERIAL PRIMARY KEY,
    etat biblio.EtatExemplaire NOT NULL,
    ressource VARCHAR(20),
    FOREIGN KEY (ressource) REFERENCES biblio.Ressource(codeRessource)
);

-- Table CompteUtilisateur avec ENUM pour rôle
CREATE TABLE biblio.CompteUtilisateur (
    login VARCHAR(50) PRIMARY KEY,
    motDePasse VARCHAR(100) NOT NULL,
    role biblio.RoleUtilisateur NOT NULL
);

-- Table Adherent
CREATE TABLE biblio.Adherent (
    id_adherent SERIAL PRIMARY KEY,
    informationsAdherent JSON NOT NULL,
    adherentActuel BOOLEAN NOT NULL,
    blacklister BOOLEAN NOT NULL,
    compteUtilisateur VARCHAR(50) UNIQUE,
    FOREIGN KEY (compteUtilisateur) REFERENCES biblio.CompteUtilisateur(login)
);


-- Table Personnel
CREATE TABLE biblio.Personnel (
    id_personnel SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    adresse VARCHAR(150),
    email VARCHAR(100),
    compteUtilisateur VARCHAR(50) UNIQUE,
    FOREIGN KEY (compteUtilisateur) REFERENCES biblio.CompteUtilisateur(login)
);

-- Table Pret
CREATE TABLE biblio.Pret (
    id_pret SERIAL PRIMARY KEY,
    datePret DATE NOT NULL,
    dateRendu DATE NOT NULL,
    statut biblio.StatutPret NOT NULL DEFAULT 'en cours',
    adherent INT NOT NULL,
    exemplaire INT NOT NULL,
    FOREIGN KEY (adherent) REFERENCES biblio.Adherent(id_adherent),
    FOREIGN KEY (exemplaire) REFERENCES biblio.Exemplaire(id_exemplaire),
    CHECK (dateRendu > datePret)
);

-- Table Suspension
CREATE TABLE biblio.Suspension (
    id_suspension SERIAL PRIMARY KEY,
    adherent INT,
    cause VARCHAR(255) NOT NULL,
    dateSuspension DATE NOT NULL,
    dureeSuspension INT,
    FOREIGN KEY (adherent) REFERENCES biblio.Adherent(id_adherent),
    CHECK (dureeSuspension > 0)
);

-- Table Contributeur
CREATE TABLE biblio.Contributeur (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    dateNaissance DATE,
    nationalite VARCHAR(50)
);

-- Table Auteur
CREATE TABLE biblio.Auteur (
    livre VARCHAR(20),
    contributeur INT,
    PRIMARY KEY (livre, contributeur),
    FOREIGN KEY (livre) REFERENCES biblio.Livre(codeRessource),
    FOREIGN KEY (contributeur) REFERENCES biblio.Contributeur(id)
);

-- Table Compositeur
CREATE TABLE biblio.Compositeur (
    oeuvreMusicale VARCHAR(20),
    contributeur INT,
    PRIMARY KEY (oeuvreMusicale, contributeur),
    FOREIGN KEY (oeuvreMusicale) REFERENCES biblio.OeuvreMusicale(codeRessource),
    FOREIGN KEY (contributeur) REFERENCES biblio.Contributeur(id)
);

-- Table Interprete
CREATE TABLE biblio.Interprete (
    oeuvreMusicale VARCHAR(20),
    contributeur INT,
    PRIMARY KEY (oeuvreMusicale, contributeur),
    FOREIGN KEY (oeuvreMusicale) REFERENCES biblio.OeuvreMusicale(codeRessource),
    FOREIGN KEY (contributeur) REFERENCES biblio.Contributeur(id)
);

-- Table Realisateur
CREATE TABLE biblio.Realisateur (
    film VARCHAR(20),
    contributeur INT,
    PRIMARY KEY (film, contributeur),
    FOREIGN KEY (film) REFERENCES biblio.Film(codeRessource),
    FOREIGN KEY (contributeur) REFERENCES biblio.Contributeur(id)
);

-- Table Acteur
CREATE TABLE biblio.Acteur (
    film VARCHAR(20),
    contributeur INT,
    PRIMARY KEY (film, contributeur),
    FOREIGN KEY (film) REFERENCES biblio.Film(codeRessource),
    FOREIGN KEY (contributeur) REFERENCES biblio.Contributeur(id)
);

-- Vues pour les types de ressources
CREATE VIEW biblio.VueLivre AS
SELECT 
    R.codeRessource,
    R.titre,
    R.dateApparition,
    R.editeur,
    R.genre,
    R.codeClassification,
    L.isbn,
    L.resume,
    L.langue,
    C.nom AS auteur_nom,
    C.prenom AS auteur_prenom
FROM biblio.Ressource R
JOIN biblio.Livre L ON R.codeRessource = L.codeRessource
JOIN biblio.Auteur A ON L.codeRessource = A.livre
JOIN biblio.Contributeur C ON A.contributeur = C.id;

CREATE VIEW biblio.VueFilm AS
SELECT 
    R.codeRessource,
    R.titre,
    R.dateApparition,
    R.editeur,
    R.genre,
    R.codeClassification,
    F.longueur,
    F.langue,
    F.synopsis,
    Cr.nom AS realisateur_nom,
    Cr.prenom AS realisateur_prenom,
    Cac.nom AS acteur_nom,
    Cac.prenom AS acteur_prenom
FROM biblio.Ressource R
JOIN biblio.Film F ON R.codeRessource = F.codeRessource
LEFT JOIN biblio.Realisateur Re ON F.codeRessource = Re.film
LEFT JOIN biblio.Contributeur Cr ON Re.contributeur = Cr.id
LEFT JOIN biblio.Acteur Ac ON F.codeRessource = Ac.film
LEFT JOIN biblio.Contributeur Cac ON Ac.contributeur = Cac.id;


CREATE VIEW biblio.VueOeuvreMusicale AS
SELECT 
    R.codeRessource,
    R.titre,
    R.dateApparition,
    R.editeur,
    R.genre,
    R.codeClassification,
    O.longueur,
    Cm.nom AS compositeur_nom,
    Cm.prenom AS compositeur_prenom,
    Intc.nom AS interprete_nom,
    Intc.prenom AS interprete_prenom
FROM biblio.Ressource R
JOIN biblio.OeuvreMusicale O ON R.codeRessource = O.codeRessource
LEFT JOIN biblio.Compositeur C ON O.codeRessource = C.oeuvreMusicale
LEFT JOIN biblio.Contributeur Cm ON C.contributeur = Cm.id
LEFT JOIN biblio.Interprete I ON O.codeRessource = I.oeuvreMusicale
LEFT JOIN biblio.Contributeur Intc ON I.contributeur = Intc.id;