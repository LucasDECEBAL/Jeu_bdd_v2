import personnages
import game
from database import create_client, database_name
from pymongo.errors import PyMongoError


# PROGRAMME PRINCIPAL
def programme_principal(db):
#   MENU
    choix = menu()
#   Si le choix est 1
    if choix == "1":
#       PARTIE
        partie(db)
#   Sinon si le choix est 2
    elif choix == "2":
#       DEMANDER un pseudo du joueur
        pseudo = demander("Votre pseudo : ")
#       RECUPERER LES SCORES
        scores = recuperer_les_scores(db, pseudo)
#       AFFICHAGE DU CLASSEMENT
        affichage_du_classement(scores)
#   Sinon
    else:
#       Quitter
        return

# MENU
def menu():
#   DEMANDER le numero parmi (1 Jouer, 2 Classement, 3 Quitter)
    choix = demander("1. Jouer\n2. Classement\n3. Quitter\nVotre choix : ", ["1", "2", "3"])
#   Retourner le choix
    return choix

# PARTIE
def partie(db):
#   DEMANDER un pseudo au joueur
    pseudo = demander("Ton pseudo : ")
#   CREER L'UTILISATEUR
    creer_utilisateur(db, pseudo)
#   CHARGER PERSONNAGES ET MONSTRES
    personnages_disponibles, monstres = charger_personnages_et_monstres(db)
#   Repeter
    while True:
#       CREATION DE L'EQUIPE
        equipe = creation_de_l_equipe(personnages_disponibles)
#       Lancer le combat et recuperer le score
        score = game.lancer_le_combat(equipe, monstres)
#       Enregistrer le score
        db["user"].update_one({"name": pseudo}, {"$push": {"score": {"$each": [score], "$sort": -1}}})
#       Afficher le score de la partie
        print(f"Ton score : {score}")
#       RECUPERER LES SCORES
        scores = recuperer_les_scores(db, pseudo)
#       AFFICHAGE DU CLASSEMENT
        affichage_du_classement(scores)
#       REJOUER
        continuer = rejouer()
#       Si REJOUER renvoie faux
        if not continuer:
#           Sortir
            break

# CREER L'UTILISATEUR
def creer_utilisateur(db, pseudo):
#   Si le joueur n'existe pas dans la bdd
    joueur = db["user"].find_one({"name": pseudo})

    if joueur is None:
#       Ajouter le joueur avec une liste de scores vide
        db["user"].insert_one({"name": pseudo, "score": []})
#   Sinon 
    else:
#       Garder le joueur et ses scores
        pass

# CREATION DE L'EQUIPE
def creation_de_l_equipe(personnages):
#   Creer une equipe vide
    equipe = []
#   Repeter jusqu'a avoir 3 personnages
    while len(equipe) < 3:
#       Afficher les personnages disponibles numerotes a partir de 1
        for position, personnage_affiche in enumerate(personnages, start=1):
            print(f"{position}. {personnage_affiche['name']} : {personnage_affiche['atk']} ATK -- {personnage_affiche['def']} DEF -- {personnage_affiche['hp']} PV")
#       DEMANDER le numero parmi (1 a len)
        numeros = [str(n) for n in range(1, len(personnages) + 1)]
        numero = demander("Numero du personnage : ", numeros)
#       Prendre le personnage a la position numero - 1
        personnage = dict(personnages[int(numero) - 1])
#       Si le personnage est deja dans l'equipe
        if any(membre["name"] == personnage["name"] for membre in equipe):
#           Afficher "Ce personnage est deja pris"
            print("Ce personnage est deja pris")
#       Sinon
        else:
#           Ajouter le personnage a l'equipe
            equipe.append(personnage)
#           AFFICHAGE DE L'EQUIPE
            affichage_de_l_equipe(equipe)
#   Retourner l'equipe
    return equipe

# CHARGER PERSONNAGES ET MONSTRES
def charger_personnages_et_monstres(db):
#   Lire tous les personnages de la collection characters
    personnages = list(db["characters"].find())
#   Si la liste est vide
    if not personnages:
#       Afficher "Aucun personnage dans la bdd, lance db_init.py"
        print("Aucun personnage dans la bdd, lance db_init.py")
#       Quitter
        raise SystemExit()
#   Lire tous les monstres de la collection monsters
    monstres = list(db["monsters"].find())
#   Si la liste est vide
    if not monstres:
#       Afficher "Aucun monstre dans la bdd, lance db_init.py"
        print("Aucun monstre dans la bdd, lance db_init.py")
#       Quitter
        raise SystemExit()
#   Retourner les personnages et les monstres
    return personnages, monstres

# DEMANDER
def demander(message, options=None):
#   Repeter jusqu'a obtenir une reponse valide
        while True:
#       Afficher le message et lire la reponse du joueur
                reponse = input(message).strip()
                if options is None:
                    valide = reponse != ""
                else:
                    valide = reponse in options
                if valide:
                    break
#       Si la reponse n'est pas valide
#           Afficher "Reponse incorrect, recommence"
                print("Reponse incorrect, recommence")
#   Retourner la reponse
        return reponse

# AFFICHAGE DE L'EQUIPE
def affichage_de_l_equipe(equipe):
#   Afficher le titre "Mon equipe"
        print("Mon equipe")
#   Parcourir les personnages
        for personnage in equipe:
#       Afficher nom attaque defense et points de vie
                print(f"{personnage['name']} : {personnage['atk']} ATK -- {personnage['def']} DEF -- {personnage['hp']} PV")

# RECUPERER LES SCORES
def recuperer_les_scores(db, pseudo):
#   Lire l'historique du joueur dans la bdd
        joueur = db["user"].find_one({"name" : pseudo})
#   Si le joueur n'existe pas
        if joueur is None:
#       Retourner une liste vide
                return []
        scores = joueur.get("score", [])
#   Si la liste contient plus de 3 scores
        if len(scores) > 3:
#       Garder les 3 meilleurs
                scores =scores[:3]
#   Retourner la liste
        return scores

# AFFICHAGE DU CLASSEMENT
def affichage_du_classement(scores):
#   Recevoir la liste des scores
#   Si la liste est vide
        if not scores:
#       Afficher "Aucun score enregistre"
                print("Aucun socre enregistre")
#   Sinon
        else:
#       Parcourir la liste
                for i, score in enumerate(scores, start=1):
#           Afficher chaque score avec son numero
                        print(f"{i}- {score}")

# REJOUER
def rejouer():
#   DEMANDER la reponse parmi (Oui, Non)
        reponse = demander("Veux tu rejouer ? (Oui/Non)", ["Oui", "Non"]) 
#   Si la reponse est Oui
        if reponse == "Oui":
#       Retourner vrai
                return True
#   Sinon
        else:
#       Retourner faux
                return False

# POINT D'ENTREE
def point_d_entree():
#   Connexion a la bdd
    client = create_client()

    try:
        db = client[database_name()]
#       Lancer le programme
        programme_principal(db)
    except PyMongoError:
        print("Connexion a MongoDB impossible, verifie le service")
    finally:
#       Fermer la connexion
        client.close()

if __name__ == "__main__":
    point_d_entree()
