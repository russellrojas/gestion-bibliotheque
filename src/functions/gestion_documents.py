from datetime import datetime
from .utils.db_actions import execute_query


def ajouter_document(conn):
    """Ajoute un nouveau document dans la base avec un code ressource, une table spécifique et un exemplaire associé."""
    print("## Ajouter un Document ##")
    titre = input("Titre du document : ")
    while True:
        date_apparition = input("Date d'apparition (YYYY-MM-DD) : ")
        try:
            date_apparition = datetime.strptime(date_apparition, "%Y-%m-%d")
            break
        except ValueError:
            print("Erreur : le format de la date est incorrect. Veuillez entrer une date au format YYYY-MM-DD.")
    
    
    editeur = input("Éditeur (laisser vide si non applicable) : ").strip() or None
    genre = input("Genre (laisser vide si non applicable) : ").strip() or None
    

    # Génération du codeRessource et codeClassification
    query_code = "SELECT COALESCE(MAX(codeRessource), 'R000') FROM biblio.Ressource"
    resp_code = execute_query(conn, query_code)
    dernier_code = resp_code[0][0]
    numero_suivant = int(dernier_code[1:]) + 1
    code_ressource = f"R{numero_suivant:03d}"
    code_classification = code_ressource[-3:]

    while True:
        query_check_classification = "SELECT COUNT(*) FROM biblio.Ressource WHERE codeClassification = %s"
        resp_check = execute_query(conn, query_check_classification, (code_classification,))
        if resp_check[0][0] == 0:
            break
        numero_suivant += 1
        code_ressource = f"R{numero_suivant:03d}"
        code_classification = code_ressource[-3:]

    # Ajout à la table Ressource
    query_insert = """
        INSERT INTO biblio.Ressource (codeRessource, titre, dateApparition, editeur, genre, codeClassification)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING codeRessource
    """
    resp = execute_query(conn, query_insert, (code_ressource, titre, date_apparition, editeur, genre, code_classification))

    if resp:
        print(f"Document ajouté avec succès. Code Ressource : {resp[0][0]}")
        # Demande du type de document
        type_document = input("Type de document (Livre, Film, Oeuvre musicale) : ").strip().lower()

        if type_document == "livre":
            isbn = input("ISBN : ")
            resume = input("Résumé : ")
            langue = input("Langue : ")
            query_insert_livre = """
                INSERT INTO biblio.Livre (codeRessource, isbn, resume, langue)
                VALUES (%s, %s, %s, %s)
            """
            execute_query(conn, query_insert_livre, (code_ressource, isbn, resume, langue))
            print("Livre ajouté avec succès.")
        
        elif type_document == "film":
            longueur = int(input("Longueur (en minutes) : "))
            langue = input("Langue : ")
            synopsis = input("Synopsis : ")
            query_insert_film = """
                INSERT INTO biblio.Film (codeRessource, longueur, langue, synopsis)
                VALUES (%s, %s, %s, %s)
            """
            execute_query(conn, query_insert_film, (code_ressource, longueur, langue, synopsis))
            print("Film ajouté avec succès.")
        
        elif type_document == "oeuvre musicale":
            longueur = int(input("Longueur (en minutes) : "))
            query_insert_oeuvre = """
                INSERT INTO biblio.OeuvreMusicale (codeRessource, longueur)
                VALUES (%s, %s)
            """
            execute_query(conn, query_insert_oeuvre, (code_ressource, longueur))
            print("Oeuvre musicale ajoutée avec succès.")
        
        else:
            print("Erreur : type de document non reconnu. Aucun ajout dans une table spécifique.")

        # Ajout d'un exemplaire
        print("\n## Ajouter un Exemplaire ##")
        print("État de l'exemplaire :")
        print("1. Neuf")
        print("2. Bon")
        print("3. Abîmé")
        print("4. Perdu")
        while True:
            try:
                choix_etat = int(input("Choisissez l'état de l'exemplaire (1-4) : "))
                if choix_etat in [1, 2, 3, 4]:
                    etat_map = {1: 'neuf', 2: 'bon', 3: 'abime', 4: 'perdu'}
                    etat_exemplaire = etat_map[choix_etat]
                    break
                else:
                    print("Erreur : choisissez un numéro entre 1 et 4.")
            except ValueError:
                print("Erreur : entrez un nombre valide.")

        query_insert_exemplaire = """
            INSERT INTO biblio.Exemplaire (etat, ressource)
            VALUES (%s, %s)
        """
        execute_query(conn, query_insert_exemplaire, (etat_exemplaire, code_ressource))
        print(f"Exemplaire ajouté avec succès. État : {etat_exemplaire}")
    else:
        print("Erreur lors de l'ajout du document dans la table Ressource.")


