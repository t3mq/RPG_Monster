from utils import get_characters, request_integer
from models import Character

# Demander le nom du joueur
# Définir ask_name():
#   boucle 
#   demander le nom avec un input et enlever les espaces autour avec .strip()
#   si le nom n'est pas vite : on le retour
#   sinon on renvoie "le nom ne peux pas être vide"
def ask_name():
    while True:
        name = input("Quel est votre nom d'utilisateur ? ").strip()
        if name:
            return name
        else:
            print("Le nom ne peut pas être vide, veuillez saisir un nom d'utilisateur.")

# Composer une équipe de 3
# définir create_team():
#   available = get_characters()
#   team = [] (liste vide)
#   
#   tant que la taille de l'équipe est inférieur à 3:
#       afficher "équipe actuel :"
#       pour chaque perso dans l'équipe 
#           afficher character.name
#
#       afficher "Personnages disponible":
#           pour chaque doc
#               afficher numéro, name, atk, def, pv du doc
#
#       choice = request_integer entre 1 et len(available)
#       doc = available.pop(choice - 1)
#       character = personnage crée avec doc["name"], doc["atk"], doc["def"], doc["pv"]
#       ajouter le perso à team (append)
#
#   return team
def create_team():
    available = get_characters()
    team = []

    while len(team) < 3:
        print("\nEquipe actuel :")

        for character in team:
            print(character.name)

        print("\nPersonnages disponibles:")
        for i, doc in enumerate(available, start=1):
            print(
                f"{i}. {doc['name']} -"
                f"ATK: {doc['atk']} -"
                f"DEF: {doc['def']} -"
                f"PV: {doc['pv']}"
            )

        choice = request_integer("Choisissez un personnage: ", 1, len(available))

        doc = available.pop(choice - 1)

        character = Character(
            doc["name"],
            doc["atk"],
            doc["def"],
            doc["pv"]
        )
