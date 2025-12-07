-- ==========================
-- VUES SUR LES EMPRUNTS
-- ==========================

-- Emprunts en retard (suppose que les emprunts soient retirés de la bd quand ils sont rendus)
CREATE VIEW biblio.VueEmpruntsEnRetard AS
SELECT 
    A.id_adherent, 
    A.informationsAdherent->>'nom' AS nom_adherent,
    A.informationsAdherent->>'prenom' AS prenom_adherent,
    R.titre, 
    P.id_pret,
    P.datePret, 
    P.dateRendu AS dateRetourPrevue
FROM biblio.Pret P
FULL JOIN biblio.Adherent A ON P.adherent = A.id_adherent
FULL JOIN biblio.Exemplaire E ON P.exemplaire = E.id_exemplaire
FULL JOIN biblio.Ressource R ON E.ressource = R.codeRessource
WHERE P.dateRendu < CURRENT_DATE AND P.statut = 'en cours';

-- Emprunts en cours par adhérent
CREATE VIEW biblio.VueEmpruntsEnCoursParAdherent AS
SELECT 
    A.id_adherent, 
    A.informationsAdherent->>'nom' AS nom_adherent,
    A.informationsAdherent->>'prenom' AS prenom_adherent,
    R.titre, 
    P.id_pret,
    P.datePret, 
    P.dateRendu AS dateRetourPrevue
FROM biblio.Pret P
FULL JOIN biblio.Adherent A ON P.adherent = A.id_adherent
FULL JOIN biblio.Exemplaire E ON P.exemplaire = E.id_exemplaire
FULL JOIN biblio.Ressource R ON E.ressource = R.codeRessource
WHERE (P.statut = 'en cours');

-- Historique des emprunts par adhérent
CREATE VIEW biblio.VueHistoriqueEmpruntsParAdherent AS
SELECT 
    A.id_adherent, 
    A.informationsAdherent->>'nom' AS nom_adherent,
    A.informationsAdherent->>'prenom' AS prenom_adherent, 
    R.titre, 
    P.id_pret, 
    P.datePret, 
    P.dateRendu
FROM biblio.Pret P
JOIN biblio.Adherent A ON P.adherent = A.id_adherent
JOIN biblio.Exemplaire E ON P.exemplaire = E.id_exemplaire
JOIN biblio.Ressource R ON E.ressource = R.codeRessource
WHERE P.statut = 'rendu';

-- Dernier emprunt de chaque membre
CREATE OR REPLACE VIEW biblio.VueDernierPretParAdherent AS
SELECT 
    A.id_adherent, 
    A.informationsAdherent->>'nom' AS nom_adherent,
    A.informationsAdherent->>'prenom' AS prenom_adherent, 
    MAX(P.datePret) AS dernier_pret
FROM biblio.Adherent A
JOIN biblio.Pret P ON A.id_adherent = P.adherent
GROUP BY A.id_adherent, nom_adherent, prenom_adherent
ORDER BY A.id_adherent;

-- ==========================
-- VUES SUR LES ADHÉRENTS
-- ==========================
--afficher tous les adherents
CREATE VIEW biblio.VueAdherents AS
SELECT 
    A.id_adherent,
    A.informationsAdherent->>'nom' AS nom_adherent,
    A.informationsAdherent->>'prenom' AS prenom_adherent,
    C.login
FROM biblio.CompteUtilisateur C
INNER JOIN biblio.Adherent A ON C.login = A.compteUtilisateur
WHERE C.role = 'adhérent';

-- Adhérents suspendus
CREATE VIEW biblio.VueAdherentsSuspendus AS
SELECT A.id_adherent, A.informationsAdherent->>'nom' AS nom_adherent,A.informationsAdherent->>'prenom' AS prenom_adherent, S.cause, S.dateSuspension, S.dureeSuspension
FROM biblio.Adherent A
JOIN biblio.Suspension S ON A.id_adherent = S.adherent
WHERE A.blacklister = TRUE OR S.dureeSuspension IS NOT NULL;

-- Adhérents blacklistés
CREATE OR REPLACE VIEW biblio.VueAdherentsBlackListes AS
SELECT 
    A.id_adherent, 
    A.informationsAdherent->>'nom' AS nom_adherent,
    A.informationsAdherent->>'prenom' AS prenom_adherent,
    A.informationsAdherent->>'email' AS email_adherent,
    A.informationsAdherent->>'numeroTel' AS numeroTel_adherent,
    A.informationsAdherent->>'adresse' AS adresse_adherent,
    S.cause AS cause_suspension, 
    S.dateSuspension, 
    S.dureeSuspension 
FROM biblio.Adherent A
LEFT JOIN biblio.Suspension S ON A.id_adherent = S.adherent
WHERE A.blacklister = TRUE;


