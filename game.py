import random
import time

import personnages


# LANCER LE COMBAT
def lancer_le_combat(equipe, monstres):
#   Initialiser le numero de manche a 1
    manche = 1
#   Repeter
    while True:
#       TIRER UN MONSTRE
        monstre = tirer_un_monstre(monstres, manche)
#       Afficher le numero de manche
        print(f"Manche {manche}")
#       JOUER UNE MANCHE
        jouer_une_manche(equipe, monstre)
#       Si EQUIPE VIDE
        if personnages.equipe_vide(equipe):
#           Afficher la fin de la partie
            print(f"Partie terminee a la manche {manche}")
#           Retourner le numero de manche
            return manche
#       Si tous les monstres ont ete vaincus
        if manche == len(monstres):
#           Afficher la victoire
            print(print(f"GG, tu as survecu a {len(monstres)} manches"))
#           Retourner le nombre de manches gagnees
            return manche
#       Passer a la manche suivante
        manche = manche + 1

# TIRER UN MONSTRE
def tirer_un_monstre(monstres, manche):
#   Trier les monstres du plus faible au plus fort
    monstres_tries = sorted(monstres, key=lambda monstre: monstre["hp"])
#   Prendre une fenetre de 3 monstres autour de la manche
    debut = max(0, manche - 2)
    fin = min(len(monstres_tries), manche + 1)
    candidats = monstres_tries[debut:fin]
#   Choisir un monstre au hasard dans la fenetre
    doc = random.choice(candidats)
#   Le transformer en personnage
    return {
        "name": doc["name"],
        "atk": doc["atk"],
        "def": doc["def"],
        "hp": doc["hp"],
    }

# JOUER UNE MANCHE
def jouer_une_manche(equipe, monstre):
#   Repeter
    while True:
#       FAIRE ATTAQUER L'EQUIPE
        equipe_attaque(equipe, monstre)
#       AFFICHER LES PARTICIPANTS
        afficher_les_participants(equipe, monstre)
#       Si le monstre n'est pas vivant
        if not personnages.est_vivant(monstre):
#           Afficher la manche gagnee
            print("Manche gagnee")
#           Sortir
            return
#       FAIRE ATTAQUER LE MONSTRE
        monstre_attaque(monstre, equipe)
#       AFFICHER LES PARTICIPANTS
        afficher_les_participants(equipe, monstre)
#       RETIRER LES MORTS
        personnages.retirer_les_morts(equipe)
#       Si EQUIPE VIDE
        if personnages.equipe_vide(equipe):
#           Afficher la manche perdue
            print("Manche perdue")
#           Sortir
            return

# FAIRE ATTAQUER L'EQUIPE
def equipe_attaque(equipe, monstre):
#   Pour chaque personnage vivant de l'equipe
    for personnage in personnages.personnages_vivants(equipe):
#       ATTAQUER le monstre
        personnages.attaquer(personnage, monstre)


# FAIRE ATTAQUER LE MONSTRE
def monstre_attaque(monstre, equipe):
#   Choisir une cible vivante au hasard
    cible = random.choice(personnages.personnages_vivants(equipe))
#   ATTAQUER la cible
    personnages.attaquer(monstre, cible)

# AFFICHER LES PARTICIPANTS
def afficher_les_participants(equipe, monstre):
#   Attendre une seconde
    time.sleep(1)
#   AFFICHAGE DE L'EQUIPE
    print("Mon equipe :")
    for personnage in equipe:
#       Afficher nom attaque defense et points de vie
        print(f"{personnage['name']} : {personnage['atk']} ATK -- {personnage['def']} DEF -- {personnage['hp']} PV")
#   Sauter une ligne
    print()
#   AFFICHAGE DU MONSTRE
    print("Monstre :")
    print(f"{monstre['name']} : {monstre['atk']} ATK -- {monstre['def']} DEF -- {monstre['hp']} PV")