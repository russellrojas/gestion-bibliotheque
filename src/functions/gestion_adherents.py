from .utils.db_actions import execute_query,reset_sequence
from datetime import datetime
import json

def ajouter_adherent(conn):
    """
    Ajoute un nouvel adhérent à la base de données avec gestion des erreurs et des champs obligatoires.
    """
    while True:
        try:
            print("\n=== Ajouter un adhérent ===")
            
            # Champs obligatoires
            nom = input("Nom : ").strip()
            if not nom:
                raise ValueError("Le champ 'Nom' est obligatoire.")
            
            prenom = input("Prénom : ").strip()
            if not prenom:
                raise ValueError("Le champ 'Prénom' est obligatoire.")
            
            date_naissance = input("Date de naissance (YYYY-MM-DD) : ").strip()
            if not date_naissance:
                raise ValueError("Le champ 'Date de naissance' est obligatoire.")
            
            # Validation de la date
            import datetime
            try:
                datetime.datetime.strptime(date_naissance, '%Y-%m-%d')
            except ValueError:
                raise ValueError("La date de naissance doit être au format 'YYYY-MM-DD'.")
            
            # Champs optionnels
            adresse = input("Adresse (laisser vide si non applicable) : ").strip() or None
            email = input("Email (laisser vide si non applicable) : ").strip() or None
            numero_tel = input("Numéro de téléphone (laisser vide si non applicable) : ").strip() or None
            
            # Création d'un compte utilisateur associé
            compte_utilisateur = input("Identifiant pour le compte utilisateur : ").strip()
            if not compte_utilisateur:
                raise ValueError("Le champ 'Identifiant pour le compte utilisateur' est obligatoire.")
            
            mot_de_passe = input("Mot de passe pour le compte utilisateur : ").strip()
            if not mot_de_passe:
                raise ValueError("Le champ 'Mot de passe' est obligatoire.")

            # Insertion dans la table CompteUtilisateur
            query_compte = (
                "INSERT INTO biblio.CompteUtilisateur (login, motDePasse, role) "
                "VALUES (%s, %s, 'adhérent')"
            )
            execute_query(conn, query_compte, (compte_utilisateur, mot_de_passe))

            infos_utilisateur = {
                "nom": nom,
                "prenom": prenom,
                "dateNaissance": date_naissance,
                "adresse": adresse,
                "email": email,
                "numeroTel": numero_tel
            }
            infos_utilisateur = json.dumps(infos_utilisateur)

            # Insertion dans la table Adherent
            query_adherent = (
                "INSERT INTO biblio.Adherent (informationsAdherent, "
                "adherentActuel, blacklister, compteUtilisateur) "
                "VALUES (%s, %s, %s, %s);"
            )
            params_adherent = (
                infos_utilisateur,
                True,  # adherentActuel par défaut
                False,  # blacklister par défaut
                compte_utilisateur,
            )
            execute_query(conn, query_adherent, params_adherent)

            print("Adhérent ajouté avec succès !")
            break

        except ValueError as e:
            print(f"Erreur : {e}")
            retry = input("Voulez-vous réessayer ? (oui/non) : ").strip().lower()
            if retry != "oui":
                print("Retour au menu précédent.")
                break

        except Exception as e:
            print(f"Erreur inattendue lors de l'ajout de l'adhérent : {e}")
            retry = input("Voulez-vous réessayer ? (oui/non) : ").strip().lower()
            if retry != "oui":
                print("Retour au menu précédent.")
                break

def modifier_adherent(conn):
    """
    Modifie les informations d'un adhérent existant.
    """
    try:
        print("\n=== Modifier un adhérent ===")
        id_adherent = input("ID de l'adhérent à modifier : ").strip()

        # Afficher les informations actuelles
        query_select = "SELECT * FROM biblio.Adherent WHERE id_adherent = %s"
        adherent = execute_query(conn, query_select, (id_adherent,))
        if not adherent:
            print("Aucun adhérent trouvé avec cet ID.")
            return

        adherent = adherent[0]  # Extraire les données
        print("\n## Informations de l'adhérent ##")
        print(f"ID: {adherent[0]}")
        print(f"Nom: {adherent[1]['nom']}")
        print(f"Prénom: {adherent[1]['prenom']}")
        print(f"Date de naissance: {adherent[1]['dateNaissance']}")
        print(f"Adresse: {adherent[1]['adresse']}")
        print(f"Email: {adherent[1]['email']}")
        print(f"Téléphone: {adherent[1]['numeroTel']}")
        # Demander les nouvelles valeurs
        print("Touchez ENTER pour ne pas modifier")
        nom = input(f"Nom : ").strip() or adherent[1]["nom"]
        prenom = input(f"Prénom : ").strip() or adherent[1]["prenom"]
        date_naissance = input(f"Date de naissance: ").strip() or adherent[1]["dateNaissance"]
        adresse = input(f"Adresse: ").strip() or adherent[1]["adresse"]
        email = input(f"Email : ").strip() or adherent[1]["email"]
        numero_tel = input(f"Numéro de téléphone: ").strip() or adherent[1]["numeroTel"]
        if adherent[2]:
            actif = input("Adhérent actif, rendre inactif ? (oui/laisser vide) : ")
            actif = not (actif.lower() == "oui")
        else:
            actif = input("Adhérent inactif, rendre actif ? (oui/laisser vide) : ")
            actif = actif.lower() == "oui"

        infos_utilisateur = {
            "nom": nom,
            "prenom": prenom,
            "dateNaissance": date_naissance,
            "adresse": adresse,
            "email": email,
            "numeroTel": numero_tel
        }
        infos_utilisateur = json.dumps(infos_utilisateur)

        # Mettre à jour les informations
        query_update = (
            "UPDATE biblio.Adherent SET informationsAdherent = %s, "
            "adherentActuel = %s WHERE id_adherent = %s"
        )
        execute_query(conn, query_update, (infos_utilisateur, actif, id_adherent))

        print("Adhérent modifié avec succès !")
    except Exception as e:
        print(f"Erreur lors de la modification de l'adhérent : {e}")

