from pymongo import *
import random

client = MongoClient("mongodb://localhost:27017/")

def get_db():
    return client["rpg_monster"]

def request_integer(message, min, max):
    # On boucle
    # afficher le message et récupérer la saisie
    # essayer de convertir en entier
        # si ça échoue (lettre, vide) : message d'erreur
    # si le nombre est entre min et max : on renvoie le nombre
    # sinon : message d'erreur, on recommence
    while True:
        entry = input(message)
        try:
            value = int(entry)
        except ValueError:
            print("Erreur : Veuillez entrer un entier valide")
            continue

        if (min <= value <= max):
            return value
        else:
            print(f"Erreur : Veuillez entrer un entier entre {min} et {max}.")

# lire les personnages
# définir get_characters():
#   renvoyer la liste les docs de la collection "characters" (list + find)
def get_characters():
    return list(get_db()["characters"].find())

# tirer un monstre au hasard
# get_random_monster():
#   récupérer tous les docs de la collection "monsters" dans une liste
#   renvoyer un élement
def get_random_monster():
    monsters = list(get_db()["monsters"].find())

    if not monsters:
        return None

    return random.choice(monsters)

# sauvegarder un score
# définir save_score(name, waves):
#   insérer dans la collection "scores" un doc { "player": name, "waves": waves } (insert_one)
def save_score(name, waves):
    get_db()["scores"].insert_one({
        "player": name,
        "waves": waves
    })

# Voir le top 3
# définir get_top_scores():
#   renvoyer la liste des scores triés par "vagues" décroissante, limités à 3
#   (find().sort("waves", -1).limit(3), dans un list())
def get_top_scores():
    return list(get_db["scores"].find().sort("waves", -1).limit(3))
