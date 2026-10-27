from models import Character, Monster
from utils import get_db, get_random_monster
import random

# vérifier si l'équipe est toujours en vie
# pour chaque personnage de l'équipe 
# si le personnage est en vie 
#   retourne True 
# si aucun personnage n'est vivant, retourne false
def team_alive(team):
    for character in team:
        if character.is_alive():
            return True
    # renvoie falese seulement après avoir vérifié toute l'équipe
    return False

# créer un objet Monstre à partir de la base de données
# récupérer un document de monstre aléatoire depuis la DB
# si aucun docuement n'est pas trouvé, retourner None
# instancier et retourner un objet Monster avec les données
def create_monster():
    doc = get_random_monster()
    if not doc:
        return None
    return {
        "name": doc.get("name", "Monstre"),
        "pv": doc.get("pv", 50),
        "attack": doc.get("atk", 10)
    }

# gérer les attaques de la team sur les monstre
# Pour chaque personnage de l'équipe
#   si le personnage est vivant ET que le monstre est encore en vie
#       le personnage attaque le monstre 
#       afficher le combat
def handle_character_attacks(team, monster):
    for character in team:
        if character.is_alive() and monster["pv"] > 0:
            damage = getattr(character, "attack", getattr(character, "atk", 10))
            monster["pv"] -= damage
            if monster["pv"] < 0:
                monster["pv"] = 0

            print(f"{character.name} attaque {monster['name']} : {damage} dégâts, PV restants du monstre: {monster['pv']}")

# gère les attaques du monstre sur une cible aléatoire
# Filtre la liste pour obtenir uniquement les personnages vivant
# s'il ne reste aucun personnage vivant, arrêt de la fonction
# choisir aléatoirement une cible parmis la liste des personnages vivant
# le monstre attaque la cible et inflige les dégats
# affiche le combat
def handle_monster_attacks(team, monster):
    alive = [c for c in team if c.is_alive()]
    if not alive:
        return

    target = random.choice(alive)
    damage = monster["attack"]

    target.pv -= damage
    if target.pv < 0:
        target.pv = 0

    print(f"{monster['name']} attaque {target.name} : {damage} dégâts, PV restant : {target.pv}")

    if not target.is_alive():
        print(f"character ({target.name}) est K.O")

# orchestre la boucle principale du jeu
# initialiser le compteur de vague à 0
# tant que l'équipe est en vie,  enchaîne les vagues 
#   generer un monstre pour la vague
#   incrémente le numéro de la vague
#   affiche l'apparition du monstr
# tour d'attaque des personnages
#   si le monstre est vaincu pendant le tour des personnages
# tour d'attaque du monstre
# equipe mort = arrêt de la fonction
def start_game(team):
    waves = 0

    while team_alive(team):
        monster = create_monster()
        if not monster:
            print("Erreur : aucun monstre trouvé")
            break

        waves += 1
        print(f"\n Vague {waves} : un {monster['name']} apparait (PV: {monster['pv']}, Attaque : {monster['attack']})")

        while monster['pv'] > 0 and team_alive(team):
            handle_character_attacks(team, monster)

            if monster['pv'] <= 0:
                print("victoire")
                break

            handle_monster_attacks(team, monster)

    print("Défaite")
    print(f"Nombre total de vagues survécues : {waves}")
    return waves
