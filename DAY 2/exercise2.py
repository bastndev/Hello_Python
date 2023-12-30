""" age_input = input("Enter your age: ")

# Check if the input is a numeric value
if age_input.isnumeric():
    age = int(age_input)
    life_data = 90
    days_in_year = 365

    # Calculate the remaining weeks
    weeks_left = (life_data - age) * days_in_year // 7

    print(f"You have {weeks_left} weeks left.")
else:
    print("Please enter a valid numeric age.") """

age = input("Enter your age: ")

years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")
