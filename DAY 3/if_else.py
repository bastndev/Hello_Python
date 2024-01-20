""" print("Welcome to the rollercoaster!")
height = float(input("Was is your height in cm? "))

if height >= 1.20:
    print("Please enter")
else:
    print("sorry you don't enters")
"""

print("Welcome to the rollercoaster!")
height = float(input("Was is your height in cm? "))

if height >= 1.20:
    print("Please enter")
    age = int(input("How old are you: "))
    if age < 12:
        print("please pay 5$")
    elif age <= 18:
        print("please pay 7$")
    else:
        print("please pay 12$")
else:
    print("sorry you don't enters")
