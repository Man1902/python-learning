# Ex1 : Perform a Task
def greet(name):
    print(f"Welcome {name} to Python Learning")
greet("Alex")

#Ex2 : Return a value
def get_greeting(name):
    return f"Hello {name}"
message = get_greeting("Alex")
print(message)

def increment(number, by=2):  # 2nd arg with default value
    return number + by
#result = increment(2, 1) # or
#result = increment(2, by=1) # or
result = increment(2)
print(result)

def multiply(*numbers):  # variable number of args (tuples)
    result = 1
    for number in numbers:
        result *= number
    return result
print(multiply(2, 3, 4, 5))



