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
    choix = demander("1. Jouer\n2. Classement\n3. Quitter\nVotre choix : " ["1", "2", "3"],)
#   Retourner le choix
    return choix

# PARTIE
def partie(db):
#   DEMANDER un pseudo au joueur
    pseudo = demander("Ton pseudo : ")
#   CREER L'UTILISATEUR
    creer_utilisateur(db, pseudo)
#   Repeter
    while True:
#       CREATION DE L'EQUIPE
        equipe = creation_de_l_equipe(db)
#       RECUPERER LES MONSTRES
        monstres = recuperer_les_monstres(db)
#       Lancer le combat et recuperer le score
        score = game.start_fight(equipe, monstres)
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
def creation_de_l_equipe(db):
#   Creer une equipe vide
    equipe = []
#   RECUPERER LES PERSONNAGES DISPONIBLES
    personnages = recuperer_les_personnages(db)
#   Repeter jusqu'a avoir 3 personnages
    while len(equipe) < 3:    
#       Afficher les personnages disponibles numerotes a partir de 1
        for position, personnage_affiche in enumerate(personnages, start=1):
            print(f"{position}. {personnage_affiche['name']} : {personnage_affiche['atk']} ATK -- {personnage_affiche['def']} DEF -- {personnage_affiche['hp']} PV")
#       DEMANDER le numero parmi (1 a len)
        numeros = [str(n) for n in range(1, len(personnages) + 1)]
#       Prendre le personnage a la position numero - 1
        personnage = personnages[int(numero) - 1]
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

# RECUPERER LES PERSONNAGES DISPONIBLES
#   Lire tous les personnages de la collection characters
#   Si la liste est vide
#       Afficher "Aucun personnage dans la bdd, lance db_init.py"
#       Quitter
#   Sinon
#       Retourner la liste

# DEMANDER
#   Repeter jusqu'a obtenir une reponse valide
#       Afficher le message et lire la reponse du joueur
#       Si la reponse n'est pas valide
#           Afficher "Reponse incorrect, recommence"
#   Retourner la reponse

# AFFICHAGE DE L'EQUIPE
#   Afficher le titre "Mon equipe"
#   Parcourir les personnages
#       Afficher nom attaque defense et points de vie

# RECUPERER LES SCORES
#   Lire l'historique du joueur dans la bdd
#   Si le joueur n'existe pasc
#       Retourner une liste vide
#   Si la liste contient plus de 3 scores
#       Garder les 3 meilleurs
#   Retourner la liste

# AFFICHAGE DU CLASSEMENT
#   Recevoir la liste des scores
#   Si la liste est vide
#       Afficher "Aucun score enregistre"
#   Sinon
#       Parcourir la liste
#           Afficher chaque score avec son numero

# REJOUER
#   DEMANDER la reponse parmi (Oui, Non)
#   Si la reponse est Oui
#       Retourner vrai
#   Sinon
#       Retourner faux

# POINT D'ENTREE
#   Connexion a la bdd
#   Lancer le programme
#   Fermer la connexion