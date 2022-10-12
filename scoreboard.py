from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0, 260)
        self.updateScore()
        self.hideturtle()
    def updateScore(self):
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))
    def increaseScore(self):
        self.score += 1
        self.updateScore()

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))