def supprimer_adherent(conn):
    """
    Fonction pour supprimer un adhérent de la base de données.
    """
    while True:
        try:
            id_adherent = input("Entrez l'ID de l'adhérent à supprimer : ").strip()

            # Vérification que l'ID est un entier
            if not id_adherent.isdigit():
                print("Erreur : L'ID doit être un nombre entier.")
                raise ValueError("ID non valide.")

            # Vérifier si l'adhérent existe
            query = "SELECT * FROM biblio.Adherent WHERE id_adherent = %s"
            adherent = execute_query(conn, query, (id_adherent,))

            if not adherent:  # Verificar si no se encontró ningún adherente
                print("Aucun adhérent trouvé avec cet ID.")
                raise ValueError("Adhérent introuvable.")
            
            adherent = adherent[0] 
            login = adherent[4]
            print(f"\nAdhérent trouvé : {adherent[1]['nom']} {adherent[1]['prenom']}")

            # Vérifier s'il y a des enregistrements liés dans Suspension
            query_suspension = "SELECT * FROM biblio.Suspension WHERE adherent = %s"
            suspensions = execute_query(conn, query_suspension, (id_adherent,))
            if suspensions:
                print(f"L'adhérent a {len(suspensions)} suspension(s).")

            # Vérifier s'il y a des enregistrements liés dans Pret
            query_pret = "SELECT * FROM biblio.Pret WHERE adherent = %s"
            prets = execute_query(conn, query_pret, (id_adherent,))
            if prets:
                print(f"L'adhérent a {len(prets)} prêt(s) en cours.")

            # Confirmar antes de eliminar
            confirmation = input("\nÊtes-vous sûr de vouloir supprimer cet adhérent ? (oui/non) : ").strip().lower()
            if confirmation != "oui":
                print("Opération annulée.")
                break
            
            # Supprimer les enregistrements liés dans Suspension
            delete_suspension = "DELETE FROM biblio.Suspension WHERE adherent = %s"
            execute_query(conn, delete_suspension, (id_adherent,))

            # Supprimer les enregistrements liés dans Pret
            delete_pret = "DELETE FROM biblio.Pret WHERE adherent = %s"
            execute_query(conn, delete_pret, (id_adherent,))

            # Supprimer adherent
            delete_adherent = "DELETE FROM biblio.Adherent WHERE id_adherent = %s"
            execute_query(conn, delete_adherent, (id_adherent,))

            # Supprimer le compte utilisateur associé
            delete_compte = "DELETE FROM biblio.CompteUtilisateur WHERE login = %s"
            execute_query(conn, delete_compte, (login,))

            reset_sequence(conn)  #reset le compteur id
            print("Adhérent supprimé avec succès.")
            break

        except ValueError as e:
            print(f"\nErreur : {e}")
            retry = input("Voulez-vous réessayer ? (oui/non) : ").strip().lower()
            if retry != "oui":
                print("Retour au menu précédent.")
                break

        except Exception as e:
            print(f"\nErreur inattendue : {e}")
            retry = input("Voulez-vous réessayer ? (oui/non) : ").strip().lower()
            if retry != "oui":
                print("Retour au menu précédent.")
                break

        break

