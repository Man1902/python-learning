# in meter
height = float(input("Enter height in meter : "))

# in kg
weight = 67.5
weight = float(input("Enter weight in kg : "))

bmi = weight / (height ** 2)

bmi = round(bmi,1)

print("Your BMI is : ", bmi)

if bmi < 18.5:
    print("You are Underweight!")
elif bmi >= 18.5 and bmi < 24.9:
    print("You are Healthy!")
elif bmi >= 24.9 and bmi < 29.9:
    print("You are Overweight!")
else:
    print("You are Obese!")