-- Adhérents qui n’ont pas de prêts en cours
CREATE OR REPLACE VIEW biblio.VueAdherentsSansEmprunts AS
SELECT 
    A.id_adherent, 
    A.informationsAdherent->>'nom' AS nom_adherent,
    A.informationsAdherent->>'prenom' AS prenom_adherent,
    A.informationsAdherent->>'email' AS email_adherent
FROM biblio.Adherent A
LEFT JOIN biblio.Pret P ON A.id_adherent = P.adherent 
    AND P.statut = 'en cours'
WHERE P.id_pret IS NULL
ORDER BY A.id_adherent;

-- ==========================
-- VUE COMPTE UTILISATEUR
-- ==========================

-- Utilisé pour la connexion, jointure entre compte utilisateurs, adherents et personnel
-- Permet de récupérer les informations d’un adhérent ou d’un personnel à partir de ses identifiants
CREATE VIEW biblio.VueCompteUtilisateur AS
SELECT 
    C.login, 
    C.motDePasse,
    C.role,
    A.id_adherent AS id_adherent, 
    A.informationsAdherent->>'nom' AS nom_adherent,
    A.informationsAdherent->>'prenom' AS prenom_adherent,
    P.id_personnel AS id_personnel, 
    P.nom AS nom_personnel, 
    P.prenom AS prenom_personnel
FROM biblio.CompteUtilisateur C
LEFT JOIN biblio.Adherent A ON C.login = A.compteUtilisateur
LEFT JOIN biblio.Personnel P ON C.login = P.compteUtilisateur;

-- ==========================
-- STATISTIQUES
-- ==========================

-- Nombre d'emprunts par genre
CREATE VIEW biblio.VueNbEmpruntsParGenre AS
SELECT 
    R.genre, 
    COUNT(P.id_pret) AS nombre_emprunts
FROM biblio.Pret P
JOIN biblio.Exemplaire E ON P.exemplaire = E.id_exemplaire
JOIN biblio.Ressource R ON E.ressource = R.codeRessource
GROUP BY R.genre;

-- Nombre d'emprunts par adhérent
CREATE VIEW biblio.VueNbEmpruntsEnCoursParAdherent AS
SELECT 
    A.id_adherent, 
    A.informationsAdherent->>'nom' AS nom_adherent,
    A.informationsAdherent->>'prenom' AS prenom_adherent,
    COUNT(P.id_pret) AS nombre_emprunts
FROM biblio.Pret P
JOIN biblio.Adherent A ON P.adherent = A.id_adherent
WHERE P.statut = 'en cours'
GROUP BY A.id_adherent, nom_adherent, prenom_adherent;

-- Ressources les plus empruntées
CREATE VIEW biblio.VueRessourcesPlusEmpruntees AS
SELECT 
    R.codeRessource, 
    R.titre, 
    R.genre, 
    COUNT(P.id_pret) AS nombre_emprunts
FROM biblio.Ressource R
JOIN biblio.Exemplaire E ON R.codeRessource = E.ressource
JOIN biblio.Pret P ON E.id_exemplaire = P.exemplaire
GROUP BY R.codeRessource, R.titre, R.genre
ORDER BY nombre_emprunts DESC;

-- Statistiques d'emprunts mensuels
CREATE VIEW biblio.VueStatistiquesEmpruntsMensuels AS
SELECT 
    DATE_TRUNC('month', P.datePret) AS mois, 
    COUNT(P.id_pret) AS nombre_emprunts
FROM biblio.Pret P
GROUP BY DATE_TRUNC('month', P.datePret)
ORDER BY mois;

-- ==========================
-- RESSOURCES ET EXEMPLAIRES
-- ==========================

-- Toutes les ressources groupées par type

-- Ressources disponibles
CREATE VIEW biblio.VueRessourcesDisponibles AS
SELECT 
    R.codeRessource, 
    R.titre, 
    R.genre, 
    COUNT(E.id_exemplaire) AS nombre_disponible
FROM biblio.Ressource R
JOIN biblio.Exemplaire E ON R.codeRessource = E.ressource
LEFT JOIN (
    SELECT exemplaire 
    FROM biblio.Pret P
    WHERE P.statut = 'en cours'
) EmpruntsActifs ON E.id_exemplaire = EmpruntsActifs.exemplaire
WHERE EmpruntsActifs.exemplaire IS NULL
GROUP BY R.codeRessource, R.titre, R.genre
ORDER BY R.codeRessource; 

--films disponibles
CREATE VIEW biblio.VueFilmsDisponibles AS
SELECT 
    R.codeRessource, 
    R.titre, 
    R.genre, 
    COUNT(E.id_exemplaire) AS nombre_disponible
