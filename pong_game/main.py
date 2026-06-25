from turtle import Screen, colormode
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

LEFT_POSITION = (-350,0)
RIGHT_POSITION = (350,0)

LEFT_PADDLE_COLOR= (255, 0, 191) # Hot Pink
RIGHT_PADDLE_COLOR= (0, 242, 255) # Electric Blue

WINING_SCORE = 5

colormode(255)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(RIGHT_PADDLE_COLOR,RIGHT_POSITION)
l_paddle = Paddle(LEFT_PADDLE_COLOR, LEFT_POSITION)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "Left")
screen.onkey(l_paddle.go_down, "Right")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle misses the ball
    if ball.xcor() > 380:
      ball.reset_position()
      scoreboard.l_pont()

    # Detect left paddle misses the ball
    if ball.xcor() < -380:
      ball.reset_position()
      scoreboard.r_pont()

    if scoreboard.l_score == WINING_SCORE or scoreboard.r_score == WINING_SCORE:
      is_game_on = False
      scoreboard.game_over()

    
screen.exitonclick()