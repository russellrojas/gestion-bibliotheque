from .utils.db_actions import execute_query

def afficher_emprunts_actifs(conn, adherent_id):
    # on utilise la vue VueEmpruntsEnCoursParAdherent
    query = f"SELECT id_pret, titre, datePret, dateRetourPrevue FROM VueEmpruntsEnCoursParAdherent WHERE id_adherent = {adherent_id}"
    resp = execute_query(conn, query)
    print("## Emprunts en cours ##")
    if not resp:
        print("Aucun emprunt en cours.")
        return
    for ligne in resp:
        # calculer la date de retour
        date_pret = ligne[2]
        date_retour_prevue = ligne[3]
        print(f"ID Emprunt: {ligne[0]}, Titre: {ligne[1]}, Emprunté le {date_pret.strftime('%d/%m/%Y')}, Date de retour prevue: {date_retour_prevue.strftime('%d/%m/%Y')}")


def afficher_historique_emprunts(conn, adherent_id):
    query = f"SELECT id_pret, titre, datePret, dateRendu FROM biblio.VueHistoriqueEmpruntsParAdherent WHERE id_adherent = {adherent_id}"
    resp = execute_query(conn, query)
    print("## Historique des emprunts ##")
    
    if not resp:
        print("Aucun emprunt terminé.")
        return
    
    for ligne in resp:
        date_pret = ligne[2]
        date_rendu = ligne[3]
        print(f"ID Emprunt: {ligne[0]}, Titre: {ligne[1]}, Emprunté le {date_pret.strftime('%d/%m/%Y')}, Rendu le {date_rendu.strftime('%d/%m/%Y')}")