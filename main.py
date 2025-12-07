import psycopg2
import sys
from config import *
from src.menu_principal import gestion_menu_principal
from src.functions.utils.db_actions import *

if __name__ == "__main__":
    # A l'execution du script :
    # Connexion à la base de données
    try:
        conn = psycopg2.connect(host=HOST, dbname=DATABASE, user=USER, password=PASSWORD, options="-c search_path=biblio,public")
    except psycopg2.Error as e:
        print("Erreur lors de la connexion à la base de données:", e)
        sys.exit(1)

    gestion_menu_principal(conn)
    conn.close()