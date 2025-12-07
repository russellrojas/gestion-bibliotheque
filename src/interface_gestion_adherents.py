from .functions.gestion_adherents import *

def gestion_adherents(conn):
    """
    Fonction interactive pour gérer les adhérents.
    Permet d'ajouter, modifier, supprimer ou consulter les informations des adhérents.
    """
    while True:
        print("\n=== Gestion des Adhérents ===")
        print("1. Ajouter un adhérent")
        print("2. Modifier un adhérent")
        print("3. Supprimer un adhérent")
        print("4. Suspendre un adhérent")
        print("5. Blacklister ou déblacklister un adhérent")
        print("6. Afficher tous les adhérents")
        print("7. Afficher les adhérents blacklistés")
        print("8. Afficher les adhérents suspendus")
        print("9. Consulter les informations d'un adhérent")
        print("10. Retour au menu principal")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            ajouter_adherent(conn)
        elif choix == "2":
            modifier_adherent(conn)
        elif choix == "3":
            supprimer_adherent(conn)
        elif choix == "4":
            suspendre_adherent(conn)    
        elif choix == "5":
            blacklister_adherent(conn)
        elif choix == "6":
            afficher_tous_les_adherents(conn)
        elif choix == "7":
            afficher_adherents_blacklistes(conn)
        elif choix == "8":
            afficher_adherents_suspendus(conn)    
        elif choix == "9":
            consulter_informations_adherent(conn)
        elif choix == "10":
            print("Retour au menu principal.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
