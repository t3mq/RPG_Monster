from pymongo import *

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
