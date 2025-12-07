from .functions.gestion_documents import ajouter_document, modifier_document, supprimer_document
from .functions.gestion_exemplaires import voir_exemplaires_document, ajouter_exemplaire, modifier_etat_exemplaire, supprimer_exemplaire
from .interface_catalogue import rechercher_document

def gestion_documents(conn):
    """
    Fonction interactive pour gérer les documents.
    Permet d'ajouter, modifier, supprimer ou gérer les exemplaires de documents.
    """
    while True:
        print("\n## Interface de Gestion des Documents ##")
        print("1. Ajouter un document")
        print("2. Modifier un document")
        print("3. Supprimer un document")
        print("4. Rechercher un document")
        print("5. Voir les exemplaires d'un document")
        print("6. Ajouter un exemplaire d'un document")
        print("7. Modifier l'état d'un exemplaire")
        print("8. Supprimer un exemplaire")
        print("9. Retour au menu principal")
        choix = input("Entrez votre choix : ")

        if choix == "1":
            ajouter_document(conn)
        elif choix == "2":
            modifier_document(conn)
        elif choix == "3":
            supprimer_document(conn)
        elif choix == "4":
            rechercher_document(conn)
        elif choix == "5":
            voir_exemplaires_document(conn)
        elif choix == "6":
            ajouter_exemplaire(conn)
        elif choix == "7":
            modifier_etat_exemplaire(conn)
        elif choix == "8":
            supprimer_exemplaire(conn)
        elif choix == "9":
            print("Retour au menu principal.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")