##### Primitive data types #####
# string
name = "Alex"
print(f"Employee Name : {name}  # having type {type(name)}")
# Integer
id = 707
print(f"Employee Id : {id}  # having type {type(id)}")

# float
salary = 654321.50
print(f"Salary : {salary}   # having type {type(salary)}")

# bool
is_permanent_employee = True
print(f"Permanent Employee : {is_permanent_employee}    # of type {type(is_permanent_employee)}")

##### Sequence/collection data types #####
# list (mutable)
tech_stack = ["Python", "Java", "Go"]
tech_stack.append("NodeJs")
print(f"Tech stack : {tech_stack}  # having type {type(tech_stack)}")

# tuple (immutable)
tech_stack = ("Python", "Java", "Go")
print(f"Tech stack : {tech_stack}  # having type {type(tech_stack)}")
print(f"Is Python exist ? : {'Python' in tech_stack}")

# range (immutable)
nums = range(1,10)
print(f"Number range: {nums}  # having type {type(nums)}")

# set (mutable and unique)
tech_stack = {"Python", "Java", "Go"}
tech_stack.add("NodeJs")
print(f"Tech stack : {tech_stack}  # having type {type(tech_stack)}")

# frozenset (immutable and unique)
tech_stack = frozenset({"Python", "Java", "Go"})
print(f"Tech stack : {tech_stack}  # having type {type(tech_stack)}")

# map / dict (mutable and keys unique)
experience = {
    "Company1": 6, 
    "Company2": 2, 
    "Company3": 4
}
print(f" Experience : {experience}  # having type {type(experience)}")

##### Special data types #####
# NoneType
result = None
print(f" Result : {result}  # having type {type(result)}")