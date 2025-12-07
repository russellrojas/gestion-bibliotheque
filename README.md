# 📚 Gestion d’une Bibliothèque 

Projet réalisé dans le cadre de l’UV **NF18 – Bases de Données**.  
Travail en groupe réalisé par : **Russell Rojas**, Yanis Djahnit, Zaher Bakhache et Eliott Thomann.

L’objectif du projet était de concevoir une application complète de gestion d’une médiathèque, incluant la modélisation UML, la transformation **UML → MLD**, et le développement d’une application Python connectée à une base de données relationnelle.

-------------------------------------------------------------

## 🎯 Objectifs du projet

- Concevoir un schéma UML complet et le transformer en **Modèle Logique de Données (MLD)**.  
- Construire une base de données cohérente : ressources, prêts, adhérents, suspensions, contributeurs…  
- Développer une application Python gérant les documents, adhérents, emprunts et statistiques.  
- Implémenter les contraintes métier : disponibilité, retards, suspensions, limites de prêts, etc.

-------------------------------------------------------------

## 🏗 Modélisation : UML → MLD

Le dépôt contient :
- `UML.puml` — schéma UML en PlantUML  
- `UML.png` — version image du diagramme  

La transformation UML → MLD repose sur :
- un **héritage par référence** pour Livre, Film, OeuvreMusicale  
- des **tables d’association** pour Auteur, Acteur, Compositeur, Interprète…  
- des **vues SQL** pour représenter les sous-types  
- des **contraintes métier** gérées au niveau applicatif Python  

-------------------------------------------------------------

## ⚙ Installation
```bash
Cloner le dépôt :  
   git clone https://github.com/russellrojas/NF18-projet.git  
   cd NF18-projet  

Installer les dépendances Python :  
   pip install -r requirements.txt  

Créer un fichier `config.py` dans *Rendu 4* :  
   HOST = "XXX.X.X.X"  
   USER = "your_user"  
   PASSWORD = "your_password"  
   DATABASE = "your_data_base"  
```
-------------------------------------------------------------

## 🧩 Fonctionnalités principales

### 👥 Gestion des adhérents
- Ajout, modification, suppression  
- Suspension, blacklist  
- Consultation du profil  
- Historique et emprunts en cours  

### 📘 Gestion des documents
- Ajout et modification de ressources  
- Ajout / suppression d’exemplaires  
- Mise à jour de l’état d’un exemplaire  
- Recherche de documents  

### 📦 Gestion des emprunts
- Enregistrement d’un emprunt  
- Vérification des suspensions  
- Retour et détection des retards  
- Génération de suspensions automatisée  
- Liste des emprunts en cours et en retard  

### 📊 Statistiques
- Nombre total d’emprunts  
- Top 5 des ressources les plus empruntées  
- Suggestions personnalisées  
- Graphiques générés automatiquement  

-------------------------------------------------------------

## 📝 Remarque

Projet réalisé **en 2024** dans le cadre universitaire, puis **révisé et adapté en 2025** pour être intégré à mon GitHub.

-------------------------------------------------------------

## 👨‍💻 Auteurs

- **Russell Rojas**  
- Yanis Djahnit  
- Zaher Bakhache  
- Eliott Thomann  

-------------------------------------------------------------
