def execute_query(conn, query, params=None):
    """Exécute une requête SQL sur la base de données et retourne les résultats."""
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
            if cursor.description:
                return cursor.fetchall()
    except Exception as e:
        print(f"Erreur lors de l'exécution de la requête : {e}")
        conn.rollback()

def reset_sequence(conn):
    """
    Fonction pour réinitialiser la séquence du champ 'id_adherent' 
    pour qu'elle commence à la prochaine valeur disponible.
    """
    try:
        # Ajuste la séquence pour commencer desde el siguiente valor disponible
        reset_serial_query = """
            SELECT SETVAL('biblio.adherent_id_adherent_seq', COALESCE(
                (SELECT MAX(id_adherent) FROM biblio.Adherent), 1));
        """
        execute_query(conn, reset_serial_query)
        print("Séquence d'ID réinitialisée avec succès.")
    except Exception as e:
        print(f"Erreur lors de la réinitialisation de la séquence : {e}")