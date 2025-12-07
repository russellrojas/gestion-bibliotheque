from .functions.affichages_emprunts_personnel import ajouter_emprunt, rendu_emprunt, afficher_emprunts_actifs, afficher_emprunts_retard
from .interface_gestion_adherents import gestion_adherents
from .interface_gestion_documents import gestion_documents
from .interface_statistiques_emprunt_personnel import interface_statistiques_emprunts

def menu_personnel(conn, personnel_id):
    while True:
        print("\n=== Menu Personnel ===")
        print("1. Gérer les adhérents")
        print("2. Gérer les documents")
        print("3. Voir les emprunts actifs")
        print("4. Voir les emprunts en retard")
        print("5. Enregistrer un nouvel emprunt")
        print("6. Valider le rendu d'un emprunt")
        print("7. Statistiques sur les emprunts")
        print("8. Retour au menu principal")

        choix = input("Sélectionnez une option: ")
        if choix == "1":
            gestion_adherents(conn)
            continue
        elif choix == "2":
            gestion_documents(conn)
            continue
        elif choix == "3":
            afficher_emprunts_actifs(conn)
        elif choix == "4":
            afficher_emprunts_retard(conn)
        elif choix == "5":
            ajouter_emprunt(conn)
        elif choix == "6":
            rendu_emprunt(conn)
        elif choix == "7":
            interface_statistiques_emprunts(conn)
        elif choix == "8":
            break
        else:
            print("Cette fonctionnalité est en cours de développement.")
