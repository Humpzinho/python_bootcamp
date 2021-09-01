from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(self.color_car())
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.penup()
        self.setheading(180)
        self.random_pos()
        self.speed_car = 5

    def color_car(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        return (r, g, b)

    def random_pos(self):
        self.goto(230, random.randrange(-200, 200, 20))

    def move(self):
        self.forward(self.speed_car)