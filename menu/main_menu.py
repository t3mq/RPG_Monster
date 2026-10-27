from utils import request_integer, save_score
from menu.team_menu import ask_name, create_team
from menu.leaderboard_menu import show_leaderboard
from game import start_game

import sys

# afficher le menu de lancement
# définir main_menu():
#   afficher une ligne vide puis "Bienvenue dans RPG Monster"
#   afficher "1. Démarrer le jeu"
#   afficher "2. Afficher le classement"
#   affichier "3. Quitter"
#   renvoyer request_integer("Votre choix (1-3): ", 1, 3)
def main_menu():
    print("\n Bienvenue dans RPG Monster")
    print("1. Démarrer le jeu")
    print("2. Afficher le classement")
    print("3. Quitter")
    return request_integer("Votre choix (1-3): ", 1, 3)

# faire tourner le menu et lancer la bonne action
# definir start_menu():
#   boucle 
#       choice = main_menu()
#
#       si choix vaut 1 :
#           name = ask_name()
#           team = create_team()
#           waves = start_game(team)
#           save_score(name, waves)
#           afficher "Partie terminée, <name> : <waves> vagues survécues"
#
#       si choix vaut 2:
#           show_leaderboard()
#
#       si choix vaut 3:
#           affichier "au revoir"
#           sys.exit()
def start_menu():
    while True:
        choice = main_menu()

        if (choice == 1):
            name = ask_name()
            team = create_team()
            waves = start_game()
            save_score(name, waves)
            print(f"Parti terminée, {name} : {waves} vagues survécues")
        elif (choice == 2):
            show_leaderboard()
        elif (choice == 3):
            print("Au revoir")
            sys.exit()
