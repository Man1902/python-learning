course = "Python Programming"
print(course)
print(f"Welcome to {course}")

# built in functions
print(course.upper())
print(course.lower())
print(course.split(" "))
print(course.strip())
print(course.index("n"))
print(course.find("Pro"))
print(course.replace("Python", "Go"))

# string slice
print(course[0:6])
print(course[:6])
print(course[7:])

print(len(course))

print("Pro" in course)
print("Go" not in course)
