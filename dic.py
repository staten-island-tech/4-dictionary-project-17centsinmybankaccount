shop = {
    "covid" : "Dangerous, 2019, 7 million" ,
    "spanish flu" : "Dangerous, 1920, 50 million" ,
    "jerry virus" : "Deadly, 3000, 1"
}
cart = []
while True:
    action1 = input("What do you want to do?")
    if action1 == "shop":
        actionshop = input("What are you trying to buy")
        print(shop[actionshop])
        cart.append(actionshop)
    elif action1 == "see cart":
        print(cart)
    elif action1 == "checkout":
        print(f"You brought {cart}")
        break