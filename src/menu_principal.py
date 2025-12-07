from .menu_adherent import menu_adherent
from .menu_personnel import menu_personnel
from .interface_connexion import gestion_connexion_utilisateur
from .interface_catalogue import choix_catalogue


def afficher_menu_principal():
    print("\n=== Menu Principal ===")
    print("1. Catalogue (Accès libre)")
    print("2. Connexion utilisateur")
    print("3. Quitter")

def gestion_menu_principal(conn):
    """
    Gère le menu principal de l'application.
    
    Args:
        conn: Connexion à la base de données.
    """
    while True:
        afficher_menu_principal()
        choix = input("Sélectionnez une option: ")

        if choix == "1":
            choix_catalogue(conn)  # Affiche le sous-menu pour le catalogue
        elif choix == "2":
            gestion_connexion_utilisateur(conn)
        elif choix == "3":
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")