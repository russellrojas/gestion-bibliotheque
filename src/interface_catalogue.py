from .functions.utils.db_actions import execute_query
from .functions.catalogue import afficher_catalogue_par_type, rechercher_films, rechercher_oeuvres_musicales, rechercher_livres

def choix_catalogue(conn):
    """
    Permet de naviguer dans les catalogues pour voir les films, œuvres musicales ou livres.
    """
    while True:
        print("\n=== Catalogue Complet ===")
        print("1. Films")
        print("2. Œuvres musicales")
        print("3. Livres")
        print("4. Retour au menu principal")
        choix = input("Choisissez une option (1-4) : ")

        if choix == "1":
            afficher_catalogue_par_type(conn, "film")
            input("Appuyez sur une touche pour continuer...")
        elif choix == "2":
            afficher_catalogue_par_type(conn, "musique")
            input("Appuyez sur une touche pour continuer...")
        elif choix == "3":
            afficher_catalogue_par_type(conn, "livre")
            input("Appuyez sur une touche pour continuer...")
        elif choix == "4":
            break
        else:
            print("Option invalide. Veuillez réessayer.")

def rechercher_document(conn):
    while True:
        print("\n=== RESSOURCES DISPONIBLES ===")
        print("1. Films")
        print("2. Œuvres musicales")
        print("3. Livres")
        print("4. Retour ")

        choix = input("Sélectionnez une option: ")
        if choix == "1":
            rechercher_films(conn)
        elif choix == "2":
            rechercher_oeuvres_musicales(conn)
        elif choix == "3":
            rechercher_livres(conn)
        elif choix == "4":
            break
        else:
            print("Option invalide, veuillez réessayer.")