from turtle import Turtle


class Turtle_Cross(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -230)
        
    def move(self):
        self.forward(10)
        
    def move_back(self):
        self.backward(10)