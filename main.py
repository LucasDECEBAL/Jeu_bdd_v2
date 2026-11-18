# PROGRAMME PRINCIPAL
#   MENU
#   Si le choix est 1
#       PARTIE
#   Sinon si le choix est 2
#       DEMANDER un pseudo du joueur
#       RECUPERER LES SCORES
#       AFFICHAGE DU CLASSEMENT
#   Sinon
#       Quitter

# MENU
#   Afficher les 3 options numerotees
#   DEMANDER le numero parmi (1, 2, 3)
#   Retourner le choix

# PARTIE
#   DEMANDER un pseudo au joueur
#   CREER L'UTILISATEUR
#   Repeter
#       CREATION DE L'EQUIPE
#       Lancer le combat et recuperer le score
#       Enregistrer le score
#       Afficher le score de la partie
#       RECUPERER LES SCORES
#       AFFICHAGE DU CLASSEMENT
#       REJOUER
#       Si REJOUER renvoie faux
#           Sortir

# CREER L'UTILISATEUR
#   Si le joueur n'existe pas dans la bdd
#       Ajouter le joueur avec une liste de scores vide 
#   Sinon 
#       Garder le joueur et ses scores

# CREATION DE L'EQUIPE
#   Creer une equipe vide
#   RECUPERER LES PERSONNAGES DISPONIBLES
#   Repeter jusqu'a avoir 3 personnages
#       Afficher les personnages disponibles numerotes a partir de 1
#       DEMANDER le numero parmi (1 a len)
#       Prendre le personnage a la position numero - 1
#       Si le personnage est deja dans l'equipe
#           Afficher "Ce personnage est deja pris"
#       Sinon
#           Ajouter le personnage a l'equipe
#           AFFICHAGE DE L'EQUIPE
#   Retourner l'equipe

# RECUPERER LES PERSONNAGES DISPONIBLES
#   Lire tous les personnages de la collection characters
#   Si la liste est vide
#       Afficher un message d'erreur
#       Quitter
#   Sinon
#       Retourner la liste

# DEMANDER
#   Repeter jusqu'a obtenir une reponse valide
#       Afficher le message et lire la reponse du joueur
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