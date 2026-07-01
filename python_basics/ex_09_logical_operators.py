# Logical operators : and or not
 
high_income = True
good_credit = True
student = False

if high_income and good_credit and not student:
    print("Eligible")
else:
    print("Not eligible")

day = "Sat"
if day == "Sat" or day == "Sun":
    print("Weekend")
else:
     print("Working Day")
    
age = 22
# if age >=18 and age < 65:   # OR
if 18 <= age < 65:            # Chaining comparision operators
    print("Eligible")
else:
    print("Not eligible")