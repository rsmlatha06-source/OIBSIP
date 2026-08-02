# BMI Calculator Project
# BMI Calculator

try:
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))
    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be greater than 0.")
    else:
        bmi = weight / (height ** 2)
        print("Your BMI is:", round(bmi, 2))
        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")
except ValueError:
    print("Error: Please enter only numbers.")