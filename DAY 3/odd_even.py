print("Do you want to know if your number is even or odd? 😋")

oddEven = int(input("Enter a number: "))
number = oddEven % 2

if number == 0:
    print("This is an even number. 👾👾")
else:
    print("This is an odd number.👾")
