import random


# EST VIVANT
def est_vivant(personnage):
#   Recevoir un personnage
#   Retourner vrai si ses points de vie sont superieurs a 0
    return personnage["hp"] > 0

# CALCULER LES DEGATS
def calculer_degats(attaquant, cible):
#   Soustraire la defense de la cible a l'attaque de l'attaquant
    degats = attaquant["atk"] - cible["def"]
#   Garantir au moins 1 degat
    if degats < 1:
        return 1
#   Retourner les degats
    return degats

# ATTAQUER
def attaquer(attaquant, cible):
#   Calculer les degats sur la cible
    degats = calculer_degats(attaquant, cible)
#   Une chance sur cinq de coup critique
    if random.randint(1, 5) == 1:
#       Doubler les degats et annoncer le critique
        degats = degats * 2
        print(f"Coup critique de {attaquant['name']} !")
#   Retirer les degats aux points de vie de la cible
    cible["hp"] = cible["hp"] - degats
#   Ne jamais descendre sous 0
    if cible["hp"] < 0:
        cible["hp"] = 0

# PERSONNAGES VIVANTS
def personnages_vivants(equipe):
#   Recevoir une equipe
#   Retourner la liste des personnages vivants
    return [personnage for personnage in equipe if est_vivant(personnage)]

# RETIRER LES MORTS
def retirer_les_morts(equipe):
#   Parcourir une copie de l'equipe
    for personnage in list(equipe):
#   Retirer les personnages qui ne sont plus vivants
        if not est_vivant(personnage):
            equipe.remove(personnage)

# EQUIPE VIDE
def equipe_vide(equipe):
#   Retourner vrai si l'equipe n'a plus personne
    return len(equipe) == 0