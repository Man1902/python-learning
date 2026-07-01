import random
from turtle import Turtle, Screen, colormode

tim = Turtle()

# Initialize the screen
screen = Screen()

# Set color mode to 255 to use RGB values in range 0-255
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# 1 Draw diffrent shapes
def draw_shape(no_of_sides):
    angle = 360/no_of_sides

    for i in range(no_of_sides):
        tim.forward(100)
        tim.right(angle)

def draw_diffrent_shapes():
    for no_of_sides in range(3, 11):
        tim.color(random_color())
        draw_shape(no_of_sides)

# 2 Random Walk
def random_walk():
    directions = [0, 90, 180, 270]
    tim.speed("fastest")
    tim.pensize(15)

    for _ in range(200):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(directions))

# 3 Draw Spirograph
def draw_spirograph(size_of_gap):
    tim.speed("fastest")
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

# user_input = int(input("Select any one option. 1: Draw diffrent shapes, 2: Random Walk, 3: Draw Spirograph"))
user_input = screen.textinput(title="Turtle GUI", prompt="Select any one option. 1: Draw diffrent shapes, 2: Random Walk, 3: Draw Spirograph")

if user_input == "1":
    draw_diffrent_shapes()
elif user_input == "2":
    random_walk()
else:
    draw_spirograph(5)

screen.exitonclick()
