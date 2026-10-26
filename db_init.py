from utils import get_db, client

db = get_db()

characters = db["characters"]
monsters = db["monsters"]

list_characters = [
    { "name": "Mage", "atk": 20, "def": 5, "pv": 80 },
    { "name": "Archer", "atk": 18, "def": 7, "pv": 90 },
    { "name": "Voleur", "atk": 22, "def": 8, "pv": 85 },
    { "name": "Paladin", "atk": 14, "def": 12, "pv": 110 },
    { "name": "Sorcier", "atk": 25, "def": 3, "pv": 75},
    { "name": "Chevalier", "atk": 17, "def": 15, "pv": 120 },
    { "name": "Moine", "atk": 19, "def": 9, "pv": 95 },
    { "name": "Berserker", "atk": 23, "def": 6, "pv": 105 },
    { "name": "Chasseur", "atk": 16, "def": 11, "pv": 100 },
]

list_monsters = [
    { "name": "Gobelin", "atk": 10, "def": 5, "pv": 50 },
    { "name": "Orc", "atk": 20, "def": 8, "pv": 120 },
    { "name": "Dragon", "atk": 35, "def": 20, "pv": 300 },
    { "name": "Zombie", "atk": 12, "def": 6, "pv": 70 },
    { "name": "Troll", "atk": 25, "def": 15, "pv": 200 },
    { "name": "Spectre", "atk": 18, "def": 10, "pv": 100 },
    { "name": "Golem", "atk": 30, "def": 25, "pv": 250 },
    { "name": "Vampire", "atk": 22, "def": 12, "pv": 150 },
    { "name": "Loup-Garou", "atk": 28, "def": 18, "pv": 180 },
    { "name": "Squelette", "atk": 15, "def": 7, "pv": 90 },
]

for character in list_characters:
    characters.replace_one(
        {"name": character["name"]},
        character,
        upsert=True
    )

for monster in list_monsters:
    monsters.replace_one(
        {"name": monster["name"]},
        monster,
        upsert=True
    )

print("Database initialized !")
print("Characters : ", characters.count_documents({}))
print("Monsters : ", monsters.count_documents({}))

client.close()
