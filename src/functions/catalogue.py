from .utils.db_actions import execute_query

def afficher_catalogue_par_type(conn, type_ressource):
    """
    Affiche le catalogue selon le type de ressource (film, musique, livre).

    Args:
        conn: Connexion à la base de données.
        type_ressource: Type de la ressource à afficher (film, musique, livre).
    """
    # Requête adaptée pour chaque type de ressource
    if type_ressource == "film":
        # Utilise la vue VueCatalogueLivres
        query = """
            SELECT * FROM VueCatalogueFilms;
        """
    elif type_ressource == "musique":
        query = """
            SELECT * FROM VueCatalogueOeuvresMusicales;
        """
    elif type_ressource == "livre":

        query = """
            SELECT * FROM VueCatalogueLivres;
        """
    else:
        print("Type de ressource invalide.")
        return

    resp = execute_query(conn, query)
    print(f"## Catalogue des {type_ressource}s ##")
    if not resp:
        print(f"Aucun {type_ressource} trouvé.")
        return
    for ressource in resp:
        print(f"Code: {ressource[0]}, Titre: {ressource[1]}, Genre: {ressource[2]}, Exemplaires: {ressource[3]}")

def rechercher_films(conn):
    query = """
    SELECT codeRessource, titre, genre, nombre_disponible
    FROM biblio.VueFilmsDisponibles
    """
    resp = execute_query(conn, query)
    print("\nFilms disponibles:")
    if not resp:
        print("Aucun film disponible.")
        return
    for ligne in resp:
        print(f"Code: {ligne[0]}, Titre: {ligne[1]}, Genre: {ligne[2]}, Nombre disponible: {ligne[3]}")
    input("Appuyez sur une touche pour continuer...")

def rechercher_oeuvres_musicales(conn):
    query = """
    SELECT codeRessource, titre, genre, nombre_disponible
    FROM biblio.VueOeuvresMusicalesDisponibles
    """
    resp = execute_query(conn, query)
    print("\nŒuvres musicales disponibles:")
    if not resp:
        print("Aucune œuvre musicale disponible.")
        return
    for ligne in resp:
        print(f"Code Ressource: {ligne[0]}, Titre: {ligne[1]}, Genre: {ligne[2]}, Nombre disponible: {ligne[3]}")
    input("Appuyez sur une touche pour continuer...")

def rechercher_livres(conn):
    query = """
    SELECT codeRessource, titre, genre, nombre_disponible
    FROM biblio.VueLivresDisponibles
    """
    resp = execute_query(conn, query)
    print("\nLivres disponibles:")
    if not resp:
        print("Aucun livre disponible.")
        return
    for ligne in resp:
        print(f"Code Ressource: {ligne[0]}, Titre: {ligne[1]}, Genre: {ligne[2]}, Nombre disponible: {ligne[3]}")
    input("Appuyez sur une touche pour continuer...")