FROM biblio.Film F
JOIN biblio.Ressource R ON F.codeRessource = R.codeRessource
JOIN biblio.Exemplaire E ON R.codeRessource = E.ressource
LEFT JOIN (
    SELECT exemplaire 
    FROM biblio.Pret P
    WHERE P.statut = 'en cours'
) EmpruntsActifs ON E.id_exemplaire = EmpruntsActifs.exemplaire
WHERE EmpruntsActifs.exemplaire IS NULL
GROUP BY R.codeRessource, R.titre, R.genre
ORDER BY R.codeRessource;  

--ouvres musicales disponibles
CREATE VIEW biblio.VueOeuvresMusicalesDisponibles AS
SELECT 
    R.codeRessource, 
    R.titre, 
    R.genre, 
    COUNT(E.id_exemplaire) AS nombre_disponible
FROM biblio.Ressource R
JOIN biblio.OeuvreMusicale O ON R.codeRessource = O.codeRessource
JOIN biblio.Exemplaire E ON R.codeRessource = E.ressource
LEFT JOIN (
    SELECT exemplaire 
    FROM biblio.Pret P
    WHERE P.statut = 'en cours'
) EmpruntsActifs ON E.id_exemplaire = EmpruntsActifs.exemplaire
WHERE EmpruntsActifs.exemplaire IS NULL
GROUP BY R.codeRessource, R.titre, R.genre
ORDER BY R.codeRessource;  

--livres disponibles
CREATE VIEW biblio.VueLivresDisponibles AS
SELECT 
    R.codeRessource, 
    R.titre, 
    R.genre, 
    COUNT(E.id_exemplaire) AS nombre_disponible
FROM biblio.Livre L
JOIN biblio.Ressource R ON L.codeRessource = R.codeRessource
JOIN biblio.Exemplaire E ON R.codeRessource = E.ressource
LEFT JOIN (
    SELECT exemplaire 
    FROM biblio.Pret P
    WHERE P.statut = 'en cours'
) EmpruntsActifs ON E.id_exemplaire = EmpruntsActifs.exemplaire
WHERE EmpruntsActifs.exemplaire IS NULL
GROUP BY R.codeRessource, R.titre, R.genre
ORDER BY R.codeRessource;  

-- Ressources en mauvais état
CREATE VIEW biblio.VueExemplairesMauvaisEtat AS
SELECT 
    E.id_exemplaire, 
    R.titre, 
    R.genre, 
    E.etat
FROM biblio.Exemplaire E
JOIN biblio.Ressource R ON E.ressource = R.codeRessource
WHERE E.etat IN ('abime', 'perdu');

-- Exemplaires qui n'ont pas été prêtées
CREATE OR REPLACE VIEW biblio.VueExemplairesJamaisEmpruntes AS
SELECT 
    E.id_exemplaire, 
    R.titre, 
    R.genre, 
    E.etat
FROM biblio.Exemplaire E
LEFT JOIN biblio.Pret P ON E.id_exemplaire = P.exemplaire
JOIN biblio.Ressource R ON E.ressource = R.codeRessource
WHERE P.id_pret IS NULL
ORDER BY E.id_exemplaire;

-- Vues pour le catalogue
-- Films :
CREATE VIEW biblio.VueCatalogueLivres AS
SELECT 
    R.codeRessource, 
    R.titre, 
    R.genre, 
    COUNT(E.id_exemplaire) AS nombre_exemplaires
FROM biblio.Ressource R
JOIN biblio.Film F ON R.codeRessource = F.codeRessource
JOIN biblio.Exemplaire E ON R.codeRessource = E.ressource
GROUP BY R.codeRessource, R.titre, R.genre
ORDER BY R.titre;

-- Livres :
CREATE VIEW biblio.VueCatalogueFilms AS
SELECT 
    R.codeRessource, 
    R.titre, 
    R.genre, 
    COUNT(E.id_exemplaire) AS nombre_exemplaires
FROM biblio.Ressource R
JOIN biblio.Livre L ON R.codeRessource = L.codeRessource
JOIN biblio.Exemplaire E ON R.codeRessource = E.ressource
GROUP BY R.codeRessource, R.titre, R.genre
ORDER BY R.titre;

-- Musiques :
CREATE VIEW biblio.VueCatalogueOeuvresMusicales AS
SELECT 
    R.codeRessource, 
    R.titre, 
    R.genre, 
    COUNT(E.id_exemplaire) AS nombre_exemplaires
FROM biblio.Ressource R
JOIN biblio.OeuvreMusicale M ON R.codeRessource = M.codeRessource
JOIN biblio.Exemplaire E ON R.codeRessource = E.ressource
GROUP BY R.codeRessource, R.titre, R.genre
ORDER BY R.titre;
