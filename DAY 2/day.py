""" print("> Welcome to the tip calculators")

bill = float(input("What was the total bill?: $"))
tip = int(input("Whats percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip =  tip / 100  * bill + bill / people
print(f"Each person should pay: {bill_with_tip:1f}")
"""

print("> Welcome to the tip calculators")

bill = float(input("What was the total bill?: $"))
tip = int(input("Whats percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + tip
bill_person =  total_bill / people
result = round(bill_person, 2)

print(f"Each person should pay: {result}")
