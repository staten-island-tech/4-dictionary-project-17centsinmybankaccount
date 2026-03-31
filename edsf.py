wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}
staff = []
x = input("Who are you trying to find?: ")
def directory(doctor):

    for x, y in wards.items():
        if doctor in y:
            print(x)
            staff.append(f"{doctor}, is in {x}")
        else:
            z = input("This person is not in the direcotry. Would you like to add him or her?")
            if z.upper == "YES":
                z2


    print(staff)
directory(x)
x = input("Who are you trying to find?: ")