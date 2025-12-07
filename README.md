# NF18-projet

Projet de groupe pour l'UV NF18.

Réalisé au sein du TD1 par Russell Rojas, Yanis Djahnit, Zaher Bakhache et Eliott Thomann.

## Sujet : Gestion d'une bibliothèque

[Lien vers le sujet](https://moodle.utc.fr/pluginfile.php/246372/mod_resource/content/2/co/biblio.html)

## Schéma UML

Le code pour un schéma en plantUML est accessible dans [UML.puml](./UML.puml).
![PlantUML]( ./UML.png "Schéma UML")

## Pour lancer le code chez vous :
- clonez le repo sur votre machine
- dans un terminal, téléchargez les librairies python requises avec 
    ```pip install -r requirements.txt```
- pour le Rendu 4, créez un fichier config.py tel que décrit dans la section suivante et placez le dans le dossier 'Rendu 4'

## fichier config.py :
Le fichier config.py contient vos identifiants et permet de vous connecter à la base de donnée.
Il est importé et donc requis par notre application python. POue executer le code il faudra le créer, le placer au bon endroit et le completer avec vos identifiants.
Son format est le suivant :

```
HOST = "tuxa.sme.utc"

USER = ""

PASSWORD = ""

DATABASE = ""
```

## L'Application

**Infos importantes** :

Les adhérents sont actifs par défaut, pour marquer un adhérent comme inactif il faut aller dans "modifier adhérent" dans le menu de gestion des adhérents.
Les adhérents n'empruntent pas directement dans l'appli, les emprunts ne sont gérés que par le personnel.
Un emprunt se fait à partir de l'ID d'un adhérent, on considère que les adhérents ont une carte d'adhérent sur laquelle le n° est inscrit.

### Bilan sur les besoins :

- Faciliter aux adhérents la recherche de documents et la gestion de leurs emprunts.
=> Les adhérents ont accès au catalogue et peuvent visualiser leurs emprunts en cours et passés.

- Faciliter la gestion des ressources documentaires : ajouter des documents, modifier leur description, ajouter des exemplaires d'un document, etc.
=> Le personnel peut ajouter, supprimer ou modifier les documents et les exemplaires. 

- Faciliter au personnel la gestion des prêts, des retards et des réservation.
=> Le personnel peut ajouter un prêt, marquer un prêt comme validé, visualiser les emprunts en retards (à implémenter). Les réservations ne sont pas gérés car non mentionnées dans la spécification.

- Faciliter la gestion des utilisateurs et de leurs données.
=> Le personnel peut ajouter, modifier et supprimer les comptes des adhérents

- Établir des statistiques sur les documents empruntés par les adhérents, cela permettra par exemple d'établir la liste des documents populaires, mais aussi d'étudier le profil des adhérents pour pouvoir leur suggérer des documents.
=> Page de statistique pour voir les emprunts de chaque adhérent, avec graphique.

## À implémenter dans l'appli python :

### Interfaces :

- Personnel :
    - [x] Gestion des emprunts et retards : 
        - [x] Enregistrer un nouvel emprunt
        - [x] Ajouter vérification des suspensions au moment de l'emprunt
        - [x] Marquer un emprunt comme rendu
        - [x] Proposer une suspension si rendu en retard
        - [x] Lister tous les emprunts en cours
        - [x] Lister les emprunts en retard
    - [x] Gestion des adherents:
        - [x] Ajouter un adhérent
        - [x] Modifier un adhérent
        - [x] Supprimer un adhérent
        - [x] Suspendre un adhérenet
        - [x] Blacklister un adhérent
        - [x] Afficher tous les adhérents
        - [x] Afficher les adhérents blacklistés
        - [x] Afficher les adhérents suspendus
        - [x] Consulter les informations d'un adhérent
    - [x] Interface de gestion des documents : ajouter des documents, modifier leur description, ajouter des exemplaires d'un document, etc.
        - [x] Rechercher un document ?
        - [x] Afficher tous les exemplaires d'un document
        - [x] Supprimer un exemplaire
        - [x] Modifier l'etat d'un exemplaire
    - [x] Interface de statistique sur les emprunts : lister tous les documents empruntés, le nombre d'emprunts...
        - [x] Générer un graphique pour les docuemnts empruntés 
        - [x] Affciher le nombre total d'emprunts
        - [x] Afficher les 5 ressources les plus populaires
        - [x] Suggérer des ressources en fonctions de ses emprunts 


- Adhérents :
    - [x] Voir ses emprunts en cours
    - [x] Voir son historique d'emprunt
    - [x] rechercher un document disponible dans le catalogue par categorie

- [x] Vérifier que tous les checks mentionnés dans le MLD sont bien vérifiés
- [x] Implémenter un N maximum d'emprunts à la fois par adhérent.
- [ ] Ajouter des vérification des entrées et de la gestion d'erreur.
    => implémenté partiellement mais on va se contenter de ça
