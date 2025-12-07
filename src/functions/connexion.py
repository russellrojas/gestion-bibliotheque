from .utils.db_actions import execute_query

def get_user(conn, login, mot_de_passe):
    """
    Récupère les informations d'un utilisateur ou d'un personnel en fonction de l'identifiant et du mot de passe.
    
    Args:
        conn: Connexion à la base de données.
        login (str): Nom d'utilisateur.
        mot_de_passe (str): Mot de passe.
        
    Returns:
        dict: Informations du personnel ou de l'adhérent.
        None: Si les identifiants sont invalides.
    """

    query = """
        SELECT
            role,
            id_adherent, 
            nom_adherent, 
            prenom_adherent, 
            id_personnel, 
            nom_personnel,
            prenom_personnel
        FROM VueCompteUtilisateur
        WHERE login = %s AND motDePasse = %s;
    """
    params = (login, mot_de_passe)
    result = execute_query(conn, query, params)
    
    if result:
        if result[0][0] == 'adhérent':
            return {
                'role': 'adhérent',
                'id': result[0][1],
                'nom': result[0][2],
                'prenom': result[0][3]
            }
        elif result[0][0] == 'personnel':
            return {
                'role': 'personnel',
                'id': result[0][4],
                'nom': result[0][5],
                'prenom': result[0][6]
            }
    else:
        return None