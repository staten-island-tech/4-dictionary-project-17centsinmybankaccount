thisdict = {
    "egg" : ["kidney,5000,rotting"],
    "potato" : ["potato,10,rotting"],
    "mouse" : ["mouse,1,possibly edible"] }
y = []
while True:
    action = input("What do you want to do")
    if action == "shop":
        x = input("We have egg, potato, and mouse")
        print(thisdict[x])
        y.append(x)
    if action == "see cart":
        print(y)
    if action == "end":
        print(y)
        break