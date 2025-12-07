## Modèle Logique de Données (MLD)
Ce MLD est issu de la transformation du modèle UML réalisé pour l’application de gestion de médiathèque.
L’objectif est de fournir une structure relationnelle cohérente, normalisée et directement exploitable en base de données.

### Ressources et héritage
**Ressource** *(#codeRessource:chaîne, titre:chaîne, dateApparition:date, editeur:chaîne, genre:chaîne, codeClassification:chaîne)*

Les types de ressources sont des héritages par référence.

**Livre** *(#codeRessource=>Ressource, isbn:chaîne, resume:texte, langue:chaîne)* codeRessource UNIQUE 

**Film** *(#codeRessource=>Ressource, longueur:entier, langue:chaîne, synopsis:texte)* codeRessource UNIQUE 

**OeuvreMusicale** *(#codeRessource=>Ressource, longueur:entier)* codeRessource UNIQUE 

**Exemplaire** *(#id_exemplaire:entier, etat:{neuf|bon|abime|perdu}, ressource=>Ressource)* etat NON NUL

Pour les comptes utilisateurs, on garde les trois relations avec des clés étrangères et des contraites d'unicité pour conserver des relations 1..1.

**Adherent** (#id_adherent: entier, informationsAdherent: JSON, adherentActuel: booléen, blacklisté: booléen, compteUtilisateur => CompteUtilisateur)

informationsAdherent regroupe les champs suivants dans un format JSON :
    * nom: chaîne
    * prenom: chaîne
    * dateNaissance: date
    * adresse: chaîne
    * email: chaîne
    * numeroTel: chaîne

**Personnel** *(#id_personnel:entier, nom:chaîne, prenom:chaîne, adresse:chaîne, email:chaîne, compteUtilisateur=>CompteUtilisateur) ; compte utilisateur UNIQUE*

**CompteUtilisateur** *(#login:chaîne, motDePasse:chaîne, rôle:{administrateur|adhérent})*

**Pret** *(#id_pret:entier, datePret:date, dureePret:entier, adherent=>Adherent, exemplaire=>Exemplaire)* Adhérent, Exemplaire, datePret, dureePret NON NUL

**Suspension** *(#id_suspension:entier, cause:chaîne, dureeSuspension:entier, dateSuspension:date, adherent=>Adherent)* On ajoute une clé artificielle car on conservera les supensions pour l'historique. dureeSuspension peut être NUL pour signifier que la durée est indéfinie. Un adhérent peut donc avoir plusieurs suspensions, mais pas en même temps. On conservera donc simplement la suspension a la date de fin la plus longue.

**Contributeur** *(#id:entier, nom:chaîne, prenom:chaîne, dateNaissance:date, nationalite:chaîne)* Nom et Prénom NON NUL

On crée des classes d'association pour chaque type de contribution. La clé primaire est constituée des deux clés étrangères.
Grâce à cela on peut dire qu'un contributeur peut-être à la fois un compositeur et un interprete.

**Auteur** *(#livre=>Livre, #contributeur=>Contributeur)*

**Compositeur** *(#oeuvreMusicale=>OeuvreMusicale, #contributeur=>Contributeur)*

**Interprete** *(#oeuvreMusicale=>OeuvreMusicale, #contributeur=>Contributeur)*

**Realisateur** *(#film=>Film, #contributeur=>Contributeur)*

**Acteur** *(#film=>Film, #contributeur=>Contributeur)*

## Contraites supplémentaires :

**Intégré à l'application**
- Un document ne peut être emprunté que s'il est disponible et en bon état.
- Un adhérent peut emprunter un maximum de N documents à la fois.
- Rendre un document en retard entraine une suspension d'une durée égale au nombre de jours de retard.
- En cas de dégats sur une oeuvre, suspension de durée indéfinie
- Un adhérent ne peut pas avoir plusieurs supensions en même temps : la suspension de durée la plus longue est conservée.
- Un adhérent ne peut pas emprunter s'il est suspendu


## Contraintes d'héritage:
*Héritage Ressource*
- PROJECTION(Ressource,codeRessource) = PROJECTION (Livre, codeRessource) U PROJECTION(Film, codeRessource) U 
PROJECTION(OuvreMusicale,codeRessource)


## Justification des Transformations d'Héritage
- L'héritage par référence a été utilisé pour les types de ressources Livre, Film, et OeuvreMusicale afin de centraliser les informations partagées dans la table Ressource. Cela permet d'éviter la duplication de données et de simplifier la gestion des ressources.

- Nous avons choisi l'héritage par référence car la relation Livre est héritage non exclusif, abstraite et non complète.

- Des classes d'association ont été créées pour gérer les différents types de contribution (Auteur, Compositeur, Interprète, Réalisateur, Acteur). Chaque association est représentée par une table qui lie un contributeur à un type de ressource spécifique grâce à notre modélisation on peut avoir un contributeur qui est par exemple à la fois Compositeur et Interprètre.

## Vues Nécessaires suite à notre transformation d'héritage: 

- CREATE VIEW VueLivre AS
SELECT R.codeRessource, R.titre, R.dateApparition, R.editeur, L.isbn, L.resume, L.langue
FROM Ressource R
JOIN Livre L ON R.codeRessource = L.codeRessource;

- CREATE VIEW VueFilm AS
SELECT R.codeRessource, R.titre, R.dateApparition, R.editeur, F.longueur, F.langue, F.synopsis
FROM Ressource R
JOIN Film F ON R.codeRessource = F.codeRessource;

- CREATE VIEW VueOeuvreMusicale AS
SELECT R.codeRessource, R.titre, R.dateApparition, R.editeur, O.longueur
FROM Ressource R
JOIN OeuvreMusicale O ON R.codeRessource = O.codeRessource;