def modifier_document(conn):
    """Modifie la description d'un document existant et affiche l'état avant et après modification."""
    print("## Modifier un Document ##")
    code_ressource = input("Code du document à modifier : ")
    query_select = "SELECT * FROM biblio.Ressource WHERE codeRessource = %s"
    etat_avant = execute_query(conn, query_select, (code_ressource,))

    if not etat_avant:
        print(f"Aucun document trouvé avec le code '{code_ressource}'.")
        return

    print("\n### État avant modification ###")
    print_document(etat_avant[0])
    titre = input("Nouveau titre (laisser vide pour conserver l'ancien) : ")
    date_apparition = input("Nouvelle date d'apparition (YYYY-MM-DD, laisser vide pour conserver l'ancien) : ")
    editeur = input("Nouvel éditeur (laisser vide pour conserver l'ancien) : ")
    genre = input("Nouveau genre (laisser vide pour conserver l'ancien) : ")
    code_classification = input("Nouveau code de classification (laisser vide pour conserver l'ancien) : ")

    fields, values = [], []
    if titre:
        fields.append("titre = %s")
        values.append(titre)
    if date_apparition:
        fields.append("dateApparition = %s")
        values.append(date_apparition)
    if editeur:
        fields.append("editeur = %s")
        values.append(editeur)
    if genre:
        fields.append("genre = %s")
        values.append(genre)
    if code_classification:
        fields.append("codeClassification = %s")
        values.append(code_classification)

    if not fields:
        print("Aucune modification spécifiée.")
        return

    query_update = f"UPDATE biblio.Ressource SET {', '.join(fields)} WHERE codeRessource = %s"
    values.append(code_ressource)

    execute_query(conn, query_update, tuple(values))
    etat_apres = execute_query(conn, query_select, (code_ressource,))
    print("\n### État après modification ###")
    print_document(etat_apres[0])

def supprimer_document(conn):
    """Supprime un document et toutes ses relations après confirmation."""
    print("## Supprimer un Document ##")
    code_ressource = input("Code du document à supprimer : ")
    
    # Vérification de l'existence du document
    query_select = "SELECT * FROM biblio.Ressource WHERE codeRessource = %s"
    document = execute_query(conn, query_select, (code_ressource,))

    print("\n### Document à supprimer ###")
    print_document(document[0])

    
    if not document:
        print(f"Aucun document trouvé avec le code '{code_ressource}'.")
        return

    confirmation = input("Êtes-vous sûr de vouloir supprimer ce document ? (oui/non) : ").lower()

    if confirmation == "oui":
        try:
            # Supprimer les exemplaires liés
            query_delete_exemplaires = "DELETE FROM biblio.Exemplaire WHERE ressource = %s"
            execute_query(conn, query_delete_exemplaires, (code_ressource,))

            # Supprimer des tables spécifiques
            execute_query(conn, "DELETE FROM biblio.Livre WHERE codeRessource = %s", (code_ressource,))
            execute_query(conn, "DELETE FROM biblio.Film WHERE codeRessource = %s", (code_ressource,))
            execute_query(conn, "DELETE FROM biblio.OeuvreMusicale WHERE codeRessource = %s", (code_ressource,))

            # Supprimer le document de la table Ressource
            query_delete_ressource = "DELETE FROM biblio.Ressource WHERE codeRessource = %s"
            execute_query(conn, query_delete_ressource, (code_ressource,))
            
            print("Document supprimé avec succès.")
        except Exception as e:
            print(f"Erreur lors de la suppression : {e}")
    else:
        print("Suppression annulée.")

def print_document(doc):
    """Affiche les informations d'un document de manière lisible."""
    print(f"Code : {doc[0]}")
    print(f"Titre : {doc[1]}")
    print(f"Date d'apparition : {doc[2]}")
    print(f"Éditeur : {doc[3]}")
    print(f"Genre : {doc[4]}")
    print(f"Code de classification : {doc[5]}")