def suspendre_adherent(conn):
    while True:
        try:
            id_adherent = input("Entrez l'ID de l'adhérent à suspendre : ")

            if not id_adherent.isdigit():
                print("Erreur : L'ID doit être un nombre entier.")
                raise ValueError("ID non valide.")

            query = f"SELECT * FROM biblio.Adherent WHERE id_adherent = {id_adherent}"
            adherent = execute_query(conn, query)

            if not adherent:
                print("Aucun adhérent trouvé avec cet ID.")
                raise ValueError("Adhérent introuvable.")

            # Vérifier si l'adhérent est blacklisté
            query = f"SELECT * FROM biblio.VueAdherentsBlacklistes WHERE id_adherent = {id_adherent}"
            resp = execute_query(conn, query)

            if resp:
                raise ValueError("L'adhérent est blacklisté, impossible de suspendre.")
                
            # Vérifier si l'adhérent est déjà suspendu
            query = f"SELECT * FROM biblio.Suspension WHERE adherent = {id_adherent}"
            suspension = execute_query(conn, query)

            if suspension:
                print("Cet adhérent est déjà suspendu.")
                raise ValueError("Adhérent déjà suspendu.")

            # Afficher les informations actuelles
            adherent = adherent[0]
            print("\n### Informations actuelles de l'adhérent ###")
            print(f"ID : {adherent[0]}")
            print(f"Nom : {adherent[1]['nom']}")
            print(f"Prénom : {adherent[1]['prenom']}")

            # Saisie des informations de suspension
            cause = input("Entrez la cause de la suspension : ").strip()

            # Validation de la date de suspension pour qu'elle soit dans le futur
            while True:
                date_suspension_input = input("Entrez la date de suspension (YYYY-MM-DD) : ").strip()
                try:
                    date_suspension = datetime.strptime(date_suspension_input, "%Y-%m-%d")
                    if date_suspension < datetime.now():
                        print("Erreur : La date de suspension doit être une date future.")
                    else:
                        break
                except ValueError:
                    print("Erreur : Le format de la date est incorrect. Utilisez le format YYYY-MM-DD.")

            # Durée de suspension
            duree_suspension = input("Entrez la durée de la suspension en jours : ").strip()

            if not duree_suspension.isdigit() or int(duree_suspension) <= 0:
                print("Erreur : La durée de suspension doit être un nombre positif.")
                raise ValueError("Durée non valide.")

            # Insérer la suspension dans la table
            query = """
                INSERT INTO biblio.Suspension (adherent, cause, dateSuspension, dureeSuspension)
                VALUES (%s, %s, %s, %s)
            """
            execute_query(conn, query, (id_adherent, cause, date_suspension, int(duree_suspension)))
            print("Suspension ajoutée avec succès.")
            break

        except ValueError as e:
            print(f"\nErreur : {e}")
            retry = input("Voulez-vous réessayer ? (oui/non) : ").strip().lower()
            if retry != "oui":
                print("Retour au menu précédent.")
                break


def blacklister_adherent(conn):
    """
    Fonction pour blacklister ou déblacklister un adhérent dans la base de données.
    """
    while True:
        try:
            id_adherent = input("Entrez l'ID de l'adhérent à blacklister ou déblacklister : ").strip()

            # Vérification que l'ID est un entier
            if not id_adherent.isdigit():
                print("Erreur : L'ID doit être un nombre entier.")
                raise ValueError("ID non valide.")

            # Vérifier si l'adhérent existe
            query = "SELECT * FROM biblio.Adherent WHERE id_adherent = %s"
            adherent = execute_query(conn, query, (id_adherent,))

            if not adherent:
                print("Aucun adhérent trouvé avec cet ID.")
                raise ValueError("Adhérent introuvable.")

            # Vérifier l'état actuel de l'adhérent
            adherent = adherent[0]
            print("\n### Informations actuelles de l'adhérent ###")
            print(f"ID : {adherent[0]}")
            print(f"Nom : {adherent[1]['nom']}")
            print(f"Prénom : {adherent[1]['prenom']}")
            print(f"Blacklisté : {'Oui' if adherent[3] else 'Non'}")

            # Demander s'il veut blacklister ou déblacklister
            if adherent[3]:  # Si l'adhérent est blacklisté
                action = input("Cet adhérent est déjà blacklisté. Voulez-vous le retirer de la liste noire ? (oui/non) : ").strip().lower()
                if action == "oui":
                    query_update = "UPDATE biblio.Adherent SET blacklister = FALSE WHERE id_adherent = %s"
                    execute_query(conn, query_update, (id_adherent,))
                    print("\nAdhérent retiré de la liste noire avec succès.")
                else:
                    print("Opération annulée.")
            else:
                action = input("Cet adhérent n'est pas blacklisté. Voulez-vous le blacklister ? (oui/non) : ").strip().lower()
                if action == "oui":
                    query_update = "UPDATE biblio.Adherent SET blacklister = TRUE WHERE id_adherent = %s"
                    execute_query(conn, query_update, (id_adherent,))
                    print("\nAdhérent blacklisté avec succès.")
                else:
                    print("Opération annulée.")

            break

        except ValueError as e:
            print(f"\nErreur : {e}")
            retry = input("Voulez-vous réessayer ? (oui/non) : ").strip().lower()
            if retry != "oui":
                print("Retour au menu précédent.")
                break

        except Exception as e:
            print(f"\nErreur inattendue : {e}")
            retry = input("Voulez-vous réessayer ? (oui/non) : ").strip().lower()
            if retry != "oui":
                print("Retour au menu précédent.")
                break


