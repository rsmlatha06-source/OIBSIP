# BMI Calculator Project
# BMI Calculator

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))