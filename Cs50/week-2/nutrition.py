def main():
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 105,
        "cantaloupe": 50,
        "grapefruit": 52,
        "grapes": 62,
        "honeydew melon": 61,
        "kiwifruit": 90,
        "lemon": 17,
        "lime": 20,
        "nectarine": 63,
        "orange": 62,
        "peach": 59,
        "pear": 100,
        "pineapple": 50,
        "plums": 30,
        "strawberries": 4,
        "sweet cherries": 100,
        "tangerine": 47,
        "watermelon": 86
    }

    fruit = input("Fruit: ").strip().lower()

    if fruit in fruits:
        print(f"Calories: {fruits[fruit]}")

if __name__=="__main__":
    main()

