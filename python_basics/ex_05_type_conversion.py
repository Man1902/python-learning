# int(x)
# float(x)
# bool(x)
# str(x)

x = input("x : ")
print(f"type of x is : {type(x)}")

y = int(x) + 1

print(y)

print(bool(""))
print(bool(0))
print(bool(None))

print(bool("Any value"))
print(bool(1))
print(bool(-1))
print(bool(5))
print(bool("0"))        # important : will return True
print(bool("False"))    # important : will return True