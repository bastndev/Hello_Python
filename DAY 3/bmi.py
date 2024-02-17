height = float(input("Enter your height: "))
weight = int(input("Enter your weight: "))

bmi = weight / (height ** 2)

if bmi < 18:
  print(f"Your BMI is: {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is: {bmi}, you have a normal")
elif bmi > 32:
  print(f"Your BMI is: {bmi}, you are Obese.")
else:
  print(f"Your BMI is: {bmi}")

  
