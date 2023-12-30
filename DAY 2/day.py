print("> Welcome to the tip calculators")
bill = input("What was the total bill?: $")
porcent = input("Whats percentage tip would you like to give? 10, 12, or 15?")
person = input("How many people to split the bill?")

bill_add =  float(bill)
porcent =  bill_add / int(porcent)
person1= int(person) / bill
result = person1 + bill
print(f"Each person should pay: {result}")
