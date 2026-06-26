from turtle import Screen,Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
X_POSITION = 380
Y_POSITIONS = [-70, -40, -10, 20, 50, 80 ]

is_race_on = True

screen = Screen()
screen.setup(width=800, height=500)
screen.title("Turtle Race")
screen.tracer(0)
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color from {COLORS}: ")

all_turtles: list[Turtle] = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(COLORS[turtle_index])
    new_turtle.goto(x=-X_POSITION, y=Y_POSITIONS[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    time.sleep(0.1)
    screen.update()
    for turtle in all_turtles:
        if turtle.xcor() > 375:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

        



screen.exitonclick()