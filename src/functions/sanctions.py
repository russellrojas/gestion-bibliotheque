from datetime import datetime, timedelta, date
from .utils.db_actions import execute_query

def insert_suspension(conn, adherent_id, date_suspension, cause, duree_suspension):
    """
    Suspend un adhérent pour une durée limitée ou illimitée (duree Null).
    """
    # Vérifier si l'adhérent est blacklisté
    query = "SELECT * FROM biblio.VueAdherentsBlacklistes WHERE id_adherent = %s"
    resp = execute_query(conn, query, (adherent_id,))

    if resp:
        print("L'adhérent est blacklisté, impossible de suspendre.")
        return

    # Suspendre l'adhérent
    query = "INSERT INTO biblio.Suspension (adherent, dateSuspension, cause, dureeSuspension) VALUES (%s, %s, %s, %s)"
    execute_query(conn, query, (adherent_id, date_suspension, cause, duree_suspension))

def suspension_pour_retard(conn, adherent_id, duree_retard: int):
    """
    Fonction interractive pour proposer la suspension d'un adhérent lors d'un rendu en retard.
    prend en paramètre le retard en jours.
    """

    susp = input("Ce rendu a été validé en retard, voulez vous suspendre l'adhérent ? (o/n) : ")

    if not susp:
        return
    
    # valider durée, défaut : duree_retard
    duree_suspension = int(input(f"Durée de suspension en jours (laisser vide pour conserver la durée du retard : {duree_retard} jours) : ") or duree_retard)

    date_suspension = datetime.now() + timedelta(days=duree_suspension)

    cause = "Retard de rendu"

    insert_suspension(conn, adherent_id, date_suspension, cause, duree_suspension)

    print(f"Adhérent {adherent_id} suspendu pour une durée de {duree_suspension} jours.")







