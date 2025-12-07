from .interface_gestion_documents import rechercher_document
from .functions.emprunts_adherent import afficher_emprunts_actifs, afficher_historique_emprunts

def menu_adherent(conn, adherent_id):
    while True:
        print("\n=== Menu Adhérent ===")
        print("1. Rechercher un document")
        print("2. Voir les emprunts actifs")
        print("3. Voir l'historique des emprunts")
        print("4. Retour au menu principal")

        choix = input("Sélectionnez une option: ")
        if choix == "1":
            rechercher_document(conn)
            continue
        elif choix == "2":
            afficher_emprunts_actifs(conn, adherent_id)
            continue
        elif choix == "3":
            afficher_historique_emprunts(conn, adherent_id)
            continue
        elif choix == "4":
            break
        else:
            print("Cette fonctionnalité est en cours de développement.")