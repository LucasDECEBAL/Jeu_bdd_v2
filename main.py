# PROGRAMME PRINCIPAL
#   MENU
#   Si le choix est 1
#       PARTIE
#   Si le choix est 2
#       Afficher les scores
#   Si le choix est 3
#       Quitter

# MENU
#   Repeter
#       Afficher 3 options (1 Jouer, 2 Scores, 3 Quitter)
#       Lire la reponse du joueur
#       Si la reponse fait partie des options
#           Retourner le choix valide

# PARTIE
#   Demander un pseudo au joueur
#   Repeter
#       CREATION DE L'EQUIPE
#       Lancer le combat et recuperer le score
#       Enregistrer le score
#       Afficher le score de la partie
#       Si le joueur ne veut pas rejouer
#           Sortir

# CREATION DE L'EQUIPE
#   Creer une equipe vide
#   Repeter jusqu'a avoir 3 personnages
#       Afficher les personnages disponibles
#       Demander le nom du personnage
#       VERIFICATION DU PERSONNAGE
#       Si la verification renvoie vrai
#           Charger le personnage depuis la bdd
#           Ajouter le personnage a l'equipe
#           AFFICHAGE DE L'EQUIPE
#   Retourner l'equipe complete

# AFFICHAGE DE L'EQUIPE
#   Afficher le titre "Mon equipe"
#   Parcourir les personnages
#       Afficher nom attaque defense et points de vie

# VERIFICATION DU PERSONNAGE
#   Si le personnage n'est pas deja dans l'equipe et qu'il existe en base
#       Retourner vrai
#   Sinon
#       Retourner faux