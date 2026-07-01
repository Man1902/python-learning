
try:
    no1 = float(input("Enter No1: "))
    no2 = float(input("Enter No2: "))

    result = no1 / no2
    print(f"Result: {result}")

except Exception as e:
    print(f"Error occurred: : {e}")