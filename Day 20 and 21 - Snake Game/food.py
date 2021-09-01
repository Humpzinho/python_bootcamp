from turtle import Turtle
from snake import Snake
import random

class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.speed("fastest")
        self.refresh_c()
        self.color((255, 99, 71))

    def refresh_c(self):
        random_x = random.randrange(-260, 260, 20)
        random_y = random.randrange(-260, 260, 20)
        self.setheading(random.randrange(0, 360))
        self.goto(x=random_x, y=random_y)
    