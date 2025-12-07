from .utils.options import DUREE_PRET_PAR_DEFAUT
from .utils.db_actions import execute_query
from .sanctions import suspension_pour_retard
from .emprunts_personnel import check_suspendu_adherent, check_emprunt_exemplaire, check_suspendu_adherent, enregistrer_emprunt, enregistrer_emprunt_rendu, check_max_emprunts
from datetime import datetime, timedelta, date


def afficher_emprunts_actifs(conn):
    query = "SELECT * FROM biblio.VueEmpruntsEnCoursParAdherent"
    resp = execute_query(conn, query)
    print("## Emprunts en cours ##")
    if not resp:
        print("Aucun emprunt en cours.")
        return
    for emprunt in resp:
        print(f"ID Adhérent: {emprunt[0]}, "
              f"ID Emprunt: {emprunt[4]}",
              f"Nom: {emprunt[1]} {emprunt[2]}, "
              f"Titre: {emprunt[3]}, "
              f"Date Prêt: {emprunt[5].strftime('%d/%m/%Y')}, "
              f"Date Retour Prévue: {emprunt[6].strftime('%d/%m/%Y')}")

    input("Appuyez sur une touche pour continuer...")

def afficher_emprunts_retard(conn):
    query = "SELECT * FROM biblio.VueEmpruntsEnRetard"
    resp = execute_query(conn, query)

    # SELECT P.id_pret, P.datePret, P.dateRendu, A.nom, A.prenom, E.id_exemplaire, E.etat
    
    print("## Emprunts en retard ##")
    if not resp:
        print("Aucun emprunt en retard.")
        return
    for emprunt in resp:
        print(f"ID Adhérent: {emprunt[0]}, "
              f"ID Emprunt: {emprunt[4]}",
              f"Nom: {emprunt[1]} {emprunt[2]}, "
              f"Titre: {emprunt[3]}, "
              f"Date Prêt: {emprunt[5].strftime('%d/%m/%Y')}, "
              f"Date Retour Prévue: {emprunt[6].strftime('%d/%m/%Y')}")

    input("Appuyez sur une touche pour continuer...")

def ajouter_emprunt(conn):
    """ 
    Fonction interractive permettant à un membre du personnel d'enregistrer un emprunt pour un adhérent.
    """

    # input n° adherent
    n_adherent = input("Entrez le n° de l'adhérent: ")

    # input n° exemplaire
    n_exemplaire = input("Entrez le n° de l'exemplaire: ")

    # valider la date d'emprunt
    date_emprunt = datetime.now()

    # durée du pret par défault : importé de options
    duree_pret = DUREE_PRET_PAR_DEFAUT

    # valider la durée du pret
    duree_input = input(f"Entrez la durée du prêts (si vide, 14 jours) : ")
    if duree_input:
        try:
            duree_pret = int(duree_input)
        except ValueError:
            print("Format de durée incorrect. Utilisation de 14 jours.")

    date_rendu = date_emprunt + timedelta(days=duree_pret)

    print(f"Date de rendu : {date_rendu.strftime('%d/%m/%Y')}")
    print("Vérification des conditions d'emprunt...")

    # vérifier si le exemplaire peut être emprunté
    if not check_emprunt_exemplaire(conn, n_exemplaire):
        return
    
    # vérifier si l'adhérent est suspendu ou blacklisté
    if check_suspendu_adherent(conn, n_adherent):
        return
    
    if check_max_emprunts(conn, n_adherent):
        return

    print("Emprunt possible, enregistrement...")

    # enregistrer l'emprunt
    resp = enregistrer_emprunt(conn, n_adherent, n_exemplaire, date_emprunt, date_rendu) 
    
    if resp:
        print(f"Emprunt enregistré avec le n° {resp[0][0]}")
    else:
        print("Echec de l'emprunt.")

def rendu_emprunt(conn):
    """
    Fonction interractive permettant à un membre du personnel de marquer un emprunt comme rendu.
    """
    # input n° emprunt
    n_emprunt = input("Entrez le n° de l'emprunt: ")

    # verifier si l'emprunt existe
    query = "SELECT id_pret, statut, dateRendu, adherent FROM biblio.Pret WHERE id_pret = %s"
    resp = execute_query(conn, query, (n_emprunt,))

    if not resp:
        print("L'emprunt n'existe pas.")
        return
    
    # vérifier que l'emprunt n'est pas deja rendu
    if resp[0][1] == "rendu":
        print("L'emprunt est deja rendu.")
        return

    # Vérifier si il y avait un retard
    if resp[0][2] < date.today():
        duree_retard = (date.today() - resp[0][2]).days
        suspension_pour_retard(conn, resp[0][3], duree_retard)
    
    # marquer l'emprunt comme rendu
    enregistrer_emprunt_rendu(conn, n_emprunt)

    print("Emprunt marqué comme rendu.")