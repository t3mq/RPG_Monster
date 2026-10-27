from models import Character, Monster
from utils import get_random_monster

import random

# savoir si l'équipe est toujours en vie
# définir team_alive(team):
#   pour chaque perso dans equipe
#       si perso est vivant : renvoyer True
#   (après la boucle) renvoyer False
def team_alive(team):
    for character in team:
        if character.is_alive():
            return True
        else:
            return False
        
# vague de combat
# définir start_game(team):
#   waves = 0 
#
#   tant que l'équipe est vivante
#       doc = get_random_monster()
#       monster = monstré crée à partir du doc
#       afficher "Vague X": un <monstre> apparait (avec ces stats)

#
#   tant que monstre est vivant ET l'équipe est vivante
#       (les perso attaques d'abord)
#       pour chaque perso dans l'équipe
#           si le perso est vivant ET le monstre est vivant
#               damage = perso attaque monstre
#               afficher qui attaque, combien de degats, PV restants du monstre

#       si le monstre est mort
#           afficher "victoire"
#           waves = waves + 1
#           sortir de cette boucle (break)
#
#       (au tour du monstre)
#       alive = liste des perso de l'équipe qui sont vivant
#       target = un perso au hasard dans vivant (random.choice)
#       damage = monstre attaque cible 
#       afficher qui est attaqué, combien de dégats, PV restants
#       si la cible est mort : afficher <character (name)> est K.O
#
#   afficher "Défaite !"
#   return waves
