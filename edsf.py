egg = {
    "name": "egg",
    "cost": 5000,
    "quality": "rotting"
}

potato = {
    "name": "potato",
    "cost": 10,
    "quality": "rotting"
}

mouse = {
    "name": "mouse",
    "cost": 1,
    "quality": "possibly edible"
}

items = [egg, potato, mouse]

y = []

while True:
    action = input("What do you want to do: ")

    if action == "shop":
        x = input("We have egg, potato, and mouse: ")

        found = False
        for item in items:
            if item["name"] == x:
                y.append(item)
                print(x)
                found = True
                break

        if not found:
            print("This item is misspelled or not in inventory.")

    elif action == "see cart":
        print(y)

    elif action == "end":
        print(y)
        break