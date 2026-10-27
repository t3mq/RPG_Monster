class Entite():
    # Attributs du personnage : nom, attaque, defense, pv
    def __init__(self, name, attack, defense, pv):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.pv = pv

    # Renvoie true si le personnage a encore de la vie
    def is_alive(self):
        return self.pv > 0

    # faire une attaque
    # définir to_attack(self, target) :
        # degats = attaque - defense
        # min 1 degats (sinon combat infinie)
        # on retire les degats à la cible
        # les pv ne descend pas en dessous de 0
        # on renvoie les dégats pour pouvoir les affichers
    def to_attack(self, target):
        damage = self.attack - target.defense
        damage = max(1, damage)
        target.pv = target.pv - damage
        target.pv = max(0, target.pv)
        return damage

class Character(Entite):
    pass

class Monster(Entite):
    pass