def afficher_tous_les_adherents(conn):
    """
    Affiche tous les adhérents en utilisant la vue biblio.VueAdherents.
    """
    print("## Liste de tous les adhérents ##")
    
    query = "SELECT id_adherent, nom_adherent, prenom_adherent, login FROM biblio.VueAdherents"
    results = execute_query(conn, query)
    
    if results:
        print(f"{'ID':<10}{'Nom':<20}{'Prénom':<20}{'Login':<20}")
        print("-" * 70)
        for row in results:
            print(f"{row[0]:<10}{row[1]:<20}{row[2]:<20}{row[3]:<20}")
    else:
        print("Aucun adhérent trouvé.")
    input("Appuyez sur une touche pour continuer...")

def afficher_adherents_blacklistes(conn):
    query = """
    SELECT id_adherent, nom_adherent, prenom_adherent, email_adherent, numeroTel_adherent, adresse_adherent
    FROM biblio.VueAdherentsBlackListes
    """
    resp = execute_query(conn, query)
    print("## Adhérents Blacklistés ##")

    if not resp:
        print("Aucun adhérent blacklisté.")
    else:
        for idx, ligne in enumerate(resp, 1):
            print(f"{idx}. {ligne[1]} {ligne[2]} :")
            print(f"    ID: {ligne[0]}")
            print(f"    Email: {ligne[3]}")
            print(f"    Téléphone: {ligne[4]}")
            print(f"    Adresse: {ligne[5]}")
            print("-" * 40) 
    input("Appuyez sur une touche pour continuer...")


def afficher_adherents_suspendus(conn):
    query = """
    SELECT id_adherent, nom_adherent, prenom_adherent, cause, dureeSuspension
    FROM biblio.VueAdherentsSuspendus
    """
    resp = execute_query(conn, query)
    print("## Adhérents Suspendus ##")
    
    if not resp:
        print("Aucun adhérent suspendu.")
    else:
        for idx, ligne in enumerate(resp, 1):
            print(f"{idx}. {ligne[1]} {ligne[2]} (Nom Prénom):")
            print(f"    ID: {ligne[0]}")
            cause_suspension = ligne[3] if ligne[3] is not None else "Non spécifié"
            print(f"    Cause de suspension: {cause_suspension}")
            duree_suspension = ligne[4] if ligne[4] is not None else "Non spécifié"
            print(f"    Durée de suspension: {duree_suspension} jours")
            print("-" * 40)
    
    input("Appuyez sur une touche pour continuer...")


def consulter_informations_adherent(conn):
    while True:
        try:
            id_adherent = input("Entrez l'ID de l'adhérent à consulter : ")

            # Vérification que l'entrée est un nombre entier
            if not id_adherent.isdigit():
                print("Erreur : L'ID doit être un nombre entier.")
                raise ValueError("ID non valide.")

            # Exécution de la requête
            query = f"SELECT id_adherent, informationsAdherent, adherentActuel, blacklister, compteUtilisateur FROM biblio.Adherent WHERE id_adherent = {id_adherent}"
            adherent = execute_query(conn, query)

            if not adherent:
                print("Aucun adhérent trouvé avec cet ID.")
                raise ValueError("Adhérent introuvable.")

            # Afficher les informations de l'adhérent
            adherent = adherent[0]
            print("\n## Informations de l'adhérent ##")
            print(f"ID: {adherent[0]}")
            print(f"Nom: {adherent[1]['nom']}")
            print(f"Prénom: {adherent[1]['prenom']}")
            print(f"Date de naissance: {adherent[1]['dateNaissance']}")
            print(f"Adresse: {adherent[1]['adresse']}")
            print(f"Email: {adherent[1]['email']}")
            print(f"Téléphone: {adherent[1]['numeroTel']}")
            print(f"Adhérent actif: {'Oui' if adherent[2] else 'Non'}")
            print(f"Adhérent blacklisté: {'Oui' if adherent[3] else 'Non'}")
            print(f"Compte utilisateur: {adherent[4]}")

            input("Appuyez sur une touche pour continuer...")
            break  # Sortir de la boucle si tout est correct

        except ValueError as e:
            print(f"\nErreur : {e}")
            retry = input("Voulez-vous réessayer ? (oui/non) : ").strip().lower()
            if retry != "oui":
                print("Retour au menu précédent.")
                break
