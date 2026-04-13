egg = {
    "name" : "egg",
    "cost" : 5000,
    "quality" : "rotting"
}
potato = {
    "name" : "potato",
    "cost" : 10,
    "quality" : "rotting"
}
mouse = {
    "name" : "mouse",
    "cost": 1,
    "quality" : "possibly edible"
}
y = []
cost = 0
while True:
    action = input("What do you want to do")
    if action == "shop":
        x = input("We have egg, potato, and mouse")
        print(x)
        y.append(x)
    if action == "see cart":
        print(y)
    if action == "end":
        print(y)
        
        break