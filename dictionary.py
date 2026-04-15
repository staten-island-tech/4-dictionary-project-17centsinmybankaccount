    
egg = {
    "name" : "egg",
    "cost" : 5000,
    "quality" : "rotting"  
    } ,
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
random = [egg, potato, mouse]    
y = []
cost = 0
while True:
    action = input("What do you want to do: ")
    if action == "shop":
        x = input("We have egg, potato, and mouse: ")
        if x == "Egg":
            print(egg['name'])
            y.append(x)
        if x == "Potato":
            y.append(x)
        if x == "Mouse":
            y.append(x)
        else:
            print("This item is misspled or not in inventory.")
    if action == "see cart":
        print(y)
    if action == "end":
        print(y)
        
        break