# print(str(70) + str(100))

""" Mathematical """
3 + 5
7 - 4
3 * 2
6 / 2
2**3  # raised to power. exponentiation^


# print(6 / 2)
# print(2 * 2)


"""PEMDAS  """
# Parentheses ()
# Exponents **
# Multiplication *
# Division /
# Additions +
# Subtractions -


# print(3 * 3 + 3 / 3 - 3)
# print(3 / 3 + 3 * 3 - 3)
# print(3 * (3 + 3) / 3 - 3)

""" height = 1.70
weight = 80

BMI = weight / (height * height)
print(f"you BMI is: {BMI}") """


""" height = 1.58
weight = 57

BMI = int(weight / (height * height))
print(f"you BMI is: {BMI}") """

""" height = 1.70
weight = 80

BMI = int(weight / (height * height))
print(f"you BMI is: {BMI}") """

""" height = 1.63
weight = 69

BMI = int(weight / (height * height))
print(f"you BMI is: {BMI}") """

# Teacher
height = input("Enter your height: ")
weight = input("Enter your weight: ")

weightInt = int(weight)
heightFloat = float(height)

bmi = weightInt / heightFloat ** 2
bmi = weightInt / (heightFloat * heightFloat)

bmi_int = int(bmi)
print(bmi_int)
