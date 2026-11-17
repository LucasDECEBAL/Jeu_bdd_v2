# PROGRAMME PRINCIPAL
#   MENU
#   Si le choix est 1
#       PARTIE
#   Si le choix est 2
#       Demander un pseudo au joueur
#       RECUPERER LES SCORES
#       AFFICHAGE DU CLASSEMENT
#   Si le choix est 3
#       Quitter

# MENU
#   Repeter
#       Afficher 3 options (1 Jouer, 2 Classement, 3 Quitter)
#       Lire la reponse du joueur
#       Si la reponse fait partie des options
#           Retourner le choix valide

# PARTIE
#   Demander un pseudo au joueur
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
#       Afficher les personnages disponibles
#       Demander le nom du personnage
#       VERIFICATION DU PERSONNAGE
#       Si la verification renvoie vrai
#           Charger le personnage depuis la liste
#           Ajouter le personnage a l'equipe
#           AFFICHAGE DE L'EQUIPE
#   Retourner l'equipe complete

# RECUPERER LES PERSONNAGES DISPONIBLES
#   Lire tous les personnages de la collection charcters
#   Si la liste est vide
#       Afficher un message d'erreur
#       Quitter
#   Sinon
#       Retourner la liste

# VERIFICATION DU PERSONNAGE
#   Si le personnage n'est pas deja dans l'equipe et qu'il existe dans la liste
#       Retourner vrai
#   Sinon
#       Retourner faux

# AFFICHAGE DE L'EQUIPE
#   Afficher le titre "Mon equipe"
#   Parcourir les personnages
#       Afficher nom attaque defense et points de vie

# RECUPERER LES SCORES
#   Lire l'historique du joueur dans la bdd
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
#   Repeter
#       Demander au joueur s'il veut rejouer ou non
#       Repeter tant que la reponse n'est pas Oui ou Non en lui redemandant d'ecrire une reponse correcte
#       Lire la reponse du joueur
#       Si la reponse est Oui
#           Retourner vrai
#       Sinon
#           Retourner faux

# POINT D'ENTREE
#   Connexion a la bdd
#   Lancer le programme
#   Fermer la connexion