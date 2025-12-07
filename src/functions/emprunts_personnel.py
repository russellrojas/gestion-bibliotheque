from .utils.options import MAX_EMPRUNTS_PAR_ADHERENT
from .utils.db_actions import execute_query

def enregistrer_emprunt(conn, adherent_id, exemplaire_id, date_emprunt, dateRendu):
    """
    Effectue la requête SQL pour valider un emprunt, renvoie le n° de l'emprunt si l'emprunt est validé,
    sinon renvoie None.
    """
    query = "INSERT INTO biblio.Pret (datePret, dateRendu, statut, adherent, exemplaire) VALUES (%s, %s, %s, %s, %s) RETURNING id_pret"

    resp = execute_query(conn, query, (date_emprunt, dateRendu, "en cours", adherent_id, exemplaire_id))
    
    return resp

def check_emprunt_exemplaire(conn, exemplaire_id):
    """
    Vérifie si un exemplaire peut être emprunté, renvoie True si oui, False sinon
    Un document peut être emprunté seulement si :
        - l'exemplaire est disponible (non emprunté et existe)
        - l'exemplaire est en bon état
    """
    
    query = "SELECT etat FROM biblio.Exemplaire WHERE id_exemplaire = %s"
    resp = execute_query(conn, query, (exemplaire_id,))

    if not resp:
        print("L'exemplaire n'existe pas.")
        return False

    if not (resp[0][0] == "bon" or resp[0][0] == "neuf"):
        print("L'exemplaire n'est pas en bon état, état :", resp[0][0])
        return False

    # vérifier si l'exemplaire est disponible
    query = "SELECT statut FROM biblio.Pret WHERE exemplaire = %s AND statut = 'en cours'"
    resp = execute_query(conn, query, (exemplaire_id,))

    if resp:
        print("L'exemplaire est déjà emprunté.")
        return False
    
    return True

def check_suspendu_adherent(conn, adherent_id):
    """
    Vérifie si un adhérent est suspendu ou blacklisté, renvoie True si oui, False sinon.
    """
    query = "SELECT * FROM biblio.VueAdherentsSuspendus WHERE id_adherent = %s"
    resp = execute_query(conn, query, (adherent_id,))

    if resp:
        print("L'adhérent est suspendu, impossible d'emprunter.")
        return True
    return False

def check_max_emprunts(conn, adherent_id):
    """
    Vérifie si un adhérent a atteint son nombre maximum d'emprunts, renvoie True si oui, False sinon.
    """
    query = "SELECT nombre_emprunts FROM biblio.VueNbEmpruntsEnCoursParAdherent WHERE id_adherent = %s"
    resp = execute_query(conn, query, (adherent_id,))

    if resp[0][0] >= MAX_EMPRUNTS_PAR_ADHERENT:
        print("L'adhérent a atteint son nombre maximum d'emprunts, impossible d'emprunter.")
        return True
    return False

def enregistrer_emprunt_rendu(conn, emprunt_id):
    """
    Fonction permettant de marquer un emprunt comme rendu.
    """
    query = "UPDATE biblio.Pret SET statut = 'rendu' WHERE id_pret = %s"
    execute_query(conn, query, (emprunt_id,))