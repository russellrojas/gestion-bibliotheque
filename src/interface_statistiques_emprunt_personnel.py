from .functions.utils.db_actions import execute_query
from .functions.statistiques import (
    generer_graphique_historique_emprunts, 
    afficher_nombre_total_emprunts, 
    afficher_documents_plus_empruntes, 
    suggérer_ressources
)

def interface_statistiques_emprunts(conn):
    """
    Interface interactive pour afficher des statistiques sur les emprunts.
    """
    while True:
        print("\n## Interface de Statistiques sur les Emprunts ##")
        print("1. Générer un graphique des historiques d'emprunts")
        print("2. Afficher le nombre total d'emprunts")
        print("3. Afficher les documents les plus empruntés")
        print("4. Suggérer des ressources personnalisées")
        print("5. Retour au menu principal")
        choix = input("Entrez votre choix : ")

        if choix == "1":
            generer_graphique_historique_emprunts(conn)
        elif choix == "2":
            afficher_nombre_total_emprunts(conn)
        elif choix == "3":
            afficher_documents_plus_empruntes(conn)
        elif choix == "4":
            suggérer_ressources(conn)
        elif choix == "5":
            print("Retour au menu principal.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
