from pymongo.errors import PyMongoError

from database import create_client, database_name


def seed_database(db):
    characters = [
        {"name": "Guerrier",  "atk": 15, "def": 10, "hp": 100},
        {"name": "Mage",      "atk": 20, "def": 5,  "hp": 80},
        {"name": "Archer",    "atk": 18, "def": 7,  "hp": 90},
        {"name": "Voleur",    "atk": 12, "def": 12, "hp": 85},
        {"name": "Paladin",   "atk": 17, "def": 8,  "hp": 110},
        {"name": "Sorcier",   "atk": 22, "def": 4,  "hp": 70},
        {"name": "Chevalier", "atk": 19, "def": 6,  "hp": 120},
        {"name": "Moine",     "atk": 14, "def": 9,  "hp": 95},
        {"name": "Berserker", "atk": 25, "def": 3,  "hp": 80},
        {"name": "Chasseur",  "atk": 16, "def": 11, "hp": 90},
    ]

    monsters = [
        {"name": "Gobelin",    "atk": 10, "def": 3,  "hp": 50},
        {"name": "Zombie",     "atk": 12, "def": 4,  "hp": 70},
        {"name": "Squelette",  "atk": 14, "def": 5,  "hp": 90},
        {"name": "Spectre",    "atk": 16, "def": 5,  "hp": 100},
        {"name": "Orc",        "atk": 18, "def": 6,  "hp": 120},
        {"name": "Vampire",    "atk": 20, "def": 6,  "hp": 150},
        {"name": "Loup-garou", "atk": 22, "def": 7,  "hp": 180},
        {"name": "Troll",      "atk": 24, "def": 8,  "hp": 200},
        {"name": "Golem",      "atk": 26, "def": 9,  "hp": 250},
        {"name": "Dragon",     "atk": 30, "def": 10, "hp": 260},
    ]

    for collection, documents in (("characters", characters), ("monsters", monsters)):
        for document in documents:
            db[collection].update_one(
                {"name": document["name"]}, {"$setOnInsert": document}, upsert=True
            )


def main():
    client = create_client()
    try:
        seed_database(client[database_name()])
        print("Personnages et monstres initialises. Les scores existants sont conserves.")
    except PyMongoError:
        raise SystemExit("Initialisation impossible. Verifiez le service MongoDB.") from None
    finally:
        client.close()


if __name__ == "__main__":
    main()