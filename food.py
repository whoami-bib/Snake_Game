from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super(). __init__()
        self.shape("circle")
        self.penup()
        self.color("red")

        self.refresh()

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
