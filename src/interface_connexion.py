from .functions.connexion import get_user
from .menu_adherent import menu_adherent
from .menu_personnel import menu_personnel

def gestion_connexion_utilisateur(conn):
    """
    Gère la connexion d'un utilisateur ou d'un personnel.
    
    Args:
        conn: Connexion à la base de données.
    """
    login = input("Entrez votre nom d'utilisateur: ")
    mot_de_passe = input("Entrez votre mot de passe: ")

    user_infos = get_user(conn, login, mot_de_passe)

    if user_infos:
        print()
        print()
        print(f"Bienvenue, {user_infos['prenom']} {user_infos['nom']} !")
        if user_infos['role'] == 'adhérent':
            menu_adherent(conn, user_infos['id'])
        elif user_infos['role'] == 'personnel':
            menu_personnel(conn, user_infos['id'])
    else:
        print("Nom d'utilisateur ou mot de passe incorrect.")