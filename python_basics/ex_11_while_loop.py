number = 100

while number > 0:
    print(number)
    number //= 2
    
# infinite loop
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

count = 0
for number in range(1,10):
    if number % 2 == 0:
        print(number)
        count += 1
print(f"We have {count} even numbers")
