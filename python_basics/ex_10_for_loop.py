
print(type(range(3)))

# Iterable range
for number in range(3):
    print(f"Attempt {number + 1}")

for number in range(1,4):
    print(f"Attempt {number}")

for number in range(1,10,2):
    print((number) * "* ")

for number in range(5):
    print((number) * "* ")

# for else example
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# Nested loop
for x in range(3):
    for y in range(3):
        print(f"({x}, {y})")

# Iterable string
for ch in "Python":
    print(ch)

# Iterable list
for mark in [98, 94, 90, 80, 91]:
    print(mark)