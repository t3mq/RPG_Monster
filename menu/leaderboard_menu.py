from utils import get_top_scores

# afficher le top 3
# définir show_leaderboard():
#   scores = get_top_scores()
#   afficher "Classement :"
#   si scores est vides
#       afficher "aucun scores pour le moment"
#       sortir de la fonction (return)
#   pour chaque position, score dans enumerate(scores, 1)
#       afficher position, score["player"], score["waves"] vagues, 
def show_leaderboard():
    scores = get_top_scores()

    print("Classement :")
    if not scores:
        print("Aucun scores pour le moment")
        return
    for position, score in enumerate(scores, 1):
        print(f"{position}. {score['player']} - {score['waves']} vagues")
    print("-" * 18)
