from turtle import Turtle

class Scoreboard(Turtle):

    def  __init__(self) -> None:
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 240)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def l_pont(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_pont(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 50, "normal"))

