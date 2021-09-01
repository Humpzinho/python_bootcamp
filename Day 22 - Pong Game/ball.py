from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(135)
        self.goto(0, -180)
        self.game_over = False
        self.BALL_SPEED = 15

    def move(self):
        self.forward(self.BALL_SPEED)