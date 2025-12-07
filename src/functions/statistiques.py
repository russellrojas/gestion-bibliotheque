import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backend_bases import MouseEvent
from .utils.db_actions import execute_query
import random



import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backend_bases import MouseEvent
from .utils.db_actions import execute_query
import random


def generer_graphique_historique_emprunts(conn):
    """
    Génère un graphique interactif des historiques d'emprunts.
    Affiche les emprunts en cours, rendus et en retard par adhérent.
    Lorsqu'une barre est cliquée, affiche les ressources empruntées et le compte utilisateur.
    """
    print("\n## Génération d'un graphique des historiques d'emprunts ##")

    query = """
        SELECT 
            (a.informationsadherent->>'nom')::text || ' ' || (a.informationsadherent->>'prenom')::text AS adherent, 
            COUNT(CASE WHEN p.statut = 'en cours' AND p.dateRendu >= CURRENT_DATE THEN 1 END) AS en_cours,
            COUNT(CASE WHEN p.statut = 'en cours' AND p.dateRendu < CURRENT_DATE THEN 1 END) AS en_retard,
            COUNT(CASE WHEN p.statut = 'rendu' THEN 1 END) AS rendus,
            COUNT(*) AS total, 
            STRING_AGG(r.titre || ' (Prêt: ' || p.datePret || ', Rendu: ' || COALESCE(p.dateRendu::text, 'Non rendu') || ')', ', ') AS ressources,
            STRING_AGG(
                CASE 
                    WHEN r.codeRessource IN (SELECT codeRessource FROM biblio.Livre) THEN 'Livre'
                    WHEN r.codeRessource IN (SELECT codeRessource FROM biblio.Film) THEN 'Film'
                    WHEN r.codeRessource IN (SELECT codeRessource FROM biblio.OeuvreMusicale) THEN 'Oeuvre Musicale'
                    ELSE 'Autre'
                END, ', ') AS type_ressources,
            a.compteUtilisateur
        FROM biblio.Pret p
        JOIN biblio.Adherent a ON p.adherent = a.id_adherent
        JOIN biblio.Exemplaire e ON p.exemplaire = e.id_exemplaire
        JOIN biblio.Ressource r ON e.ressource = r.codeRessource
        GROUP BY (a.informationsadherent->>'nom')::text, (a.informationsadherent->>'prenom')::text, a.compteUtilisateur
        ORDER BY total DESC;
    """
    resp = execute_query(conn, query)

    if not resp:
        print("Aucune donnée à afficher.")
        return

    adherents = [row[0] for row in resp]
    en_cours = [row[1] for row in resp]
    en_retard = [row[2] for row in resp]
    rendus = [row[3] for row in resp]
    ressources = [row[5] for row in resp]
    types_ressources = [row[6] for row in resp]  # Les types de ressources
    comptes_utilisateur = [row[7] for row in resp]

    x = np.arange(len(adherents))
    fig, ax = plt.subplots(figsize=(14, 8))

    bars_rendus = ax.bar(x, rendus, width=0.6, label='Rendus', color='#4CAF50', zorder=3)
    bars_en_retard = ax.bar(x, en_retard, width=0.6, bottom=rendus, label='En retard', color='#F44336', zorder=3)
    bars_en_cours = ax.bar(x, en_cours, width=0.6, bottom=np.array(rendus) + np.array(en_retard), label='En cours', color='#FF9800', zorder=3)

    ax.set_xlabel('Adhérents', fontsize=12, fontweight='bold')
    ax.set_ylabel('Nombre d\'emprunts', fontsize=12, fontweight='bold')
    ax.set_title('Historique des emprunts par adhérent (trié par total)', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(adherents, rotation=45, ha='right', fontsize=10, fontweight='light')
    ax.set_ylim(0, max(en_cours) + max(en_retard) + max(rendus) + 5)

    ax.legend(title="Statut de l'emprunt", title_fontsize='13', loc='upper left', fontsize='11')
    for i in range(len(adherents)):
        total_emprunts = en_cours[i] + en_retard[i] + rendus[i]
        ax.text(x[i], total_emprunts + 0.5, str(total_emprunts), ha='center', va='bottom', fontsize=10)

    plt.style.use('seaborn-v0_8-deep')

    def on_click(event: MouseEvent):
        if event.inaxes != ax: return
        bar_width = event.xdata
        if bar_width is None: return

        bar_idx = int(np.floor(bar_width))
        if bar_idx >= len(ressources): return

        print(f"\nDétails des emprunts pour l'adhérent {adherents[bar_idx]} (Compte Utilisateur: {comptes_utilisateur[bar_idx]}):")
        print(f"Ressources empruntées : {ressources[bar_idx]}")
        print(f"Type de ressource : {types_ressources[bar_idx]}")  # Affichage du type de ressource

    fig.canvas.mpl_connect('button_press_event', on_click)

    plt.tight_layout()
    plt.show()


def suggérer_ressources(conn):
    """
    Suggère jusqu'à 3 ressources pour un utilisateur spécifique en fonction des genres qu'il a empruntés,
    et indique également le type de chaque ressource. Si plus de 3 ressources sont trouvées, en choisir 3 au hasard.
    """
    print("\n## Suggestions de ressources personnalisées ##")

    compte_utilisateur = input("Veuillez entrer votre identifiant (compte utilisateur) : ").strip()

    query_check_user = """
        SELECT id_adherent, (informationsadherent->>'nom')::text || ' ' || (informationsadherent->>'prenom')::text AS nom_complet
        FROM biblio.Adherent
        WHERE compteUtilisateur = %s;
    """
    user_resp = execute_query(conn, query_check_user, (compte_utilisateur,))

    if not user_resp:
        print("Identifiant non trouvé. Veuillez vérifier et réessayer.")
        return

    nom_complet = user_resp[0][1]
    print(f"Utilisateur trouvé : {nom_complet}")

    query_suggestions = """
        WITH genres_empruntes AS (
            SELECT r.genre, COUNT(*) AS nb_emprunts
            FROM biblio.Pret p
            JOIN biblio.Exemplaire e ON p.exemplaire = e.id_exemplaire
            JOIN biblio.Ressource r ON e.ressource = r.codeRessource
            WHERE p.adherent = (SELECT id_adherent FROM biblio.Adherent WHERE compteUtilisateur = %s)
            GROUP BY r.genre
            ORDER BY nb_emprunts DESC
        )
        SELECT DISTINCT r.titre, r.genre,
            CASE 
                WHEN r.codeRessource IN (SELECT codeRessource FROM biblio.Livre) THEN 'Livre'
                WHEN r.codeRessource IN (SELECT codeRessource FROM biblio.Film) THEN 'Film'
                WHEN r.codeRessource IN (SELECT codeRessource FROM biblio.OeuvreMusicale) THEN 'Oeuvre Musicale'
                ELSE 'Autre'
            END AS type_ressource
        FROM genres_empruntes ge
        JOIN biblio.Ressource r ON r.genre = ge.genre
        WHERE NOT EXISTS (
            SELECT 1
            FROM biblio.Pret p
            JOIN biblio.Exemplaire e ON p.exemplaire = e.id_exemplaire
            WHERE e.ressource = r.codeRessource AND p.adherent = (SELECT id_adherent FROM biblio.Adherent WHERE compteUtilisateur = %s)
        );
    """
    suggestions_resp = execute_query(conn, query_suggestions, (compte_utilisateur, compte_utilisateur))

    if suggestions_resp:
        print(f"Voici des suggestions pour l'utilisateur {nom_complet} :")
        
        # Si plus de 3 suggestions, on sélectionne 3 au hasard
        if len(suggestions_resp) > 3:
            suggestions_resp = random.sample(suggestions_resp, 3)
        
        for row in suggestions_resp:
            print(f"- Titre: {row[0]}, Genre: {row[1]}, Type: {row[2]}")  # Affiche le type de ressource
    else:
        print(f"Aucune suggestion disponible pour l'utilisateur {nom_complet}.")


def afficher_documents_plus_empruntes(conn):
    """
    Affiche les documents les plus empruntés, en incluant le type de chaque ressource.
    """
    print("\n## Documents les Plus Empruntés ##")
    
    query = """
        SELECT r.titre, 
               COUNT(p.id_pret) AS nb_emprunts,  -- Correction du nom de la colonne
               CASE 
                   WHEN r.codeRessource IN (SELECT codeRessource FROM biblio.Livre) THEN 'Livre'
                   WHEN r.codeRessource IN (SELECT codeRessource FROM biblio.Film) THEN 'Film'
                   WHEN r.codeRessource IN (SELECT codeRessource FROM biblio.OeuvreMusicale) THEN 'Oeuvre Musicale'
                   ELSE 'Autre'
               END AS type_ressource
        FROM biblio.Pret p
        JOIN biblio.Exemplaire e ON p.exemplaire = e.id_exemplaire
        JOIN biblio.Ressource r ON e.ressource = r.codeRessource
        GROUP BY r.titre, r.codeRessource
        ORDER BY nb_emprunts DESC
        LIMIT 5;
    """
    try:
        results = execute_query(conn, query)
        if results:
            print(f"Voici les 5 documents les plus empruntés :")
            for row in results:
                print(f"- Titre: {row[0]}, Nombre d'emprunts: {row[1]}, Type: {row[2]}")
        else:
            print("Aucun document trouvé.")
    except Exception as e:
        print(f"Erreur lors de l'exécution de la requête : {e}")


def afficher_nombre_total_emprunts(conn):
    """
    Affiche le nombre total d'emprunts enregistrés, classés par statut (en cours, en retard, rendu).
    """
    print("\n## Nombre Total d'Emprunts ##")
    
    query_total = "SELECT COUNT(*) FROM biblio.Pret;"
    resp_total = execute_query(conn, query_total)

    if resp_total:
        total_emprunts = resp_total[0][0]
        print(f"Nombre total d'emprunts enregistrés : {total_emprunts}")
    else:
        print("Impossible de récupérer le nombre total d'emprunts.")

    query = """
        SELECT 
            COUNT(*) FILTER (WHERE statut = 'en cours' AND dateRendu >= CURRENT_DATE) AS en_cours,
            COUNT(*) FILTER (WHERE statut = 'rendu') AS rendu
        FROM biblio.Pret;
    """
    
    resp = execute_query(conn, query)

    if resp:
        en_cours, rendu = resp[0]
        print(f"Nombre d'emprunts en cours : {en_cours}")
        print(f"Nombre d'emprunts rendus : {rendu}")
    else:
        print("Impossible de récupérer le nombre d'emprunts.")

    query_retard = """
        SELECT COUNT(*) 
        FROM biblio.Pret P
        WHERE P.statut = 'en cours' AND P.dateRendu < CURRENT_DATE;
    """
    resp_retard = execute_query(conn, query_retard)

    if resp_retard:
        en_retard = resp_retard[0][0]
        print(f"Nombre d'emprunts en retard : {en_retard}")
    else:
        print("Impossible de récupérer le nombre d'emprunts en retard.")
