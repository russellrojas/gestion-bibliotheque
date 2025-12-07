-- Test des vues sur les emprunts

-- Vue des emprunts en retard
SELECT * FROM biblio.VueEmpruntsEnRetard;

-- Vue des emprunts en cours par adhérent
SELECT * FROM biblio.VueEmpruntsEnCoursParAdherent;

-- Vue de l'historique des emprunts par adhérent
SELECT * FROM biblio.VueHistoriqueEmpruntsParAdherent;

-- Vue du dernier emprunt de chaque membre
SELECT * FROM biblio.VueDernierPretParAdherent;

-- Test des vues sur les adhérents

-- Vue de tous les adhérents
SELECT * FROM biblio.VueAdherents;

-- Vue des adhérents suspendus
SELECT * FROM biblio.VueAdherentsSuspendus;

-- Vue des adhérents blacklistés
SELECT * FROM biblio.VueAdherentsBlackListes;

-- Vue des adhérents sans emprunts en cours
SELECT * FROM biblio.VueAdherentsSansEmprunts;

-- Test des vues sur le compte utilisateur

-- Vue du compte utilisateur
SELECT * FROM biblio.VueCompteUtilisateur;

-- Test des vues statistiques

-- Nombre d'emprunts par genre
SELECT * FROM biblio.VueNbEmpruntsParGenre;

-- Nombre d'emprunts par adhérent
SELECT * FROM biblio.VueNbEmpruntsEnCoursParAdherent;

-- Ressources les plus empruntées
SELECT * FROM biblio.VueRessourcesPlusEmpruntees;

-- Statistiques d'emprunts mensuels
SELECT * FROM biblio.VueStatistiquesEmpruntsMensuels;

-- Test des vues sur les ressources et exemplaires

-- Ressources disponibles
SELECT * FROM biblio.VueRessourcesDisponibles;

-- Films disponibles
SELECT * FROM biblio.VueFilmsDisponibles;

-- Oeuvres musicales disponibles
SELECT * FROM biblio.VueOeuvresMusicalesDisponibles;

-- Livres disponibles
SELECT * FROM biblio.VueLivresDisponibles;

-- Ressources en mauvais état
SELECT * FROM biblio.VueExemplairesMauvaisEtat;

-- Exemplaires jamais empruntés
SELECT * FROM biblio.VueExemplairesJamaisEmpruntes;

-- Test des vues pour le catalogue

-- Vue du catalogue des livres
SELECT * FROM biblio.VueCatalogueLivres;

-- Vue du catalogue des films
SELECT * FROM biblio.VueCatalogueFilms;

-- Vue du catalogue des oeuvres musicales
SELECT * FROM biblio.VueCatalogueOeuvresMusicales;
