# MENU
#   Repeter tant que la reponse est invalide
#       Afficher 3 options (1 Jouer, 2 Scores, 3 Quitter)
#       Lire la reponse du joueur
#       Verifier que la reponse fait partie des options
#       Si la reponse est valide
#           Retourner le choix valide
#   Lancer le processus choisi selon la reponse

# PARTIE
#   Demander un pseudo au joueur
#   Repeter
#       Construire l'equipe de 3 personnages
#       Lancer le combat et recuperer le score
#       Enregistrer le score
#       Afficher le score de la partie
#       Demander si le joueur veut rejouer
#       Si oui
#           Rejouer
#       Si non
#           Sortir

# CREATION DE L'EQUIPE
#   Creer une equipe vide
#   Repeter jusqu'a avoir 3 personnages
#       Afficher les personnages disponibles
#       Demander le nom du personnage
#       Verifier que le personnage existe et n'est pas deja pris
#       Si le nom est valide
#           Charger le personnage depuis la bdd
#           Ajouter le personnage a l'equipe
#           Afficher l'equipe courante
#   Retourner l'equipe complete

# AFFICHAGE DE L'EQUIPE
#   Afficher le titre
#   Parcourir les personnages
#       Afficher nom attaque defense et points de vie

