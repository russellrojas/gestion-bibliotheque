from .utils.db_actions import execute_query

def voir_exemplaires_document(conn):
    print("## Voir les Exemplaires d'un Document ##")
    code_ressource = input("Code ressource du document : ")
    
    query = "SELECT * FROM biblio.Exemplaire WHERE ressource = %s"
    exemplaires = execute_query(conn, query, (code_ressource,))
    
    if exemplaires:
        for exemplaire in exemplaires:
            print(f"ID Exemplaire : {exemplaire[0]}, Etat : {exemplaire[1]}")
    else:
        print(f"Aucun exemplaire trouvé pour le code ressource '{code_ressource}'.")

def ajouter_exemplaire(conn):
    """Ajoute un exemplaire pour un document donné."""
    print("## Ajouter un Exemplaire ##")
    code_ressource = input("Code Ressource du document : ")
    etat = input("État de l'exemplaire (neuf, bon, abîmé, perdu) : ")
    query = """
        INSERT INTO biblio.Exemplaire (etat, ressource)
        VALUES (%s, %s)
        RETURNING id_exemplaire
    """
    resp = execute_query(conn, query, (etat, code_ressource))

    if resp:
        print(f"Exemplaire ajouté avec succès. ID Exemplaire : {resp[0][0]}")
    else:
        print("Erreur lors de l'ajout de l'exemplaire.")

def modifier_etat_exemplaire(conn):
    """
    Fonction interractive pour modifier l'état d'un exemplaire.
    """
    print("## Modifier l'état d'un Exemplaire ##")
    id_exemplaire = input("ID de l'exemplaire : ")

    # Vérifier si l'exemplaire existe
    query = "SELECT * FROM biblio.Exemplaire WHERE id_exemplaire = %s"
    exemplaire = execute_query(conn, query, (id_exemplaire,))

    if not exemplaire:
        print("Aucun exemplaire correspondant trouvé.")
        return

    # Demander l'etat
    etats = ["neuf", "bon", "abîmé", "perdu"]
    etat = input("État (1. neuf, 2. bon, 3. abîmé, 4. perdu) : ")
    
    try:
        etat = etats[int(etat) - 1]
    except (ValueError, IndexError):
        print("Etat invalide. Veuillez entrer un nombre entre 1 et 4.")
        return
    
    query = "UPDATE biblio.Exemplaire SET etat = %s WHERE id_exemplaire = %s"
    execute_query(conn, query, (etat, id_exemplaire))
    
    print("Etat modifié avec succès.")

def supprimer_exemplaire(conn):
    print("## Supprimer un Exemplaire ##")
    id_exemplaire = input("ID de l'exemplaire : ")

    query_select = "SELECT * FROM biblio.Exemplaire WHERE id_exemplaire = %s"
    exemplaire = execute_query(conn, query_select, (id_exemplaire,))

    if not exemplaire:
        print("Aucun exemplaire trouvé.")
        return

    query = "DELETE FROM biblio.Exemplaire WHERE id_exemplaire = %s"
    execute_query(conn, query, (id_exemplaire,))
    print("Exemplaire supprimé avec succès.")