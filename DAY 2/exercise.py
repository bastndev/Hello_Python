# 21. [Interactive Coding Exercise] Data Types
""" number = input("Enter the number: ")
number1 = float(number[0])
number2 = float(number[1])

print(int(number1 + number2) ) """

""" try:
    number = input("Enter the number: ")
    number1 = float(number[0])
    number2 = float(number[1])

    result = int(number1 + number2)
    print(f"The result is: {result}")

except ValueError:
    print("Error: Please enter a valid number.")
except IndexError:
    print("Error: Please enter at least two digits.")
except Exception as e:
    print(f"An unexpected error occurred: {e}") """


""" number = input("Enter the number: ")
number1 = int(number[0])
number2 = int(number[1])

result = (number1 + number2)
print(f"The result is: {result}") """

# Teacher

twoNumbers = input("Enter Number pls: ")

firstNumber = int(twoNumbers[0])
secondNumber = int(twoNumbers[1])

result = firstNumber + secondNumber
print(f"The number result is: {result}")
